### NAME

Tcl_GetStdChannel, Tcl_SetStdChannel — procedures for retrieving and replacing
the standard channels

### SYNOPSIS

**#include <tcl.h>**  
[Tcl_Channel](../TclLib/OpenFileChnl.md)  
**Tcl_GetStdChannel**(*type*)  
**Tcl_SetStdChannel**(*channel, type*)  

### ARGUMENTS

int **type** (in)     The identifier for the standard channel to retrieve or
modify. Must be one of **TCL_STDIN** , **TCL_STDOUT** , or **TCL_STDERR**.

[Tcl_Channel](../TclLib/OpenFileChnl.md) **channel** (in)     The channel to
use as the new value for the specified standard channel.

### DESCRIPTION

Tcl defines three special channels that are used by various I/O related
commands if no other channels are specified. The standard input channel has a
channel name of **stdin** and is used by **[read](../TclCmd/read.md)** and
**[gets](../TclCmd/gets.md)**. The standard output channel is named **stdout**
and is used by **[puts](../TclCmd/puts.md)**. The standard error channel is
named **stderr** and is used for reporting errors. In addition, the standard
channels are inherited by any child processes created using
**[exec](../TclCmd/exec.md)** or **[open](../TclCmd/open.md)** in the absence
of any other redirections.

The standard channels are actually aliases for other normal channels. The
current channel associated with a standard channel can be retrieved by calling
**Tcl_GetStdChannel** with one of **TCL_STDIN** , **TCL_STDOUT** , or
**TCL_STDERR** as the *type*. The return value will be a valid channel, or
NULL.

A new channel can be set for the standard channel specified by *type* by
calling **Tcl_SetStdChannel** with a new channel or NULL in the *channel*
argument. If the specified channel is closed by a later call to
**[Tcl_Close](../TclLib/OpenFileChnl.md)** , then the corresponding standard
channel will automatically be set to NULL.

If a non-NULL value for *channel* is passed to **Tcl_SetStdChannel** , then
that same value should be passed to
**[Tcl_RegisterChannel](../TclLib/OpenFileChnl.md)** , like so:

    
    
    [Tcl_RegisterChannel](../TclLib/OpenFileChnl.md)(NULL, channel);

This is a workaround for a misfeature in **Tcl_SetStdChannel** that it fails to
do some reference counting housekeeping. This misfeature cannot be corrected
without contradicting the assumptions of some existing code that calls
**Tcl_SetStdChannel**.

If **Tcl_GetStdChannel** is called before **Tcl_SetStdChannel** , Tcl will
construct a new channel to wrap the appropriate platform-specific standard file
handle. If **Tcl_SetStdChannel** is called before **Tcl_GetStdChannel** , then
the default channel will not be created.

If one of the standard channels is set to NULL, either by calling
**Tcl_SetStdChannel** with a NULL *channel* argument, or by calling
**[Tcl_Close](../TclLib/OpenFileChnl.md)** on the channel, then the next call
to **[Tcl_CreateChannel](../TclLib/CrtChannel.md)** will automatically set the
standard channel with the newly created channel. If more than one standard
channel is NULL, then the standard channels will be assigned starting with
standard input, followed by standard output, with standard error being last.

See **[Tcl_StandardChannels](../TclLib/StdChannels.md)** for a general
treatise about standard channels and the behavior of the Tcl library with
regard to them.

### SEE ALSO

**[Tcl_Close](../TclLib/OpenFileChnl.md)** ,
**[Tcl_CreateChannel](../TclLib/CrtChannel.md)** ,
**[Tcl_Main](../TclLib/Tcl_Main.md)** , **[tclsh](../UserCmd/tclsh.md)**

### KEYWORDS

[standard channel](../Keywords/S.htm#standard channel), [standard
input](../Keywords/S.htm#standard input), [standard
output](../Keywords/S.htm#standard output), [standard
error](../Keywords/S.htm#standard error)

Copyright © 1996 Sun Microsystems, Inc.
