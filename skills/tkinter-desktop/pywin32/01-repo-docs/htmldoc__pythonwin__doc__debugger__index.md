# pythonwin/doc/debugger/index.html

> 来源：https://github.com/mhammond/pywin32/blob/main/pythonwin/doc/debugger/index.html
> （该文档在 mhammond.github.io 文档站已 404，仅仓库内存在，此处为全文转录）

## Pythonwin Debugger Overview

News Flash:

We take full advantage of Scintilla from Neil Hodgson (see [scintilla.org](https://www.scintilla.org)) This offers a much better interface, including Visual C++/VB type indicators for breakpoints in the left column, etc

This document gives a general overview of the Pythonwin Debugger package.

- If you are using or looking at this package for the first time, you should check out the debugger tutorial.
- For reference information, check out the general debugger documentation
- If something doesn't work, please read the known problems with the debugger before mailing me!

## Introduction

This package is a general-purpose debugger for Python on Win32 platforms. It is a full-blown GUI debugger with the following features:

- Works from almost any Python program - be it inside Pythonwin, a console "Python.exe" program - even from within a COM object hosted by Visual Basic or Microsoft Internet Explorer (but not from a Tkinter app, apparently?)
- MSVC style debugging interface, including breakpoint etc indicators in the margin, and dockable debugging windows.
- Call-stack display lets you see each individual stack entry, and examine the local and global variables.
- Iinteractive window fully operarable in the context of the code being debugged!

There used to be more out-of-date stuff here, but not any more :-) The tutorial is also a little out of date, but is worth following along with (but as you notice the old screen shots, say a praise for Scintilla!)

---

- For questions or comments about the debugger, send email to MarkH@ActiveState.com (Mark Hammond).
