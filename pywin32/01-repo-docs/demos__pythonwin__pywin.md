# 官方示例源码 · pythonwin/pywin

> 来源 https://github.com/mhammond/pywin32/tree/main/pythonwin/pywin （共 29 个 .py，全文内联）


---

## pythonwin/pywin/Demos/app/basictimerapp.py

```python
# basictimerapp - a really simple timer application.
# This should be run using the command line:
# pythonwin /app demos\basictimerapp.py
import sys
import time

import timer
import win32api
import win32con
import win32ui
from pywin.framework import dlgappcore


class TimerAppDialog(dlgappcore.AppDialog):
    softspace = 1

    def __init__(self, appName=""):
        dlgappcore.AppDialog.__init__(self, win32ui.IDD_GENERAL_STATUS)
        self.timerAppName = appName
        self.argOff = 0
        if len(self.timerAppName) == 0:
            if len(sys.argv) > 1 and sys.argv[1][0] != "/":
                self.timerAppName = sys.argv[1]
                self.argOff = 1

    def PreDoModal(self):
        # 		sys.stderr = sys.stdout
        pass

    def ProcessArgs(self, args):
        for arg in args:
            if arg == "/now":
                self.OnOK()

    def OnInitDialog(self):
        win32ui.SetProfileFileName("pytimer.ini")
        self.title = win32ui.GetProfileVal(
            self.timerAppName, "Title", "Remote System Timer"
        )
        self.buildTimer = win32ui.GetProfileVal(
            self.timerAppName, "Timer", "EachMinuteIntervaler()"
        )
        self.doWork = win32ui.GetProfileVal(self.timerAppName, "Work", "DoDemoWork()")
        # replace "\n" with real \n.
        self.doWork = self.doWork.replace("\\n", "\n")
        dlgappcore.AppDialog.OnInitDialog(self)

        self.SetWindowText(self.title)
        self.prompt1 = self.GetDlgItem(win32ui.IDC_PROMPT1)
        self.prompt2 = self.GetDlgItem(win32ui.IDC_PROMPT2)
        self.prompt3 = self.GetDlgItem(win32ui.IDC_PROMPT3)
        self.butOK = self.GetDlgItem(win32con.IDOK)
        self.butCancel = self.GetDlgItem(win32con.IDCANCEL)
        self.prompt1.SetWindowText("Python Timer App")
        self.prompt2.SetWindowText("")
        self.prompt3.SetWindowText("")
        self.butOK.SetWindowText("Do it now")
        self.butCancel.SetWindowText("Close")

        self.timerManager = TimerManager(self)
        self.ProcessArgs(sys.argv[self.argOff :])
        self.timerManager.go()
        return 1

    def OnDestroy(self, msg):
        dlgappcore.AppDialog.OnDestroy(self, msg)
        self.timerManager.stop()

    def OnOK(self):
        # stop the timer, then restart after setting special boolean
        self.timerManager.stop()
        self.timerManager.bConnectNow = 1
        self.timerManager.go()
        return


# 	def OnCancel(self): default behaviour - cancel == close.
# 		return


class TimerManager:
    def __init__(self, dlg):
        self.dlg = dlg
        self.timerId = None
        self.intervaler = eval(self.dlg.buildTimer)
        self.bConnectNow = 0
        self.bHaveSetPrompt1 = 0

    def CaptureOutput(self):
        self.oldOut = sys.stdout
        self.oldErr = sys.stderr
        sys.stdout = sys.stderr = self
        self.bHaveSetPrompt1 = 0

    def ReleaseOutput(self):
        sys.stdout = self.oldOut
        sys.stderr = self.oldErr

    def write(self, str):
        s = str.strip()
        if len(s):
            if self.bHaveSetPrompt1:
                dest = self.dlg.prompt3
            else:
                dest = self.dlg.prompt1
                self.bHaveSetPrompt1 = 1
            dest.SetWindowText(s)

    def go(self):
        self.OnTimer(None, None)

    def stop(self):
        if self.timerId:
            timer.kill_timer(self.timerId)
        self.timerId = None

    def OnTimer(self, id, timeVal):
        if id:
            timer.kill_timer(id)
        if self.intervaler.IsTime() or self.bConnectNow:
            # do the work.
            try:
                self.dlg.SetWindowText(self.dlg.title + " - Working...")
                self.dlg.butOK.EnableWindow(0)
                self.dlg.butCancel.EnableWindow(0)
                self.CaptureOutput()
                try:
                    exec(self.dlg.doWork)
                    print("The last operation completed successfully.")
                except:
                    t, v, tb = sys.exc_info()
                    str = f"Failed: {t}: {v!r}"
                    print(str)
                    self.oldErr.write(str)
                    tb = None  # Prevent cycle
            finally:
                self.ReleaseOutput()
                self.dlg.butOK.EnableWindow()
                self.dlg.butCancel.EnableWindow()
                self.dlg.SetWindowText(self.dlg.title)
        else:
            now = time.time()
            nextTime = self.intervaler.GetNextTime()
            if nextTime:
                timeDiffSeconds = nextTime - now
                timeDiffMinutes = int(timeDiffSeconds / 60)
                timeDiffSeconds %= 60
                timeDiffHours = int(timeDiffMinutes / 60)
                timeDiffMinutes %= 60
                self.dlg.prompt1.SetWindowText(
                    "Next connection due in %02d:%02d:%02d"
                    % (timeDiffHours, timeDiffMinutes, timeDiffSeconds)
                )
        self.timerId = timer.set_timer(
            self.intervaler.GetWakeupInterval(), self.OnTimer
        )
        self.bConnectNow = 0


class TimerIntervaler:
    def __init__(self):
        self.nextTime = None
        self.wakeUpInterval = 2000

    def GetWakeupInterval(self):
        return self.wakeUpInterval

    def GetNextTime(self):
        return self.nextTime

    def IsTime(self):
        now = time.time()
        if self.nextTime is None:
            self.nextTime = self.SetFirstTime(now)
        ret = 0
        if now >= self.nextTime:
            ret = 1
            self.nextTime = self.SetNextTime(self.nextTime, now)
            # do the work.
        return ret


class EachAnyIntervaler(TimerIntervaler):
    def __init__(self, timeAt, timePos, timeAdd, wakeUpInterval=None):
        TimerIntervaler.__init__(self)
        self.timeAt = timeAt
        self.timePos = timePos
        self.timeAdd = timeAdd
        if wakeUpInterval:
            self.wakeUpInterval = wakeUpInterval

    def SetFirstTime(self, now):
        timeTup = time.localtime(now)
        lst = []
        for item in timeTup:
            lst.append(item)
        bAdd = timeTup[self.timePos] > self.timeAt
        lst[self.timePos] = self.timeAt
        for pos in range(self.timePos + 1, 6):
            lst[pos] = 0
        ret = time.mktime(tuple(lst))
        if bAdd:
            ret += self.timeAdd
        return ret

    def SetNextTime(self, lastTime, now):
        return lastTime + self.timeAdd


class EachMinuteIntervaler(EachAnyIntervaler):
    def __init__(self, at=0):
        EachAnyIntervaler.__init__(self, at, 5, 60, 2000)


class EachHourIntervaler(EachAnyIntervaler):
    def __init__(self, at=0):
        EachAnyIntervaler.__init__(self, at, 4, 3600, 10000)


class EachDayIntervaler(EachAnyIntervaler):
    def __init__(self, at=0):
        EachAnyIntervaler.__init__(self, at, 3, 86400, 10000)


class TimerDialogApp(dlgappcore.DialogApp):
    def CreateDialog(self):
        return TimerAppDialog()


def DoDemoWork():
    print("Doing the work...")
    print("About to connect")
    win32api.MessageBeep(win32con.MB_ICONASTERISK)
    win32api.Sleep(2000)
    print("Doing something else...")
    win32api.MessageBeep(win32con.MB_ICONEXCLAMATION)
    win32api.Sleep(2000)
    print("More work.")
    win32api.MessageBeep(win32con.MB_ICONHAND)
    win32api.Sleep(2000)
    print("The last bit.")
    win32api.MessageBeep(win32con.MB_OK)
    win32api.Sleep(2000)


app = TimerDialogApp()


def t():
    t = TimerAppDialog("Test Dialog")
    t.DoModal()
    return t


if __name__ == "__main__":
    import demoutils

    demoutils.NeedApp()

```


---

## pythonwin/pywin/Demos/app/customprint.py

```python
# A demo of an Application object that has some custom print functionality.

# If you desire, you can also run this from inside Pythonwin, in which
# case it will do the demo inside the Pythonwin environment.

# This sample was contributed by Roger Burnham.

import win32con
import win32ui
from pywin.framework import app
from pywin.mfc import afxres, dialog, docview

PRINTDLGORD = 1538
IDC_PRINT_MAG_EDIT = 1010


class PrintDemoTemplate(docview.DocTemplate):
    def _SetupSharedMenu_(self):
        pass


class PrintDemoView(docview.ScrollView):
    def OnInitialUpdate(self):
        ret = self._obj_.OnInitialUpdate()
        self.colors = {
            "Black": (0x00 << 0) + (0x00 << 8) + (0x00 << 16),
            "Red": (0xFF << 0) + (0x00 << 8) + (0x00 << 16),
            "Green": (0x00 << 0) + (0xFF << 8) + (0x00 << 16),
            "Blue": (0x00 << 0) + (0x00 << 8) + (0xFF << 16),
            "Cyan": (0x00 << 0) + (0xFF << 8) + (0xFF << 16),
            "Magenta": (0xFF << 0) + (0x00 << 8) + (0xFF << 16),
            "Yellow": (0xFF << 0) + (0xFF << 8) + (0x00 << 16),
        }
        self.pens = {}
        for name, color in self.colors.items():
            self.pens[name] = win32ui.CreatePen(win32con.PS_SOLID, 5, color)
        self.pen = None
        self.size = (128, 128)
        self.SetScaleToFitSize(self.size)
        self.HookCommand(self.OnFilePrint, afxres.ID_FILE_PRINT)
        self.HookCommand(self.OnFilePrintPreview, win32ui.ID_FILE_PRINT_PREVIEW)
        return ret

    def OnDraw(self, dc):
        oldPen = None
        x, y = self.size
        delta = 2
        colors = sorted(self.colors) * 2
        for color in colors:
            if oldPen is None:
                oldPen = dc.SelectObject(self.pens[color])
            else:
                dc.SelectObject(self.pens[color])
            dc.MoveTo((delta, delta))
            dc.LineTo((x - delta, delta))
            dc.LineTo((x - delta, y - delta))
            dc.LineTo((delta, y - delta))
            dc.LineTo((delta, delta))
            delta += 4
            if x - delta <= 0 or y - delta <= 0:
                break
        dc.SelectObject(oldPen)

    def OnPrepareDC(self, dc, pInfo):
        if dc.IsPrinting():
            mag = self.prtDlg["mag"]
            dc.SetMapMode(win32con.MM_ANISOTROPIC)
            dc.SetWindowOrg((0, 0))
            dc.SetWindowExt((1, 1))
            dc.SetViewportOrg((0, 0))
            dc.SetViewportExt((mag, mag))

    def OnPreparePrinting(self, pInfo):
        flags = (
            win32ui.PD_USEDEVMODECOPIES
            | win32ui.PD_PAGENUMS
            | win32ui.PD_NOPAGENUMS
            | win32ui.PD_NOSELECTION
        )
        self.prtDlg = ImagePrintDialog(pInfo, PRINTDLGORD, flags)
        pInfo.SetPrintDialog(self.prtDlg)
        pInfo.SetMinPage(1)
        pInfo.SetMaxPage(1)
        pInfo.SetFromPage(1)
        pInfo.SetToPage(1)
        ret = self.DoPreparePrinting(pInfo)
        return ret

    def OnBeginPrinting(self, dc, pInfo):
        return self._obj_.OnBeginPrinting(dc, pInfo)

    def OnEndPrinting(self, dc, pInfo):
        del self.prtDlg
        return self._obj_.OnEndPrinting(dc, pInfo)

    def OnFilePrintPreview(self, *arg):
        self._obj_.OnFilePrintPreview()

    def OnFilePrint(self, *arg):
        self._obj_.OnFilePrint()

    def OnPrint(self, dc, pInfo):
        doc = self.GetDocument()
        metrics = dc.GetTextMetrics()
        cxChar = metrics["tmAveCharWidth"]
        cyChar = metrics["tmHeight"]
        left, top, right, bottom = pInfo.GetDraw()
        dc.TextOut(0, 2 * cyChar, doc.GetTitle())
        top += 7 * cyChar / 2
        dc.MoveTo(left, top)
        dc.LineTo(right, top)
        top += cyChar
        # this seems to have not effect...
        # get what I want with the dc.SetWindowOrg calls
        pInfo.SetDraw((left, top, right, bottom))
        dc.SetWindowOrg((0, -top))

        self.OnDraw(dc)
        dc.SetTextAlign(win32con.TA_LEFT | win32con.TA_BOTTOM)

        rect = self.GetWindowRect()
        rect = self.ScreenToClient(rect)
        height = rect[3] - rect[1]
        dc.SetWindowOrg((0, -(top + height + cyChar)))
        dc.MoveTo(left, 0)
        dc.LineTo(right, 0)

        x = 0
        y = (3 * cyChar) / 2

        dc.TextOut(x, y, doc.GetTitle())
        y += cyChar


class PrintDemoApp(app.CApp):
    def __init__(self):
        app.CApp.__init__(self)

    def InitInstance(self):
        template = PrintDemoTemplate(None, None, None, PrintDemoView)
        self.AddDocTemplate(template)
        self._obj_.InitMDIInstance()
        self.LoadMainFrame()
        doc = template.OpenDocumentFile(None)
        doc.SetTitle("Custom Print Document")


class ImagePrintDialog(dialog.PrintDialog):
    sectionPos = "Image Print Demo"

    def __init__(self, pInfo, dlgID, flags=win32ui.PD_USEDEVMODECOPIES):
        dialog.PrintDialog.__init__(self, pInfo, dlgID, flags=flags)
        mag = win32ui.GetProfileVal(self.sectionPos, "Document Magnification", 0)
        if mag <= 0:
            mag = 2
            win32ui.WriteProfileVal(self.sectionPos, "Document Magnification", mag)

        self["mag"] = mag

    def OnInitDialog(self):
        self.magCtl = self.GetDlgItem(IDC_PRINT_MAG_EDIT)
        self.magCtl.SetWindowText(repr(self["mag"]))
        return dialog.PrintDialog.OnInitDialog(self)

    def OnOK(self):
        dialog.PrintDialog.OnOK(self)
        strMag = self.magCtl.GetWindowText()
        try:
            self["mag"] = int(strMag)
        except:
            pass
        win32ui.WriteProfileVal(self.sectionPos, "Document Magnification", self["mag"])


if __name__ == "__main__":
    # Running under Pythonwin
    def test():
        template = PrintDemoTemplate(None, None, None, PrintDemoView)
        template.OpenDocumentFile(None)

    test()
else:
    app = PrintDemoApp()

```


