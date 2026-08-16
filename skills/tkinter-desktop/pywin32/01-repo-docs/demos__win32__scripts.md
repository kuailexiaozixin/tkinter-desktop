# 官方示例源码 · win32/scripts

> 来源 https://github.com/mhammond/pywin32/tree/main/win32/scripts （共 12 个 .py，全文内联）


---

## win32/scripts/ControlService.py

```python
# ControlService.py
#
# A simple app which duplicates some of the functionality in the
# Services applet of the control panel.
#
# Suggested enhancements (in no particular order):
#
# 1. When changing the service status, continue to query the status
# of the service until the status change is complete.  Use this
# information to put up some kind of a progress dialog like the CP
# applet does.  Unlike the CP, allow canceling out in the event that
# the status change hangs.
# 2. When starting or stopping a service with dependencies, alert
# the user about the dependent services, then start (or stop) all
# dependent services as appropriate.
# 3. Allow toggling between service view and device view
# 4. Allow configuration of other service parameters such as startup
# name and password.
# 5. Allow connection to remote SCMs.  This is just a matter of
# reconnecting to the SCM on the remote machine; the rest of the
# code should still work the same.
# 6. Either implement the startup parameters or get rid of the editbox.
# 7. Either implement or get rid of "H/W Profiles".
# 8. Either implement or get rid of "Help".
# 9. Improve error handling.  Ideally, this would also include falling
# back to lower levels of functionality for users with less rights.
# Right now, we always try to get all the rights and fail when we can't


import win32con
import win32service
import win32ui
from pywin.mfc import dialog


class StartupDlg(dialog.Dialog):
    IDC_LABEL = 127
    IDC_DEVICE = 128
    IDC_BOOT = 129
    IDC_SYSTEM = 130
    IDC_AUTOMATIC = 131
    IDC_MANUAL = 132
    IDC_DISABLED = 133

    def __init__(self, displayname, service):
        dialog.Dialog.__init__(self, self.GetResource())
        self.name = displayname
        self.service = service

    def __del__(self):
        win32service.CloseServiceHandle(self.service)

    def OnInitDialog(self):
        cfg = win32service.QueryServiceConfig(self.service)
        self.GetDlgItem(self.IDC_BOOT + cfg[1]).SetCheck(1)

        status = win32service.QueryServiceStatus(self.service)
        if (status[0] & win32service.SERVICE_KERNEL_DRIVER) or (
            status[0] & win32service.SERVICE_FILE_SYSTEM_DRIVER
        ):
            # driver
            self.GetDlgItem(self.IDC_LABEL).SetWindowText("Device:")
        else:
            # service
            self.GetDlgItem(self.IDC_LABEL).SetWindowText("Service:")
            self.GetDlgItem(self.IDC_BOOT).EnableWindow(0)
            self.GetDlgItem(self.IDC_SYSTEM).EnableWindow(0)
        self.GetDlgItem(self.IDC_DEVICE).SetWindowText(str(self.name))

        return dialog.Dialog.OnInitDialog(self)

    def OnOK(self):
        self.BeginWaitCursor()
        starttype = (
            self.GetCheckedRadioButton(self.IDC_BOOT, self.IDC_DISABLED) - self.IDC_BOOT
        )
        try:
            win32service.ChangeServiceConfig(
                self.service,
                win32service.SERVICE_NO_CHANGE,
                starttype,
                win32service.SERVICE_NO_CHANGE,
                None,
                None,
                0,
                None,
                None,
                None,
                None,
            )
        except:
            self.MessageBox(
                "Unable to change startup configuration",
                None,
                win32con.MB_ICONEXCLAMATION,
            )
        self.EndWaitCursor()
        return dialog.Dialog.OnOK(self)

    def GetResource(self):
        style = (
            win32con.WS_POPUP
            | win32con.DS_SETFONT
            | win32con.WS_SYSMENU
            | win32con.WS_CAPTION
            | win32con.WS_VISIBLE
            | win32con.DS_MODALFRAME
        )
        exstyle = None
        t = [
            ["Service Startup", (6, 18, 188, 107), style, exstyle, (8, "MS Shell Dlg")],
        ]
        t.append(
            [
                130,
                "Device:",
                self.IDC_LABEL,
                (6, 7, 40, 8),
                win32con.WS_VISIBLE | win32con.WS_CHILD | win32con.SS_LEFT,
            ]
        )
        t.append(
            [
                130,
                "",
                self.IDC_DEVICE,
                (48, 7, 134, 8),
                win32con.WS_VISIBLE | win32con.WS_CHILD | win32con.SS_LEFT,
            ]
        )
        t.append(
            [
                128,
                "Startup Type",
                -1,
                (6, 21, 130, 80),
                win32con.WS_VISIBLE
                | win32con.WS_CHILD
                | win32con.WS_GROUP
                | win32con.BS_GROUPBOX,
            ]
        )
        t.append(
            [
                128,
                "&Boot",
                self.IDC_BOOT,
                (12, 33, 39, 10),
                win32con.WS_VISIBLE
                | win32con.WS_CHILD
                | win32con.WS_TABSTOP
                | win32con.BS_AUTORADIOBUTTON,
            ]
        )
        t.append(
            [
                128,
                "&System",
                self.IDC_SYSTEM,
                (12, 46, 39, 10),
                win32con.WS_VISIBLE
                | win32con.WS_CHILD
                | win32con.WS_TABSTOP
                | win32con.BS_AUTORADIOBUTTON,
            ]
        )
        t.append(
            [
                128,
                "&Automatic",
                self.IDC_AUTOMATIC,
                (12, 59, 118, 10),
                win32con.WS_VISIBLE
                | win32con.WS_CHILD
                | win32con.WS_TABSTOP
                | win32con.BS_AUTORADIOBUTTON,
            ]
        )
        t.append(
            [
                128,
                "&Manual",
                self.IDC_MANUAL,
                (12, 72, 118, 10),
                win32con.WS_VISIBLE
                | win32con.WS_CHILD
                | win32con.WS_TABSTOP
                | win32con.BS_AUTORADIOBUTTON,
            ]
        )
        t.append(
            [
                128,
                "&Disabled",
                self.IDC_DISABLED,
                (12, 85, 118, 10),
                win32con.WS_VISIBLE
                | win32con.WS_CHILD
                | win32con.WS_TABSTOP
                | win32con.BS_AUTORADIOBUTTON,
            ]
        )
        t.append(
            [
                128,
                "OK",
                win32con.IDOK,
                (142, 25, 40, 14),
                win32con.WS_VISIBLE
                | win32con.WS_CHILD
                | win32con.WS_TABSTOP
                | win32con.WS_GROUP
                | win32con.BS_DEFPUSHBUTTON,
            ]
        )
        t.append(
            [
                128,
                "Cancel",
                win32con.IDCANCEL,
                (142, 43, 40, 14),
                win32con.WS_VISIBLE
                | win32con.WS_CHILD
                | win32con.WS_TABSTOP
                | win32con.BS_PUSHBUTTON,
            ]
        )
        t.append(
            [
                128,
                "&Help",
                win32con.IDHELP,
                (142, 61, 40, 14),
                win32con.WS_VISIBLE
                | win32con.WS_CHILD
                | win32con.WS_TABSTOP
                | win32con.BS_PUSHBUTTON,
            ]
        )
        return t


class ServiceDlg(dialog.Dialog):
    IDC_LIST = 128
    IDC_START = 129
    IDC_STOP = 130
    IDC_PAUSE = 131
    IDC_CONTINUE = 132
    IDC_STARTUP = 133
    IDC_PROFILES = 134
    IDC_PARAMS = 135

    def __init__(self, machineName=""):
        dialog.Dialog.__init__(self, self.GetResource())
        self.HookCommand(self.OnListEvent, self.IDC_LIST)
        self.HookCommand(self.OnStartCmd, self.IDC_START)
        self.HookCommand(self.OnStopCmd, self.IDC_STOP)
        self.HookCommand(self.OnPauseCmd, self.IDC_PAUSE)
        self.HookCommand(self.OnContinueCmd, self.IDC_CONTINUE)
        self.HookCommand(self.OnStartupCmd, self.IDC_STARTUP)
        self.machineName = machineName
        self.scm = win32service.OpenSCManager(
            self.machineName, None, win32service.SC_MANAGER_ALL_ACCESS
        )

    def __del__(self):
        win32service.CloseServiceHandle(self.scm)

    def OnInitDialog(self):
        self.listCtrl = self.GetDlgItem(self.IDC_LIST)
        self.listCtrl.SetTabStops([158, 200])
        if self.machineName:
            self.SetWindowText("Services on %s" % self.machineName)
        self.ReloadData()
        return dialog.Dialog.OnInitDialog(self)

    def ReloadData(self):
        service = self.GetSelService()
        self.listCtrl.SetRedraw(0)
        self.listCtrl.ResetContent()
        svcs = win32service.EnumServicesStatus(self.scm)
        i = 0
        self.data = []
        for svc in svcs:
            try:
                status = (
                    "Unknown",
                    "Stopped",
                    "Starting",
                    "Stopping",
                    "Running",
                    "Continuing",
                    "Pausing",
                    "Paused",
                )[svc[2][1]]
            except:
                status = "Unknown"
            s = win32service.OpenService(
                self.scm, svc[0], win32service.SERVICE_ALL_ACCESS
            )
            cfg = win32service.QueryServiceConfig(s)
            try:
                startup = ("Boot", "System", "Automatic", "Manual", "Disabled")[cfg[1]]
            except:
                startup = "Unknown"
            win32service.CloseServiceHandle(s)

            # svc[2][2] control buttons
            pos = self.listCtrl.AddString(str(svc[1]) + "\t" + status + "\t" + startup)
            self.listCtrl.SetItemData(pos, i)
            self.data.append(
                tuple(svc[2])
                + (
                    svc[1],
                    svc[0],
                )
            )
            i += 1

            if service and service[1] == svc[0]:
                self.listCtrl.SetCurSel(pos)
        self.OnListEvent(self.IDC_LIST, win32con.LBN_SELCHANGE)
        self.listCtrl.SetRedraw(1)

    def OnListEvent(self, id, code):
        if code == win32con.LBN_SELCHANGE or code == win32con.LBN_SELCANCEL:
            pos = self.listCtrl.GetCurSel()
            if pos >= 0:
                data = self.data[self.listCtrl.GetItemData(pos)][2]
                canstart = (
                    self.data[self.listCtrl.GetItemData(pos)][1]
                    == win32service.SERVICE_STOPPED
                )
            else:
                data = 0
                canstart = 0
            self.GetDlgItem(self.IDC_START).EnableWindow(canstart)
            self.GetDlgItem(self.IDC_STOP).EnableWindow(
                data & win32service.SERVICE_ACCEPT_STOP
            )
            self.GetDlgItem(self.IDC_PAUSE).EnableWindow(
                data & win32service.SERVICE_ACCEPT_PAUSE_CONTINUE
            )
            self.GetDlgItem(self.IDC_CONTINUE).EnableWindow(
                data & win32service.SERVICE_ACCEPT_PAUSE_CONTINUE
            )

    def GetSelService(self):
        pos = self.listCtrl.GetCurSel()
        if pos < 0:
            return None
        pos = self.listCtrl.GetItemData(pos)
        return self.data[pos][-2:]

    def OnStartCmd(self, id, code):
        service = self.GetSelService()
        if not service:
            return
        s = win32service.OpenService(
            self.scm, service[1], win32service.SERVICE_ALL_ACCESS
        )
        win32service.StartService(s, None)
        win32service.CloseServiceHandle(s)
        self.ReloadData()

    def OnStopCmd(self, id, code):
        service = self.GetSelService()
        if not service:
            return
        s = win32service.OpenService(
            self.scm, service[1], win32service.SERVICE_ALL_ACCESS
        )
        win32service.ControlService(s, win32service.SERVICE_CONTROL_STOP)
        win32service.CloseServiceHandle(s)
        self.ReloadData()

    def OnPauseCmd(self, id, code):
        service = self.GetSelService()
        if not service:
            return
        s = win32service.OpenService(
            self.scm, service[1], win32service.SERVICE_ALL_ACCESS
        )
        win32service.ControlService(s, win32service.SERVICE_CONTROL_PAUSE)
        win32service.CloseServiceHandle(s)
        self.ReloadData()

    def OnContinueCmd(self, id, code):
        service = self.GetSelService()
        if not service:
            return
        s = win32service.OpenService(
            self.scm, service[1], win32service.SERVICE_ALL_ACCESS
        )
        win32service.ControlService(s, win32service.SERVICE_CONTROL_CONTINUE)
        win32service.CloseServiceHandle(s)
        self.ReloadData()

    def OnStartupCmd(self, id, code):
        service = self.GetSelService()
        if not service:
            return
        s = win32service.OpenService(
            self.scm, service[1], win32service.SERVICE_ALL_ACCESS
        )
        if StartupDlg(service[0], s).DoModal() == win32con.IDOK:
            self.ReloadData()

    def GetResource(self):
        style = (
            win32con.WS_POPUP
            | win32con.DS_SETFONT
            | win32con.WS_SYSMENU
            | win32con.WS_CAPTION
            | win32con.WS_VISIBLE
            | win32con.DS_MODALFRAME
        )
        exstyle = None
        t = [
            ["Services", (16, 16, 333, 157), style, exstyle, (8, "MS Shell Dlg")],
        ]
        t.append(
            [
                130,
                "Ser&vice",
                -1,
                (6, 6, 70, 8),
                win32con.WS_VISIBLE | win32con.WS_CHILD | win32con.SS_LEFT,
            ]
        )
        t.append(
            [
                130,
                "Status",
                -1,
                (164, 6, 42, 8),
                win32con.WS_VISIBLE | win32con.WS_CHILD | win32con.SS_LEFT,
            ]
        )
        t.append(
            [
                130,
                "Startup",
                -1,
                (206, 6, 50, 8),
                win32con.WS_VISIBLE | win32con.WS_CHILD | win32con.SS_LEFT,
            ]
        )
        t.append(
            [
                131,
                "",
                self.IDC_LIST,
                (6, 16, 255, 106),
                win32con.LBS_USETABSTOPS
                | win32con.LBS_SORT
                | win32con.LBS_NOINTEGRALHEIGHT
                | win32con.WS_BORDER
                | win32con.WS_CHILD
                | win32con.WS_VISIBLE
                | win32con.WS_TABSTOP
                | win32con.LBS_NOTIFY
                | win32con.WS_VSCROLL,
            ]
        )
        t.append(
            [
                128,
                "Close",
                win32con.IDOK,
                (267, 6, 60, 14),
                win32con.WS_VISIBLE
                | win32con.WS_CHILD
                | win32con.WS_GROUP
                | win32con.WS_TABSTOP
                | win32con.BS_DEFPUSHBUTTON,
            ]
        )
        t.append(
            [
                128,
                "&Start",
                self.IDC_START,
                (267, 27, 60, 14),
                win32con.WS_VISIBLE
                | win32con.WS_CHILD
                | win32con.WS_TABSTOP
                | win32con.BS_PUSHBUTTON,
            ]
        )
        t.append(
            [
                128,
                "S&top",
                self.IDC_STOP,
                (267, 44, 60, 14),
                win32con.WS_VISIBLE
                | win32con.WS_CHILD
                | win32con.WS_TABSTOP
                | win32con.BS_PUSHBUTTON,
            ]
        )
        t.append(
            [
                128,
                "&Pause",
                self.IDC_PAUSE,
                (267, 61, 60, 14),
                win32con.WS_VISIBLE
                | win32con.WS_CHILD
                | win32con.WS_TABSTOP
                | win32con.BS_PUSHBUTTON,
            ]
        )
        t.append(
            [
                128,
                "&Continue",
                self.IDC_CONTINUE,
                (267, 78, 60, 14),
                win32con.WS_VISIBLE
                | win32con.WS_CHILD
                | win32con.WS_TABSTOP
                | win32con.BS_PUSHBUTTON,
            ]
        )
        t.append(
            [
                128,
                "Sta&rtup...",
                self.IDC_STARTUP,
                (267, 99, 60, 14),
                win32con.WS_VISIBLE
                | win32con.WS_CHILD
                | win32con.WS_TABSTOP
                | win32con.BS_PUSHBUTTON,
            ]
        )
        t.append(
            [
                128,
                "H&W Profiles...",
                self.IDC_PROFILES,
                (267, 116, 60, 14),
                win32con.WS_VISIBLE
                | win32con.WS_CHILD
                | win32con.WS_TABSTOP
                | win32con.BS_PUSHBUTTON,
            ]
        )
        t.append(
            [
                128,
                "&Help",
                win32con.IDHELP,
                (267, 137, 60, 14),
                win32con.WS_VISIBLE
                | win32con.WS_CHILD
                | win32con.WS_TABSTOP
                | win32con.BS_PUSHBUTTON,
            ]
        )
        t.append(
            [
                130,
                "St&artup Parameters:",
                -1,
                (6, 128, 70, 8),
                win32con.WS_VISIBLE | win32con.WS_CHILD | win32con.SS_LEFT,
            ]
        )
        t.append(
            [
                129,
                "",
                self.IDC_PARAMS,
                (6, 139, 247, 12),
                win32con.WS_VISIBLE
                | win32con.WS_CHILD
                | win32con.WS_GROUP
                | win32con.WS_BORDER
                | win32con.ES_AUTOHSCROLL,
            ]
        )
        return t


if __name__ == "__main__":
    import sys

    machine = ""
    if len(sys.argv) > 1:
        machine = sys.argv[1]
    ServiceDlg(machine).DoModal()

```


