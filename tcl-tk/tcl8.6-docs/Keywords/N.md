## [Tcl8.6.18/Tk8.6.18 Documentation](../contents.md) > Tcl/Tk Keywords - N

### [Tcl/Tk Applications](../UserCmd/contents.md) | [Tcl Commands](../TclCmd/contents.md) | [Tk Commands](../TkCmd/contents.md) | [[incr Tcl] Package Commands](../ItclCmd/contents.md) | [SQLite3 Package Commands](../SqliteCmd/contents.md) | [TDBC Package Commands](../TdbcCmd/contents.md) | [tdbc::mysql Package Commands](../TdbcmysqlCmd/contents.md) | [tdbc::odbc Package Commands](../TdbcodbcCmd/contents.md) | [tdbc::postgres Package Commands](../TdbcpostgresCmd/contents.md) | [tdbc::sqlite3 Package Commands](../TdbcsqliteCmd/contents.md) | [Thread Package Commands](../ThreadCmd/contents.md) | [Tcl C API](../TclLib/contents.md) | [Tk C API](../TkLib/contents.md) | [[incr Tcl] Package C API](../ItclLib/contents.md) | [TDBC Package C API](../TdbcLib/contents.md)

### [A](A.md) | [B](B.md) | [C](C.md) | [D](D.md) | [E](E.md) | [F](F.md) | [G](G.md) | [H](H.md) | [I](I.md) | [J](J.md) | [K](K.md) | [L](L.md) | [M](M.md) | [N](N.md) | [O](O.md) | [P](P.md) | [Q](Q.md) | [R](R.md) | [S](S.md) | [T](T.md) | [U](U.md) | [V](V.md) | [W](W.md) | [X](X.md) | [Y](Y.md) | [Z](Z.md)

name

     [dde](../TclCmd/dde.md "dde - Execute a Dynamic Data Exchange command"), [file](../TclCmd/file.md "file - Manipulate file names and attributes"), [options](../TkCmd/options.md "options - Standard options supported by widgets"), [send](../TkCmd/send.md "send - Execute a command in a different application"), [AddOption](../TkLib/AddOption.md "Tk_AddOption - Add an option to the option database"), [GetOption](../TkLib/GetOption.md "Tk_GetOption - retrieve an option from the option database"), [GetRelief](../TkLib/GetRelief.md "Tk_GetReliefFromObj, Tk_GetRelief, Tk_NameOfRelief - translate between strings and relief values"), [Name](../TkLib/Name.md "Tk_Name, Tk_PathName, Tk_NameToWindow - convert between names and window tokens"), [SetAppName](../TkLib/SetAppName.md "Tk_SetAppName - Set the name of an application for 'send' commands")
namespace

     [global](../TclCmd/global.md "global - Access global variables"), [info](../TclCmd/info.md "info - Return information about the state of the Tcl interpreter"), [rename](../TclCmd/rename.md "rename - Rename or delete a command"), [uplevel](../TclCmd/uplevel.md "uplevel - Execute a script in a different stack frame"), [upvar](../TclCmd/upvar.md "upvar - Create link to variable in a different stack frame"), [variable](../TclCmd/variable.md "variable - create and initialize a namespace variable"), [code](../ItclCmd/code.md "itcl::code - capture the namespace context for a code fragment"), [delete](../ItclCmd/delete.md "itcl::delete - delete things in the interpreter"), [itcl](../ItclCmd/itcl.md "itcl - object-oriented extensions to Tcl"), [scope](../ItclCmd/scope.md "itcl::scope - capture the namespace context for a variable"), [CrtCommand](../TclLib/CrtCommand.md "Tcl_CreateCommand - implement new commands in C"), [CrtObjCmd](../TclLib/CrtObjCmd.md "Tcl_CreateObjCommand, Tcl_DeleteCommand, Tcl_DeleteCommandFromToken, Tcl_GetCommandInfo, Tcl_GetCommandInfoFromToken, Tcl_SetCommandInfo, Tcl_SetCommandInfoFromToken, Tcl_GetCommandName, Tcl_GetCommandFullName, Tcl_GetCommandFromObj - implement new commands in C"), [Namespace](../TclLib/Namespace.md "Tcl_AppendExportList, Tcl_CreateNamespace, Tcl_DeleteNamespace, Tcl_Export, Tcl_FindCommand, Tcl_FindNamespace, Tcl_ForgetImport, Tcl_GetCurrentNamespace, Tcl_GetGlobalNamespace, Tcl_GetNamespaceUnknownHandler, Tcl_Import, Tcl_SetNamespaceUnknownHandler - manipulate namespaces")
