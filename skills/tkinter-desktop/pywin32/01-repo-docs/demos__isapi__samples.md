# 官方示例源码 · isapi/samples

> 来源 https://github.com/mhammond/pywin32/tree/main/isapi/samples （共 5 个 .py，全文内联）


---

## isapi/samples/advanced.py

```python
# This extension demonstrates some advanced features of the Python ISAPI
# framework.
# We demonstrate:
# * Reloading your Python module without shutting down IIS (eg, when your
#   .py implementation file changes.)
# * Custom command-line handling - both additional options and commands.
# * Using a query string - any part of the URL after a '?' is assumed to
#   be "variable names" separated by '&' - we will print the values of
#   these server variables.
# * If the tail portion of the URL is "ReportUnhealthy", IIS will be
#   notified we are unhealthy via a HSE_REQ_REPORT_UNHEALTHY request.
#   Whether this is acted upon depends on if the IIS health-checking
#   tools are installed, but you should always see the reason written
#   to the Windows event log - see the IIS documentation for more.

import os
import stat
import sys

from isapi import isapicon
from isapi.simple import SimpleExtension

if hasattr(sys, "isapidllhandle"):
    import win32traceutil

# Notes on reloading
# If your HttpFilterProc or HttpExtensionProc functions raises
# 'isapi.InternalReloadException', the framework will not treat it
# as an error but instead will terminate your extension, reload your
# extension module, re-initialize the instance, and re-issue the request.
# The Initialize functions are called with None as their param.  The
# return code from the terminate function is ignored.
#
# This is all the framework does to help you.  It is up to your code
# when you raise this exception.  This sample uses a Win32 "find
# notification".  Whenever windows tells us one of the files in the
# directory has changed, we check if the time of our source-file has
# changed, and set a flag.  Next imcoming request, we check the flag and
# raise the special exception if set.
#
# The end result is that the module is automatically reloaded whenever
# the source-file changes - you need take no further action to see your
# changes reflected in the running server.

# The framework only reloads your module - if you have libraries you
# depend on and also want reloaded, you must arrange for this yourself.
# One way of doing this would be to special case the import of these
# modules.  Eg:
# --
# try:
#    my_module = reload(my_module) # module already imported - reload it
# except NameError:
#    import my_module # first time around - import it.
# --
# When your module is imported for the first time, the NameError will
# be raised, and the module imported.  When the ISAPI framework reloads
# your module, the existing module will avoid the NameError, and allow
# you to reload that module.

import threading

import win32con
import win32event
import win32file
import winerror

from isapi import InternalReloadException

try:
    reload_counter += 1  # type: ignore[used-before-def]
except NameError:
    reload_counter = 0


# A watcher thread that checks for __file__ changing.
# When it detects it, it simply sets "change_detected" to true.
class ReloadWatcherThread(threading.Thread):
    def __init__(self):
        self.change_detected = False
        self.filename = __file__
        if self.filename.endswith("c") or self.filename.endswith("o"):
            self.filename = self.filename[:-1]
        self.handle = win32file.FindFirstChangeNotification(
            os.path.dirname(self.filename),
            False,  # watch tree?
            win32con.FILE_NOTIFY_CHANGE_LAST_WRITE,
        )
        threading.Thread.__init__(self)

    def run(self):
        last_time = os.stat(self.filename)[stat.ST_MTIME]
        while 1:
            try:
                rc = win32event.WaitForSingleObject(self.handle, win32event.INFINITE)
                win32file.FindNextChangeNotification(self.handle)
            except win32event.error as details:
                # handle closed - thread should terminate.
                if details.winerror != winerror.ERROR_INVALID_HANDLE:
                    raise
                break
            this_time = os.stat(self.filename)[stat.ST_MTIME]
            if this_time != last_time:
                print("Detected file change - flagging for reload.")
                self.change_detected = True
                last_time = this_time

    def stop(self):
        win32file.FindCloseChangeNotification(self.handle)


# The ISAPI extension - handles requests in our virtual dir, and sends the
# response to the client.
class Extension(SimpleExtension):
    "Python advanced sample Extension"

    def __init__(self):
        self.reload_watcher = ReloadWatcherThread()
        self.reload_watcher.start()

    def HttpExtensionProc(self, ecb):
        # NOTE: If you use a ThreadPoolExtension, you must still perform
        # this check in HttpExtensionProc - raising the exception from
        # The "Dispatch" method will just cause the exception to be
        # rendered to the browser.
        if self.reload_watcher.change_detected:
            print("Doing reload")
            raise InternalReloadException

        url = ecb.GetServerVariable("UNICODE_URL")
        if url.endswith("ReportUnhealthy"):
            ecb.ReportUnhealthy("I'm a little sick")

        ecb.SendResponseHeaders("200 OK", "Content-Type: text/html\r\n\r\n", 0)
        print("<HTML><BODY>", file=ecb)

        qs = ecb.GetServerVariable("QUERY_STRING")
        if qs:
            queries = qs.split("&")
            print("<PRE>", file=ecb)
            for q in queries:
                val = ecb.GetServerVariable(q, "&lt;no such variable&gt;")
                print(f"{q}={val!r}", file=ecb)
            print("</PRE><P/>", file=ecb)

        print("This module has been imported", file=ecb)
        print("%d times" % (reload_counter,), file=ecb)
        print("</BODY></HTML>", file=ecb)
        ecb.close()
        return isapicon.HSE_STATUS_SUCCESS

    def TerminateExtension(self, status):
        self.reload_watcher.stop()


# The entry points for the ISAPI extension.
def __ExtensionFactory__():
    return Extension()


# Our special command line customization.
# Pre-install hook for our virtual directory.
def PreInstallDirectory(params, options):
    # If the user used our special '--description' option,
    # then we override our default.
    if options.description:
        params.Description = options.description


# Post install hook for our entire script
def PostInstall(params, options):
    print()
    print("The sample has been installed.")
    print("Point your browser to /AdvancedPythonSample")
    print("If you modify the source file and reload the page,")
    print("you should see the reload counter increment")


# Handler for our custom 'status' argument.
def status_handler(options, log, arg):
    "Query the status of something"
    print("Everything seems to be fine!")


custom_arg_handlers = {"status": status_handler}

if __name__ == "__main__":
    # If run from the command-line, install ourselves.
    from isapi.install import *

    params = ISAPIParameters(PostInstall=PostInstall)
    # Setup the virtual directories - this is a list of directories our
    # extension uses - in this case only 1.
    # Each extension has a "script map" - this is the mapping of ISAPI
    # extensions.
    sm = [ScriptMapParams(Extension="*", Flags=0)]
    vd = VirtualDirParameters(
        Name="AdvancedPythonSample",
        Description=Extension.__doc__,
        ScriptMaps=sm,
        ScriptMapUpdate="replace",
        # specify the pre-install hook.
        PreInstall=PreInstallDirectory,
    )
    params.VirtualDirs = [vd]
    # Setup our custom option parser.
    from optparse import OptionParser

    parser = OptionParser("")  # blank usage, so isapi sets it.
    parser.add_option(
        "",
        "--description",
        action="store",
        help="custom description to use for the virtual directory",
    )

    HandleCommandLine(
        params, opt_parser=parser, custom_arg_handlers=custom_arg_handlers
    )

```


