### NAME

Tcl_GetOpenFile — Return a FILE* for a channel registered in the given
interpreter (Unix only)

### SYNOPSIS

**#include <tcl.h>**  
int  
**Tcl_GetOpenFile**(*interp, chanID, write, checkUsage, filePtr*)  

### ARGUMENTS

[Tcl_Interp](../TclLib/Interp.md) ***interp** (in)     Tcl interpreter from
which file handle is to be obtained.

const char ***chanID** (in)     String identifying channel, such as
**[stdin](../TclLib/GetStdChan.md)** or **file4**.

int **write** (in)     Non-zero means the file will be used for writing, zero
means it will be used for reading.

int **checkUsage** (in)     If non-zero, then an error will be generated if the
file was not opened for the access indicated by *write*.

ClientData ***filePtr** (out)     Points to word in which to store pointer to
FILE structure for the file given by *chanID*.

### DESCRIPTION

**Tcl_GetOpenFile** takes as argument a file identifier of the form returned by
the **[open](../TclCmd/open.md)** command and returns at **filePtr* a pointer
to the FILE structure for the file. The *write* argument indicates whether the
FILE pointer will be used for reading or writing. In some cases, such as a
channel that connects to a pipeline of subprocesses, different FILE pointers
will be returned for reading and writing. **Tcl_GetOpenFile** normally returns
**[TCL_OK](../TclCmd/catch.md)**. If an error occurs in **Tcl_GetOpenFile**
(e.g. *chanID* did not make any sense or *checkUsage* was set and the file was
not opened for the access specified by *write*) then
**[TCL_ERROR](../TclCmd/catch.md)** is returned and the interpreter's result
will contain an error message. In the current implementation *checkUsage* is
ignored and consistency checks are always performed.

Note that this interface is only supported on the Unix platform.

### KEYWORDS

[channel](../Keywords/C.htm#channel), [file handle](../Keywords/F.htm#file
handle), [permissions](../Keywords/P.htm#permissions),
[pipeline](../Keywords/P.htm#pipeline), [read](../Keywords/R.htm#read),
[write](../Keywords/W.htm#write)

Copyright © 1996-1997 Sun Microsystems, Inc.
