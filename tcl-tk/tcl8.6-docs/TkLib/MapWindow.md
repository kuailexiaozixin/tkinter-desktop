### NAME

Tk_MapWindow, Tk_UnmapWindow — map or unmap a window

### SYNOPSIS

**#include <tk.h>**  
[Tk_Window](../TkLib/WindowId.md)  
**Tk_MapWindow**(*tkwin*)  
**Tk_UnmapWindow**(*tkwin*)  

### ARGUMENTS

[Tk_Window](../TkLib/WindowId.md) **tkwin** (in)     Token for window.

### DESCRIPTION

These procedures may be used to map and unmap windows managed by Tk.
**Tk_MapWindow** maps the window given by *tkwin* , and also creates an X
window corresponding to *tkwin* if it does not already exist. See the
**[Tk_CreateWindow](../TkLib/CrtWindow.md)** manual entry for information on
deferred window creation. **Tk_UnmapWindow** unmaps *tkwin* 's window from the
screen.

If *tkwin* is a child window (i.e.
**[Tk_CreateWindow](../TkLib/CrtWindow.md)** was used to create a child
window), then event handlers interested in map and unmap events are invoked
immediately. If *tkwin* is not an internal window, then the event handlers will
be invoked later, after X has seen the request and returned an event for it.

These procedures should be used in place of the X procedures **XMapWindow** and
**XUnmapWindow** , since they update Tk's local data structure for *tkwin*.
Applications using Tk should not invoke **XMapWindow** and **XUnmapWindow**
directly.

### KEYWORDS

[map](../Keywords/M.htm#map), [unmap](../Keywords/U.htm#unmap),
[window](../Keywords/W.htm#window)

Copyright © 1990 The Regents of the University of California.  
Copyright © 1994-1997 Sun Microsystems, Inc.
