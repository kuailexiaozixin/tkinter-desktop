# 其它零散页面合集

> 共 26 页，均来自 https://mhammond.github.io/pywin32/


---

<!-- page: PyDEVMODE__Clear_meth.html -->

## PyDEVMODE.Clear

 Clear()

Resets all members of the structure


---

<!-- page: PyIFolderView__GetAutoArrange_meth.html -->

## PyIFolderView.GetAutoArrange

 GetAutoArrange()

Description of GetAutoArrange.


---

<!-- page: PyIFolderView__GetCurrentViewMode_meth.html -->

## PyIFolderView.GetCurrentViewMode

 GetCurrentViewMode()

Description of GetCurrentViewMode.


---

<!-- page: PyIFolderView__GetDefaultSpacing_meth.html -->

## PyIFolderView.GetDefaultSpacing

 GetDefaultSpacing()

Description of GetDefaultSpacing.


---

<!-- page: PyIFolderView__GetFocusedItem_meth.html -->

## PyIFolderView.GetFocusedItem

 GetFocusedItem()

Description of GetFocusedItem.


---

<!-- page: PyIFolderView__GetFolder_meth.html -->

## PyIFolderView.GetFolder

 GetFolder(riid)

Description of GetFolder.

#### Parameters

- riid : PyIID

 Description for riid


---

<!-- page: PyIFolderView__GetItemPosition_meth.html -->

## PyIFolderView.GetItemPosition

 GetItemPosition(pidl)

Description of GetItemPosition.

#### Parameters

- pidl : PyIDL

 Description for pidl


---

<!-- page: PyIFolderView__GetSelectionMarkedItem_meth.html -->

## PyIFolderView.GetSelectionMarkedItem

 GetSelectionMarkedItem()

Description of GetSelectionMarkedItem.


---

<!-- page: PyIFolderView__GetSpacing_meth.html -->

## PyIFolderView.GetSpacing

 GetSpacing(pt)

Description of GetSpacing.

#### Parameters

- pt : (int, int)

 Coordinates of an item


---

<!-- page: PyIFolderView__ItemCount_meth.html -->

## PyIFolderView.ItemCount

 ItemCount(uFlags)

Description of ItemCount.

#### Parameters

- uFlags : int

 Description for uFlags


---

<!-- page: PyIFolderView__Item_meth.html -->

## PyIFolderView.Item

 Item(iItemIndex)

Description of Item.

#### Parameters

- iItemIndex : int

 Description for iItemIndex


---

<!-- page: PyIFolderView__Items_meth.html -->

## PyIFolderView.Items

 Items()

Description of Items.


---

<!-- page: PyIFolderView__SelectAndPositionItems_meth.html -->

## PyIFolderView.SelectAndPositionItems

 SelectAndPositionItems()

Description of SelectAndPositionItems.


---

<!-- page: PyIFolderView__SelectItem_meth.html -->

## PyIFolderView.SelectItem

 SelectItem(iItem, dwFlags)

Description of SelectItem.

#### Parameters

- iItem : int

 Description for iItem

- dwFlags : int

 Description for dwFlags


---

<!-- page: PyIFolderView__SetCurrentViewMode_meth.html -->

## PyIFolderView.SetCurrentViewMode

 SetCurrentViewMode(ViewMode)

Description of SetCurrentViewMode.

#### Parameters

- ViewMode : int

 Description for ViewMode


---

<!-- page: Source_Safe_Integration.html -->

---

## Source Safe Integration

 Note you will need to restart Pythonwin for this option to take effect.

 Before using the VSS integration, you must create a "mssccprj.scc" file in the directory, or a parent directory, of the files you wish to integrate. There are no limits on how many of these files exist. This is the same name and format as VB uses for VSS integration - a Windows INI file.

 This file must have a section [Python] with entry "Project=ProjectName". The project name is the name of the VSS project used to check the out the file. If the .scc file is in a parent directory, the correct relative VSS path is built - so if your file system matches your VSS structure, you only need a single .scc file in the VSS "root" directory.

