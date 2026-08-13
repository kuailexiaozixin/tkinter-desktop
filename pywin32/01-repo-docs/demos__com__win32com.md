# 官方示例源码 · com/win32com

> 来源 https://github.com/mhammond/pywin32/tree/main/com/win32com （共 11 个 .py，全文内联）


---

## com/win32com/demos/__init__.py

```python

```


---

## com/win32com/demos/connect.py

```python
# Implements _both_ a connectable client, and a connectable server.
#
# Note that we cheat just a little - the Server in this demo is not created
# via Normal COM - this means we can avoid registering the server.
# However, the server _is_ accessed as a COM object - just the creation
# is cheated on - so this is still working as a fully-fledged server.

import pythoncom
import pywintypes
import win32com.server.connect
import win32com.server.util

# This is the IID of the Events interface both Client and Server support.
IID_IConnectDemoEvents = pywintypes.IID("{A4988850-49C3-11d0-AE5D-52342E000000}")

# The server which implements
# Create a connectable class, that has a single public method
# 'DoIt', which echos to a single sink 'DoneIt'


class ConnectableServer(win32com.server.connect.ConnectableServer):
    _public_methods_ = [
        "DoIt"
    ] + win32com.server.connect.ConnectableServer._public_methods_
    _connect_interfaces_ = [IID_IConnectDemoEvents]

    # The single public method that the client can call on us
    # (ie, as a normal COM server, this exposes just this single method.
    def DoIt(self, arg):
        # Simply broadcast a notification.
        self._BroadcastNotify(self.NotifyDoneIt, (arg,))

    def NotifyDoneIt(self, interface, arg):
        interface.Invoke(1000, 0, pythoncom.DISPATCH_METHOD, 1, arg)


# Here is the client side of the connection world.
# Define a COM object which implements the methods defined by the
# IConnectDemoEvents interface.
class ConnectableClient:
    # This is another cheat - I _know_ the server defines the "DoneIt" event
    # as DISPID==1000 - I also know from the implementation details of COM
    # that the first method in _public_methods_ gets 1000.
    # Normally some explicit DISPID->Method mapping is required.
    _public_methods_ = ["OnDoneIt"]

    def __init__(self):
        self.last_event_arg = None

    # A client must implement QI, and respond to a query for the Event interface.
    # In addition, it must provide a COM object (which server.util.wrap) does.
    def _query_interface_(self, iid):
        # Note that this seems like a necessary hack.  I am responding to IID_IConnectDemoEvents
        # but only creating an IDispatch gateway object.
        if iid == IID_IConnectDemoEvents:
            return win32com.server.util.wrap(self)

    # And here is our event method which gets called.
    def OnDoneIt(self, arg):
        self.last_event_arg = arg


def CheckEvent(server, client, val, verbose):
    client.last_event_arg = None
    server.DoIt(val)
    if client.last_event_arg != val:
        raise RuntimeError(f"Sent {val!r}, but got back {client.last_event_arg!r}")
    if verbose:
        print("Sent and received %r" % val)


# A simple test script for all this.
# In the real world, it is likely that the code controlling the server
# will be in the same class as that getting the notifications.
def test(verbose=0):
    import win32com.client.connect
    import win32com.client.dynamic
    import win32com.server.policy

    server = win32com.client.dynamic.Dispatch(
        win32com.server.util.wrap(ConnectableServer())
    )
    connection = win32com.client.connect.SimpleConnection()
    client = ConnectableClient()
    connection.Connect(server, client, IID_IConnectDemoEvents)
    CheckEvent(server, client, "Hello", verbose)
    CheckEvent(server, client, b"Here is a null>\x00<", verbose)
    CheckEvent(server, client, "Here is a null>\x00<", verbose)
    val = "test-\xe0\xf2"  # 2 extended characters.
    CheckEvent(server, client, val, verbose)
    if verbose:
        print("Everything seemed to work!")
    # Aggressive memory leak checking (ie, do nothing!) :-)  All should cleanup OK???


if __name__ == "__main__":
    test(1)

```


---

## com/win32com/demos/dump_clipboard.py

```python
import pythoncom
import win32con

formats = """CF_TEXT CF_BITMAP CF_METAFILEPICT CF_SYLK CF_DIF CF_TIFF
            CF_OEMTEXT CF_DIB CF_PALETTE CF_PENDATA CF_RIFF CF_WAVE
            CF_UNICODETEXT CF_ENHMETAFILE CF_HDROP CF_LOCALE CF_MAX
            CF_OWNERDISPLAY CF_DSPTEXT CF_DSPBITMAP CF_DSPMETAFILEPICT
            CF_DSPENHMETAFILE""".split()
format_name_map = {}
for f in formats:
    val = getattr(win32con, f)
    format_name_map[val] = f

tymeds = [attr for attr in pythoncom.__dict__ if attr.startswith("TYMED_")]


def DumpClipboard():
    do = pythoncom.OleGetClipboard()
    print("Dumping all clipboard formats...")
    for fe in do.EnumFormatEtc():
        fmt, td, aspect, index, tymed = fe
        tymeds_this = [
            getattr(pythoncom, t) for t in tymeds if tymed & getattr(pythoncom, t)
        ]
        print("Clipboard format", format_name_map.get(fmt, str(fmt)))
        for t_this in tymeds_this:
            # As we are enumerating there should be no need to call
            # QueryGetData, but we do anyway!
            fetc_query = fmt, td, aspect, index, t_this
            try:
                do.QueryGetData(fetc_query)
            except pythoncom.com_error:
                print("Eeek - QGD indicated failure for tymed", t_this)
            # now actually get it.
            try:
                medium = do.GetData(fetc_query)
            except pythoncom.com_error as exc:
                print("Failed to get the clipboard data:", exc)
                continue
            if medium.tymed == pythoncom.TYMED_GDI:
                data = "GDI handle %d" % medium.data
            elif medium.tymed == pythoncom.TYMED_MFPICT:
                data = "METAFILE handle %d" % medium.data
            elif medium.tymed == pythoncom.TYMED_ENHMF:
                data = "ENHMETAFILE handle %d" % medium.data
            elif medium.tymed == pythoncom.TYMED_HGLOBAL:
                data = "%d bytes via HGLOBAL" % len(medium.data)
            elif medium.tymed == pythoncom.TYMED_FILE:
                data = "filename '%s'" % data
            elif medium.tymed == pythoncom.TYMED_ISTREAM:
                stream = medium.data
                stream.Seek(0, 0)
                bytes = 0
                while 1:
                    chunk = stream.Read(4096)
                    if not chunk:
                        break
                    bytes += len(chunk)
                data = "%d bytes via IStream" % bytes
            elif medium.tymed == pythoncom.TYMED_ISTORAGE:
                data = "a IStorage"
            else:
                data = "*** unknown tymed!"
            print(" -> got", data)
    do = None


if __name__ == "__main__":
    DumpClipboard()
    if pythoncom._GetInterfaceCount() + pythoncom._GetGatewayCount():
        print(
            "XXX - Leaving with %d/%d COM objects alive"
            % (pythoncom._GetInterfaceCount(), pythoncom._GetGatewayCount())
        )

```


---

## com/win32com/demos/eventsApartmentThreaded.py