---

## pythonwin/pywin/Demos/app/demoutils.py

```python
# Utilities for the demos

import sys

import win32api
import win32con
import win32ui

NotScriptMsg = """\
This demo program is not designed to be run as a Script, but is
probably used by some other test program.  Please try another demo.
"""

NeedGUIMsg = """\
This demo program can only be run from inside of Pythonwin

You must start Pythonwin, and select 'Run' from the toolbar or File menu
"""


NeedAppMsg = """\
This demo program is a 'Pythonwin Application'.

It is more demo code than an example of Pythonwin's capabilities.

To run it, you must execute the command:
Pythonwin.exe /app "%s"

Would you like to execute it now?
"""


def NotAScript():
    import win32ui

    win32ui.MessageBox(NotScriptMsg, "Demos")


def NeedGoodGUI():
    from pywin.framework.app import HaveGoodGUI

    rc = HaveGoodGUI()
    if not rc:
        win32ui.MessageBox(NeedGUIMsg, "Demos")
    return rc


def NeedApp():
    import win32ui

    rc = win32ui.MessageBox(NeedAppMsg % sys.argv[0], "Demos", win32con.MB_YESNO)
    if rc == win32con.IDYES:
        try:
            parent = win32ui.GetMainFrame().GetSafeHwnd()
            win32api.ShellExecute(
                parent, None, "Pythonwin.exe", '/app "%s"' % sys.argv[0], None, 1
            )
        except win32api.error as details:
            win32ui.MessageBox("Error executing command - %s" % (details), "Demos")


if __name__ == "__main__":
    NotAScript()

```


---

## pythonwin/pywin/Demos/app/dlgappdemo.py

```python
# dlgappdemo - a demo of a dialog application.
# This is a demonstration of both a custom "application" module,
# and a Python program in a dialog box.
#
# NOTE:  You CAN NOT import this module from either PythonWin or Python.
# This module must be specified on the commandline to PythonWin only.
# eg, PythonWin /app dlgappdemo.py

import sys

import win32ui
from pywin.framework import dlgappcore


class TestDialogApp(dlgappcore.DialogApp):
    def CreateDialog(self):
        return TestAppDialog()


class TestAppDialog(dlgappcore.AppDialog):
    def __init__(self):
        self.edit = None
        dlgappcore.AppDialog.__init__(self, win32ui.IDD_LARGE_EDIT)

    def OnInitDialog(self):
        self.SetWindowText("Test dialog application")
        self.edit = self.GetDlgItem(win32ui.IDC_EDIT1)
        print("Hello from Python")
        print("args are:", end=" ")
        for arg in sys.argv:
            print(arg)
        return 1

    def PreDoModal(self):
        sys.stdout = sys.stderr = self

    def write(self, str):
        if self.edit:
            self.edit.SetSel(-2)
            # translate \n to \n\r
            self.edit.ReplaceSel(str.replace("\n", "\r\n"))
        else:
            win32ui.OutputDebug("dlgapp - no edit control! >>\n%s\n<<\n" % str)


app = TestDialogApp()

if __name__ == "__main__":
    import demoutils

    demoutils.NeedApp()

```


---

## pythonwin/pywin/Demos/app/dojobapp.py

```python
# dojobapp - do a job, show the result in a dialog, and exit.
#
# Very simple - faily minimal dialog based app.
#
# This should be run using the command line:
# pythonwin /app demos\dojobapp.py


import win32con
import win32ui
from pywin.framework import dlgappcore


class DoJobAppDialog(dlgappcore.AppDialog):
    softspace = 1

    def __init__(self, appName=""):
        self.appName = appName
        dlgappcore.AppDialog.__init__(self, win32ui.IDD_GENERAL_STATUS)

    def PreDoModal(self):
        pass

    def ProcessArgs(self, args):
        pass

    def OnInitDialog(self):
        self.SetWindowText(self.appName)
        butCancel = self.GetDlgItem(win32con.IDCANCEL)
        butCancel.ShowWindow(win32con.SW_HIDE)
        p1 = self.GetDlgItem(win32ui.IDC_PROMPT1)
        p2 = self.GetDlgItem(win32ui.IDC_PROMPT2)

        # Do something here!

        p1.SetWindowText("Hello there")
        p2.SetWindowText("from the demo")

    def OnDestroy(self, msg):
        pass


# 	def OnOK(self):
# 		pass
# 	def OnCancel(self): default behaviour - cancel == close.
# 		return


class DoJobDialogApp(dlgappcore.DialogApp):
    def CreateDialog(self):
        return DoJobAppDialog("Do Something")


class CopyToDialogApp(DoJobDialogApp):
    def __init__(self):
        DoJobDialogApp.__init__(self)


app = DoJobDialogApp()


def t():
    t = DoJobAppDialog("Copy To")
    t.DoModal()
    return t


if __name__ == "__main__":
    import demoutils

    demoutils.NeedApp()

```


---

## pythonwin/pywin/Demos/app/helloapp.py

```python
##
## helloapp.py
##
##
## A nice, small 'hello world' Pythonwin application.
## NOT an MDI application - just a single, normal, top-level window.
##
## MUST be run with the command line "Pythonwin.exe /app helloapp.py"
## (or if you are really keen, rename "Pythonwin.exe" to something else, then
## using MSVC or similar, edit the string section in the .EXE to name this file)
##
## Originally by Willy Heineman <wheineman@uconect.net>


import win32con
import win32ui
from pywin.mfc import window
from pywin.mfc.thread import WinApp


# The main frame.
# Does almost nothing at all - doesn't even create a child window!
class HelloWindow(window.Wnd):
    def __init__(self):
        # The window.Wnd ctor creates a Window object, and places it in
        # self._obj_.  Note the window object exists, but the window itself
        # does not!
        window.Wnd.__init__(self, win32ui.CreateWnd())

        # Now we ask the window object to create the window itself.
        self._obj_.CreateWindowEx(
            win32con.WS_EX_CLIENTEDGE,
            win32ui.RegisterWndClass(0, 0, win32con.COLOR_WINDOW + 1),
            "Hello World!",
            win32con.WS_OVERLAPPEDWINDOW,
            (100, 100, 400, 300),
            None,
            0,
            None,
        )


# The application object itself.
class HelloApp(WinApp):
    def InitInstance(self):
        self.frame = HelloWindow()
        self.frame.ShowWindow(win32con.SW_SHOWNORMAL)
        # We need to tell MFC what our main frame is.
        self.SetMainFrame(self.frame)


# Now create the application object itself!
app = HelloApp()

```


---

## pythonwin/pywin/Demos/cmdserver.py

```python
# cmdserver.py

# Demo code that is not Pythonwin related, but too good to throw away...

import _thread
import sys
import traceback

import win32api
from pywin.framework import winout


class ThreadWriter:
    "Assign an instance to sys.stdout for per-thread printing objects - Courtesy Guido!"

    def __init__(self):
        "Constructor -- initialize the table of writers"
        self.writers = {}
        self.origStdOut = None

    def register(self, writer):
        "Register the writer for the current thread"
        self.writers[_thread.get_ident()] = writer
        if self.origStdOut is None:
            self.origStdOut = sys.stdout
            sys.stdout = self

    def unregister(self):
        "Remove the writer for the current thread, if any"
        try:
            del self.writers[_thread.get_ident()]
        except KeyError:
            pass
        if len(self.writers) == 0:
            sys.stdout = self.origStdOut
            self.origStdOut = None

    def getwriter(self):
        "Return the current thread's writer, default sys.stdout"
        self.writers.get(_thread.get_ident(), self.origStdOut)

    def write(self, str):
        "Write to the current thread's writer, default sys.stdout"
        self.getwriter().write(str)


def Test():
    num = 1
    while num < 1000:
        print("Hello there no", num)
        win32api.Sleep(50)
        num += 1


class flags:
    SERVER_BEST = 0
    SERVER_IMMEDIATE = 1
    SERVER_THREAD = 2
    SERVER_PROCESS = 3


def StartServer(cmd, title=None, bCloseOnEnd=0, serverFlags=flags.SERVER_BEST):
    out = winout.WindowOutput(title, None, winout.flags.WQ_IDLE)
    if not title:
        title = cmd
    out.Create(title)
    # 	ServerThread((out, cmd, title, bCloseOnEnd))
    # 	out = sys.stdout
    _thread.start_new_thread(ServerThread, (out, cmd, title, bCloseOnEnd))


def ServerThread(myout, cmd, title, bCloseOnEnd):
    try:
        writer.register(myout)
        print('Executing "%s"\n' % cmd)
        bOK = 1
        try:
            import __main__

            exec(cmd + "\n", __main__.__dict__)
        except:
            bOK = 0
        if bOK:
            print("Command terminated without errors.")
        else:
            t, v, tb = sys.exc_info()
            print(t, ": ", v)
            traceback.print_tb(tb)
            tb = None  # prevent a cycle
            print("Command terminated with an unhandled exception")
        writer.unregister()
        if bOK and bCloseOnEnd:
            myout.frame.DestroyWindow()

    # Unhandled exception of any kind in a thread kills the gui!
    except:
        t, v, tb = sys.exc_info()
        print(t, ": ", v)
        traceback.print_tb(tb)
        tb = None
        print("Thread failed")


# assist for reloading (when debugging) - use only 1 tracer object,
# else a large chain of tracer objects will exist.
try:
    writer
except NameError:
    writer = ThreadWriter()
if __name__ == "__main__":
    import demoutils

    demoutils.NotAScript()

```


---

## pythonwin/pywin/Demos/createwin.py

```python
#
# Window creation example
#
# 	This example creates a minimal "control" that just fills in its
# 	window with red.  To make your own control, subclass Control and
# 	write your own OnPaint() method.  See PyCWnd.HookMessage for what
# 	the parameters to OnPaint are.
#

import win32api
import win32con
import win32ui
from pywin.mfc import dialog, window


class Control(window.Wnd):
    """Generic control class"""

    def __init__(self):
        window.Wnd.__init__(self, win32ui.CreateWnd())

    def OnPaint(self):
        dc, paintStruct = self.BeginPaint()
        self.DoPaint(dc)
        self.EndPaint(paintStruct)

    def DoPaint(self, dc):  # Override this!
        pass


class RedBox(Control):
    def DoPaint(self, dc):
        dc.FillSolidRect(self.GetClientRect(), win32api.RGB(255, 0, 0))


class RedBoxWithPie(RedBox):
    def DoPaint(self, dc):
        RedBox.DoPaint(self, dc)
        r = self.GetClientRect()
        dc.Pie(r[0], r[1], r[2], r[3], 0, 0, r[2], r[3] // 2)


def MakeDlgTemplate():
    style = (
        win32con.DS_MODALFRAME
        | win32con.WS_POPUP
        | win32con.WS_VISIBLE
        | win32con.WS_CAPTION
        | win32con.WS_SYSMENU
        | win32con.DS_SETFONT
    )
    cs = win32con.WS_CHILD | win32con.WS_VISIBLE

    w = 64
    h = 64

    dlg = [
        ["Red box", (0, 0, w, h), style, None, (8, "MS Sans Serif")],
    ]

    s = win32con.WS_TABSTOP | cs

    dlg.append(
        [
            128,
            "Cancel",
            win32con.IDCANCEL,
            (7, h - 18, 50, 14),
            s | win32con.BS_PUSHBUTTON,
        ]
    )

    return dlg


class TestDialog(dialog.Dialog):
    def OnInitDialog(self):
        rc = dialog.Dialog.OnInitDialog(self)
        self.redbox = RedBox()
        self.redbox.CreateWindow(
            None,
            "RedBox",
            win32con.WS_CHILD | win32con.WS_VISIBLE,
            (5, 5, 90, 68),
            self,
            1003,
        )
        return rc


class TestPieDialog(dialog.Dialog):
    def OnInitDialog(self):
        rc = dialog.Dialog.OnInitDialog(self)
        self.control = RedBoxWithPie()
        self.control.CreateWindow(
            None,
            "RedBox with Pie",
            win32con.WS_CHILD | win32con.WS_VISIBLE,
            (5, 5, 90, 68),
            self,
            1003,
        )


def demo(modal=0):
    d = TestPieDialog(MakeDlgTemplate())
    if modal:
        d.DoModal()
    else:
        d.CreateWindow()


if __name__ == "__main__":
    demo(1)

```


