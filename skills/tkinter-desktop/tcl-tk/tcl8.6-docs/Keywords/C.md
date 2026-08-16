## [Tcl8.6.18/Tk8.6.18 Documentation](../contents.md) > Tcl/Tk Keywords - C

### [Tcl/Tk Applications](../UserCmd/contents.md) | [Tcl Commands](../TclCmd/contents.md) | [Tk Commands](../TkCmd/contents.md) | [[incr Tcl] Package Commands](../ItclCmd/contents.md) | [SQLite3 Package Commands](../SqliteCmd/contents.md) | [TDBC Package Commands](../TdbcCmd/contents.md) | [tdbc::mysql Package Commands](../TdbcmysqlCmd/contents.md) | [tdbc::odbc Package Commands](../TdbcodbcCmd/contents.md) | [tdbc::postgres Package Commands](../TdbcpostgresCmd/contents.md) | [tdbc::sqlite3 Package Commands](../TdbcsqliteCmd/contents.md) | [Thread Package Commands](../ThreadCmd/contents.md) | [Tcl C API](../TclLib/contents.md) | [Tk C API](../TkLib/contents.md) | [[incr Tcl] Package C API](../ItclLib/contents.md) | [TDBC Package C API](../TdbcLib/contents.md)

### [A](A.md) | [B](B.md) | [C](C.md) | [D](D.md) | [E](E.md) | [F](F.md) | [G](G.md) | [H](H.md) | [I](I.md) | [J](J.md) | [K](K.md) | [L](L.md) | [M](M.md) | [N](N.md) | [O](O.md) | [P](P.md) | [Q](Q.md) | [R](R.md) | [S](S.md) | [T](T.md) | [U](U.md) | [V](V.md) | [W](W.md) | [X](X.md) | [Y](Y.md) | [Z](Z.md)

cache

     [InternAtom](../TkLib/InternAtom.md "Tk_InternAtom, Tk_GetAtomName - manage cache of X atoms")
call

     [next](../TclCmd/next.md "next, nextto - invoke superclass method implementations"), [self](../TclCmd/self.md "self - method call internal introspection"), [tailcall](../TclCmd/tailcall.md "tailcall - Replace the current procedure with another command"), [tdbc_resultset](../TdbcCmd/tdbc_resultset.md "tdbc::resultset - TDBC result set object"), [tdbc_statement](../TdbcCmd/tdbc_statement.md "tdbc::statement - TDBC statement object")
callback

     [code](../ItclCmd/code.md "itcl::code - capture the namespace context for a code fragment"), [CallDel](../TclLib/CallDel.md "Tcl_CallWhenDeleted, Tcl_DontCallWhenDeleted - Arrange for callback when interpreter is deleted"), [CrtChnlHdlr](../TclLib/CrtChnlHdlr.md "Tcl_CreateChannelHandler, Tcl_DeleteChannelHandler - call a procedure when a channel becomes readable or writable"), [CrtCloseHdlr](../TclLib/CrtCloseHdlr.md "Tcl_CreateCloseHandler, Tcl_DeleteCloseHandler - arrange for callbacks when channels are closed"), [CrtFileHdlr](../TclLib/CrtFileHdlr.md "Tcl_CreateFileHandler, Tcl_DeleteFileHandler - associate procedure callbacks with files or devices \(Unix only\)"), [CrtTimerHdlr](../TclLib/CrtTimerHdlr.md "Tcl_CreateTimerHandler, Tcl_DeleteTimerHandler - call a procedure at a given time"), [DoOneEvent](../TclLib/DoOneEvent.md "Tcl_DoOneEvent - wait for events and invoke event handlers"), [DoWhenIdle](../TclLib/DoWhenIdle.md "Tcl_DoWhenIdle, Tcl_CancelIdleCall - invoke a procedure when there are no pending events"), [Exit](../TclLib/Exit.md "Tcl_Exit, Tcl_Finalize, Tcl_CreateExitHandler, Tcl_DeleteExitHandler, Tcl_ExitThread, Tcl_FinalizeThread, Tcl_CreateThreadExitHandler, Tcl_DeleteThreadExitHandler, Tcl_SetExitProc - end the application or thread \(and invoke exit handlers\)"), [Limit](../TclLib/Limit.md "Tcl_LimitAddHandler, Tcl_LimitCheck, Tcl_LimitExceeded, Tcl_LimitGetCommands, Tcl_LimitGetGranularity, Tcl_LimitGetTime, Tcl_LimitReady, Tcl_LimitRemoveHandler, Tcl_LimitSetCommands, Tcl_LimitSetGranularity, Tcl_LimitSetTime, Tcl_LimitTypeEnabled, Tcl_LimitTypeExceeded, Tcl_LimitTypeReset, Tcl_LimitTypeSet - manage and check resource limits on interpreters"), [CrtCmHdlr](../TkLib/CrtCmHdlr.md "Tk_CreateClientMessageHandler, Tk_DeleteClientMessageHandler - associate procedure callback with ClientMessage type X events"), [CrtErrHdlr](../TkLib/CrtErrHdlr.md "Tk_CreateErrorHandler, Tk_DeleteErrorHandler - handle X protocol errors"), [CrtGenHdlr](../TkLib/CrtGenHdlr.md "Tk_CreateGenericHandler, Tk_DeleteGenericHandler - associate procedure callback with all X events"), [EventHndlr](../TkLib/EventHndlr.md "Tk_CreateEventHandler, Tk_DeleteEventHandler - associate procedure callback with an X event"), [HandleEvent](../TkLib/HandleEvent.md "Tk_HandleEvent - invoke event handlers for window system events"), [ManageGeom](../TkLib/ManageGeom.md "Tk_ManageGeometry - arrange to handle geometry requests for a window"), [QWinEvent](../TkLib/QWinEvent.md "Tk_CollapseMotionEvents, Tk_QueueWindowEvent - Add a window event to the Tcl event queue"), [SetClassProcs](../TkLib/SetClassProcs.md "Tk_SetClassProcs - register widget specific procedures")
cancel

     [after](../TclCmd/after.md "after - Execute a command after a time delay"), [Cancel](../TclLib/Cancel.md "Tcl_CancelEval, Tcl_Canceled - cancel Tcl scripts")