---

## win32/scripts/VersionStamp/BrandProject.py

```python
# BrandProject.py
#
# Brand a VSS project with a "build number", then optionally
# stamp DLL/EXE files with version information.

import getopt
import os
import sys

import bulkstamp
import vssutil
import win32api


def BrandProject(
    vssProjectName,
    descFile,
    stampPath,
    filesToSubstitute,
    buildDesc=None,
    auto=0,
    bRebrand=0,
):
    # vssProjectName -- The name of the VSS project to brand.
    # descFile -- A test file containing descriptions of the files in the release.
    # stampPath -- The full path to where the files referenced in descFile can be found.
    path = win32api.GetFullPathName(stampPath)

    build = vssutil.MakeNewBuildNo(vssProjectName, buildDesc, auto, bRebrand)
    if build is None:
        print("Cancelled")
        return

    bulkstamp.scan(build, stampPath, descFile)
    for infile, outfile in filesToSubstitute:
        vssutil.SubstituteVSSInFile(vssProjectName, infile, outfile)
    return 1


def usage(msg):
    print(msg)
    print(
        f"""\
{os.path.basename(sys.argv[0])} Usage:
{os.path.basename(sys.argv[0])} [options] vssProject descFile stampPath

Automatically brand a VSS project with an automatically incremented
build number, and stamp DLL/EXE files with the build number.

Checks that no files are checked out in the project, and finds the last
build number, and suggests the next number.

Options:
-a     - Auto increment the build number, and brand (otherwise prompt
         for the build number after looking for the previous)
-r     - Restamp the files with the existing build number.
-d     - A description for the VSS Label.
-f infile=outfile - Substitute special VSS labels in the specified text
                    file with the text extracted from VSS.
"""
    )
    sys.exit(1)


if __name__ == "__main__":
    import getopt

    try:
        opts, args = getopt.getopt(sys.argv[1:], "af:d:r")
    except getopt.GetoptError as msg:
        usage(msg)
    bAuto = bRebrand = 0
    stampFiles = []
    desc = None
    for opt, val in opts:
        if opt == "-a":
            bAuto = 1
        if opt == "-f":
            infile, outfile = val.split("=", 2)
            stampFiles.append((infile, outfile))
        if opt == "-d":
            desc = val
        if opt == "-r":
            bRebrand = 1
    if len(args) < 3:
        usage("You must specify the required arguments")
    vssProjectName = "$\\" + args[0]
    descFile = args[1]
    if not os.path.exists(descFile):
        usage(f"The description file '{descFile}' can not be found")
    path = args[2]
    if not os.path.isdir(path):
        usage(f"The path to the files to stamp '{path}' does not exist")

    BrandProject(vssProjectName, descFile, path, stampFiles, desc, bAuto, bRebrand)

```


---

## win32/scripts/VersionStamp/bulkstamp.py

