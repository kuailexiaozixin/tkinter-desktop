# com/win32com/readme.html

> 来源：https://github.com/mhammond/pywin32/blob/main/com/win32com/readme.html
> （该文档在 mhammond.github.io 文档站已 404，仅仓库内存在，此处为全文转录）

## Python COM Extensions Readme

This is the readme for win32com. Please check out the win32com documentation index

The win32com/test directory contains some interesting scripts (and a new readme.txt). Although these are used for testing, they do show a variety of COM techniques.

#### VARIANT objects

win32com.client now has explicit VARIANT objects which can be used in situations where you need more control over the argument types passed when calling COM methods. See the documentation on
this object

#### Important Currency changes

 In all builds prior to 204, a COM currency value was returned as a tuple of integers. Working with 2 integers to represent a currency object was a poor choice, but the alternative was never clear. Now Python ships with the [decimal](https://docs.python.org/dev/library/decimal.html) module, the alternative has arrived!

 Up until build 212, code could set `pythoncom.__future_currency__ = True` to force use of the decimal module, with a warning issued otherwise. In builds 213 and later, the decimal module is unconditionally used when pythoncom returns you a currency value.

#### Recent Changes

#### Lots of internal changes on the road to py3k

#### win32com.axcontrol and win2con.internet

 Many more interfaces for hosting AX controls and the interfaces used by Internet Explorer.

#### win32com.shell

 The shell interfaces have undergone a number of enhancements and changes. A couple of methods have changed signature between the first build with shell support (200) and later builds. SHGetFileInfo was broken in its result handling, so had to be changed - this is the only function used by the samples that changed, but others not used by the samples also have changed. These shell interfaces are now generally stable.

#### New win32com.taskscheduler module

 Roger Upole has contributed an interface to the Windows task scheduler. This is actually very neat, and it allows Python to edit the task list as shown by Windows Control Panel. Property page suppport may even appear later, now that the win32 library has the new win32rcparser module.

#### ActiveX Scripting

Python only supports "trusted" execution hosts - thus, it will no longer work as an engine inside IE (Python itself no longer has a restricted execution environment). Python continues to work fine as an Active Scripting Engine in all other applications, including Windows Scripting Host, and ASP.

There is also support for Python as an ActiveX Scripting Host.

Active Debugging seems to be fully functional.

#### Older stuff

- Unexpected exceptions in Python COM objects will generally now dump the exception and traceback to stdout. This is useful for debugging and testing - it means that in some cases there will be no need to register an object with --debug to see these tracebacks. Note that COM objects used by server processes (such as ASP) generally have no valid stdout, so will still need to use --debug as usual.

- universal gateway support has been improved - we can now work as an Outlook Addin