For example, assuming you have the file c:\\src\\mssccprj.scc with the contents:
[Python]
Project=OurProject
-eof-
The file c:\\src\\source1.py will be checked out from project OurProject, c:\\src\\sub\\source2.py will be checked out from project OurProject\\sub, etc.


---

<!-- page: Source_code_folding_in_the_editor.html -->

---

## Source code folding in the editor

 Thanks to Scintilla (https://www.scintilla.org), Pythonwin supports source code folding. Folding is the ability to collapse sections of your source-code into a single line, making it easier to navigate around large files. Any Python statement which introduces a new block can be folded either by clicking on the indicator in the folding margin (if enabled via the View->Options->Editor dialog), by selecting one of the folding keystrokes (see Keyboard Bindings, or by using View->Folding menu.)

 All find/replace or 'goto linenumber' functions work correctly when code is folded - the code is simply unfolded if necessary before the relevant operation.

 You may configure Pythonwin so that all files have their top-levels folded when opened. Only the first level folds are collapsed using this function, so expanding the top-level fold reveals the entire class/method that was folded. Alternatively, you can use the Keypad-Multiply key to toggle the first level folds for the entire file at any time.


---

<!-- page: authorization__EditSecurity_meth.html -->

## authorization.EditSecurity

 EditSecurity(hwndOwner, psi)

Creates a security editor dialog

#### Parameters

- hwndOwner : PyHANDLE

 Handle to window that owns dialog, can be None

- psi : PyGSecurityInformation

 Class instance that implements the ISecurityInformation interface


---

<!-- page: classesandcmember.html -->

## Classes and class members


---

<!-- page: functions.html -->

## Functions


---

<!-- page: isapi_modules.html -->

## Modules

- isapi
- isapi.install
- isapi.isapicon
- isapi.simple
- isapi.threaded_extension


---

<!-- page: isapi_objects.html -->

## Objects

- EXTENSION_CONTROL_BLOCK
- HSE_VERSION_INFO
- HTTP_FILTER_AUTHENT
- HTTP_FILTER_CONTEXT
- HTTP_FILTER_LOG
- HTTP_FILTER_PREPROC_HEADERS
- HTTP_FILTER_RAW_DATA
- HTTP_FILTER_URL_MAP
- HTTP_FILTER_VERSION
- isapi.simple.SimpleExtension
- isapi.simple.SimpleFilter
- isapi.threaded_extension.ThreadPoolExtension


---

<!-- page: isapi_overview.html -->

## Overviews

- Introduction to Python ISAPI support


---

<!-- page: objectmodprops.html -->

## Object and Module Properties

- pythoncom.dcom
- pythoncom.frozen


---

<!-- page: overviews.html -->

### Overviews

- ASP and Python
- DirectSound examples
- Keyboard Bindings
- MTS and Python for NT
- Python, C++, and COM
- Recursive directory deletes and special files
- Source code folding in the editor
- Source Safe Integration
- Tabs and indentation in the editor
- win32com.shell and Windows Shell Links
- Windows NT Eventlog
- Windows NT Eventlog and Threading
- Windows NT Files -- Locking
- Windows NT Security -- Impersonation

#### Win32 API

- Directory permissions with GetNamedSecurityInfo
- Getting process info (with some COM thrown it!)
- Windows NT/2000 Networking with the win32net module

#### Python COM

- ADSI Python
- Active Directory
- Important notes about COM currency support changes
- win32com documentation index
- win32com readme

#### Pythonwin and win32ui

- Pythonwin Debugger documentation
- Pythonwin readme
- The Pythonwin environment

#### ISAPI filters and extensions

- Introduction to Python ISAPI support


---

<!-- page: structsnenum.html -->

## Structures and enumerations
