# 模块 win32help

> 来源：https://mhammond.github.io/pywin32/win32help.html （及其成员页，已全部内联）

## Module win32help

 A module, encapsulating the Win32 help API's.

#### Methods

- WinHelp

 Invokes the Windows Help system.

- HH_AKLINK

 Create and returns an HH_AKLINK structure

- HH_FTS_QUERY

 Create and returns an HH_FTS_QUERY structure

- HH_POPUP

 Create and returns an HH_POPUP structure

- HH_WINTYPE

 Create and returns an HH_WINTYPE structure

- NMHDR

 Create and returns an NMHDR structure

- HHN_NOTIFY

 Create and returns an HHN_NOTIFY structure

- HHNTRACK

 Create and returns an HHNTRACK structure

- HtmlHelp

 Invokes the Windows HTML Help system.


---

# win32help 成员详细文档（共 9 项）


---

<!-- page: win32help__HHNTRACK_meth.html -->

## win32help.HHNTRACK

 PyHHNTRACK = HHNTRACK()

Creates a new HHNTRACK object.


---

<!-- page: win32help__HHN_NOTIFY_meth.html -->

## win32help.HHN_NOTIFY

 PyHHN_NOTIFY = HHN_NOTIFY()

Creates a new HHN_NOTIFY object.


---

<!-- page: win32help__HH_AKLINK_meth.html -->

## win32help.HH_AKLINK

 PyHH_AKLINK = HH_AKLINK()

Creates a new HH_AKLINK object.


---

<!-- page: win32help__HH_FTS_QUERY_meth.html -->

## win32help.HH_FTS_QUERY

 PyHH_FTS_QUERY = HH_FTS_QUERY()

Creates a new HH_FTS_QUERY object.


---

<!-- page: win32help__HH_POPUP_meth.html -->

## win32help.HH_POPUP

 PyHH_POPUP = HH_POPUP()

Creates a new HH_POPUP object.


---

<!-- page: win32help__HH_WINTYPE_meth.html -->

## win32help.HH_WINTYPE

 PyHH_WINTYPE = HH_WINTYPE()

Creates a new HH_WINTYPE object.


---

<!-- page: win32help__HtmlHelp_meth.html -->

## win32help.HtmlHelp

 int = HtmlHelp(hwnd, file , cmd , data )

Invokes the Windows Html Help system.

#### Parameters

- hwnd : int

 The handle of the window requesting help.

- file : string/None

 The name of the help file, or None.