```python
#
# bulkstamp.py:
#    Stamp versions on all files that can be found in a given tree.
#
# USAGE: python bulkstamp.py <version> <root directory> <descriptions>
#
# Example: python bulkstamp.py 103 ..\win32\Build\ desc.txt
#
# <version> corresponds to the build number. It will be concatenated with
# the major and minor version numbers found in the description file.
#
# Description information is pulled from an input text file with lines of
# the form:
#
#    <basename> <white space> <description>
#
# For example:
#
#    PyWinTypes.dll Common types for Python on Win32
#    etc
#
# The product's name, major, and minor versions are specified as:
#
#    name <white space> <value>
#    major <white space> <value>
#    minor <white space> <value>
#
# The tags are case-sensitive.
#
# Any line beginning with "#" will be ignored. Empty lines are okay.
#

import fnmatch
import os
import sys
from collections.abc import Iterable, Mapping
from optparse import Values

try:
    import win32verstamp
except ModuleNotFoundError:
    # If run with pywin32 not already installed
    sys.path.append(os.path.abspath(__file__ + "/../../../Lib"))
    import win32verstamp

g_patterns = [
    "*.dll",
    "*.pyd",
    "*.exe",
    "*.ocx",
]


def walk(
    vars: Mapping[str, str], debug, descriptions, dirname, names: Iterable[str]
) -> int:
    """Returns the number of stamped files."""
    numStamped = 0
    for name in names:
        for pat in g_patterns:
            if fnmatch.fnmatch(name, pat):
                # Handle the "_d" thing.
                pathname = os.path.join(dirname, name)
                base, ext = os.path.splitext(name)
                name = base.removesuffix("_d") + ext
                is_dll = ext.lower() != ".exe"
                if os.path.normcase(name) in descriptions:
                    description = descriptions[os.path.normcase(name)]
                    try:
                        options = Values(
                            {**vars, "description": description, "dll": is_dll}
                        )
                        win32verstamp.stamp(pathname, options)
                        numStamped += 1
                    except OSError as exc:
                        print(
                            "Could not stamp",
                            pathname,
                            "Error",
                            exc.winerror,
                            "-",
                            exc.strerror,
                        )
                else:
                    print("WARNING: description not provided for:", name)
                    # skip branding this - assume already branded or handled elsewhere
    return numStamped


# print("Stamped", pathname)


def load_descriptions(fname, vars):
    retvars: dict[str, str] = {}
    descriptions = {}

    lines = open(fname, "r").readlines()

    for i in range(len(lines)):
        line = lines[i].strip()
        if line != "" and line[0] != "#":
            idx1 = line.find(" ")
            idx2 = line.find("\t")
            if idx1 == -1 or idx2 < idx1:
                idx1 = idx2
            if idx1 == -1:
                print("ERROR: bad syntax in description file at line %d." % (i + 1))
                sys.exit(1)

            key = line[:idx1]
            val = line[idx1:].strip()
            if key in vars:
                retvars[key] = val
            else:
                descriptions[key] = val

    if "product" not in retvars:
        print("ERROR: description file is missing the product name.")
        sys.exit(1)
    if "major" not in retvars:
        print("ERROR: description file is missing the major version number.")
        sys.exit(1)
    if "minor" not in retvars:
        print("ERROR: description file is missing the minor version number.")
        sys.exit(1)

    return retvars, descriptions


def scan(build, root: str, desc, **custom_vars):
    try:
        build = int(build)
    except ValueError:
        print("ERROR: build number is not a number: %s" % build)
        sys.exit(1)

    debug = 0  ### maybe fix this one day

    varList = ["major", "minor", "sub", "company", "copyright", "trademarks", "product"]

    vars, descriptions = load_descriptions(desc, varList)
    vars["build"] = build
    vars.update(custom_vars)

    numStamped = 0
    for directory, dirnames, filenames in os.walk(root):
        numStamped += walk(vars, debug, descriptions, directory, filenames)

    print(f"Stamped {numStamped} files.")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("ERROR: incorrect invocation. See script's header comments.")
        sys.exit(1)

    scan(*sys.argv[1:])

```


---

## win32/scripts/VersionStamp/vssutil.py

```python
import time
import traceback

import pythoncom
import win32com.client
import win32com.client.gencache
import win32con

constants = win32com.client.constants

win32com.client.gencache.EnsureModule("{783CD4E0-9D54-11CF-B8EE-00608CC9A71F}", 0, 5, 0)


def GetSS():
    ss = win32com.client.Dispatch("SourceSafe")
    # SS seems a bit weird.  It defaults the arguments as empty strings, but
    # then complains when they are used - so we pass "Missing"
    ss.Open(pythoncom.Missing, pythoncom.Missing, pythoncom.Missing)
    return ss


def test(projectName):
    ss = GetSS()
    project = ss.VSSItem(projectName)

    for item in project.GetVersions(constants.VSSFLAG_RECURSYES):
        print(item.VSSItem.Name, item.VersionNumber, item.Action)

    # item=i.Versions[0].VSSItem
    # for h in i.Versions:
    #     print("h.Comment", h.Action, h.VSSItem.Name)


def SubstituteInString(inString, evalEnv):
    substChar = "$"
    fields = inString.split(substChar)
    newFields = []
    for i in range(len(fields)):
        didSubst = 0
        strVal = fields[i]
        if i % 2 != 0:
            try:
                strVal = eval(strVal, evalEnv[0], evalEnv[1])
                newFields.append(strVal)
                didSubst = 1
            except:
                traceback.print_exc()
                print("Could not substitute", strVal)
        if not didSubst:
            newFields.append(strVal)
    return "".join(map(str, newFields))


def SubstituteInFile(inName, outName, evalEnv):
    inFile = open(inName, "r")
    try:
        outFile = open(outName, "w")
        try:
            while 1:
                line = inFile.read()
                if not line:
                    break
                outFile.write(SubstituteInString(line, evalEnv))
        finally:
            outFile.close()
    finally:
        inFile.close()


def VssLog(project, linePrefix="", noLabels=5, maxItems=150):
    lines = []
    num = 0
    labelNum = 0
    for i in project.GetVersions(constants.VSSFLAG_RECURSYES):
        num += 1
        if num > maxItems:
            break
        commentDesc = itemDesc = ""
        if i.Action[:5] == "Added":
            continue
        if len(i.Label):
            labelNum += 1
            itemDesc = i.Action
        else:
            itemDesc = i.VSSItem.Name
            if str(itemDesc[-4:]) == ".dsp":
                continue
        if i.Comment:
            commentDesc = f"\n{linePrefix}\t{i.Comment}"
        lines.append(
            "{}{}\t{}{}".format(
                linePrefix,
                time.asctime(time.localtime(int(i.Date))),
                itemDesc,
                commentDesc,
            )
        )
        if labelNum > noLabels:
            break
    return "\n".join(lines)


def SubstituteVSSInFile(projectName, inName, outName):
    import win32api

    if win32api.GetFullPathName(inName) == win32api.GetFullPathName(outName):
        raise RuntimeError("The input and output filenames can not be the same")
    sourceSafe = GetSS()
    project = sourceSafe.VSSItem(projectName)
    # Find the last label
    label = None
    for version in project.Versions:
        if version.Label:
            break
    else:
        print("Couldn't find a label in the sourcesafe project!")
        return
    # Setup some local helpers for the conversion strings.
    vss_label = version.Label
    vss_date = time.asctime(time.localtime(int(version.Date)))
    now = time.asctime(time.localtime(time.time()))
    SubstituteInFile(inName, outName, (locals(), globals()))


def CountCheckouts(item):
    num = 0
    if item.Type == constants.VSSITEM_PROJECT:
        for sub in item.Items:
            num += CountCheckouts(sub)
    else:
        if item.IsCheckedOut:
            num += 1
    return num


def GetLastBuildNo(project):
    i = GetSS().VSSItem(project)
    # Find the last label
    lab = None
    for version in i.Versions:
        lab = str(version.Label)
        if lab:
            return lab
    return None


def MakeNewBuildNo(project, buildDesc=None, auto=0, bRebrand=0):
    if buildDesc is None:
        buildDesc = "Created by Python"
    ss = GetSS()
    i = ss.VSSItem(project)
    num = CountCheckouts(i)
    if num > 0:
        msg = (
            "This project has %d items checked out\r\n\r\nDo you still want to continue?"
            % num
        )
        import win32ui

        if win32ui.MessageBox(msg, project, win32con.MB_YESNO) != win32con.IDYES:
            return

    oldBuild = buildNo = GetLastBuildNo(project)
    if buildNo is None:
        buildNo = "1"
        oldBuild = "<None>"
    else:
        try:
            buildNo = int(buildNo)
            if not bRebrand:
                buildNo += 1
            buildNo = str(buildNo)
        except ValueError as error:
            raise ValueError(
                f"The previous label could not be incremented: {oldBuild}"
            ) from error

    if not auto:
        from pywin.mfc import dialog

        buildNo = dialog.GetSimpleInput(
            "Enter new build number", buildNo, f"{project} - Prev: {oldBuild}"
        )
        if buildNo is None:
            return
    i.Label(buildNo, f"Build {buildNo}: {buildDesc}")
    if auto:
        print(f"Branded project {project} with label {buildNo}")
    return buildNo


if __name__ == "__main__":
    # 	UpdateWiseExeName("PyWiseTest.wse", "PyWiseTest-10.exe")

    # 	MakeVersion()
    # 	test(tp)
    # 	MakeNewBuildNo(tp)
    tp = "\\Python\\Python Win32 Extensions"
    SubstituteVSSInFile(
        tp, "d:\\src\\pythonex\\win32\\win32.txt", "d:\\temp\\win32.txt"
    )

```


---

## win32/scripts/backupEventLog.py

```python
# Generate a base file name
import os
import time

import win32api
import win32evtlog


def BackupClearLog(logType):
    datePrefix = time.strftime("%Y%m%d", time.localtime(time.time()))
    retry = 0
    while True:  # file exists
        index = "" if retry == 0 else f"-{retry}"
        fname = os.path.join(
            win32api.GetTempPath(),
            f"{datePrefix}{index}-{logType}.evt",
        )
        if not os.path.exists(fname):
            break
        retry += 1
    # OK - have unique file name.
    try:
        hlog = win32evtlog.OpenEventLog(None, logType)
    except win32evtlog.error as details:
        print("Could not open the event log", details)
        return
    try:
        if win32evtlog.GetNumberOfEventLogRecords(hlog) == 0:
            print("No records in event log %s - not backed up" % logType)
            return
        win32evtlog.ClearEventLog(hlog, fname)
        print(f"Backed up {logType} log to {fname}")
    finally:
        win32evtlog.CloseEventLog(hlog)


if __name__ == "__main__":
    BackupClearLog("Application")
    BackupClearLog("System")
    BackupClearLog("Security")

```


---

## win32/scripts/h2py.py

