# 模块 win32ui

> 来源：https://mhammond.github.io/pywin32/win32ui.html （及其成员页，已全部内联）

## Module win32ui

 A module, encapsulating the Microsoft Foundation Classes.

#### Methods

- AddToRecentFileList

 Add a file name to the Recent File List.

- ComparePath

 Compares 2 paths.

- CreateMDIFrame

 Creates an MDI Frame window.

- CreateMDIChild

 Creates an MDI Child window.

- CreateBitmap

 Create a bitmap object.

- CreateBitmapFromHandle

 Creates a bitmap object from a HBITMAP.

- CreateBrush

 Creates a new GDI brush object. Returns a PyCBrush object.

- CreateButton

 Creates a button object. PyCButton::CreateWindow creates the actual control.

- CreateColorDialog

 Creates a color selection dialog box.

- CreateControl

 Creates an OLE control.

- CreateControlBar

 Creates an ControlBar

- CreateCtrlView

 Creates a control view object.

- CreateDC

 Creates a PyCDC object.

- CreateDCFromHandle

 Creates a PyCDC object from an integer handle.

- CreateDialog

 Creates a PyCDialog object.

- CreateDialogBar

 Creates a PyCDialogBar object.

- CreateDialogIndirect

 Creates a PyCDialog object from a template.

- CreatePrintDialog

 Creates a PyCPrintDialog object.

- CreateDocTemplate

 Create a PyCDocTemplate object.

- CreateEdit

 Creates an edit object. PyCEdit::CreateWindow creates the actual control.

- CreateFileDialog

 Creates a FileOpen common dialog.

- CreateFontDialog

 Creates a font selection dialog box.

- CreateFormView

 Creates a form view object.

- CreateFrame

 Creates a frame window.

- CreateImageList

 Creates an PyCImageList object.

- CreateListCtrl

 Creates a list control.

- CreateListView

 Creates a PyCListView object.

- CreateTreeCtrl

 Creates a tree control.

- CreateTreeView

 Creates a PyCTreeView object.

- CreatePalette

 Returns a HPALETTE

- CreatePopupMenu

 Creates a popup menu.

- CreateMenu

 Creates a menu

- CreatePen

 Creates a PyCPen object.

- CreateProgressCtrl

 Creates a progress bar object. PyCProgressCtrl::CreateWindow creates the actual control.

- CreatePropertyPage

 Creates a PyCPropertyPage object.

- CreatePropertyPageIndirect

 Creates a PyCPropertyPage object from a template.

- CreatePropertySheet

 Creates a PyCPropertySheet object

- CreateRectRgn

 Initializes a PyCRgn to a rectangle

- CreateRgn

 Creates a new PyCRgn object.

- CreateRichEditCtrl

 Creates a rich edit control.

- CreateRichEditDocTemplate

 Create a PyCRichEditDocTemplate object.

- CreateRichEditView

 Creates a PyCRichEditView object.

- CreateSliderCtrl

 Creates a slider control object. PyCSliderCtrl::CreateWindow creates the actual control.

- CreateSplitter

 Creates a splitter window.

- CreateStatusBar

 Creates a status bar object.

- CreateStatusBarCtrl

 Creates a new status bar control object. PyCStatusBarCtrl::CreateWindow creates the actual control.

- CreateFont

 Creates a PyCFont object.

- CreateToolBar

 Creates a toolbar object.

- CreateToolBarCtrl

 Creates a toolbar object.

- CreateToolTipCtrl

 Creates a tooltip control object.

- CreateThread

 Creates a PyCWinThread object.

- CreateView

 Creates a PyCView object.

- CreateEditView

 Creates an PyCEditView object.

- CreateDebuggerThread

 Starts a debugging thread.

- CreateWindowFromHandle

 Creates a PyCWnd from an integer containing a HWND

- CreateWnd

 Create a new unitialized PyCWnd object

- DestroyDebuggerThread

 Cleans up the debugger thread.

- DoWaitCursor

 Changes the cursor to/from a wait cursor.

- DisplayTraceback

 Displays a traceback in a dialog box.

- Enable3dControls

 Enables 3d controls for the application.

- FindWindow

 Searches for the specified top-level window

- FindWindowEx

 Searches for the specified top-level or child window

- FullPath

 Returns the full path name of the file.

- GetActiveWindow

 Retrieves the active window.

- GetApp

 Retrieves the application object.

- GetAppName

 Retrieves the name of the current application.

- GetAppRegistryKey

 Returns the registry key for the application.

- GetBytes

 Gets raw bytes from memory

- GetCommandLine

 Returns the command line for hte application.

- GetDeviceCaps

 Calls the API version of GetDeviceCaps. See also PyCDC::GetDeviceCaps

- GetFileTitle

 Given a file name, return its title

- GetFocus

 Retrieves the window with the focus.

- GetForegroundWindow

 Retrieves the foreground window.

- GetHalftoneBrush

 Returns a halftone brush.

- GetInitialStateRequest

 Returns the requested state that the application start in. This is the same as the parameter available to PyCWnd::ShowWindow

- GetMainFrame

 Returns a window object for the main application frame.

- GetName

 Returns the name of the current application.

- GetProfileFileName

 Returns the name of the INI file used by the application.

- GetProfileVal

 Returns a value from the applications INI file.

- GetRecentFileList

 Returns the recent file list.

- GetResource

 Gets a resource.

- GetThread

 Retrieves the current thread object.

- GetType

 Retrieves a Python Type object given its name

- InitRichEdit

 Initializes the rich edit framework.

- InstallCallbackCaller

 Installs a callback caller.