nesting depth

     [SetRecLmt](../TclLib/SetRecLmt.md "Tcl_SetRecursionLimit - set maximum allowable nesting depth in interpreter")
network address

     [socket](../TclCmd/socket.md "socket - Open a TCP network connection")
newline

     [fconfigure](../TclCmd/fconfigure.md "fconfigure - Set and get options on a channel"), [puts](../TclCmd/puts.md "puts - Write to a channel")
non-blocking

     [chan](../TclCmd/chan.md "chan - Read, write and manipulate channels"), [gets](../TclCmd/gets.md "gets - Read a line from a channel"), [open](../TclCmd/open.md "open - Open a file-based or command pipeline channel")
non-existent command

     [unknown](../TclCmd/unknown.md "unknown - Handle attempts to use non-existent commands")
nonblocking

     [close](../TclCmd/close.md "close - Close an open channel"), [fblocked](../TclCmd/fblocked.md "fblocked - Test whether the last input operation exhausted all available input"), [fconfigure](../TclCmd/fconfigure.md "fconfigure - Set and get options on a channel"), [fcopy](../TclCmd/fcopy.md "fcopy - Copy data from one channel to another"), [fileevent](../TclCmd/fileevent.md "fileevent - Execute a script when a channel becomes readable or writable"), [flush](../TclCmd/flush.md "flush - Flush buffered output for a channel"), [read](../TclCmd/read.md "read - Read from a channel"), [CrtChannel](../TclLib/CrtChannel.md "Tcl_CreateChannel, Tcl_GetChannelInstanceData, Tcl_GetChannelType, Tcl_GetChannelName, Tcl_GetChannelHandle, Tcl_GetChannelMode, Tcl_GetChannelBufferSize, Tcl_SetChannelBufferSize, Tcl_NotifyChannel, Tcl_BadChannelOption, Tcl_ChannelName, Tcl_ChannelVersion, Tcl_ChannelBlockModeProc, Tcl_ChannelCloseProc, Tcl_ChannelClose2Proc, Tcl_ChannelInputProc, Tcl_ChannelOutputProc, Tcl_ChannelSeekProc, Tcl_ChannelWideSeekProc, Tcl_ChannelTruncateProc, Tcl_ChannelSetOptionProc, Tcl_ChannelGetOptionProc, Tcl_ChannelWatchProc, Tcl_ChannelGetHandleProc, Tcl_ChannelFlushProc, Tcl_ChannelHandlerProc, Tcl_ChannelThreadActionProc, Tcl_IsChannelShared, Tcl_IsChannelRegistered, Tcl_CutChannel, Tcl_SpliceChannel, Tcl_IsChannelExisting, Tcl_ClearChannelHandlers, Tcl_GetChannelThread, Tcl_ChannelBuffered - procedures for creating and manipulating channels"), [CrtChnlHdlr](../TclLib/CrtChnlHdlr.md "Tcl_CreateChannelHandler, Tcl_DeleteChannelHandler - call a procedure when a channel becomes readable or writable"), [OpenFileChnl](../TclLib/OpenFileChnl.md "Tcl_OpenFileChannel, Tcl_OpenCommandChannel, Tcl_MakeFileChannel, Tcl_GetChannel, Tcl_GetChannelNames, Tcl_GetChannelNamesEx, Tcl_RegisterChannel, Tcl_UnregisterChannel, Tcl_DetachChannel, Tcl_IsStandardChannel, Tcl_Close, Tcl_CloseEx, Tcl_ReadChars, Tcl_Read, Tcl_GetsObj, Tcl_Gets, Tcl_WriteObj, Tcl_WriteChars, Tcl_Write, Tcl_Flush, Tcl_Seek, Tcl_Tell, Tcl_TruncateChannel, Tcl_GetChannelOption, Tcl_SetChannelOption, Tcl_Eof, Tcl_InputBlocked, Tcl_InputBuffered, Tcl_OutputBuffered, Tcl_Ungets, Tcl_ReadRaw, Tcl_WriteRaw - buffered I/O facilities using channels")