```python
#! /usr/bin/env python3
"""
Vendored from https://github.com/python/cpython/blob/3.8/Tools/scripts/h2py.py

Changes since vendored version:
- Minimal changes to satisfy our checkers.
- Rename `p_hex` to `p_signed_hex` and improve to include lowercase l
- Fixed `pytify` to remove leftover L after numbers and actually compute negative hexadecimal constants
- Added `p_int_cast` and `p_literal_constant`

---

Read #define's and translate to Python code.
Handle #include statements.
Handle #define macros with one argument.
Anything that isn't recognized or doesn't translate into valid
Python is ignored.

Without filename arguments, acts as a filter.
If one or more filenames are given, output is written to corresponding
filenames in the local directory, translated to all uppercase, with
the extension replaced by ".py".

By passing one or more options of the form "-i regular_expression"
you can specify additional strings to be ignored.  This is useful
e.g. to ignore casts to u_long: simply specify "-i '(u_long)'".
"""

# XXX To do:
# - turn trailing C comments into Python comments
# - turn C Boolean operators "&& || !" into Python "and or not"
# - what to do about #if(def)?
# - what to do about macros with multiple parameters?
from __future__ import annotations

import ctypes
import getopt
import os
import re
import sys

p_define = re.compile(r"^[\t ]*#[\t ]*define[\t ]+([a-zA-Z0-9_]+)[\t ]+")

p_macro = re.compile(
    r"^[\t ]*#[\t ]*define[\t ]+" r"([a-zA-Z0-9_]+)\(([_a-zA-Z][_a-zA-Z0-9]*)\)[\t ]+"
)

p_include = re.compile(r"^[\t ]*#[\t ]*include[\t ]+<([^>\n]+)>")

p_comment = re.compile(r"/\*([^*]+|\*+[^/])*(\*+/)?")
p_cpp_comment = re.compile("//.*")
# Maybe we want these to cause integer truncation instead?
p_int_cast = re.compile(r"\((DWORD|HRESULT|SCODE|LONG|HWND|HANDLE|int|HBITMAP)\)")

ignores = [p_comment, p_cpp_comment, p_int_cast]

p_char = re.compile(r"'(\\.[^\\]*|[^\\])'")
p_signed_hex = re.compile(r"0x([0-9a-fA-F]+)[lL]?")
p_literal_constant = re.compile(r"((0x[0-9a-fA-F]+?)|([0-9]+?))[uUlL]")

filedict: dict[str, None] = {}
importable: dict[str, str] = {}

try:
    searchdirs = os.environ["include"].split(";")
except KeyError:
    try:
        searchdirs = os.environ["INCLUDE"].split(";")
    except KeyError:
        searchdirs = ["/usr/include"]
        try:
            searchdirs.insert(0, os.path.join("/usr/include", os.environ["MULTIARCH"]))
        except KeyError:
            pass


def main():
    global filedict
    opts, args = getopt.getopt(sys.argv[1:], "i:")
    for o, a in opts:
        if o == "-i":
            ignores.append(re.compile(a))
    if not args:
        args = ["-"]
    for filename in args:
        if filename == "-":
            sys.stdout.write("# Generated by h2py from stdin\n")
            process(sys.stdin, sys.stdout)
        else:
            with open(filename) as fp:
                outfile = os.path.basename(filename)
                i = outfile.rfind(".")
                if i > 0:
                    outfile = outfile[:i]
                modname = outfile.upper()
                outfile = modname + ".py"
                with open(outfile, "w") as outfp:
                    outfp.write("# Generated by h2py from %s\n" % filename)
                    filedict = {}
                    for dir in searchdirs:
                        if filename[: len(dir)] == dir:
                            filedict[filename[len(dir) + 1 :]] = None  # no '/' trailing
                            importable[filename[len(dir) + 1 :]] = modname
                            break
                    process(fp, outfp)


def pytify(body):
    # replace ignored patterns by spaces
    for p in ignores:
        body = p.sub(" ", body)
    # replace char literals by ord(...)
    body = p_char.sub("ord('\\1')", body)
    # Compute negative hexadecimal constants
    start = 0
    while 1:
        m = p_signed_hex.search(body, start)
        if not m:
            break
        s, e = m.span()
        val = ctypes.c_int32(int(body[slice(*m.span(1))], 16)).value
        if val < 0:
            body = body[:s] + "(" + str(val) + ")" + body[e:]
        start = s + 1
    # remove literal constant indicator (u U l L)
    body = p_literal_constant.sub("\\1", body)
    return body


def process(fp, outfp, env={}):
    lineno = 0
    while 1:
        line = fp.readline()
        if not line:
            break
        lineno = lineno + 1
        match = p_define.match(line)
        if match:
            # gobble up continuation lines
            while line[-2:] == "\\\n":
                nextline = fp.readline()
                if not nextline:
                    break
                lineno = lineno + 1
                line = line + nextline
            name = match.group(1)
            body = line[match.end() :]
            body = pytify(body)
            ok = 0
            stmt = "%s = %s\n" % (name, body.strip())
            try:
                exec(stmt, env)
            except:
                sys.stderr.write("Skipping: %s" % stmt)
            else:
                outfp.write(stmt)
        match = p_macro.match(line)
        if match:
            macro, arg = match.group(1, 2)
            body = line[match.end() :]
            body = pytify(body)
            stmt = "def %s(%s): return %s\n" % (macro, arg, body)
            try:
                exec(stmt, env)
            except:
                sys.stderr.write("Skipping: %s" % stmt)
            else:
                outfp.write(stmt)
        match = p_include.match(line)
        if match:
            regs = match.regs
            a, b = regs[1]
            filename = line[a:b]
            if filename in importable:
                outfp.write("from %s import *\n" % importable[filename])
            elif filename not in filedict:
                filedict[filename] = None
                inclfp = None
                for dir in searchdirs:
                    try:
                        inclfp = open(dir + "/" + filename)
                        break
                    except OSError:
                        pass
                if inclfp:
                    with inclfp:
                        outfp.write("\n# Included from %s\n" % filename)
                        process(inclfp, outfp, env)
                else:
                    sys.stderr.write("Warning - could not find file %s\n" % filename)


if __name__ == "__main__":
    main()

```


---

## win32/scripts/killProcName.py

```python
# Kills a process by process name
#
# Uses the Performance Data Helper to locate the PID, then kills it.
# Will only kill the process if there is only one process of that name
# (eg, attempting to kill "Python.exe" will only work if there is only
# one Python.exe running.  (Note that the current process does not
# count - ie, if Python.exe is hosting this script, you can still kill
# another Python.exe (as long as there is only one other Python.exe)

# Really just a demo for the win32pdh(util) module, which allows you
# to get all sorts of information about a running process and many
# other aspects of your system.

import sys

import win32api
import win32con
import win32pdhutil


def killProcName(procname):
    # Change suggested by Dan Knierim, who found that this performed a
    # "refresh", allowing us to kill processes created since this was run
    # for the first time.
    try:
        win32pdhutil.GetPerformanceAttributes("Process", "ID Process", procname)
    except:
        pass

    pids = win32pdhutil.FindPerformanceAttributesByName(procname)

    # If _my_ pid in there, remove it!
    try:
        pids.remove(win32api.GetCurrentProcessId())
    except ValueError:
        pass

    if len(pids) == 0:
        result = "Can't find %s" % procname
    elif len(pids) > 1:
        result = f"Found too many {procname}'s - pids=`{pids}`"
    else:
        handle = win32api.OpenProcess(win32con.PROCESS_TERMINATE, 0, pids[0])
        win32api.TerminateProcess(handle, 0)
        win32api.CloseHandle(handle)
        result = ""

    return result


if __name__ == "__main__":
    if len(sys.argv) > 1:
        for procname in sys.argv[1:]:
            result = killProcName(procname)
            if result:
                print(result)
                print("Dumping all processes...")
                win32pdhutil.ShowAllProcesses()
            else:
                print("Killed %s" % procname)
    else:
        print("Usage: killProcName.py procname ...")

```


---

## win32/scripts/pywin32_postinstall.py

