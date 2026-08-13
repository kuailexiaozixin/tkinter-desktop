# 模块 shell

> 来源：https://mhammond.github.io/pywin32/shell.html （及其成员页，已全部内联）

## Module shell

 A module wrapping Windows Shell functions and interfaces

#### Methods

- AssocCreate

 Creates a PyIQueryAssociations object

- AssocCreateForClasses

 Retrieves an object that implements an IQueryAssociations interface."}

- DragQueryFile

 Retrieves the file names of dropped files that have resulted from a successful drag-and-drop operation.

- DragQueryFileW

 Retrieves the file names of dropped files that have resulted from a successful drag-and-drop operation.

- DragQueryPoint

 Retrieves the position of the mouse pointer at the time a file was dropped during a drag-and-drop operation.

- IsUserAnAdmin

 Tests whether the current user is a member of the Administrator's group.

- SHCreateDataObject

 Creates a data object in a parent folder.

- SHCreateDefaultContextMenu

- SHCreateDefaultExtractIcon

 Creates a standard icon extractor, whose defaults can be further configured via the IDefaultExtractIconInit interface.

- SHCreateShellFolderView

 Creates a new instance of the default Shell folder view object.

- SHCreateShellItemArray

 Creates a Shell item array object.

- SHCreateShellItemArrayFromDataObject

 Creates a shell item array from an IDataObject interface

- SHCreateShellItemArrayFromIDLists

 Creates a shell item array from a number of item identifiers

- SHCreateShellItemArrayFromShellItem

- SHGetPathFromIDList

 Converts an PyIDL to a path.

- SHGetPathFromIDListW

 Converts an PyIDL to a unicode path.

- SHBrowseForFolder

 Displays a dialog box that enables the user to select a shell folder.

- SHGetFileInfo

 Retrieves information about an object in the file system, such as a file, a folder, a directory, or a drive root.

- SHGetFolderPath

 Retrieves the path of a folder.

- SHSetFolderPath

 Sets the location of a special folder

- SHGetFolderLocation

 Retrieves the PyIDL of a folder.

- SHGetNameFromIDList

 Retrieves the display name of an item from an ID list.

- SHGetSpecialFolderPath

 Retrieves the path of a special folder.

- SHGetSpecialFolderLocation

 Retrieves the PyIDL of a special folder.

- SHGetKnownFolderPath

 Retrieves the full path of a known folder identified by the folder's KNOWNFOLDERID.

- SHAddToRecentDocs

 Adds a document to the shell's list of recently used documents or clears all documents from the list. The user gains access to the list through the Start menu of the Windows taskbar.

- SHChangeNotify

 Notifies the system of an event that an application has performed. An application should use this function if it performs an action that may affect the shell.

- SHEmptyRecycleBin

 Empties the recycle bin on the specified drive.

- SHQueryRecycleBin

 Returns the number of items and total size of recycle bin

- SHGetDesktopFolder

 Retrieves the PyIShellFolder interface for the desktop folder, which is the root of the shell's namespace.

- SHUpdateImage

 Notifies the shell that an image in the system image list has changed.

- SHChangeNotify

 Notifies the system of an event that an application has performed.

- SHChangeNotifyRegister

 Registers a window that receives notifications from the file system or shell.

- SHChangeNotifyDeregister

 Unregisters the client's window process from receiving notification events

- SHCreateItemFromIDList

 Creates and initializes a Shell item object.

- SHCreateItemFromParsingName

 Creates and initializes a Shell item object from a parsing name.

- SHCreateItemFromRelativeName

 Creates and initializes a Shell item object from a relative parsing name.

- SHCreateItemInKnownFolder

 Creates a Shell item object for a single file that exists inside a known folder.

- SHCreateItemWithParent

 Create a Shell item, given a parent folder and a child item ID.

- SHGetIDListFromObject

 Retrieves the PIDL of an object.

- SHGetInstanceExplorer

 Allows components that run in a Web browser (Iexplore.exe) or a nondefault Windows Explorer (Explorer.exe) process to hold a reference to the process. The components can use the reference to prevent the process from closing prematurely.

- SHFileOperation

 Copies, moves, renames, or deletes a file system object.

- StringAsCIDA

 Given a CIDA as a raw string, return pidl_folder, [pidl_children, ...]

- CIDAAsString

 Given a (pidl, child_pidls) object, return a CIDA as a string

- StringAsPIDL

 Given a PIDL as a raw string, return a PIDL object (ie, a list of strings)

- AddressAsPIDL

 Given the address of a PIDL, return a PIDL object (ie, a list of strings)