- IsDebug

 Returns a flag indicating if the current win32ui build is a DEBUG build.

- IsWin32s

 Determines if the application is running under Win32s.

- IsObject

 Determines if the passed object is a win32ui object.

- LoadDialogResource

 Loads a dialog resource, and returns a list detailing the objects.

- LoadLibrary

 Creates a PyDLL object.

- LoadMenu

 Loads a menu.

- LoadStdProfileSettings

 Loads standard application profile settings.

- LoadString

 Loads a string from a resource file.

- MessageBox

 Displays a message box.

- OutputDebugString

 Writes output to the Windows debugger.

- EnableControlContainer

 Call this function in your application object's InitInstance function to enable support for containment of OLE controls.

- PrintTraceback

 Prints a Traceback using the default Python traceback printer.

- PumpWaitingMessages

 Pumps all waiting messages to the application.

- RegisterWndClass

 Registers a window class

- RemoveRecentFile

 Removes the recent file at list index.

- SetAppHelpPath

 Sets the application help file path, i.e. the pApp->m_pszHelpFilePath member variable.

- SetAppName

 Sets the application name.

- SetCurrentInstanceHandle

 Sets the MFC variable afxCurrentInstanceHandle.

- SetCurrentResourceHandle

 Sets the MFC variable afxCurrentResourceHandle.

- SetDialogBkColor

 Sets the default background and text color for dialog boxes and message boxes within the application.

- SetProfileFileName

 Sets the INI file name used by the application.

- SetRegistryKey

 Causes application settings to be stored in the registry instead of INI files.

- SetResource

 Specifies the default DLL object for application resources.

- SetStatusText

 Sets the text in the status bar.

- StartDebuggerPump

 Starts the debugger message pump.

- StopDebuggerPump

 Stops the debugger message pump.

- TranslateMessage

 Calls ::TranslateMessage.

- TranslateVirtualKey

 Translates a virtual key.

- WinHelp

 Invokes the Window Help engine.

- WriteProfileVal

 Writes a value to the INI file.


---

# win32ui 成员详细文档（共 115 项）


---

<!-- page: win32ui__AddToRecentFileList_meth.html -->

## win32ui.AddToRecentFileList

 AddToRecentFileList(fileName)

Adds an entry to the applications Recent File List.

#### Parameters

- fileName : string

 The file name to be added to the list.

#### MFC References

- CWinApp::AddToRecentFileList


---

<!-- page: win32ui__ComparePath_meth.html -->

## win32ui.ComparePath

 int = ComparePath(path1, path2 )

Compares 2 paths.

#### Parameters

- path1 : string

 The path name.

- path2 : string

 The path name.


---

<!-- page: win32ui__CreateBitmapFromHandle_meth.html -->

## win32ui.CreateBitmapFromHandle

 PyCBitMap = CreateBitmapFromHandle()

Creates a bitmap object from a HBITMAP.


---

<!-- page: win32ui__CreateBitmap_meth.html -->

## win32ui.CreateBitmap

 PyCBitMap = CreateBitmap()

Creates a bitmap object.


---

<!-- page: win32ui__CreateBrush_meth.html -->

## win32ui.CreateBrush

 PyCBrush = CreateBrush()

Creates a new brush object.

#### Alternative Parameters

- style

 The brush style.

- color

 The brush color.

- hatch

 The brush hatching.

#### Comments

 If called with no arguments, an uninitialized brush is created.


---

<!-- page: win32ui__CreateButton_meth.html -->

## win32ui.CreateButton

 PyCButton = CreateButton()

Creates a button object. PyCButton::CreateWindow creates the actual control.


---

<!-- page: win32ui__CreateColorDialog_meth.html -->

## win32ui.CreateColorDialog

 PyCColorDialog = CreateColorDialog(initColor, flags , parent )

Creates a color selection dialog box. self*/, PyObject *args)

#### Parameters

- initColor=0 : int

 The initial color.

- flags=0 : int

 The choose-color flags to use.

- parent=None : PyCWnd

 The parent or owner window of the dialog.


---

<!-- page: win32ui__CreateControlBar_meth.html -->

## win32ui.CreateControlBar

 PyCControlBar = CreateControlBar()

Creates a control bar object.


---

<!-- page: win32ui__CreateControl_meth.html -->

## win32ui.CreateControl

 PyCWnd = CreateControl(classId, windowName , style , rect , parent , id , obPersist , bStorage , licKey )

Creates an OLE control.

#### Parameters

- classId : string

 The class ID for the window.

- windowName : string

 The title for the window.

- style : int

 The style for the control.

- rect : (left, top, right, bottom)

 The default position of the window.

- parent : PyCWnd

 The parent window

- id : int

 The child ID for the view

- obPersist=None : object

 Place holder for future support.

- bStorage=FALSE : int

 Not used.

- licKey=None : string

 The license key for the control.

#### Return Value

The result is a PyCWnd (or derived) object, or a win32ui.error exception is raised.


---

<!-- page: win32ui__CreateCtrlView_meth.html -->

## win32ui.CreateCtrlView

 PyCCtrlView = CreateCtrlView(doc, className , style )

Creates a control view object.

#### Parameters

- doc : PyCDocument

 The document.

- className : string

 The class name of the control

- style=0 : int

 Additional style bits


---

<!-- page: win32ui__CreateDCFromHandle_meth.html -->

## win32ui.CreateDCFromHandle

 CreateDCFromHandle()

Creates a DC object from an integer handle.


---

<!-- page: win32ui__CreateDC_meth.html -->

## win32ui.CreateDC

 CreateDC()