```python
# A sample originally provided by Richard Bell, and modified by Mark Hammond.

# This sample demonstrates how to use COM events in an aparment-threaded
# world.  In this world, COM itself ensures that all calls to and events
# from an object happen on the same thread that created the object, even
# if they originated from different threads.  For this cross-thread
# marshalling to work, this main thread *must* run a "message-loop" (ie,
# a loop fetching and dispatching Windows messages).  Without such message
# processing, dead-locks can occur.

# See also eventsFreeThreaded.py for how to do this in a free-threaded
# world where these marshalling considerations do not exist.

# NOTE: This example uses Internet Explorer, but it should not be considerd
# a "best-practices" for writing against IE events, but for working with
# events in general. For example:
# * The first OnDocumentComplete event is not a reliable indicator that the
#   URL has completed loading
# * As we are demonstrating the most efficient way of handling events, when
#   running this sample you will see an IE Windows briefly appear, but
#   vanish without ever being repainted.

import time

# sys.coinit_flags not set, so pythoncom initializes apartment-threaded.
import pythoncom
import win32api
import win32com.client
import win32event


class ExplorerEvents:
    def __init__(self):
        self.event = win32event.CreateEvent(None, 0, 0, None)

    def OnDocumentComplete(self, pDisp=pythoncom.Empty, URL=pythoncom.Empty):
        thread = win32api.GetCurrentThreadId()
        print("OnDocumentComplete event processed on thread %d" % thread)
        # Set the event our main thread is waiting on.
        win32event.SetEvent(self.event)

    def OnQuit(self):
        thread = win32api.GetCurrentThreadId()
        print("OnQuit event processed on thread %d" % thread)
        win32event.SetEvent(self.event)


def WaitWhileProcessingMessages(event, timeout=2):
    start = time.perf_counter()
    while True:
        # Wake 4 times a second - we can't just specify the
        # full timeout here, as then it would reset for every
        # message we process.
        rc = win32event.MsgWaitForMultipleObjects(
            (event,), 0, 250, win32event.QS_ALLEVENTS
        )
        if rc == win32event.WAIT_OBJECT_0:
            # event signalled - stop now!
            return True
        if (time.perf_counter() - start) > timeout:
            # Timeout expired.
            return False
        # must be a message.
        pythoncom.PumpWaitingMessages()


def TestExplorerEvents():
    iexplore = win32com.client.DispatchWithEvents(
        "InternetExplorer.Application", ExplorerEvents
    )

    thread = win32api.GetCurrentThreadId()
    print("TestExplorerEvents created IE object on thread %d" % thread)

    iexplore.Visible = 1
    try:
        iexplore.Navigate(win32api.GetFullPathName("..\\readme.html"))
    except pythoncom.com_error as details:
        print("Warning - could not open the test HTML file", details)

    # Wait for the event to be signalled while pumping messages.
    if not WaitWhileProcessingMessages(iexplore.event):
        print("Document load event FAILED to fire!!!")

    iexplore.Quit()
    #
    # Give IE a chance to shutdown, else it can get upset on fast machines.
    # Note, Quit generates events.  Although this test does NOT catch them
    # it is NECESSARY to pump messages here instead of a sleep so that the Quit
    # happens properly!
    if not WaitWhileProcessingMessages(iexplore.event):
        print("OnQuit event FAILED to fire!!!")

    iexplore = None


if __name__ == "__main__":
    TestExplorerEvents()

```


---

## com/win32com/demos/eventsFreeThreaded.py

```python
# A sample originally provided by Richard Bell, and modified by Mark Hammond.

# This sample demonstrates how to use COM events in a free-threaded world.
# In this world, there is no need to marshall calls across threads, so
# no message loops are needed at all.  This means regular cross-thread
# synchronization can be used.  In this sample we just wait on win32 event
# objects.

# See also ieEventsApartmentThreaded.py for how to do this in an
# aparment-threaded world, where thread-marshalling complicates things.

# NOTE: This example uses Internet Explorer, but it should not be considered
# a "best-practices" for writing against IE events, but for working with
# events in general. For example:
# * The first OnDocumentComplete event is not a reliable indicator that the
#   URL has completed loading
# * As we are demonstrating the most efficient way of handling events, when
#   running this sample you will see an IE Windows briefly appear, but
#   vanish without ever being repainted.

import sys

sys.coinit_flags = 0  # specify free threading


import pythoncom
import win32api
import win32com.client
import win32event


# The print statements indicate that COM has actually started another thread
# and will deliver the events to that thread (ie, the events do not actually
# fire on our main thread.
class ExplorerEvents:
    def __init__(self):
        # We reuse this event for all events.
        self.event = win32event.CreateEvent(None, 0, 0, None)

    def OnDocumentComplete(self, pDisp=pythoncom.Empty, URL=pythoncom.Empty):
        #
        # Caution:  Since the main thread and events thread(s) are different
        # it may be necessary to serialize access to shared data.  Because
        # this is a simple test case, that is not required here.  Your
        # situation may be different.   Caveat programmer.
        #
        thread = win32api.GetCurrentThreadId()
        print("OnDocumentComplete event processed on thread %d" % thread)
        # Set the event our main thread is waiting on.
        win32event.SetEvent(self.event)

    def OnQuit(self):
        thread = win32api.GetCurrentThreadId()
        print("OnQuit event processed on thread %d" % thread)
        win32event.SetEvent(self.event)


def TestExplorerEvents():
    iexplore = win32com.client.DispatchWithEvents(
        "InternetExplorer.Application", ExplorerEvents
    )

    thread = win32api.GetCurrentThreadId()
    print("TestExplorerEvents created IE object on thread %d" % thread)

    iexplore.Visible = 1
    try:
        iexplore.Navigate(win32api.GetFullPathName("..\\readme.html"))
    except pythoncom.com_error as details:
        print("Warning - could not open the test HTML file", details)

    # In this free-threaded example, we can simply wait until an event has
    # been set - we will give it 2 seconds before giving up.
    rc = win32event.WaitForSingleObject(iexplore.event, 2000)
    if rc != win32event.WAIT_OBJECT_0:
        print("Document load event FAILED to fire!!!")

    iexplore.Quit()
    # Now we can do the same thing to wait for exit!
    # Although Quit generates events, in this free-threaded world we
    # do *not* need to run any message pumps.

    rc = win32event.WaitForSingleObject(iexplore.event, 2000)
    if rc != win32event.WAIT_OBJECT_0:
        print("OnQuit event FAILED to fire!!!")

    iexplore = None
    print("Finished the IE event sample!")


if __name__ == "__main__":
    TestExplorerEvents()

```


---

## com/win32com/demos/excelAddin.py

