## [Tcl8.6.18/Tk8.6.18 Documentation](../contents.md) > Tcl/Tk Keywords - F

### [Tcl/Tk Applications](../UserCmd/contents.md) | [Tcl Commands](../TclCmd/contents.md) | [Tk Commands](../TkCmd/contents.md) | [[incr Tcl] Package Commands](../ItclCmd/contents.md) | [SQLite3 Package Commands](../SqliteCmd/contents.md) | [TDBC Package Commands](../TdbcCmd/contents.md) | [tdbc::mysql Package Commands](../TdbcmysqlCmd/contents.md) | [tdbc::odbc Package Commands](../TdbcodbcCmd/contents.md) | [tdbc::postgres Package Commands](../TdbcpostgresCmd/contents.md) | [tdbc::sqlite3 Package Commands](../TdbcsqliteCmd/contents.md) | [Thread Package Commands](../ThreadCmd/contents.md) | [Tcl C API](../TclLib/contents.md) | [Tk C API](../TkLib/contents.md) | [[incr Tcl] Package C API](../ItclLib/contents.md) | [TDBC Package C API](../TdbcLib/contents.md)

### [A](A.md) | [B](B.md) | [C](C.md) | [D](D.md) | [E](E.md) | [F](F.md) | [G](G.md) | [H](H.md) | [I](I.md) | [J](J.md) | [K](K.md) | [L](L.md) | [M](M.md) | [N](N.md) | [O](O.md) | [P](P.md) | [Q](Q.md) | [R](R.md) | [S](S.md) | [T](T.md) | [U](U.md) | [V](V.md) | [W](W.md) | [X](X.md) | [Y](Y.md) | [Z](Z.md)

false

     [if](../TclCmd/if.md "if - Execute scripts conditionally")
fatal

     [Panic](../TclLib/Panic.md "Tcl_Panic, Tcl_PanicVA, Tcl_SetPanicProc - report fatal error and abort")
file

     [file](../TclCmd/file.md "file - Manipulate file names and attributes"), [glob](../TclCmd/glob.md "glob - Return names of files that match patterns"), [open](../TclCmd/open.md "open - Open a file-based or command pipeline channel"), [pid](../TclCmd/pid.md "pid - Retrieve process identifiers"), [seek](../TclCmd/seek.md "seek - Change the access position for an open channel"), [source](../TclCmd/source.md "source - Evaluate a file or resource as a Tcl script"), [CrtFileHdlr](../TclLib/CrtFileHdlr.md "Tcl_CreateFileHandler, Tcl_DeleteFileHandler - associate procedure callbacks with files or devices \(Unix only\)"), [Eval](../TclLib/Eval.md "Tcl_EvalObjEx, Tcl_EvalFile, Tcl_EvalObjv, Tcl_Eval, Tcl_EvalEx, Tcl_GlobalEval, Tcl_GlobalEvalObj, Tcl_VarEval, Tcl_VarEvalVA - execute Tcl scripts"), [SplitPath](../TclLib/SplitPath.md "Tcl_SplitPath, Tcl_JoinPath, Tcl_GetPathType - manipulate platform-dependent file paths")
file events

     [Notifier](../TclLib/Notifier.md "Tcl_CreateEventSource, Tcl_DeleteEventSource, Tcl_SetMaxBlockTime, Tcl_QueueEvent, Tcl_ThreadQueueEvent, Tcl_ThreadAlert, Tcl_GetCurrentThread, Tcl_DeleteEvents, Tcl_InitNotifier, Tcl_FinalizeNotifier, Tcl_WaitForEvent, Tcl_AlertNotifier, Tcl_SetTimer, Tcl_ServiceAll, Tcl_ServiceEvent, Tcl_GetServiceMode, Tcl_SetServiceMode, Tcl_ServiceModeHook, Tcl_SetNotifier - the event queue and notifier interfaces")