---

## isapi/samples/redirector.py

```python
# This is a sample ISAPI extension written in Python.
#
# Please see README.txt in this directory, and specifically the
# information about the "loader" DLL - installing this sample will create
# "_redirector.dll" in the current directory.  The readme explains this.

# Executing this script (or any server config script) will install the extension
# into your web server. As the server executes, the PyISAPI framework will load
# this module and create your Extension and Filter objects.

# This is the simplest possible redirector (or proxy) we can write.  The
# extension installs with a mask of '*' in the root of the site.
# As an added bonus though, we optionally show how, on IIS6 and later, we
# can use HSE_ERQ_EXEC_URL to ignore certain requests - in IIS5 and earlier
# we can only do this with an ISAPI filter - see redirector_with_filter for
# an example.  If this sample is run on IIS5 or earlier it simply ignores
# any excludes.

import sys
from urllib.request import urlopen

import win32api

from isapi import isapicon, threaded_extension

# sys.isapidllhandle will exist when we are loaded by the IIS framework.
# In this case we redirect our output to the win32traceutil collector.
if hasattr(sys, "isapidllhandle"):
    import win32traceutil

# The site we are proxying.
proxy = "https://www.python.org"

# Urls we exclude (ie, allow IIS to handle itself) - all are lowered,
# and these entries exist by default on Vista...
excludes = ["/iisstart.htm", "/welcome.png"]


# An "io completion" function, called when ecb.ExecURL completes...
def io_callback(ecb, url, cbIO, errcode):
    # Get the status of our ExecURL
    httpstatus, substatus, win32 = ecb.GetExecURLStatus()
    print(
        "ExecURL of %r finished with http status %d.%d, win32 status %d (%s)"
        % (url, httpstatus, substatus, win32, win32api.FormatMessage(win32).strip())
    )
    # nothing more to do!
    ecb.DoneWithSession()


# The ISAPI extension - handles all requests in the site.
class Extension(threaded_extension.ThreadPoolExtension):
    "Python sample Extension"

    def Dispatch(self, ecb):
        # Note that our ThreadPoolExtension base class will catch exceptions
        # in our Dispatch method, and write the traceback to the client.
        # That is perfect for this sample, so we don't catch our own.
        # print(f'IIS dispatching "{ecb.GetServerVariable("URL")}"')
        url = ecb.GetServerVariable("URL").decode("ascii")
        for exclude in excludes:
            if url.lower().startswith(exclude):
                print("excluding %s" % url)
                if ecb.Version < 0x60000:
                    print("(but this is IIS5 or earlier - can't do 'excludes')")
                else:
                    ecb.IOCompletion(io_callback, url)
                    ecb.ExecURL(
                        None,
                        None,
                        None,
                        None,
                        None,
                        isapicon.HSE_EXEC_URL_IGNORE_CURRENT_INTERCEPTOR,
                    )
                    return isapicon.HSE_STATUS_PENDING

        new_url = proxy + url
        print("Opening %s" % new_url)
        fp = urlopen(new_url)
        headers = fp.info()
        # subtle breakage: str(headers) normalizes \r\n
        # back to \n and also sticks an extra \n term.
        # take *all* trailing \n off, replace remaining with
        # \r\n, then add the 2 trailing \r\n.
        header_text = str(headers).rstrip("\n").replace("\n", "\r\n") + "\r\n\r\n"
        ecb.SendResponseHeaders("200 OK", header_text, False)
        ecb.WriteClient(fp.read())
        ecb.DoneWithSession()
        print(f"Returned data from '{new_url}'")
        return isapicon.HSE_STATUS_SUCCESS


# The entry points for the ISAPI extension.
def __ExtensionFactory__():
    return Extension()


if __name__ == "__main__":
    # If run from the command-line, install ourselves.
    from isapi.install import *

    params = ISAPIParameters()
    # Setup the virtual directories - this is a list of directories our
    # extension uses - in this case only 1.
    # Each extension has a "script map" - this is the mapping of ISAPI
    # extensions.
    sm = [ScriptMapParams(Extension="*", Flags=0)]
    vd = VirtualDirParameters(
        Name="/",
        Description=Extension.__doc__,
        ScriptMaps=sm,
        ScriptMapUpdate="replace",
    )
    params.VirtualDirs = [vd]
    HandleCommandLine(params)

```


