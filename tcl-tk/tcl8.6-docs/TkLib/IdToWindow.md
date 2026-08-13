### NAME

Tk_IdToWindow — Find Tk's window information for an X window

### SYNOPSIS

**#include <tk.h>**  
[Tk_Window](../TkLib/WindowId.md)  
**Tk_IdToWindow**(*display, window*)  

### ARGUMENTS

Display ***display** (in)     X display containing the window.

Window **window** (in)     X id for window.

### DESCRIPTION

Given an X window identifier and the X display it corresponds to, this
procedure returns the corresponding [Tk_Window](../TkLib/WindowId.md) handle.
If there is no [Tk_Window](../TkLib/WindowId.md) corresponding to *window*
then NULL is returned.

### KEYWORDS

[X window id](../Keywords/X.htm#X window id)

Copyright © 1995-1996 Sun Microsystems, Inc.