canvas

     [canvas](../TkCmd/canvas.md "canvas - Create and manipulate 'canvas' hypergraphics drawing surface widgets"), [CanvPsY](../TkLib/CanvPsY.md "Tk_CanvasPsY, Tk_CanvasPsBitmap, Tk_CanvasPsColor, Tk_CanvasPsFont, Tk_CanvasPsPath, Tk_CanvasPsStipple - utility procedures for generating Postscript for canvases"), [CanvTkwin](../TkLib/CanvTkwin.md "Tk_CanvasTkwin, Tk_CanvasGetCoord, Tk_CanvasDrawableCoords, Tk_CanvasSetStippleOrigin, Tk_CanvasWindowCoords, Tk_CanvasEventuallyRedraw, Tk_CanvasTagsOption - utility procedures for canvas type managers"), [CanvTxtInfo](../TkLib/CanvTxtInfo.md "Tk_CanvasTextInfo - additional information for managing text items in canvases"), [CrtItemType](../TkLib/CrtItemType.md "Tk_CreateItemType, Tk_GetItemTypes - define new kind of canvas item")
cap style

     [ConfigWidg](../TkLib/ConfigWidg.md "Tk_ConfigureWidget, Tk_ConfigureInfo, Tk_ConfigureValue, Tk_FreeOptions - process configuration options for widgets"), [GetCapStyl](../TkLib/GetCapStyl.md "Tk_GetCapStyle, Tk_NameOfCapStyle - translate between strings and cap styles")
caret

     [SetCaret](../TkLib/SetCaret.md "Tk_SetCaretPos - set the display caret location")
carriage return

     [fconfigure](../TclCmd/fconfigure.md "fconfigure - Set and get options on a channel")
case

     [ToUpper](../TclLib/ToUpper.md "Tcl_UniCharToUpper, Tcl_UniCharToLower, Tcl_UniCharToTitle, Tcl_UtfToUpper, Tcl_UtfToLower, Tcl_UtfToTitle - routines for manipulating the case of Unicode characters and UTF-8 strings")
case conversion

     [string](../TclCmd/string.md "string - Manipulate strings")
catch

     [catch](../TclCmd/catch.md "catch - Evaluate script and trap exceptional returns"), [return](../TclCmd/return.md "return - Return from a procedure, or set return code of a script")
cell

     [grid](../TkCmd/grid.md "grid - Geometry manager that arranges widgets in a grid")
center

     [GetJustify](../TkLib/GetJustify.md "Tk_GetJustifyFromObj, Tk_GetJustify, Tk_NameOfJustify - translate between strings and justification styles")
centimeters

     [GetPixels](../TkLib/GetPixels.md "Tk_GetPixelsFromObj, Tk_GetPixels, Tk_GetMMFromObj, Tk_GetScreenMM - translate between strings and screen units")
channel

     [chan](../TclCmd/chan.md "chan - Read, write and manipulate channels"), [close](../TclCmd/close.md "close - Close an open channel"), [eof](../TclCmd/eof.md "eof - Check for end of file condition on channel"), [fcopy](../TclCmd/fcopy.md "fcopy - Copy data from one channel to another"), [fileevent](../TclCmd/fileevent.md "fileevent - Execute a script when a channel becomes readable or writable"), [flush](../TclCmd/flush.md "flush - Flush buffered output for a channel"), [gets](../TclCmd/gets.md "gets - Read a line from a channel"), [puts](../TclCmd/puts.md "puts - Write to a channel"), [read](../TclCmd/read.md "read - Read from a channel"), [refchan](../TclCmd/refchan.md "refchan - command handler API of reflected channels"), [socket](../TclCmd/socket.md "socket - Open a TCP network connection"), [tell](../TclCmd/tell.md "tell - Return current access position for an open channel"), [transchan](../TclCmd/transchan.md "transchan - command handler API of channel transforms"), [ChnlStack](../TclLib/ChnlStack.md "Tcl_StackChannel, Tcl_UnstackChannel, Tcl_GetStackedChannel, Tcl_GetTopChannel - manipulate stacked I/O channels"), [CrtChnlHdlr](../TclLib/CrtChnlHdlr.md "Tcl_CreateChannelHandler, Tcl_DeleteChannelHandler - call a procedure when a channel becomes readable or writable"), [GetOpnFl](../TclLib/GetOpnFl.md "Tcl_GetOpenFile - Return a FILE* for a channel registered in the given interpreter \(Unix only\)"), [OpenFileChnl](../TclLib/OpenFileChnl.md "Tcl_OpenFileChannel, Tcl_OpenCommandChannel, Tcl_MakeFileChannel, Tcl_GetChannel, Tcl_GetChannelNames, Tcl_GetChannelNamesEx, Tcl_RegisterChannel, Tcl_UnregisterChannel, Tcl_DetachChannel, Tcl_IsStandardChannel, Tcl_Close, Tcl_CloseEx, Tcl_ReadChars, Tcl_Read, Tcl_GetsObj, Tcl_Gets, Tcl_WriteObj, Tcl_WriteChars, Tcl_Write, Tcl_Flush, Tcl_Seek, Tcl_Tell, Tcl_TruncateChannel, Tcl_GetChannelOption, Tcl_SetChannelOption, Tcl_Eof, Tcl_InputBlocked, Tcl_InputBuffered, Tcl_OutputBuffered, Tcl_Ungets, Tcl_ReadRaw, Tcl_WriteRaw - buffered I/O facilities using channels"), [OpenTcp](../TclLib/OpenTcp.md "Tcl_OpenTcpClient, Tcl_MakeTcpClientChannel, Tcl_OpenTcpServer - procedures to open channels using TCP sockets")
channel closing

     [CrtCloseHdlr](../TclLib/CrtCloseHdlr.md "Tcl_CreateCloseHandler, Tcl_DeleteCloseHandler - arrange for callbacks when channels are closed")
