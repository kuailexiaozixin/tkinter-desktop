### NAME

Tcl_PkgRequire, Tcl_PkgRequireEx, Tcl_PkgRequireProc, Tcl_PkgPresent,
Tcl_PkgPresentEx, Tcl_PkgProvide, Tcl_PkgProvideEx — package version control

### SYNOPSIS

**#include <tcl.h>**  
const char *  
**Tcl_PkgRequire**(*interp, name, version, exact*)  
const char *  
**Tcl_PkgRequireEx**(*interp, name, version, exact, clientDataPtr*)  
int  
**Tcl_PkgRequireProc**(*interp, name, objc, objv, clientDataPtr*)  
const char *  
**Tcl_PkgPresent**(*interp, name, version, exact*)  
const char *  
**Tcl_PkgPresentEx**(*interp, name, version, exact, clientDataPtr*)  
int  
**Tcl_PkgProvide**(*interp, name, version*)  
int  
**Tcl_PkgProvideEx**(*interp, name, version, clientData*)  

### ARGUMENTS

[Tcl_Interp](../TclLib/Interp.md) ***interp** (in)     Interpreter where
package is needed or available.

const char ***name** (in)     Name of package.

const char ***version** (in)     A version specification string as described
for **[package require](../TclCmd/package.md)**.

int **exact** (in)     Non-zero means that only the particular version
specified by *version* is acceptable. Zero means that newer versions than
*version* are also acceptable as long as they have the same major version
number as *version*.

const void ***clientData** (in)     Arbitrary value to be associated with the
package.

void ***clientDataPtr** (out)     Pointer to place to store the value
associated with the matching package. It is only changed if the pointer is not
NULL and the function completed successfully. The storage can be any pointer
type with the same size as a void pointer.

int **objc** (in)     Number of requirements.

[Tcl_Obj](../TclLib/Object.md)* **objv[]** (in)     Array of requirements.

### DESCRIPTION

These procedures provide C-level interfaces to Tcl's package and version
management facilities.

**Tcl_PkgRequire** is equivalent to the **[package
require](../TclCmd/package.md)** command, **Tcl_PkgPresent** is equivalent to
the **[package present](../TclCmd/package.md)** command, and
**Tcl_PkgProvide** is equivalent to the **[package
provide](../TclCmd/package.md)** command.

See the documentation for the Tcl commands for details on what these procedures
do.

If **Tcl_PkgPresent** or **Tcl_PkgRequire** complete successfully they return a
pointer to the version string for the version of the package that is provided
in the interpreter (which may be different than *version*); if an error occurs
they return NULL and leave an error message in the interpreter's result.

**Tcl_PkgProvide** returns **[TCL_OK](../TclCmd/catch.md)** if it completes
successfully; if an error occurs it returns
**[TCL_ERROR](../TclCmd/catch.md)** and leaves an error message in the
interpreter's result.

**Tcl_PkgProvideEx** , **Tcl_PkgPresentEx** and **Tcl_PkgRequireEx** allow the
setting and retrieving of the client data associated with the package. In all
other respects they are equivalent to the matching functions.

**Tcl_PkgRequireProc** is the form of **[package
require](../TclCmd/package.md)** handling multiple requirements. The other
forms are present for backward compatibility and translate their invocations to
this form.

### KEYWORDS

[package](../Keywords/P.htm#package), [present](../Keywords/P.htm#present),
[provide](../Keywords/P.htm#provide), [require](../Keywords/R.htm#require),
[version](../Keywords/V.htm#version)

### SEE ALSO

**[package](../TclCmd/package.md)** ,
**[Tcl_StaticPackage](../TclLib/StaticPkg.md)**

Copyright © 1996 Sun Microsystems, Inc.