```python
# A demo plugin for Microsoft Excel
#
# This addin simply adds a new button to the main Excel toolbar,
# and displays a message box when clicked.  Thus, it demonstrates
# how to plug in to Excel itself, and hook Excel events.
#
#
# To register the addin, simply execute:
#   excelAddin.py
# This will install the COM server, and write the necessary
# AddIn key to Excel
#
# To unregister completely:
#   excelAddin.py --unregister
#
# To debug, execute:
#   excelAddin.py --debug
#
# Then open Pythonwin, and select "Tools->Trace Collector Debugging Tool"
# Restart excel, and you should see some output generated.
#
# NOTE: If the AddIn fails with an error, Excel will re-register
# the addin to not automatically load next time Excel starts.  To
# correct this, simply re-register the addin (see above)
#
# Author <ekoome@yahoo.com> Eric Koome
# Copyright (c) 2003 Wavecom Inc.  All rights reserved
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#
# THIS SOFTWARE IS PROVIDED ``AS IS'' AND ANY EXPRESSED OR IMPLIED
# WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
# OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED.  IN NO EVENT SHALL ERIC KOOME OR
# ITS CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF
# USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT
# OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
# SUCH DAMAGE.

import sys

import pythoncom
from win32com import universal
from win32com.client import DispatchWithEvents, constants, gencache

# Support for COM objects we use.
gencache.EnsureModule(
    "{00020813-0000-0000-C000-000000000046}", 0, 1, 3, bForDemand=True
)  # Excel 9
gencache.EnsureModule(
    "{2DF8D04C-5BFA-101B-BDE5-00AA0044DE52}", 0, 2, 1, bForDemand=True
)  # Office 9

# The TLB defining the interfaces we implement
universal.RegisterInterfaces(
    "{AC0714F2-3D04-11D1-AE7D-00A0C90F26F4}", 0, 1, 0, ["_IDTExtensibility2"]
)


class ButtonEvent:
    def OnClick(self, button, cancel):
        import win32con  # Possible, but not necessary, to use a Pythonwin GUI
        import win32ui

        win32ui.MessageBox("Hello from Python", "Python Test", win32con.MB_OKCANCEL)
        return cancel


class ExcelAddin:
    _com_interfaces_ = ["_IDTExtensibility2"]
    _public_methods_ = []
    _reg_clsctx_ = pythoncom.CLSCTX_INPROC_SERVER
    _reg_clsid_ = "{C5482ECA-F559-45A0-B078-B2036E6F011A}"
    _reg_progid_ = "Python.Test.ExcelAddin"
    _reg_policy_spec_ = "win32com.server.policy.EventHandlerPolicy"

    def __init__(self):
        self.appHostApp = None

    def OnConnection(self, application, connectMode, addin, custom):
        print("OnConnection", application, connectMode, addin, custom)
        try:
            self.appHostApp = application
            cbcMyBar = self.appHostApp.CommandBars.Add(
                Name="PythonBar",
                Position=constants.msoBarTop,
                MenuBar=constants.msoBarTypeNormal,
                Temporary=True,
            )
            btnMyButton = cbcMyBar.Controls.Add(
                Type=constants.msoControlButton, Parameter="Greetings"
            )
            btnMyButton = self.toolbarButton = DispatchWithEvents(
                btnMyButton, ButtonEvent
            )
            btnMyButton.Style = constants.msoButtonCaption
            btnMyButton.BeginGroup = True
            btnMyButton.Caption = "&Python"
            btnMyButton.TooltipText = "Python rules the World"
            btnMyButton.Width = "34"
            cbcMyBar.Visible = True
        except pythoncom.com_error as xxx_todo_changeme:
            (hr, msg, exc, arg) = xxx_todo_changeme.args
            print("The Excel call failed with code %d: %s" % (hr, msg))
            if exc is None:
                print("There is no extended error information")
            else:
                wcode, source, text, helpFile, helpId, scode = exc
                print("The source of the error is", source)
                print("The error message is", text)
                print("More info can be found in %s (id=%d)" % (helpFile, helpId))

    def OnDisconnection(self, mode, custom):
        print("OnDisconnection")
        self.appHostApp.CommandBars("PythonBar").Delete
        self.appHostApp = None

    def OnAddInsUpdate(self, custom):
        print("OnAddInsUpdate", custom)

    def OnStartupComplete(self, custom):
        print("OnStartupComplete", custom)

    def OnBeginShutdown(self, custom):
        print("OnBeginShutdown", custom)


def RegisterAddin(klass):
    import winreg

    key = winreg.CreateKey(
        winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Office\\Excel\\Addins"
    )
    subkey = winreg.CreateKey(key, klass._reg_progid_)
    winreg.SetValueEx(subkey, "CommandLineSafe", 0, winreg.REG_DWORD, 0)
    winreg.SetValueEx(subkey, "LoadBehavior", 0, winreg.REG_DWORD, 3)
    winreg.SetValueEx(subkey, "Description", 0, winreg.REG_SZ, "Excel Addin")
    winreg.SetValueEx(subkey, "FriendlyName", 0, winreg.REG_SZ, "A Simple Excel Addin")


def UnregisterAddin(klass):
    import winreg

    try:
        winreg.DeleteKey(
            winreg.HKEY_CURRENT_USER,
            "Software\\Microsoft\\Office\\Excel\\Addins\\" + klass._reg_progid_,
        )
    except OSError:
        pass


if __name__ == "__main__":
    import win32com.server.register

    win32com.server.register.UseCommandLine(ExcelAddin)
    if "--unregister" in sys.argv:
        UnregisterAddin(ExcelAddin)
    else:
        RegisterAddin(ExcelAddin)

```


---

## com/win32com/demos/excelRTDServer.py

