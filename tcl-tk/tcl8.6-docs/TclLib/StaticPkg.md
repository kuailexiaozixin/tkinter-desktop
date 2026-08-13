### NAME

Tcl_StaticPackage — make a statically linked package available via the 'load'
command

### SYNOPSIS

**#include <tcl.h>**  
**Tcl_StaticPackage**(*interp, prefix, initProc, safeInitProc*)  

### ARGUMENTS

[Tcl_Interp](../TclLib/Interp.md) ***interp** (in)     If not NULL, points to
an interpreter into which the package has already been loaded (i.e., the caller
has already invoked the appropriate initialization procedure). NULL means the
package has not yet been incorporated into any interpreter.

const char ***prefix** (in)     Prefix for library initialization function;
should be properly capitalized (first letter upper-case, all others lower-
case).

Tcl_PackageInitProc ***initProc** (in)     Procedure to invoke to incorporate
this package into a trusted interpreter.

Tcl_PackageInitProc ***safeInitProc** (in)     Procedure to call to incorporate
this package into a safe interpreter (one that will execute untrusted scripts).
NULL means the package cannot be used in safe interpreters.

### DESCRIPTION

This procedure may be invoked to announce that a package has been linked
statically with a Tcl application and, optionally, that it has already been
loaded into an interpreter. Once **Tcl_StaticPackage** has been invoked for a
package, it may be loaded into interpreters using the
**[load](../TclCmd/load.md)** command. **Tcl_StaticPackage** is normally
invoked only by the **[Tcl_AppInit](../TclLib/AppInit.md)** procedure for the
application, not by packages for themselves (**Tcl_StaticPackage** should only
be invoked for statically loaded packages, and code in the package itself
should not need to know whether the package is dynamically or statically
loaded).

When the **[load](../TclCmd/load.md)** command is used later to load the
package into an interpreter, one of *initProc* and *safeInitProc* will be
invoked, depending on whether the target interpreter is safe or not. *initProc*
and *safeInitProc* must both match the following prototype:

    
    
    typedef int **Tcl_PackageInitProc**(
            [Tcl_Interp](../TclLib/Interp.md) **interp*);

The *interp* argument identifies the interpreter in which the package is to be
loaded. The initialization procedure must return
**[TCL_OK](../TclCmd/catch.md)** or **[TCL_ERROR](../TclCmd/catch.md)** to
indicate whether or not it completed successfully; in the event of an error it
should set the interpreter's result to point to an error message. The result or
error from the initialization procedure will be returned as the result of the
**[load](../TclCmd/load.md)** command that caused the initialization procedure
to be invoked.

### KEYWORDS

[initialization procedure](../Keywords/I.htm#initialization procedure),
[package](../Keywords/P.htm#package), [static linking](../Keywords/S.htm#static
linking)

### SEE ALSO

**[load](../TclCmd/load.md)** , **[package](../TclCmd/package.md)** ,
**[Tcl_PkgRequire](../TclLib/PkgRequire.md)**

Copyright © 1995-1996 Sun Microsystems, Inc.