Creates an uninitialised device context.


---

<!-- page: win32ui__CreateDebuggerThread_meth.html -->

## win32ui.CreateDebuggerThread

 CreateDebuggerThread()

Starts a debugging thread (ie, creates the "break" button).

#### Comments

 This allows an application which is performing a long operation to dispatch paint messages during the operation.


---

<!-- page: win32ui__CreateDialogBar_meth.html -->

## win32ui.CreateDialogBar

 PyCDialogBar = CreateDialogBar()

Creates a PyCDialogBar object.


---

<!-- page: win32ui__CreateDialogIndirect_meth.html -->

## win32ui.CreateDialogIndirect

 PyCDialog = CreateDialogIndirect(obList)

Creates a dialog object from a template.

#### Parameters

- obList : list

 A list of [PyDLGTEMPLATE, PyDLGITEMTEMPLATE, ...], which describe the dialog to be created.


---

<!-- page: win32ui__CreateDialog_meth.html -->

## win32ui.CreateDialog

 PyCDialog = CreateDialog(idRes, dll )

Creates a dialog object.

#### Parameters

- idRes : int

 The ID of the dialog resource to load.

- dll=None : PyDLL

 The DLL object to load the dialog from.


---

<!-- page: win32ui__CreateDocTemplate_meth.html -->

## win32ui.CreateDocTemplate

 PyCDocTemplate = CreateDocTemplate(idRes)

Creates a document template object.

#### Parameters

- idRes : int

 The ID for resources for documents of this type.


---

<!-- page: win32ui__CreateEditView_meth.html -->

## win32ui.CreateEditView

 PyCEditView = CreateEditView(doc)

Creates a PyEditView object.

#### Parameters

- doc : PyCDocument

 The document to use with the view.


---

<!-- page: win32ui__CreateEdit_meth.html -->

## win32ui.CreateEdit

 PyCEdit = CreateEdit()

Creates an Edit object. PyCEdit::CreateWindow creates the actual control.


---

<!-- page: win32ui__CreateFileDialog_meth.html -->

## win32ui.CreateFileDialog

 PyCFileDialog = CreateFileDialog(bFileOpen, defExt , fileName , flags , filter , parent )

Creates a File Open/Save/etc Common Dialog. self*/, PyObject *args)

#### Parameters

- bFileOpen : int

 A flag indicating if the Dialog is a FileOpen or FileSave dialog.

- defExt=None : string

 The default file extension for saved files. If None, no extension is supplied.

- fileName=None : string

 The initial filename that appears in the filename edit box. If None, no filename initially appears.

- flags=win32con.OFN_HIDEREADONLY|win32con.OFN_OVERWRITEPROMPT : int

 The flags for the dialog. See the API documentation for full details.

- filter=None : string

 A series of string pairs that specify filters you can apply to the file. If you specify file filters, only selected files will appear in the Files list box. The first string in the string pair describes the filter; the second string indicates the file extension to use. Multiple extensions may be specified using ';' as the delimiter. The string ends with two '|' characters. May be None.

- parent=None : PyCWnd

 The parent or owner window of the dialog.


---

<!-- page: win32ui__CreateFontDialog_meth.html -->

## win32ui.CreateFontDialog

 PyCFontDialog = CreateFontDialog(font, flags , dcPrinter , parent )

Creates a font selection dialog box. self*/, PyObject *args)

#### Parameters

- font=None : dict/tuple

 A dictionary describing a LOGFONT, or a tuple describing a CHARFORMAT.

- flags=win32con.CF_EFFECTS|win32con.CF_SCREENFONTS : int

 The choose-font flags to use.

- dcPrinter=None : PyCDC

 Show fonts available for the specified device.

- parent=None : PyCWnd

 The parent or owner window of the dialog.


---

<!-- page: win32ui__CreateFont_meth.html -->

## win32ui.CreateFont

 PyCFont = CreateFont(properties)

Creates a PyCFont object.

#### Parameters

- properties : dict

 A dictionary containing the font properties. Valid dictionary keys are:
 height
 width
 escapement
 orientation
 weight
 italic
 underline
 strike out
 charset
 out precision
 clip precision
 quality
 pitch and family
 name

#### Comments

 The code for the PyCFont was contributed by Dave Brennan (Last known address is brennan@hal.com, but I hear he is now at Microsoft) args contains a dict of font properties


---

<!-- page: win32ui__CreateFormView_meth.html -->

## win32ui.CreateFormView

 PyCFormView = CreateFormView(doc, Template )

Creates a form view object.

#### Parameters

- doc : PyCDocument

 The document to use with the view.

- Template : int/str

 Name or ID of the dialog template resource


---

<!-- page: win32ui__CreateFrame_meth.html -->

## win32ui.CreateFrame

 PyFrameWnd = CreateFrame()

Creates a Frame window.

#### Return Value

The window object (not the OS window) created. An exception is raised if an error occurs.


---

<!-- page: win32ui__CreateImageList_meth.html -->

## win32ui.CreateImageList

 int = CreateImageList(cx, cy , mask , initial , grow )

Creates an image list.

#### Parameters

- cx : int

 Dimension of each image, in pixels.

- cy : int

 Dimension of each image, in pixels.

- mask : int

 TRUE if the image contains a mask; otherwise FALSE.

- initial : int

 Number of images that the image list initially contains.

- grow : int

 Number of images by which the image list can grow when the system needs to resize the list to make room for new images. This parameter represents the number of new images the resized image list can contain.

#### Alternative Parameters

- bitmapId

 Resource name or ID of the bitmap to be associated with the image list.