---

## pythonwin/pywin/Demos/demoutils.py

```python
# Utilities for the demos

import sys

import win32api
import win32con
import win32ui

NotScriptMsg = """\
This demo program is not designed to be run as a Script, but is
probably used by some other test program.  Please try another demo.
"""

NeedGUIMsg = """\
This demo program can only be run from inside of Pythonwin

You must start Pythonwin, and select 'Run' from the toolbar or File menu
"""


NeedAppMsg = """\
This demo program is a 'Pythonwin Application'.

It is more demo code than an example of Pythonwin's capabilities.

To run it, you must execute the command:
Pythonwin.exe /app "%s"

Would you like to execute it now?
"""


def NotAScript():
    import win32ui

    win32ui.MessageBox(NotScriptMsg, "Demos")


def NeedGoodGUI():
    from pywin.framework.app import HaveGoodGUI

    rc = HaveGoodGUI()
    if not rc:
        win32ui.MessageBox(NeedGUIMsg, "Demos")
    return rc


def NeedApp():
    import win32ui

    rc = win32ui.MessageBox(NeedAppMsg % sys.argv[0], "Demos", win32con.MB_YESNO)
    if rc == win32con.IDYES:
        try:
            parent = win32ui.GetMainFrame().GetSafeHwnd()
            win32api.ShellExecute(
                parent, None, "Pythonwin.exe", '/app "%s"' % sys.argv[0], None, 1
            )
        except win32api.error as details:
            win32ui.MessageBox("Error executing command - %s" % (details), "Demos")


if __name__ == "__main__":
    import demoutils

    demoutils.NotAScript()

```


---

## pythonwin/pywin/Demos/dibdemo.py

```python
# A demo which creates a view and a frame which displays a PPM format bitmap
#
# This hasnnt been run in a while, as I don't have many of that format around!

import win32api
import win32con
import win32ui


class DIBView:
    def __init__(self, doc, dib):
        self.dib = dib
        self.view = win32ui.CreateView(doc)
        self.width = self.height = 0
        # set up message handlers
        # 		self.view.OnPrepareDC = self.OnPrepareDC
        self.view.HookMessage(self.OnSize, win32con.WM_SIZE)

    def OnSize(self, params):
        lParam = params[3]
        self.width = win32api.LOWORD(lParam)
        self.height = win32api.HIWORD(lParam)

    def OnDraw(self, ob, dc):
        # set sizes used for "non strecth" mode.
        self.view.SetScrollSizes(win32con.MM_TEXT, self.dib.GetSize())
        dibSize = self.dib.GetSize()
        dibRect = (0, 0, dibSize[0], dibSize[1])
        # stretch BMP.
        # self.dib.Paint(dc, (0,0,self.width, self.height),dibRect)
        # non stretch.
        self.dib.Paint(dc)


class DIBDemo:
    def __init__(self, filename, *bPBM):
        # init data members
        f = open(filename, "rb")
        dib = win32ui.CreateDIBitmap()
        if len(bPBM) > 0:
            magic = f.readline()
            if magic != "P6\n":
                print("The file is not a PBM format file")
                raise ValueError("Failed - The file is not a PBM format file")
            # check magic?
            rowcollist = f.readline().split()
            cols = int(rowcollist[0])
            rows = int(rowcollist[1])
            f.readline()  # what's this one?
            dib.LoadPBMData(f, (cols, rows))
        else:
            dib.LoadWindowsFormatFile(f)
        f.close()
        # create doc/view
        self.doc = win32ui.CreateDoc()
        self.dibView = DIBView(self.doc, dib)
        self.frame = win32ui.CreateMDIFrame()
        self.frame.LoadFrame()  # this will force OnCreateClient
        self.doc.SetTitle("DIB Demo")
        self.frame.ShowWindow()

        # display the sucka
        self.frame.ActivateFrame()

    def OnCreateClient(self, createparams, context):
        self.dibView.view.CreateWindow(self.frame)
        return 1


if __name__ == "__main__":
    import demoutils

    demoutils.NotAScript()

```


---

## pythonwin/pywin/Demos/dlgtest.py

```python
# A Demo of Pythonwin's Dialog and Property Page support.

###################
#
# First demo - use the built-in to Pythonwin "Tab Stop" dialog, but
# customise it heavily.
#
# ID's for the tabstop dialog - out test.
#
import win32con
import win32ui
from pywin.mfc import dialog
from win32con import IDCANCEL
from win32ui import IDC_EDIT_TABS, IDC_PROMPT_TABS, IDD_SET_TABSTOPS


class TestDialog(dialog.Dialog):
    def __init__(self, modal=1):
        dialog.Dialog.__init__(self, IDD_SET_TABSTOPS)
        self.counter = 0
        if modal:
            self.DoModal()
        else:
            self.CreateWindow()

    def OnInitDialog(self):
        # Set the caption of the dialog itself.
        self.SetWindowText("Used to be Tab Stops!")
        # Get a child control, remember it, and change its text.
        self.edit = self.GetDlgItem(IDC_EDIT_TABS)  # the text box.
        self.edit.SetWindowText("Test")
        # Hook a Windows message for the dialog.
        self.edit.HookMessage(self.KillFocus, win32con.WM_KILLFOCUS)
        # Get the prompt control, and change its next.
        prompt = self.GetDlgItem(IDC_PROMPT_TABS)  # the prompt box.
        prompt.SetWindowText("Prompt")
        # And the same for the button..
        cancel = self.GetDlgItem(IDCANCEL)  # the cancel button
        cancel.SetWindowText("&Kill me")

        # And just for demonstration purposes, we hook the notify message for the dialog.
        # This allows us to be notified when the Edit Control text changes.
        self.HookCommand(self.OnNotify, IDC_EDIT_TABS)

    def OnNotify(self, controlid, code):
        if code == win32con.EN_CHANGE:
            print("Edit text changed!")
        return 1  # I handled this, so no need to call defaults!

    # kill focus for the edit box.
    # Simply increment the value in the text box.
    def KillFocus(self, msg):
        self.counter += 1
        if self.edit is not None:
            self.edit.SetWindowText(str(self.counter))

    # Called when the dialog box is terminating...
    def OnDestroy(self, msg):
        del self.edit
        del self.counter


# A very simply Property Sheet.
# We only make a new class for demonstration purposes.
class TestSheet(dialog.PropertySheet):
    def __init__(self, title):
        dialog.PropertySheet.__init__(self, title)
        self.HookMessage(self.OnActivate, win32con.WM_ACTIVATE)

    def OnActivate(self, msg):
        pass


# A very simply Property Page, which will be "owned" by the above
# Property Sheet.
# We create a new class, just so we can hook a control notification.
class TestPage(dialog.PropertyPage):
    def OnInitDialog(self):
        # We use the HookNotify function to allow Python to respond to
        # Windows WM_NOTIFY messages.
        # In this case, we are interested in BN_CLICKED messages.
        self.HookNotify(self.OnNotify, win32con.BN_CLICKED)

    def OnNotify(self, std, extra):
        print("OnNotify", std, extra)


# Some code that actually uses these objects.
def demo(modal=0):
    TestDialog(modal)

    # property sheet/page demo
    ps = win32ui.CreatePropertySheet("Property Sheet/Page Demo")
    # Create a completely standard PropertyPage.
    page1 = win32ui.CreatePropertyPage(win32ui.IDD_PROPDEMO1)
    # Create our custom property page.
    page2 = TestPage(win32ui.IDD_PROPDEMO2)
    ps.AddPage(page1)
    ps.AddPage(page2)
    if modal:
        ps.DoModal()
    else:
        style = (
            win32con.WS_SYSMENU
            | win32con.WS_POPUP
            | win32con.WS_CAPTION
            | win32con.DS_MODALFRAME
            | win32con.WS_VISIBLE
        )
        styleex = win32con.WS_EX_DLGMODALFRAME | win32con.WS_EX_PALETTEWINDOW
        ps.CreateWindow(win32ui.GetMainFrame(), style, styleex)


def test(modal=1):
    # 	dlg=dialog.Dialog(1010)
    # 	dlg.CreateWindow()
    # 	dlg.EndDialog(0)
    # 	del dlg
    # 	return
    # property sheet/page demo
    ps = TestSheet("Property Sheet/Page Demo")
    page1 = win32ui.CreatePropertyPage(win32ui.IDD_PROPDEMO1)
    page2 = win32ui.CreatePropertyPage(win32ui.IDD_PROPDEMO2)
    ps.AddPage(page1)
    ps.AddPage(page2)
    del page1
    del page2
    if modal:
        ps.DoModal()
    else:
        ps.CreateWindow(win32ui.GetMainFrame())
    return ps


def d():
    dlg = win32ui.CreateDialog(win32ui.IDD_DEBUGGER)
    dlg.datalist.append((win32ui.IDC_DBG_RADIOSTACK, "radio"))
    print("data list is ", dlg.datalist)
    dlg.data["radio"] = 1
    dlg.DoModal()
    print(dlg.data["radio"])


if __name__ == "__main__":
    demo(1)

```


---

## pythonwin/pywin/Demos/dyndlg.py

```python
# dyndlg.py
# contributed by Curt Hagenlocher <chi@earthlink.net>

# Dialog Template params:
# 	Parameter 0 - Window caption
# 	Parameter 1 - Bounds (rect tuple)
# 	Parameter 2 - Window style
# 	Parameter 3 - Extended style
# 	Parameter 4 - Font tuple
# 	Parameter 5 - Menu name
# 	Parameter 6 - Window class
# Dialog item params:
# 	Parameter 0 - Window class
# 	Parameter 1 - Text
# 	Parameter 2 - ID
# 	Parameter 3 - Bounds
# 	Parameter 4 - Style
# 	Parameter 5 - Extended style
# 	Parameter 6 - Extra data


import win32con
import win32ui
from pywin.mfc import dialog


def MakeDlgTemplate():
    style = (
        win32con.DS_MODALFRAME
        | win32con.WS_POPUP
        | win32con.WS_VISIBLE
        | win32con.WS_CAPTION
        | win32con.WS_SYSMENU
        | win32con.DS_SETFONT
    )
    cs = win32con.WS_CHILD | win32con.WS_VISIBLE
    dlg = [
        ["Select Warehouse", (0, 0, 177, 93), style, None, (8, "MS Sans Serif")],
    ]
    dlg.append([130, "Current Warehouse:", -1, (7, 7, 69, 9), cs | win32con.SS_LEFT])
    dlg.append([130, "ASTORIA", 128, (16, 17, 99, 7), cs | win32con.SS_LEFT])
    dlg.append([130, "New &Warehouse:", -1, (7, 29, 69, 9), cs | win32con.SS_LEFT])
    s = win32con.WS_TABSTOP | cs
    # 	dlg.append([131, None, 130, (5, 40, 110, 48),
    # 		s | win32con.LBS_NOTIFY | win32con.LBS_SORT | win32con.LBS_NOINTEGRALHEIGHT | win32con.WS_VSCROLL | win32con.WS_BORDER])
    dlg.append(
        [
            "{8E27C92B-1264-101C-8A2F-040224009C02}",
            None,
            131,
            (5, 40, 110, 48),
            win32con.WS_TABSTOP,
        ]
    )

    dlg.append(
        [128, "OK", win32con.IDOK, (124, 5, 50, 14), s | win32con.BS_DEFPUSHBUTTON]
    )
    s = win32con.BS_PUSHBUTTON | s
    dlg.append([128, "Cancel", win32con.IDCANCEL, (124, 22, 50, 14), s])
    dlg.append([128, "&Help", 100, (124, 74, 50, 14), s])

    return dlg


def test1():
    win32ui.CreateDialogIndirect(MakeDlgTemplate()).DoModal()


def test2():
    dialog.Dialog(MakeDlgTemplate()).DoModal()


def test3():
    dlg = win32ui.LoadDialogResource(win32ui.IDD_SET_TABSTOPS)
    dlg[0][0] = "New Dialog Title"
    dlg[0][1] = (80, 20, 161, 60)
    dlg[1][1] = "&Confusion:"
    cs = (
        win32con.WS_CHILD
        | win32con.WS_VISIBLE
        | win32con.WS_TABSTOP
        | win32con.BS_PUSHBUTTON
    )
    dlg.append([128, "&Help", 100, (111, 41, 40, 14), cs])
    dialog.Dialog(dlg).DoModal()


def test4():
    page1 = dialog.PropertyPage(win32ui.LoadDialogResource(win32ui.IDD_PROPDEMO1))
    page2 = dialog.PropertyPage(win32ui.LoadDialogResource(win32ui.IDD_PROPDEMO2))
    ps = dialog.PropertySheet("Property Sheet/Page Demo", None, [page1, page2])
    ps.DoModal()


def testall():
    test1()
    test2()
    test3()
    test4()


if __name__ == "__main__":
    testall()

```