```python
"""Excel IRTDServer implementation.

This module is a functional example of how to implement the IRTDServer interface
in python, using the pywin32 extensions. Further details, about this interface
and it can be found at:
     https://learn.microsoft.com/en-us/previous-versions/office/developer/office-xp/aa140060(v=office.10)
"""

# Copyright (c) 2003-2004 by Chris Nilsson <chris@slort.org>
#
# By obtaining, using, and/or copying this software and/or its
# associated documentation, you agree that you have read, understood,
# and will comply with the following terms and conditions:
#
# Permission to use, copy, modify, and distribute this software and
# its associated documentation for any purpose and without fee is
# hereby granted, provided that the above copyright notice appears in
# all copies, and that both that copyright notice and this permission
# notice appear in supporting documentation, and that the name of
# Christopher Nilsson (the author) not be used in advertising or publicity
# pertaining to distribution of the software without specific, written
# prior permission.
#
# THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD
# TO THIS SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANT-
# ABILITY AND FITNESS.  IN NO EVENT SHALL THE AUTHOR
# BE LIABLE FOR ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY
# DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS,
# WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS
# ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE
# OF THIS SOFTWARE.

import datetime  # For the example classes...
import threading

import pythoncom
import win32com.client
from win32com import universal
from win32com.client import gencache
from win32com.server.exception import COMException

# Typelib info for version 10 - aka Excel XP.
# This is the minimum version of excel that we can work with as this is when
# Microsoft introduced these interfaces.
EXCEL_TLB_GUID = "{00020813-0000-0000-C000-000000000046}"
EXCEL_TLB_LCID = 0
EXCEL_TLB_MAJOR = 1
EXCEL_TLB_MINOR = 4

# Import the excel typelib to make sure we've got early-binding going on.
# The "ByRef" parameters we use later won't work without this.
gencache.EnsureModule(EXCEL_TLB_GUID, EXCEL_TLB_LCID, EXCEL_TLB_MAJOR, EXCEL_TLB_MINOR)

# Tell pywin to import these extra interfaces.
# --
# QUESTION: Why? The interfaces seem to descend from IDispatch, so
# I'd have thought, for example, calling callback.UpdateNotify() (on the
# IRTDUpdateEvent callback excel gives us) would work without molestation.
# But the callback needs to be cast to a "real" IRTDUpdateEvent type. Hmm...
# This is where my small knowledge of the pywin framework / COM gets hazy.
# --
# Again, we feed in the Excel typelib as the source of these interfaces.
universal.RegisterInterfaces(
    EXCEL_TLB_GUID,
    EXCEL_TLB_LCID,
    EXCEL_TLB_MAJOR,
    EXCEL_TLB_MINOR,
    ["IRtdServer", "IRTDUpdateEvent"],
)


class ExcelRTDServer:
    """Base RTDServer class.

    Provides most of the features needed to implement the IRtdServer interface.
    Manages topic adding, removal, and packing up the values for excel.

    Shouldn't be instanciated directly.

    Instead, descendant classes should override the CreateTopic() method.
    Topic objects only need to provide a GetValue() function to play nice here.
    The values given need to be atomic (eg. string, int, float... etc).

    Also note: nothing has been done within this class to ensure that we get
    time to check our topics for updates. I've left that up to the subclass
    since the ways, and needs, of refreshing your topics will vary greatly. For
    example, the sample implementation uses a timer thread to wake itself up.
    Whichever way you choose to do it, your class needs to be able to wake up
    occaisionally, since excel will never call your class without being asked to
    first.

    Excel will communicate with our object in this order:
      1. Excel instanciates our object and calls ServerStart, providing us with
         an IRTDUpdateEvent callback object.
      2. Excel calls ConnectData when it wants to subscribe to a new "topic".
      3. When we have new data to provide, we call the UpdateNotify method of the
         callback object we were given.
      4. Excel calls our RefreshData method, and receives a 2d SafeArray (row-major)
         containing the Topic ids in the 1st dim, and the topic values in the
         2nd dim.
      5. When not needed anymore, Excel will call our DisconnectData to
         unsubscribe from a topic.
      6. When there are no more topics left, Excel will call our ServerTerminate
         method to kill us.

    Throughout, at undetermined periods, Excel will call our Heartbeat
    method to see if we're still alive. It must return a non-zero value, or
    we'll be killed.

    NOTE: By default, excel will at most call RefreshData once every 2 seconds.
          This is a setting that needs to be changed excel-side. To change this,
          you can set the throttle interval like this in the excel VBA object model:
            Application.RTD.ThrottleInterval = 1000 ' milliseconds
    """

    _com_interfaces_ = ["IRtdServer"]
    _public_methods_ = [
        "ConnectData",
        "DisconnectData",
        "Heartbeat",
        "RefreshData",
        "ServerStart",
        "ServerTerminate",
    ]
    _reg_clsctx_ = pythoncom.CLSCTX_INPROC_SERVER
    # _reg_clsid_ = "# subclass must provide this class attribute"
    # _reg_desc_ = "# subclass should provide this description"
    # _reg_progid_ = "# subclass must provide this class attribute"

    ALIVE = 1
    NOT_ALIVE = 0

    def __init__(self):
        """Constructor"""
        super().__init__()
        self.IsAlive = self.ALIVE
        self.__callback = None
        self.topics = {}

    def SignalExcel(self):
        """Use the callback we were given to tell excel new data is available."""
        if self.__callback is None:
            raise COMException(desc="Callback excel provided is Null")
        self.__callback.UpdateNotify()

    def ConnectData(self, TopicID, Strings, GetNewValues):
        """Creates a new topic out of the Strings excel gives us."""
        try:
            self.topics[TopicID] = self.CreateTopic(Strings)
        except Exception as why:
            raise COMException(desc=str(why))
        GetNewValues = True
        result = self.topics[TopicID]
        if result is None:
            result = "# %s: Waiting for update" % self.__class__.__name__
        else:
            result = result.GetValue()

        # fire out internal event...
        self.OnConnectData(TopicID)

        # GetNewValues as per interface is ByRef, so we need to pass it back too.
        return result, GetNewValues

    def DisconnectData(self, TopicID):
        """Deletes the given topic."""
        self.OnDisconnectData(TopicID)

        if TopicID in self.topics:
            self.topics[TopicID] = None
            del self.topics[TopicID]

    def Heartbeat(self):
        """Called by excel to see if we're still here."""
        return self.IsAlive

    def RefreshData(self, TopicCount):
        """Packs up the topic values. Called by excel when it's ready for an update.

        Needs to:
          * Return the current number of topics, via the "ByRef" TopicCount
          * Return a 2d SafeArray of the topic data.
            - 1st dim: topic numbers
            - 2nd dim: topic values

        We could do some caching, instead of repacking everytime...
        But this works for demonstration purposes."""
        TopicCount = len(self.topics)
        self.OnRefreshData()

        # Grow the lists, so we don't need a heap of calls to append()
        results = [[None] * TopicCount, [None] * TopicCount]

        # Excel expects a 2-dimensional array. The first dim contains the
        # topic numbers, and the second contains the values for the topics.
        # In true VBA style (yuck), we need to pack the array in row-major format,
        # which looks like:
        #   ( (topic_num1, topic_num2, ..., topic_numN), \
        #     (topic_val1, topic_val2, ..., topic_valN) )
        for idx, topicdata in enumerate(self.topics.items()):
            topicNum, topic = topicdata
            results[0][idx] = topicNum
            results[1][idx] = topic.GetValue()

        # TopicCount is meant to be passed to us ByRef, so return it as well, as per
        # the way pywin32 handles ByRef arguments.
        return tuple(results), TopicCount

    def ServerStart(self, CallbackObject):
        """Excel has just created us... We take its callback for later, and set up shop."""
        self.IsAlive = self.ALIVE

        if CallbackObject is None:
            raise COMException(desc="Excel did not provide a callback")

        # Need to "cast" the raw PyIDispatch object to the IRTDUpdateEvent interface
        IRTDUpdateEventKlass = win32com.client.CLSIDToClass.GetClass(
            "{A43788C1-D91B-11D3-8F39-00C04F3651B8}"
        )
        self.__callback = IRTDUpdateEventKlass(CallbackObject)

        self.OnServerStart()

        return self.IsAlive

    def ServerTerminate(self):
        """Called when excel no longer wants us."""
        self.IsAlive = self.NOT_ALIVE  # On next heartbeat, excel will free us
        self.OnServerTerminate()

    def CreateTopic(self, TopicStrings=None):
        """Topic factory method. Subclass must override.

        Topic objects need to provide:
          * GetValue() method which returns an atomic value.

        Will raise NotImplemented if not overridden.
        """
        raise NotImplemented("Subclass must implement")

    # Overridable class events...
    def OnConnectData(self, TopicID):
        """Called when a new topic has been created, at excel's request."""
        pass

    def OnDisconnectData(self, TopicID):
        """Called when a topic is about to be deleted, at excel's request."""
        pass

    def OnRefreshData(self):
        """Called when excel has requested all current topic data."""
        pass

    def OnServerStart(self):
        """Called when excel has instanciated us."""
        pass

    def OnServerTerminate(self):
        """Called when excel is about to destroy us."""
        pass


class RTDTopic:
    """Base RTD Topic.
    Only method required by our RTDServer implementation is GetValue().
    The others are more for convenience."""

    def __init__(self, TopicStrings):
        super().__init__()
        self.TopicStrings = TopicStrings
        self.__currentValue = None
        self.__dirty = False

    def Update(self, sender):
        """Called by the RTD Server.
        Gives us a chance to check if our topic data needs to be
        changed (eg. check a file, quiz a database, etc)."""
        raise NotImplemented("subclass must implement")

    def Reset(self):
        """Call when this topic isn't considered "dirty" anymore."""
        self.__dirty = False

    def GetValue(self):
        return self.__currentValue

    def SetValue(self, value):
        self.__dirty = True
        self.__currentValue = value

    def HasChanged(self):
        return self.__dirty


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

######################################
# Example classes
######################################


class TimeServer(ExcelRTDServer):
    """Example Time RTD server.

    Sends time updates back to excel.

    example of use, in an excel sheet:
      =RTD("Python.RTD.TimeServer","","seconds","5")

    This will cause a timestamp string to fill the cell, and update its value
    every 5 seconds (or as close as possible depending on how busy excel is).

    The empty string parameter denotes the com server is running on the local
    machine. Otherwise, put in the hostname to look on. For more info
    on this, lookup the Excel help for its "RTD" worksheet function.

    Obviously, you'd want to wrap this kind of thing in a friendlier VBA
    function.

    Also, remember that the RTD function accepts a maximum of 28 arguments!
    If you want to pass more, you may need to concatenate arguments into one
    string, and have your topic parse them appropriately.
    """

    # win32com.server setup attributes...
    # Never copy the _reg_clsid_ value in your own classes!
    _reg_clsid_ = "{EA7F2CF1-11A2-45E4-B2D5-68E240DB8CB1}"
    _reg_progid_ = "Python.RTD.TimeServer"
    _reg_desc_ = "Python class implementing Excel IRTDServer -- feeds time"

    # other class attributes...
    INTERVAL = 0.5  # secs. Threaded timer will wake us up at this interval.

    def __init__(self):
        super().__init__()

        # Simply timer thread to ensure we get to update our topics, and
        # tell excel about any changes. This is a pretty basic and dirty way to
        # do this. Ideally, there should be some sort of waitable (eg. either win32
        # event, socket data event...) and be kicked off by that event triggering.
        # As soon as we set up shop here, we _must_ return control back to excel.
        # (ie. we can't block and do our own thing...)
        self.ticker = threading.Timer(self.INTERVAL, self.Update)

    def OnServerStart(self):
        self.ticker.start()

    def OnServerTerminate(self):
        if not self.ticker.finished.is_set():
            self.ticker.cancel()  # Cancel our wake-up thread. Excel has killed us.

    def Update(self):
        # Get our wake-up thread ready...
        self.ticker = threading.Timer(self.INTERVAL, self.Update)
        try:
            # Check if any of our topics have new info to pass on
            if len(self.topics):
                refresh = False
                for topic in self.topics.values():
                    topic.Update(self)
                    if topic.HasChanged():
                        refresh = True
                    topic.Reset()

                if refresh:
                    self.SignalExcel()
        finally:
            self.ticker.start()  # Make sure we get to run again

    def CreateTopic(self, TopicStrings=None):
        """Topic factory. Builds a TimeTopic object out of the given TopicStrings."""
        return TimeTopic(TopicStrings)


class TimeTopic(RTDTopic):
    """Example topic for example RTD server.

    Will accept some simple commands to alter how long to delay value updates.

    Commands:
      * seconds, delay_in_seconds
      * minutes, delay_in_minutes
      * hours, delay_in_hours
    """

    def __init__(self, TopicStrings):
        super().__init__(TopicStrings)
        try:
            self.cmd, self.delay = self.TopicStrings
        except Exception as E:
            # We could simply return a "# ERROR" type string as the
            # topic value, but explosions like this should be able to get handled by
            # the VBA-side "On Error" stuff.
            raise ValueError("Invalid topic strings: %s" % str(TopicStrings))

        # self.cmd = str(self.cmd)
        self.delay = float(self.delay)

        # setup our initial value
        self.checkpoint = self.timestamp()
        self.SetValue(str(self.checkpoint))

    def timestamp(self):
        return datetime.datetime.now()

    def Update(self, sender):
        now = self.timestamp()
        delta = now - self.checkpoint
        refresh = False
        if self.cmd == "seconds":
            if delta.seconds >= self.delay:
                refresh = True
        elif self.cmd == "minutes":
            if delta.minutes >= self.delay:
                refresh = True
        elif self.cmd == "hours":
            if delta.hours >= self.delay:
                refresh = True
        else:
            self.SetValue("#Unknown command: " + self.cmd)

        if refresh:
            self.SetValue(str(now))
            self.checkpoint = now


if __name__ == "__main__":
    import win32com.server.register

    # Register/Unregister TimeServer example
    # eg. at the command line: excelrtd.py --register
    # Then type in an excel cell something like:
    # =RTD("Python.RTD.TimeServer","","seconds","5")
    win32com.server.register.UseCommandLine(TimeServer)

```


