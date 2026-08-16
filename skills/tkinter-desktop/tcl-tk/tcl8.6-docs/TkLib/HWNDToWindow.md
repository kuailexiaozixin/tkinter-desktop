### NAME

Tk_HWNDToWindow — Find Tk's window information for a Windows window

### SYNOPSIS

**#include <tkPlatDecls.h>**  
[Tk_Window](../TkLib/WindowId.md)  
**Tk_HWNDToWindow**(*hwnd*)  

### ARGUMENTS

HWND **hwnd** (in)     Windows handle for the window.

### DESCRIPTION

Given a Windows HWND window identifier, this procedure returns the
corresponding [Tk_Window](../TkLib/WindowId.md) handle. If there is no
[Tk_Window](../TkLib/WindowId.md) corresponding to *hwnd* then NULL is
returned.

### KEYWORDS

[Windows window id](../Keywords/W.htm#Windows window id)

Copyright © 1998-2000 by Scriptics Corporation.
