### NAME

Tk_GetJoinStyle, Tk_NameOfJoinStyle — translate between strings and join styles

### SYNOPSIS

**#include <tk.h>**  
int  
**Tk_GetJoinStyle(***interp, string, joinPtr***)**  
const char *  
**Tk_NameOfJoinStyle(***join***)**  

### ARGUMENTS

[Tcl_Interp](../TclLib/Interp.md) ***interp** (in)     Interpreter to use for
error reporting.

const char ***string** (in)     String containing name of join style - one of
“**bevel** ”, “**miter** ”, or “**round** ” \- or a unique abbreviation of one.

int ***joinPtr** (out)     Pointer to location in which to store X join style
corresponding to *string*.

int **[join](../TclCmd/join.md)** (in)     Join style: one of **JoinBevel** ,
**JoinMiter** , **JoinRound**.

### DESCRIPTION

**Tk_GetJoinStyle** places in **joinPtr* the X join style corresponding to
*string* , which will be one of **JoinBevel** , **JoinMiter** , or
**JoinRound**. Join styles are typically used in X graphics contexts to
indicate how adjacent line segments should be joined together. See the X
documentation for information on what each style implies.

Under normal circumstances the return value is
**[TCL_OK](../TclCmd/catch.md)** and *interp* is unused. If *string* does not
contain a valid join style or an abbreviation of one of these names, then an
error message is stored in interpreter *interp* 's result,
**[TCL_ERROR](../TclCmd/catch.md)** is returned, and **joinPtr* is unmodified.

**Tk_NameOfJoinStyle** is the logical inverse of **Tk_GetJoinStyle**. Given a
join style such as **JoinBevel** it returns a statically-allocated string
corresponding to *join*. If *join* is not a legal join style, then “unknown
join style” is returned.

### KEYWORDS

[bevel](../Keywords/B.htm#bevel), [join style](../Keywords/J.htm#join style),
[miter](../Keywords/M.htm#miter), [round](../Keywords/R.htm#round)

Copyright © 1990 The Regents of the University of California.  
Copyright © 1994-1996 Sun Microsystems, Inc.