- PIDLAsString

 Given a PIDL object, return the raw PIDL bytes as a string

- SHGetSettings

 Retrieves the current shell option settings.

- FILEGROUPDESCRIPTORAsString

 Creates a FILEGROUPDESCRIPTOR from a sequence of mapping objects, each with FILEDESCRIPTOR attributes

- StringAsFILEGROUPDESCRIPTOR

 Decodes a FILEGROUPDESCRIPTOR packed in a string

- ShellExecuteEx

 Performs an action on a file.

- SHGetViewStatePropertyBag

 Retrieves an interface for a folder's view state

- SHILCreateFromPath

 Returns the PIDL and attributes of a path

- SHCreateShellItem

 Creates an IShellItem interface from a PIDL

- SHOpenFolderAndSelectItems

 Displays a shell folder with items pre-selected

- SHCreateStreamOnFileEx

 Creates a PyIStream that reads and writes to a file

- SetCurrentProcessExplicitAppUserModelID

 Sets the taskbar identifier

- GetCurrentProcessExplicitAppUserModelID

 Retrieves the current taskbar identifier

- SHParseDisplayName

 Translates a display name into a shell item identifier


---

# shell 成员详细文档（共 58 项）


---

<!-- page: shell__AddressAsPIDL_meth.html -->

## shell.AddressAsPIDL

 PyIDL = AddressAsPIDL(address)

Given the address of a PIDL in memory, return a PIDL object (ie, a list of strings)

#### Parameters

- address : int

 The address of the PIDL


---

<!-- page: shell__AssocCreateForClasses_meth.html -->

## shell.AssocCreateForClasses

 PyIUnknown = AssocCreateForClasses()

Retrieves an object that implements an IQueryAssociations interface.


---

<!-- page: shell__AssocCreate_meth.html -->

## shell.AssocCreate

 PyIQueryAssociations = AssocCreate()

Creates a PyIQueryAssociations object


---

<!-- page: shell__CIDAAsString_meth.html -->

## shell.CIDAAsString

 string = CIDAAsString(pidl)

Given a (pidl, child_pidls) object, return a CIDA as a string

#### Parameters

- pidl : string

 The PIDL as a raw string.

#### Return Value

The result is a string with the CIDA bytes.


---

<!-- page: shell__DragQueryFileW_meth.html -->

## shell.DragQueryFileW

 int/string = DragQueryFileW(hglobal, index )

Retrieves the names (or count) of dropped files

#### Parameters

- hglobal : PyHANDLE

 The HGLOBAL object - generally obtained via the 'data_handle' property of a PySTGMEDIUM object.

- index : int

 The index to retrieve. If -1, the result if an integer representing the valid index values.


---

<!-- page: shell__DragQueryFile_meth.html -->

## shell.DragQueryFile

 int/string = DragQueryFile(hglobal, index )

Retrieves the names (or count) of dropped files

#### Parameters

- hglobal : PyHANDLE

 The HGLOBAL object - generally obtained via the 'data_handle' property of a PySTGMEDIUM object.

- index : int

 The index to retrieve. If -1, the result if an integer representing the valid index values.


---

<!-- page: shell__DragQueryPoint_meth.html -->

## shell.DragQueryPoint

 int, (int,int) = DragQueryPoint(hglobal)

Retrieves the position of the mouse pointer at the time a file was dropped during a drag-and-drop operation.

#### Parameters

- hglobal : PyHANDLE

 The HGLOBAL object - generally obtained the 'data_handle' property of a PySTGMEDIUM

#### Comments

 The window for which coordinates are returned is the window that received the WM_DROPFILES message

#### Return Value

The first item of the return tuple is True if the drop occurred in the client area of the window, or False if the drop did not occur in the client area of the window.


---

<!-- page: shell__FILEGROUPDESCRIPTORAsString_meth.html -->

## shell.FILEGROUPDESCRIPTORAsString

 string = FILEGROUPDESCRIPTORAsString(descriptors, make_unicode )

Creates a FILEGROUPDESCRIPTOR from a sequence of mapping objects, each with FILEDESCRIPTOR attributes

#### Parameters

- descriptors : [FILEDESCRIPTOR, ...]

 A sequence of FILEDESCRIPTOR objects. Each filedescriptor object must be a mapping/dictionary, with the following optional attributes: dwFlags, clsid, sizel, pointl, dwFileAttributes, ftCreationTime, ftLastAccessTime, ftLastWriteTime, nFileSize If these attributes do not exist, or are None, they will be ignored - hence you only need specify attributes you care about.
