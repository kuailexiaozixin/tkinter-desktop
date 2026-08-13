### NAME

Tcl_SetChannelError, Tcl_SetChannelErrorInterp, Tcl_GetChannelError,
Tcl_GetChannelErrorInterp — functions to create/intercept Tcl errors by channel
drivers.

### SYNOPSIS

**#include <tcl.h>**  
void  
**Tcl_SetChannelError**(*chan, msg*)  
void  
**Tcl_SetChannelErrorInterp**(*interp, msg*)  
void  
**Tcl_GetChannelError**(*chan, msgPtr*)  
void  
**Tcl_GetChannelErrorInterp**(*interp, msgPtr*)  

### ARGUMENTS

[Tcl_Channel](../TclLib/OpenFileChnl.md) **[chan](../TclCmd/chan.md)** (in)
Refers to the Tcl channel whose bypass area is accessed.

[Tcl_Interp](../TclLib/Interp.md)* **[interp](../TclCmd/interp.md)** (in)
Refers to the Tcl interpreter whose bypass area is accessed.

[Tcl_Obj](../TclLib/Object.md)* **msg** (in)     Error message put into a
bypass area. A list of return options and values, followed by a string message.
Both message and the option/value information are optional.

[Tcl_Obj](../TclLib/Object.md)** **msgPtr** (out)     Reference to a place
where the message stored in the accessed bypass area can be stored in.

### DESCRIPTION

The current definition of a Tcl channel driver does not permit the direct
return of arbitrary error messages, except for the setting and retrieval of
channel options. All other functions are restricted to POSIX error codes.

The functions described here overcome this limitation. Channel drivers are
allowed to use **Tcl_SetChannelError** and **Tcl_SetChannelErrorInterp** to
place arbitrary error messages in **bypass areas** defined for channels and
interpreters. And the generic I/O layer uses **Tcl_GetChannelError** and
**Tcl_GetChannelErrorInterp** to look for messages in the bypass areas and
arrange for their return as errors. The POSIX error codes set by a driver are
used now if and only if no messages are present.

**Tcl_SetChannelError** stores error information in the bypass area of the
specified channel. The number of references to the **msg** value goes up by
one. Previously stored information will be discarded, by releasing the
reference held by the channel. The channel reference must not be NULL.

**Tcl_SetChannelErrorInterp** stores error information in the bypass area of
the specified interpreter. The number of references to the **msg** value goes
up by one. Previously stored information will be discarded, by releasing the
reference held by the interpreter. The interpreter reference must not be NULL.

**Tcl_GetChannelError** places either the error message held in the bypass area
of the specified channel into *msgPtr* , or NULL; and resets the bypass, that
is, after an invocation all following invocations will return NULL, until an
intervening invocation of **Tcl_SetChannelError** with a non-NULL message. The
*msgPtr* must not be NULL. The reference count of the message is not touched.
The reference previously held by the channel is now held by the caller of the
function and it is its responsibility to release that reference when it is done
with the value.

**Tcl_GetChannelErrorInterp** places either the error message held in the
bypass area of the specified interpreter into *msgPtr* , or NULL; and resets
the bypass, that is, after an invocation all following invocations will return
NULL, until an intervening invocation of **Tcl_SetChannelErrorInterp** with a
non-NULL message. The *msgPtr* must not be NULL. The reference count of the
message is not touched. The reference previously held by the interpreter is now
held by the caller of the function and it is its responsibility to release that
reference when it is done with the value.

Which functions of a channel driver are allowed to use which bypass function is
listed below, as is which functions of the public channel API may leave a
messages in the bypass areas.

**Tcl_DriverCloseProc**     May use **Tcl_SetChannelErrorInterp** , and only
this function.

**Tcl_DriverInputProc**     May use **Tcl_SetChannelError** , and only this
function.

**Tcl_DriverOutputProc**     May use **Tcl_SetChannelError** , and only this
function.

**Tcl_DriverSeekProc**     May use **Tcl_SetChannelError** , and only this
function.

**Tcl_DriverWideSeekProc**     May use **Tcl_SetChannelError** , and only this
function.

**Tcl_DriverSetOptionProc**     Has already the ability to pass arbitrary error
messages. Must *not* use any of the new functions.

**Tcl_DriverGetOptionProc**     Has already the ability to pass arbitrary error
messages. Must *not* use any of the new functions.

**Tcl_DriverWatchProc**     Must *not* use any of the new functions. Is
internally called and has no ability to return any type of error whatsoever.

**Tcl_DriverBlockModeProc**     May use **Tcl_SetChannelError** , and only this
function.

**Tcl_DriverGetHandleProc**     Must *not* use any of the new functions. It is
only a low-level function, and not used by Tcl commands.

**Tcl_DriverHandlerProc**     Must *not* use any of the new functions. Is
internally called and has no ability to return any type of error whatsoever.

Given the information above the following public functions of the Tcl C API are
affected by these changes; when these functions are called, the channel may now
contain a stored arbitrary error message requiring processing by the caller.

    **[Tcl_Flush](../TclLib/OpenFileChnl.md)**| **[Tcl_GetsObj](../TclLib/OpenFileChnl.md)**| **[Tcl_Gets](../TclLib/OpenFileChnl.md)**| **[Tcl_ReadChars](../TclLib/OpenFileChnl.md)**| **[Tcl_ReadRaw](../TclLib/OpenFileChnl.md)**| **[Tcl_Read](../TclLib/OpenFileChnl.md)**| **[Tcl_Seek](../TclLib/OpenFileChnl.md)**| **[Tcl_StackChannel](../TclLib/ChnlStack.md)**| **[Tcl_Tell](../TclLib/OpenFileChnl.md)**| **[Tcl_WriteChars](../TclLib/OpenFileChnl.md)**| **[Tcl_WriteObj](../TclLib/OpenFileChnl.md)**| **[Tcl_WriteRaw](../TclLib/OpenFileChnl.md)**| **[Tcl_Write](../TclLib/OpenFileChnl.md)** All other API functions are unchanged. In particular, the functions below leave all their error information in the interpreter result. 

    | **[Tcl_Close](../TclLib/OpenFileChnl.md)**| **[Tcl_UnstackChannel](../TclLib/ChnlStack.md)**| **[Tcl_UnregisterChannel](../TclLib/OpenFileChnl.md)**

### SEE ALSO

**[Tcl_Close](../TclLib/OpenFileChnl.md)** ,
**[Tcl_OpenFileChannel](../TclLib/OpenFileChnl.md)** ,
**[Tcl_SetErrno](../TclLib/SetErrno.md)**

### KEYWORDS

[channel driver](../Keywords/C.htm#channel driver), [error
messages](../Keywords/E.htm#error messages), [channel
type](../Keywords/C.htm#channel type) Copyright © 2005 Andreas Kupries
<andreas_kupries(at)users.sourceforge.net>