---

## com/win32com/demos/iebutton.py

```python
# PyWin32 Internet Explorer Button
#
# written by Leonard Ritter (paniq@gmx.net)
# and Robert Förtsch (info@robert-foertsch.com)


"""
This sample implements a simple IE Button COM server
with access to the IWebBrowser2 interface.

To demonstrate:
* Execute this script to register the server.
* Open Pythonwin's Tools -> Trace Collector Debugging Tool, so you can
  see the output of 'print' statements in this demo.
* Open a new IE instance.  The toolbar should have a new "scissors" icon,
  with tooltip text "IE Button" - this is our new button - click it.
* Switch back to the Pythonwin window - you should see:
   IOleCommandTarget::Exec called.
  This is the button being clicked.  Extending this to do something more
  useful is left as an exercise.

Contribtions to this sample to make it a little "friendlier" welcome!
"""

# imports section

import pythoncom
import win32api
import win32com
import win32com.server.register

# This demo uses 'print' - use win32traceutil to see it if we have no
# console.
try:
    win32api.GetConsoleTitle()
except win32api.error:
    import win32traceutil


from win32com.axcontrol import axcontrol

# ensure we know the ms internet controls typelib so we have access to IWebBrowser2 later on
win32com.client.gencache.EnsureModule("{EAB22AC0-30C1-11CF-A7EB-0000C05BAE0B}", 0, 1, 1)


#
IObjectWithSite_methods = ["SetSite", "GetSite"]
IOleCommandTarget_methods = ["Exec", "QueryStatus"]

_iebutton_methods_ = IOleCommandTarget_methods + IObjectWithSite_methods
_iebutton_com_interfaces_ = [
    axcontrol.IID_IOleCommandTarget,
    axcontrol.IID_IObjectWithSite,  # IObjectWithSite
]


class Stub:
    """
    this class serves as a method stub,
    outputting debug info whenever the object
    is being called.
    """

    def __init__(self, name):
        self.name = name

    def __call__(self, *args):
        print("STUB: ", self.name, args)


class IEButton:
    """
    The actual COM server class
    """

    _com_interfaces_ = _iebutton_com_interfaces_
    _public_methods_ = _iebutton_methods_
    _reg_clsctx_ = pythoncom.CLSCTX_INPROC_SERVER
    _button_text_ = "IE Button"
    _tool_tip_ = "An example implementation for an IE Button."
    _icon_ = ""
    _hot_icon_ = ""

    def __init__(self):
        # put stubs for non-implemented methods
        for method in self._public_methods_:
            if not hasattr(self, method):
                print("providing default stub for %s" % method)
                setattr(self, method, Stub(method))

    def QueryStatus(self, pguidCmdGroup, prgCmds, cmdtextf):
        # 'cmdtextf' is the 'cmdtextf' element from the OLECMDTEXT structure,
        # or None if a NULL pointer was passed.
        result = []
        for id, flags in prgCmds:
            flags |= axcontrol.OLECMDF_SUPPORTED | axcontrol.OLECMDF_ENABLED
            result.append((id, flags))
        if cmdtextf is None:
            cmdtext = None  # must return None if nothing requested.
        # IE never seems to want any text - this code is here for
        # demo purposes only
        elif cmdtextf == axcontrol.OLECMDTEXTF_NAME:
            cmdtext = "IEButton Name"
        else:
            cmdtext = "IEButton State"
        return result, cmdtext

    def Exec(self, pguidCmdGroup, nCmdID, nCmdExecOpt, pvaIn):
        print(pguidCmdGroup, nCmdID, nCmdExecOpt, pvaIn)
        print("IOleCommandTarget::Exec called.")
        # self.webbrowser.ShowBrowserBar(GUID_IETOOLBAR, not is_ietoolbar_visible())

    def SetSite(self, unknown):
        if unknown:
            # first get a command target
            cmdtarget = unknown.QueryInterface(axcontrol.IID_IOleCommandTarget)
            # then travel over to a service provider
            serviceprovider = cmdtarget.QueryInterface(pythoncom.IID_IServiceProvider)
            # finally ask for the internet explorer application, returned as a dispatch object
            self.webbrowser = win32com.client.Dispatch(
                serviceprovider.QueryService(
                    "{0002DF05-0000-0000-C000-000000000046}", pythoncom.IID_IDispatch
                )
            )
        else:
            # lose all references
            self.webbrowser = None

    def GetClassID(self):
        return self._reg_clsid_


def register(classobj):
    import winreg

    subKeyCLSID = (
        "SOFTWARE\\Microsoft\\Internet Explorer\\Extensions\\%38s"
        % classobj._reg_clsid_
    )
    try:
        hKey = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, subKeyCLSID)
        subKey = winreg.SetValueEx(
            hKey, "ButtonText", 0, winreg.REG_SZ, classobj._button_text_
        )
        winreg.SetValueEx(
            hKey, "ClsidExtension", 0, winreg.REG_SZ, classobj._reg_clsid_
        )  # reg value for calling COM object
        winreg.SetValueEx(
            hKey, "CLSID", 0, winreg.REG_SZ, "{1FBA04EE-3024-11D2-8F1F-0000F87ABD16}"
        )  # CLSID for button that sends command to COM object
        winreg.SetValueEx(hKey, "Default Visible", 0, winreg.REG_SZ, "Yes")
        winreg.SetValueEx(hKey, "ToolTip", 0, winreg.REG_SZ, classobj._tool_tip_)
        winreg.SetValueEx(hKey, "Icon", 0, winreg.REG_SZ, classobj._icon_)
        winreg.SetValueEx(hKey, "HotIcon", 0, winreg.REG_SZ, classobj._hot_icon_)
    except OSError:
        print("Couldn't set standard toolbar reg keys.")
    else:
        print("Set standard toolbar reg keys.")


def unregister(classobj):
    import winreg

    subKeyCLSID = (
        "SOFTWARE\\Microsoft\\Internet Explorer\\Extensions\\%38s"
        % classobj._reg_clsid_
    )
    try:
        hKey = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, subKeyCLSID)
        subKey = winreg.DeleteValue(hKey, "ButtonText")
        winreg.DeleteValue(hKey, "ClsidExtension")  # for calling COM object
        winreg.DeleteValue(hKey, "CLSID")
        winreg.DeleteValue(hKey, "Default Visible")
        winreg.DeleteValue(hKey, "ToolTip")
        winreg.DeleteValue(hKey, "Icon")
        winreg.DeleteValue(hKey, "HotIcon")
        winreg.DeleteKey(winreg.HKEY_LOCAL_MACHINE, subKeyCLSID)
    except OSError:
        print("Couldn't delete Standard toolbar regkey.")
    else:
        print("Deleted Standard toolbar regkey.")


#
# test implementation
#


class PyWin32InternetExplorerButton(IEButton):
    _reg_clsid_ = "{104B66A9-9E68-49D1-A3F5-94754BE9E0E6}"
    _reg_progid_ = "PyWin32.IEButton"
    _reg_desc_ = "Test Button"
    _button_text_ = "IE Button"
    _tool_tip_ = "An example implementation for an IE Button."
    _icon_ = ""
    _hot_icon_ = _icon_


def DllRegisterServer():
    register(PyWin32InternetExplorerButton)


def DllUnregisterServer():
    unregister(PyWin32InternetExplorerButton)


if __name__ == "__main__":
    win32com.server.register.UseCommandLine(
        PyWin32InternetExplorerButton,
        finalize_register=DllRegisterServer,
        finalize_unregister=DllUnregisterServer,
    )

```