- cmd : int

 The type of help. Valid values are:

 HH_ALINK_LOOKUP : Looks up one or more Associative link (ALink) names in a compiled help (.chm) file.
 The ALink names to search for, and the action to be taken if no matches are found, are specified in the win32help::HH_AKLINK structure.

 file : Specifies a compiled help (.chm) file, or a specific topic within a compiled help file.
 data : Specifies NULL or a pointer to a topic within a compiled help file.

 HH_CLOSE_ALL : Closes all windows opened directly or indirectly by the calling program. The args are not checked for type, values are set as they "Must" be.

 hwnd : Must be None.
 file : Must be None.
 data : Must be zero.

 HH_DISPLAY_INDEX : Selects the Index tab in the Navigation pane of the HTML Help Viewer and searches for the keyword specified in the data parameter.

 file : Specifies a compiled help (.chm) file, or a specific topic within a compiled help file.
 data : Specifies the keyword to select in the index (.hhk) file.

 HH_DISPLAY_SEARCH : Selects the Search tab in the Navigation pane of the HTML Help Viewer and performs a search for the term specified in the searchQuery parameter of the win32help::HH_FTS_QUERY structure.

 file : Specifies a compiled help (.chm) file, or a specific topic within a compiled help file.
 data : Specifies a pointer to an win32help::HH_FTS_QUERY structure.

 HH_DISPLAY_TEXT_POPUP : Opens a pop-up window that displays the contents of one of the following:
 An explicit text string.
 A text string based on a resource ID.
 A text string ID based on a text file contained in a compiled help (.chm) file.

 file : To use an explicit text string, use None. To use a text string from a resource, use None. To use text string from a text file contained in a compiled help file, specify the .chm file and the text file within the .chm file.
 data : Specifies a pointer to an win32help::HH_POPUP structure.

 HH_DISPLAY_TOC : Selects the Contents tab in the Navigation pane of the HTML Help Viewer.

 file : Specifies a compiled help (.chm) file, or a specific topic within a compiled help file.
 data : Specifies None or a pointer to a topic within a compiled help file.

 HH_DISPLAY_TOPIC : Opens a help topic in a specified help window.
 If a window type is not specified, a default window type is used. If the window type or default window type is open, the help topic replaces the current topic in the window.

 file : Specifies a compiled help (.chm) file, or a specific topic within a compiled help file. To specify a defined window type, insert a greater-than (>) character followed by the name of the window type.
 data : Specifies None or a pointer to a topic within a compiled help file.

 HH_GET_LAST_ERROR : Returns information about the last error that occurred in the HTML Help ActiveX control (Hhctrl.ocx).

 file : Must be None
 data : A pointer to a HH_LAST_ERROR structure.

 Has not been implemented by Microsoft yet

 HH_GET_WIN_HANDLE : Returns the handle (hwnd) of a specified window type.

 file : Specifies the name of the compiled help (.chm) file in which the window type is defined.
 data : Specifies the name of the window type whose handle you want to return.

 HH_GET_WIN_TYPE : Retrieves a pointer to the win32help::HH_WINTYPE structure associated with a specified window type.

 file : Specifies the name of the window type whose information you want to get and the name of the compiled help (.chm) file in which the window type is defined. The window name must begin with a greater-than (>) character and must be preceded by the name of the compiled help file it is defined in.
 data : Ignored.

 HH_HELP_CONTEXT : Displays a help topic based on a mapped topic ID. If a window type is not specified, a default window type is used. If the window type or default window type is open, the help topic replaces the current topic in the window.

 file : Specifies the compiled help (.chm) file that contains the mapping information. To specify a defined window type, insert a greater-than (>) character followed by the name of the window type.
 data : Specifies the numeric ID of the topic to display. You must map symbolic IDs of dialog boxes to numeric IDs in the [MAP] section of your project (.hhp) file.

 HH_INITIALIZE : This command initializes the help system for use and must be the first HTML Help command called. It returns a cookie which must be used in the HH_UNINITIALIZE call. HH_INITIALIZE configures HTML Help to run on the same thread as the calling application instead of a secondary thread by setting the global property HH_GPROPID_SINGLETHREAD to VARIANT_TRUE. Running HTML Help on the same thread as the calling application requires the calling application to send messages to HTML Help by calling the HH_PRETRANSLATEMESSAGE command.

 file : Must be None.
 data : Ignored.

 HH_KEYWORD_LOOKUP : Looks up one or more keywords in a compiled help (.chm) file. The keywords to search for and the action to be taken if no matches are found are specified in the win32help::HH_AKLINK structure.

 file : Specifies the compiled help (.chm) file that contains keywords.
 data : Points to an win32help::HH_AKLINK structure.

 HH_PRETRANSLATEMESSAGE : This command is called in the message loop of your Windows application to ensure proper handling of Windows messages, especially keyboard messages when running HTML Help single thread. The HTML Help API is not thread safe and must be called from one and only one thread in a process.

 file data : Points to a Win32 MSG structure.

 Has not been implemented yet

 HH_SET_WIN_TYPE : Creates a new help window or modifies an existing help window at run time.

 file : Specifies the name of the window type that you want to create or modify and the name of the compiled help (.chm) file in which the window type is defined. The window type name must begin with a greater-than (>) character and must be preceded by the name of the compiled help file in which it is defined.
 data : Points to an win32help::HH_WINTYPE structure.

 HH_SYNC : Locates and selects the contents entry for the help topic that is open in the Topic pane of the HTML Help Viewer.

 file : Specifies the name of the window type that you want to sync and the name of the compiled help (.chm) file in which the window type is defined. The window type name must begin with a greater-than (>) character and must be preceded by the name of the compiled help file in which it is defined.
 data : Specifies a pointer to a topic within a compiled help file. This value is the topic file to which the contents will synchronize.

 HH_TP_HELP_CONTEXTMENU : Opens a pop-up context menu. Generally used in response to the Windows WM_CONTEXTMENU message. For example, this message is sent when a user right-clicks a dialog box control.

 hwnd : Specifies the window handle of the dialog box control for which you want pop-up help to appear. This is typically the control that has focus.
 file : Specifies the compiled help (.chm) file, and the text file that contains the pop-up help topics. By default, the text file is named Cshelp.txt. If Cshelp.txt is located in the root of the compiled help file, then you only need to specify the help file name. If not, you must also specify the relative path.
 data : Specifies an array of DWORDs containing pairs of dialog box control IDs and help topic IDs. The array must be terminated by zero, as in the following example:
 DWORD ids[3];
 ids[0] = ControlId;
 ids[1] = HelpId;
 ids[2] = 0;

 HH_TP_HELP_WM_HELP : Opens a pop-up help topic. Generally used in response to the Windows WM_HELP message. For example, this message is sent when a user presses F1.

 hwnd : Specifies the window handle of the dialog box control for which you want pop-up help to appear. This is typically the control that has focus.
 file : Specifies the compiled help (.chm) file, and the text file that contains the pop-up help topics. By default, the text file is named Cshelp.txt. If Cshelp.txt is located in the root of the compiled help file, then you only need to specify the help file name. If not, you must also specify the relative path.
 data : Specifies an array of DWORDs containing pairs of dialog box control IDs and help topic IDs. The array must be terminated by 0, as in the following example:
 DWORD ids[3];
 ids[0] = ControlId;
 ids[1] = HelpId;
 ids[2] = 0;

 HH_UNINITIALIZE : This command is called to properly shut down HTML Help. This function should be the last help command the application calls. HH_UNINITIALIZE should not be called during DLL process detach, but during the normal application shutdown process. The type of the file arg is not checked, just set to the value it "Must" be.

 file : Must be None.
 data : Specifies a cookie. This is the cookie returned by HH_INITIALIZE .