In general, you can omit dwFlags - it will be set correctly based on what other attributes exist.

- make_unicode=True : bool

 If true, a FILEDESCRIPTORW object is created


---

<!-- page: shell__GetCurrentProcessExplicitAppUserModelID_meth.html -->

## shell.GetCurrentProcessExplicitAppUserModelID

 str = GetCurrentProcessExplicitAppUserModelID()

Retrieves the current taskbar identifier

#### Comments

 Will only retrieve an identifier if set by the application, not a system-assigned default.


---

<!-- page: shell__IsUserAnAdmin_meth.html -->

## shell.IsUserAnAdmin

 bool = IsUserAnAdmin()

Tests whether the current user is a member of the Administrator's group.

#### Return Value

The result is true or false,


---

<!-- page: shell__PIDLAsString_meth.html -->

## shell.PIDLAsString

 string = PIDLAsString(pidl)

Given a PIDL object, return the raw PIDL bytes as a string

#### Parameters

- pidl : PyIDL

 The PIDL object (ie, a list of strings)


---

<!-- page: shell__SHAddToRecentDocs_meth.html -->

## shell.SHAddToRecentDocs

 SHAddToRecentDocs(Flags, data)

Adds a document to the shell's list of recently used documents or clears all documents from the list. The user gains access to the list through the Start menu of the Windows taskbar.

#### Parameters

- Flags : int

 Value from SHARD enum indicating how the item is identified.

- data : object

 Type of input is determined by the SHARD_* flag. Use None to clear recent items list.

| | Flags | Type of input
| |

---

 |

---

| | SHARD_PATHA | String containing a file path
| | SHARD_PATHW | String containing a file path
| | SHARD_PIDL | PyIDL, or a buffer containing a PIDL (see shell::PIDLAsString)
| | SHARD_APPIDINFO | Tuple of (PyIShellItem, str), where str is an AppID
| | SHARD_APPIDINFOIDLIST | Tuple of (PyIDL, str), where str is an AppID
| | SHARD_LINK | PyIShellLink
| | SHARD_APPIDINFOLINK | Tuple of (PyIShellLink, str) where str is an AppID
| | SHARD_SHELLITEM | PyIShellItem

#### Comments

 The entry is also added to the application's jump list.

 The underlying API function has no return value, and therefore no way to indicate failure.

#### Win32 API References

- Search for SHAddToRecentDocs at [msdn](https://learn.microsoft.com/en-ca/search/?terms=SHAddToRecentDocs), [google](https://www.google.com/search?q=SHAddToRecentDocs) or [google groups](https://groups.google.com/groups?q=SHAddToRecentDocs).


---

<!-- page: shell__SHBrowseForFolder_meth.html -->

## shell.SHBrowseForFolder

 (PyIDL, string displayName, iImage) = SHBrowseForFolder(hwndOwner, pidlRoot , title , flags , callback , callback_data )

Displays a dialog box that enables the user to select a shell folder.

#### Parameters

- hwndOwner=None : PyHANDLE

 Parent window for the dialog box, can be None

- pidlRoot=None : PyIDL

 PIDL identifying the place to start browsing. Desktop is used if not specified

- title=None : string

 Title to be displayed with the directory tree

- flags=0 : int

 Combination of shellcon.BIF_* flags

- callback=None : object

 A callable object to be used as the callback, or None

- callback_data=None : object

 An object passed to the callback function

#### Comments

 If you provide a callback function, it should take 4 args: hwnd, msg, lp, data. Data will be whatever you passed as callback_data, and the rest are integers. See the Microsoft documentation for SHBrowseForFolder, or the browse_for_folder.py shell sample for more information.

#### Return Value

The result is ALWAYS a tuple of 3 items. If the user cancels the dialog, all items are None. If the dialog is closed normally, the result is a tuple of (PIDL, DisplayName, iImageList)


---

<!-- page: shell__SHChangeNotifyDeregister_meth.html -->

## shell.SHChangeNotifyDeregister

 SHChangeNotifyDeregister(id)

Unregisters the client's window process from receiving notification events

#### Parameters

- id : int

 The registration identifier (ID) returned by shell::SHChangeNotifyRegister.


---

<!-- page: shell__SHChangeNotifyRegister_meth.html -->

## shell.SHChangeNotifyRegister

 int = SHChangeNotifyRegister(hwnd, sources , events , msg )

Registers a window that receives notifications from the file system or shell.

#### Parameters

- hwnd : PyHANDLE

 Handle to the window that receives the change or notification messages.

- sources : int

 One or more values that indicate the type of events for which to receive notifications.

- events : int

 Change notification events for which to receive notification.

- msg : int

 Message to be posted to the window procedure.


---

<!-- page: shell__SHChangeNotify_meth.html -->

## shell.SHChangeNotify

 SHChangeNotify(EventId, Flags, Item1, Item2)

Notifies the system of an event that an application has performed. An application should use this function if it performs an action that may affect the shell.

#### Parameters

- EventId : int

 Combination of shellcon.SHCNE_* constants

- Flags : int

 Combination of shellcon.SHCNF_* constants that specify type of last 2 parameters Only one of the type flags may be specified, combined with one of the SHCNF_FLUSH* flags

- Item1 : object

 Type is dependent on the event to be signalled

- Item2 : object

 Type is dependent on the event to be signalled


---

<!-- page: shell__SHCreateDataObject_meth.html -->

## shell.SHCreateDataObject

 PyIUnknown = SHCreateDataObject(parent, children , do_inner , iid )

#### Parameters

- parent : PIDL

- children : [PIDL, ...]

- do_inner : PyIDataObject

 The inner data object, or None bNoneOK */))