---

## pythonwin/pywin/Demos/fontdemo.py

```python
# Demo of Generic document windows, DC, and Font usage
# by Dave Brennan (brennan@hal.com)

# usage examples:

# >>> from fontdemo import *
# >>> d = FontDemo('Hello, Python')
# >>> f1 = { 'name':'Arial', 'height':36, 'weight':win32con.FW_BOLD}
# >>> d.SetFont(f1)
# >>> f2 = {'name':'Courier New', 'height':24, 'italic':1}
# >>> d.SetFont (f2)

import win32api
import win32con
import win32ui
from pywin.mfc import docview

# font is a dictionary in which the following elements matter:
# (the best matching font to supplied parameters is returned)
#   name		string name of the font as known by Windows
#   size		point size of font in logical units
#   weight		weight of font (win32con.FW_NORMAL, win32con.FW_BOLD)
#   italic		boolean; true if set to anything but None
#   underline	boolean; true if set to anything but None


class FontView(docview.ScrollView):
    def __init__(
        self, doc, text="Python Rules!", font_spec={"name": "Arial", "height": 42}
    ):
        docview.ScrollView.__init__(self, doc)
        self.font = win32ui.CreateFont(font_spec)
        self.text = text
        self.width = self.height = 0
        # set up message handlers
        self.HookMessage(self.OnSize, win32con.WM_SIZE)

    def OnAttachedObjectDeath(self):
        docview.ScrollView.OnAttachedObjectDeath(self)
        del self.font

    def SetFont(self, new_font):
        # Change font on the fly
        self.font = win32ui.CreateFont(new_font)
        # redraw the entire client window
        self.InvalidateRect(None)

    def OnSize(self, params):
        lParam = params[3]
        self.width = win32api.LOWORD(lParam)
        self.height = win32api.HIWORD(lParam)

    def OnPrepareDC(self, dc, printinfo):
        # Set up the DC for forthcoming OnDraw call
        self.SetScrollSizes(win32con.MM_TEXT, (100, 100))
        dc.SetTextColor(win32api.RGB(0, 0, 255))
        dc.SetBkColor(win32api.GetSysColor(win32con.COLOR_WINDOW))
        dc.SelectObject(self.font)
        dc.SetTextAlign(win32con.TA_CENTER | win32con.TA_BASELINE)

    def OnDraw(self, dc):
        if self.width == 0 and self.height == 0:
            left, top, right, bottom = self.GetClientRect()
            self.width = right - left
            self.height = bottom - top
        x, y = self.width // 2, self.height // 2
        dc.TextOut(x, y, self.text)


def FontDemo():
    # create doc/view
    template = docview.DocTemplate(win32ui.IDR_PYTHONTYPE, None, None, FontView)
    doc = template.OpenDocumentFile(None)
    doc.SetTitle("Font Demo")
    # print("template is ", template, "obj is", template._obj_)
    template.close()
    # print("closed")
    # del template


if __name__ == "__main__":
    import demoutils

    if demoutils.NeedGoodGUI():
        FontDemo()

```


---

## pythonwin/pywin/Demos/guidemo.py

```python
# GUI Demo - just a worker script to invoke all the other demo/test scripts.
import sys

import __main__
import pywin.dialogs.list

demos = [
    ("Font", "import fontdemo;fontdemo.FontDemo()"),
    ("Open GL Demo", "import openGLDemo;openGLDemo.test()"),
    ("Threaded GUI", "import threadedgui;threadedgui.ThreadedDemo()"),
    ("Tree View Demo", "import hiertest;hiertest.demoboth()"),
    ("3-Way Splitter Window", "import splittst;splittst.demo()"),
    ("Custom Toolbars and Tooltips", "import toolbar;toolbar.test()"),
    ("Progress Bar", "import progressbar;progressbar.demo()"),
    ("Slider Control", "import sliderdemo;sliderdemo.demo()"),
    ("Dynamic window creation", "import createwin;createwin.demo()"),
    ("Various Dialog demos", "import dlgtest;dlgtest.demo()"),
    ("OCX Control Demo", "from ocx import ocxtest;ocxtest.demo()"),
    ("OCX Serial Port Demo", "from ocx import ocxserialtest; ocxserialtest.test()"),
    (
        "Internet Explorer Control Demo",
        'from ocx import webbrowser; webbrowser.Demo("https://www.python.org")',
    ),
]


def _exec_demo(cmd):
    try:
        exec(cmd)
    except Exception as error:
        print(f"Demo of {cmd} failed - {type(error)}:{error}")


def demo():
    if "/go" in sys.argv:
        for name, cmd in demos:
            _exec_demo(cmd)
        return

    # Otherwise allow the user to select the demo to run
    while True:
        rc = pywin.dialogs.list.SelectFromLists("Select a Demo", demos, ["Demo Title"])
        if rc is None:
            break
        title, cmd = demos[rc]
        _exec_demo(cmd)


if __name__ == __main__.__name__:
    import demoutils

    if demoutils.NeedGoodGUI():
        demo()

```


---

## pythonwin/pywin/Demos/hiertest.py

```python
import os

import commctrl
import win32ui
from pywin.mfc import docview, window
from pywin.tools import hierlist


# directory listbox
# This has obvious limitations - doesn't track subdirs, etc.  Demonstrates
# simple use of Python code for querying the tree as needed.
# Only use strings, and lists of strings (from curdir())
class DirHierList(hierlist.HierList):
    def __init__(self, root, listBoxID=win32ui.IDC_LIST1):
        hierlist.HierList.__init__(self, root, win32ui.IDB_HIERFOLDERS, listBoxID)

    def GetText(self, item):
        return os.path.basename(item)

    def GetSubList(self, item):
        if os.path.isdir(item):
            ret = [os.path.join(item, fname) for fname in os.listdir(item)]
        else:
            ret = None
        return ret

    # if the item is a dir, it is expandable.
    def IsExpandable(self, item):
        return os.path.isdir(item)

    def GetSelectedBitmapColumn(self, item):
        return self.GetBitmapColumn(item) + 6  # Use different color for selection


class TestDocument(docview.Document):
    def __init__(self, template):
        docview.Document.__init__(self, template)
        self.hierlist = hierlist.HierListWithItems(
            HLIFileDir("\\"), win32ui.IDB_HIERFOLDERS, win32ui.AFX_IDW_PANE_FIRST
        )


class HierListView(docview.TreeView):
    def OnInitialUpdate(self):
        rc = self._obj_.OnInitialUpdate()
        self.hierList = self.GetDocument().hierlist
        self.hierList.HierInit(self.GetParent())
        self.hierList.SetStyle(
            commctrl.TVS_HASLINES | commctrl.TVS_LINESATROOT | commctrl.TVS_HASBUTTONS
        )
        return rc


class HierListFrame(window.MDIChildWnd):
    pass


def GetTestRoot():
    tree1 = ("Tree 1", [("Item 1", "Item 1 data"), "Item 2", 3])
    tree2 = ("Tree 2", [("Item 2.1", "Item 2 data"), "Item 2.2", 2.3])
    return ("Root", [tree1, tree2, "Item 3"])


def demoboth():
    template = docview.DocTemplate(
        win32ui.IDR_PYTHONTYPE, TestDocument, HierListFrame, HierListView
    )
    template.OpenDocumentFile(None).SetTitle("Hierlist demo")

    demomodeless()


def demomodeless():
    testList2 = DirHierList("\\")
    dlg = hierlist.HierDialog("hier list test", testList2)
    dlg.CreateWindow()


def demodlg():
    testList2 = DirHierList("\\")
    dlg = hierlist.HierDialog("hier list test", testList2)
    dlg.DoModal()


def demo():
    template = docview.DocTemplate(
        win32ui.IDR_PYTHONTYPE, TestDocument, HierListFrame, HierListView
    )
    template.OpenDocumentFile(None).SetTitle("Hierlist demo")


#
# Demo/Test for HierList items.
#
# Easy to make a better directory program.
#
class HLIFileDir(hierlist.HierListItem):
    def __init__(self, filename):
        self.filename = filename
        hierlist.HierListItem.__init__(self)

    def GetText(self):
        try:
            return f"{os.path.basename(self.filename):<20} {os.stat(self.filename)[6]} bytes"
        except OSError as details:
            return f"{self.filename:<20} - {details[1]}"

    def IsExpandable(self):
        return os.path.isdir(self.filename)

    def GetSubList(self):
        ret = []
        for newname in os.listdir(self.filename):
            if newname not in (".", ".."):
                ret.append(HLIFileDir(os.path.join(self.filename, newname)))
        return ret


def demohli():
    template = docview.DocTemplate(
        win32ui.IDR_PYTHONTYPE,
        TestDocument,
        hierlist.HierListFrame,
        hierlist.HierListView,
    )
    template.OpenDocumentFile(None).SetTitle("Hierlist demo")


if __name__ == "__main__":
    import demoutils

    if demoutils.HaveGoodGUI():
        demoboth()
    else:
        demodlg()

```


---

## pythonwin/pywin/Demos/menutest.py

```python
# Run this as a python script, to gray "close" off the edit window system menu.
import win32con
from pywin.framework import interact

if __name__ == "__main__":
    import demoutils

    if demoutils.NeedGoodGUI():
        win = interact.edit.currentView.GetParent()
        menu = win.GetSystemMenu()
        id = menu.GetMenuItemID(6)
        menu.EnableMenuItem(id, win32con.MF_BYCOMMAND | win32con.MF_GRAYED)
        print("The interactive window's 'Close' menu item is now disabled.")

```


---

## pythonwin/pywin/Demos/objdoc.py

```python
# This is a sample file, and shows the basic framework for using an "Object" based
# document, rather than a "filename" based document.
# This is referenced by the Pythonwin .html documentation.

# In the example below, the OpenObject() method is used instead of OpenDocumentFile,
# and all the core MFC document open functionality is retained.

import win32ui
from pywin.mfc import docview


class object_template(docview.DocTemplate):
    def __init__(self):
        docview.DocTemplate.__init__(self, None, None, None, object_view)

    def OpenObject(self, object):  # Use this instead of OpenDocumentFile.
        # Look for existing open document
        for doc in self.GetDocumentList():
            print("document is ", doc)
            if doc.object is object:
                doc.GetFirstView().ActivateFrame()
                return doc
        # not found - new one.
        doc = object_document(self, object)
        frame = self.CreateNewFrame(doc)
        doc.OnNewDocument()
        doc.SetTitle(str(object))
        self.InitialUpdateFrame(frame, doc)
        return doc


class object_document(docview.Document):
    def __init__(self, template, object):
        docview.Document.__init__(self, template)
        self.object = object

    def OnOpenDocument(self, name):
        raise RuntimeError("Should not be called if template strings set up correctly")
        return 0


class object_view(docview.EditView):
    def OnInitialUpdate(self):
        self.ReplaceSel(f"Object is {self.GetDocument().object!r}")


def demo():
    t = object_template()
    d = t.OpenObject(win32ui)
    return (t, d)


if __name__ == "__main__":
    import demoutils

    if demoutils.NeedGoodGUI():
        demo()

```


---

## pythonwin/pywin/Demos/ocx/demoutils.py

```python
# Utilities for the demos

import sys

import win32api
import win32con
import win32ui

NotScriptMsg = """\
This demo program is not designed to be run as a Script, but is
probably used by some other test program.  Please try another demo.
"""

NeedGUIMsg = """\
This demo program can only be run from inside of Pythonwin

You must start Pythonwin, and select 'Run' from the toolbar or File menu
"""


NeedAppMsg = """\
This demo program is a 'Pythonwin Application'.

It is more demo code than an example of Pythonwin's capabilities.

To run it, you must execute the command:
Pythonwin.exe /app "%s"

Would you like to execute it now?
"""


def NotAScript():
    import win32ui

    win32ui.MessageBox(NotScriptMsg, "Demos")


def NeedGoodGUI():
    from pywin.framework.app import HaveGoodGUI

    rc = HaveGoodGUI()
    if not rc:
        win32ui.MessageBox(NeedGUIMsg, "Demos")
    return rc


def NeedApp():
    import win32ui

    rc = win32ui.MessageBox(NeedAppMsg % sys.argv[0], "Demos", win32con.MB_YESNO)
    if rc == win32con.IDYES:
        try:
            parent = win32ui.GetMainFrame().GetSafeHwnd()
            win32api.ShellExecute(
                parent, None, "Pythonwin.exe", '/app "%s"' % sys.argv[0], None, 1
            )
        except win32api.error as details:
            win32ui.MessageBox("Error executing command - %s" % (details), "Demos")


if __name__ == "__main__":
    NotAScript()

```


---

## pythonwin/pywin/Demos/ocx/flash.py