---

## isapi/samples/redirector_asynch.py

```python
# This is a sample ISAPI extension written in Python.

# This is like the other 'redirector' samples, but uses asnch IO when writing
# back to the client (it does *not* use asynch io talking to the remote
# server!)

import sys
import urllib.error
import urllib.parse
import urllib.request

from isapi import isapicon, threaded_extension

# sys.isapidllhandle will exist when we are loaded by the IIS framework.
# In this case we redirect our output to the win32traceutil collector.
if hasattr(sys, "isapidllhandle"):
    import win32traceutil

# The site we are proxying.
proxy = "https://www.python.org"

# We synchronously read chunks of this size then asynchronously write them.
CHUNK_SIZE = 8192


# The callback made when IIS completes the asynch write.
def io_callback(ecb, fp, cbIO, errcode):
    print("IO callback", ecb, fp, cbIO, errcode)
    chunk = fp.read(CHUNK_SIZE)
    if chunk:
        ecb.WriteClient(chunk, isapicon.HSE_IO_ASYNC)
        # and wait for the next callback to say this chunk is done.
    else:
        # eof - say we are complete.
        fp.close()
        ecb.DoneWithSession()


# The ISAPI extension - handles all requests in the site.
class Extension(threaded_extension.ThreadPoolExtension):
    "Python sample proxy server - asynch version."

    def Dispatch(self, ecb):
        print('IIS dispatching "{}"'.format(ecb.GetServerVariable("URL")))
        url = ecb.GetServerVariable("URL")

        new_url = proxy + url
        print("Opening %s" % new_url)
        fp = urllib.request.urlopen(new_url)
        headers = fp.info()
        ecb.SendResponseHeaders("200 OK", str(headers) + "\r\n", False)
        # now send the first chunk asynchronously
        ecb.ReqIOCompletion(io_callback, fp)
        chunk = fp.read(CHUNK_SIZE)
        if chunk:
            ecb.WriteClient(chunk, isapicon.HSE_IO_ASYNC)
            return isapicon.HSE_STATUS_PENDING
        # no data - just close things now.
        ecb.DoneWithSession()
        return isapicon.HSE_STATUS_SUCCESS


# The entry points for the ISAPI extension.
def __ExtensionFactory__():
    return Extension()


if __name__ == "__main__":
    # If run from the command-line, install ourselves.
    from isapi.install import *

    params = ISAPIParameters()
    # Setup the virtual directories - this is a list of directories our
    # extension uses - in this case only 1.
    # Each extension has a "script map" - this is the mapping of ISAPI
    # extensions.
    sm = [ScriptMapParams(Extension="*", Flags=0)]
    vd = VirtualDirParameters(
        Name="/",
        Description=Extension.__doc__,
        ScriptMaps=sm,
        ScriptMapUpdate="replace",
    )
    params.VirtualDirs = [vd]
    HandleCommandLine(params)

```