- iid=IID_IDataObject : PyIID

 The IID to query for


---

<!-- page: shell__SHCreateDefaultContextMenu_meth.html -->

## shell.SHCreateDefaultContextMenu

 PyIUnknown = SHCreateDefaultContextMenu(dcm, iid )

#### Parameters

- dcm : DEFAULTCONTEXTMENU

- iid=IID_IContextMenu : PyIID

 The IID to query for


---

<!-- page: shell__SHCreateDefaultExtractIcon_meth.html -->

## shell.SHCreateDefaultExtractIcon

 PyIDefaultExtractIconInit = SHCreateDefaultExtractIcon()

Creates a standard icon extractor, whose defaults can be further configured via the IDefaultExtractIconInit interface.


---

<!-- page: shell__SHCreateItemFromIDList_meth.html -->

## shell.SHCreateItemFromIDList

 PyIShellItem = SHCreateItemFromIDList(pidl, riid )

Creates and initializes a Shell item object from a PIDL. Can also create PyIShellItem2 objects.

#### Parameters

- pidl : PyIDL

 An absolute item identifier list

- riid=IID_IShellItem : PyIID

 The interface to create


---

<!-- page: shell__SHCreateItemFromParsingName_meth.html -->

## shell.SHCreateItemFromParsingName

 PyIShellItem = SHCreateItemFromParsingName(name, ctx , riid )

Creates and initializes a Shell item object from a parsing name.

#### Parameters

- name : str

 The display name of the item to create, eg a file path

- ctx : PyIBindCtx

 Bind context, can be None

- riid : PyIID

 The interface to create, IID_IShellItem or IID_IShellItem2


---

<!-- page: shell__SHCreateItemFromRelativeName_meth.html -->

## shell.SHCreateItemFromRelativeName

 PyIShellItem = SHCreateItemFromRelativeName(Parent, Name , ctx , riid )

Creates and initializes a Shell item object from a relative parsing name.

#### Parameters

- Parent : PyIShellItem

 Shell item interface on the parent folder

- Name : str

 Relative name of an item within the parent folder

- ctx : PyIBindCtx

 Bind context for parsing, can be None

- riid : PyIID

 The interface to return, IID_IShellItem or IID_IShellItem2


---

<!-- page: shell__SHCreateItemInKnownFolder_meth.html -->

## shell.SHCreateItemInKnownFolder

 PyIShellItem = SHCreateItemInKnownFolder(FolderId, Flags , Name , riid )

Creates a Shell item object for a single file that exists inside a known folder.

#### Parameters

- FolderId : PyIID

 The GUID of a known folder (shell.FOLDERID_*)

- Flags : int

 Combination of shellcon.KF_FLAG_* flags controlling how folder is handled

- Name : str

 Name of an item in the folder. Pass None to bind to the known folder itself.

- riid=IID_IShellItem : PyIID

 The interface to return, usually IID_IShellItem or IID_IShellItem2


---

<!-- page: shell__SHCreateItemWithParent_meth.html -->

## shell.SHCreateItemWithParent

 PyIShellItem = SHCreateItemWithParent(Parent, sfParent , child , riid )

Create a Shell item, given a parent folder and a child item ID.

#### Parameters

- Parent : PyIDL

 Absolute item id list of the parent folder. Pass None if the below shell folder is used.