```python
# By Bradley Schatz
# simple flash/python application demonstrating bidirectional
# communicaion between flash and python. Click the sphere to see
# behavior. Uses Bounce.swf from FlashBounce.zip, available from
# https://cspages.ucalgary.ca/~saul/vb_examples/tutorial12/

# Update to the path of the .swf file (note it could be a true URL)
flash_url = "c:\\bounce.swf"

import sys

import regutil
import win32api
import win32con
import win32ui
from pywin.mfc import activex, window
from win32com.client import gencache

FlashModule = gencache.EnsureModule("{D27CDB6B-AE6D-11CF-96B8-444553540000}", 0, 1, 0)

if FlashModule is None:
    raise ImportError("Flash does not appear to be installed.")


class MyFlashComponent(activex.Control, FlashModule.ShockwaveFlash):
    def __init__(self):
        activex.Control.__init__(self)
        FlashModule.ShockwaveFlash.__init__(self)
        self.x = 50
        self.y = 50
        self.angle = 30
        self.started = 0

    def OnFSCommand(self, command, args):
        print("FSCommend", command, args)
        self.x += 20
        self.y += 20
        self.angle += 20
        if self.x > 200 or self.y > 200:
            self.x = 0
            self.y = 0
        if self.angle > 360:
            self.angle = 0
        self.SetVariable("xVal", self.x)
        self.SetVariable("yVal", self.y)
        self.SetVariable("angle", self.angle)
        self.TPlay("_root.mikeBall")

    def OnProgress(self, percentDone):
        print("PercentDone", percentDone)

    def OnReadyStateChange(self, newState):
        # 0=Loading, 1=Uninitialized, 2=Loaded, 3=Interactive, 4=Complete
        print("State", newState)


class BrowserFrame(window.MDIChildWnd):
    def __init__(self, url=None):
        if url is None:
            self.url = regutil.GetRegisteredHelpFile("Main Python Documentation")
        else:
            self.url = url
        pass  # Don't call base class doc/view version...

    def Create(self, title, rect=None, parent=None):
        style = win32con.WS_CHILD | win32con.WS_VISIBLE | win32con.WS_OVERLAPPEDWINDOW
        self._obj_ = win32ui.CreateMDIChild()
        self._obj_.AttachObject(self)
        self._obj_.CreateWindow(None, title, style, rect, parent)
        rect = self.GetClientRect()
        rect = (0, 0, rect[2] - rect[0], rect[3] - rect[1])
        self.ocx = MyFlashComponent()
        self.ocx.CreateControl(
            "Flash Player", win32con.WS_VISIBLE | win32con.WS_CHILD, rect, self, 1000
        )
        self.ocx.LoadMovie(0, flash_url)
        self.ocx.Play()
        self.HookMessage(self.OnSize, win32con.WM_SIZE)

    def OnSize(self, params):
        rect = self.GetClientRect()
        rect = (0, 0, rect[2] - rect[0], rect[3] - rect[1])
        self.ocx.SetWindowPos(0, rect, 0)


def Demo():
    url = None
    if len(sys.argv) > 1:
        url = win32api.GetFullPathName(sys.argv[1])
    f = BrowserFrame(url)
    f.Create("Flash Player")


if __name__ == "__main__":
    Demo()

```


---

## pythonwin/pywin/Demos/ocx/msoffice.py

```python
# This demo uses some of the Microsoft Office components.
#
# It was taken from an MSDN article showing how to embed excel.
# It is not comlpete yet, but it _does_ show an Excel spreadsheet in a frame!
#

import win32con
import win32ui
import win32uiole
from pywin.mfc import activex, docview, object, window
from win32com.client import gencache


class OleClientItem(object.CmdTarget):
    def __init__(self, doc):
        object.CmdTarget.__init__(self, win32uiole.CreateOleClientItem(doc))

    def OnGetItemPosition(self):
        # For now return a hard-coded rect.
        return (10, 10, 210, 210)

    def OnActivate(self):
        # Allow only one inplace activate item per frame
        view = self.GetActiveView()
        item = self.GetDocument().GetInPlaceActiveItem(view)
        if item is not None and item._obj_ != self._obj_:
            item.Close()
        self._obj_.OnActivate()

    def OnChange(self, oleNotification, dwParam):
        self._obj_.OnChange(oleNotification, dwParam)
        self.GetDocument().UpdateAllViews(None)

    def OnChangeItemPosition(self, rect):
        # During in-place activation CEmbed_ExcelCntrItem::OnChangeItemPosition
        #  is called by the server to change the position of the in-place
        #  window.  Usually, this is a result of the data in the server
        #  document changing such that the extent has changed or as a result
        #  of in-place resizing.
        #
        # The default here is to call the base class, which will call
        #  COleClientItem::SetItemRects to move the item
        #  to the new position.
        if not self._obj_.OnChangeItemPosition(self, rect):
            return 0

        # TODO: update any cache you may have of the item's rectangle/extent
        return 1


class OleDocument(object.CmdTarget):
    def __init__(self, template):
        object.CmdTarget.__init__(self, win32uiole.CreateOleDocument(template))
        self.EnableCompoundFile()


class ExcelView(docview.ScrollView):
    def OnInitialUpdate(self):
        self.HookMessage(self.OnSetFocus, win32con.WM_SETFOCUS)
        self.HookMessage(self.OnSize, win32con.WM_SIZE)

        self.SetScrollSizes(win32con.MM_TEXT, (100, 100))
        rc = self._obj_.OnInitialUpdate()
        self.EmbedExcel()
        return rc

    def EmbedExcel(self):
        doc = self.GetDocument()
        self.clientItem = OleClientItem(doc)
        self.clientItem.CreateNewItem("Excel.Sheet")
        self.clientItem.DoVerb(-1, self)
        doc.UpdateAllViews(None)

    def OnDraw(self, dc):
        doc = self.GetDocument()
        pos = doc.GetStartPosition()
        clientItem, pos = doc.GetNextItem(pos)
        clientItem.Draw(dc, (10, 10, 210, 210))

    # Special handling of OnSetFocus and OnSize are required for a container
    #  when an object is being edited in-place.
    def OnSetFocus(self, msg):
        item = self.GetDocument().GetInPlaceActiveItem(self)
        if (
            item is not None
            and item.GetItemState() == win32uiole.COleClientItem_activeUIState
        ):
            wnd = item.GetInPlaceWindow()
            if wnd is not None:
                wnd.SetFocus()
            return 0  # Don't get the base version called.
        return 1  # Call the base version.

    def OnSize(self, params):
        item = self.GetDocument().GetInPlaceActiveItem(self)
        if item is not None:
            item.SetItemRects()
        return 1  # do call the base!


class OleTemplate(docview.DocTemplate):
    def __init__(
        self, resourceId=None, MakeDocument=None, MakeFrame=None, MakeView=None
    ):
        if MakeDocument is None:
            MakeDocument = OleDocument
        if MakeView is None:
            MakeView = ExcelView
        docview.DocTemplate.__init__(
            self, resourceId, MakeDocument, MakeFrame, MakeView
        )


class WordFrame(window.MDIChildWnd):
    def __init__(self, doc=None):
        self._obj_ = win32ui.CreateMDIChild()
        self._obj_.AttachObject(self)
        # Don't call base class doc/view version...

    def Create(self, title, rect=None, parent=None):
        WordModule = gencache.EnsureModule(
            "{00020905-0000-0000-C000-000000000046}", 1033, 8, 0
        )
        if WordModule is None:
            raise ImportError(
                "Microsoft Word version 8 does not appear to be installed."
            )

        # WordModule.Word doesn't exist in WordModule, WordModule.Words does, but CreateControl still fails
        class MyWordControl(activex.Control, WordModule.Word): ...

        style = win32con.WS_CHILD | win32con.WS_VISIBLE | win32con.WS_OVERLAPPEDWINDOW
        self._obj_.CreateWindow(None, title, style, rect, parent)

        rect = self.GetClientRect()
        rect = (0, 0, rect[2] - rect[0], rect[3] - rect[1])
        self.ocx = MyWordControl()
        self.ocx.CreateControl(
            "Microsoft Word", win32con.WS_VISIBLE | win32con.WS_CHILD, rect, self, 20000
        )


def Demo():
    import sys

    import win32api

    docName = None
    if len(sys.argv) > 1:
        docName = win32api.GetFullPathName(sys.argv[1])
    OleTemplate().OpenDocumentFile(docName)

    # ActiveX not currently working
    # f = WordFrame(docName)
    # f.Create("Microsoft Office")


if __name__ == "__main__":
    Demo()

```


---

## pythonwin/pywin/Demos/ocx/ocxserialtest.py

```python
# ocxserialtest.py
#
# Sample that uses the mscomm OCX to talk to a serial
# device.

# Very simple -  queries a modem for ATI responses

import pythoncom
import win32con
import win32ui
from pywin.mfc import activex, dialog
from win32com.client import gencache

SERIAL_SETTINGS = "19200,n,8,1"
SERIAL_PORT = 2

win32ui.DoWaitCursor(1)
serialModule = gencache.EnsureModule("{648A5603-2C6E-101B-82B6-000000000014}", 0, 1, 1)
win32ui.DoWaitCursor(0)
if serialModule is None:
    raise ImportError("MS COMM Control does not appear to be installed on the PC")


def MakeDlgTemplate():
    style = (
        win32con.DS_MODALFRAME
        | win32con.WS_POPUP
        | win32con.WS_VISIBLE
        | win32con.WS_CAPTION
        | win32con.WS_SYSMENU
        | win32con.DS_SETFONT
    )
    cs = win32con.WS_CHILD | win32con.WS_VISIBLE
    dlg = [
        ["Very Basic Terminal", (0, 0, 350, 180), style, None, (8, "MS Sans Serif")],
    ]
    s = win32con.WS_TABSTOP | cs
    dlg.append(
        [
            "RICHEDIT",
            None,
            132,
            (5, 5, 340, 170),
            s
            | win32con.ES_WANTRETURN
            | win32con.ES_MULTILINE
            | win32con.ES_AUTOVSCROLL
            | win32con.WS_VSCROLL,
        ]
    )
    return dlg


####################################
#
# Serial Control
#
class MySerialControl(activex.Control, serialModule.MSComm):
    def __init__(self, parent):
        activex.Control.__init__(self)
        serialModule.MSComm.__init__(self)
        self.parent = parent

    def OnComm(self):
        self.parent.OnComm()


class TestSerDialog(dialog.Dialog):
    def __init__(self, *args):
        dialog.Dialog.__init__(*(self,) + args)
        self.olectl = None

    def OnComm(self):
        event = self.olectl.CommEvent
        if event == serialModule.OnCommConstants.comEvReceive:
            self.editwindow.ReplaceSel(self.olectl.Input)

    def OnKey(self, key):
        if self.olectl:
            self.olectl.Output = chr(key)

    def OnInitDialog(self):
        rc = dialog.Dialog.OnInitDialog(self)
        self.editwindow = self.GetDlgItem(132)
        self.editwindow.HookAllKeyStrokes(self.OnKey)

        self.olectl = MySerialControl(self)
        try:
            self.olectl.CreateControl(
                "OCX",
                win32con.WS_TABSTOP | win32con.WS_VISIBLE,
                (7, 43, 500, 300),
                self._obj_,
                131,
            )
        except win32ui.error:
            self.MessageBox("The Serial Control could not be created")
            self.olectl = None
            self.EndDialog(win32con.IDCANCEL)
        if self.olectl:
            self.olectl.Settings = SERIAL_SETTINGS
            self.olectl.CommPort = SERIAL_PORT
            self.olectl.RThreshold = 1
            try:
                self.olectl.PortOpen = 1
            except pythoncom.com_error as details:
                print(
                    "Could not open the specified serial port - %s"
                    % (details.excepinfo[2])
                )
                self.EndDialog(win32con.IDCANCEL)
        return rc

    def OnDestroy(self, msg):
        if self.olectl:
            try:
                self.olectl.PortOpen = 0
            except pythoncom.com_error as details:
                print("Error closing port - %s" % (details.excepinfo[2]))
        return dialog.Dialog.OnDestroy(self, msg)


def test():
    d = TestSerDialog(MakeDlgTemplate())
    d.DoModal()


if __name__ == "__main__":
    import demoutils

    if demoutils.NeedGoodGUI():
        test()

```


---

## pythonwin/pywin/Demos/ocx/ocxtest.py

