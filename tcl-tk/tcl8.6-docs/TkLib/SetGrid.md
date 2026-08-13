### NAME

Tk_SetGrid, Tk_UnsetGrid — control the grid for interactive resizing

### SYNOPSIS

**#include <tk.h>**  
**Tk_SetGrid**(*tkwin, reqWidth, reqHeight, widthInc, heightInc*)  
**Tk_UnsetGrid**(*tkwin*)  

### ARGUMENTS

[Tk_Window](../TkLib/WindowId.md) **tkwin** (in)     Token for window.

int **reqWidth** (in)     Width in grid units that corresponds to the pixel
dimension *tkwin* has requested via
**[Tk_GeometryRequest](../TkLib/GeomReq.md)**.

int **reqHeight** (in)     Height in grid units that corresponds to the pixel
dimension *tkwin* has requested via
**[Tk_GeometryRequest](../TkLib/GeomReq.md)**.

int **widthInc** (in)     Width of one grid unit, in pixels.

int **heightInc** (in)     Height of one grid unit, in pixels.

### DESCRIPTION

**Tk_SetGrid** turns on gridded geometry management for *tkwin* 's toplevel
window and specifies the geometry of the grid. **Tk_SetGrid** is typically
invoked by a widget when its **setGrid** option is true. It restricts
interactive resizing of *tkwin* 's toplevel window so that the space allocated
to the toplevel is equal to its requested size plus or minus even multiples of
*widthInc* and *heightInc*. Furthermore, the *reqWidth* and *reqHeight* values
are passed to the window manager so that it can report the window's size in
grid units during interactive resizes. If *tkwin* 's configuration changes
(e.g., the size of a grid unit changes) then the widget should invoke
**Tk_SetGrid** again with the new information.

**Tk_UnsetGrid** cancels gridded geometry management for *tkwin* 's toplevel
window.

For each toplevel window there can be at most one internal window with gridding
enabled. If **Tk_SetGrid** or **Tk_UnsetGrid** is invoked when some other
window is already controlling gridding for *tkwin* 's toplevel, the calls for
the new window have no effect.

See the **[wm](../TkCmd/wm.md)** manual entry for additional information on
gridded geometry management.

### KEYWORDS

[grid](../Keywords/G.htm#grid), [window](../Keywords/W.htm#window), [window
manager](../Keywords/W.htm#window manager)

Copyright © 1990-1994 The Regents of the University of California.  
Copyright © 1994-1996 Sun Microsystems, Inc.
