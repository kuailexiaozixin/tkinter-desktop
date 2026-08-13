### NAME

Tk_SetWindowVisual — change visual characteristics of window

### SYNOPSIS

**#include <tk.h>**  
int  
**Tk_SetWindowVisual**(*tkwin, visual, depth, colormap*)  

### ARGUMENTS

[Tk_Window](../TkLib/WindowId.md) **tkwin** (in)     Token for window.

Visual ***visual** (in)     New visual type to use for *tkwin*.

int **depth** (in)     Number of bits per pixel desired for *tkwin*.

Colormap **colormap** (in)     New colormap for *tkwin* , which must be
compatible with *visual* and *depth*.

### DESCRIPTION

When Tk creates a new window it assigns it the default visual characteristics
(visual, depth, and colormap) for its screen. **Tk_SetWindowVisual** may be
called to change them. **Tk_SetWindowVisual** must be called before the window
has actually been created in X (e.g. before
**[Tk_MapWindow](../TkLib/MapWindow.md)** or
**[Tk_MakeWindowExist](../TkLib/CrtWindow.md)** has been invoked for the
window). The safest thing is to call **Tk_SetWindowVisual** immediately after
calling **[Tk_CreateWindow](../TkLib/CrtWindow.md)**. If *tkwin* has already
been created before **Tk_SetWindowVisual** is called then it returns 0 and does
not make any changes; otherwise it returns 1 to signify that the operation
completed successfully.

Note: **Tk_SetWindowVisual** should not be called if you just want to change a
window's colormap without changing its visual or depth; call
**[Tk_SetWindowColormap](../TkLib/ConfigWind.md)** instead.

### KEYWORDS

[colormap](../Keywords/C.htm#colormap), [depth](../Keywords/D.htm#depth),
[visual](../Keywords/V.htm#visual)

Copyright © 1992 The Regents of the University of California.  
Copyright © 1994-1996 Sun Microsystems, Inc.
