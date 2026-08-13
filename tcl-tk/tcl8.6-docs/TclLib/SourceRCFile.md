### NAME

Tcl_SourceRCFile — source the Tcl rc file

### SYNOPSIS

**#include <tcl.h>**  
void  
**Tcl_SourceRCFile**(*interp*)  

### ARGUMENTS

[Tcl_Interp](../TclLib/Interp.md) ***interp** (in)     Tcl interpreter to
source rc file into.

### DESCRIPTION

**Tcl_SourceRCFile** is used to source the Tcl rc file at startup. It is
typically invoked by [Tcl_Main](../TclLib/Tcl_Main.md) or
[Tk_Main](../TkLib/Tk_Main.md). The name of the file sourced is obtained from
the global variable **tcl_rcFileName** in the interpreter given by *interp*. If
this variable is not defined, or if the file it indicates cannot be found, no
action is taken.

### KEYWORDS

[application-specific initialization](../Keywords/A.htm#application-specific
initialization), [main program](../Keywords/M.htm#main program), [rc
file](../Keywords/R.htm#rc file)

Copyright © 1998-2000 Scriptics Corporation.