- cx

 Dimension of each image, in pixels.

- grow

 Number of images by which the image list can grow when the system needs to resize the list to make room for new images. This parameter represents the number of new images the resized image list can contain.

- crMask

 Color used to generate a mask. Each pixel of this color in the specified bitmap is changed to black, and the corresponding bit in the mask is set to one.


---

<!-- page: win32ui__CreateListCtrl_meth.html -->

## win32ui.CreateListCtrl

 PyCListCtrl = CreateListCtrl()

Creates a list control.


---

<!-- page: win32ui__CreateListView_meth.html -->

## win32ui.CreateListView

 PyCListView = CreateListView(doc)

Creates a PyCListView object.

#### Parameters

- doc : PyCDocument

 The document to use with the view.


---

<!-- page: win32ui__CreateMDIChild_meth.html -->

## win32ui.CreateMDIChild

 PyCMDIChildWnd = CreateMDIChild()

Creates an MDI Child window.

#### Return Value

The window object created. An exception is raised if an error occurs.


---

<!-- page: win32ui__CreateMDIFrame_meth.html -->

## win32ui.CreateMDIFrame

 PyCMDIFrameWnd = CreateMDIFrame()

Creates an MDI Frame window.

#### Comments

 An MDI Frame Window is usually the main application window. Therefore there is uaually only one of these windows per application.

 An application can only hae one main window. This method will fail if the application window already exists.

#### Return Value

The window object created. An exception is raised if an error occurs.


---

<!-- page: win32ui__CreateMenu_meth.html -->

## win32ui.CreateMenu

 PyCMenu = CreateMenu()

Creates a menu object.


---

<!-- page: win32ui__CreatePalette_meth.html -->

## win32ui.CreatePalette

 int = CreatePalette(lp)

Creates a HPALETTE

#### Parameters

- lp : LOGPALETTE

 The entries for the palette.


---

<!-- page: win32ui__CreatePen_meth.html -->

## win32ui.CreatePen

 PyCPen = CreatePen(style, width , color )

Creates a PyCPen object. static*/ PyObject *ui_pen_object::create(PyObject *self, PyObject *args)

#### Parameters

- style : int

 The pen style.

- width : int

 The pen width.

- color : long

 The pen color.


---

<!-- page: win32ui__CreatePopupMenu_meth.html -->

## win32ui.CreatePopupMenu

 PyCMenu = CreatePopupMenu()

Creates a popup menu object.


---

<!-- page: win32ui__CreatePrintDialog_meth.html -->

## win32ui.CreatePrintDialog

 PyCPrintDialog = CreatePrintDialog(idRes, bPrintSetupOnly , dwFlags , parent , dll )

Creates a print dialog object.

#### Parameters

- idRes : int

 The ID of the dialog resource to load.

- bPrintSetupOnly=FALSE : int

 Specifies whether the standard Windows Print dialog box or Print Setup dialog box is displayed.

- dwFlags=PD_ALLPAGES|PD_USEDEVMODECOPIES|PD_NOPAGENUMS|PD_HIDEPRINTTOFILE|PD_NOSELECTION : int

 One or more flags you can use to customize the settings of the dialog box, combined using the bitwise OR operator.

- parent=None : PyCWnd

 A pointer to the dialog box parent or owner window.

- dll=None : PyDLL

 The DLL object to load the dialog from.


---

<!-- page: win32ui__CreateProgressCtrl_meth.html -->

## win32ui.CreateProgressCtrl

 PyCProgressCtrl = CreateProgressCtrl()

Creates a progress control object. PyProgressCtrl::Create creates the actual control.


---

<!-- page: win32ui__CreatePropertyPageIndirect_meth.html -->

## win32ui.CreatePropertyPageIndirect

 PyCPropertyPage = CreatePropertyPageIndirect(resourceList, caption )

Creates a property page object from a template.

#### Parameters

- resourceList : PyDialogTemplate

 Definition of the page to be created.

- caption=0 : int

 The ID if the string resource to use for the caption.


---

<!-- page: win32ui__CreatePropertyPage_meth.html -->

## win32ui.CreatePropertyPage

 PyCPropertyPage = CreatePropertyPage(resource, caption )

Creates a property page object.

#### Parameters

- resource : PyResourceId

 String template name or inteter resource ID to use for the page.

- caption=0 : int

 The ID if the string resource to use for the caption.


---

<!-- page: win32ui__CreatePropertySheet_meth.html -->

## win32ui.CreatePropertySheet

 PyCPropertySheet = CreatePropertySheet(caption, parent , select )

Creates a property sheet object.

#### Parameters

- caption : PyResourceId

 The caption for the property sheet, or id of the caption

- parent=None : PyCWnd

 The parent window of the property sheet.

- select=0 : int

 The index of the first page to be selected.


---

<!-- page: win32ui__CreateRgn_meth.html -->

## win32ui.CreateRgn

 PyCRgn = CreateRgn()

Creates a new rgn object. Return Values: a PyCRgn object


---

<!-- page: win32ui__CreateRichEditCtrl_meth.html -->

## win32ui.CreateRichEditCtrl

 PyCRichEditCtrl = CreateRichEditCtrl()

Creates a rich edit control.

#### Comments

 This method only creates the RichEdit object. To create the window, (ie, the control itself), call PyCRichEdit::CreateWindow


---

<!-- page: win32ui__CreateRichEditDocTemplate_meth.html -->

## win32ui.CreateRichEditDocTemplate

 PyCRichEditDocTemplate = CreateRichEditDocTemplate(idRes)

Creates a document template object.

#### Parameters