- sfParent : PyIShellFolder

 Parent folder object. Can be None if parent id list is specified.

- child : PyIDL

 Relative item id list for an object in the parent folder

- riid=IID_IShellItem : PyIID

 The interface to return, usually IID_IShellItem or IID_IShellItem2


---

<!-- page: shell__SHCreateShellFolderView_meth.html -->

## shell.SHCreateShellFolderView

 PyIShellView = SHCreateShellFolderView(sf, viewOuter , callbacks )

Creates a new instance of the default Shell folder view object.

#### Parameters

- sf : PyIShellFolder

- viewOuter=None : PyIShellView

- callbacks=None : PyIShellFolderViewCB


---

<!-- page: shell__SHCreateShellItemArrayFromDataObject_meth.html -->

## shell.SHCreateShellItemArrayFromDataObject

 PyIShellItemArray = SHCreateShellItemArrayFromDataObject(do, iid )

Creates a shell item array from an IDataObject interface that contains a list of items (eg CF_HDROP)

#### Parameters

- do : PyIDataObject

 A data object that can be rendered as a list of items

- iid=IID_IShellItemArray : PyIID

 The interface to create


---

<!-- page: shell__SHCreateShellItemArrayFromIDLists_meth.html -->

## shell.SHCreateShellItemArrayFromIDLists

 PyIShellItemArray = SHCreateShellItemArrayFromIDLists(pidls)

Creates a shell item array from a number of item identifiers

#### Parameters

- pidls : [PyIDL, ...]

 A sequence of absolute IDLs.


---

<!-- page: shell__SHCreateShellItemArrayFromShellItem_meth.html -->

## shell.SHCreateShellItemArrayFromShellItem

 PyIShellItemArray = SHCreateShellItemArrayFromShellItem(si, riid )

Creates an item array containing a single item

#### Parameters

- si : PyIShellItem

 A shell item bNoneOK */))

- riid=IID_IShellItemArray : PyIID

 The interface to return


---

<!-- page: shell__SHCreateShellItemArray_meth.html -->

## shell.SHCreateShellItemArray

 PyIShellItemArray = SHCreateShellItemArray(parent, sf , children )

Creates a Shell item array object.

#### Parameters

- parent : PyIDL

 Absolute ID list of parent folder, or None if sf is specified

- sf : PyIShellFolder

 The Shell data source object that is the parent of the child items specified in children. If parent is specified, this parameter can be NULL. bNoneOK */))

- children : [PyIDL, ...]

 Sequence of relative IDLs for items in the parent folder


---

<!-- page: shell__SHCreateShellItem_meth.html -->

## shell.SHCreateShellItem

 PyIShellItem = SHCreateShellItem(pidlParent, sfParent , Child )

Creates an IShellItem interface from a PIDL

#### Parameters

- pidlParent : PyIDL

 PIDL of parent folder, can be None

- sfParent : PyIShellFolder

 IShellFolder interface of parent folder, can be None

- Child : PyIDL

 PIDL identifying desired item. Must be an absolute PIDL if parent is not specified.


---

<!-- page: shell__SHCreateStreamOnFileEx_meth.html -->

## shell.SHCreateStreamOnFileEx

 PyIStream = SHCreateStreamOnFileEx(File, Mode , Attributes , Create , Template )

Creates an IStream interface that reads and writes to a file

#### Parameters

- File : str

 Name of file to be connected to the stream

- Mode : int

 Combination of storagecon.STGM_* flags specifying the access mode

- Attributes : int

 Combination of win32con.FILE_ATTRIBUTE_* flags

- Create : bool

 Determines if function should fail when file exists (see MSDN docs for full explanation)

- Template=None : None

 Reserved, use only None

#### Comments

 Accepts keyword args.


---

<!-- page: shell__SHEmptyRecycleBin_meth.html -->

## shell.SHEmptyRecycleBin

 SHEmptyRecycleBin(hwnd, path, flags)

Empties the recycle bin on the specified drive.

#### Parameters

- hwnd : PyHANDLE

 Handle to parent window, can be None

- path : string

 A NULL-terminated string that contains the path of the root drive on which the recycle bin is located. This parameter can contain the address of a string formatted with the drive, folder, and subfolder names (c:\\windows\\system . . .). It can also contain an empty string or NULL. If this value is an empty string or NULL, all recycle bins on all drives will be emptied.

- flags : int

 One of the SHERB_* values.


---

<!-- page: shell__SHFileOperation_meth.html -->

## shell.SHFileOperation

 int, int = SHFileOperation(operation)

