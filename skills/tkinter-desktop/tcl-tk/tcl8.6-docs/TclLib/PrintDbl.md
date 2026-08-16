### NAME

Tcl_PrintDouble — Convert floating value to string

### SYNOPSIS

**#include <tcl.h>**  
**Tcl_PrintDouble**(*interp, value, dst*)  

### ARGUMENTS

[Tcl_Interp](../TclLib/Interp.md) ***interp** (in)     Before Tcl 8.0, the
**[tcl_precision](../TclCmd/tclvars.md)** variable in this interpreter
controlled the conversion. As of Tcl 8.0, this argument is ignored and the
conversion is controlled by the **[tcl_precision](../TclCmd/tclvars.md)**
variable that is now shared by all interpreters.

double **value** (in)     Floating-point value to be converted.

char ***dst** (out)     Where to store the string representing *value*. Must
have at least **TCL_DOUBLE_SPACE** characters of storage.

### DESCRIPTION

**Tcl_PrintDouble** generates a string that represents the value of *value* and
stores it in memory at the location given by *dst*. It uses **%g** format to
generate the string, with one special twist: the string is guaranteed to
contain either a “.” or an “e” so that it does not look like an integer. Where
**%g** would generate an integer with no decimal point, **Tcl_PrintDouble**
adds “.0”.

If the **[tcl_precision](../TclCmd/tclvars.md)** value is non-zero, the result
will have precisely that many digits of significance. If the value is zero (the
default), the result will have the fewest digits needed to represent the number
in such a way that **[Tcl_NewDoubleObj](../TclLib/DoubleObj.md)** will
generate the same number when presented with the given string. IEEE semantics
of rounding to even apply to the conversion.

### KEYWORDS

[conversion](../Keywords/C.htm#conversion), [double-
precision](../Keywords/D.htm#double-precision), [floating-
point](../Keywords/F.htm#floating-point), [string](../Keywords/S.htm#string)

Copyright © 1989-1993 The Regents of the University of California.  
Copyright © 1994-1997 Sun Microsystems, Inc.
