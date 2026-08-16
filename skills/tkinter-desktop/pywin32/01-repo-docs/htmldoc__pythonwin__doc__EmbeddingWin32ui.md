# pythonwin/doc/EmbeddingWin32ui.html

> 来源：https://github.com/mhammond/pywin32/blob/main/pythonwin/doc/EmbeddingWin32ui.html
> （该文档在 mhammond.github.io 文档站已 404，仅仓库内存在，此处为全文转录）

## Embedding Pythonwin.

Pythonwin is distributed as 2 key components - Pythonwin.exe and win32ui.pyd. Win32ui.pyd contains the raw functionality of Pythonwin - Pythonwin.exe is a simple "wrapper" .exe that hosts win32ui.pyd.

This document describes how to embed the win32ui extension module in your own application.

### Limitations.

The biggest limitations you will find are that a host application must

- Have some small changes made to the application source to fully support win32ui command handling and routing (although most things work without modification)
- Be an MFC application

Below is some example code needed to embed win32ui in your application..

### Changes to the application.

#### Subclass a Win32uiHostGlue class

You must instantiate a Win32uiHostGlue class. This class is used as a glue between win32ui.pyd and the host .exe, and is defined in Win32uiHostGlue.h

Currently, this consists of about 5 methods that must be called by your application. The principle is that the Application must hook certain handlers, and delegate them to the HostGlue class. This will ensure the appropriate Win32ui internals are called.

### Embedding win32ui Architecture

#### Win32uiHostGlue.h

The Win32uiHostGlue.h module defines a class which makes interfacing fairly simple. This Win32uiHostGlue class is used as a glue between win32ui.pyd and the host .exe. In the most simple case, you need to instantiate one of the classes, and at certain key points in your CWinApp derived class, call the appropriate methods. You may choose to provide your own glue class derived from Win32uiHostGlue in certain cases.

Below is an example class, which overrides the "SetStatusText" method, so that status information displays in the applications status bar (this is only necessary if your application has a "non standard" status bar - normally you could omit this.).

```
GameApp NEAR theApp; // My existing CWinApp derived class.
// HostGlue class.

class GameHostGlue : public Win32uiHostGlue
{
  virtual void SetStatusText(const char *text, BOOL bForce)
    // Assuming our GameApp above defines a SetStatusText method
    {GetApp()->SetStatusText(text, bForce);}
};

// The one and only Glue object.
GameHostGlue NEAR glue;
```

And now we are well on our way.

#### Delegating to win32uiHostGlue

You need to either implement, or modify, certain key methods of your Application object. Probably the most important is the call to initialise win32ui. You need to modify your CWinApp::InitInstance method (it is almost certain you already have one). The following code needs to be executed in this method:

#### InitInstance

```
BOOL GameApp::InitInstance()
{
...
  if (!glue.DynamicApplicationInit("import initscore", csScripts)) {
  // Assuming you have a ReportError method - do whatever makes sense!
    ReportError("Could not attach to the Python win32ui extensions");
    return FALSE;
  }
...
```

Note the following:

- The first param - "import initscore" is the Python command that will be executed to kick in the Python side of the world. For Pythonwin, this is "import pywin.framework.startup" - see "initscore.py" below.
- The second param may be empty or NULL, and defines an additional PythonPath to be added. This is useful if you do not want your application .py/.pyd files on the main PythonPath. In the example above, code not shown loads csScripts from the applications INI file.
- The example above assumes the Python code is not responsible for creating the main application window. In the case of Pythonwin (where the Python code does create the main window) this call actually appears in InitApplication() for the CWinApp class. The example above assumes you have existing C++ code which creates the main frame window. Your Python code could create child windows, as the initscore.py file demonstrates.

#### And the Rest

Below is the rest of the code you need to implement. You may need to create these methods, as the AppWizard generated MFC application does not have some.

```
BOOL
GameApp::OnCmdMsg (UINT nID, int nCode,
void* pExtra, AFX_CMDHANDLERINFO*pHandlerInfo)
{
  // yield to Python first - send to the main frame, as there is no Python app object.
  if (glue.OnCmdMsg (m_pMainWnd, nID, nCode, pExtra, pHandlerInfo))
    return TRUE;
  else
    return CWinApp::OnCmdMsg (nID, nCode, pExtra, pHandlerInfo);
}

BOOL GameApp::PreTranslateMessage(MSG *pMsg)
{
  if (glue.PreTranslateMessage(pMsg))
    return TRUE;
  else
    return CWinApp::PreTranslateMessage(pMsg);
}
BOOL GameApp::OnIdle( LONG lCount )
{
  // call base class idle first
  if (CWinApp::OnIdle(lCount))
    return TRUE;
  return glue.OnIdle(lCount);
}
```

####
- initscore.py

- Below is the code for initscore.py. Obviously your code will vary, depending on your requirements.

```
import sys
import win32ui
# First step - redirect python output to the debugging device, until we
# can create a window to capture it.

# Note that this is only useful while debugging, and simply sends any
# Python output (ie, exceptions while developing the startup code) is
# printed to the MSVC debugger. Note that since this code was written,
# the win32trace module has appeared, giving another alternative to
# debugging this code.
class DebugOutput:
  softspace=1
  def write(self,message):
    win32ui.OutputDebug(message)
sys.stderr=sys.stdout=DebugOutput()

# One of your first priorities should be to set sys.stdout to somewhere useful,
# depending on what useful means to your application. This code simply creates
# the Pythonwin Interactive Window, which handles this automatically.

# Now here is the code that does the real work.
import win32con
```

from pywin.framework import intpyapp, app

```

class ScoreApp(intpyapp.InteractivePythonApp):
  def InitInstance(self):
    # Call the base class (if you want)
    intpyapp.InteractivePythonApp.InitInstance(self)
    # Do domething useful, specific to your app.
    # Here, we minimise the interactive window.
    # (after painting the main frame)
    win32ui.PumpWaitingMessages()
    interact.edit.currentView.GetParent().ShowWindow(win32con.SW_MINIMIZE)

#  def OnExitInstance(self):
#    return 0

app = ScoreApp()
```

And we are done
