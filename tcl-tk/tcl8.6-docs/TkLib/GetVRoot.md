### NAME

Tk_GetVRootGeometry — Get location and size of virtual root for window

### SYNOPSIS

**#include <tk.h>**  
**Tk_GetVRootGeometry(***tkwin, xPtr, yPtr, widthPtr, heightPtr***)**  

### ARGUMENTS

[Tk_Window](../TkLib/WindowId.md) **tkwin** (in)     Token for window whose
virtual root is to be queried.

int **xPtr** (out)     Points to word in which to store x-offset of virtual
root.

int **yPtr** (out)     Points to word in which to store y-offset of virtual
root.

int **widthPtr** (out)     Points to word in which to store width of virtual
root.

int **heightPtr** (out)     Points to word in which to store height of virtual
root.

### DESCRIPTION

**Tk_GetVRootGeometry** returns geometry information about the virtual root
window associated with *tkwin*. The “associated” virtual root is the one in
which *tkwin* 's nearest top-level ancestor (or *tkwin* itself if it is a top-
level window) has been reparented by the window manager. This window is
identified by a **__SWM_ROOT** or **__WM_ROOT** property placed on the top-
level window by the window manager. If *tkwin* is not associated with a virtual
root (e.g. because the window manager does not use virtual roots) then **xPtr*
and **yPtr* will be set to 0 and **widthPtr* and **heightPtr* will be set to
the dimensions of the screen containing *tkwin*.

### KEYWORDS

[geometry](../Keywords/G.htm#geometry), [height](../Keywords/H.htm#height),
[location](../Keywords/L.htm#location), [virtual
root](../Keywords/V.htm#virtual root), [width](../Keywords/W.htm#width),
[window manager](../Keywords/W.htm#window manager)

Copyright © 1990 The Regents of the University of California.  
Copyright © 1994-1996 Sun Microsystems, Inc.