---

## com/win32com/demos/ietoolbar.py

```python
# PyWin32 Internet Explorer Toolbar
#
# written by Leonard Ritter (paniq@gmx.net)
# and Robert Förtsch (info@robert-foertsch.com)


"""
This sample implements a simple IE Toolbar COM server
supporting Windows XP styles and access to
the IWebBrowser2 interface.

It also demonstrates how to hijack the parent window
to catch WM_COMMAND messages.
"""

import array
import struct

# imports section
import sys
import winreg

import commctrl
import pythoncom
import win32com
import win32con
import win32gui
import win32ui
from win32com.axcontrol import axcontrol
from win32com.client import Dispatch, gencache
from win32com.shell import shell
from win32com.shell.shellcon import DBIMF_VARIABLEHEIGHT

# ensure we know the ms internet controls typelib so we have access to IWebBrowser2 later on
gencache.EnsureModule("{EAB22AC0-30C1-11CF-A7EB-0000C05BAE0B}", 0, 1, 1)

#
IDeskBand_methods = ["GetBandInfo"]
IDockingWindow_methods = ["ShowDW", "CloseDW", "ResizeBorderDW"]
IOleWindow_methods = ["GetWindow", "ContextSensitiveHelp"]
IInputObject_methods = ["UIActivateIO", "HasFocusIO", "TranslateAcceleratorIO"]
IObjectWithSite_methods = ["SetSite", "GetSite"]
IPersistStream_methods = ["GetClassID", "IsDirty", "Load", "Save", "GetSizeMax"]

_ietoolbar_methods_ = (
    IDeskBand_methods
    + IDockingWindow_methods
    + IOleWindow_methods
    + IInputObject_methods
    + IObjectWithSite_methods
    + IPersistStream_methods
)
_ietoolbar_com_interfaces_ = [
    shell.IID_IDeskBand,  # IDeskBand
    axcontrol.IID_IObjectWithSite,  # IObjectWithSite
    pythoncom.IID_IPersistStream,
    axcontrol.IID_IOleCommandTarget,
]


class WIN32STRUCT:
    def __init__(self, **kw):
        full_fmt = ""
        for name, fmt, default in self._struct_items_:
            self.__dict__[name] = None
            if fmt == "z":
                full_fmt += "pi"
            else:
                full_fmt += fmt
        for name, val in kw.items():
            self.__dict__[name] = val

    def __setattr__(self, attr, val):
        if not attr.startswith("_") and attr not in self.__dict__:
            raise AttributeError(attr)
        self.__dict__[attr] = val

    def toparam(self):
        self._buffs = []
        full_fmt = ""
        vals = []
        for name, fmt, default in self._struct_items_:
            val = self.__dict__[name]
            if fmt == "z":
                fmt = "Pi"
                if val is None:
                    vals.append(0)
                    vals.append(0)
                else:
                    str_buf = array.array("c", val + "\0")
                    vals.append(str_buf.buffer_info()[0])
                    vals.append(len(val))
                    self._buffs.append(str_buf)  # keep alive during the call.
            else:
                if val is None:
                    val = default
                vals.append(val)
            full_fmt += fmt
        return struct.pack(*(full_fmt,) + tuple(vals))


class TBBUTTON(WIN32STRUCT):
    _struct_items_ = [
        ("iBitmap", "i", 0),
        ("idCommand", "i", 0),
        ("fsState", "B", 0),
        ("fsStyle", "B", 0),
        ("bReserved", "H", 0),
        ("dwData", "I", 0),
        ("iString", "z", None),
    ]


class Stub:
    """
    this class serves as a method stub,
    outputting debug info whenever the object
    is being called.
    """

    def __init__(self, name):
        self.name = name

    def __call__(self, *args):
        print("STUB: ", self.name, args)


class IEToolbarCtrl:
    """
    a tiny wrapper for our winapi-based
    toolbar control implementation.
    """

    def __init__(self, hwndparent):
        styles = (
            win32con.WS_CHILD
            | win32con.WS_VISIBLE
            | win32con.WS_CLIPSIBLINGS
            | win32con.WS_CLIPCHILDREN
            | commctrl.TBSTYLE_LIST
            | commctrl.TBSTYLE_FLAT
            | commctrl.TBSTYLE_TRANSPARENT
            | commctrl.CCS_TOP
            | commctrl.CCS_NODIVIDER
            | commctrl.CCS_NORESIZE
            | commctrl.CCS_NOPARENTALIGN
        )
        self.hwnd = win32gui.CreateWindow(
            "ToolbarWindow32",
            None,
            styles,
            0,
            0,
            100,
            100,
            hwndparent,
            0,
            win32gui.dllhandle,
            None,
        )
        win32gui.SendMessage(self.hwnd, commctrl.TB_BUTTONSTRUCTSIZE, 20, 0)

    def ShowWindow(self, mode):
        win32gui.ShowWindow(self.hwnd, mode)

    def AddButtons(self, *buttons):
        tbbuttons = ""
        for button in buttons:
            tbbuttons += button.toparam()
        return win32gui.SendMessage(
            self.hwnd, commctrl.TB_ADDBUTTONS, len(buttons), tbbuttons
        )

    def GetSafeHwnd(self):
        return self.hwnd


class IEToolbar:
    """
    The actual COM server class
    """

    _com_interfaces_ = _ietoolbar_com_interfaces_
    _public_methods_ = _ietoolbar_methods_
    _reg_clsctx_ = pythoncom.CLSCTX_INPROC_SERVER
    # if you copy and modify this example, be sure to change the clsid below
    _reg_clsid_ = "{F21202A2-959A-4149-B1C3-68B9013F3335}"
    _reg_progid_ = "PyWin32.IEToolbar"
    _reg_desc_ = "PyWin32 IE Toolbar"

    def __init__(self):
        # put stubs for non-implemented methods
        for method in self._public_methods_:
            if not hasattr(self, method):
                print("providing default stub for %s" % method)
                setattr(self, method, Stub(method))

    def GetWindow(self):
        return self.toolbar.GetSafeHwnd()

    def Load(self, stream):
        # called when the toolbar is loaded
        pass

    def Save(self, pStream, fClearDirty):
        # called when the toolbar shall save its information
        pass

    def CloseDW(self, dwReserved):
        del self.toolbar

    def ShowDW(self, bShow):
        if bShow:
            self.toolbar.ShowWindow(win32con.SW_SHOW)
        else:
            self.toolbar.ShowWindow(win32con.SW_HIDE)

    def on_first_button(self):
        print("first!")
        self.webbrowser.Navigate2("https://github.com/mhammond/pywin32")

    def on_second_button(self):
        print("second!")

    def on_third_button(self):
        print("third!")

    def toolbar_command_handler(self, args):
        hwnd, message, wparam, lparam, time, point = args
        if lparam == self.toolbar.GetSafeHwnd():
            self._command_map[wparam]()

    def SetSite(self, unknown):
        if unknown:
            # retrieve the parent window interface for this site
            olewindow = unknown.QueryInterface(pythoncom.IID_IOleWindow)
            # ask the window for its handle
            hwndparent = olewindow.GetWindow()

            # first get a command target
            cmdtarget = unknown.QueryInterface(axcontrol.IID_IOleCommandTarget)
            # then travel over to a service provider
            serviceprovider = cmdtarget.QueryInterface(pythoncom.IID_IServiceProvider)
            # finally ask for the internet explorer application, returned as a dispatch object
            self.webbrowser = Dispatch(
                serviceprovider.QueryService(
                    "{0002DF05-0000-0000-C000-000000000046}", pythoncom.IID_IDispatch
                )
            )

            # now create and set up the toolbar
            self.toolbar = IEToolbarCtrl(hwndparent)

            buttons = [
                ("Visit PyWin32 Homepage", self.on_first_button),
                ("Another Button", self.on_second_button),
                ("Yet Another Button", self.on_third_button),
            ]

            self._command_map = {}
            # wrap our parent window so we can hook message handlers
            window = win32ui.CreateWindowFromHandle(hwndparent)

            # add the buttons
            for i in range(len(buttons)):
                button = TBBUTTON()
                name, func = buttons[i]
                id = 0x4444 + i
                button.iBitmap = -2
                button.idCommand = id
                button.fsState = commctrl.TBSTATE_ENABLED
                button.fsStyle = commctrl.TBSTYLE_BUTTON
                button.iString = name
                self._command_map[0x4444 + i] = func
                self.toolbar.AddButtons(button)
                window.HookMessage(self.toolbar_command_handler, win32con.WM_COMMAND)
        else:
            # lose all references
            self.webbrowser = None

    def GetClassID(self):
        return self._reg_clsid_

    def GetBandInfo(self, dwBandId, dwViewMode, dwMask):
        ptMinSize = (0, 24)
        ptMaxSize = (2000, 24)
        ptIntegral = (0, 0)
        ptActual = (2000, 24)
        wszTitle = "PyWin32 IE Toolbar"
        dwModeFlags = DBIMF_VARIABLEHEIGHT
        crBkgnd = 0
        return (
            ptMinSize,
            ptMaxSize,
            ptIntegral,
            ptActual,
            wszTitle,
            dwModeFlags,
            crBkgnd,
        )


# used for HKLM install
def DllInstall(bInstall, cmdLine):
    comclass = IEToolbar


# register plugin
def DllRegisterServer():
    comclass = IEToolbar

    # register toolbar with IE
    try:
        print("Trying to register Toolbar.\n")
        hkey = winreg.CreateKey(
            winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Microsoft\\Internet Explorer\\Toolbar"
        )
        subKey = winreg.SetValueEx(
            hkey, comclass._reg_clsid_, 0, winreg.REG_BINARY, b"\0"
        )
    except OSError:
        print(
            "Couldn't set registry value.\nhkey: %d\tCLSID: %s\n"
            % (hkey, comclass._reg_clsid_)
        )
    else:
        print(
            "Set registry value.\nhkey: %d\tCLSID: %s\n" % (hkey, comclass._reg_clsid_)
        )
    # TODO: implement reg settings for standard toolbar button


# unregister plugin
def DllUnregisterServer():
    comclass = IEToolbar

    # unregister toolbar from internet explorer
    try:
        print("Trying to unregister Toolbar.\n")
        hkey = winreg.CreateKey(
            winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Microsoft\\Internet Explorer\\Toolbar"
        )
        winreg.DeleteValue(hkey, comclass._reg_clsid_)
    except OSError:
        print(
            "Couldn't delete registry value.\nhkey: %d\tCLSID: %s\n"
            % (hkey, comclass._reg_clsid_)
        )
    else:
        print("Deleting reg key succeeded.\n")


# entry point
if __name__ == "__main__":
    import win32com.server.register

    win32com.server.register.UseCommandLine(IEToolbar)

    # parse actual command line option
    if "--unregister" in sys.argv:
        DllUnregisterServer()
    else:
        DllRegisterServer()
else:
    # import trace utility for remote debugging
    import win32traceutil

```


