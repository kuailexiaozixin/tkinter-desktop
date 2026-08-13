### NAME

Tk_MainWindow, Tk_GetNumMainWindows — functions for querying main window
information

### SYNOPSIS

**#include <tk.h>**  
[Tk_Window](../TkLib/WindowId.md)  
**Tk_MainWindow**(*interp*)  
int  
**Tk_GetNumMainWindows**()  

### ARGUMENTS

[Tcl_Interp](../TclLib/Interp.md) ***interp** (in/out)     Interpreter
associated with the application.

### DESCRIPTION

A main window is a special kind of toplevel window used as the outermost window
in an application.

If *interp* is associated with a Tk application then **Tk_MainWindow** returns
the application's main window. If there is no Tk application associated with
*interp* then **Tk_MainWindow** returns NULL and leaves an error message in
interpreter *interp* 's result.

**Tk_GetNumMainWindows** returns a count of the number of main windows
currently open in the current thread.

### KEYWORDS

[application](../Keywords/A.htm#application), [main
window](../Keywords/M.htm#main window)

Copyright © 1990 The Regents of the University of California.  
Copyright © 1994-1996 Sun Microsystems, Inc.
