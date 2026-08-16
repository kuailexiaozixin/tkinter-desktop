### NAME

Tcl_CreateCloseHandler, Tcl_DeleteCloseHandler — arrange for callbacks when
channels are closed

### SYNOPSIS

**#include <tcl.h>**  
void  
**Tcl_CreateCloseHandler**(*channel, proc, clientData*)  
void  
**Tcl_DeleteCloseHandler**(*channel, proc, clientData*)  

### ARGUMENTS

[Tcl_Channel](../TclLib/OpenFileChnl.md) **channel** (in)     The channel for
which to create or delete a close callback.

Tcl_CloseProc ***proc** (in)     The procedure to call as the callback.

ClientData **clientData** (in)     Arbitrary one-word value to pass to *proc*.

### DESCRIPTION

**Tcl_CreateCloseHandler** arranges for *proc* to be called when *channel* is
closed with **[Tcl_Close](../TclLib/OpenFileChnl.md)** or
**[Tcl_UnregisterChannel](../TclLib/OpenFileChnl.md)** , or using the Tcl
**[close](../TclCmd/close.md)** command. *Proc* should match the following
prototype:

    
    
    typedef void **Tcl_CloseProc**(
            ClientData *clientData*);

The *clientData* is the same as the value provided in the call to
**Tcl_CreateCloseHandler**.

**Tcl_DeleteCloseHandler** removes a close callback for *channel*. The *proc*
and *clientData* identify which close callback to remove;
**Tcl_DeleteCloseHandler** does nothing if its *proc* and *clientData*
arguments do not match the *proc* and *clientData* for a close handler for
*channel*.

### SEE ALSO

**[close](../TclCmd/close.md)** , **[Tcl_Close](../TclLib/OpenFileChnl.md)**
, **[Tcl_UnregisterChannel](../TclLib/OpenFileChnl.md)**

### KEYWORDS

[callback](../Keywords/C.htm#callback), [channel
closing](../Keywords/C.htm#channel closing)

Copyright © 1994-1996 Sun Microsystems, Inc.
