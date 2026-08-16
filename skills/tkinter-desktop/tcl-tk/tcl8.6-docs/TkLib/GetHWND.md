### NAME

Tk_GetHWND, Tk_AttachHWND — manage interactions between the Windows handle and
an X window

### SYNOPSIS

**#include <tkPlatDecls.h>**  
HWND  
**Tk_GetHWND**(*window*)  
Window  
**Tk_AttachHWND**(*tkwin, hwnd*)  

### ARGUMENTS

Window **window** (in)     X token for window.

[Tk_Window](../TkLib/WindowId.md) **tkwin** (in)     Tk window for window.

HWND **hwnd** (in)     Windows HWND for window.

### DESCRIPTION

**Tk_GetHWND** returns the Windows HWND identifier for X Windows window given
by *window*.

**Tk_AttachHWND** binds the Windows HWND identifier to the specified
[Tk_Window](../TkLib/WindowId.md) given by *tkwin*. It returns an X Windows
window that encapsulates the HWND.

### KEYWORDS

[identifier](../Keywords/I.htm#identifier), [window](../Keywords/W.htm#window)

Copyright © 1998-2000 by Scriptics Corporation.