channel driver

     [CrtChannel](../TclLib/CrtChannel.md "Tcl_CreateChannel, Tcl_GetChannelInstanceData, Tcl_GetChannelType, Tcl_GetChannelName, Tcl_GetChannelHandle, Tcl_GetChannelMode, Tcl_GetChannelBufferSize, Tcl_SetChannelBufferSize, Tcl_NotifyChannel, Tcl_BadChannelOption, Tcl_ChannelName, Tcl_ChannelVersion, Tcl_ChannelBlockModeProc, Tcl_ChannelCloseProc, Tcl_ChannelClose2Proc, Tcl_ChannelInputProc, Tcl_ChannelOutputProc, Tcl_ChannelSeekProc, Tcl_ChannelWideSeekProc, Tcl_ChannelTruncateProc, Tcl_ChannelSetOptionProc, Tcl_ChannelGetOptionProc, Tcl_ChannelWatchProc, Tcl_ChannelGetHandleProc, Tcl_ChannelFlushProc, Tcl_ChannelHandlerProc, Tcl_ChannelThreadActionProc, Tcl_IsChannelShared, Tcl_IsChannelRegistered, Tcl_CutChannel, Tcl_SpliceChannel, Tcl_IsChannelExisting, Tcl_ClearChannelHandlers, Tcl_GetChannelThread, Tcl_ChannelBuffered - procedures for creating and manipulating channels"), [OpenFileChnl](../TclLib/OpenFileChnl.md "Tcl_OpenFileChannel, Tcl_OpenCommandChannel, Tcl_MakeFileChannel, Tcl_GetChannel, Tcl_GetChannelNames, Tcl_GetChannelNamesEx, Tcl_RegisterChannel, Tcl_UnregisterChannel, Tcl_DetachChannel, Tcl_IsStandardChannel, Tcl_Close, Tcl_CloseEx, Tcl_ReadChars, Tcl_Read, Tcl_GetsObj, Tcl_Gets, Tcl_WriteObj, Tcl_WriteChars, Tcl_Write, Tcl_Flush, Tcl_Seek, Tcl_Tell, Tcl_TruncateChannel, Tcl_GetChannelOption, Tcl_SetChannelOption, Tcl_Eof, Tcl_InputBlocked, Tcl_InputBuffered, Tcl_OutputBuffered, Tcl_Ungets, Tcl_ReadRaw, Tcl_WriteRaw - buffered I/O facilities using channels"), [SetChanErr](../TclLib/SetChanErr.md "Tcl_SetChannelError, Tcl_SetChannelErrorInterp, Tcl_GetChannelError, Tcl_GetChannelErrorInterp - functions to create/intercept Tcl errors by channel drivers.")
channel registration

     [CrtChannel](../TclLib/CrtChannel.md "Tcl_CreateChannel, Tcl_GetChannelInstanceData, Tcl_GetChannelType, Tcl_GetChannelName, Tcl_GetChannelHandle, Tcl_GetChannelMode, Tcl_GetChannelBufferSize, Tcl_SetChannelBufferSize, Tcl_NotifyChannel, Tcl_BadChannelOption, Tcl_ChannelName, Tcl_ChannelVersion, Tcl_ChannelBlockModeProc, Tcl_ChannelCloseProc, Tcl_ChannelClose2Proc, Tcl_ChannelInputProc, Tcl_ChannelOutputProc, Tcl_ChannelSeekProc, Tcl_ChannelWideSeekProc, Tcl_ChannelTruncateProc, Tcl_ChannelSetOptionProc, Tcl_ChannelGetOptionProc, Tcl_ChannelWatchProc, Tcl_ChannelGetHandleProc, Tcl_ChannelFlushProc, Tcl_ChannelHandlerProc, Tcl_ChannelThreadActionProc, Tcl_IsChannelShared, Tcl_IsChannelRegistered, Tcl_CutChannel, Tcl_SpliceChannel, Tcl_IsChannelExisting, Tcl_ClearChannelHandlers, Tcl_GetChannelThread, Tcl_ChannelBuffered - procedures for creating and manipulating channels")
channel type

     [CrtChannel](../TclLib/CrtChannel.md "Tcl_CreateChannel, Tcl_GetChannelInstanceData, Tcl_GetChannelType, Tcl_GetChannelName, Tcl_GetChannelHandle, Tcl_GetChannelMode, Tcl_GetChannelBufferSize, Tcl_SetChannelBufferSize, Tcl_NotifyChannel, Tcl_BadChannelOption, Tcl_ChannelName, Tcl_ChannelVersion, Tcl_ChannelBlockModeProc, Tcl_ChannelCloseProc, Tcl_ChannelClose2Proc, Tcl_ChannelInputProc, Tcl_ChannelOutputProc, Tcl_ChannelSeekProc, Tcl_ChannelWideSeekProc, Tcl_ChannelTruncateProc, Tcl_ChannelSetOptionProc, Tcl_ChannelGetOptionProc, Tcl_ChannelWatchProc, Tcl_ChannelGetHandleProc, Tcl_ChannelFlushProc, Tcl_ChannelHandlerProc, Tcl_ChannelThreadActionProc, Tcl_IsChannelShared, Tcl_IsChannelRegistered, Tcl_CutChannel, Tcl_SpliceChannel, Tcl_IsChannelExisting, Tcl_ClearChannelHandlers, Tcl_GetChannelThread, Tcl_ChannelBuffered - procedures for creating and manipulating channels"), [SetChanErr](../TclLib/SetChanErr.md "Tcl_SetChannelError, Tcl_SetChannelErrorInterp, Tcl_GetChannelError, Tcl_GetChannelErrorInterp - functions to create/intercept Tcl errors by channel drivers.")
character

     [string](../TclCmd/string.md "string - Manipulate strings")
check

     [ttk_checkbutton](../TkCmd/ttk_checkbutton.md "ttk::checkbutton - On/off widget")
checkbutton

     [checkbutton](../TkCmd/checkbutton.md "checkbutton - Create and manipulate 'checkbutton' boolean selection widgets")
child

     [CrtAlias](../TclLib/CrtAlias.md "Tcl_IsSafe, Tcl_MakeSafe, Tcl_CreateChild, Tcl_CreateSlave, Tcl_GetChild, Tcl_GetSlave, Tcl_GetParent, Tcl_GetMaster, Tcl_GetInterpPath, Tcl_CreateAlias, Tcl_CreateAliasObj, Tcl_GetAlias, Tcl_GetAliasObj, Tcl_ExposeCommand, Tcl_HideCommand - manage multiple Tcl interpreters, aliases and hidden commands"), [DetachPids](../TclLib/DetachPids.md "Tcl_DetachPids, Tcl_ReapDetachedProcs, Tcl_WaitPid - manage child processes in background")
child interpreter

     [interp](../TclCmd/interp.md "interp - Create and manipulate Tcl interpreters"), [safe](../TclCmd/safe.md "safe - Creating and manipulating safe interpreters"), [loadTk](../TkCmd/loadTk.md "safe::loadTk - Load Tk into a safe interpreter.")
children

     [winfo](../TkCmd/winfo.md "winfo - Return window-related information")
choice

     [ttk_combobox](../TkCmd/ttk_combobox.md "ttk::combobox - text field with popdown selection list")