Copies, moves, renames, or deletes a file system object.

#### Parameters

- operation : SHFILEOPSTRUCT

 Defines the operation to perform.

#### Return Value

The result is a tuple containing int result of the function itself, and the result of the fAnyOperationsAborted member after the operation. If Flags contains FOF_WANTMAPPINGHANDLE, returned tuple will have a 3rd member containing a sequence of 2-tuples with the old and new file names of renamed files. This will only have any content if FOF_RENAMEONCOLLISION was specified, and some filename conflicts actually occurred.


---

<!-- page: shell__SHGetDesktopFolder_meth.html -->

## shell.SHGetDesktopFolder

 PyIShellFolder = SHGetDesktopFolder()

Retrieves the PyIShellFolder interface for the desktop folder, which is the root of the shell's namespace.


---

<!-- page: shell__SHGetFileInfo_meth.html -->

## shell.SHGetFileInfo

 int, SHFILEINFO = SHGetFileInfo(name, dwFileAttributes , uFlags , infoAttrs )

Retrieves information about an object in the file system, such as a file, a folder, a directory, or a drive root.

#### Parameters

- name : string/PyIDL

 The path and file name. Both absolute and relative paths are valid.
If the uFlags parameter includes the SHGFI_PIDL flag, this parameter must be a valid PyIDL object that uniquely identifies the file within the shell's namespace. The PIDL must be a fully qualified PIDL. Relative PIDLs are not allowed.
If the uFlags parameter includes the SHGFI_USEFILEATTRIBUTES flag, this parameter does not have to be a valid file name. The function will proceed as if the file exists with the specified name and with the file attributes passed in the dwFileAttributes parameter. This allows you to obtain information about a file type by passing just the extension for pszPath and passing FILE_ATTRIBUTE_NORMAL in dwFileAttributes.
This string can use either short (the 8.3 form) or long file names.

- dwFileAttributes : int

 Combination of one or more file attribute flags (FILE_ATTRIBUTE_ values). If uFlags does not include the SHGFI_USEFILEATTRIBUTES flag, this parameter is ignored.

- uFlags : int

 Combination of shellcon.SHGFI_* flags that specify the file information to retrieve. See MSDN for details

- infoAttrs=0 : int

 Flags copied to the SHFILEINFO.dwAttributes member - useful when flags contains SHGFI_ATTR_SPECIFIED


---

<!-- page: shell__SHGetFolderLocation_meth.html -->

## shell.SHGetFolderLocation

 PyIDL = SHGetFolderLocation(hwndOwner, nFolder , hToken , reserved )

Retrieves the PIDL of a folder.

#### Parameters

- hwndOwner : int

 Window in which to display any neccessary dialogs

- nFolder : int

 One of the CSIDL_* constants specifying the path.

- hToken=None : PyHANDLE

 An access token that can be used to represent a particular user, or None

- reserved=0 : int

 Must be 0


---

<!-- page: shell__SHGetFolderPath_meth.html -->

## shell.SHGetFolderPath

 string = SHGetFolderPath(hwndOwner, nFolder , handle , flags )

Retrieves the path of a folder.

#### Parameters

- hwndOwner : PyHANDLE

 Parent window, can be None (or 0)

- nFolder : int

 One of the CSIDL_* constants specifying the path.

- handle : PyHANDLE

 An access token that can be used to represent a particular user, or None

- flags : int

 Controls which path is returned. May be SHGFP_TYPE_CURRENT or SHGFP_TYPE_DEFAULT


---

<!-- page: shell__SHGetIDListFromObject_meth.html -->

## shell.SHGetIDListFromObject

 PyIDL = SHGetIDListFromObject(unk)

Retrieves the PIDL of an object.

#### Parameters

- unk : PyIUnknown


---

<!-- page: shell__SHGetInstanceExplorer_meth.html -->

## shell.SHGetInstanceExplorer

 PyIUnknown = SHGetInstanceExplorer()

Allows components that run in a Web browser (Iexplore.exe) or a nondefault Windows Explorer (Explorer.exe) process to hold a reference to the process. The components can use the reference to prevent the process from closing prematurely.

#### Comments

 SHGetInstanceExplorer succeeds only if it is called from within an Explorer.exe or Iexplorer.exe process. It is typically used by components that run in the context of the Web browser (Iexplore.exe). However, it is also useful when Explorer.exe has been configured to run all folders in a second process. SHGetInstanceExplorer fails if the component is running in the default Explorer.exe process. There is no need to hold a reference to this process, as it is shut down only when the user logs out.


---