```python
# postinstall script for pywin32
#
# copies pywintypesXX.dll and pythoncomXX.dll into the system directory,
# and creates a pth file
import argparse
import glob
import os
import shutil
import sys
import sysconfig
import tempfile
import winreg

tee_f = open(
    os.path.join(
        tempfile.gettempdir(),  # Send output somewhere so it can be found if necessary...
        "pywin32_postinstall.log",
    ),
    "w",
)


class Tee:
    def __init__(self, file):
        self.f = file

    def write(self, what):
        if self.f is not None:
            try:
                self.f.write(what.replace("\n", "\r\n"))
            except OSError:
                pass
        tee_f.write(what)

    def flush(self):
        if self.f is not None:
            try:
                self.f.flush()
            except OSError:
                pass
        tee_f.flush()


sys.stderr = Tee(sys.stderr)
sys.stdout = Tee(sys.stdout)

com_modules = [
    # module_name,                      class_names
    ("win32com.servers.interp", "Interpreter"),
    ("win32com.servers.dictionary", "DictionaryPolicy"),
    ("win32com.axscript.client.pyscript", "PyScript"),
]

# Is this a 'silent' install - ie, avoid all dialogs.
# Different than 'verbose'
silent = 0

# Verbosity of output messages.
verbose = 1

root_key_name = "Software\\Python\\PythonCore\\" + sys.winver


def get_root_hkey():
    try:
        winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE, root_key_name, 0, winreg.KEY_CREATE_SUB_KEY
        )
        return winreg.HKEY_LOCAL_MACHINE
    except OSError:
        # Either not exist, or no permissions to create subkey means
        # must be HKCU
        return winreg.HKEY_CURRENT_USER


# Create a function with the same signature as create_shortcut
# previously provided by bdist_wininst
def create_shortcut(
    path, description, filename, arguments="", workdir="", iconpath="", iconindex=0
):
    import pythoncom
    from win32com.shell import shell

    ilink = pythoncom.CoCreateInstance(
        shell.CLSID_ShellLink,
        None,
        pythoncom.CLSCTX_INPROC_SERVER,
        shell.IID_IShellLink,
    )
    ilink.SetPath(path)
    ilink.SetDescription(description)
    if arguments:
        ilink.SetArguments(arguments)
    if workdir:
        ilink.SetWorkingDirectory(workdir)
    if iconpath or iconindex:
        ilink.SetIconLocation(iconpath, iconindex)
    # now save it.
    ipf = ilink.QueryInterface(pythoncom.IID_IPersistFile)
    ipf.Save(filename, 0)


# Support the same list of "path names" as bdist_wininst used to
def get_special_folder_path(path_name):
    from win32com.shell import shell, shellcon

    for maybe in """
        CSIDL_COMMON_STARTMENU CSIDL_STARTMENU CSIDL_COMMON_APPDATA
        CSIDL_LOCAL_APPDATA CSIDL_APPDATA CSIDL_COMMON_DESKTOPDIRECTORY
        CSIDL_DESKTOPDIRECTORY CSIDL_COMMON_STARTUP CSIDL_STARTUP
        CSIDL_COMMON_PROGRAMS CSIDL_PROGRAMS CSIDL_PROGRAM_FILES_COMMON
        CSIDL_PROGRAM_FILES CSIDL_FONTS""".split():
        if maybe == path_name:
            csidl = getattr(shellcon, maybe)
            return shell.SHGetSpecialFolderPath(0, csidl, False)
    raise ValueError(f"{path_name} is an unknown path ID")


def CopyTo(desc, src, dest):
    import win32api
    import win32con

    while 1:
        try:
            win32api.CopyFile(src, dest, 0)
            return
        except win32api.error as details:
            if details.winerror == 5:  # access denied - user not admin.
                raise
            if silent:
                # Running silent mode - just re-raise the error.
                raise
            full_desc = (
                f"Error {desc}\n\n"
                "If you have any Python applications running, "
                f"please close them now\nand select 'Retry'\n\n{details.strerror}"
            )
            rc = win32api.MessageBox(
                0, full_desc, "Installation Error", win32con.MB_ABORTRETRYIGNORE
            )
            if rc == win32con.IDABORT:
                raise
            elif rc == win32con.IDIGNORE:
                return
            # else retry - around we go again.


# We need to import win32api to determine the Windows system directory,
# so we can copy our system files there - but importing win32api will
# load the pywintypes.dll already in the system directory preventing us
# from updating them!
# So, we pull the same trick pywintypes.py does, but it loads from
# our pywintypes_system32 directory.
def LoadSystemModule(lib_dir, modname):
    # See if this is a debug build.
    import importlib.machinery
    import importlib.util

    suffix = "_d" if "_d.pyd" in importlib.machinery.EXTENSION_SUFFIXES else ""
    filename = "%s%d%d%s.dll" % (
        modname,
        sys.version_info.major,
        sys.version_info.minor,
        suffix,
    )
    filename = os.path.join(lib_dir, "pywin32_system32", filename)
    loader = importlib.machinery.ExtensionFileLoader(modname, filename)
    spec = importlib.machinery.ModuleSpec(name=modname, loader=loader, origin=filename)
    mod = importlib.util.module_from_spec(spec)
    loader.exec_module(mod)


def SetPyKeyVal(key_name, value_name, value):
    root_hkey = get_root_hkey()
    root_key = winreg.OpenKey(root_hkey, root_key_name)
    try:
        my_key = winreg.CreateKey(root_key, key_name)
        try:
            winreg.SetValueEx(my_key, value_name, 0, winreg.REG_SZ, value)
            if verbose:
                print(f"-> {root_key_name}\\{key_name}[{value_name}]={value!r}")
        finally:
            my_key.Close()
    finally:
        root_key.Close()


def UnsetPyKeyVal(key_name, value_name, delete_key=False):
    root_hkey = get_root_hkey()
    root_key = winreg.OpenKey(root_hkey, root_key_name)
    try:
        my_key = winreg.OpenKey(root_key, key_name, 0, winreg.KEY_SET_VALUE)
        try:
            winreg.DeleteValue(my_key, value_name)
            if verbose:
                print(f"-> DELETE {root_key_name}\\{key_name}[{value_name}]")
        finally:
            my_key.Close()
        if delete_key:
            winreg.DeleteKey(root_key, key_name)
            if verbose:
                print(f"-> DELETE {root_key_name}\\{key_name}")
    except OSError as why:
        winerror = getattr(why, "winerror", why.errno)
        if winerror != 2:  # file not found
            raise
    finally:
        root_key.Close()


def RegisterCOMObjects(register=True):
    import win32com.server.register

    if register:
        func = win32com.server.register.RegisterClasses
    else:
        func = win32com.server.register.UnregisterClasses
    flags = {}
    if not verbose:
        flags["quiet"] = 1
    for module, klass_name in com_modules:
        __import__(module)
        mod = sys.modules[module]
        flags["finalize_register"] = getattr(mod, "DllRegisterServer", None)
        flags["finalize_unregister"] = getattr(mod, "DllUnregisterServer", None)
        klass = getattr(mod, klass_name)
        func(klass, **flags)


def RegisterHelpFile(register=True, lib_dir=None):
    if lib_dir is None:
        lib_dir = sysconfig.get_paths()["platlib"]
    if register:
        # Register the .chm help file.
        chm_file = os.path.join(lib_dir, "PyWin32.chm")
        if os.path.isfile(chm_file):
            # This isn't recursive, so if 'Help' doesn't exist, we croak
            SetPyKeyVal("Help", None, None)
            SetPyKeyVal("Help\\Pythonwin Reference", None, chm_file)
            return chm_file
        else:
            print("NOTE: PyWin32.chm can not be located, so has not been registered")
    else:
        UnsetPyKeyVal("Help\\Pythonwin Reference", None, delete_key=True)
    return None


def RegisterPythonwin(register=True, lib_dir=None):
    """Add (or remove) Pythonwin to context menu for python scripts.
    ??? Should probably also add Edit command for pys files also.
    Also need to remove these keys on uninstall, but there's no function
    to add registry entries to uninstall log ???
    """
    import os

    if lib_dir is None:
        lib_dir = sysconfig.get_paths()["platlib"]
    classes_root = get_root_hkey()
    ## Installer executable doesn't seem to pass anything to postinstall script indicating if it's a debug build
    pythonwin_exe = os.path.join(lib_dir, "Pythonwin", "Pythonwin.exe")
    pythonwin_edit_command = pythonwin_exe + ' -edit "%1"'

    keys_vals = [
        (
            "Software\\Microsoft\\Windows\\CurrentVersion\\App Paths\\Pythonwin.exe",
            "",
            pythonwin_exe,
        ),
        (
            "Software\\Classes\\Python.File\\shell\\Edit with Pythonwin",
            "command",
            pythonwin_edit_command,
        ),
        (
            "Software\\Classes\\Python.NoConFile\\shell\\Edit with Pythonwin",
            "command",
            pythonwin_edit_command,
        ),
    ]

    try:
        if register:
            for key, sub_key, val in keys_vals:
                ## Since winreg only uses the character Api functions, this can fail if Python
                ##  is installed to a path containing non-ascii characters
                hkey = winreg.CreateKey(classes_root, key)
                if sub_key:
                    hkey = winreg.CreateKey(hkey, sub_key)
                winreg.SetValueEx(hkey, None, 0, winreg.REG_SZ, val)
                hkey.Close()
        else:
            for key, sub_key, val in keys_vals:
                try:
                    if sub_key:
                        hkey = winreg.OpenKey(classes_root, key)
                        winreg.DeleteKey(hkey, sub_key)
                        hkey.Close()
                    winreg.DeleteKey(classes_root, key)
                except OSError as why:
                    winerror = getattr(why, "winerror", why.errno)
                    if winerror != 2:  # file not found
                        raise
    finally:
        # tell windows about the change
        from win32com.shell import shell, shellcon

        shell.SHChangeNotify(
            shellcon.SHCNE_ASSOCCHANGED, shellcon.SHCNF_IDLIST, None, None
        )


def get_shortcuts_folder():
    if get_root_hkey() == winreg.HKEY_LOCAL_MACHINE:
        fldr = get_special_folder_path("CSIDL_COMMON_PROGRAMS")
    else:
        # non-admin install - always goes in this user's start menu.
        fldr = get_special_folder_path("CSIDL_PROGRAMS")

    try:
        install_group = winreg.QueryValue(
            get_root_hkey(), root_key_name + "\\InstallPath\\InstallGroup"
        )
    except OSError:
        install_group = "Python %d.%d" % (
            sys.version_info.major,
            sys.version_info.minor,
        )
    return os.path.join(fldr, install_group)


# Get the system directory, which may be the Wow64 directory if we are a 32bit
# python on a 64bit OS.
def get_system_dir():
    import win32api  # we assume this exists.

    try:
        import pythoncom
        import win32process
        from win32com.shell import shell, shellcon

        try:
            if win32process.IsWow64Process():
                return shell.SHGetSpecialFolderPath(0, shellcon.CSIDL_SYSTEMX86)
            return shell.SHGetSpecialFolderPath(0, shellcon.CSIDL_SYSTEM)
        except (pythoncom.com_error, win32process.error):
            return win32api.GetSystemDirectory()
    except ImportError:
        return win32api.GetSystemDirectory()


def fixup_dbi():
    # We used to have a dbi.pyd with our .pyd files, but now have a .py file.
    # If the user didn't uninstall, they will find the .pyd which will cause
    # problems - so handle that.
    import win32api
    import win32con

    pyd_name = os.path.join(os.path.dirname(win32api.__file__), "dbi.pyd")
    pyd_d_name = os.path.join(os.path.dirname(win32api.__file__), "dbi_d.pyd")
    py_name = os.path.join(os.path.dirname(win32con.__file__), "dbi.py")
    for this_pyd in (pyd_name, pyd_d_name):
        this_dest = this_pyd + ".old"
        if os.path.isfile(this_pyd) and os.path.isfile(py_name):
            try:
                if os.path.isfile(this_dest):
                    print(
                        f"Old dbi '{this_dest}' already exists - deleting '{this_pyd}'"
                    )
                    os.remove(this_pyd)
                else:
                    os.rename(this_pyd, this_dest)
                    print(f"renamed '{this_pyd}'->'{this_pyd}.old'")
            except OSError as exc:
                print(f"FAILED to rename '{this_pyd}': {exc}")


def install(lib_dir):
    import traceback

    # The .pth file is now installed as a regular file.
    # Create the .pth file in the site-packages dir, and use only relative paths
    # We used to write a .pth directly to sys.prefix - clobber it.
    if os.path.isfile(os.path.join(sys.prefix, "pywin32.pth")):
        os.unlink(os.path.join(sys.prefix, "pywin32.pth"))
    # The .pth may be new and therefore not loaded in this session.
    # Setup the paths just in case.
    for name in "win32 win32\\lib Pythonwin".split():
        sys.path.append(os.path.join(lib_dir, name))
    # It is possible people with old versions installed with still have
    # pywintypes and pythoncom registered.  We no longer need this, and stale
    # entries hurt us.
    for name in "pythoncom pywintypes".split():
        keyname = "Software\\Python\\PythonCore\\" + sys.winver + "\\Modules\\" + name
        for root in winreg.HKEY_LOCAL_MACHINE, winreg.HKEY_CURRENT_USER:
            try:
                winreg.DeleteKey(root, keyname + "\\Debug")
            except OSError:
                pass
            try:
                winreg.DeleteKey(root, keyname)
            except OSError:
                pass
    LoadSystemModule(lib_dir, "pywintypes")
    LoadSystemModule(lib_dir, "pythoncom")
    import win32api

    # and now we can get the system directory:
    files = glob.glob(os.path.join(lib_dir, "pywin32_system32\\*.*"))
    if not files:
        raise RuntimeError("No system files to copy!!")
    # Try the system32 directory first - if that fails due to "access denied",
    # it implies a non-admin user, and we use sys.prefix
    for dest_dir in [get_system_dir(), sys.prefix]:
        # and copy some files over there
        worked = 0
        try:
            for fname in files:
                base = os.path.basename(fname)
                dst = os.path.join(dest_dir, base)
                CopyTo("installing %s" % base, fname, dst)
                if verbose:
                    print(f"Copied {base} to {dst}")
                worked = 1
                # Nuke any other versions that may exist - having
                # duplicates causes major headaches.
                bad_dest_dirs = [
                    os.path.join(sys.prefix, "Library\\bin"),
                    os.path.join(sys.prefix, "Lib\\site-packages\\win32"),
                ]
                if dest_dir != sys.prefix:
                    bad_dest_dirs.append(sys.prefix)
                for bad_dest_dir in bad_dest_dirs:
                    bad_fname = os.path.join(bad_dest_dir, base)
                    if os.path.exists(bad_fname):
                        # let exceptions go here - delete must succeed
                        os.unlink(bad_fname)
            if worked:
                break
        except win32api.error as details:
            if details.winerror == 5:
                # access denied - user not admin - try sys.prefix dir,
                # but first check that a version doesn't already exist
                # in that place - otherwise that one will still get used!
                if os.path.exists(dst):
                    msg = (
                        "The file '%s' exists, but can not be replaced "
                        "due to insufficient permissions.  You must "
                        "reinstall this software as an Administrator" % dst
                    )
                    print(msg)
                    raise RuntimeError(msg)
                continue
            raise
    else:
        raise RuntimeError(
            "You don't have enough permissions to install the system files"
        )

    # Register our demo COM objects.
    try:
        try:
            RegisterCOMObjects()
        except win32api.error as details:
            if details.winerror != 5:  # ERROR_ACCESS_DENIED
                raise
            print("You do not have the permissions to install COM objects.")
            print("The sample COM objects were not registered.")
    except Exception:
        print("FAILED to register the Python COM objects")
        traceback.print_exc()

    # There may be no main Python key in HKCU if, eg, an admin installed
    # python itself.
    winreg.CreateKey(get_root_hkey(), root_key_name)

    chm_file = None
    try:
        chm_file = RegisterHelpFile(True, lib_dir)
    except Exception:
        print("Failed to register help file")
        traceback.print_exc()
    else:
        if verbose:
            print("Registered help file")

    # misc other fixups.
    fixup_dbi()

    # Register Pythonwin in context menu
    try:
        RegisterPythonwin(True, lib_dir)
    except Exception:
        print("Failed to register pythonwin as editor")
        traceback.print_exc()
    else:
        if verbose:
            print("Pythonwin has been registered in context menu")

    # Create the win32com\gen_py directory.
    make_dir = os.path.join(lib_dir, "win32com", "gen_py")
    if not os.path.isdir(make_dir):
        if verbose:
            print(f"Creating directory {make_dir}")
        os.mkdir(make_dir)

    try:
        # create shortcuts
        # CSIDL_COMMON_PROGRAMS only available works on NT/2000/XP, and
        # will fail there if the user has no admin rights.
        fldr = get_shortcuts_folder()
        # If the group doesn't exist, then we don't make shortcuts - its
        # possible that this isn't a "normal" install.
        if os.path.isdir(fldr):
            dst = os.path.join(fldr, "PythonWin.lnk")
            create_shortcut(
                os.path.join(lib_dir, "pythonwin", "Pythonwin.exe"),
                "The Pythonwin IDE",
                dst,
                "",
                sys.prefix,
            )
            if verbose:
                print("Shortcut for Pythonwin created")
            # And the docs.
            if chm_file:
                dst = os.path.join(fldr, "Python for Windows Documentation.lnk")
                doc = "Documentation for the PyWin32 extensions"
                create_shortcut(chm_file, doc, dst)
                if verbose:
                    print("Shortcut to documentation created")
        else:
            if verbose:
                print(f"Can't install shortcuts - {fldr!r} is not a folder")
    except Exception as details:
        print(details)

    # importing win32com.client ensures the gen_py dir created - not strictly
    # necessary to do now, but this makes the installation "complete"
    try:
        import win32com.client  # noqa
    except ImportError:
        # Don't let this error sound fatal
        pass
    print("The pywin32 extensions were successfully installed.")


def uninstall(lib_dir):
    # First ensure our system modules are loaded from pywin32_system, so
    # we can remove the ones we copied...
    LoadSystemModule(lib_dir, "pywintypes")
    LoadSystemModule(lib_dir, "pythoncom")

    try:
        RegisterCOMObjects(False)
    except Exception as why:
        print(f"Failed to unregister COM objects: {why}")

    try:
        RegisterHelpFile(False, lib_dir)
    except Exception as why:
        print(f"Failed to unregister help file: {why}")
    else:
        if verbose:
            print("Unregistered help file")

    try:
        RegisterPythonwin(False, lib_dir)
    except Exception as why:
        print(f"Failed to unregister Pythonwin: {why}")
    else:
        if verbose:
            print("Unregistered Pythonwin")

    try:
        # remove gen_py directory.
        gen_dir = os.path.join(lib_dir, "win32com", "gen_py")
        if os.path.isdir(gen_dir):
            shutil.rmtree(gen_dir)
            if verbose:
                print(f"Removed directory {gen_dir}")

        # Remove pythonwin compiled "config" files.
        pywin_dir = os.path.join(lib_dir, "Pythonwin", "pywin")
        for fname in glob.glob(os.path.join(pywin_dir, "*.cfc")):
            os.remove(fname)

        # The dbi.pyd.old files we may have created.
        try:
            os.remove(os.path.join(lib_dir, "win32", "dbi.pyd.old"))
        except OSError:
            pass
        try:
            os.remove(os.path.join(lib_dir, "win32", "dbi_d.pyd.old"))
        except OSError:
            pass

    except Exception as why:
        print(f"Failed to remove misc files: {why}")

    try:
        fldr = get_shortcuts_folder()
        for link in ("PythonWin.lnk", "Python for Windows Documentation.lnk"):
            fqlink = os.path.join(fldr, link)
            if os.path.isfile(fqlink):
                os.remove(fqlink)
                if verbose:
                    print(f"Removed {link}")
    except Exception as why:
        print(f"Failed to remove shortcuts: {why}")
    # Now remove the system32 files.
    files = glob.glob(os.path.join(lib_dir, "pywin32_system32\\*.*"))
    # Try the system32 directory first - if that fails due to "access denied",
    # it implies a non-admin user, and we use sys.prefix
    try:
        for dest_dir in [get_system_dir(), sys.prefix]:
            # and copy some files over there
            worked = 0
            for fname in files:
                base = os.path.basename(fname)
                dst = os.path.join(dest_dir, base)
                if os.path.isfile(dst):
                    try:
                        os.remove(dst)
                        worked = 1
                        if verbose:
                            print("Removed file %s" % (dst))
                    except Exception:
                        print(f"FAILED to remove {dst}")
            if worked:
                break
    except Exception as why:
        print(f"FAILED to remove system files: {why}")


# NOTE: This used to be run from inside the bdist_wininst created binary un/installer.
# From inside the binary installer this script HAD to NOT
# call sys.exit() or raise SystemExit, otherwise the installer would also terminate!
# Out of principle, we're still not using system exits.


def verify_destination(location: str) -> str:
    location = os.path.abspath(location)
    if not os.path.isdir(location):
        raise argparse.ArgumentTypeError(
            f'Path "{location}" is not an existing directory!'
        )
    return location


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="""A post-install script for the pywin32 extensions.

    * Typical usage:

    > python -m pywin32_postinstall -install

    * or (shorter but you don't have control over which python environment is used)

    > pywin32_postinstall -install

    You need to execute this script, with a '-install' parameter,
    to ensure the environment is setup correctly to install COM objects, services, etc.
    """,
    )
    parser.add_argument(
        "-install",
        default=False,
        action="store_true",
        help="Configure the Python environment correctly for pywin32.",
    )
    parser.add_argument(
        "-remove",
        default=False,
        action="store_true",
        help="Try and remove everything that was installed or copied.",
    )
    parser.add_argument(
        "-wait",
        type=int,
        help="Wait for the specified process to terminate before starting.",
    )
    parser.add_argument(
        "-silent",
        default=False,
        action="store_true",
        help='Don\'t display the "Abort/Retry/Ignore" dialog for files in use.',
    )
    parser.add_argument(
        "-quiet",
        default=False,
        action="store_true",
        help="Don't display progress messages.",
    )
    parser.add_argument(
        "-destination",
        default=sysconfig.get_paths()["platlib"],
        type=verify_destination,
        help="Location of the PyWin32 installation",
    )

    args = parser.parse_args()

    if not args.quiet:
        print(f"Parsed arguments are: {args}")

    if not args.install ^ args.remove:
        parser.error("You need to either choose to -install or -remove!")

    if args.wait is not None:
        try:
            os.waitpid(args.wait, 0)
        except OSError:
            # child already dead
            pass

    silent = args.silent
    verbose = not args.quiet

    if args.install:
        install(args.destination)

    if args.remove:
        uninstall(args.destination)


if __name__ == "__main__":
    main()

```