file handle

     [GetOpnFl](../TclLib/GetOpnFl.md "Tcl_GetOpenFile - Return a FILE* for a channel registered in the given interpreter \(Unix only\)")
file name

     [Translate](../TclLib/Translate.md "Tcl_TranslateFileName - convert file name to native form and replace tilde with home directory")
file selection dialog

     [getOpenFile](../TkCmd/getOpenFile.md "tk_getOpenFile, tk_getSaveFile - pop up a dialog box for the user to select a file to open or save.")
filename

     [SplitPath](../TclLib/SplitPath.md "Tcl_SplitPath, Tcl_JoinPath, Tcl_GetPathType - manipulate platform-dependent file paths")
filesystem

     [FileSystem](../TclLib/FileSystem.md "Tcl_FSRegister, Tcl_FSUnregister, Tcl_FSData, Tcl_FSMountsChanged, Tcl_FSGetFileSystemForPath, Tcl_FSGetPathType, Tcl_FSCopyFile, Tcl_FSCopyDirectory, Tcl_FSCreateDirectory, Tcl_FSDeleteFile, Tcl_FSRemoveDirectory, Tcl_FSRenameFile, Tcl_FSListVolumes, Tcl_FSEvalFile, Tcl_FSEvalFileEx, Tcl_FSLoadFile, Tcl_FSUnloadFile, Tcl_FSMatchInDirectory, Tcl_FSLink, Tcl_FSLstat, Tcl_FSUtime, Tcl_FSFileAttrsGet, Tcl_FSFileAttrsSet, Tcl_FSFileAttrStrings, Tcl_FSStat, Tcl_FSAccess, Tcl_FSOpenFileChannel, Tcl_FSGetCwd, Tcl_FSChdir, Tcl_FSPathSeparator, Tcl_FSJoinPath, Tcl_FSSplitPath, Tcl_FSEqualPaths, Tcl_FSGetNormalizedPath, Tcl_FSJoinToPath, Tcl_FSConvertToPathType, Tcl_FSGetInternalRep, Tcl_FSGetTranslatedPath, Tcl_FSGetTranslatedStringPath, Tcl_FSNewNativePath, Tcl_FSGetNativePath, Tcl_FSFileSystemInfo, Tcl_GetAccessTimeFromStat, Tcl_GetBlockSizeFromStat, Tcl_GetBlocksFromStat, Tcl_GetChangeTimeFromStat, Tcl_GetDeviceTypeFromStat, Tcl_GetFSDeviceFromStat, Tcl_GetFSInodeFromStat, Tcl_GetGroupIdFromStat, Tcl_GetLinkCountFromStat, Tcl_GetModeFromStat, Tcl_GetModificationTimeFromStat, Tcl_GetSizeFromStat, Tcl_GetUserIdFromStat, Tcl_AllocStatBuf - procedures to interact with any filesystem")
fill

     [GetJustify](../TkLib/GetJustify.md "Tk_GetJustifyFromObj, Tk_GetJustify, Tk_NameOfJustify - translate between strings and justification styles")
filter

     [dict](../TclCmd/dict.md "dict - Manipulate dictionaries"), [fconfigure](../TclCmd/fconfigure.md "fconfigure - Set and get options on a channel"), [RestrictEv](../TkLib/RestrictEv.md "Tk_RestrictEvents - filter and selectively delay X events")
final

     [try](../TclCmd/try.md "try - Trap and process errors and exceptions")
find

     [Class](../ItclLib/Class.md "Itcl_CreateClass, Itcl_DeleteClass, Itcl_FindClass, Itcl_IsClass, Itcl_IsClassNamespace - Manipulate classes.")
floating-point

     [GetInt](../TclLib/GetInt.md "Tcl_GetInt, Tcl_GetDouble, Tcl_GetBoolean - convert from string to integer, double, or boolean"), [PrintDbl](../TclLib/PrintDbl.md "Tcl_PrintDouble - Convert floating value to string")