<!-- page: shell__SHGetKnownFolderPath_meth.html -->

## shell.SHGetKnownFolderPath

 string = SHGetKnownFolderPath(fid, flags , token )

Retrieves the full path of a known folder identified by the folder's KNOWNFOLDERID.

#### Parameters

- fid : IID

 One of the KNOWNFOLDERID constants.

- flags=0 : int

 Flags that specify special retrieval options. This value can be 0; otherwise, one or more of the KNOWN_FOLDER_FLAG values.

- token=None : PyHANDLE

 An access token that represents a particular user. If this parameter is NULL, which is the most common usage, the function requests the known folder for the current user.


---

<!-- page: shell__SHGetNameFromIDList_meth.html -->

## shell.SHGetNameFromIDList

 str = SHGetNameFromIDList(pidl, flags )

Retrieves the display name of an item from an ID list.

#### Parameters

- pidl : PyIDL

 Absolute ID list of the item

- flags : int

 Type of name to return, shellcon.SIGDN_*


---

<!-- page: shell__SHGetPathFromIDListW_meth.html -->

## shell.SHGetPathFromIDListW

 string = SHGetPathFromIDListW(idl)

Converts an IDLIST to a path.

#### Parameters

- idl : PyIDL

 The ITEMIDLIST


---

<!-- page: shell__SHGetPathFromIDList_meth.html -->

## shell.SHGetPathFromIDList

 string = SHGetPathFromIDList(idl)

Converts an IDLIST to a path.

#### Parameters

- idl : PyIDL

 The ITEMIDLIST


---

<!-- page: shell__SHGetSettings_meth.html -->

## shell.SHGetSettings

 dict = SHGetSettings(mask)

Retrieves the current shell option settings.

#### Parameters

- mask=-1 : int

 The values being requested - one of the shellcon.SSF_* constants

#### Return Value

The result is a dictionary, the contents of which depend on the mask param. Key names are the same as the SHELLFLAGSTATE structure members - 'fShowExtensions', 'fNoConfirmRecycle', etc


---

<!-- page: shell__SHGetSpecialFolderLocation_meth.html -->

## shell.SHGetSpecialFolderLocation

 PyIDL = SHGetSpecialFolderLocation(hwndOwner, nFolder )

Retrieves the PIDL of a special folder.

#### Parameters

- hwndOwner : PyHANDLE

 Parent window, can be None (or 0)

- nFolder : int

 One of the CSIDL_* constants specifying the path.


---

<!-- page: shell__SHGetSpecialFolderPath_meth.html -->

## shell.SHGetSpecialFolderPath

 string = SHGetSpecialFolderPath(hwndOwner, nFolder , bCreate )

Retrieves the path of a special folder.

#### Parameters

- hwndOwner : PyHANDLE

 Parent window, can be None (or 0)

- nFolder : int

 One of the CSIDL_* constants specifying the path.

- bCreate=0 : int

 Should the path be created.


---

<!-- page: shell__SHGetViewStatePropertyBag_meth.html -->

## shell.SHGetViewStatePropertyBag

 PyIPropertyBag = SHGetViewStatePropertyBag(pidl, BagName , Flags , riid )

Retrieves an interface for the view state of a folder

#### Parameters

- pidl : PyIDL

 An item id list that identifies the folder

- BagName : string

 Name of the property bag to retrieve

- Flags : int

 Combination of SHGVSPB_* flags

- riid : PyIID

 The interface to return, usually IID_IPropertyBag

#### Comments

 This function will also return IPropertyBag2, but we don't have a python implementation of this interface yet


---

<!-- page: shell__SHILCreateFromPath_meth.html -->

## shell.SHILCreateFromPath

 (PyIDL, int) = SHILCreateFromPath(Path, Flags )

Retrieves the PIDL and attributes for a path

#### Parameters

- Path : string

 The path whose PIDL will be returned

- Flags : int

 A combination of SFGAO_* constants as used with GetAttributesOf

#### Return Value

Returns the PIDL for the given path and any requested attributes


---

<!-- page: shell__SHOpenFolderAndSelectItems_meth.html -->

## shell.SHOpenFolderAndSelectItems

 SHOpenFolderAndSelectItems(Folder, Items, Flags)

Displays a shell folder with items pre-selected

#### Parameters

- Folder : PyIDL

 An absolute item id list identifying a shell folder

- Items : (PyIDL,...)

 A sequence of relative item ids identifying items in the folder

- Flags=0 : int

 Combination of OFASI_* flags (not used on XP)


---