---

## win32/scripts/pywin32_testall.py

```python
"""A test runner for pywin32"""

import os
import site
import subprocess
import sys

# locate the dirs based on where this script is - it may be either in the
# source tree, or in an installed Python 'Scripts' tree.
project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
site_packages = [site.getusersitepackages()] + site.getsitepackages()

failures = []


# Run a test using subprocess and wait for the result.
# If we get an returncode != 0, we know that there was an error, but we don't
# abort immediately - we run as many tests as we can.
def run_test(script, cmdline_extras):
    dirname, scriptname = os.path.split(script)
    # some tests prefer to be run from their directory.
    cmd = [sys.executable, "-u", scriptname] + cmdline_extras
    print("--- Running '%s' ---" % script)
    sys.stdout.flush()
    result = subprocess.run(cmd, check=False, cwd=dirname)
    print(f"*** Test script '{script}' exited with {result.returncode}")
    sys.stdout.flush()
    if result.returncode:
        failures.append(script)


def find_and_run(possible_locations, extras):
    for maybe in possible_locations:
        if os.path.isfile(maybe):
            run_test(maybe, extras)
            break
    else:
        raise RuntimeError(
            "Failed to locate a test script in one of %s" % possible_locations
        )


def main():
    import argparse

    code_directories = [project_root] + site_packages

    parser = argparse.ArgumentParser(
        description="A script to trigger tests in all subprojects of PyWin32."
    )
    parser.add_argument(
        "-no-user-interaction",
        default=False,
        action="store_true",
        help="(This is now the default - use `-user-interaction` to include them)",
    )

    parser.add_argument(
        "-user-interaction",
        action="store_true",
        help="Include tests which require user interaction",
    )

    parser.add_argument(
        "-skip-adodbapi",
        default=False,
        action="store_true",
        help="Skip the adodbapi tests; useful for CI where there's no provider",
    )

    args, remains = parser.parse_known_args()

    # win32, win32ui / Pythonwin

    extras = []
    if args.user_interaction:
        extras.append("-user-interaction")
    extras.extend(remains)
    scripts = [
        "win32/test/testall.py",
        "pythonwin/pywin/test/all.py",
    ]
    for script in scripts:
        maybes = [os.path.join(directory, script) for directory in code_directories]
        find_and_run(maybes, extras)

    # win32com
    maybes = [
        os.path.join(directory, "win32com", "test", "testall.py")
        for directory in [os.path.join(project_root, "com")] + site_packages
    ]
    extras = remains + ["1"]  # only run "level 1" tests in CI
    find_and_run(maybes, extras)

    # adodbapi
    if not args.skip_adodbapi:
        maybes = [
            os.path.join(directory, "adodbapi", "test", "adodbapitest.py")
            for directory in code_directories
        ]
        find_and_run(maybes, remains)
        # This script has a hard-coded sql server name in it, (and markh typically
        # doesn't have a different server to test on) but there is now supposed to be a server out there on the Internet
        # just to run these tests, so try it...
        maybes = [
            os.path.join(directory, "adodbapi", "test", "test_adodbapi_dbapi20.py")
            for directory in code_directories
        ]
        find_and_run(maybes, remains)

    if failures:
        print("The following scripts failed")
        for failure in failures:
            print(">", failure)
        sys.exit(1)
    print("All tests passed \\o/")


if __name__ == "__main__":
    main()

```


---

## win32/scripts/rasutil.py

```python
# A demo of using the RAS API from Python
import sys

import win32api
import win32ras


# The error raised if we can not
class ConnectionError(Exception):
    pass


def Connect(rasEntryName, numRetries=5):
    """Make a connection to the specified RAS entry.

    Returns a tuple of (bool, handle) on success.
    - bool is 1 if a new connection was established, or 0 is a connection already existed.
    - handle is a RAS HANDLE that can be passed to Disconnect() to end the connection.

    Raises a ConnectionError if the connection could not be established.
    """
    assert numRetries > 0
    for info in win32ras.EnumConnections():
        if info[1].lower() == rasEntryName.lower():
            print("Already connected to", rasEntryName)
            return 0, info[0]

    dial_params, have_pw = win32ras.GetEntryDialParams(None, rasEntryName)
    if not have_pw:
        print("Error: The password is not saved for this connection")
        print(
            "Please connect manually selecting the 'save password' option and try again"
        )
        sys.exit(1)

    print("Connecting to", rasEntryName, "...")
    retryCount = numRetries
    while retryCount > 0:
        rasHandle, errCode = win32ras.Dial(None, None, dial_params, None)
        if win32ras.IsHandleValid(rasHandle):
            bValid = 1
            break
        print("Retrying...")
        win32api.Sleep(5000)
        retryCount -= 1

    if errCode:
        raise ConnectionError(errCode, win32ras.GetErrorString(errCode))
    return 1, rasHandle


def Disconnect(handle):
    if isinstance(handle, str):  # have they passed a connection name?
        for info in win32ras.EnumConnections():
            if info[1].lower() == handle.lower():
                handle = info[0]
                break
        else:
            raise ConnectionError(0, "Not connected to entry '%s'" % handle)

    win32ras.HangUp(handle)


usage = """rasutil.py - Utilities for using RAS

Usage:
  rasutil [-r retryCount] [-c rasname] [-d rasname]

  -r retryCount - Number of times to retry the RAS connection
  -c rasname - Connect to the phonebook entry specified by rasname
  -d rasname - Disconnect from the phonebook entry specified by rasname
"""


def Usage(why):
    print(why)
    print(usage)
    sys.exit(1)


if __name__ == "__main__":
    import getopt

    try:
        opts, args = getopt.getopt(sys.argv[1:], "r:c:d:")
    except getopt.error as why:
        Usage(why)
    retries = 5
    if len(args) != 0:
        Usage("Invalid argument")

    for opt, val in opts:
        if opt == "-c":
            Connect(val, retries)
        if opt == "-d":
            Disconnect(val)
        if opt == "-r":
            retries = int(val)

```


