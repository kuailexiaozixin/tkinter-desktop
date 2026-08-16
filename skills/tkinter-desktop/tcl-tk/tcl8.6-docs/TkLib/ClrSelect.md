### NAME

Tk_ClearSelection — Deselect a selection

### SYNOPSIS

**#include <tk.h>**  
**Tk_ClearSelection**(*tkwin, selection*)  

### ARGUMENTS

[Tk_Window](../TkLib/WindowId.md) **tkwin** (in)     The selection will be
cleared from the display containing this window.

Atom **[selection](../TkCmd/selection.md)** (in)     The name of selection to
be cleared.

### DESCRIPTION

**Tk_ClearSelection** cancels the selection specified by the atom *selection*
for the display containing *tkwin*. The selection need not be in *tkwin* itself
or even in *tkwin* 's application. If there is a window anywhere on *tkwin* 's
display that owns *selection* , the window will be notified and the selection
will be cleared. If there is no owner for *selection* on the display, then the
procedure has no effect.

### KEYWORDS

[clear](../Keywords/C.htm#clear), [selection](../Keywords/S.htm#selection)

Copyright © 1992-1994 The Regents of the University of California.  
Copyright © 1994-1996 Sun Microsystems, Inc.
