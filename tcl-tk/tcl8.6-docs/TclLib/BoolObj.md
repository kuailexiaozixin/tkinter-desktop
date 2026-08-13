### NAME

Tcl_NewBooleanObj, Tcl_SetBooleanObj, Tcl_GetBooleanFromObj — store/retrieve
boolean value in a [Tcl_Obj](../TclLib/Object.md)

### SYNOPSIS

**#include <tcl.h>**  
[Tcl_Obj](../TclLib/Object.md) *  
**Tcl_NewBooleanObj**(*intValue*)  
**Tcl_SetBooleanObj**(*objPtr, intValue*)  
int  
**Tcl_GetBooleanFromObj**(*interp, objPtr, intPtr*)  

### ARGUMENTS

int **intValue** (in)     Integer value to be stored as a boolean value in a
[Tcl_Obj](../TclLib/Object.md).

[Tcl_Obj](../TclLib/Object.md) ***objPtr** (in/out)     Points to the
[Tcl_Obj](../TclLib/Object.md) in which to store, or from which to retrieve a
boolean value.

[Tcl_Interp](../TclLib/Interp.md) ***interp** (in/out)     If a boolean value
cannot be retrieved, an error message is left in the interpreter's result value
unless *interp* is NULL.

int ***intPtr** (out)     Points to place where **Tcl_GetBooleanFromObj**
stores the boolean value (0 or 1) obtained from *objPtr*.

### DESCRIPTION

These procedures are used to pass boolean values to and from Tcl as
[Tcl_Obj](../TclLib/Object.md)'s. When storing a boolean value into a
[Tcl_Obj](../TclLib/Object.md), any non-zero integer value in *intValue* is
taken to be the boolean value **1** , and the integer value **0** is taken to
be the boolean value **0**.

**Tcl_NewBooleanObj** creates a new [Tcl_Obj](../TclLib/Object.md), stores the
boolean value *intValue* in it, and returns a pointer to the new
[Tcl_Obj](../TclLib/Object.md). The new [Tcl_Obj](../TclLib/Object.md) has
reference count of zero.

**Tcl_SetBooleanObj** accepts *objPtr* , a pointer to an existing
[Tcl_Obj](../TclLib/Object.md), and stores in the
[Tcl_Obj](../TclLib/Object.md) **objPtr* the boolean value *intValue*. This is
a write operation on **objPtr* , so *objPtr* must be unshared. Attempts to
write to a shared [Tcl_Obj](../TclLib/Object.md) will panic. A successful
write of *intValue* into **objPtr* implies the freeing of any former value
stored in **objPtr*.

**Tcl_GetBooleanFromObj** attempts to retrieve a boolean value from the value
stored in **objPtr*. If *objPtr* holds a string value recognized by
**[Tcl_GetBoolean](../TclLib/GetInt.md)** , then the recognized boolean value
is written at the address given by *intPtr*. If *objPtr* holds any value
recognized as a number by Tcl, then if that value is zero a 0 is written at the
address given by *intPtr* and if that value is non-zero a 1 is written at the
address given by *intPtr*. In all cases where a value is written at the address
given by *intPtr* , **Tcl_GetBooleanFromObj** returns
**[TCL_OK](../TclCmd/catch.md)**. If the value of *objPtr* does not meet any
of the conditions above, then **[TCL_ERROR](../TclCmd/catch.md)** is returned
and an error message is left in the interpreter's result unless *interp* is
NULL. **Tcl_GetBooleanFromObj** may also make changes to the internal fields of
**objPtr* so that future calls to **Tcl_GetBooleanFromObj** on the same
*objPtr* can be performed more efficiently.

Note that the routines **Tcl_GetBooleanFromObj** and
**[Tcl_GetBoolean](../TclLib/GetInt.md)** are not functional equivalents. The
set of values for which **Tcl_GetBooleanFromObj** will return
**[TCL_OK](../TclCmd/catch.md)** is strictly larger than the set of values for
which **[Tcl_GetBoolean](../TclLib/GetInt.md)** will do the same. For example,
the value “5” passed to **Tcl_GetBooleanFromObj** will lead to a
**[TCL_OK](../TclCmd/catch.md)** return (and the boolean value 1), while the
same value passed to **[Tcl_GetBoolean](../TclLib/GetInt.md)** will lead to a
**[TCL_ERROR](../TclCmd/catch.md)** return.

### SEE ALSO

**[Tcl_NewObj](../TclLib/Object.md)** ,
**[Tcl_IsShared](../TclLib/Object.md)** ,
**[Tcl_GetBoolean](../TclLib/GetInt.md)**

### KEYWORDS

[boolean](../Keywords/B.htm#boolean), [value](../Keywords/V.htm#value)

Copyright © 1996-1997 Sun Microsystems, Inc.
