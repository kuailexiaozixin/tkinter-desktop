### NAME

Tcl_RecordAndEvalObj — save command on history list before evaluating

### SYNOPSIS

**#include <tcl.h>**  
int  
**Tcl_RecordAndEvalObj**(*interp, cmdPtr, flags*)  

### ARGUMENTS

[Tcl_Interp](../TclLib/Interp.md) ***interp** (in)     Tcl interpreter in
which to evaluate command.

[Tcl_Obj](../TclLib/Object.md) ***cmdPtr** (in)     Points to a Tcl value
containing a command (or sequence of commands) to execute.

int **flags** (in)     An OR'ed combination of flag bits. **TCL_NO_EVAL** means
record the command but do not evaluate it. **TCL_EVAL_GLOBAL** means evaluate
the command at global level instead of the current stack level.

### DESCRIPTION

**Tcl_RecordAndEvalObj** is invoked to record a command as an event on the
history list and then execute it using **[Tcl_EvalObjEx](../TclLib/Eval.md)**
(or **[Tcl_GlobalEvalObj](../TclLib/Eval.md)** if the **TCL_EVAL_GLOBAL** bit
is set in *flags*). It returns a completion code such as
**[TCL_OK](../TclCmd/catch.md)** just like
**[Tcl_EvalObjEx](../TclLib/Eval.md)** , as well as a result value containing
additional information (a result value or error message) that can be retrieved
using **[Tcl_GetObjResult](../TclLib/SetResult.md)**. If you do not want the
command recorded on the history list then you should invoke
**[Tcl_EvalObjEx](../TclLib/Eval.md)** instead of **Tcl_RecordAndEvalObj**.
Normally **Tcl_RecordAndEvalObj** is only called with top-level commands typed
by the user, since the purpose of history is to allow the user to re-issue
recently invoked commands. If the *flags* argument contains the **TCL_NO_EVAL**
bit then the command is recorded without being evaluated.

### SEE ALSO

**[Tcl_EvalObjEx](../TclLib/Eval.md)** ,
**[Tcl_GetObjResult](../TclLib/SetResult.md)**

### KEYWORDS

[command](../Keywords/C.htm#command), [event](../Keywords/E.htm#event),
[execute](../Keywords/E.htm#execute), [history](../Keywords/H.htm#history),
[interpreter](../Keywords/I.htm#interpreter), [value](../Keywords/V.htm#value),
[record](../Keywords/R.htm#record)

Copyright © 1997 Sun Microsystems, Inc.