class

     [class](../TclCmd/class.md "oo::class - class of all classes"), [define](../TclCmd/define.md "oo::define, oo::objdefine, oo::Slot - define and configure classes and objects"), [object](../TclCmd/object.md "oo::object - root class of the class hierarchy"), [options](../TkCmd/options.md "options - Standard options supported by widgets"), [winfo](../TkCmd/winfo.md "winfo - Return window-related information"), [body](../ItclCmd/body.md "itcl::body - change the body for a class method/proc"), [class](../ItclCmd/class.md "itcl::class - create a class of objects"), [configbody](../ItclCmd/configbody.md "itcl::configbody - change the "config" code for a public variable"), [find](../ItclCmd/find.md "itcl::find - search for classes and objects"), [is](../ItclCmd/is.md "itcl::is - test argument to see if it is a class or an object"), [itcl](../ItclCmd/itcl.md "itcl - object-oriented extensions to Tcl"), [local](../ItclCmd/local.md "itcl::local - create an object local to a procedure"), [Class](../TclLib/Class.md "Tcl_ClassGetMetadata, Tcl_ClassSetMetadata, Tcl_CopyObjectInstance, Tcl_GetClassAsObject, Tcl_GetObjectAsClass, Tcl_GetObjectCommand, Tcl_GetObjectFromObj, Tcl_GetObjectName, Tcl_GetObjectNamespace, Tcl_NewObjectInstance, Tcl_ObjectDeleted, Tcl_ObjectGetMetadata, Tcl_ObjectGetMethodNameMapper, Tcl_ObjectSetMetadata, Tcl_ObjectSetMethodNameMapper - manipulate objects and classes"), [AddOption](../TkLib/AddOption.md "Tk_AddOption - Add an option to the option database"), [GetOption](../TkLib/GetOption.md "Tk_GetOption - retrieve an option from the option database"), [SetClass](../TkLib/SetClass.md "Tk_SetClass, Tk_Class - set or retrieve a window's class"), [SetClassProcs](../TkLib/SetClassProcs.md "Tk_SetClassProcs - register widget specific procedures"), [Class](../ItclLib/Class.md "Itcl_CreateClass, Itcl_DeleteClass, Itcl_FindClass, Itcl_IsClass, Itcl_IsClassNamespace - Manipulate classes."), [RegisterC](../ItclLib/RegisterC.md "Itcl_RegisterC, Itcl_RegisterObjC, Itcl_RegisterObjC2, Itcl_FindC, Itcl_FindC2 - Associate a symbolic name with a C procedure.")
classification

     [UniCharIsAlpha](../TclLib/UniCharIsAlpha.md "Tcl_UniCharIsAlnum, Tcl_UniCharIsAlpha, Tcl_UniCharIsControl, Tcl_UniCharIsDigit, Tcl_UniCharIsGraph, Tcl_UniCharIsLower, Tcl_UniCharIsPrint, Tcl_UniCharIsPunct, Tcl_UniCharIsSpace, Tcl_UniCharIsUpper, Tcl_UniCharIsWordChar - routines for classification of Tcl_UniChar characters")
cleanup

     [try](../TclCmd/try.md "try - Trap and process errors and exceptions"), [CallDel](../TclLib/CallDel.md "Tcl_CallWhenDeleted, Tcl_DontCallWhenDeleted - Arrange for callback when interpreter is deleted"), [Exit](../TclLib/Exit.md "Tcl_Exit, Tcl_Finalize, Tcl_CreateExitHandler, Tcl_DeleteExitHandler, Tcl_ExitThread, Tcl_FinalizeThread, Tcl_CreateThreadExitHandler, Tcl_DeleteThreadExitHandler, Tcl_SetExitProc - end the application or thread \(and invoke exit handlers\)")
clear

     [clipboard](../TkCmd/clipboard.md "clipboard - Manipulate Tk clipboard"), [selection](../TkCmd/selection.md "selection - Manipulate the X selection"), [Clipboard](../TkLib/Clipboard.md "Tk_ClipboardClear, Tk_ClipboardAppend - Manage the clipboard"), [ClrSelect](../TkLib/ClrSelect.md "Tk_ClearSelection - Deselect a selection")
client

     [OpenTcp](../TclLib/OpenTcp.md "Tcl_OpenTcpClient, Tcl_MakeTcpClientChannel, Tcl_OpenTcpServer - procedures to open channels using TCP sockets")
clientData

     [TraceCmd](../TclLib/TraceCmd.md "Tcl_CommandTraceInfo, Tcl_TraceCommand, Tcl_UntraceCommand - monitor renames and deletes of a command"), [TraceVar](../TclLib/TraceVar.md "Tcl_TraceVar, Tcl_TraceVar2, Tcl_UntraceVar, Tcl_UntraceVar2, Tcl_VarTraceInfo, Tcl_VarTraceInfo2 - monitor accesses to a variable")
clipboard

     [clipboard](../TkCmd/clipboard.md "clipboard - Manipulate Tk clipboard"), [Clipboard](../TkLib/Clipboard.md "Tk_ClipboardClear, Tk_ClipboardAppend - Manage the clipboard")
clock

     [clock](../TclCmd/clock.md "clock - Obtain and manipulate dates and times"), [CrtTimerHdlr](../TclLib/CrtTimerHdlr.md "Tcl_CreateTimerHandler, Tcl_DeleteTimerHandler - call a procedure at a given time"), [QWinEvent](../TkLib/QWinEvent.md "Tk_CollapseMotionEvents, Tk_QueueWindowEvent - Add a window event to the Tcl event queue")
clone

     [copy](../TclCmd/copy.md "oo::copy - create copies of objects and classes")
close

     [close](../TclCmd/close.md "close - Close an open channel")
code

     [scope](../ItclCmd/scope.md "itcl::scope - capture the namespace context for a variable")