- idRes : int

 The ID for resources for documents of this type.


---

<!-- page: win32ui__CreateRichEditView_meth.html -->

## win32ui.CreateRichEditView

 PyCRichEditView = CreateRichEditView(doc)

Creates a PyRichEditView object.

#### Parameters

- doc=None : PyCDocument

 The document to use with the view, or None for NULL.


---

<!-- page: win32ui__CreateSliderCtrl_meth.html -->

## win32ui.CreateSliderCtrl

 PyCSliderCtrl = CreateSliderCtrl()

Creates a Slider control object.

#### Comments

 The method PySliderCtrl::CreateWindow is used to create the actual control.


---

<!-- page: win32ui__CreateSplitter_meth.html -->

## win32ui.CreateSplitter

 PyCSplitterWnd = CreateSplitter()

Creates a splitter window object.


---

<!-- page: win32ui__CreateStatusBarCtrl_meth.html -->

## win32ui.CreateStatusBarCtrl

 PyCStatusBarCtrl = CreateStatusBarCtrl()

Creates a progress control object. PyStatusBarCtrl::Create creates the actual control.


---

<!-- page: win32ui__CreateStatusBar_meth.html -->

## win32ui.CreateStatusBar

 PyCStatusBar = CreateStatusBar(parent, style , windowId , ctrlStype )

Creates a statusbar object.

#### Parameters

- parent : PyCWnd

 The parent window for the status bar.

- style=afxres.WS_CHILD | afxres.WS_VISIBLE | afxres.CBRS_BOTTOM : int

 The style for the status bar.

- windowId=afxres.AFX_IDW_STATUS_BAR : int

 The child window ID.

- ctrlStype=0 : int

 Additional styles for the creation of the embedded PyCStatusBarCtrl object.
Status bar styles supported are:
commctrl.SBARS_SIZEGRIP - The status bar control includes a sizing grip at the right end of the status bar. A sizing grip is similar to a sizing border; it is a rectangular area that the user can click and drag to resize the parent window.
commctrl.SBT_TOOLTIPS - The status bar supports tooltips.

#### Comments

 You must ensure no 2 status bars share the same ID.

#### MFC References

- CStatusBar::CreateEx


---

<!-- page: win32ui__CreateThread_meth.html -->

## win32ui.CreateThread

 PyCWinThread = CreateThread()

Creates a new PyCWinThread object


---

<!-- page: win32ui__CreateToolBarCtrl_meth.html -->

## win32ui.CreateToolBarCtrl

 PyCToolBarCtrl = CreateToolBarCtrl()

Creates a toolbar control object. PyCToolBarCtrl::CreateWindow creates the actual control.


---

<!-- page: win32ui__CreateToolBar_meth.html -->

## win32ui.CreateToolBar

 PyCToolBar = CreateToolBar(parent, style , windowId )

Creates a toolbar object.

#### Parameters

- parent : PyCWnd

 The parent window for the toolbar.

- style : int

 The style for the toolbar.

- windowId=afxres.AFX_IDW_TOOLBAR : int

 The child window ID.

#### Comments

 You must ensure no 2 toolbars share the same ID.


---

<!-- page: win32ui__CreateToolTipCtrl_meth.html -->

## win32ui.CreateToolTipCtrl

 PyCToolTipCtrl = CreateToolTipCtrl()

Creates a progress control object. PyToolTipCtrl::Create creates the actual control.


---

<!-- page: win32ui__CreateTreeCtrl_meth.html -->

## win32ui.CreateTreeCtrl

 PyCTreeCtrl = CreateTreeCtrl()

Creates a tree control.


---

<!-- page: win32ui__CreateTreeView_meth.html -->

## win32ui.CreateTreeView

 PyCTreeView = CreateTreeView(doc)

Creates a PyCTreeView object.

#### Parameters

- doc : PyCDocument

 The document to use with the view.


---

<!-- page: win32ui__CreateView_meth.html -->

## win32ui.CreateView

 PyCScrollView = CreateView(doc)

Creates a generic view object.

#### Parameters

- doc : PyCDocument

 The document to use with the view.


---

<!-- page: win32ui__CreateWindowFromHandle_meth.html -->

## win32ui.CreateWindowFromHandle

 PyCWnd = CreateWindowFromHandle(hwnd)

Creates a PyCWnd from an integer containing a HWND

#### Parameters

- hwnd : int

 The window handle.

#### Return Value

The result is a PyCWnd (or derived) object, or a win32ui.error exception is raised.


---

<!-- page: win32ui__CreateWnd_meth.html -->

## win32ui.CreateWnd

 PyCWnd = CreateWnd()

Creates an unitialized PyCWnd


---

<!-- page: win32ui__DestroyDebuggerThread_meth.html -->

## win32ui.DestroyDebuggerThread

 DestroyDebuggerThread()

Cleans up the debugger thread. See win32ui::CreateDebuggerThread.


---

<!-- page: win32ui__DisplayTraceback_meth.html -->

## win32ui.DisplayTraceback

 DisplayTraceback()

Displays a traceback in a dialog box.


---

<!-- page: win32ui__DoWaitCursor_meth.html -->

## win32ui.DoWaitCursor

 DoWaitCursor(code)

Dispay a wait cursor.

#### Parameters

- code : int

 If this parameter is 0, the original cursor is restored. If 1, a wait cursor appears. If -1, the wait cursor ends.


---

<!-- page: win32ui__Enable3dControls_meth.html -->

## win32ui.Enable3dControls

 int = Enable3dControls()

Enables 3d controls for the application.

#### Return Value