<!-- page: shell__SHParseDisplayName_meth.html -->

## shell.SHParseDisplayName

 (PyIDL, int) = SHParseDisplayName(Name, Attributes , BindCtx )

Translates a display name into a shell item identifier

#### Parameters

- Name : str

 Display name of a shell item, such as a file path

- Attributes : int

 Bitmask of shell attributes to retrieve, combination of shellcon.SFGAO_*

- BindCtx=None : PyIBindCtx

 Bind context, can be None

#### Comments

 Accepts keyword args

#### Return Value

Returns the item id list and any requested attribute flags


---

<!-- page: shell__SHQueryRecycleBin_meth.html -->

## shell.SHQueryRecycleBin

 long,long = SHQueryRecycleBin(RootPath)

Retrieves the total size and number of items in the Recycle Bin for a specified drive

#### Parameters

- RootPath=None : string

 A path containing the drive whose recycle bin will be queried, or None for all drives


---

<!-- page: shell__SHSetFolderPath_meth.html -->

## shell.SHSetFolderPath

 SHSetFolderPath(csidl, Path, hToken)

Sets the location of one of the special folders

#### Parameters

- csidl : int

 One of the shellcon.CSIDL_* values

- Path : string

 The full path to be set

- hToken=None : PyHANDLE

 Handle to an access token, can be None


---

<!-- page: shell__SHUpdateImage_meth.html -->

## shell.SHUpdateImage

 SHUpdateImage(HashItem, Index, Flags, ImageIndex)

Notifies the shell that an image in the system image list has changed.

#### Parameters

- HashItem : string

 Full path of file containing the icon as returned by PyIExtractIcon::GetIconLocation

- Index : int

 Index of the icon in the above file

- Flags : int

 GIL_NOTFILENAME or GIL_SIMULATEDOC

- ImageIndex : int

 Index of the icon in the system image list


---

<!-- page: shell__SetCurrentProcessExplicitAppUserModelID_meth.html -->

## shell.SetCurrentProcessExplicitAppUserModelID

 SetCurrentProcessExplicitAppUserModelID(AppID)

Sets the taskbar identifier

#### Parameters

- AppID : str

 The Application User Model ID used to group taskbar buttons

#### Comments

 Should be used early in process startup before creating any windows


---

<!-- page: shell__ShellExecuteEx_meth.html -->

## shell.ShellExecuteEx

 dict = ShellExecuteEx(fMask, hwnd , lpVerb , lpFile , lpParameters , lpDirectory , nShow , lpIDList , obClass , hkeyClass , dwHotKey , hMonitor )

Performs an operation on a file.

#### Parameters

- fMask=0 : int

 The default mask for the structure. Other masks may be added based on what parameters are supplied.

- hwnd=0 : PyHANDLE

- lpVerb : string

- lpFile : string

- lpParameters : string

- lpDirectory : string

- nShow=0 : int

- lpIDList : PyIDL

- obClass : string

- hkeyClass : int

- dwHotKey : int

- hMonitor : PyHANDLE

#### Return Value

The result is a dictionary based on documented result values in the structure. Currently this is "hInstApp" and "hProcess"


---

<!-- page: shell__StringAsCIDA_meth.html -->

## shell.StringAsCIDA

 PyIDL, list = StringAsCIDA(pidl)

Given a CIDA as a raw string, return the folder PIDL and list of children

#### Parameters

- pidl : string

 The PIDL as a raw string.

#### Return Value

The result is the PIDL of the folder, and a list of child PIDLs.


---

<!-- page: shell__StringAsFILEGROUPDESCRIPTOR_meth.html -->

## shell.StringAsFILEGROUPDESCRIPTOR

 [dict, ...] = StringAsFILEGROUPDESCRIPTOR(buf, make_unicode )

Decodes a FILEGROUPDESCRIPTOR packed in a string

#### Parameters

- buf : buffer

 A string packed as either FILEGROUPDESCRIPTORW or FILEGROUPDESCRIPTORW

- make_unicode=-1 : bool

 Should this be treated as a FILEDESCRIPTORW? If -1 the size of the buffer will be used to make that determination. Thus, if the buffer is not the exact size of a correct FILEDESCRIPTORW or FILEDESCRIPTORA, you will need to specify this parameter.


---

<!-- page: shell__StringAsPIDL_meth.html -->

## shell.StringAsPIDL

 PyIDL = StringAsPIDL(pidl)

Given a PIDL as a raw string, return a PIDL object (ie, a list of strings)

#### Parameters

- pidl : string

 The PIDL as a raw string.