---

## com/win32com/demos/outlookAddin.py

```python
# A demo plugin for Microsoft Outlook (NOT Outlook Express)
#
# This addin simply adds a new button to the main Outlook toolbar,
# and displays a message box when clicked.  Thus, it demonstrates
# how to plug in to Outlook itself, and hook outlook events.
#
# Additionally, each time a new message arrives in the Inbox, a message
# is printed with the subject of the message.
#
# To register the addin, simply execute:
#   outlookAddin.py
# This will install the COM server, and write the necessary
# AddIn key to Outlook
#
# To unregister completely:
#   outlookAddin.py --unregister
#
# To debug, execute:
#   outlookAddin.py --debug
#
# Then open Pythonwin, and select "Tools->Trace Collector Debugging Tool"
# Restart Outlook, and you should see some output generated.
#
# NOTE: If the AddIn fails with an error, Outlook will re-register
# the addin to not automatically load next time Outlook starts.  To
# correct this, simply re-register the addin (see above)

import sys

import pythoncom
from win32com import universal
from win32com.client import DispatchWithEvents, constants, gencache

# Support for COM objects we use.
gencache.EnsureModule(
    "{00062FFF-0000-0000-C000-000000000046}", 0, 9, 0, bForDemand=True
)  # Outlook 9
gencache.EnsureModule(
    "{2DF8D04C-5BFA-101B-BDE5-00AA0044DE52}", 0, 2, 1, bForDemand=True
)  # Office 9

# The TLB defining the interfaces we implement
universal.RegisterInterfaces(
    "{AC0714F2-3D04-11D1-AE7D-00A0C90F26F4}", 0, 1, 0, ["_IDTExtensibility2"]
)


class ButtonEvent:
    def OnClick(self, button, cancel):
        import win32ui  # Possible, but not necessary, to use a Pythonwin GUI

        win32ui.MessageBox("Hello from Python")
        return cancel


class FolderEvent:
    def OnItemAdd(self, item):
        try:
            print("An item was added to the inbox with subject:", item.Subject)
        except AttributeError:
            print(f"An item was added to the inbox, but it has no subject! - {item!r}")


class OutlookAddin:
    _com_interfaces_ = ["_IDTExtensibility2"]
    _public_methods_ = []
    _reg_clsctx_ = pythoncom.CLSCTX_INPROC_SERVER
    _reg_clsid_ = "{0F47D9F3-598B-4d24-B7E3-92AC15ED27E2}"
    _reg_progid_ = "Python.Test.OutlookAddin"
    _reg_policy_spec_ = "win32com.server.policy.EventHandlerPolicy"

    def OnConnection(self, application, connectMode, addin, custom):
        print("OnConnection", application, connectMode, addin, custom)
        # ActiveExplorer may be none when started without a UI (eg, WinCE synchronisation)
        activeExplorer = application.ActiveExplorer()
        if activeExplorer is not None:
            bars = activeExplorer.CommandBars
            toolbar = bars.Item("Standard")
            item = toolbar.Controls.Add(Type=constants.msoControlButton, Temporary=True)
            # Hook events for the item
            item = self.toolbarButton = DispatchWithEvents(item, ButtonEvent)
            item.Caption = "Python"
            item.TooltipText = "Click for Python"
            item.Enabled = True

        # And now, for the sake of demonstration, setup a hook for all new messages
        inbox = application.Session.GetDefaultFolder(constants.olFolderInbox)
        self.inboxItems = DispatchWithEvents(inbox.Items, FolderEvent)

    def OnDisconnection(self, mode, custom):
        print("OnDisconnection")

    def OnAddInsUpdate(self, custom):
        print("OnAddInsUpdate", custom)

    def OnStartupComplete(self, custom):
        print("OnStartupComplete", custom)

    def OnBeginShutdown(self, custom):
        print("OnBeginShutdown", custom)


def RegisterAddin(klass):
    import winreg

    key = winreg.CreateKey(
        winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Office\\Outlook\\Addins"
    )
    subkey = winreg.CreateKey(key, klass._reg_progid_)
    winreg.SetValueEx(subkey, "CommandLineSafe", 0, winreg.REG_DWORD, 0)
    winreg.SetValueEx(subkey, "LoadBehavior", 0, winreg.REG_DWORD, 3)
    winreg.SetValueEx(subkey, "Description", 0, winreg.REG_SZ, klass._reg_progid_)
    winreg.SetValueEx(subkey, "FriendlyName", 0, winreg.REG_SZ, klass._reg_progid_)


def UnregisterAddin(klass):
    import winreg

    try:
        winreg.DeleteKey(
            winreg.HKEY_CURRENT_USER,
            "Software\\Microsoft\\Office\\Outlook\\Addins\\" + klass._reg_progid_,
        )
    except OSError:
        pass


if __name__ == "__main__":
    import win32com.server.register

    win32com.server.register.UseCommandLine(OutlookAddin)
    if "--unregister" in sys.argv:
        UnregisterAddin(OutlookAddin)
    else:
        RegisterAddin(OutlookAddin)

```