flush

     [flush](../TclCmd/flush.md "flush - Flush buffered output for a channel"), [update](../TclCmd/update.md "update - Process pending events and idle callbacks"), [OpenFileChnl](../TclLib/OpenFileChnl.md "Tcl_OpenFileChannel, Tcl_OpenCommandChannel, Tcl_MakeFileChannel, Tcl_GetChannel, Tcl_GetChannelNames, Tcl_GetChannelNamesEx, Tcl_RegisterChannel, Tcl_UnregisterChannel, Tcl_DetachChannel, Tcl_IsStandardChannel, Tcl_Close, Tcl_CloseEx, Tcl_ReadChars, Tcl_Read, Tcl_GetsObj, Tcl_Gets, Tcl_WriteObj, Tcl_WriteChars, Tcl_Write, Tcl_Flush, Tcl_Seek, Tcl_Tell, Tcl_TruncateChannel, Tcl_GetChannelOption, Tcl_SetChannelOption, Tcl_Eof, Tcl_InputBlocked, Tcl_InputBuffered, Tcl_OutputBuffered, Tcl_Ungets, Tcl_ReadRaw, Tcl_WriteRaw - buffered I/O facilities using channels")
flushing

     [fconfigure](../TclCmd/fconfigure.md "fconfigure - Set and get options on a channel")
focus

     [focus](../TkCmd/focus.md "focus - Manage the input focus"), [focusNext](../TkCmd/focusNext.md "tk_focusNext, tk_focusPrev, tk_focusFollowsMouse - Utility procedures for managing the input focus."), [CanvTkwin](../TkLib/CanvTkwin.md "Tk_CanvasTkwin, Tk_CanvasGetCoord, Tk_CanvasDrawableCoords, Tk_CanvasSetStippleOrigin, Tk_CanvasWindowCoords, Tk_CanvasEventuallyRedraw, Tk_CanvasTagsOption - utility procedures for canvas type managers"), [CanvTxtInfo](../TkLib/CanvTxtInfo.md "Tk_CanvasTextInfo - additional information for managing text items in canvases"), [CrtItemType](../TkLib/CrtItemType.md "Tk_CreateItemType, Tk_GetItemTypes - define new kind of canvas item"), [DrawFocHlt](../TkLib/DrawFocHlt.md "Tk_DrawFocusHighlight - draw the traversal highlight ring for a widget")
focus model

     [wm](../TkCmd/wm.md "wm - Communicate with window manager")