```python
# OCX Tester for Pythonwin
#
# This file _is_ ready to run.  All that is required is that the OCXs being tested
# are installed on your machine.
#
# The .py files behind the OCXs will be automatically generated and imported.

import glob
import os

import win32api
import win32con
import win32ui
from pywin.mfc import activex, dialog, window
from win32com.client import gencache


def MakeDlgTemplate():
    style = (
        win32con.DS_MODALFRAME
        | win32con.WS_POPUP
        | win32con.WS_VISIBLE
        | win32con.WS_CAPTION
        | win32con.WS_SYSMENU
        | win32con.DS_SETFONT
    )
    cs = win32con.WS_CHILD | win32con.WS_VISIBLE
    dlg = [
        ["OCX Demos", (0, 0, 350, 350), style, None, (8, "MS Sans Serif")],
    ]
    s = win32con.WS_TABSTOP | cs
    # 	dlg.append([131, None, 130, (5, 40, 110, 48),
    # 		s | win32con.LBS_NOTIFY | win32con.LBS_SORT | win32con.LBS_NOINTEGRALHEIGHT | win32con.WS_VSCROLL | win32con.WS_BORDER])
    # 	dlg.append(["{8E27C92B-1264-101C-8A2F-040224009C02}", None, 131, (5, 40, 110, 48),win32con.WS_TABSTOP])

    dlg.append(
        [128, "About", win32con.IDOK, (124, 5, 50, 14), s | win32con.BS_DEFPUSHBUTTON]
    )
    s = win32con.BS_PUSHBUTTON | s
    dlg.append([128, "Close", win32con.IDCANCEL, (124, 22, 50, 14), s])

    return dlg


####################################
#
# Calendar test code
#


def GetTestCalendarClass():
    global calendarParentModule
    win32ui.DoWaitCursor(1)
    calendarParentModule = gencache.EnsureModule(
        "{8E27C92E-1264-101C-8A2F-040224009C02}", 0, 7, 0
    )
    win32ui.DoWaitCursor(0)
    if calendarParentModule is None:
        return None

    class TestCalDialog(dialog.Dialog):
        def OnInitDialog(self):
            class MyCal(activex.Control, calendarParentModule.Calendar):
                def OnAfterUpdate(self):
                    print("OnAfterUpdate")

                def OnClick(self):
                    print("OnClick")

                def OnDblClick(self):
                    print("OnDblClick")

                def OnKeyDown(self, KeyCode, Shift):
                    print("OnKeyDown", KeyCode, Shift)

                def OnKeyPress(self, KeyAscii):
                    print("OnKeyPress", KeyAscii)

                def OnKeyUp(self, KeyCode, Shift):
                    print("OnKeyUp", KeyCode, Shift)

                def OnBeforeUpdate(self, Cancel):
                    print("OnBeforeUpdate", Cancel)

                def OnNewMonth(self):
                    print("OnNewMonth")

                def OnNewYear(self):
                    print("OnNewYear")

            rc = dialog.Dialog.OnInitDialog(self)
            self.olectl = MyCal()
            try:
                self.olectl.CreateControl(
                    "OCX",
                    win32con.WS_TABSTOP | win32con.WS_VISIBLE,
                    (7, 43, 500, 300),
                    self._obj_,
                    131,
                )
            except win32ui.error:
                self.MessageBox("The Calendar Control could not be created")
                self.olectl = None
                self.EndDialog(win32con.IDCANCEL)

            return rc

        def OnOK(self):
            self.olectl.AboutBox()

    return TestCalDialog


####################################
#
# Video Control
#
def GetTestVideoModule():
    global videoControlModule, videoControlFileName
    win32ui.DoWaitCursor(1)
    videoControlModule = gencache.EnsureModule(
        "{05589FA0-C356-11CE-BF01-00AA0055595A}", 0, 2, 0
    )
    win32ui.DoWaitCursor(0)
    if videoControlModule is None:
        return None
    fnames = glob.glob(os.path.join(win32api.GetWindowsDirectory(), "*.avi"))
    if not fnames:
        print("No AVI files available in system directory")
        return None
    videoControlFileName = fnames[0]
    return videoControlModule


def GetTestVideoDialogClass():
    if GetTestVideoModule() is None:
        return None

    class TestVideoDialog(dialog.Dialog):
        def OnInitDialog(self):
            rc = dialog.Dialog.OnInitDialog(self)
            try:
                self.olectl = activex.MakeControlInstance(
                    videoControlModule.ActiveMovie
                )
                self.olectl.CreateControl(
                    "",
                    win32con.WS_TABSTOP | win32con.WS_VISIBLE,
                    (7, 43, 500, 300),
                    self._obj_,
                    131,
                )
            except win32ui.error:
                self.MessageBox("The Video Control could not be created")
                self.olectl = None
                self.EndDialog(win32con.IDCANCEL)
                return

            self.olectl.FileName = videoControlFileName
            # 			self.olectl.Run()
            return rc

        def OnOK(self):
            self.olectl.AboutBox()

    return TestVideoDialog


###############
#
# An OCX in an MDI Frame
#
class OCXFrame(window.MDIChildWnd):
    def __init__(self):
        pass  # Don't call base class doc/view version...

    def Create(self, controlClass, title, rect=None, parent=None):
        style = win32con.WS_CHILD | win32con.WS_VISIBLE | win32con.WS_OVERLAPPEDWINDOW
        self._obj_ = win32ui.CreateMDIChild()
        self._obj_.AttachObject(self)
        self._obj_.CreateWindow(None, title, style, rect, parent)

        rect = self.GetClientRect()
        rect = (0, 0, rect[2] - rect[0], rect[3] - rect[1])
        self.ocx = controlClass()
        self.ocx.CreateControl(
            "", win32con.WS_VISIBLE | win32con.WS_CHILD, rect, self, 1000
        )


def MDITest():
    calendarParentModule = gencache.EnsureModule(
        "{8E27C92E-1264-101C-8A2F-040224009C02}", 0, 7, 0
    )

    class MyCal(activex.Control, calendarParentModule.Calendar):
        def OnAfterUpdate(self):
            print("OnAfterUpdate")

        def OnClick(self):
            print("OnClick")

    f = OCXFrame()
    f.Create(MyCal, "Calendar Test")


def test1():
    klass = GetTestCalendarClass()
    if klass is None:
        print(
            "Can not test the MSAccess Calendar control - it does not appear to be installed"
        )
        return

    d = klass(MakeDlgTemplate())
    d.DoModal()


def test2():
    klass = GetTestVideoDialogClass()
    if klass is None:
        print("Can not test the Video OCX - it does not appear to be installed,")
        print("or no AVI files can be found.")
        return
    d = klass(MakeDlgTemplate())
    d.DoModal()
    d = None


def testall():
    test1()
    test2()


def demo():
    testall()


if __name__ == "__main__":
    import demoutils

    if demoutils.NeedGoodGUI():
        testall()

```


---

## pythonwin/pywin/Demos/ocx/webbrowser.py

```python
# This demo uses the Internet Explorer Web Browser control.

# It catches an "OnNavigate" event, and updates the frame title.
# (event stuff by Neil Hodgson)

import sys

import regutil
import win32api
import win32con
import win32ui
from pywin.mfc import activex, window
from win32com.client import gencache

WebBrowserModule = gencache.EnsureModule(
    "{EAB22AC0-30C1-11CF-A7EB-0000C05BAE0B}", 0, 1, 1
)
if WebBrowserModule is None:
    raise ImportError("Internet Explorer does not appear to be installed.")


class MyWebBrowser(activex.Control, WebBrowserModule.WebBrowser):
    def OnBeforeNavigate2(
        self, pDisp, URL, Flags, TargetFrameName, PostData, Headers, Cancel
    ):
        self.GetParent().OnNavigate(URL)
        # print("BeforeNavigate2", pDisp, URL, Flags, TargetFrameName, PostData, Headers, Cancel)


class BrowserFrame(window.MDIChildWnd):
    def __init__(self, url=None):
        if url is None:
            self.url = regutil.GetRegisteredHelpFile("Main Python Documentation")
            if self.url is None:
                self.url = "https://www.python.org"
        else:
            self.url = url
        pass  # Don't call base class doc/view version...

    def Create(self, title, rect=None, parent=None):
        style = win32con.WS_CHILD | win32con.WS_VISIBLE | win32con.WS_OVERLAPPEDWINDOW
        self._obj_ = win32ui.CreateMDIChild()
        self._obj_.AttachObject(self)
        self._obj_.CreateWindow(None, title, style, rect, parent)
        rect = self.GetClientRect()
        rect = (0, 0, rect[2] - rect[0], rect[3] - rect[1])
        self.ocx = MyWebBrowser()
        self.ocx.CreateControl(
            "Web Browser", win32con.WS_VISIBLE | win32con.WS_CHILD, rect, self, 1000
        )
        self.ocx.Navigate(self.url)
        self.HookMessage(self.OnSize, win32con.WM_SIZE)

    def OnSize(self, params):
        rect = self.GetClientRect()
        rect = (0, 0, rect[2] - rect[0], rect[3] - rect[1])
        self.ocx.SetWindowPos(0, rect, 0)

    def OnNavigate(self, url):
        title = f"Web Browser - {url}"
        self.SetWindowText(title)


def Demo(url=None):
    if url is None and len(sys.argv) > 1:
        url = win32api.GetFullPathName(sys.argv[1])
    f = BrowserFrame(url)
    f.Create("Web Browser")


if __name__ == "__main__":
    Demo()

```


---

## pythonwin/pywin/Demos/openGLDemo.py