color

     [chooseColor](../TkCmd/chooseColor.md "tk_chooseColor - pops up a dialog box for the user to select a color."), [colors](../TkCmd/colors.md "colors - symbolic color names recognized by Tk"), [palette](../TkCmd/palette.md "tk_setPalette, tk_bisque - Modify the Tk color palette"), [photo](../TkCmd/photo.md "photo - Full-color images"), [3DBorder](../TkLib/3DBorder.md "Tk_Alloc3DBorderFromObj, Tk_Get3DBorder, Tk_Get3DBorderFromObj, Tk_Draw3DRectangle, Tk_Fill3DRectangle, Tk_Draw3DPolygon, Tk_Fill3DPolygon, Tk_3DVerticalBevel, Tk_3DHorizontalBevel, Tk_SetBackgroundFromBorder, Tk_NameOf3DBorder, Tk_3DBorderColor, Tk_3DBorderGC, Tk_Free3DBorderFromObj, Tk_Free3DBorder - draw borders with three-dimensional appearance"), [CanvPsY](../TkLib/CanvPsY.md "Tk_CanvasPsY, Tk_CanvasPsBitmap, Tk_CanvasPsColor, Tk_CanvasPsFont, Tk_CanvasPsPath, Tk_CanvasPsStipple - utility procedures for generating Postscript for canvases"), [ConfigWidg](../TkLib/ConfigWidg.md "Tk_ConfigureWidget, Tk_ConfigureInfo, Tk_ConfigureValue, Tk_FreeOptions - process configuration options for widgets"), [ConfigWind](../TkLib/ConfigWind.md "Tk_ConfigureWindow, Tk_MoveWindow, Tk_ResizeWindow, Tk_MoveResizeWindow, Tk_SetWindowBorderWidth, Tk_ChangeWindowAttributes, Tk_SetWindowBackground, Tk_SetWindowBackgroundPixmap, Tk_SetWindowBorder, Tk_SetWindowBorderPixmap, Tk_SetWindowColormap, Tk_DefineCursor, Tk_UndefineCursor - change window configuration or attributes"), [GetColor](../TkLib/GetColor.md "Tk_AllocColorFromObj, Tk_GetColor, Tk_GetColorFromObj, Tk_GetColorByValue, Tk_NameOfColor, Tk_FreeColorFromObj, Tk_FreeColor - maintain database of colors"), [SetOptions](../TkLib/SetOptions.md "Tk_CreateOptionTable, Tk_DeleteOptionTable, Tk_InitOptions, Tk_SetOptions, Tk_FreeSavedOptions, Tk_RestoreSavedOptions, Tk_GetOptionValue,  Tk_GetOptionInfo, Tk_FreeConfigOptions, Tk_Offset - process configuration options")
color selection

     [chooseColor](../TkCmd/chooseColor.md "tk_chooseColor - pops up a dialog box for the user to select a color.")
colormap

     [GetClrmap](../TkLib/GetClrmap.md "Tk_GetColormap, Tk_PreserveColormap, Tk_FreeColormap - allocate and free colormaps"), [GetVisual](../TkLib/GetVisual.md "Tk_GetVisual - translate from string to visual"), [SetVisual](../TkLib/SetVisual.md "Tk_SetWindowVisual - change visual characteristics of window"), [WindowId](../TkLib/WindowId.md "Tk_WindowId, Tk_Parent, Tk_Display, Tk_DisplayName, Tk_ScreenNumber, Tk_Screen, Tk_X, Tk_Y, Tk_Width, Tk_Height, Tk_Changes, Tk_Attributes, Tk_IsContainer, Tk_IsEmbedded, Tk_IsMapped, Tk_IsTopLevel, Tk_ReqWidth, Tk_ReqHeight, Tk_MinReqWidth, Tk_MinReqHeight, Tk_InternalBorderLeft, Tk_InternalBorderRight, Tk_InternalBorderTop, Tk_InternalBorderBottom, Tk_Visual, Tk_Depth, Tk_Colormap, Tk_Interp  - retrieve information from Tk's local data structure")
command

     [info](../TclCmd/info.md "info - Return information about the state of the Tcl interpreter"), [mathop](../TclCmd/mathop.md "mathop - Mathematical operators as Tcl commands"), [namespace](../TclCmd/namespace.md "namespace - create and manipulate contexts for commands and variables"), [rename](../TclCmd/rename.md "rename - Rename or delete a command"), [Tcl](../TclCmd/Tcl.md "Tcl - Tool Command Language"), [trace](../TclCmd/trace.md "trace - Monitor variable accesses, command usages and command executions"), [ttk_button](../TkCmd/ttk_button.md "ttk::button - Widget that issues a command when pressed"), [AppInit](../TclLib/AppInit.md "Tcl_AppInit - perform application-specific initialization"), [CrtAlias](../TclLib/CrtAlias.md "Tcl_IsSafe, Tcl_MakeSafe, Tcl_CreateChild, Tcl_CreateSlave, Tcl_GetChild, Tcl_GetSlave, Tcl_GetParent, Tcl_GetMaster, Tcl_GetInterpPath, Tcl_CreateAlias, Tcl_CreateAliasObj, Tcl_GetAlias, Tcl_GetAliasObj, Tcl_ExposeCommand, Tcl_HideCommand - manage multiple Tcl interpreters, aliases and hidden commands"), [CrtCommand](../TclLib/CrtCommand.md "Tcl_CreateCommand - implement new commands in C"), [CrtInterp](../TclLib/CrtInterp.md "Tcl_CreateInterp, Tcl_DeleteInterp, Tcl_InterpActive, Tcl_InterpDeleted - create and delete Tcl command interpreters"), [CrtObjCmd](../TclLib/CrtObjCmd.md "Tcl_CreateObjCommand, Tcl_DeleteCommand, Tcl_DeleteCommandFromToken, Tcl_GetCommandInfo, Tcl_GetCommandInfoFromToken, Tcl_SetCommandInfo, Tcl_SetCommandInfoFromToken, Tcl_GetCommandName, Tcl_GetCommandFullName, Tcl_GetCommandFromObj - implement new commands in C"), [CrtTrace](../TclLib/CrtTrace.md "Tcl_CreateTrace, Tcl_CreateObjTrace, Tcl_DeleteTrace - arrange for command execution to be traced"), [Ensemble](../TclLib/Ensemble.md "Tcl_CreateEnsemble, Tcl_FindEnsemble, Tcl_GetEnsembleFlags, Tcl_GetEnsembleMappingDict, Tcl_GetEnsembleNamespace, Tcl_GetEnsembleParameterList, Tcl_GetEnsembleUnknownHandler, Tcl_GetEnsembleSubcommandList, Tcl_IsEnsemble, Tcl_SetEnsembleFlags, Tcl_SetEnsembleMappingDict, Tcl_SetEnsembleParameterList, Tcl_SetEnsembleSubcommandList, Tcl_SetEnsembleUnknownHandler - manipulate ensemble commands"), [Namespace](../TclLib/Namespace.md "Tcl_AppendExportList, Tcl_CreateNamespace, Tcl_DeleteNamespace, Tcl_Export, Tcl_FindCommand, Tcl_FindNamespace, Tcl_ForgetImport, Tcl_GetCurrentNamespace, Tcl_GetGlobalNamespace, Tcl_GetNamespaceUnknownHandler, Tcl_Import, Tcl_SetNamespaceUnknownHandler - manipulate namespaces"), [NRE](../TclLib/NRE.md "Tcl_NRCreateCommand, Tcl_NRCallObjProc, Tcl_NREvalObj, Tcl_NREvalObjv, Tcl_NRCmdSwap, Tcl_NRExprObj, Tcl_NRAddCallback - Non-Recursive \(stackless\) evaluation of Tcl scripts."), [ParseCmd](../TclLib/ParseCmd.md "Tcl_ParseCommand, Tcl_ParseExpr, Tcl_ParseBraces, Tcl_ParseQuotedString, Tcl_ParseVarName, Tcl_ParseVar, Tcl_FreeParse, Tcl_EvalTokens, Tcl_EvalTokensStandard - parse Tcl scripts and expressions"), [RecEvalObj](../TclLib/RecEvalObj.md "Tcl_RecordAndEvalObj - save command on history list before evaluating"), [RecordEval](../TclLib/RecordEval.md "Tcl_RecordAndEval - save command on history list before evaluating"), [SetResult](../TclLib/SetResult.md "Tcl_SetObjResult, Tcl_GetObjResult, Tcl_SetResult, Tcl_GetStringResult, Tcl_AppendResult, Tcl_AppendResultVA, Tcl_AppendElement, Tcl_ResetResult, Tcl_TransferResult, Tcl_FreeResult - manipulate Tcl result"), [TraceCmd](../TclLib/TraceCmd.md "Tcl_CommandTraceInfo, Tcl_TraceCommand, Tcl_UntraceCommand - monitor renames and deletes of a command"), [WrongNumArgs](../TclLib/WrongNumArgs.md "Tcl_WrongNumArgs - generate standard error message for wrong number of arguments")