True if 3d controls could be enabled, false otherwise.


---

<!-- page: win32ui__EnableControlContainer_meth.html -->

## win32ui.EnableControlContainer

 int = EnableControlContainer()

Enables support for containment of OLE controls.


---

<!-- page: win32ui__FindWindowEx_meth.html -->

## win32ui.FindWindowEx

 PyCWnd = FindWindowEx(parentWindow, childAfter , className , windowName )

Searches for the specified top-level or child window

#### Parameters

- parentWindow : PyCWnd

 The parent whose children will be searched. If None, the desktops window will be used.

- childAfter : PyCWnd

 The search begins with the next window in the Z order. If None, all children are searched.

- className : string

 The window class name to find, else None

- windowName : string

 The window name (ie, title) to find, else None

#### Return Value

The result is a PyCWnd (or derived) object, or a win32ui.error exception is raised.


---

<!-- page: win32ui__FindWindow_meth.html -->

## win32ui.FindWindow

 PyCWnd = FindWindow(className, windowName )

Searches for the specified top-level window

#### Parameters

- className : string

 The window class name to find, else None

- windowName : string

 The window name (ie, title) to find, else None

#### Return Value

The result is a PyCWnd (or derived) object, or a win32ui.error exception is raised.


---

<!-- page: win32ui__FullPath_meth.html -->

## win32ui.FullPath

 string = FullPath(path)

Return the fully qualified path of a file name.

#### Parameters

- path : string

 The path name.


---

<!-- page: win32ui__GetActiveWindow_meth.html -->

## win32ui.GetActiveWindow

 PyCWnd = GetActiveWindow()

Retrieves the active window.

#### Return Value

The result is a PyCWnd (or derived) object, or a win32ui.error exception is raised.


---

<!-- page: win32ui__GetAppName_meth.html -->

## win32ui.GetAppName

 int = GetAppName()

Returns the application name.


---

<!-- page: win32ui__GetAppRegistryKey_meth.html -->

## win32ui.GetAppRegistryKey

 GetAppRegistryKey()

Returns the registry key for the application.


---

<!-- page: win32ui__GetApp_meth.html -->

## win32ui.GetApp

 PyCWinApp = GetApp()

Retrieves the application object.

#### Comments

 There will only ever be one application object per application.


---

<!-- page: win32ui__GetBytes_meth.html -->

## win32ui.GetBytes

 string = GetBytes(address, size )

Gets raw bytes from memory

#### Parameters

- address : int

 The memory address

- size : int

 The size to get.

#### Comments

 This method is useful to help decode unknown notify messages. You must be very carefull when using this method.

#### Return Value

The result is a string with a length of size.


---

<!-- page: win32ui__GetCommandLine_meth.html -->

## win32ui.GetCommandLine

 string = GetCommandLine()

Returns the application's command line.

#### Win32 API References

