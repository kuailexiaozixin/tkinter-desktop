### NAME

Tk_MainLoop — loop for events until all windows are deleted

### SYNOPSIS

**#include <tk.h>**  
**Tk_MainLoop**()  

### DESCRIPTION

**Tk_MainLoop** is a procedure that loops repeatedly calling
**[Tcl_DoOneEvent](../TclLib/DoOneEvent.md)**. It returns only when there are
no applications left in this process (i.e. no main windows exist anymore). Most
windowing applications will call **Tk_MainLoop** after initialization; the main
execution of the application will consist entirely of callbacks invoked via
**[Tcl_DoOneEvent](../TclLib/DoOneEvent.md)**.

### KEYWORDS

[application](../Keywords/A.htm#application), [event](../Keywords/E.htm#event),
[main loop](../Keywords/M.htm#main loop)

Copyright © 1990-1992 The Regents of the University of California.  
Copyright © 1994-1996 Sun Microsystems, Inc.
