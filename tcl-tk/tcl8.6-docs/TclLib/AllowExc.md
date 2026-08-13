### NAME

Tcl_AllowExceptions — allow all exceptions in next script evaluation

### SYNOPSIS

**#include <tcl.h>**  
**Tcl_AllowExceptions**(*interp*)  

### ARGUMENTS

[Tcl_Interp](../TclLib/Interp.md) ***interp** (in)     Interpreter in which
script will be evaluated.

### DESCRIPTION

If a script is evaluated at top-level (i.e. no other scripts are pending
evaluation when the script is invoked), and if the script terminates with a
completion code other than **[TCL_OK](../TclCmd/catch.md)** ,
**[TCL_ERROR](../TclCmd/catch.md)** or **[TCL_RETURN](../TclCmd/catch.md)** ,
then Tcl normally converts this into a **[TCL_ERROR](../TclCmd/catch.md)**
return with an appropriate message. The particular script evaluation procedures
of Tcl that act in the manner are **[Tcl_EvalObjEx](../TclLib/Eval.md)** ,
**[Tcl_EvalObjv](../TclLib/Eval.md)** , **[Tcl_Eval](../TclLib/Eval.md)** ,
**[Tcl_EvalEx](../TclLib/Eval.md)** , **[Tcl_GlobalEval](../TclLib/Eval.md)**
, **[Tcl_GlobalEvalObj](../TclLib/Eval.md)** ,
**[Tcl_VarEval](../TclLib/Eval.md)** and
**[Tcl_VarEvalVA](../TclLib/Eval.md)**.

However, if **Tcl_AllowExceptions** is invoked immediately before calling one
of those a procedures, then arbitrary completion codes are permitted from the
script, and they are returned without modification. This is useful in cases
where the caller can deal with exceptions such as
**[TCL_BREAK](../TclCmd/catch.md)** or **[TCL_CONTINUE](../TclCmd/catch.md)**
in a meaningful way.

### KEYWORDS

[continue](../Keywords/C.htm#continue), [break](../Keywords/B.htm#break),
[exception](../Keywords/E.htm#exception),
[interpreter](../Keywords/I.htm#interpreter)

Copyright © 1989-1993 The Regents of the University of California.  
Copyright © 1994-1996 Sun Microsystems, Inc.