command line

     [ParseArgv](../TkLib/ParseArgv.md "Tk_ParseArgv - process command-line options")
command substitution

     [subst](../TclCmd/subst.md "subst - Perform backslash, command, and variable substitutions"), [SubstObj](../TclLib/SubstObj.md "Tcl_SubstObj - perform substitutions on Tcl values")
command tracing

     [ttrace](../ThreadCmd/ttrace.md "ttrace - Trace-based interpreter initialization")
command-line arguments

     [Tcl_Main](../TclLib/Tcl_Main.md "Tcl_Main, Tcl_MainEx, Tcl_MainExW, Tcl_SetStartupScript, Tcl_GetStartupScript, Tcl_SetMainLoop - main program, startup script, and event loop definition for Tcl-based applications"), [Tk_Main](../TkLib/Tk_Main.md "Tk_Main - main program for Tk-based applications")
commands

     [Limit](../TclLib/Limit.md "Tcl_LimitAddHandler, Tcl_LimitCheck, Tcl_LimitExceeded, Tcl_LimitGetCommands, Tcl_LimitGetGranularity, Tcl_LimitGetTime, Tcl_LimitReady, Tcl_LimitRemoveHandler, Tcl_LimitSetCommands, Tcl_LimitSetGranularity, Tcl_LimitSetTime, Tcl_LimitTypeEnabled, Tcl_LimitTypeExceeded, Tcl_LimitTypeReset, Tcl_LimitTypeSet - manage and check resource limits on interpreters")
comment

     [Tcl](../TclCmd/Tcl.md "Tcl - Tool Command Language")
compare

     [expr](../TclCmd/expr.md "expr - Evaluate an expression"), [string](../TclCmd/string.md "string - Manipulate strings")
compiler

     [tclvars](../TclCmd/tclvars.md "argc, argv, argv0, auto_path, env, errorCode, errorInfo, tcl_interactive, tcl_library, tcl_patchLevel, tcl_pkgPath, tcl_platform, tcl_precision, tcl_rcFileName, tcl_traceCompile, tcl_traceExec, tcl_version - Variables used by Tcl")
complete command

     [CmdCmplt](../TclLib/CmdCmplt.md "Tcl_CommandComplete - Check for unmatched braces in a Tcl command")
component

     [itclcomponent](../ItclCmd/itclcomponent.md "itcl::component - define components for extendedclass, widget or widgetadaptor")
compress

     [zlib](../TclCmd/zlib.md "zlib - compression and decompression operations"), [TclZlib](../TclLib/TclZlib.md "Tcl_ZlibAdler32, Tcl_ZlibCRC32, Tcl_ZlibDeflate, Tcl_ZlibInflate, Tcl_ZlibStreamChecksum, Tcl_ZlibStreamClose, Tcl_ZlibStreamEof, Tcl_ZlibStreamGet, Tcl_ZlibStreamGetCommandName, Tcl_ZlibStreamInit, Tcl_ZlibStreamPut - compression and decompression functions")
compression

     [ChnlStack](../TclLib/ChnlStack.md "Tcl_StackChannel, Tcl_UnstackChannel, Tcl_GetStackedChannel, Tcl_GetTopChannel - manipulate stacked I/O channels")
concat

     [StringObj](../TclLib/StringObj.md "Tcl_NewStringObj, Tcl_NewUnicodeObj, Tcl_SetStringObj, Tcl_SetUnicodeObj, Tcl_GetStringFromObj, Tcl_GetString, Tcl_GetUnicodeFromObj, Tcl_GetUnicode, Tcl_GetUniChar, Tcl_GetCharLength, Tcl_GetRange, Tcl_AppendToObj, Tcl_AppendUnicodeToObj, Tcl_AppendObjToObj, Tcl_AppendStringsToObj, Tcl_AppendStringsToObjVA, Tcl_AppendLimitedToObj, Tcl_Format, Tcl_AppendFormatToObj, Tcl_ObjPrintf, Tcl_AppendPrintfToObj, Tcl_SetObjLength, Tcl_AttemptSetObjLength, Tcl_ConcatObj - manipulate Tcl values as strings")