```python
# Ported from the win32 and MFC OpenGL Samples.

import sys

try:
    from OpenGL.GL import (
        GL_COLOR_BUFFER_BIT,
        GL_DEPTH_BUFFER_BIT,
        GL_DEPTH_TEST,
        GL_MODELVIEW,
        GL_PROJECTION,
        GL_QUAD_STRIP,
        GL_QUADS,
        GL_TRIANGLE_FAN,
        glBegin,
        glClear,
        glClearColor,
        glClearDepth,
        glColor3f,
        glEnable,
        glEnd,
        glFinish,
        glLoadIdentity,
        glMatrixMode,
        glPopMatrix,
        glPushMatrix,
        glRotatef,
        glTranslatef,
        glVertex3f,
        glViewport,
    )
    from OpenGL.GLU import (
        GLU_FILL,
        GLU_SMOOTH,
        gluCylinder,
        gluNewQuadric,
        gluPerspective,
        gluQuadricDrawStyle,
        gluQuadricNormals,
    )
    from OpenGL.WGL import (
        PIXELFORMATDESCRIPTOR,
        ChoosePixelFormat,
        DescribePixelFormat,
        GetPixelFormat,
        SetPixelFormat,
        SwapBuffers,
        wglCreateContext,
        wglDeleteContext,
        wglGetCurrentContext,
        wglGetCurrentDC,
        wglMakeCurrent,
    )
except ImportError:
    print("The OpenGL extensions do not appear to be installed.")
    print("This Pythonwin demo can not run")
    sys.exit(1)

import timer
import win32api
import win32con
import win32ui
from pywin.mfc import docview

PFD_TYPE_RGBA = 0
PFD_TYPE_COLORINDEX = 1
PFD_MAIN_PLANE = 0
PFD_OVERLAY_PLANE = 1
PFD_UNDERLAY_PLANE = -1
PFD_DOUBLEBUFFER = 0x00000001
PFD_STEREO = 0x00000002
PFD_DRAW_TO_WINDOW = 0x00000004
PFD_DRAW_TO_BITMAP = 0x00000008
PFD_SUPPORT_GDI = 0x00000010
PFD_SUPPORT_OPENGL = 0x00000020
PFD_GENERIC_FORMAT = 0x00000040
PFD_NEED_PALETTE = 0x00000080
PFD_NEED_SYSTEM_PALETTE = 0x00000100
PFD_SWAP_EXCHANGE = 0x00000200
PFD_SWAP_COPY = 0x00000400
PFD_SWAP_LAYER_BUFFERS = 0x00000800
PFD_GENERIC_ACCELERATED = 0x00001000
PFD_DEPTH_DONTCARE = 0x20000000
PFD_DOUBLEBUFFER_DONTCARE = 0x40000000
PFD_STEREO_DONTCARE = 0x80000000


# threeto8 = [0, 0o111>>1, 0o222>>1, 0o333>>1, 0o444>>1, 0o555>>1, 0o666>>1, 0o377]
threeto8 = [0, 73 >> 1, 146 >> 1, 219 >> 1, 292 >> 1, 365 >> 1, 438 >> 1, 255]
twoto8 = [0, 0x55, 0xAA, 0xFF]
oneto8 = [0, 255]


def ComponentFromIndex(i, nbits, shift):
    # val = (unsigned char) (i >> shift);
    val = (i >> shift) & 0xF
    if nbits == 1:
        val &= 0x1
        return oneto8[val]
    elif nbits == 2:
        val &= 0x3
        return twoto8[val]
    elif nbits == 3:
        val &= 0x7
        return threeto8[val]
    else:
        return 0


OpenGLViewParent = docview.ScrollView


class OpenGLView(OpenGLViewParent):
    def PreCreateWindow(self, cc):
        self.HookMessage(self.OnSize, win32con.WM_SIZE)
        # An OpenGL window must be created with the following flags and must not
        # include CS_PARENTDC for the class style. Refer to SetPixelFormat
        # documentation in the "Comments" section for further information.
        style = cc[5]
        style |= win32con.WS_CLIPSIBLINGS | win32con.WS_CLIPCHILDREN
        cc = cc[0], cc[1], cc[2], cc[3], cc[4], style, cc[6], cc[7], cc[8]
        cc = self._obj_.PreCreateWindow(cc)
        return cc

    def OnSize(self, params):
        lParam = params[3]
        cx = win32api.LOWORD(lParam)
        cy = win32api.HIWORD(lParam)
        glViewport(0, 0, cx, cy)

        if self.oldrect[2] > cx or self.oldrect[3] > cy:
            self.RedrawWindow()

        self.OnSizeChange(cx, cy)

        self.oldrect = self.oldrect[0], self.oldrect[1], cx, cy

    def OnInitialUpdate(self):
        self.SetScaleToFitSize(
            (100, 100)
        )  # or SetScrollSizes() - A Pythonwin requirement
        return self._obj_.OnInitialUpdate()

    # 		return rc

    def OnCreate(self, cs):
        self.oldrect = self.GetClientRect()
        self._InitContexts()
        self.Init()

    def OnDestroy(self, msg):
        self.Term()
        self._DestroyContexts()
        return OpenGLViewParent.OnDestroy(self, msg)

    def OnDraw(self, dc):
        self.DrawScene()

    def OnEraseBkgnd(self, dc):
        return 1

    # The OpenGL helpers
    def _SetupPixelFormat(self):
        dc = self.dc.GetSafeHdc()
        pfd = PIXELFORMATDESCRIPTOR()
        pfd.dwFlags = PFD_DRAW_TO_WINDOW | PFD_SUPPORT_OPENGL | PFD_DOUBLEBUFFER
        pfd.iPixelType = PFD_TYPE_RGBA
        pfd.cColorBits = 24
        pfd.cDepthBits = 32
        pfd.iLayerType = PFD_MAIN_PLANE
        pixelformat = ChoosePixelFormat(dc, pfd)
        SetPixelFormat(dc, pixelformat, pfd)
        self._CreateRGBPalette(pfd)

    def _CreateRGBPalette(self, pfd):
        hdc = self.dc.GetSafeHdc()
        iPixelFormat = GetPixelFormat(hdc)
        DescribePixelFormat(hdc, iPixelFormat, pfd.nSize, pfd)
        if pfd.dwFlags & PFD_NEED_PALETTE:
            iPixelFormat = 1 << pfd.cColorBits
            pal = []
            for i in range(iPixelFormat):
                this = (
                    ComponentFromIndex(i, pfd.cRedBits, pfd.cRedShift),
                    ComponentFromIndex(i, pfd.cGreenBits, pfd.cGreenShift),
                    ComponentFromIndex(i, pfd.cBlueBits, pfd.cBlueShift),
                    0,
                )
                pal.append(this)
            hpal = win32ui.CreatePalette(pal)
            self.dc.SelectPalette(hpal, 0)
            self.dc.RealizePalette()

    def _InitContexts(self):
        self.dc = self.GetDC()
        self._SetupPixelFormat()
        hrc = wglCreateContext(self.dc.GetSafeHdc())
        wglMakeCurrent(self.dc.GetSafeHdc(), hrc)

    def _DestroyContexts(self):
        hrc = wglGetCurrentContext()
        wglMakeCurrent(0, 0)
        if hrc:
            wglDeleteContext(hrc)

    # The methods to support OpenGL
    def DrawScene(self):
        raise NotImplementedError("You must override this method")

    def Init(self):
        raise NotImplementedError("You must override this method")

    def OnSizeChange(self, cx, cy):
        pass

    def Term(self):
        pass


class TestView(OpenGLView):
    def OnSizeChange(self, right, bottom):
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClearDepth(1.0)
        glEnable(GL_DEPTH_TEST)

        glMatrixMode(GL_PROJECTION)
        if bottom:
            aspect = right / bottom
        else:
            aspect = 0  # When window created!
        glLoadIdentity()
        gluPerspective(45.0, aspect, 3.0, 7.0)
        glMatrixMode(GL_MODELVIEW)

        near_plane = 3.0
        far_plane = 7.0
        maxObjectSize = 3.0
        self.radius = near_plane + maxObjectSize / 2.0

    def Init(self):
        pass

    def DrawScene(self):
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glPushMatrix()
        glTranslatef(0.0, 0.0, -self.radius)

        self._DrawCone()

        self._DrawPyramid()

        glPopMatrix()
        glFinish()

        SwapBuffers(wglGetCurrentDC())

    def _DrawCone(self):
        glColor3f(0.0, 1.0, 0.0)

        glPushMatrix()
        glTranslatef(-1.0, 0.0, 0.0)
        quadObj = gluNewQuadric()
        gluQuadricDrawStyle(quadObj, GLU_FILL)
        gluQuadricNormals(quadObj, GLU_SMOOTH)
        gluCylinder(quadObj, 1.0, 0.0, 1.0, 20, 10)
        # 		gluDeleteQuadric(quadObj);
        glPopMatrix()

    def _DrawPyramid(self):
        glPushMatrix()
        glTranslatef(1.0, 0.0, 0.0)
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(1.0, 0.0, 0.0)
        glVertex3f(0.0, 1.0, 0.0)
        glColor3f(0.0, 1.0, 0.0)
        glVertex3f(-1.0, 0.0, 0.0)
        glColor3f(0.0, 0.0, 1.0)
        glVertex3f(0.0, 0.0, 1.0)
        glColor3f(0.0, 1.0, 0.0)
        glVertex3f(1.0, 0.0, 0.0)
        glEnd()
        glPopMatrix()


class CubeView(OpenGLView):
    def OnSizeChange(self, right, bottom):
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClearDepth(1.0)
        glEnable(GL_DEPTH_TEST)

        glMatrixMode(GL_PROJECTION)
        if bottom:
            aspect = right / bottom
        else:
            aspect = 0  # When window created!
        glLoadIdentity()
        gluPerspective(45.0, aspect, 3.0, 7.0)
        glMatrixMode(GL_MODELVIEW)

        near_plane = 3.0
        far_plane = 7.0
        maxObjectSize = 3.0
        self.radius = near_plane + maxObjectSize / 2.0

    def Init(self):
        self.busy = 0
        self.wAngleY = 10.0
        self.wAngleX = 1.0
        self.wAngleZ = 5.0
        self.timerid = timer.set_timer(150, self.OnTimer)

    def OnTimer(self, id, timeVal):
        self.DrawScene()

    def Term(self):
        timer.kill_timer(self.timerid)

    def DrawScene(self):
        if self.busy:
            return
        self.busy = 1

        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glPushMatrix()

        glTranslatef(0.0, 0.0, -self.radius)
        glRotatef(self.wAngleX, 1.0, 0.0, 0.0)
        glRotatef(self.wAngleY, 0.0, 1.0, 0.0)
        glRotatef(self.wAngleZ, 0.0, 0.0, 1.0)

        self.wAngleX += 1.0
        self.wAngleY += 10.0
        self.wAngleZ += 5.0

        glBegin(GL_QUAD_STRIP)
        glColor3f(1.0, 0.0, 1.0)
        glVertex3f(-0.5, 0.5, 0.5)

        glColor3f(1.0, 0.0, 0.0)
        glVertex3f(-0.5, -0.5, 0.5)

        glColor3f(1.0, 1.0, 1.0)
        glVertex3f(0.5, 0.5, 0.5)

        glColor3f(1.0, 1.0, 0.0)
        glVertex3f(0.5, -0.5, 0.5)

        glColor3f(0.0, 1.0, 1.0)
        glVertex3f(0.5, 0.5, -0.5)

        glColor3f(0.0, 1.0, 0.0)
        glVertex3f(0.5, -0.5, -0.5)

        glColor3f(0.0, 0.0, 1.0)
        glVertex3f(-0.5, 0.5, -0.5)

        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(-0.5, -0.5, -0.5)

        glColor3f(1.0, 0.0, 1.0)
        glVertex3f(-0.5, 0.5, 0.5)

        glColor3f(1.0, 0.0, 0.0)
        glVertex3f(-0.5, -0.5, 0.5)

        glEnd()

        glBegin(GL_QUADS)
        glColor3f(1.0, 0.0, 1.0)
        glVertex3f(-0.5, 0.5, 0.5)

        glColor3f(1.0, 1.0, 1.0)
        glVertex3f(0.5, 0.5, 0.5)

        glColor3f(0.0, 1.0, 1.0)
        glVertex3f(0.5, 0.5, -0.5)

        glColor3f(0.0, 0.0, 1.0)
        glVertex3f(-0.5, 0.5, -0.5)
        glEnd()

        glBegin(GL_QUADS)
        glColor3f(1.0, 0.0, 0.0)
        glVertex3f(-0.5, -0.5, 0.5)

        glColor3f(1.0, 1.0, 0.0)
        glVertex3f(0.5, -0.5, 0.5)

        glColor3f(0.0, 1.0, 0.0)
        glVertex3f(0.5, -0.5, -0.5)

        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(-0.5, -0.5, -0.5)
        glEnd()

        glPopMatrix()

        glFinish()
        SwapBuffers(wglGetCurrentDC())

        self.busy = 0


def test():
    template = docview.DocTemplate(None, None, None, CubeView)
    # 	template = docview.DocTemplate(None, None, None, TestView )
    template.OpenDocumentFile(None)


if __name__ == "__main__":
    test()

```


---

## pythonwin/pywin/Demos/progressbar.py

```python
#
# Progress bar control example
#
# 	PyCProgressCtrl encapsulates the MFC CProgressCtrl class.  To use it,
# 	you:
#
# 	- Create the control with win32ui.CreateProgressCtrl()
# 	- Create the control window with PyCProgressCtrl.CreateWindow()
# 	- Initialize the range if you want it to be other than (0, 100) using
# 	  PyCProgressCtrl.SetRange()
# 	- Either:
# 	  - Set the step size with PyCProgressCtrl.SetStep(), and
# 	  - Increment using PyCProgressCtrl.StepIt()
# 	  or:
# 	  - Set the amount completed using PyCProgressCtrl.SetPos()
#
# Example and progress bar code courtesy of KDL Technologies, Ltd., Hong Kong SAR, China.
#

import win32con
import win32ui
from pywin.mfc import dialog


def MakeDlgTemplate():
    style = (
        win32con.DS_MODALFRAME
        | win32con.WS_POPUP
        | win32con.WS_VISIBLE
        | win32con.WS_CAPTION
        | win32con.WS_SYSMENU
        | win32con.DS_SETFONT
    )
    cs = win32con.WS_CHILD | win32con.WS_VISIBLE

    w = 215
    h = 36

    dlg = [
        [
            "Progress bar control example",
            (0, 0, w, h),
            style,
            None,
            (8, "MS Sans Serif"),
        ],
    ]

    s = win32con.WS_TABSTOP | cs

    dlg.append(
        [
            128,
            "Tick",
            win32con.IDOK,
            (10, h - 18, 50, 14),
            s | win32con.BS_DEFPUSHBUTTON,
        ]
    )

    dlg.append(
        [
            128,
            "Cancel",
            win32con.IDCANCEL,
            (w - 60, h - 18, 50, 14),
            s | win32con.BS_PUSHBUTTON,
        ]
    )

    return dlg


class TestDialog(dialog.Dialog):
    def OnInitDialog(self):
        rc = dialog.Dialog.OnInitDialog(self)
        self.pbar = win32ui.CreateProgressCtrl()
        self.pbar.CreateWindow(
            win32con.WS_CHILD | win32con.WS_VISIBLE, (10, 10, 310, 24), self, 1001
        )
        # self.pbar.SetStep (5)
        self.progress = 0
        self.pincr = 5
        return rc

    def OnOK(self):
        # NB: StepIt wraps at the end if you increment past the upper limit!
        # self.pbar.StepIt()
        self.progress += self.pincr
        if self.progress > 100:
            self.progress = 100
        if self.progress <= 100:
            self.pbar.SetPos(self.progress)


def demo(modal=0):
    d = TestDialog(MakeDlgTemplate())
    if modal:
        d.DoModal()
    else:
        d.CreateWindow()


if __name__ == "__main__":
    demo(1)

```


---

## pythonwin/pywin/Demos/sliderdemo.py

```python
# sliderdemo.py
# Demo of the slider control courtesy of Mike Fletcher.

import win32con
import win32ui
from pywin.mfc import dialog


class MyDialog(dialog.Dialog):
    """
    Example using simple controls
    """

    _dialogstyle = (
        win32con.WS_MINIMIZEBOX
        | win32con.WS_DLGFRAME
        | win32con.DS_MODALFRAME
        | win32con.WS_POPUP
        | win32con.WS_VISIBLE
        | win32con.WS_CAPTION
        | win32con.WS_SYSMENU
        | win32con.DS_SETFONT
    )
    _buttonstyle = (
        win32con.BS_PUSHBUTTON
        | win32con.WS_TABSTOP
        | win32con.WS_CHILD
        | win32con.WS_VISIBLE
    )
    ### The static template, contains all "normal" dialog items
    DIALOGTEMPLATE = [
        # the dialog itself is the first element in the template
        ["Example slider", (0, 0, 50, 43), _dialogstyle, None, (8, "MS SansSerif")],
        # rest of elements are the controls within the dialog
        # standard "Close" button
        [128, "Close", win32con.IDCANCEL, (0, 30, 50, 13), _buttonstyle],
    ]
    ### ID of the control to be created during dialog initialisation
    IDC_SLIDER = 9500

    def __init__(self):
        dialog.Dialog.__init__(self, self.DIALOGTEMPLATE)

    def OnInitDialog(self):
        rc = dialog.Dialog.OnInitDialog(self)
        # now initialise your controls that you want to create
        # programmatically, including those which are OLE controls
        # those created directly by win32ui.Create*
        # and your "custom controls" which are subclasses/whatever
        win32ui.EnableControlContainer()
        self.slider = win32ui.CreateSliderCtrl()
        self.slider.CreateWindow(
            win32con.WS_TABSTOP | win32con.WS_VISIBLE,
            (0, 0, 100, 30),
            self._obj_,
            self.IDC_SLIDER,
        )
        self.HookMessage(self.OnSliderMove, win32con.WM_HSCROLL)
        return rc

    def OnSliderMove(self, params):
        print("Slider moved")

    def OnCancel(self):
        print("The slider control is at position", self.slider.GetPos())
        self._obj_.OnCancel()


###
def demo():
    dia = MyDialog()
    dia.DoModal()


if __name__ == "__main__":
    demo()

```


---

## pythonwin/pywin/Demos/splittst.py