---

## isapi/samples/redirector_with_filter.py

```python
# This is a sample configuration file for an ISAPI filter and extension
# written in Python.
#
# Please see README.txt in this directory, and specifically the
# information about the "loader" DLL - installing this sample will create
# "_redirector_with_filter.dll" in the current directory.  The readme explains
# this.

# Executing this script (or any server config script) will install the extension
# into your web server. As the server executes, the PyISAPI framework will load
# this module and create your Extension and Filter objects.

# This sample provides sample redirector:
# It is implemented by a filter and an extension, so that some requests can
# be ignored.  Compare with 'redirector_simple' which avoids the filter, but
# is unable to selectively ignore certain requests.
# The process is sample uses is:
# * The filter is installed globally, as all filters are.
# * A Virtual Directory named "python" is setup.  This dir has our ISAPI
#   extension as the only application, mapped to file-extension '*'.  Thus, our
#   extension handles *all* requests in this directory.
# The basic process is that the filter does URL rewriting, redirecting every
# URL to our Virtual Directory.  Our extension then handles this request,
# forwarding the data from the proxied site.
# For example:
# * URL of "index.html" comes in.
# * Filter rewrites this to "/python/index.html"
# * Our extension sees the full "/python/index.html", removes the leading
#   portion, and opens and forwards the remote URL.


# This sample is very small - it avoid most error handling, etc.  It is for
# demonstration purposes only.

import sys
import urllib.error
import urllib.parse
import urllib.request

from isapi import isapicon, threaded_extension
from isapi.simple import SimpleFilter

# sys.isapidllhandle will exist when we are loaded by the IIS framework.
# In this case we redirect our output to the win32traceutil collector.
if hasattr(sys, "isapidllhandle"):
    import win32traceutil

# The site we are proxying.
proxy = "https://www.python.org"
# The name of the virtual directory we install in, and redirect from.
virtualdir = "/python"

# The key feature of this redirector over the simple redirector is that it
# can choose to ignore certain responses by having the filter not rewrite them
# to our virtual dir. For this sample, we just exclude the IIS help directory.


# The ISAPI extension - handles requests in our virtual dir, and sends the
# response to the client.
class Extension(threaded_extension.ThreadPoolExtension):
    "Python sample Extension"

    def Dispatch(self, ecb):
        # Note that our ThreadPoolExtension base class will catch exceptions
        # in our Dispatch method, and write the traceback to the client.
        # That is perfect for this sample, so we don't catch our own.
        # print(f'IIS dispatching "{ecb.GetServerVariable("URL")}"')
        url = ecb.GetServerVariable("URL")
        if url.startswith(virtualdir):
            new_url = proxy + url[len(virtualdir) :]
            print("Opening", new_url)
            fp = urllib.request.urlopen(new_url)
            headers = fp.info()
            ecb.SendResponseHeaders("200 OK", str(headers) + "\r\n", False)
            ecb.WriteClient(fp.read())
            ecb.DoneWithSession()
            print(f"Returned data from '{new_url}'!")
        else:
            # this should never happen - we should only see requests that
            # start with our virtual directory name.
            print(f"Not proxying '{url}'")


# The ISAPI filter.
class Filter(SimpleFilter):
    "Sample Python Redirector"

    filter_flags = isapicon.SF_NOTIFY_PREPROC_HEADERS | isapicon.SF_NOTIFY_ORDER_DEFAULT

    def HttpFilterProc(self, fc):
        # print("Filter Dispatch")
        nt = fc.NotificationType
        if nt != isapicon.SF_NOTIFY_PREPROC_HEADERS:
            return isapicon.SF_STATUS_REQ_NEXT_NOTIFICATION

        pp = fc.GetData()
        url = pp.GetHeader("url")
        # print(f"URL is '{url}'")
        prefix = virtualdir
        if not url.startswith(prefix):
            new_url = prefix + url
            print(f"New proxied URL is '{new_url}'")
            pp.SetHeader("url", new_url)
            # For the sake of demonstration, show how the FilterContext
            # attribute is used.  It always starts out life as None, and
            # any assignments made are automatically decref'd by the
            # framework during a SF_NOTIFY_END_OF_NET_SESSION notification.
            if fc.FilterContext is None:
                fc.FilterContext = 0
            fc.FilterContext += 1
            print("This is request number %d on this connection" % fc.FilterContext)
            return isapicon.SF_STATUS_REQ_HANDLED_NOTIFICATION
        else:
            print(f"Filter ignoring URL '{url}'")

            # Some older code that handled SF_NOTIFY_URL_MAP.
            # print("Have URL_MAP notify")
            # urlmap = fc.GetData()
            # print("URI is", urlmap.URL)
            # print("Path is", urlmap.PhysicalPath)
            # if urlmap.URL.startswith("/UC/"):
            # # Find the /UC/ in the physical path, and nuke it (except
            # # as the path is physical, it is \)
            # p = urlmap.PhysicalPath
            # pos = p.index("\\UC\\")
            # p = p[:pos] + p[pos+3:]
            # p = r"E:\src\pyisapi\webroot\PyTest\formTest.htm"
            # print("New path is", p)
            # urlmap.PhysicalPath = p


# The entry points for the ISAPI extension.
def __FilterFactory__():
    return Filter()


def __ExtensionFactory__():
    return Extension()


if __name__ == "__main__":
    # If run from the command-line, install ourselves.
    from isapi.install import *

    params = ISAPIParameters()
    # Setup all filters - these are global to the site.
    params.Filters = [
        FilterParameters(Name="PythonRedirector", Description=Filter.__doc__),
    ]
    # Setup the virtual directories - this is a list of directories our
    # extension uses - in this case only 1.
    # Each extension has a "script map" - this is the mapping of ISAPI
    # extensions.
    sm = [ScriptMapParams(Extension="*", Flags=0)]
    vd = VirtualDirParameters(
        Name=virtualdir[1:],
        Description=Extension.__doc__,
        ScriptMaps=sm,
        ScriptMapUpdate="replace",
    )
    params.VirtualDirs = [vd]
    HandleCommandLine(params)

```