---

## com/win32com/demos/trybag.py

```python
import pythoncom
from win32com.server import util
from win32com.server.exception import COMException

VT_EMPTY = pythoncom.VT_EMPTY


class Bag:
    _public_methods_ = ["Read", "Write"]
    _com_interfaces_ = [pythoncom.IID_IPropertyBag]

    def __init__(self):
        self.data = {}

    def Read(self, propName, varType, errorLog):
        print("read: name=", propName, "type=", varType)
        if propName not in self.data:
            if errorLog:
                hr = 0x80070057
                exc = pythoncom.com_error(0, "Bag.Read", "no such item", None, 0, hr)
                errorLog.AddError(propName, exc)
            raise COMException(scode=hr)
        return self.data[propName]

    def Write(self, propName, value):
        print("write: name=", propName, "value=", value)
        self.data[propName] = value


class Target:
    _public_methods_ = ["GetClassID", "InitNew", "Load", "Save"]
    _com_interfaces_ = [pythoncom.IID_IPersist, pythoncom.IID_IPersistPropertyBag]

    def GetClassID(self):
        raise COMException(scode=0x80004005)  # E_FAIL

    def InitNew(self):
        pass

    def Load(self, bag, log):
        print(bag.Read("prop1", VT_EMPTY, log))
        print(bag.Read("prop2", VT_EMPTY, log))
        try:
            print(bag.Read("prop3", VT_EMPTY, log))
        except COMException:
            pass

    def Save(self, bag, clearDirty, saveAllProps):
        bag.Write("prop1", "prop1.hello")
        bag.Write("prop2", "prop2.there")


class Log:
    _public_methods_ = ["AddError"]
    _com_interfaces_ = [pythoncom.IID_IErrorLog]

    def AddError(self, propName, excepInfo):
        print("error: propName=", propName, "error=", excepInfo)


def test():
    bag = Bag()
    target = Target()
    log = Log()

    target.Save(bag, 1, 1)
    target.Load(bag, log)

    comBag = util.wrap(bag, pythoncom.IID_IPropertyBag)
    comTarget = util.wrap(target, pythoncom.IID_IPersistPropertyBag)
    comLog = util.wrap(log, pythoncom.IID_IErrorLog)

    comTarget.Save(comBag, 1, 1)
    comTarget.Load(comBag, comLog)


if __name__ == "__main__":
    test()

```
