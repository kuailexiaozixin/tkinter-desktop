### NAME

Tcl_Backslash — parse a backslash sequence

### SYNOPSIS

**#include <tcl.h>**  
char  
**Tcl_Backslash**(*src, countPtr*)  

### ARGUMENTS

const char ***src** (in)     Pointer to a string starting with a backslash.

int ***countPtr** (out)     If *countPtr* is not NULL, **countPtr* gets filled
in with number of characters in the backslash sequence, including the backslash
character.

### DESCRIPTION

The use of **Tcl_Backslash** is deprecated in favor of
**[Tcl_UtfBackslash](../TclLib/Utf.md)**.

This is a utility procedure provided for backwards compatibility with non-
internationalized Tcl extensions. It parses a backslash sequence and returns
the low byte of the Unicode character corresponding to the sequence.
**Tcl_Backslash** modifies **countPtr* to contain the number of characters in
the backslash sequence.

See the [Tcl](../TclCmd/Tcl.md) manual entry for information on the valid
backslash sequences. All of the sequences described in the
[Tcl](../TclCmd/Tcl.md) manual entry are supported by **Tcl_Backslash**.

### SEE ALSO

**[Tcl](../TclCmd/Tcl.md)** , **[Tcl_UtfBackslash](../TclLib/Utf.md)**

### KEYWORDS

[backslash](../Keywords/B.htm#backslash), [parse](../Keywords/P.htm#parse)

Copyright © 1989-1993 The Regents of the University of California.  
Copyright © 1994-1996 Sun Microsystems, Inc.