font

     [font](../TkCmd/font.md "font - Create and inspect fonts."), [fontchooser](../TkCmd/fontchooser.md "fontchooser - control font selection dialog"), [CanvPsY](../TkLib/CanvPsY.md "Tk_CanvasPsY, Tk_CanvasPsBitmap, Tk_CanvasPsColor, Tk_CanvasPsFont, Tk_CanvasPsPath, Tk_CanvasPsStipple - utility procedures for generating Postscript for canvases"), [ConfigWidg](../TkLib/ConfigWidg.md "Tk_ConfigureWidget, Tk_ConfigureInfo, Tk_ConfigureValue, Tk_FreeOptions - process configuration options for widgets"), [FontId](../TkLib/FontId.md "Tk_FontId, Tk_GetFontMetrics, Tk_PostscriptFontName - accessor functions for
fonts"), [GetFont](../TkLib/GetFont.md "Tk_AllocFontFromObj, Tk_GetFont,
Tk_GetFontFromObj, Tk_NameOfFont, Tk_FreeFontFromObj, Tk_FreeFont - maintain
database of fonts"), [MeasureChar](../TkLib/MeasureChar.md "Tk_MeasureChars,
Tk_TextWidth, Tk_DrawChars, Tk_UnderlineChars - routines to measure and display
simple single-line strings."), [SetOptions](../TkLib/SetOptions.md
"Tk_CreateOptionTable, Tk_DeleteOptionTable, Tk_InitOptions, Tk_SetOptions,
Tk_FreeSavedOptions, Tk_RestoreSavedOptions, Tk_GetOptionValue,
Tk_GetOptionInfo, Tk_FreeConfigOptions, Tk_Offset - process configuration
options"), [TextLayout](../TkLib/TextLayout.md "Tk_ComputeTextLayout,
Tk_FreeTextLayout, Tk_DrawTextLayout, Tk_UnderlineTextLayout, Tk_PointToChar,
Tk_CharBbox, Tk_DistanceToTextLayout, Tk_IntersectTextLayout,
Tk_TextLayoutToPostscript - routines to measure and display single-font, multi-
line, justified text.")

font chooser

     [fontchooser](../TkCmd/fontchooser.md "fontchooser - control font selection dialog")
font panel

     [fontchooser](../TkCmd/fontchooser.md "fontchooser - control font selection dialog")
font selection

     [fontchooser](../TkCmd/fontchooser.md "fontchooser - control font selection dialog")
for

     [for](../TclCmd/for.md "for - 'For' loop")
foreach

     [foreach](../TclCmd/foreach.md "foreach - Iterate over all elements in one or more lists"), [lmap](../TclCmd/lmap.md "lmap - Iterate over all elements in one or more lists and collect results")
format

     [binary](../TclCmd/binary.md "binary - Insert and extract fields from binary strings"), [format](../TclCmd/format.md "format - Format a string in the style of sprintf"), [clipboard](../TkCmd/clipboard.md "clipboard - Manipulate Tk clipboard"), [selection](../TkCmd/selection.md "selection - Manipulate the X selection"), [Clipboard](../TkLib/Clipboard.md "Tk_ClipboardClear, Tk_ClipboardAppend - Manage the clipboard"), [CrtSelHdlr](../TkLib/CrtSelHdlr.md "Tk_CreateSelHandler, Tk_DeleteSelHandler - arrange to handle requests for a selection"), [GetSelect](../TkLib/GetSelect.md "Tk_GetSelection - retrieve the contents of a selection")
frame

     [upvar](../TclCmd/upvar.md "upvar - Create link to variable in a different stack frame"), [frame](../TkCmd/frame.md "frame - Create and manipulate 'frame' simple container widgets"), [ttk_frame](../TkCmd/ttk_frame.md "ttk::frame - Simple container widget"), [ttk_labelframe](../TkCmd/ttk_labelframe.md "ttk::labelframe - Container widget with optional label")
free

     [Alloc](../TclLib/Alloc.md "Tcl_Alloc, Tcl_Free, Tcl_Realloc, Tcl_AttemptAlloc, Tcl_AttemptRealloc, Tcl_GetMemoryInfo, ckalloc, ckfree, ckrealloc, attemptckalloc, attemptckrealloc - allocate or free heap memory"), [DString](../TclLib/DString.md "Tcl_DStringInit, Tcl_DStringAppend, Tcl_DStringAppendElement, Tcl_DStringStartSublist, Tcl_DStringEndSublist, Tcl_DStringLength, Tcl_DStringValue, Tcl_DStringSetLength, Tcl_DStringTrunc, Tcl_DStringFree, Tcl_DStringResult, Tcl_DStringGetResult - manipulate dynamic strings"), [Interp](../TclLib/Interp.md "Tcl_Interp - client-visible fields of interpreter structures"), [Preserve](../TclLib/Preserve.md "Tcl_Preserve, Tcl_Release, Tcl_EventuallyFree - avoid freeing storage while it is being used"), [Object](../ItclLib/Object.md "Itcl_CreateObject, Itcl_DeleteObject, Itcl_FindObject, Itcl_IsObject, Itcl_IsObjectIsa - Manipulate an class instance."), [Preserve](../ItclLib/Preserve.md "Itcl_Alloc, Itcl_Free, Itcl_PreserveData, Itcl_ReleaseData, Itcl_EventuallyFree - Manipulate an Itcl list object.")
fuzzy comparison

     [expr](../TclCmd/expr.md "expr - Evaluate an expression")

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