---

## isapi/samples/test.py

```python
# This extension is used mainly for testing purposes - it is not
# designed to be a simple sample, but instead is a hotch-potch of things
# that attempts to exercise the framework.

import os
import stat
import sys

from isapi import isapicon
from isapi.simple import SimpleExtension

if hasattr(sys, "isapidllhandle"):
    import win32traceutil

# We use the same reload support as 'advanced.py' demonstrates.
import threading

import win32con
import win32event
import win32file
import winerror

from isapi import InternalReloadException


# A watcher thread that checks for __file__ changing.
# When it detects it, it simply sets "change_detected" to true.
class ReloadWatcherThread(threading.Thread):
    def __init__(self):
        self.change_detected = False
        self.filename = __file__
        if self.filename.endswith("c") or self.filename.endswith("o"):
            self.filename = self.filename[:-1]
        self.handle = win32file.FindFirstChangeNotification(
            os.path.dirname(self.filename),
            False,  # watch tree?
            win32con.FILE_NOTIFY_CHANGE_LAST_WRITE,
        )
        threading.Thread.__init__(self)

    def run(self):
        last_time = os.stat(self.filename)[stat.ST_MTIME]
        while 1:
            try:
                rc = win32event.WaitForSingleObject(self.handle, win32event.INFINITE)
                win32file.FindNextChangeNotification(self.handle)
            except win32event.error as details:
                # handle closed - thread should terminate.
                if details.winerror != winerror.ERROR_INVALID_HANDLE:
                    raise
                break
            this_time = os.stat(self.filename)[stat.ST_MTIME]
            if this_time != last_time:
                print("Detected file change - flagging for reload.")
                self.change_detected = True
                last_time = this_time

    def stop(self):
        win32file.FindCloseChangeNotification(self.handle)


def TransmitFileCallback(ecb, hFile, cbIO, errCode):
    print("Transmit complete!")
    ecb.close()


# The ISAPI extension - handles requests in our virtual dir, and sends the
# response to the client.
class Extension(SimpleExtension):
    "Python test Extension"

    def __init__(self):
        self.reload_watcher = ReloadWatcherThread()
        self.reload_watcher.start()

    def HttpExtensionProc(self, ecb):
        # NOTE: If you use a ThreadPoolExtension, you must still perform
        # this check in HttpExtensionProc - raising the exception from
        # The "Dispatch" method will just cause the exception to be
        # rendered to the browser.
        if self.reload_watcher.change_detected:
            print("Doing reload")
            raise InternalReloadException

        if ecb.GetServerVariable("UNICODE_URL").endswith("test.py"):
            file_flags = (
                win32con.FILE_FLAG_SEQUENTIAL_SCAN | win32con.FILE_FLAG_OVERLAPPED
            )
            hfile = win32file.CreateFile(
                __file__,
                win32con.GENERIC_READ,
                0,
                None,
                win32con.OPEN_EXISTING,
                file_flags,
                None,
            )
            flags = (
                isapicon.HSE_IO_ASYNC
                | isapicon.HSE_IO_DISCONNECT_AFTER_SEND
                | isapicon.HSE_IO_SEND_HEADERS
            )
            # We pass hFile to the callback simply as a way of keeping it alive
            # for the duration of the transmission
            try:
                ecb.TransmitFile(
                    TransmitFileCallback,
                    hfile,
                    int(hfile),
                    "200 OK",
                    0,
                    0,
                    None,
                    None,
                    flags,
                )
            except:
                # Errors keep this source file open!
                hfile.Close()
                raise
        else:
            # default response
            ecb.SendResponseHeaders("200 OK", "Content-Type: text/html\r\n\r\n", 0)
            print("<HTML><BODY>", file=ecb)
            print("The root of this site is at", ecb.MapURLToPath("/"), file=ecb)
            print("</BODY></HTML>", file=ecb)
            ecb.close()
        return isapicon.HSE_STATUS_SUCCESS

    def TerminateExtension(self, status):
        self.reload_watcher.stop()


# The entry points for the ISAPI extension.
def __ExtensionFactory__():
    return Extension()


# Our special command line customization.
# Pre-install hook for our virtual directory.
def PreInstallDirectory(params, options):
    # If the user used our special '--description' option,
    # then we override our default.
    if options.description:
        params.Description = options.description


# Post install hook for our entire script
def PostInstall(params, options):
    print()
    print("The sample has been installed.")
    print("Point your browser to /PyISAPITest")


# Handler for our custom 'status' argument.
def status_handler(options, log, arg):
    "Query the status of something"
    print("Everything seems to be fine!")


custom_arg_handlers = {"status": status_handler}

if __name__ == "__main__":
    # If run from the command-line, install ourselves.
    from isapi.install import *

    params = ISAPIParameters(PostInstall=PostInstall)
    # Setup the virtual directories - this is a list of directories our
    # extension uses - in this case only 1.
    # Each extension has a "script map" - this is the mapping of ISAPI
    # extensions.
    sm = [ScriptMapParams(Extension="*", Flags=0)]
    vd = VirtualDirParameters(
        Name="PyISAPITest",
        Description=Extension.__doc__,
        ScriptMaps=sm,
        ScriptMapUpdate="replace",
        # specify the pre-install hook.
        PreInstall=PreInstallDirectory,
    )
    params.VirtualDirs = [vd]
    # Setup our custom option parser.
    from optparse import OptionParser

    parser = OptionParser("")  # blank usage, so isapi sets it.
    parser.add_option(
        "",
        "--description",
        action="store",
        help="custom description to use for the virtual directory",
    )

    HandleCommandLine(
        params, opt_parser=parser, custom_arg_handlers=custom_arg_handlers
    )

```