- Search for GetCommandLine at [msdn](https://learn.microsoft.com/en-ca/search/?terms=GetCommandLine), [google](https://www.google.com/search?q=GetCommandLine) or [google groups](https://groups.google.com/groups?q=GetCommandLine).


---

<!-- page: win32ui__GetDeviceCaps_meth.html -->

## win32ui.GetDeviceCaps

 int = GetDeviceCaps(hdc, index )

Calls the API version of GetDeviceCaps. See also PyCDC::GetDeviceCaps

#### Parameters

- hdc : int

- index : int


---

<!-- page: win32ui__GetFileTitle_meth.html -->

## win32ui.GetFileTitle

 string = GetFileTitle(fileName)

Given a file name, return its title

#### Parameters

- fileName : string

 The file name.


---

<!-- page: win32ui__GetFocus_meth.html -->

## win32ui.GetFocus

 PyCWnd = GetFocus()

Retrieves the window with the focus.

#### Return Value

The result is a PyCWnd (or derived) object, or a win32ui.error exception is raised.


---

<!-- page: win32ui__GetForegroundWindow_meth.html -->

## win32ui.GetForegroundWindow

 PyCWnd = GetForegroundWindow()

Retrieves the foreground window.

#### Return Value

The result is a PyCWnd (or derived) object, or a win32ui.error exception is raised.


---

<!-- page: win32ui__GetHalftoneBrush_meth.html -->

## win32ui.GetHalftoneBrush

 PyCBrush = GetHalftoneBrush()

Creates a new halftone brush object.


---

<!-- page: win32ui__GetInitialStateRequest_meth.html -->

## win32ui.GetInitialStateRequest

 int = GetInitialStateRequest()

Returns the requested state that the application start in. This is the same as the parameter available to PyCWnd::ShowWindow

#### Comments

 In some cases, it may not be possible to start in the requested mode. An application may start in its default mode, then set its mode to match the value returned from this method.


---

<!-- page: win32ui__GetMainFrame_meth.html -->

## win32ui.GetMainFrame

 PyCWnd = GetMainFrame()

Returns a window object for the main application frame.


---

<!-- page: win32ui__GetName_meth.html -->

## win32ui.GetName

 string = GetName()

Returns the name of the current executable.


---

<!-- page: win32ui__GetProfileFileName_meth.html -->

## win32ui.GetProfileFileName

 string = GetProfileFileName()

Returns the name of the INI file used by the application.


---

<!-- page: win32ui__GetProfileVal_meth.html -->

## win32ui.GetProfileVal

 int/string = GetProfileVal(section, entry , defValue )

Returns a value from the application's INI file.

#### Parameters

- section : string

 The section in the INI file to read from.

- entry : string

 The entry within the section in the INI file to read.

- defValue : int/string

 The default value. The type of this parameter determines the method's return type.


---

<!-- page: win32ui__GetRecentFileList_meth.html -->

## win32ui.GetRecentFileList

 list = GetRecentFileList()

Returns the entries in the applications Recent File List.

#### Return Value

A list of strings containing the fully qualified file names.


---

<!-- page: win32ui__GetRect_meth.html -->

## win32ui.GetRect

 tuple = GetRect()

Returns the rectangle of the main application frame. See PyCWnd::GetWindowRecr for further details.

#### Return Value

A tuple of integers with (left, top, right, bottom)


---

<!-- page: win32ui__GetResource_meth.html -->

## win32ui.GetResource

 PyDLL = GetResource()

Retrieve the object associated with the applications resources.


---

<!-- page: win32ui__GetThread_meth.html -->

## win32ui.GetThread

 PyCWinApp = GetThread()

Retrieves the current thread object.


---

<!-- page: win32ui__GetType_meth.html -->

## win32ui.GetType

 object = GetType()

Retrieves a Python Type object given its name


---

<!-- page: win32ui__InitRichEdit_meth.html -->

## win32ui.InitRichEdit

 string = InitRichEdit()

Initializes the rich edit framework.


---

<!-- page: win32ui__InstallCallBackCaller_meth.html -->

## win32ui.InstallCallBackCaller

 object = InstallCallBackCaller()

Install a Python method which will dispatch all callbacks into Python.

#### Return Value

The previous callback caller.


---

<!-- page: win32ui__IsDebug_meth.html -->

## win32ui.IsDebug

 int = IsDebug()

Returns a flag indicating if the current win32ui build is a DEBUG build.

#### Comments

 This should not normally be of relevance to the Python programmer. However, under certain circumstances Python code may wish to detect this.


---

<!-- page: win32ui__IsObject_meth.html -->

## win32ui.IsObject

 int = IsObject(o)

Determines if the passed object is a win32ui object.

#### Parameters

- o : object

 The object to check.


---

<!-- page: win32ui__IsWin32s_meth.html -->

## win32ui.IsWin32s

 int = IsWin32s()

Returns False.


---

<!-- page: win32ui__LoadDialogResource_meth.html -->

## win32ui.LoadDialogResource

 list = LoadDialogResource(idRes, dll )

Loads a dialog resource, and returns a list detailing the objects.

#### Parameters

- idRes : int

 The ID of the dialog resource to load.

- dll=None : PyDLL

 The DLL object to load the dialog from.


---

<!-- page: win32ui__LoadLibrary_meth.html -->

## win32ui.LoadLibrary

 PyDLL = LoadLibrary(fileName)

Creates a DLL object, and loads a Windows DLL into the object.

#### Parameters

- fileName : string

 The name of the DLL file to load.


---

<!-- page: win32ui__LoadMenu_meth.html -->

## win32ui.LoadMenu

 PyCMenu = LoadMenu(id, dll )

Creates and loads a menu resource from a DLL.

#### Parameters

- id : int

 The Id of the menu to load.

- dll=None : PyDLL

 The DLL to load from.


---

<!-- page: win32ui__LoadStdProfileSettings_meth.html -->

## win32ui.LoadStdProfileSettings

 LoadStdProfileSettings(maxFiles)

Loads MFC standard settings from the applications INI file. This includes the Recent File List, etc.

#### Parameters

- maxFiles=_AFX_MRU_COUNT : int

 The maximum number of files to maintain on the Recently Used File list.

#### Comments

 This function can only be called once in an applications lifetime, else an exception is raised.


---

<!-- page: win32ui__LoadString_meth.html -->

## win32ui.LoadString

 string = LoadString(stringId)

Loads a string from a resource file.

#### Parameters

- stringId : int

 The ID of the string to load.


---

<!-- page: win32ui__MessageBox_meth.html -->

## win32ui.MessageBox

 int = MessageBox(message, title , style )

Display a message box.

#### Parameters

- message : string

 The message to be displayed in the message box.

- title=None : string/None

 The title for the message box. If None, the applications title will be used.

- style=win32con.MB_OK : int

 The style of the message box.

#### Return Value

An integer identifying the button pressed to dismiss the dialog.


---

<!-- page: win32ui__OutputDebugString_meth.html -->

## win32ui.OutputDebugString

 OutputDebugString(msg)

Sends a string to the Windows debugging device.

#### Parameters

- msg : string

 The string to write.


---

<!-- page: win32ui__PrintTraceback_meth.html -->

## win32ui.PrintTraceback

 PrintTraceback(tb, output)

Prints a traceback using the internal Python mechanism.

#### Parameters

- tb : object

 The traceback to print.

- output : object

 The object to write the traceback to.


---

<!-- page: win32ui__PumpWaitingMessages_meth.html -->

## win32ui.PumpWaitingMessages

 int = PumpWaitingMessages(firstMessage, lastMessage )

Recursively start a new message dispatching loop while any message remain in the queue.

#### Parameters

- firstMessage=WM_PAINT : int

 The lowest message ID to retrieve

- lastMessage=WM_PAINT : int

 The highest message ID to retrieve

#### Comments

 This allows an application which is performing a long operation to dispatch paint messages during the operation.

#### Return Value

The result is 1 if a WM_QUIT message was processed, otherwise 0.


---

<!-- page: win32ui__RegisterWndClass_meth.html -->

## win32ui.RegisterWndClass

 string = RegisterWndClass(style, hCursor , hBrush , hIcon )

Registers a window class

#### Parameters

- style : int

 Specifies the Windows class style or combination of styles

- hCursor=0 : int

- hBrush=0 : int

- hIcon=0 : int

#### Comments

 The Microsoft Foundation Class Library automatically registers several standard window classes for you. Call this function if you want to register your own window classes.


---

<!-- page: win32ui__RemoveRecentFile_meth.html -->

## win32ui.RemoveRecentFile

 RemoveRecentFile(index)

Removes the entry in the applications Recent File List at index.

#### Parameters

- index=0 : int

 Zero-based index of the file to be removed from the MRU (most recently used) file list.


---

<!-- page: win32ui__SetAppHelpPath_meth.html -->

## win32ui.SetAppHelpPath

 int = SetAppHelpPath()

Set the pApp->m_pszHelpFilePath variable.


---

<!-- page: win32ui__SetAppName_meth.html -->

## win32ui.SetAppName

 int = SetAppName(appName)

Sets the name of the application.

#### Parameters

- appName : string

 The new name for the application. This is used for the default registry key, and the title bar of the application.

#### MFC References

- CWinApp::m_pszAppName


---

<!-- page: win32ui__SetCurrentInstanceHandle_meth.html -->

## win32ui.SetCurrentInstanceHandle

 int = SetCurrentInstanceHandle(newVal)

Sets the MFC variable afxCurrentInstanceHandle

#### Parameters

- newVal : int

 The new value for afxCurrentInstanceHandle

#### Return Value

The result is the previous value of afxCurrentInstanceHandle


---

<!-- page: win32ui__SetCurrentResourceHandle_meth.html -->

## win32ui.SetCurrentResourceHandle

 int = SetCurrentResourceHandle(newVal)

Sets the MFC variable afxCurrentResourceHandle

#### Parameters

- newVal : int

 The new value for afxCurrentResourceHandle

#### Return Value

The result is the previous value of afxCurrentResourceHandle


---

<!-- page: win32ui__SetDialogBkColor_meth.html -->

## win32ui.SetDialogBkColor

 int = SetDialogBkColor(clrCtlBk, clrCtlText )

Sets the default background and text color for dialog boxes and message boxes within the application.

#### Parameters

- clrCtlBk=win32api.RGB(192, 192, 192) : int

 The color for the controls background.

- clrCtlText=win32api.RGB(0, 0, 0) : int

 The color for the controls text.

#### MFC References

- CWinApp::SetDialogBkColor


---

<!-- page: win32ui__SetProfileFileName_meth.html -->

## win32ui.SetProfileFileName

 SetProfileFileName(filename)

Sets the name of the INI file used by the application.

#### Parameters

- filename : string

 The name of the ini file.


---

<!-- page: win32ui__SetRegistryKey_meth.html -->

## win32ui.SetRegistryKey

 SetRegistryKey(key)

Causes application settings to be stored in the registry instead of INI files.

#### Parameters

- key : string

 A string containing the name of the key.

#### Comments

 Causes application settings to be stored in the registry instead of INI files. This function sets m_pszRegistryKey, which is then used by the GetProfileXXX and WriteProfileXXX member functions of CWinApp. If this function has been called, the list of most recently-used (MRU) files is also stored in the registry. The registry key is usually the name of a company. It is stored in a key of the following form: HKEY_CURRENT_USER\\Software\\<company name>\\<application name>\\<section name>\\<value name>.


---

<!-- page: win32ui__SetResource_meth.html -->

## win32ui.SetResource

 PyDLL = SetResource(dll)

Specifies the default DLL object for application resources.

#### Parameters

- dll : PyDll

 The dll object to use for default resources.

#### Return Value

The previous default DLL object.


---

<!-- page: win32ui__SetStatusText_meth.html -->

## win32ui.SetStatusText

 SetStatusText(msg, bForce)

Sets the text in the status bar of the application.

#### Parameters

- msg : string

 The message to write to the status bar.

- bForce=0 : int

 A flag indicating if the message should be forced to the status bar, or written in idle time.


---

<!-- page: win32ui__StartDebuggerPump_meth.html -->

## win32ui.StartDebuggerPump

 StartDebuggerPump()

Starts a recursive message loop, waiting for an application close message.

#### Comments

 This function is used by the debugger. It allows the debugger to interact with the user, even while the Python code is stopped. As the Python code may be responding to a Windows Event, this function works around the inherent message queue problems.


---

<!-- page: win32ui__StopDebuggerPump_meth.html -->

## win32ui.StopDebuggerPump

 StopDebuggerPump()

Stops the debugger pump. See win32ui::StartDebuggerPump.


---

<!-- page: win32ui__TranslateMessage_meth.html -->

## win32ui.TranslateMessage

 int = TranslateMessage()

Calls the API version of TranslateMessage.


---

<!-- page: win32ui__TranslateVirtualKey_meth.html -->

## win32ui.TranslateVirtualKey

 string/None = TranslateVirtualKey(vk)

#### Parameters

- vk : int

 The key to translate


---

<!-- page: win32ui__WinHelp_meth.html -->

## win32ui.WinHelp

 WinHelp(cmd, data)

Invokes the Windows Help system.

#### Parameters

- cmd=win32con.HELP_CONTEXT : int

 The type of help. See the api for full details.

- data : int/string

 Additional data specific to the help call.


---

<!-- page: win32ui__WriteProfileVal_meth.html -->

## win32ui.WriteProfileVal

 WriteProfileVal(section, entry, value)

Writes a value to the application's INI file.

#### Parameters

- section : string

 The section in the INI file to write to.

- entry : string

 The entry within the section in the INI file to write to.

- value : int/string

 The value to write. The type of this parameter determines the method's return type.