concatenate

     [concat](../TclCmd/concat.md "concat - Join lists together"), [eval](../TclCmd/eval.md "eval - Evaluate a Tcl script"), [Concat](../TclLib/Concat.md "Tcl_Concat - concatenate a collection of strings"), [StringObj](../TclLib/StringObj.md "Tcl_NewStringObj, Tcl_NewUnicodeObj, Tcl_SetStringObj, Tcl_SetUnicodeObj, Tcl_GetStringFromObj, Tcl_GetString, Tcl_GetUnicodeFromObj, Tcl_GetUnicode, Tcl_GetUniChar, Tcl_GetCharLength, Tcl_GetRange, Tcl_AppendToObj, Tcl_AppendUnicodeToObj, Tcl_AppendObjToObj, Tcl_AppendStringsToObj, Tcl_AppendStringsToObjVA, Tcl_AppendLimitedToObj, Tcl_Format, Tcl_AppendFormatToObj, Tcl_ObjPrintf, Tcl_AppendPrintfToObj, Tcl_SetObjLength, Tcl_AttemptSetObjLength, Tcl_ConcatObj - manipulate Tcl values as strings")
condition variable

     [Thread](../TclLib/Thread.md "Tcl_ConditionNotify, Tcl_ConditionWait, Tcl_ConditionFinalize, Tcl_GetThreadData, Tcl_MutexLock, Tcl_MutexUnlock, Tcl_MutexFinalize, Tcl_CreateThread, Tcl_JoinThread - Tcl thread support")
conditional

     [if](../TclCmd/if.md "if - Execute scripts conditionally")
configuration

     [RegConfig](../TclLib/RegConfig.md "Tcl_RegisterConfig - procedures to register embedded configuration information")
configuration option

     [SetOptions](../TkLib/SetOptions.md "Tk_CreateOptionTable, Tk_DeleteOptionTable, Tk_InitOptions, Tk_SetOptions, Tk_FreeSavedOptions, Tk_RestoreSavedOptions, Tk_GetOptionValue,  Tk_GetOptionInfo, Tk_FreeConfigOptions, Tk_Offset - process configuration options")
configuration options

     [ConfigWidg](../TkLib/ConfigWidg.md "Tk_ConfigureWidget, Tk_ConfigureInfo, Tk_ConfigureValue, Tk_FreeOptions - process configuration options for widgets")
configure

     [ttk_widget](../TkCmd/ttk_widget.md "ttk::widget - Standard options and commands supported by Tk themed widgets"), [configbody](../ItclCmd/configbody.md "itcl::configbody - change the "config" code for a public variable"), [ConfigWind](../TkLib/ConfigWind.md "Tk_ConfigureWindow, Tk_MoveWindow, Tk_ResizeWindow, Tk_MoveResizeWindow, Tk_SetWindowBorderWidth, Tk_ChangeWindowAttributes, Tk_SetWindowBackground, Tk_SetWindowBackgroundPixmap, Tk_SetWindowBorder, Tk_SetWindowBorderPixmap, Tk_SetWindowColormap, Tk_DefineCursor, Tk_UndefineCursor - change window configuration or attributes")
connection

     [socket](../TclCmd/socket.md "socket - Open a TCP network connection"), [tdbc](../TdbcCmd/tdbc.md "tdbc - Tcl Database Connectivity"), [tdbc_connection](../TdbcCmd/tdbc_connection.md "tdbc::connection - TDBC connection object"), [tdbc_resultset](../TdbcCmd/tdbc_resultset.md "tdbc::resultset - TDBC result set object"), [tdbc_statement](../TdbcCmd/tdbc_statement.md "tdbc::statement - TDBC statement object"), [tdbc_mysql](../TdbcmysqlCmd/tdbc_mysql.md "tdbc::mysql - TDBC-MYSQL bridge"), [tdbc_odbc](../TdbcodbcCmd/tdbc_odbc.md "tdbc::odbc - TDBC-ODBC bridge"), [tdbc_postgres](../TdbcpostgresCmd/tdbc_postgres.md "tdbc::postgres - TDBC-POSTGRES bridge"), [tdbc_sqlite3](../TdbcsqliteCmd/tdbc_sqlite3.md "tdbc::sqlite3 - TDBC driver for the SQLite3 database manager")
connectivity

     [tdbc](../TdbcCmd/tdbc.md "tdbc - Tcl Database Connectivity"), [tdbc_connection](../TdbcCmd/tdbc_connection.md "tdbc::connection - TDBC connection object"), [tdbc_resultset](../TdbcCmd/tdbc_resultset.md "tdbc::resultset - TDBC result set object"), [tdbc_statement](../TdbcCmd/tdbc_statement.md "tdbc::statement - TDBC statement object"), [tdbc_mysql](../TdbcmysqlCmd/tdbc_mysql.md "tdbc::mysql - TDBC-MYSQL bridge"), [tdbc_odbc](../TdbcodbcCmd/tdbc_odbc.md "tdbc::odbc - TDBC-ODBC bridge"), [tdbc_postgres](../TdbcpostgresCmd/tdbc_postgres.md "tdbc::postgres - TDBC-POSTGRES bridge"), [tdbc_sqlite3](../TdbcsqliteCmd/tdbc_sqlite3.md "tdbc::sqlite3 - TDBC driver for the SQLite3 database manager")
console

     [console](../TkCmd/console.md "console - Control the console on systems without a real console"), [CrtConsoleChan](../TkLib/CrtConsoleChan.md "Tk_InitConsoleChannels - Install the console channels as standard channels")
constructor

     [Class](../TclLib/Class.md "Tcl_ClassGetMetadata, Tcl_ClassSetMetadata, Tcl_CopyObjectInstance, Tcl_GetClassAsObject, Tcl_GetObjectAsClass, Tcl_GetObjectCommand, Tcl_GetObjectFromObj, Tcl_GetObjectName, Tcl_GetObjectNamespace, Tcl_NewObjectInstance, Tcl_ObjectDeleted, Tcl_ObjectGetMetadata, Tcl_ObjectGetMethodNameMapper, Tcl_ObjectSetMetadata, Tcl_ObjectSetMethodNameMapper - manipulate objects and classes"), [Method](../TclLib/Method.md "Tcl_ClassSetConstructor, Tcl_ClassSetDestructor, Tcl_MethodDeclarerClass, Tcl_MethodDeclarerObject, Tcl_MethodIsPublic, Tcl_MethodIsType, Tcl_MethodName, Tcl_NewInstanceMethod, Tcl_NewMethod, Tcl_ObjectContextInvokeNext, Tcl_ObjectContextIsFiltering, Tcl_ObjectContextMethod, Tcl_ObjectContextObject, Tcl_ObjectContextSkippedArgs - manipulate methods and method-call contexts")