---

## win32/scripts/regsetup.py

```python
# A tool to setup the Python registry.


class error(Exception):
    pass


import sys  # at least we can count on this!


def FileExists(fname):
    """Check if a file exists.  Returns true or false."""
    import os

    return os.path.exists(fname)


def IsPackageDir(path, packageName, knownFileName):
    """Given a path, a ni package name, and possibly a known file name in
    the root of the package, see if this path is good.
    """
    import os

    if knownFileName is None:
        knownFileName = "."
    return FileExists(os.path.join(os.path.join(path, packageName), knownFileName))


def IsDebug():
    """Return "_d" if we're running a debug version.

    This is to be used within DLL names when locating them.
    """
    import importlib.machinery

    return "_d" if "_d.pyd" in importlib.machinery.EXTENSION_SUFFIXES else ""


def FindPackagePath(packageName, knownFileName, searchPaths):
    """Find a package.

    Given a ni style package name, check the package is registered.

    First place looked is the registry for an existing entry.  Then
    the searchPaths are searched.
    """
    import os

    import regutil

    pathLook = regutil.GetRegisteredNamedPath(packageName)
    if pathLook and IsPackageDir(pathLook, packageName, knownFileName):
        return pathLook, None  # The currently registered one is good.
    # Search down the search paths.
    for pathLook in searchPaths:
        if IsPackageDir(pathLook, packageName, knownFileName):
            # Found it
            ret = os.path.abspath(pathLook)
            return ret, ret
    raise error("The package %s can not be located" % packageName)


def FindHelpPath(helpFile, helpDesc, searchPaths):
    # See if the current registry entry is OK
    import os

    import win32api
    import win32con

    try:
        key = win32api.RegOpenKey(
            win32con.HKEY_LOCAL_MACHINE,
            "Software\\Microsoft\\Windows\\Help",
            0,
            win32con.KEY_ALL_ACCESS,
        )
        try:
            try:
                path = win32api.RegQueryValueEx(key, helpDesc)[0]
                if FileExists(os.path.join(path, helpFile)):
                    return os.path.abspath(path)
            except win32api.error:
                pass  # no registry entry.
        finally:
            key.Close()
    except win32api.error:
        pass
    for pathLook in searchPaths:
        if FileExists(os.path.join(pathLook, helpFile)):
            return os.path.abspath(pathLook)
        pathLook = os.path.join(pathLook, "Help")
        if FileExists(os.path.join(pathLook, helpFile)):
            return os.path.abspath(pathLook)
    raise error("The help file %s can not be located" % helpFile)


def FindAppPath(appName, knownFileName, searchPaths):
    """Find an application.

    First place looked is the registry for an existing entry.  Then
    the searchPaths are searched.
    """
    # Look in the first path.
    import os

    import regutil

    regPath = regutil.GetRegisteredNamedPath(appName)
    if regPath:
        pathLook = regPath.split(";")[0]
    if regPath and FileExists(os.path.join(pathLook, knownFileName)):
        return None  # The currently registered one is good.
    # Search down the search paths.
    for pathLook in searchPaths:
        if FileExists(os.path.join(pathLook, knownFileName)):
            # Found it
            return os.path.abspath(pathLook)
    raise error(
        f"The file {knownFileName} can not be located for application {appName}"
    )


def FindPythonExe(exeAlias, possibleRealNames, searchPaths):
    """Find an exe.

    Returns the full path to the .exe, and a boolean indicating if the current
    registered entry is OK.  We don't trust the already registered version even
    if it exists - it may be wrong (ie, for a different Python version)
    """
    import os
    import sys

    import regutil
    import win32api

    if possibleRealNames is None:
        possibleRealNames = exeAlias
    # Look first in Python's home.
    found = os.path.join(sys.prefix, possibleRealNames)
    if not FileExists(found):  # for developers
        if "64 bit" in sys.version:
            found = os.path.join(sys.prefix, "PCBuild", "amd64", possibleRealNames)
        else:
            found = os.path.join(sys.prefix, "PCBuild", possibleRealNames)
    if not FileExists(found):
        found = LocateFileName(possibleRealNames, searchPaths)

    registered_ok = 0
    try:
        registered = win32api.RegQueryValue(
            regutil.GetRootKey(), regutil.GetAppPathsKey() + "\\" + exeAlias
        )
        registered_ok = found == registered
    except win32api.error:
        pass
    return found, registered_ok


def QuotedFileName(fname):
    """Given a filename, return a quoted version if necessary"""

    try:
        fname.index(" ")  # Other chars forcing quote?
        return '"%s"' % fname
    except ValueError:
        # No space in name.
        return fname


def LocateFileName(fileNamesString, searchPaths):
    """Locate a file name, anywhere on the search path.

    If the file can not be located, prompt the user to find it for us
    (using a common OpenFile dialog)

    Raises KeyboardInterrupt if the user cancels.
    """
    import os

    fileNames = fileNamesString.split(";")
    for path in searchPaths:
        for fileName in fileNames:
            retPath = os.path.join(path, fileName)
            if os.path.exists(retPath):
                break
            else:
                retPath = None
        if retPath:
            break
    else:
        fileName = fileNames[0]
        try:
            import win32con
            import win32ui
        except ImportError:
            raise error(
                "Need to locate the file %s, but the win32ui module is not available\nPlease run the program again, passing as a parameter the path to this file."
                % fileName
            )
        # Display a common dialog to locate the file.
        flags = win32con.OFN_FILEMUSTEXIST
        ext = os.path.splitext(fileName)[1]
        filter = f"Files of requested type (*{ext})|*{ext}||"
        dlg = win32ui.CreateFileDialog(1, None, fileName, flags, filter, None)
        dlg.SetOFNTitle("Locate " + fileName)
        if dlg.DoModal() != win32con.IDOK:
            raise KeyboardInterrupt("User cancelled the process")
        retPath = dlg.GetPathName()
    return os.path.abspath(retPath)


def LocatePath(fileName, searchPaths):
    """Like LocateFileName, but returns a directory only."""
    import os

    return os.path.abspath(os.path.split(LocateFileName(fileName, searchPaths))[0])


def LocateOptionalPath(fileName, searchPaths):
    """Like LocatePath, but returns None if the user cancels."""
    try:
        return LocatePath(fileName, searchPaths)
    except KeyboardInterrupt:
        return None


def LocateOptionalFileName(fileName, searchPaths=None):
    """Like LocateFileName, but returns None if the user cancels."""
    try:
        return LocateFileName(fileName, searchPaths)
    except KeyboardInterrupt:
        return None


def LocatePythonCore(searchPaths):
    """Locate and validate the core Python directories.  Returns a list
    of paths that should be used as the core (ie, un-named) portion of
    the Python path.
    """
    import os

    import regutil

    currentPath = regutil.GetRegisteredNamedPath(None)
    if currentPath:
        presearchPaths = currentPath.split(";")
    else:
        presearchPaths = [os.path.abspath(".")]
    libPath = None
    for path in presearchPaths:
        if FileExists(os.path.join(path, "os.py")):
            libPath = path
            break
    if libPath is None and searchPaths is not None:
        libPath = LocatePath("os.py", searchPaths)
    if libPath is None:
        raise error("The core Python library could not be located.")

    corePath = None
    suffix = IsDebug()
    for path in presearchPaths:
        if FileExists(os.path.join(path, "unicodedata%s.pyd" % suffix)):
            corePath = path
            break
    if corePath is None and searchPaths is not None:
        corePath = LocatePath("unicodedata%s.pyd" % suffix, searchPaths)
    if corePath is None:
        raise error("The core Python path could not be located.")

    installPath = os.path.abspath(os.path.join(libPath, ".."))
    return installPath, [libPath, corePath]


def FindRegisterPackage(packageName, knownFile, searchPaths, registryAppName=None):
    """Find and Register a package.

    Assumes the core registry setup correctly.

    In addition, if the location located by the package is already
    in the **core** path, then an entry is registered, but no path.
    (no other paths are checked, as the application whose path was used
    may later be uninstalled.  This should not happen with the core)
    """

    import regutil

    if not packageName:
        raise error("A package name must be supplied")
    corePaths = regutil.GetRegisteredNamedPath(None).split(";")
    if not searchPaths:
        searchPaths = corePaths
    registryAppName = registryAppName or packageName
    try:
        pathLook, pathAdd = FindPackagePath(packageName, knownFile, searchPaths)
        if pathAdd is not None:
            if pathAdd in corePaths:
                pathAdd = ""
            regutil.RegisterNamedPath(registryAppName, pathAdd)
        return pathLook
    except error as details:
        print(f"*** The {packageName} package could not be registered - {details}")
        print(
            "*** Please ensure you have passed the correct paths on the command line."
        )
        print(
            "*** - For packages, you should pass a path to the packages parent directory,"
        )
        print("*** - and not the package directory itself...")


def FindRegisterApp(appName, knownFiles, searchPaths):
    """Find and Register a package.

    Assumes the core registry setup correctly.

    """

    import regutil

    if isinstance(knownFiles, str):
        knownFiles = [knownFiles]
    paths = []
    try:
        for knownFile in knownFiles:
            pathLook = FindAppPath(appName, knownFile, searchPaths)
            if pathLook:
                paths.append(pathLook)
    except error as details:
        print("*** ", details)
        return

    regutil.RegisterNamedPath(appName, ";".join(paths))


def FindRegisterPythonExe(exeAlias, searchPaths, actualFileNames=None):
    """Find and Register a Python exe (not necessarily *the* python.exe)

    Assumes the core registry setup correctly.
    """

    import regutil

    fname, ok = FindPythonExe(exeAlias, actualFileNames, searchPaths)
    if not ok:
        regutil.RegisterPythonExe(fname, exeAlias)
    return fname


def FindRegisterHelpFile(helpFile, searchPaths, helpDesc=None):
    import regutil

    try:
        pathLook = FindHelpPath(helpFile, helpDesc, searchPaths)
    except error as details:
        print("*** ", details)
        return
    # print(f"{helpFile} found at {pathLook}")
    regutil.RegisterHelpFile(helpFile, pathLook, helpDesc)


def SetupCore(searchPaths):
    """Setup the core Python information in the registry.

    This function makes no assumptions about the current state of sys.path.

    After this function has completed, you should have access to the standard
    Python library, and the standard Win32 extensions
    """

    import sys

    for path in searchPaths:
        sys.path.append(path)

    import os

    import regutil
    import win32api
    import win32con

    installPath, corePaths = LocatePythonCore(searchPaths)
    # Register the core Pythonpath.
    print(corePaths)
    regutil.RegisterNamedPath(None, ";".join(corePaths))

    # Register the install path.
    hKey = win32api.RegCreateKey(regutil.GetRootKey(), regutil.BuildDefaultPythonKey())
    try:
        # Core Paths.
        win32api.RegSetValue(hKey, "InstallPath", win32con.REG_SZ, installPath)
    finally:
        win32api.RegCloseKey(hKey)

    # Register the win32 core paths.
    win32paths = (
        os.path.abspath(os.path.split(win32api.__file__)[0])
        + ";"
        + os.path.abspath(
            os.path.split(LocateFileName("win32con.py;win32con.pyc", sys.path))[0]
        )
    )

    # Python has builtin support for finding a "DLLs" directory, but
    # not a PCBuild.  Having it in the core paths means it is ignored when
    # an EXE not in the Python dir is hosting us - so we add it as a named
    # value
    check = os.path.join(sys.prefix, "PCBuild")
    if "64 bit" in sys.version:
        check = os.path.join(check, "amd64")
    if os.path.isdir(check):
        regutil.RegisterNamedPath("PCBuild", check)


def RegisterShellInfo(searchPaths):
    """Registers key parts of the Python installation with the Windows Shell.

    Assumes a valid, minimal Python installation exists
    (ie, SetupCore() has been previously successfully run)
    """
    import regutil
    import win32con

    suffix = IsDebug()
    # Set up a pointer to the .exe's
    exePath = FindRegisterPythonExe("Python%s.exe" % suffix, searchPaths)
    regutil.SetRegistryDefaultValue(".py", "Python.File", win32con.HKEY_CLASSES_ROOT)
    regutil.RegisterShellCommand("Open", QuotedFileName(exePath) + ' "%1" %*', "&Run")
    regutil.SetRegistryDefaultValue(
        "Python.File\\DefaultIcon", "%s,0" % exePath, win32con.HKEY_CLASSES_ROOT
    )

    FindRegisterHelpFile("Python.hlp", searchPaths, "Main Python Documentation")
    FindRegisterHelpFile("ActivePython.chm", searchPaths, "Main Python Documentation")

    # We consider the win32 core, as it contains all the win32 api type
    # stuff we need.


#       FindRegisterApp("win32", ["win32con.pyc", "win32api%s.pyd" % suffix], searchPaths)

usage = """\
regsetup.py - Setup/maintain the registry for Python apps.

Run without options, (but possibly search paths) to repair a totally broken
python registry setup.  This should allow other options to work.

Usage:   %s [options ...] paths ...
-p packageName  -- Find and register a package.  Looks in the paths for
                   a sub-directory with the name of the package, and
                   adds a path entry for the package.
-a appName      -- Unconditionally add an application name to the path.
                   A new path entry is create with the app name, and the
                   paths specified are added to the registry.
-c              -- Add the specified paths to the core Pythonpath.
                   If a path appears on the core path, and a package also
                   needs that same path, the package will not bother
                   registering it.  Therefore, By adding paths to the
                   core path, you can avoid packages re-registering the same path.
-m filename     -- Find and register the specific file name as a module.
                   Do not include a path on the filename!
--shell         -- Register everything with the Windows shell.
--upackage name -- Unregister the package
--uapp name     -- Unregister the app (identical to --upackage)
--umodule name  -- Unregister the module

--description   -- Print a description of the usage.
--examples      -- Print examples of usage.
""" % sys.argv[0]

description = """\
If no options are processed, the program attempts to validate and set
the standard Python path to the point where the standard library is
available.  This can be handy if you move Python to a new drive/sub-directory,
in which case most of the options would fail (as they need at least string.py,
os.py etc to function.)
Running without options should repair Python well enough to run with
the other options.

paths are search paths that the program will use to seek out a file.
For example, when registering the core Python, you may wish to
provide paths to non-standard places to look for the Python help files,
library files, etc.

See also the "regcheck.py" utility which will check and dump the contents
of the registry.
"""

# Using raw string so that all paths meant to be copied read correctly inline and when printed
examples = r"""
Examples:
"regsetup c:\weird\spot\1 c:\weird\spot\2"
Attempts to setup the core Python.  Looks in some standard places,
as well as the 2 weird spots to locate the core Python files (eg, Python.exe,
pythonXX.dll, the standard library and Win32 Extensions).

"regsetup -a myappname . .\subdir"
Registers a new Pythonpath entry named myappname, with "C:\I\AM\HERE" and
"C:\I\AM\HERE\subdir" added to the path (ie, all args are converted to
absolute paths)

"regsetup -c c:\my\python\files"
Unconditionally add "c:\my\python\files" to the 'core' Python path.

"regsetup -m some.pyd \windows\system"
Register the module some.pyd in \windows\system as a registered
module.  This will allow some.pyd to be imported, even though the
windows system directory is not (usually!) on the Python Path.

"regsetup --umodule some"
Unregister the module "some".  This means normal import rules then apply
for that module.
"""

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] in ["/?", "-?", "-help", "-h"]:
        print(usage)
    elif len(sys.argv) == 1 or not sys.argv[1][0] in ["/", "-"]:
        # No args, or useful args.
        searchPath = sys.path[:]
        for arg in sys.argv[1:]:
            searchPath.append(arg)
        # Good chance we are being run from the "regsetup.py" directory.
        # Typically this will be "\somewhere\win32\Scripts" and the
        # "somewhere" and "..\Lib" should also be searched.
        searchPath.append("..\\Build")
        searchPath.append("..\\Lib")
        searchPath.append("..")
        searchPath.append("..\\..")

        # for developers:
        # also search somewhere\lib, ..\build, and ..\..\build
        searchPath.append("..\\..\\lib")
        searchPath.append("..\\build")
        if "64 bit" in sys.version:
            searchPath.append("..\\..\\pcbuild\\amd64")
        else:
            searchPath.append("..\\..\\pcbuild")

        print("Attempting to setup/repair the Python core")

        SetupCore(searchPath)
        RegisterShellInfo(searchPath)
        FindRegisterHelpFile("PyWin32.chm", searchPath, "Pythonwin Reference")
        # Check the registry.
        print("Registration complete - checking the registry...")
        import regcheck

        regcheck.CheckRegistry()
    else:
        searchPaths = []
        import getopt

        opts, args = getopt.getopt(
            sys.argv[1:],
            "p:a:m:c",
            ["shell", "upackage=", "uapp=", "umodule=", "description", "examples"],
        )
        for arg in args:
            searchPaths.append(arg)
        for o, a in opts:
            if o == "--description":
                print(description)
            if o == "--examples":
                print(examples)
            if o == "--shell":
                print("Registering the Python core.")
                RegisterShellInfo(searchPaths)
            if o == "-p":
                print("Registering package", a)
                FindRegisterPackage(a, None, searchPaths)
            if o in ["--upackage", "--uapp"]:
                import regutil

                print("Unregistering application/package", a)
                regutil.UnregisterNamedPath(a)
            if o == "-a":
                import regutil

                path = ";".join(searchPaths)
                print("Registering application", a, "to path", path)
                regutil.RegisterNamedPath(a, path)
            if o == "-c":
                if not searchPaths:
                    raise error("-c option must provide at least one additional path")
                import regutil

                currentPaths = regutil.GetRegisteredNamedPath(None).split(";")
                oldLen = len(currentPaths)
                for newPath in searchPaths:
                    if newPath not in currentPaths:
                        currentPaths.append(newPath)
                if len(currentPaths) != oldLen:
                    print(
                        "Registering %d new core paths" % (len(currentPaths) - oldLen)
                    )
                    regutil.RegisterNamedPath(None, ";".join(currentPaths))
                else:
                    print("All specified paths are already registered.")

```


