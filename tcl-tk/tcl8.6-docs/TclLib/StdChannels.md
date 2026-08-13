### NAME

Tcl_StandardChannels — How the Tcl library deals with the standard channels

### DESCRIPTION

This page explains the initialization and use of standard channels in the Tcl
library.

The term *standard channels* comes out of the Unix world and refers to the
three channels automatically opened by the OS for each new application. They
are **[stdin](../TclLib/GetStdChan.md)** ,
**[stdout](../TclLib/GetStdChan.md)** and
**[stderr](../TclLib/GetStdChan.md)**. The first is the standard input an
application can read from, the other two refer to writable channels, one for
regular output and the other for error messages.

Tcl generalizes this concept in a cross-platform way and exposes standard
channels to the script level.

#### APPLICATION PROGRAMMING INTERFACES

The public API procedures dealing directly with standard channels are
**[Tcl_GetStdChannel](../TclLib/GetStdChan.md)** and
**[Tcl_SetStdChannel](../TclLib/GetStdChan.md)**. Additional public APIs to
consider are **[Tcl_RegisterChannel](../TclLib/OpenFileChnl.md)** ,
**[Tcl_CreateChannel](../TclLib/CrtChannel.md)** and
**[Tcl_GetChannel](../TclLib/OpenFileChnl.md)**.

### INITIALIZATION OF TCL STANDARD CHANNELS

Standard channels are initialized by the Tcl library in three cases: when
explicitly requested, when implicitly required before returning channel
information, or when implicitly required during registration of a new channel.

These cases differ in how they handle unavailable platform- specific standard
channels. (A channel is not “available” if it could not be successfully opened;
for example, in a Tcl application run as a Windows NT service.)

  1. A single standard channel is initialized when it is explicitly specified in a call to **[Tcl_SetStdChannel](../TclLib/GetStdChan.md)**. The states of the other standard channels are unaffected. 

Missing platform-specific standard channels do not matter here. This approach
is not available at the script level.

  2. All uninitialized standard channels are initialized to platform-specific default values: 

     1. when open channels are listed with **[Tcl_GetChannelNames](../TclLib/OpenFileChnl.md)** (or the **[file channels](../TclCmd/file.md)** script command), or 

     2. when information about any standard channel is requested with a call to **[Tcl_GetStdChannel](../TclLib/GetStdChan.md)** , or with a call to **[Tcl_GetChannel](../TclLib/OpenFileChnl.md)** which specifies one of the standard names (**[stdin](../TclLib/GetStdChan.md)** , **[stdout](../TclLib/GetStdChan.md)** and **[stderr](../TclLib/GetStdChan.md)**). 

In case of missing platform-specific standard channels, the Tcl standard
channels are considered as initialized and then immediately closed. This means
that the first three Tcl channels then opened by the application are designated
as the Tcl standard channels.

  3. All uninitialized standard channels are initialized to platform-specific default values when a user-requested channel is registered with **[Tcl_RegisterChannel](../TclLib/OpenFileChnl.md)**. 

In case of unavailable platform-specific standard channels the channel whose
creation caused the initialization of the Tcl standard channels is made a
normal channel. The next three Tcl channels opened by the application are
designated as the Tcl standard channels. In other words, of the first four Tcl
channels opened by the application the second to fourth are designated as the
Tcl standard channels.

### RE-INITIALIZATION OF TCL STANDARD CHANNELS

Once a Tcl standard channel is initialized through one of the methods above,
closing this Tcl standard channel will cause the next call to
**[Tcl_CreateChannel](../TclLib/CrtChannel.md)** to make the new channel the
new standard channel, too. If more than one Tcl standard channel was closed
**[Tcl_CreateChannel](../TclLib/CrtChannel.md)** will fill the empty slots in
the order **[stdin](../TclLib/GetStdChan.md)** ,
**[stdout](../TclLib/GetStdChan.md)** and
**[stderr](../TclLib/GetStdChan.md)**.

**[Tcl_CreateChannel](../TclLib/CrtChannel.md)** will not try to reinitialize
an empty slot if that slot was not initialized before. It is this behavior
which enables an application to employ method 1 of initialization, i.e. to
create and designate their own Tcl standard channels.

### SHELL-SPECIFIC DETAILS

#### tclsh

The Tcl shell (or rather the function **[Tcl_Main](../TclLib/Tcl_Main.md)** ,
which forms the core of the shell's implementation) uses method 2 to initialize
the standard channels.

#### wish

The windowing shell (or rather the function **Tk_MainEx** , which forms the
core of the shell's implementation) uses method 1 to initialize the standard
channels (See **[Tk_InitConsoleChannels](../TkLib/CrtConsoleChan.md)**) on
non-Unix platforms. On Unix platforms, **Tk_MainEx** implicitly uses method 2
to initialize the standard channels.

### SEE ALSO

**[Tcl_CreateChannel](../TclLib/CrtChannel.md)** ,
**[Tcl_RegisterChannel](../TclLib/OpenFileChnl.md)** ,
**[Tcl_GetChannel](../TclLib/OpenFileChnl.md)** ,
**[Tcl_GetStdChannel](../TclLib/GetStdChan.md)** ,
**[Tcl_SetStdChannel](../TclLib/GetStdChan.md)** ,
**[Tk_InitConsoleChannels](../TkLib/CrtConsoleChan.md)** ,
**[tclsh](../UserCmd/tclsh.md)** , **[wish](../UserCmd/wish.md)** ,
**[Tcl_Main](../TclLib/Tcl_Main.md)** , **Tk_MainEx**

### KEYWORDS

[standard channels](../Keywords/S.htm#standard channels)

Copyright © 2001 ActiveState Corporation