- data=0 : None/int/string/int tuple/win32help::HH_AKLINK/ win32help::HH_FTS_QUERY/win32help::HH_POPUP/ win32help::HH_WINTYPE

 Additional data specific to the help call.

#### Win32 API References

- Search for HtmlHelp at [msdn](https://learn.microsoft.com/en-ca/search/?terms=HtmlHelp), [google](https://www.google.com/search?q=HtmlHelp) or [google groups](https://groups.google.com/groups?q=HtmlHelp).

#### Return Value

Depending on the specified cmd and the result:

 HH_GET_WIN_TYPE :
 tuple: (hwnd as below, and the win32help::HH_WINTYPE object).
 Deep copy the structure to which dwData points before modifying the structure.

 HH_INITIALIZE :
 tuple: (hwnd as below, and the cookie).
 This call returns a cookie that you must pass as the value of data when you call HH_UNINITIALIZE .

 All other commands :

 HtmlHelp() returns one or both of the following:
 The handle (hwnd) of the help window.
 NULL. In some cases, NULL indicates failure; in other cases, NULL indicates that the help window has not yet been created.


---

<!-- page: win32help__NMHDR_meth.html -->

## win32help.NMHDR

 PyNMHDR = NMHDR()

Creates a new NMHDR object.


---

<!-- page: win32help__WinHelp_meth.html -->

## win32help.WinHelp

 WinHelp(hwnd, hlpFile, cmd, data)

Invokes the Windows Help system.

#### Parameters

- hwnd : int

 The handle of the window requesting help.

- hlpFile : string

 The name of the help file.

- cmd : int

 The type of help. See the api for full details.

- data=None : None/int/string

 Additional data specific to the help call. Can be a buffer or pointer-sized int.

#### Win32 API References

- Search for WinHelp at [msdn](https://learn.microsoft.com/en-ca/search/?terms=WinHelp), [google](https://www.google.com/search?q=WinHelp) or [google groups](https://groups.google.com/groups?q=WinHelp).

#### Return Value

The method raises an exception if an error occurs.