nonrecursive

     [NRE](../TclLib/NRE.md "Tcl_NRCreateCommand, Tcl_NRCallObjProc, Tcl_NREvalObj, Tcl_NREvalObjv, Tcl_NRCmdSwap, Tcl_NRExprObj, Tcl_NRAddCallback - Non-Recursive \(stackless\) evaluation of Tcl scripts.")
notifier

     [Notifier](../TclLib/Notifier.md "Tcl_CreateEventSource, Tcl_DeleteEventSource, Tcl_SetMaxBlockTime, Tcl_QueueEvent, Tcl_ThreadQueueEvent, Tcl_ThreadAlert, Tcl_GetCurrentThread, Tcl_DeleteEvents, Tcl_InitNotifier, Tcl_FinalizeNotifier, Tcl_WaitForEvent, Tcl_AlertNotifier, Tcl_SetTimer, Tcl_ServiceAll, Tcl_ServiceEvent, Tcl_GetServiceMode, Tcl_SetServiceMode, Tcl_ServiceModeHook, Tcl_SetNotifier - the event queue and notifier interfaces")
NSImage

     [tk_mac](../TkCmd/tk_mac.md "tk::mac - Access Mac-Specific Functionality on macOS from Tk")

Copyright © 1989-1994 The Regents of the University of California  
Copyright © 1992-1999 Karl Lehenbauer & Mark Diekhans  
Copyright © 1993-1997 Bell Labs Innovations for Lucent Technologies  
Copyright © 1993-1998 Lucent Technologies, Inc  
Copyright © 1994 The Australian National University  
Copyright © 1994-2000 Sun Microsystems, Inc  
Copyright © 1997-2000 Ajuba Solutions  
Copyright © 1997-2000 Scriptics Corporation  
Copyright © 1998 Mark Harrison  
Copyright © 2000 Jeffrey Hobbs  
Copyright © 2001 ActiveState Tool Corp  
Copyright © 2001 Vincent Darley  
Copyright © 2001-2004 ActiveState Corporation  
Copyright © 2001-2005 Kevin B. Kenny <kennykb(at)acm.org>  
Copyright © 2001-2012 Donal K. Fellows  
Copyright © 2002-2010 Andreas Kupries
<andreas_kupries(at)users.sourceforge.net>  
Copyright © 2003 George Petasis <petasis(at)iit.demokritos.gr>  
Copyright © 2003 Simon Geard  
Copyright © 2003-2006 Joe English  
Copyright © 2005 Sergey Brester aka sebres  
Copyright © 2006 Miguel Sofer  
Copyright © 2006-2008 ActiveState Software Inc  
Copyright © 2006-2008 Daniel A. Steffen <das(at)users.sourceforge.net>  
Copyright © 2006-2008 Joe Mistachkin  
Copyright © 2008 Arnulf Wiedemann  
Copyright © 2008 Jos Decoster  
Copyright © 2008 Pat Thoyts  
Copyright © 2008 Peter Spjuth <pspjuth(at)users.sourceforge.net>  
Copyright © 2008-2010 Kevin B. Kenny  
Copyright © 2011 Kevin Walzer  
Copyright © 2012 Trevor Davel
