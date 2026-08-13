### NAME

Tcl_Init — find and source initialization script

### SYNOPSIS

**#include <tcl.h>**  
int  
**Tcl_Init**(*interp*)  

### ARGUMENTS

[Tcl_Interp](../TclLib/Interp.md) ***interp** (in)     Interpreter to
initialize.

### DESCRIPTION

**Tcl_Init** is a helper procedure that finds and
**[source](../TclCmd/source.md)** s the **init.tcl** script, which should
exist somewhere on the Tcl library path.

**Tcl_Init** is typically called from **[Tcl_AppInit](../TclLib/AppInit.md)**
procedures.

### SEE ALSO

**[Tcl_AppInit](../TclLib/AppInit.md)** ,
**[Tcl_Main](../TclLib/Tcl_Main.md)**

### KEYWORDS

[application](../Keywords/A.htm#application),
[initialization](../Keywords/I.htm#initialization),
[interpreter](../Keywords/I.htm#interpreter)

Copyright © 1998-2000 Scriptics Corporation.