---

## win32/scripts/setup_d.py

```python
# Install and register pythonXX_d.dll, pywintypesXX_d.dll and pythoncomXX_d.dll
#
# Assumes the _d files can be found in the same directory as this script
# or in the cwd.

import os
import shutil
import sys
import winreg

import win32api


def usage_and_die(rc):
    print()
    print("This script is designed to copy and register the Python debug")
    print("binaries.  It looks for pythonXX_d.dll, pythoncomXX_d.dll etc,")
    print("and installs them to work correctly with Python debug builds.")
    print()
    print("You will generally find this script in the. zip file that")
    print("included these _d files.  Please run this script from")
    print("that directory")
    sys.exit(rc)


if os.path.splitext(os.path.basename(win32api.__file__))[0].endswith("_d"):
    print("This scripts appears to be running a DEBUG version of Python.")
    print("Please run it using a normal release build (python.exe)")
    usage_and_die(1)

try:
    import pythoncom
except ImportError as details:
    print("Could not import the release version of pythoncom")
    print(f"The error details are: {details}")
    print("Please correct this error and rerun the script")
    usage_and_die(2)

try:
    import pywintypes
except ImportError as details:
    print("Could not import the release version of pywintypes")
    print(f"The error details are: {details}")
    print("Please correct this error and rerun the script")
    usage_and_die(2)


def _docopy(src, dest):
    orig_src = src
    if not os.path.isfile(src):
        src = os.path.join(os.path.split(sys.argv[0])[0], src)
        print(
            "Can not find {} or {} to copy".format(
                os.path.abspath(orig_src), os.path.abspath(src)
            )
        )
        return 0
    try:
        shutil.copy(src, dest)
        print(f"Copied {src} -> {dest}")
        return 1
    except:
        print(f"Error copying '{src}' -> '{dest}'")
        print(sys.exc_info()[1])
        usage_and_die(3)


def _doregister(mod_name, dll_name):
    assert os.path.isfile(dll_name), "Shouldn't get here if the file doesn't exist!"
    try:
        key = winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE,
            f"Software\\Python\\PythonCore\\{sys.winver}\\Modules\\{mod_name}",
        )
    except winreg.error:
        try:
            key = winreg.OpenKey(
                winreg.HKEY_LOCAL_MACHINE,
                f"Software\\Python\\PythonCore\\{sys.winver}\\Modules\\{mod_name}",
            )
        except winreg.error:
            print(
                "Could not find the existing '{}' module registered in the registry".format(
                    mod_name
                )
            )
            usage_and_die(4)
    # Create the debug key.
    sub_key = winreg.CreateKey(key, "Debug")
    winreg.SetValue(sub_key, None, winreg.REG_SZ, dll_name)
    print(f"Registered '{dll_name}' in the registry")


def _domodule(mod_name, release_mod_filename):
    path, fname = os.path.split(release_mod_filename)
    base, ext = os.path.splitext(fname)
    new_fname = base + "_d" + ext
    if _docopy(new_fname, path):
        _doregister(mod_name, os.path.abspath(os.path.join(path, new_fname)))


# First the main Python DLL.
path, fname = path, fname = os.path.split(win32api.GetModuleFileName(sys.dllhandle))
base, ext = os.path.splitext(fname)
_docopy(base + "_d" + ext, path)

# Then pythoncom and pywintypes.
_domodule("pythoncom", pythoncom.__file__)
_domodule("pywintypes", pywintypes.__file__)

print("System _d files were setup.")

```
