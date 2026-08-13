### NAME

Tk_ClipboardClear, Tk_ClipboardAppend — Manage the clipboard

### SYNOPSIS

**#include <tk.h>**  
int  
**Tk_ClipboardClear**(*interp, tkwin*)  
int  
**Tk_ClipboardAppend**(*interp, tkwin, target, format, buffer*)  

### ARGUMENTS

[Tcl_Interp](../TclLib/Interp.md) ***interp** (in)     Interpreter to use for
reporting errors.

[Tk_Window](../TkLib/WindowId.md) **tkwin** (in)     Window that determines
which display's clipboard to manipulate.

Atom **target** (in)     Conversion type for this clipboard item; has same
meaning as *target* argument to
**[Tk_CreateSelHandler](../TkLib/CrtSelHdlr.md)**.

Atom **[format](../TclCmd/format.md)** (in)     Representation to use when
data is retrieved; has same meaning as *format* argument to
**[Tk_CreateSelHandler](../TkLib/CrtSelHdlr.md)**.

const char ***buffer** (in)     Null terminated string containing the data to
be appended to the clipboard.

### DESCRIPTION

These two procedures manage the clipboard for Tk. The clipboard is typically
managed by calling **Tk_ClipboardClear** once, then calling
**Tk_ClipboardAppend** to add data for any number of targets.

**Tk_ClipboardClear** claims the CLIPBOARD selection and frees any data items
previously stored on the clipboard in this application. It normally returns
**[TCL_OK](../TclCmd/catch.md)** , but if an error occurs it returns
**[TCL_ERROR](../TclCmd/catch.md)** and leaves an error message in interpreter
*interp* 's result. **Tk_ClipboardClear** must be called before a sequence of
**Tk_ClipboardAppend** calls can be issued.

**Tk_ClipboardAppend** appends a buffer of data to the clipboard. The first
buffer for a given *target* determines the *format* for that *target*. Any
successive appends for that *target* must have the same format or an error will
be returned. **Tk_ClipboardAppend** returns **[TCL_OK](../TclCmd/catch.md)**
if the buffer is successfully copied onto the clipboard. If the clipboard is
not currently owned by the application, either because **Tk_ClipboardClear**
has not been called or because ownership of the clipboard has changed since the
last call to **Tk_ClipboardClear** , **Tk_ClipboardAppend** returns
**[TCL_ERROR](../TclCmd/catch.md)** and leaves an error message in the result
of interpreter *interp*.

In order to guarantee atomicity, no event handling should occur between
**Tk_ClipboardClear** and the following **Tk_ClipboardAppend** calls (otherwise
someone could retrieve a partially completed clipboard or claim ownership away
from this application).

**Tk_ClipboardClear** may invoke callbacks, including arbitrary Tcl scripts, as
a result of losing the CLIPBOARD selection, so any calling function should take
care to be re-entrant at the point **Tk_ClipboardClear** is invoked.

### KEYWORDS

[append](../Keywords/A.htm#append), [clipboard](../Keywords/C.htm#clipboard),
[clear](../Keywords/C.htm#clear), [format](../Keywords/F.htm#format),
[type](../Keywords/T.htm#type)

Copyright © 1994 The Regents of the University of California.  
Copyright © 1994-1996 Sun Microsystems, Inc.