```python
import commctrl
import fontdemo
import win32ui
from pywin.mfc import docview, window

# derive from CMDIChild.  This does much work for us.


class SplitterFrame(window.MDIChildWnd):
    def __init__(self):
        # call base CreateFrame
        self.images = None
        window.MDIChildWnd.__init__(self)

    def OnCreateClient(self, cp, context):
        splitter = win32ui.CreateSplitter()
        doc = context.doc
        frame_rect = self.GetWindowRect()
        size = ((frame_rect[2] - frame_rect[0]), (frame_rect[3] - frame_rect[1]) // 2)
        sub_size = (size[0] // 2, size[1])
        splitter.CreateStatic(self, 2, 1)
        self.v1 = win32ui.CreateEditView(doc)
        self.v2 = fontdemo.FontView(doc)
        # CListControl view
        self.v3 = win32ui.CreateListView(doc)
        sub_splitter = win32ui.CreateSplitter()
        # pass "splitter" so each view knows how to get to the others
        sub_splitter.CreateStatic(splitter, 1, 2)
        sub_splitter.CreateView(self.v1, 0, 0, (sub_size))
        sub_splitter.CreateView(self.v2, 0, 1, (0, 0))  # size ignored.
        splitter.SetRowInfo(0, size[1], 0)
        splitter.CreateView(self.v3, 1, 0, (0, 0))  # size ignored.
        # Setup items in the imagelist
        self.images = win32ui.CreateImageList(32, 32, 1, 5, 5)
        self.images.Add(win32ui.GetApp().LoadIcon(win32ui.IDR_MAINFRAME))
        self.images.Add(win32ui.GetApp().LoadIcon(win32ui.IDR_PYTHONCONTYPE))
        self.images.Add(win32ui.GetApp().LoadIcon(win32ui.IDR_TEXTTYPE))
        self.v3.SetImageList(self.images, commctrl.LVSIL_NORMAL)
        self.v3.InsertItem(0, "Icon 1", 0)
        self.v3.InsertItem(0, "Icon 2", 1)
        self.v3.InsertItem(0, "Icon 3", 2)
        return 1

    def OnDestroy(self, msg):
        window.MDIChildWnd.OnDestroy(self, msg)
        if self.images:
            self.images.DeleteImageList()
            self.images = None

    def InitialUpdateFrame(self, doc, makeVisible):
        self.v1.ReplaceSel("Hello from Edit Window 1")
        self.v1.SetModifiedFlag(0)


class SampleTemplate(docview.DocTemplate):
    def __init__(self):
        docview.DocTemplate.__init__(
            self, win32ui.IDR_PYTHONTYPE, None, SplitterFrame, None
        )

    def InitialUpdateFrame(self, frame, doc, makeVisible):
        # print("frame is ", frame, frame._obj_)
        # print("doc is ", doc, doc._obj_)
        self._obj_.InitialUpdateFrame(frame, doc, makeVisible)  # call default handler.
        frame.InitialUpdateFrame(doc, makeVisible)


def demo():
    template = SampleTemplate()
    doc = template.OpenDocumentFile(None)
    doc.SetTitle("Splitter Demo")


if __name__ == "__main__":
    import demoutils

    if demoutils.NeedGoodGUI():
        demo()

```


---

## pythonwin/pywin/Demos/threadedgui.py

```python
# Demo of using just windows, without documents and views.

# Also demo of a GUI thread, pretty much direct from the MFC C++ sample MTMDI.

import timer
import win32api
import win32con
import win32ui
from pywin.mfc import window
from pywin.mfc.thread import WinThread

WM_USER_PREPARE_TO_CLOSE = win32con.WM_USER + 32

# font is a dictionary in which the following elements matter:
# (the best matching font to supplied parameters is returned)
#   name		string name of the font as known by Windows
#   size		point size of font in logical units
#   weight		weight of font (win32con.FW_NORMAL, win32con.FW_BOLD)
#   italic		boolean; true if set to anything but None
#   underline	boolean; true if set to anything but None


# This window is a child window of a frame.  It is not the frame window itself.
class FontWindow(window.Wnd):
    def __init__(self, text="Python Rules!"):
        window.Wnd.__init__(self)
        self.text = text
        self.index = 0
        self.incr = 1
        self.width = self.height = 0
        self.ChangeAttributes()
        # set up message handlers

    def Create(self, title, style, rect, parent):
        classStyle = win32con.CS_HREDRAW | win32con.CS_VREDRAW
        className = win32ui.RegisterWndClass(
            classStyle, 0, win32con.COLOR_WINDOW + 1, 0
        )
        self._obj_ = win32ui.CreateWnd()
        self._obj_.AttachObject(self)
        self._obj_.CreateWindow(
            className, title, style, rect, parent, win32ui.AFX_IDW_PANE_FIRST
        )
        self.HookMessage(self.OnSize, win32con.WM_SIZE)
        self.HookMessage(self.OnPrepareToClose, WM_USER_PREPARE_TO_CLOSE)
        self.HookMessage(self.OnDestroy, win32con.WM_DESTROY)
        self.timerid = timer.set_timer(100, self.OnTimer)
        self.InvalidateRect()

    def OnDestroy(self, msg):
        timer.kill_timer(self.timerid)

    def OnTimer(self, id, timeVal):
        self.index += self.incr
        if self.index > len(self.text):
            self.incr = -1
            self.index = len(self.text)
        elif self.index < 0:
            self.incr = 1
            self.index = 0
        self.InvalidateRect()

    def OnPaint(self):
        # print("Paint message from thread", win32api.GetCurrentThreadId())
        dc, paintStruct = self.BeginPaint()
        self.OnPrepareDC(dc, None)

        if self.width == 0 and self.height == 0:
            left, top, right, bottom = self.GetClientRect()
            self.width = right - left
            self.height = bottom - top
        x, y = self.width // 2, self.height // 2
        dc.TextOut(x, y, self.text[: self.index])
        self.EndPaint(paintStruct)

    def ChangeAttributes(self):
        font_spec = {"name": "Arial", "height": 42}
        self.font = win32ui.CreateFont(font_spec)

    def OnPrepareToClose(self, params):
        self.DestroyWindow()

    def OnSize(self, params):
        lParam = params[3]
        self.width = win32api.LOWORD(lParam)
        self.height = win32api.HIWORD(lParam)

    def OnPrepareDC(self, dc, printinfo):
        # Set up the DC for forthcoming OnDraw call
        dc.SetTextColor(win32api.RGB(0, 0, 255))
        dc.SetBkColor(win32api.GetSysColor(win32con.COLOR_WINDOW))
        dc.SelectObject(self.font)
        dc.SetTextAlign(win32con.TA_CENTER | win32con.TA_BASELINE)


class FontFrame(window.MDIChildWnd):
    def __init__(self):
        pass  # Don't call base class doc/view version...

    def Create(self, title, rect=None, parent=None):
        style = win32con.WS_CHILD | win32con.WS_VISIBLE | win32con.WS_OVERLAPPEDWINDOW
        self._obj_ = win32ui.CreateMDIChild()
        self._obj_.AttachObject(self)

        self._obj_.CreateWindow(None, title, style, rect, parent)
        rect = self.GetClientRect()
        rect = (0, 0, rect[2] - rect[0], rect[3] - rect[1])
        self.child = FontWindow("Not threaded")
        self.child.Create(
            "FontDemo", win32con.WS_CHILD | win32con.WS_VISIBLE, rect, self
        )


class TestThread(WinThread):
    def __init__(self, parentWindow):
        self.parentWindow = parentWindow
        self.child = None
        WinThread.__init__(self)

    def InitInstance(self):
        rect = self.parentWindow.GetClientRect()
        rect = (0, 0, rect[2] - rect[0], rect[3] - rect[1])

        self.child = FontWindow()
        self.child.Create(
            "FontDemo", win32con.WS_CHILD | win32con.WS_VISIBLE, rect, self.parentWindow
        )
        self.SetMainFrame(self.child)
        return WinThread.InitInstance(self)

    def ExitInstance(self):
        return 0


class ThreadedFontFrame(window.MDIChildWnd):
    def __init__(self):
        pass  # Don't call base class doc/view version...
        self.thread = None

    def Create(self, title, rect=None, parent=None):
        style = win32con.WS_CHILD | win32con.WS_VISIBLE | win32con.WS_OVERLAPPEDWINDOW
        self._obj_ = win32ui.CreateMDIChild()
        self._obj_.CreateWindow(None, title, style, rect, parent)
        self._obj_.HookMessage(self.OnDestroy, win32con.WM_DESTROY)
        self._obj_.HookMessage(self.OnSize, win32con.WM_SIZE)

        self.thread = TestThread(self)
        self.thread.CreateThread()

    def OnSize(self, msg):
        pass

    def OnDestroy(self, msg):
        win32ui.OutputDebugString("OnDestroy\n")
        if self.thread and self.thread.child:
            child = self.thread.child
            child.SendMessage(WM_USER_PREPARE_TO_CLOSE, 0, 0)
            win32ui.OutputDebugString("Destroyed\n")


def Demo():
    f = FontFrame()
    f.Create("Font Demo")


def ThreadedDemo():
    rect = win32ui.GetMainFrame().GetMDIClient().GetClientRect()
    rect = rect[0], int(rect[3] * 3 / 4), int(rect[2] / 4), rect[3]
    incr = rect[2]
    for i in range(4):
        if i == 0:
            f = FontFrame()
            title = "Not threaded"
        else:
            f = ThreadedFontFrame()
            title = "Threaded GUI Demo"
        f.Create(title, rect)
        rect = rect[0] + incr, rect[1], rect[2] + incr, rect[3]
    # Givem a chance to start
    win32api.Sleep(100)
    win32ui.PumpWaitingMessages()


if __name__ == "__main__":
    import demoutils

    if demoutils.NeedGoodGUI():
        ThreadedDemo()
# 		Demo()

```


---

## pythonwin/pywin/Demos/toolbar.py

```python
# Demo of ToolBars

# Shows the toolbar control.
# Demos how to make custom tooltips, etc.

import commctrl
import win32con
import win32ui
from pywin.mfc import afxres, docview, window


class GenericFrame(window.MDIChildWnd):
    def OnCreateClient(self, cp, context):
        # handlers for toolbar buttons
        self.HookCommand(self.OnPrevious, 401)
        self.HookCommand(self.OnNext, 402)
        # It's not necessary for us to hook both of these - the
        # common controls should fall-back all by themselves.
        # Indeed, given we hook TTN_NEEDTEXTW, commctrl.TTN_NEEDTEXTA
        # will not be called.
        self.HookNotify(self.GetTTText, commctrl.TTN_NEEDTEXT)
        self.HookNotify(self.GetTTText, commctrl.TTN_NEEDTEXTW)

        # 		parent = win32ui.GetMainFrame()
        parent = self
        style = (
            win32con.WS_CHILD
            | win32con.WS_VISIBLE
            | afxres.CBRS_SIZE_DYNAMIC
            | afxres.CBRS_TOP
            | afxres.CBRS_TOOLTIPS
            | afxres.CBRS_FLYBY
        )

        buttons = (win32ui.ID_APP_ABOUT, win32ui.ID_VIEW_INTERACTIVE)
        bitmap = win32ui.IDB_BROWSER_HIER
        tbid = 0xE840
        self.toolbar = tb = win32ui.CreateToolBar(parent, style, tbid)
        tb.LoadBitmap(bitmap)
        tb.SetButtons(buttons)

        tb.EnableDocking(afxres.CBRS_ALIGN_ANY)
        tb.SetWindowText("Test")
        parent.EnableDocking(afxres.CBRS_ALIGN_ANY)
        parent.DockControlBar(tb)
        parent.LoadBarState("ToolbarTest")
        window.MDIChildWnd.OnCreateClient(self, cp, context)
        return 1

    def OnDestroy(self, msg):
        self.SaveBarState("ToolbarTest")

    def GetTTText(self, std, extra):
        (hwndFrom, idFrom, code) = std
        text, hinst, flags = extra
        if flags & commctrl.TTF_IDISHWND:
            return  # Not handled
        if idFrom == win32ui.ID_APP_ABOUT:
            # our 'extra' return value needs to be the following
            # entries from a NMTTDISPINFO[W] struct:
            # (szText, hinst, uFlags).  None means 'don't change
            # the value'
            return 0, ("It works!", None, None)
        return None  # not handled.

    def GetMessageString(self, id):
        if id == win32ui.ID_APP_ABOUT:
            return "Dialog Test\nTest"
        else:
            return self._obj_.GetMessageString(id)

    def OnSize(self, params):
        print("OnSize called with ", params)

    def OnNext(self, id, cmd):
        print("OnNext called")

    def OnPrevious(self, id, cmd):
        print("OnPrevious called")


msg = """\
This toolbar was dynamically created.\r
\r
The first item's tooltips is provided by Python code.\r
\r
(Don't close the window with the toolbar in a floating state - it may not re-appear!)\r
"""


def test():
    template = docview.DocTemplate(
        win32ui.IDR_PYTHONTYPE, None, GenericFrame, docview.EditView
    )
    doc = template.OpenDocumentFile(None)
    doc.SetTitle("Toolbar Test")
    view = doc.GetFirstView()
    view.SetWindowText(msg)


if __name__ == "__main__":
    import demoutils

    if demoutils.NeedGoodGUI():
        test()

```