container

     [place](../TkCmd/place.md "place - Geometry manager for fixed or rubber-sheet placement"), [ttk_frame](../TkCmd/ttk_frame.md "ttk::frame - Simple container widget"), [ttk_labelframe](../TkCmd/ttk_labelframe.md "ttk::labelframe - Container widget with optional label"), [MaintGeom](../TkLib/MaintGeom.md "Tk_MaintainGeometry, Tk_UnmaintainGeometry - maintain geometry of one window relative to another")
containing

     [CoordToWin](../TkLib/CoordToWin.md "Tk_CoordsToWindow - Find window containing a point")
content

     [place](../TkCmd/place.md "place - Geometry manager for fixed or rubber-sheet placement")
context

     [uplevel](../TclCmd/uplevel.md "uplevel - Execute a script in a different stack frame"), [upvar](../TclCmd/upvar.md "upvar - Create link to variable in a different stack frame")
continue

     [continue](../TclCmd/continue.md "continue - Skip to the next iteration of a loop"), [return](../TclCmd/return.md "return - Return from a procedure, or set return code of a script"), [AllowExc](../TclLib/AllowExc.md "Tcl_AllowExceptions - allow all exceptions in next script evaluation")
conversion

     [GetInt](../TclLib/GetInt.md "Tcl_GetInt, Tcl_GetDouble, Tcl_GetBoolean - convert from string to integer, double, or boolean"), [PrintDbl](../TclLib/PrintDbl.md "Tcl_PrintDouble - Convert floating value to string"), [GetDash](../TkLib/GetDash.md "Tk_GetDash - convert from string to valid dash structure.")
conversion specifier

     [format](../TclCmd/format.md "format - Format a string in the style of sprintf"), [scan](../TclCmd/scan.md "scan - Parse string using conversion specifiers in the style of sscanf")
convert

     [Encoding](../TclLib/Encoding.md "Tcl_GetEncoding, Tcl_FreeEncoding, Tcl_GetEncodingFromObj, Tcl_ExternalToUtfDString, Tcl_ExternalToUtf, Tcl_UtfToExternalDString, Tcl_UtfToExternal, Tcl_WinTCharToUtf, Tcl_WinUtfToTChar, Tcl_GetEncodingName, Tcl_SetSystemEncoding, Tcl_GetEncodingNameFromEnvironment, Tcl_GetEncodingNames, Tcl_CreateEncoding, Tcl_GetEncodingSearchPath, Tcl_SetEncodingSearchPath, Tcl_GetDefaultEncodingDir, Tcl_SetDefaultEncodingDir - procedures for creating and using encodings"), [SplitList](../TclLib/SplitList.md "Tcl_SplitList, Tcl_Merge, Tcl_ScanElement, Tcl_ConvertElement, Tcl_ScanCountedElement, Tcl_ConvertCountedElement - manipulate Tcl lists"), [GetPixels](../TkLib/GetPixels.md "Tk_GetPixelsFromObj, Tk_GetPixels, Tk_GetMMFromObj, Tk_GetScreenMM - translate between strings and screen units")
coordinates

     [CoordToWin](../TkLib/CoordToWin.md "Tk_CoordsToWindow - Find window containing a point"), [GetRootCrd](../TkLib/GetRootCrd.md "Tk_GetRootCoords - Compute root-window coordinates of window")
copy

     [copy](../TclCmd/copy.md "oo::copy - create copies of objects and classes")
copy files

     [file](../TclCmd/file.md "file - Manipulate file names and attributes")
coroutine

     [coroutine](../TclCmd/coroutine.md "coroutine, yield, yieldto - Create and produce values from coroutines")
cpu architecture

     [platform](../TclCmd/platform.md "platform - System identification support code and utilities"), [platform_shell](../TclCmd/platform_shell.md "platform::shell - System identification support code and utilities")
create

     [dict](../TclCmd/dict.md "dict - Manipulate dictionaries"), [open](../TclCmd/open.md "open - Open a file-based or command pipeline channel"), [CrtCommand](../TclLib/CrtCommand.md "Tcl_CreateCommand - implement new commands in C"), [CrtInterp](../TclLib/CrtInterp.md "Tcl_CreateInterp, Tcl_DeleteInterp, Tcl_InterpActive, Tcl_InterpDeleted - create and delete Tcl command interpreters"), [CrtObjCmd](../TclLib/CrtObjCmd.md "Tcl_CreateObjCommand, Tcl_DeleteCommand, Tcl_DeleteCommandFromToken, Tcl_GetCommandInfo, Tcl_GetCommandInfoFromToken, Tcl_SetCommandInfo, Tcl_SetCommandInfoFromToken, Tcl_GetCommandName, Tcl_GetCommandFullName, Tcl_GetCommandFromObj - implement new commands in C"), [CrtTrace](../TclLib/CrtTrace.md "Tcl_CreateTrace, Tcl_CreateObjTrace, Tcl_DeleteTrace - arrange for command execution to be traced"), [CrtWindow](../TkLib/CrtWindow.md "Tk_CreateWindow, Tk_CreateWindowFromPath, Tk_DestroyWindow, Tk_MakeWindowExist - create or delete window")
ctype

     [string](../TclCmd/string.md "string - Manipulate strings")
current directory

     [filename](../TclCmd/filename.md "filename - File name conventions supported by Tcl commands")
cursor

     [cursors](../TkCmd/cursors.md "cursors - mouse cursors available in Tk"), [ConfigWidg](../TkLib/ConfigWidg.md "Tk_ConfigureWidget, Tk_ConfigureInfo, Tk_ConfigureValue, Tk_FreeOptions - process configuration options for widgets"), [GetCursor](../TkLib/GetCursor.md "Tk_AllocCursorFromObj, Tk_GetCursor, Tk_GetCursorFromObj, Tk_GetCursorFromData, Tk_NameOfCursor, Tk_FreeCursorFromObj, Tk_FreeCursor - maintain database of cursors"), [SetCaret](../TkLib/SetCaret.md "Tk_SetCaretPos - set the display caret location"), [SetOptions](../TkLib/SetOptions.md "Tk_CreateOptionTable, Tk_DeleteOptionTable, Tk_InitOptions, Tk_SetOptions, Tk_FreeSavedOptions, Tk_RestoreSavedOptions, Tk_GetOptionValue,  Tk_GetOptionInfo, Tk_FreeConfigOptions, Tk_Offset - process configuration options")
custom

     [ConfigWidg](../TkLib/ConfigWidg.md "Tk_ConfigureWidget, Tk_ConfigureInfo, Tk_ConfigureValue, Tk_FreeOptions - process configuration options for widgets")

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
