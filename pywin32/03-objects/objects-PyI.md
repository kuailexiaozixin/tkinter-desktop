# pywin32 对象文档 · 分卷 PyI

> 共 238 个对象，来源 https://mhammond.github.io/pywin32/<Object>.html


---

<!-- object: PyIADesktopP2 -->


<!-- page: PyIADesktopP2.html -->

---

## PyIADesktopP2 Object

 An interface to the ActiveDesktop

#### Methods

- UpdateAllDesktopSubscriptions

 Updates webpage subscriptions on the desktop


<!-- page: PyIADesktopP2__UpdateAllDesktopSubscriptions_meth.html -->

## PyIADesktopP2.UpdateAllDesktopSubscriptions

 UpdateAllDesktopSubscriptions()

Updates webpage subscriptions on the desktop


---

<!-- object: PyIADs -->


<!-- page: PyIADs.html -->

---

## PyIADs Object

 An object representing the IADs interface. In most cases you can achieve the same result via IDispatch - however, this interface allows you get get and set properties without the IDispatch overhead.

#### Methods

- GetInfo

 Description of GetInfo

- SetInfo

 Description of SetInfo

- Get

 Description of Get

- Put

 Description of Put

- get

 Synonym for Get

- put

 Synonym for Put

#### Properties

- PyUnicode ADsPath

- PyUnicode AdsPath
 Synonym for ADsPath

- PyUnicode Class

- PyUnicode GUID
 Like the IADs method, this returns a string rather than a GUID object.

- PyUnicode Name

- PyUnicode Parent

- PyUnicode Schema


<!-- page: PyIADs__GetInfo_meth.html -->

## PyIADs.GetInfo

 GetInfo()

Description of GetInfo.


<!-- page: PyIADs__Get_meth.html -->

## PyIADs.Get

 object = Get(prop)

Description of Get.

#### Parameters

- prop : PyUnicode

 The name of the property to fetch

#### Return Value

The result is a Python object converted from a COM variant. It may be an array, or any types supported by COM variant.


<!-- page: PyIADs__Put_meth.html -->

## PyIADs.Put

 Put(property, val)

Description of Put.

#### Parameters

- property : PyUnicode

 The property name to set

- val : object

 The value to set.


<!-- page: PyIADs__SetInfo_meth.html -->

## PyIADs.SetInfo

 SetInfo()

Description of SetInfo.


---

<!-- object: PyIADsContainer -->


<!-- page: PyIADsContainer.html -->

---

## PyIADsContainer Object

 A COM interface to ADSI's IADsContainer interface.
Derived from PyIUnknown

#### Methods

- GetObject

- get_Count

- get_Filter

- put_Filter

- get_Hints

- put_Hints


<!-- page: PyIADsContainer__GetObject_meth.html -->

## PyIADsContainer.GetObject

 PyIDispatch = GetObject(class, relativeName )

#### Parameters

- class : string

 Specifies the name of the object class as known in the underlying directory and identical to the one retrieved through the get_Class property method. If the class name is None, the provider returns the first item found in the container.

- relativeName : string

 Specifies the name of the object as known in the underlying directory and identical to the one retrieved through the get_Name property method.


<!-- page: PyIADsContainer__get_Count_meth.html -->

## PyIADsContainer.get_Count

 int = get_Count()


<!-- page: PyIADsContainer__get_Filter_meth.html -->

## PyIADsContainer.get_Filter

 object = get_Filter()


<!-- page: PyIADsContainer__get_Hints_meth.html -->

## PyIADsContainer.get_Hints

 object = get_Hints()


<!-- page: PyIADsContainer__put_Filter_meth.html -->

## PyIADsContainer.put_Filter

 put_Filter(val)

#### Parameters

- val : object


<!-- page: PyIADsContainer__put_Hints_meth.html -->

## PyIADsContainer.put_Hints

 put_Hints(val)

#### Parameters

- val : object


---

<!-- object: PyIADsUser -->


<!-- page: PyIADsUser.html -->

---

## PyIADsUser Object

 A COM interface to ADSI's IADsUser interface.
Derived from PyIDispatch

#### Methods

- get_AccountDisabled

- put_AccountDisabled

- get_AccountExpirationDate

- put_AccountExpirationDate

- get_BadLoginAddress

- get_BadLoginCount

- get_Department

- put_Department

- get_Description

- put_Description

- get_Division

- put_Division

- get_EmailAddress

- put_EmailAddress

- get_EmployeeID

- put_EmployeeID

- get_FirstName

- put_FirstName

- get_FullName

- put_FullName

- get_HomeDirectory

- put_HomeDirectory

- get_HomePage

- put_HomePage

- get_LoginScript

- put_LoginScript

- SetPassword

- ChangePassword


<!-- page: PyIADsUser__ChangePassword_meth.html -->

## PyIADsUser.ChangePassword

 ChangePassword(oldval, newval)

#### Parameters

- oldval : unicode

- newval : unicode


<!-- page: PyIADsUser__SetPassword_meth.html -->

## PyIADsUser.SetPassword

 SetPassword(val)

#### Parameters

- val : unicode


<!-- page: PyIADsUser__get_AccountDisabled_meth.html -->

## PyIADsUser.get_AccountDisabled

 int = get_AccountDisabled()


<!-- page: PyIADsUser__get_AccountExpirationDate_meth.html -->

## PyIADsUser.get_AccountExpirationDate

 int = get_AccountExpirationDate()


<!-- page: PyIADsUser__get_BadLoginAddress_meth.html -->

## PyIADsUser.get_BadLoginAddress

 unicode = get_BadLoginAddress()


<!-- page: PyIADsUser__get_BadLoginCount_meth.html -->

## PyIADsUser.get_BadLoginCount

 int = get_BadLoginCount()


<!-- page: PyIADsUser__get_Department_meth.html -->

## PyIADsUser.get_Department

 unicode = get_Department()


<!-- page: PyIADsUser__get_Description_meth.html -->

## PyIADsUser.get_Description

 unicode = get_Description()


<!-- page: PyIADsUser__get_Division_meth.html -->

## PyIADsUser.get_Division

 unicode = get_Division()


<!-- page: PyIADsUser__get_EmailAddress_meth.html -->

## PyIADsUser.get_EmailAddress

 unicode = get_EmailAddress()


<!-- page: PyIADsUser__get_EmployeeID_meth.html -->

## PyIADsUser.get_EmployeeID

 unicode = get_EmployeeID()


<!-- page: PyIADsUser__get_FirstName_meth.html -->

## PyIADsUser.get_FirstName

 unicode = get_FirstName()


<!-- page: PyIADsUser__get_FullName_meth.html -->

## PyIADsUser.get_FullName

 unicode = get_FullName()


<!-- page: PyIADsUser__get_HomeDirectory_meth.html -->

## PyIADsUser.get_HomeDirectory

 unicode = get_HomeDirectory()


<!-- page: PyIADsUser__get_HomePage_meth.html -->

## PyIADsUser.get_HomePage

 unicode = get_HomePage()


<!-- page: PyIADsUser__get_LoginScript_meth.html -->

## PyIADsUser.get_LoginScript

 unicode = get_LoginScript()


<!-- page: PyIADsUser__put_AccountDisabled_meth.html -->

## PyIADsUser.put_AccountDisabled

 put_AccountDisabled(val)

#### Parameters

- val : int


<!-- page: PyIADsUser__put_AccountExpirationDate_meth.html -->

## PyIADsUser.put_AccountExpirationDate

 put_AccountExpirationDate(val)

#### Parameters

- val : PyDateTime


<!-- page: PyIADsUser__put_Department_meth.html -->

## PyIADsUser.put_Department

 put_Department(val)

#### Parameters

- val : unicode


<!-- page: PyIADsUser__put_Description_meth.html -->

## PyIADsUser.put_Description

 put_Description(val)

#### Parameters

- val : unicode


<!-- page: PyIADsUser__put_Division_meth.html -->

## PyIADsUser.put_Division

 put_Division(val)

#### Parameters

- val : unicode


<!-- page: PyIADsUser__put_EmailAddress_meth.html -->

## PyIADsUser.put_EmailAddress

 put_EmailAddress(val)

#### Parameters

- val : unicode


<!-- page: PyIADsUser__put_EmployeeID_meth.html -->

## PyIADsUser.put_EmployeeID

 put_EmployeeID(val)

#### Parameters

- val : unicode


<!-- page: PyIADsUser__put_FirstName_meth.html -->

## PyIADsUser.put_FirstName

 put_FirstName(val)

#### Parameters

- val : unicode


<!-- page: PyIADsUser__put_FullName_meth.html -->

## PyIADsUser.put_FullName

 put_FullName(val)

#### Parameters

- val : unicode


<!-- page: PyIADsUser__put_HomeDirectory_meth.html -->

## PyIADsUser.put_HomeDirectory

 put_HomeDirectory(val)

#### Parameters

- val : unicode


<!-- page: PyIADsUser__put_HomePage_meth.html -->

## PyIADsUser.put_HomePage

 put_HomePage(val)

#### Parameters

- val : unicode


<!-- page: PyIADsUser__put_LoginScript_meth.html -->

## PyIADsUser.put_LoginScript

 put_LoginScript(val)

#### Parameters

- val : unicode


---

<!-- object: PyIActiveDesktop -->


<!-- page: PyIActiveDesktop.html -->

---

## PyIActiveDesktop Object

 An interface to the ActiveDesktop

#### Methods

- ApplyChanges

 Applies changes to ActiveDesktop settings and persists them to the registry.

- GetWallpaper

 Returns the current wallpaper

- SetWallpaper

 Sets the desktop wallpaper

- GetWallpaperOptions

 Returns wallpaper style

- SetWallpaperOptions

 Sets wallpaper style

- GetPattern

 Returns the wallpaper pattern

- SetPattern

 Sets the wallpaper pattern

- GetDesktopItemOptions

 Returns options for Active Desktop.

- SetDesktopItemOptions

 Sets Active Desktop options

- AddDesktopItem

 Creates a new item to display on the desktop

- AddDesktopItemWithUI

 Adds a desktop item, allowing user interaction

- ModifyDesktopItem

 Changes parameters for a desktop item

- RemoveDesktopItem

 Removes an item from the Active Desktop

- GetDesktopItemCount

 Returns number of defined desktop items.

- GetDesktopItem

 Returns desktop item parameters by index

- GetDesktopItemByID

 Returns desktop item parameters by Id

- GenerateDesktopItemHtml

 Creates an HTML page for the desktop item

- AddUrl

 Adds a web page to desktop, allowing user interaction

- GetDesktopItemBySource

 Returns desktop item parameters by URL


<!-- page: PyIActiveDesktop__AddDesktopItemWithUI_meth.html -->

## PyIActiveDesktop.AddDesktopItemWithUI

 AddDesktopItemWithUI(hwnd, comp, Flags)

Adds a desktop item, allowing user interaction

#### Parameters

- hwnd : PyHANDLE

 Handle to parent window

- comp : dict

 COMPONENT dictionary

- Flags : int

 One of shellcon.DTI_ADDUI_* flags


<!-- page: PyIActiveDesktop__AddDesktopItem_meth.html -->

## PyIActiveDesktop.AddDesktopItem

 AddDesktopItem(comp, Reserved)

Creates a new item to display on the desktop

#### Parameters

- comp : dict

 COMPONENT dictionary

- Reserved=0 : int

 Use 0 if passed in


<!-- page: PyIActiveDesktop__AddUrl_meth.html -->

## PyIActiveDesktop.AddUrl

 AddUrl(hwnd, Source, comp, Flags)

Adds a web page to desktop, allowing user interaction

#### Parameters

- hwnd : PyHANDLE

 Parent windows for any user interactive

- Source : PyUNICODE

 Source URL

- comp : dict

 COMPONENT dictionary

- Flags : int

 ADDURL_SILENT, or 0


<!-- page: PyIActiveDesktop__ApplyChanges_meth.html -->

## PyIActiveDesktop.ApplyChanges

 ApplyChanges(Flags)

Applies changes to ActiveDesktop settings and persists them to the registry.

#### Parameters

- Flags : int

 Combination of shellcon.AD_APPLY_* flags


<!-- page: PyIActiveDesktop__GenerateDesktopItemHtml_meth.html -->

## PyIActiveDesktop.GenerateDesktopItemHtml

 GenerateDesktopItemHtml(FileName, comp, Reserved)

Creates an HTML page for the desktop item

#### Parameters

- FileName : PyUNICODE

 Name of file to be created

- comp : dict

 COMPONENT dictionary specifying the desktop item

- Reserved=0 : int

 Use 0 if passed in


<!-- page: PyIActiveDesktop__GetDesktopItemByID_meth.html -->

## PyIActiveDesktop.GetDesktopItemByID

 dict = GetDesktopItemByID(ID, reserved )

Returns desktop item parameters by Id

#### Parameters

- ID : int

 The Id of the desktop item

- reserved=0 : int

 Use 0 if passed in

#### Return Value

Returns a COMPONENT dictionary


<!-- page: PyIActiveDesktop__GetDesktopItemBySource_meth.html -->

## PyIActiveDesktop.GetDesktopItemBySource

 dict = GetDesktopItemBySource(Source, Reserved )

Returns desktop item parameters by URL

#### Parameters

- Source : PyUNICODE

 The URL address of the item to retrieve

- Reserved=0 : int

 Use 0 if passed in

#### Return Value

Returns a COMPONENT dictionary


<!-- page: PyIActiveDesktop__GetDesktopItemCount_meth.html -->

## PyIActiveDesktop.GetDesktopItemCount

 GetDesktopItemCount()

Returns number of defined desktop items.


<!-- page: PyIActiveDesktop__GetDesktopItemOptions_meth.html -->

## PyIActiveDesktop.GetDesktopItemOptions

 dict = GetDesktopItemOptions()

Returns options for Active Desktop.

#### Return Value

Returns a COMPONENTSOPT dictionary


<!-- page: PyIActiveDesktop__GetDesktopItem_meth.html -->

## PyIActiveDesktop.GetDesktopItem

 dict = GetDesktopItem(Component, Reserved )

Returns desktop item parameters by index

#### Parameters

- Component : int

 The zero-based index of the component to get

- Reserved=0 : int

 Use 0 if passed in

#### Return Value

Returns a COMPONENT dictionary describing the item


<!-- page: PyIActiveDesktop__GetPattern_meth.html -->

## PyIActiveDesktop.GetPattern

 GetPattern(cchPattern, Reserved)

Returns the wallpaper pattern

#### Parameters

- cchPattern=1024 : int

 Number of characters to allocate for buffer

- Reserved=0 : int

 Use 0 if passed in

#### Return Value

Returns a unicode string containing decimal values representing the pattern


<!-- page: PyIActiveDesktop__GetWallpaperOptions_meth.html -->

## PyIActiveDesktop.GetWallpaperOptions

 int = GetWallpaperOptions(Reserved)

Returns wallpaper style

#### Parameters

- Reserved=0 : int

 Use 0 if passed in

#### Return Value

Returns one of the WPSTYLE_* values


<!-- page: PyIActiveDesktop__GetWallpaper_meth.html -->

## PyIActiveDesktop.GetWallpaper

 PyUNICODE = GetWallpaper(cchWallpaper, Reserved )

Returns the current wallpaper

#### Parameters

- cchWallpaper=MAX_PATH : int

 Number of characters to allocate for buffer

- Reserved=0 : int

 Use 0 if passed in


<!-- page: PyIActiveDesktop__ModifyDesktopItem_meth.html -->

## PyIActiveDesktop.ModifyDesktopItem

 ModifyDesktopItem(comp, Flags)

Changes parameters for a desktop item

#### Parameters

- comp : dict

 COMPONENT dictionary

- Flags : int

 Combination of shellcon.COMP_ELEM_* flags


<!-- page: PyIActiveDesktop__RemoveDesktopItem_meth.html -->

## PyIActiveDesktop.RemoveDesktopItem

 RemoveDesktopItem(comp, Reserved)

Removes an item from the Active Desktop

#### Parameters

- comp : dict

 COMPONENT dictionary specifying which component to remove

- Reserved=0 : int

 Use 0 if passed in


<!-- page: PyIActiveDesktop__SetDesktopItemOptions_meth.html -->

## PyIActiveDesktop.SetDesktopItemOptions

 SetDesktopItemOptions(comp, Reserved)

Sets Active Desktop options

#### Parameters

- comp : dict

 COMPONENTSOPT dictionary

- Reserved=0 : int

 Use 0 if passed in


<!-- page: PyIActiveDesktop__SetPattern_meth.html -->

## PyIActiveDesktop.SetPattern

 SetPattern(Pattern, Reserved)

Sets the wallpaper pattern

#### Parameters

- Pattern : PyUNICODE

 String of decimal numbers representing a picture

- Reserved=0 : int

 Use 0 if passed in


<!-- page: PyIActiveDesktop__SetWallpaperOptions_meth.html -->

## PyIActiveDesktop.SetWallpaperOptions

 SetWallpaperOptions(Style, Reserved)

Sets wallpaper style

#### Parameters

- Style : int

 The wallpaper style, one of the WPSTYLE_* constants

- Reserved=0 : int

 Reserved, use 0 if passed in


<!-- page: PyIActiveDesktop__SetWallpaper_meth.html -->

## PyIActiveDesktop.SetWallpaper

 SetWallpaper(Wallpaper, Reserved)

Sets the desktop wallpaper

#### Parameters

- Wallpaper : PyUNICODE

 File to be used as new wallpaper

- Reserved=0 : int

 Reserved, use 0 if passed in


---

<!-- object: PyIActiveDesktopP -->


<!-- page: PyIActiveDesktopP.html -->

---

## PyIActiveDesktopP Object

 An interface to the ActiveDesktop

#### Methods

- SetSafeMode

 Changes Active Desktop to safe mode


<!-- page: PyIActiveDesktopP__SetSafeMode_meth.html -->

## PyIActiveDesktopP.SetSafeMode

 SetSafeMode(Flags)

Changes Active Desktop to safe mode

#### Parameters

- Flags : int

 One of shellcon.SSM_* flags


---

<!-- object: PyIActiveScriptDebug -->


<!-- page: PyIActiveScriptDebug.html -->

---

## PyIActiveScriptDebug Object

 Description of the interface

#### Methods

- GetScriptTextAttributes

 Description of GetScriptTextAttributes

- GetScriptletTextAttributes

 Description of GetScriptletTextAttributes

- EnumCodeContextsOfPosition

 Description of EnumCodeContextsOfPosition


<!-- page: PyIActiveScriptDebug__EnumCodeContextsOfPosition_meth.html -->

## PyIActiveScriptDebug.EnumCodeContextsOfPosition

 EnumCodeContextsOfPosition(dwSourceContext, uCharacterOffset, uNumChars)

Description of EnumCodeContextsOfPosition.

#### Parameters

- dwSourceContext : int

 Description for dwSourceContext

- uCharacterOffset : int

 Description for uCharacterOffset

- uNumChars : int

 Description for uNumChars


<!-- page: PyIActiveScriptDebug__GetScriptTextAttributes_meth.html -->

## PyIActiveScriptDebug.GetScriptTextAttributes

 (int,...) = GetScriptTextAttributes(pstrCode, pstrDelimiter , dwFlags )

Returns the text attributes for an arbitrary block of script text.

#### Parameters

- pstrCode : string

 The script block text.

- pstrDelimiter : string

 See PyIActiveScriptParse::ParseScriptText for a description of this argument.

- dwFlags : int

 See PyIActiveScriptParse::ParseScriptText for a description of this argument.

#### Comments

 Smart hosts use this call to delegate GetText calls made on their axscript::PyIDebugDocumentText


<!-- page: PyIActiveScriptDebug__GetScriptletTextAttributes_meth.html -->

## PyIActiveScriptDebug.GetScriptletTextAttributes

 GetScriptletTextAttributes(pstrCode, pstrDelimiter, dwFlags)

Description of GetScriptletTextAttributes.

#### Parameters

- pstrCode : string

 The script block text.

- pstrDelimiter : string

 See PyIActiveScriptParse::ParseScriptText for a description of this argument.

- dwFlags : int

 See PyIActiveScriptParse::ParseScriptText for a description of this argument.


---

<!-- object: PyIActiveScriptError -->


<!-- page: PyIActiveScriptError.html -->

---

## PyIActiveScriptError Object

 Description of the interface

#### Methods

- GetExceptionInfo

 Description of GetExceptionInfo

- GetSourcePosition

 Description of GetSourcePosition

- GetSourceLineText

 Description of GetSourceLineText


<!-- page: PyIActiveScriptError__GetExceptionInfo_meth.html -->

## PyIActiveScriptError.GetExceptionInfo

 GetExceptionInfo()

Description of GetExceptionInfo.


<!-- page: PyIActiveScriptError__GetSourceLineText_meth.html -->

## PyIActiveScriptError.GetSourceLineText

 GetSourceLineText()

Description of GetSourceLineText.


<!-- page: PyIActiveScriptError__GetSourcePosition_meth.html -->

## PyIActiveScriptError.GetSourcePosition

 GetSourcePosition()

Description of GetSourcePosition.


---

<!-- object: PyIActiveScriptErrorDebug -->


<!-- page: PyIActiveScriptErrorDebug.html -->

---

## PyIActiveScriptErrorDebug Object

 Description of the interface

#### Methods

- GetDocumentContext

 Description of GetDocumentContext

- GetStackFrame

 Description of GetStackFrame


<!-- page: PyIActiveScriptErrorDebug__GetDocumentContext_meth.html -->

## PyIActiveScriptErrorDebug.GetDocumentContext

 GetDocumentContext()

Description of GetDocumentContext.


<!-- page: PyIActiveScriptErrorDebug__GetStackFrame_meth.html -->

## PyIActiveScriptErrorDebug.GetStackFrame

 GetStackFrame()

Description of GetStackFrame.


---

<!-- object: PyIActiveScriptParseProcedure -->


<!-- page: PyIActiveScriptParseProcedure.html -->

---

## PyIActiveScriptParseProcedure Object

 Description of the interface

#### Methods

- ParseProcedureText

 Description of ParseProcedureText


<!-- page: PyIActiveScriptParseProcedure__ParseProcedureText_meth.html -->

## PyIActiveScriptParseProcedure.ParseProcedureText

 ParseProcedureText(pstrCode, pstrFormalParams, pstrProcedureName, pstrItemName, punkContext, pstrDelimiter, dwSourceContextCookie, ulStartingLineNumber, dwFlags)

Description of ParseProcedureText.

#### Parameters

- pstrCode : unicode

 Description for pstrCode

- pstrFormalParams : unicode

 Description for pstrFormalParams

- pstrProcedureName : unicode

 Description for pstrProcedureName

- pstrItemName : unicode

 Description for pstrItemName

- punkContext : PyIUnknown

 Description for punkContext

- pstrDelimiter : unicode

 Description for pstrDelimiter

- dwSourceContextCookie : int

 Description for dwSourceContextCookie

- ulStartingLineNumber : int

 Description for ulStartingLineNumber

- dwFlags : int

 Description for dwFlags


---

<!-- object: PyIActiveScriptSite -->


<!-- page: PyIActiveScriptSite.html -->

---

## PyIActiveScriptSite Object

 An object providing the IActiveScriptSite interface

#### Methods

- GetLCID

- GetItemInfo

- GetDocVersionString

- OnStateChange

- OnEnterScript

- OnLeaveScript

- OnScriptError

- OnScriptTerminate


<!-- page: PyIActiveScriptSite__GetDocVersionString_meth.html -->

## PyIActiveScriptSite.GetDocVersionString

 int = GetDocVersionString()


<!-- page: PyIActiveScriptSite__GetItemInfo_meth.html -->

## PyIActiveScriptSite.GetItemInfo

 int = GetItemInfo()


<!-- page: PyIActiveScriptSite__GetLCID_meth.html -->

## PyIActiveScriptSite.GetLCID

 int = GetLCID()


<!-- page: PyIActiveScriptSite__OnEnterScript_meth.html -->

## PyIActiveScriptSite.OnEnterScript

 int = OnEnterScript()


<!-- page: PyIActiveScriptSite__OnLeaveScript_meth.html -->

## PyIActiveScriptSite.OnLeaveScript

 int = OnLeaveScript()


<!-- page: PyIActiveScriptSite__OnScriptError_meth.html -->

## PyIActiveScriptSite.OnScriptError

 int = OnScriptError()


<!-- page: PyIActiveScriptSite__OnScriptTerminate_meth.html -->

## PyIActiveScriptSite.OnScriptTerminate

 int = OnScriptTerminate()


<!-- page: PyIActiveScriptSite__OnStateChange_meth.html -->

## PyIActiveScriptSite.OnStateChange

 int = OnStateChange()


---

<!-- object: PyIActiveScriptSiteDebug -->


<!-- page: PyIActiveScriptSiteDebug.html -->

---

## PyIActiveScriptSiteDebug Object

 Description of the interface

#### Methods

- GetDocumentContextFromPosition

 Description of GetDocumentContextFromPosition

- GetApplication

 Description of GetApplication

- GetRootApplicationNode

 Description of GetRootApplicationNode

- OnScriptErrorDebug

 Allows a smart host to control the handling of runtime errors


<!-- page: PyIActiveScriptSiteDebug__GetApplication_meth.html -->

## PyIActiveScriptSiteDebug.GetApplication

 GetApplication()

Description of GetApplication.


<!-- page: PyIActiveScriptSiteDebug__GetDocumentContextFromPosition_meth.html -->

## PyIActiveScriptSiteDebug.GetDocumentContextFromPosition

 GetDocumentContextFromPosition(dwSourceContext, uCharacterOffset, uNumChars)

Description of GetDocumentContextFromPosition.

#### Parameters

- dwSourceContext : int

 Description for dwSourceContext

- uCharacterOffset : int

 Description for uCharacterOffset

- uNumChars : int

 Description for uNumChars


<!-- page: PyIActiveScriptSiteDebug__GetRootApplicationNode_meth.html -->

## PyIActiveScriptSiteDebug.GetRootApplicationNode

 GetRootApplicationNode()

Description of GetRootApplicationNode.


<!-- page: PyIActiveScriptSiteDebug__OnScriptErrorDebug_meth.html -->

## PyIActiveScriptSiteDebug.OnScriptErrorDebug

 int, int = OnScriptErrorDebug()

Allows a smart host to control the handling of runtime errors

#### Return Value

The result is a tuple of (bCallDebugger, bCallOnScriptErrorWhenContinuing)


---

<!-- object: PyIAddrBook -->


<!-- page: PyIAddrBook.html -->

---

## PyIAddrBook Object

 An COM interface to MAPI's IAddrBook interface.
Derived from PyIMAPIProp

#### Methods

- ResolveName

 Performs name resolution, assigning entry identifiers to recipients in a recipient list.

- OpenEntry

 Opens a folder or message and returns an interface object for further access.

- CompareEntryIDs

 Compares two entry identifiers belonging to a particular address book provider to determine if they refer to the same address book object


<!-- page: PyIAddrBook__CompareEntryIDs_meth.html -->

## PyIAddrBook.CompareEntryIDs

 int = CompareEntryIDs(entryId, entryId , flags )

Compares two entry identifiers belonging to a particular address book provider to determine if they refer to the same address book object

#### Parameters

- entryId : string

 The first entry ID to be compared

- entryId : string

 The second entry ID to be compared

- flags=0 : int

 Reserved - must be zero.

#### Return Value

The result is set to TRUE if the two entry identifiers refer to the same object, and FALSE otherwise.


<!-- page: PyIAddrBook__OpenEntry_meth.html -->

## PyIAddrBook.OpenEntry

 PyIInterface = OpenEntry(entryId, iid , flags )

Opens a folder or message and returns an interface object for further access.

#### Parameters

- entryId : string

 The entryID of the object

- iid : PyIID

 The IID of the object to return, or None for the default IID

- flags : int

 Bitmask of flags that controls how the object is opened.


<!-- page: PyIAddrBook__ResolveName_meth.html -->

## PyIAddrBook.ResolveName

 ResolveName(uiParm, flags, entryTitle, ADRLIST)

Performs name resolution, assigning entry identifiers to recipients in a recipient list.

#### Parameters

- uiParm : int

 hwnd of a dialogs parent.

- flags : int

 Bitmask of flags that controls whether a dialog box can be displayed.

- entryTitle : string

- ADRLIST : PyADRLIST

 Partial addresses to resolve.


---

<!-- object: PyIApplicationDebugger -->


<!-- page: PyIApplicationDebugger.html -->

---

## PyIApplicationDebugger Object

 Description of the interface

#### Methods

- QueryAlive

 Returns true if alive, else false.

- CreateInstanceAtDebugger

 Create objects in the application process address space.

- onDebugOutput

 Called when PyIDebugApplication::DebugOutput is called.

- onHandleBreakPoint

 Called when a breakpoint is hit.

- onClose

 Called when PyIDebugApplication::Close is called.

- onDebuggerEvent

 Handle a custom event.


<!-- page: PyIApplicationDebugger__CreateInstanceAtDebugger_meth.html -->

## PyIApplicationDebugger.CreateInstanceAtDebugger

 CreateInstanceAtDebugger(rclsid, pUnkOuter, dwClsContext, riid)

Create objects in the application process address space.

#### Parameters

- rclsid : PyIID

 Description for rclsid

- pUnkOuter : PyIUnknown

 Description for pUnkOuter

- dwClsContext : int

 Description for dwClsContext

- riid : PyIID

 Description for riid

#### Comments

 Provides a mechanism for the debugger IDE, running out-of-process to the application, to create objects in the application process. This method simply delegates to CoCreateInstance.


<!-- page: PyIApplicationDebugger__QueryAlive_meth.html -->

## PyIApplicationDebugger.QueryAlive

 QueryAlive()

Returns true if alive, else false.


<!-- page: PyIApplicationDebugger__onClose_meth.html -->

## PyIApplicationDebugger.onClose

 onClose()

Called when PyIDebugApplication::Close is called.


<!-- page: PyIApplicationDebugger__onDebugOutput_meth.html -->

## PyIApplicationDebugger.onDebugOutput

 onDebugOutput(pstr)

Called when PyIDebugApplication::DebugOutput is called.

#### Parameters

- pstr : unicode

 Description for pstr

#### Comments

 The debugger can use this to display the string in an output window.


<!-- page: PyIApplicationDebugger__onDebuggerEvent_meth.html -->

## PyIApplicationDebugger.onDebuggerEvent

 onDebuggerEvent(guid, uUnknown)

Description of onDebuggerEvent.

#### Parameters

- guid : PyIID

- uUnknown : PyIUnknown

#### Comments

 The semantics of guid and unknown are entirely application/debugger defined
This method may return E_NOTIMPL.


<!-- page: PyIApplicationDebugger__onHandleBreakPoint_meth.html -->

## PyIApplicationDebugger.onHandleBreakPoint

 onHandleBreakPoint(prpt, br, pError)

Called when a breakpoint is hit.

#### Parameters

- prpt : PyIRemoteDebugApplicationThread

 Description for prpt

- br : int

 Description for br

- pError : IActiveScriptErrorDebug

 Description for pError

#### Comments

 The application will remain suspended until the debugger IDE calls PyIDebugApplication::ResumeFromBreakPoint .


---

<!-- object: PyIApplicationDestinations -->


<!-- page: PyIApplicationDestinations.html -->

---

## PyIApplicationDestinations Object

 Allows an application to removed items from its jump lists

#### Methods

- SetAppID

 Specifies the application whose jump list is to be accessed

- RemoveDestination

 Removes a single entry from the jump list

- RemoveAllDestinations

 Removes all Recent and Frequent jump list entries


<!-- page: PyIApplicationDestinations__RemoveAllDestinations_meth.html -->

## PyIApplicationDestinations.RemoveAllDestinations

 RemoveAllDestinations()

Removes all Recent and Frequent jump list entries


<!-- page: PyIApplicationDestinations__RemoveDestination_meth.html -->

## PyIApplicationDestinations.RemoveDestination

 RemoveDestination(punk)

Removes a single entry from the jump lists

#### Parameters

- punk : PyIUnknown

 IShellItem or IShellLink representing an item in the application's jump list

#### Comments

 Does not remove pinned items


<!-- page: PyIApplicationDestinations__SetAppID_meth.html -->

## PyIApplicationDestinations.SetAppID

 SetAppID(AppID)

Specifies the application whose jump list is to be accessed

#### Parameters

- AppID : str

 Taskbar identifier for the application

#### Comments

 This method is only needed if the application sets its own taskbar identifier


---

<!-- object: PyIApplicationDocumentLists -->


<!-- page: PyIApplicationDocumentLists.html -->

---

## PyIApplicationDocumentLists Object

 Interface used to retrieve the jump lists for an application

#### Methods

- SetAppID

 Specifies the application whose jump list is to be accessed

- GetList

 Retrieves a list of items in a jump list


<!-- page: PyIApplicationDocumentLists__GetList_meth.html -->

## PyIApplicationDocumentLists.GetList

 PyIEnumObjects = GetList(ListType, ItemsDesired , riid )

Retrieves a list of items in a jump list

#### Parameters

- ListType : int

 Type of document list to return, shellcon.ADLT_RECENT or ADLT_FREQUENT

- ItemsDesired=0 : int

 Number of items to return, use 0 for all available

- riid=IID_IEnumObjects : PyIID

 The interface to return, IID_IEnumObjects or IID_IObjectArray


<!-- page: PyIApplicationDocumentLists__SetAppID_meth.html -->

## PyIApplicationDocumentLists.SetAppID

 SetAppID(AppID)

Specifies the application whose jump list is to be accessed

#### Parameters

- AppID : str

 Taskbar identifier for the application

#### Comments

 This method is only needed if the application sets its own taskbar identifier


---

<!-- object: PyIAsyncOperation -->


<!-- page: PyIAsyncOperation.html -->

---

## PyIAsyncOperation Object

 Description of the interface

#### Methods

- SetAsyncMode

 Description of SetAsyncMode

- GetAsyncMode

 Description of GetAsyncMode

- StartOperation

 Description of StartOperation

- InOperation

 Description of InOperation

- EndOperation

 Description of EndOperation


<!-- page: PyIAsyncOperation__EndOperation_meth.html -->

## PyIAsyncOperation.EndOperation

 EndOperation(hResult, pbcReserved, dwEffects)

Description of EndOperation.

#### Parameters

- hResult : int

 Description for hResult

- pbcReserved : PyIBindCtx

 Description for pbcReserved

- dwEffects : int

 Description for dwEffects


<!-- page: PyIAsyncOperation__GetAsyncMode_meth.html -->

## PyIAsyncOperation.GetAsyncMode

 bool = GetAsyncMode()

Description of GetAsyncMode.


<!-- page: PyIAsyncOperation__InOperation_meth.html -->

## PyIAsyncOperation.InOperation

 InOperation()

Description of InOperation.


<!-- page: PyIAsyncOperation__SetAsyncMode_meth.html -->

## PyIAsyncOperation.SetAsyncMode

 SetAsyncMode(fDoOpAsync)

Description of SetAsyncMode.

#### Parameters

- fDoOpAsync : int

 Description for fDoOpAsync


<!-- page: PyIAsyncOperation__StartOperation_meth.html -->

## PyIAsyncOperation.StartOperation

 StartOperation(pbcReserved)

Description of StartOperation.

#### Parameters

- pbcReserved : PyIBindCtx

 Description for pbcReserved


---

<!-- object: PyIAttach -->


<!-- page: PyIAttach.html -->

---

## PyIAttach Object

 An COM interface to MAPI
Derived from PyIMAPIProp

#### Methods

- GetLastError

 Returns the last error code for the object.


<!-- page: PyIAttach__GetLastError_meth.html -->

## PyIAttach.GetLastError

 MAPIERROR = GetLastError(hr, flags )

Returns the last error code for the object.

#### Parameters

- hr : int

 Contains the error code generated in the previous method call.

- flags : int

 Indicates for format for the output.


---

<!-- object: PyIBindCtx -->


<!-- page: PyIBindCtx.html -->

---

## PyIBindCtx Object

 A Python interface to IBindCtx. Derived from PyIUnknown

#### Methods

- GetRunningObjectTable

 Retrieves the running object table.

- GetBindOptions

 Retrieves bind options

- SetBindOptions

 Sets the bind options for the bind context

- RegisterObjectParam

 Associates a COM object to the bind context

- RevokeObjectParam

 Removes one of the bind context's associated objects

- GetObjectParam

 Retrieves one of the contexts string-keyed objects

- EnumObjectParam

 Creates an enumerator to list context's string keys

#### Based On

PyIUnknown


<!-- page: PyIBindCtx__EnumObjectParam_meth.html -->

## PyIBindCtx.EnumObjectParam

 PyIEnumString = EnumObjectParam()

Creates an enumerator to list context's string keys


<!-- page: PyIBindCtx__GetBindOptions_meth.html -->

## PyIBindCtx.GetBindOptions

 PyBIND_OPTS = GetBindOptions()

Retrieves the bind options for the bind context


<!-- page: PyIBindCtx__GetObjectParam_meth.html -->

## PyIBindCtx.GetObjectParam

 PyIUnknown = GetObjectParam(Key)

Returns one of the bind context's associated objects

#### Parameters

- Key : PyUnicode

 The string key for the object to be returned


<!-- page: PyIBindCtx__GetRunningObjectTable_meth.html -->

## PyIBindCtx.GetRunningObjectTable

 PyIRunningObjectTable = GetRunningObjectTable()

Retrieves an object interfacing to the Running Object Table.


<!-- page: PyIBindCtx__RegisterObjectParam_meth.html -->

## PyIBindCtx.RegisterObjectParam

 RegisterObjectParam(Key, punk)

Adds an object to the context's keyed table of associated objects

#### Parameters

- Key : PyUnicode

 The string key for the object to be registered

- punk : PyIUnknown

 COM object to be registered with the bind context


<!-- page: PyIBindCtx__RevokeObjectParam_meth.html -->

## PyIBindCtx.RevokeObjectParam

 RevokeObjectParam(Key)

Removes one of the bind context's registered objects

#### Parameters

- Key : PyUnicode

 The string key for the object to be removed


<!-- page: PyIBindCtx__SetBindOptions_meth.html -->

## PyIBindCtx.SetBindOptions

 SetBindOptions(bindopts)

Sets the bind options for the context

#### Parameters

- bindopts : dict

 PyBIND_OPTS dictionary containing the binding options


---

<!-- object: PyIBrowserFrameOptions -->


<!-- page: PyIBrowserFrameOptions.html -->

---

## PyIBrowserFrameOptions Object

 Description of the interface

#### Methods

- GetFrameOptions

 Description of GetFrameOptions


<!-- page: PyIBrowserFrameOptions__GetFrameOptions_meth.html -->

## PyIBrowserFrameOptions.GetFrameOptions

 GetFrameOptions(dwMask)

Description of GetFrameOptions.

#### Parameters

- dwMask : int

 Description for dwMask


---

<!-- object: PyICONINFO -->


<!-- page: PyICONINFO.html -->

---

## PyICONINFO Object

 Tuple describing an icon or cursor

#### Win32 API References

- Search for ICONINFO at [msdn](https://learn.microsoft.com/en-ca/search/?terms=ICONINFO), [google](https://www.google.com/search?q=ICONINFO) or [google groups](https://groups.google.com/groups?q=ICONINFO).

#### Items

- [0] boolean : Icon

 True indicates an icon, False for a cursor

- [1] int : xHotSpot

 For a cursor, X coord of hotspot. Ignored for icons

- [2] int : yHotSpot

 For a cursor, Y coord of hotspot. Ignored for icons

- [3] PyGdiHANDLE : hbmMask

 Monochrome mask bitmap

- [4] PyGdiHANDLE : hbmColor

 Color bitmap, may be None for black and white icon


---

<!-- object: PyICancelMethodCalls -->


<!-- page: PyICancelMethodCalls.html -->

---

## PyICancelMethodCalls Object

 Interface to request cancellation of a call. See pythoncom::CoGetCancelObject.

#### Methods

- Cancel

 Cancels a pending call

- TestCancel

 Checks if a request has been made to cancel a call


<!-- page: PyICancelMethodCalls__Cancel_meth.html -->

## PyICancelMethodCalls.Cancel

 Cancel(Seconds)

Cancels a pending call

#### Parameters

- Seconds : int

 Wait timeout in seconds


<!-- page: PyICancelMethodCalls__TestCancel_meth.html -->

## PyICancelMethodCalls.TestCancel

 int = TestCancel()

Checks if a request has been made to cancel a call

#### Return Value

Can return RPC_S_CALLPENDING or RPC_E_CALL_CANCELED


---

<!-- object: PyICatInformation -->


<!-- page: PyICatInformation.html -->

---

## PyICatInformation Object

 A Python interface to ICatInformation

#### Methods

- EnumCategories

 Returns an enumerator for the component categories registered on the system.

- GetCategoryDesc

 Retrieves the localized description string for a specific category ID.

- EnumClassesOfCategories

 Returns an enumerator over the classes that implement one or more interfaces.

#### Based On

PyIUnknown


<!-- page: PyICatInformation__EnumCategories_meth.html -->

## PyICatInformation.EnumCategories

 PyIEnumCATEGORYINFO = EnumCategories(lcid)

Returns an enumerator for the component categories registered on the system.

#### Parameters

- lcid=0 : int

 lcid


<!-- page: PyICatInformation__EnumClassesOfCategories_meth.html -->

## PyICatInformation.EnumClassesOfCategories

 PyIEnumGUID = EnumClassesOfCategories(listIIdImplemented, listIIdRequired )

Returns an enumerator over the classes that implement one or more interfaces.

#### Parameters

- listIIdImplemented=None : [PyIID, ...]

 A sequence of PyIID objects, or None.

- listIIdRequired=None : list iid

 A sequence of PyIID objects, or None.


<!-- page: PyICatInformation__GetCategoryDesc_meth.html -->

## PyICatInformation.GetCategoryDesc

 string = GetCategoryDesc(lcid)

Retrieves the localized description string for a specific category ID.

#### Parameters

- lcid=0 : int

 lcid

#### Comments

 The return type is a unicode object.


---

<!-- object: PyICatRegister -->


<!-- page: PyICatRegister.html -->

---

## PyICatRegister Object

 An interface to a COM ICatRegister interface.

#### Methods

- RegisterCategories

 Registers one or more component categories. Each component category consists of a CATID and a list of locale-dependent description strings.

- UnRegisterCategories

 Unregister one or more previously registered categories.

- RegisterClassImplCategories

 Registers the class as implementing one or more component categories.

- UnRegisterClassImplCategories

 Unregisters the class as implementing one or more component categories.

- RegisterClassReqCategories

 Registers the class as requiring one or more component categories.

- UnRegisterClassReqCategories

 Unregisters the class as requiring one or more component categories.

#### Based On

PyIUnknown


<!-- page: PyICatRegister__RegisterCategories_meth.html -->

## PyICatRegister.RegisterCategories

 RegisterCategories([ (catId, lcid, description), ...])

Registers one or more component categories. Each component category consists of a CATID and a list of locale-dependent description strings.

#### Parameters

- [ (catId, lcid, description), ...] : [ (PyIID, int, string), ...]

 A sequence of category descriptions.


<!-- page: PyICatRegister__RegisterClassImplCategories_meth.html -->

## PyICatRegister.RegisterClassImplCategories

 RegisterClassImplCategories(clsid, [catId, ...])

Registers the class as implementing one or more component categories.

#### Parameters

- clsid : PyIID

 Class ID of the relevent class

- [catId, ...] : [PyIID, ...]

 A sequence of category IDs to be associated with the class.


<!-- page: PyICatRegister__RegisterClassReqCategories_meth.html -->

## PyICatRegister.RegisterClassReqCategories

 RegisterClassReqCategories(clsid, [catId, ...])

Registers the class as requiring one or more component categories.

#### Parameters

- clsid : PyIID

 Class ID of the relevent class

- [catId, ...] : [PyIID, ...]

 A sequence of category IDs to be associated with the class.


<!-- page: PyICatRegister__UnRegisterClassImplCategories_meth.html -->

## PyICatRegister.UnRegisterClassImplCategories

 UnRegisterClassImplCategories(clsid, [catId, ...])

Unregisters the class as implementing one or more component categories.

#### Parameters

- clsid : PyIID

 Class ID of the relevent class

- [catId, ...] : [PyIID, ...]

 A sequence of category IDs to be unregistered from the class.


<!-- page: PyICatRegister__UnRegisterClassReqCategories_meth.html -->

## PyICatRegister.UnRegisterClassReqCategories

 UnRegisterClassReqCategories(clsid, [catId, ...])

Unregisters the class as requiring one or more component categories.

#### Parameters

- clsid : PyIID

 Class ID of the relevent class

- [catId, ...] : [PyIID, ...]

 A sequence of category IDs to be unregistered for the class.


<!-- page: PyICatRegister__UnregisterCategories_meth.html -->

## PyICatRegister.UnregisterCategories

 UnregisterCategories([catId, ...])

Unregister one or more previously registered categories.

#### Parameters

- [catId, ...] : [PyIID, ...]

 The list of category IDs to be unregistered.


---

<!-- object: PyICategoryProvider -->


<!-- page: PyICategoryProvider.html -->

---

## PyICategoryProvider Object

 Description of the interface

#### Methods

- CanCategorizeOnSCID

 Description of CanCategorizeOnSCID

- GetDefaultCategory

 Description of GetDefaultCategory

- GetCategoryForSCID

 Description of GetCategoryForSCID

- EnumCategories

 Description of EnumCategories

- GetCategoryName

 Description of GetCategoryName

- CreateCategory

 Description of CreateCategory


<!-- page: PyICategoryProvider__CanCategorizeOnSCID_meth.html -->

## PyICategoryProvider.CanCategorizeOnSCID

 CanCategorizeOnSCID(pscid)

Description of CanCategorizeOnSCID.

#### Parameters

- pscid : SHCOLUMNID

 Description for pscid


<!-- page: PyICategoryProvider__CreateCategory_meth.html -->

## PyICategoryProvider.CreateCategory

 CreateCategory(guid, riid)

Description of CreateCategory.

#### Parameters

- guid : PyIID

 Description for pguid

- riid : PyIID

 Description for riid


<!-- page: PyICategoryProvider__EnumCategories_meth.html -->

## PyICategoryProvider.EnumCategories

 EnumCategories()

Description of EnumCategories.


<!-- page: PyICategoryProvider__GetCategoryForSCID_meth.html -->

## PyICategoryProvider.GetCategoryForSCID

 GetCategoryForSCID(pscid)

Description of GetCategoryForSCID.

#### Parameters

- pscid : SHCOLUMNID

 Description for pscid


<!-- page: PyICategoryProvider__GetCategoryName_meth.html -->

## PyICategoryProvider.GetCategoryName

 GetCategoryName(guid)

Description of GetCategoryName.

#### Parameters

- guid : PyIID

 Description for pguid

#### Comments

 The buffer is always 1024 chars long


<!-- page: PyICategoryProvider__GetDefaultCategory_meth.html -->

## PyICategoryProvider.GetDefaultCategory

 GetDefaultCategory()

Description of GetDefaultCategory.


---

<!-- object: PyIClassFactory -->


<!-- page: PyIClassFactory.html -->

---

## PyIClassFactory Object

 An object which represents the IClassFactory interface. Derived from PyIUnknown

#### Methods

- CreateInstance

 Creates an uninitialized object.

- LockServer

 Called by the client of a class object to keep a server open in memory, allowing instances to be created more quickly.


<!-- page: PyIClassFactory__CreateInstance_meth.html -->

## PyIClassFactory.CreateInstance

 PyIUnknown = CreateInstance(outerUnknown, iid )

Creates an uninitialized object.

#### Parameters

- outerUnknown : PyIUnknown

 Usually None, otherwise the outer unknown if the object is being created as part of an aggregate.

- iid : PyIID

 The IID of the resultant object.

#### Return Value

The result object will always be derived from PyIUnknown, but will be of the type specified by iid.


<!-- page: PyIClassFactory__LockServer_meth.html -->

## PyIClassFactory.LockServer

 LockServer(bInc)

Called by the client of a class object to keep a server open in memory, allowing instances to be created more quickly.

#### Parameters

- bInc : int

 1 of the server should be locked, 0 if the server should be unlocked.


---

<!-- object: PyIClientSecurity -->


<!-- page: PyIClientSecurity.html -->

---

## PyIClientSecurity Object

 Description of the interface

#### Methods

- QueryBlanket

 Retrieves the authentication settings for an interface

- SetBlanket

 Changes the authentication options used with an interface

- CopyProxy

 Makes a private copy of a proxy interface


<!-- page: PyIClientSecurity__CopyProxy_meth.html -->

## PyIClientSecurity.CopyProxy

 PyIUnknown = CopyProxy(Proxy)

Makes a private copy of a proxy interface

#### Parameters

- Proxy : PyIUnknown

 The remote interface to be copied


<!-- page: PyIClientSecurity__QueryBlanket_meth.html -->

## PyIClientSecurity.QueryBlanket

 dict = QueryBlanket(Proxy)

Retrieves the authentication settings for an interface

#### Parameters

- Proxy : PyIUnknown

 An interface created through a proxy


<!-- page: PyIClientSecurity__SetBlanket_meth.html -->

## PyIClientSecurity.SetBlanket

 SetBlanket(Proxy, AuthnSvc, AuthzSvc, ServerPrincipalName, AuthnLevel, ImpLevel, AuthInfo, Capabilities)

Changes the authentication options used with an interface

#### Parameters

- Proxy : PyIUnknown

 The proxy interface for which to set security options

- AuthnSvc : int

 Authentication service identifier, pythoncom.RPC_C_AUTHN_* (but not RPC_C_AUTHN_LEVEL_*)

- AuthzSvc : int

 Authorization service identifier, pythoncom.RPC_C_AUTHZ_*

- ServerPrincipalName : PyUnicode

 SPN that identifies the server, can be None

- AuthnLevel : int

 Authentication level, pythoncom.RPC_C_AUTHN_LEVEL_*

- ImpLevel : int

 Impersonation level, pythoncom.RPC_C_IMP_LEVEL_*

- AuthInfo : None

 Not supported yet, use only None

- Capabilities : int

 Combination of pythoncom.EOAC_* flags. Must be a subset of the capabilities of the specified authentication service.


---

<!-- object: PyIColumnProvider -->


<!-- page: PyIColumnProvider.html -->

---

## PyIColumnProvider Object

 Description of the interface

#### Methods

- Initialize

 Description of Initialize

- GetColumnInfo

 Description of GetColumnInfo

- GetItemData

 Description of GetItemData


<!-- page: PyIColumnProvider__GetColumnInfo_meth.html -->

## PyIColumnProvider.GetColumnInfo

 GetColumnInfo(dwIndex)

Description of GetColumnInfo.

#### Parameters

- dwIndex : int

 Description for dwIndex


<!-- page: PyIColumnProvider__GetItemData_meth.html -->

## PyIColumnProvider.GetItemData

 GetItemData(pscid, pscd)

Description of GetItemData.

#### Parameters

- pscid : PySHCOLUMNID

 Description for pscid

- pscd : PySHCOLUMNDATA

 Description for pscd


<!-- page: PyIColumnProvider__Initialize_meth.html -->

## PyIColumnProvider.Initialize

 Initialize(psci)

Description of Initialize.

#### Parameters

- psci : PyCSHCOLUMNINIT

 Description for psci


---

<!-- object: PyIConnectionPoint -->


<!-- page: PyIConnectionPoint.html -->

---

## PyIConnectionPoint Object

 A Python wrapper of a COM IConnectionPoint interface.

#### Methods

- GetConnectionInterface

 Retrieves the IID of the interface represented by the connection point.

- GetConnectionPointContainer

 Gets the connection point container for the object.

- Advise

 Establishes a connection between the connection point object and the client's sink.

- Unadvise

 Terminates an advisory connection previously established through PyIConnectionPoint::Advise.

- EnumConnections

 Creates an enumerator to iterate through the connections for the connection point

#### Based On

PyIUnknown


<!-- page: PyIConnectionPoint__Advise_meth.html -->

## PyIConnectionPoint.Advise

 int = Advise(unk)

Establishes a connection between the connection point object and the client's sink.

#### Parameters

- unk : PyIUnknown

 The client's advise sink

#### Return Value

The result is the connection point identifier used by PyIConnectionPoint::Unadvise


<!-- page: PyIConnectionPoint__EnumConnections_meth.html -->

## PyIConnectionPoint.EnumConnections

 PyIEnumConnections = EnumConnections()

Creates an enumerator to iterate through the connections for the connection point


<!-- page: PyIConnectionPoint__GetConnectionInterface_meth.html -->

## PyIConnectionPoint.GetConnectionInterface

 PyIID = GetConnectionInterface()

Retrieves the IID of the interface represented by the connection point.


<!-- page: PyIConnectionPoint__GetConnectionPointContainer_meth.html -->

## PyIConnectionPoint.GetConnectionPointContainer

 PyIConnectionPointContainer = GetConnectionPointContainer()

Gets the connection point container for the object.


<!-- page: PyIConnectionPoint__Unadvise_meth.html -->

## PyIConnectionPoint.Unadvise

 Unadvise(cookie)

Terminates an advisory connection previously established through IConnectionPoint::Advise. The dwCookie parameter identifies the connection to terminate.

#### Parameters

- cookie : int

 The connection token


---

<!-- object: PyIConnectionPointContainer -->


<!-- page: PyIConnectionPointContainer.html -->

---

## PyIConnectionPointContainer Object

 A Python wrapper of a COM IConnectionPointContainer interface.

#### Methods

- EnumConnectionPoints

 Creates an enumerator object to iterate through all the connection points supported in the connectable object, one connection point per outgoing IID.

- FindConnectionPoint

 Finds a connection point for the given IID.

#### Based On

PyIUnknown


<!-- page: PyIConnectionPointContainer__EnumConnectionPoints_meth.html -->

## PyIConnectionPointContainer.EnumConnectionPoints

 PyIEnumConnectionPoints = EnumConnectionPoints()

Creates an enumerator object to iterate through all the connection points supported in the connectable object, one connection point per outgoing IID.


<!-- page: PyIConnectionPointContainer__FindConnectionPoint_meth.html -->

## PyIConnectionPointContainer.FindConnectionPoint

 PyIConnectionPoint = FindConnectionPoint(iid)

Finds a connection point for the given IID

#### Parameters

- iid : PyIID

 The IID of the requested connection.


---

<!-- object: PyIContext -->


<!-- page: PyIContext.html -->

---

## PyIContext Object

 Allows access to properties defined for the current context

#### Methods

- SetProperty

 Sets a property on the context

- RemoveProperty

 Removes a property from the context

- GetProperty

 Retrieves a context property

- EnumContextProps

 Returns an enumerator for the context properties


<!-- page: PyIContext__EnumContextProps_meth.html -->

## PyIContext.EnumContextProps

 PyIEnumContextProps = EnumContextProps()

Returns an enumerator for the context properties


<!-- page: PyIContext__GetProperty_meth.html -->

## PyIContext.GetProperty

 (int, PyIUnknown) = GetProperty(rGuid)

Retrieves a context property

#### Parameters

- rGuid : PyIID

 GUID that identifies a context property

#### Return Value

Returns flags (CPFLAGS is reserved, no defined values) and the IUnknown interface set for the property


<!-- page: PyIContext__RemoveProperty_meth.html -->

## PyIContext.RemoveProperty

 RemoveProperty(rPolicyId)

Removes a property from the context

#### Parameters

- rPolicyId : PyIID

 GUID that identifies a context property


<!-- page: PyIContext__SetProperty_meth.html -->

## PyIContext.SetProperty

 SetProperty(rpolicyId, flags, pUnk)

Sets a property on the context

#### Parameters

- rpolicyId : PyIID

 GUID identifying the property to be set

- flags : int

 Reserved, use only 0

- pUnk : PyIUnknown

 The property value


---

<!-- object: PyIContextMenu -->


<!-- page: PyIContextMenu.html -->

---

## PyIContextMenu Object

 Description of the interface

#### Methods

- QueryContextMenu

 Adds options to a context menu

- InvokeCommand

 Executes a context menu option

- GetCommandString

 Retrieves verb or help text for a context menu option


<!-- page: PyIContextMenu__GetCommandString_meth.html -->

## PyIContextMenu.GetCommandString

 str = GetCommandString(idCmd, uType , cchMax )

Retrieves verb or help text for a context menu option

#### Parameters

- idCmd : int

 Id of the command

- uType : int

 One of the shellcon.GCS_* constants

- cchMax=2048 : int

 Size of buffer to create for returned string


<!-- page: PyIContextMenu__InvokeCommand_meth.html -->

## PyIContextMenu.InvokeCommand

 InvokeCommand(pici)

Executes a context menu option

#### Parameters

- pici : PyCMINVOKECOMMANDINFO

 Tuple of parameters representing a CMINVOKECOMMANDINFO struct


<!-- page: PyIContextMenu__QueryContextMenu_meth.html -->

## PyIContextMenu.QueryContextMenu

 int = QueryContextMenu(hmenu, indexMenu , idCmdFirst , idCmdLast , uFlags )

Adds options to a context menu

#### Parameters

- hmenu : PyHANDLE

 Handle to menu to which items should be added

- indexMenu : int

 Zero-based index at which to add first item

- idCmdFirst : int

 Minimum menu item Id

- idCmdLast : int

 Max menu item Id

- uFlags : int

 Combination of shellcon.CMF_* flags, can be 0


---

<!-- object: PyICopyHookA -->


<!-- page: PyICopyHookA.html -->

---

## PyICopyHookA Object

 Description of the interface

#### Methods

- CopyCallback

 Description of CopyCallback


<!-- page: PyICopyHookA__CopyCallback_meth.html -->

## PyICopyHookA.CopyCallback

 CopyCallback(hwnd, wFunc, wFlags, srcFile, srcAttribs, destFile, destAttribs)

Description of CopyCallback.

#### Parameters

- hwnd : HWND

 Description for hwnd

- wFunc : int

 Description for wFunc

- wFlags : int

 Description for wFlags

- srcFile : string/unicode

 Description for srcFile

- srcAttribs : int

 Description for srcAttribs

- destFile : string/unicode

 Description for destFile

- destAttribs : int

 Description for destAttribs


---

<!-- object: PyICopyHookW -->


<!-- page: PyICopyHookW.html -->

---

## PyICopyHookW Object

 Description of the interface

#### Methods

- CopyCallback

 Description of CopyCallback


<!-- page: PyICopyHookW__CopyCallback_meth.html -->

## PyICopyHookW.CopyCallback

 CopyCallback(hwnd, wFunc, wFlags, srcFile, srcAttribs, destFile, destAttribs)

Description of CopyCallback.

#### Parameters

- hwnd : HWND

 Description for hwnd

- wFunc : int

 Description for wFunc

- wFlags : int

 Description for wFlags

- srcFile : string/unicode

 Description for srcFile

- srcAttribs : int

 Description for srcAttribs

- destFile : string/unicode

 Description for destFile

- destAttribs : int

 Description for destAttribs


---

<!-- object: PyICreateTypeInfo -->


<!-- page: PyICreateTypeInfo.html -->

---

## PyICreateTypeInfo Object

 Description of the interface

#### Methods

- SetGuid

 Description of SetGuid

- SetTypeFlags

 Description of SetTypeFlags

- SetDocString

 Description of SetDocString

- SetHelpContext

 Description of SetHelpContext

- SetVersion

 Description of SetVersion

- AddRefTypeInfo

 Description of AddRefTypeInfo

- AddFuncDesc

 Description of AddFuncDesc

- AddImplType

 Description of AddImplType

- SetImplTypeFlags

 Description of SetImplTypeFlags

- SetAlignment

 Description of SetAlignment

- SetSchema

 Description of SetSchema

- AddVarDesc

 Description of AddVarDesc

- SetFuncAndParamNames

 Description of SetFuncAndParamNames

- SetVarName

 Description of SetVarName

- SetTypeDescAlias

 Description of SetTypeDescAlias

- DefineFuncAsDllEntry

 Description of DefineFuncAsDllEntry

- SetFuncDocString

 Description of SetFuncDocString

- SetVarDocString

 Description of SetVarDocString

- SetFuncHelpContext

 Description of SetFuncHelpContext

- SetVarHelpContext

 Description of SetVarHelpContext

- SetMops

 Description of SetMops

- LayOut

 Description of LayOut


<!-- page: PyICreateTypeInfo__AddFuncDesc_meth.html -->

## PyICreateTypeInfo.AddFuncDesc

 AddFuncDesc(index)

Description of AddFuncDesc.

#### Parameters

- index : int

 Description for index


<!-- page: PyICreateTypeInfo__AddImplType_meth.html -->

## PyICreateTypeInfo.AddImplType

 AddImplType(index, hRefType)

Description of AddImplType.

#### Parameters

- index : int

 Description for index

- hRefType : int

 A hRefType


<!-- page: PyICreateTypeInfo__AddRefTypeInfo_meth.html -->

## PyICreateTypeInfo.AddRefTypeInfo

 AddRefTypeInfo(pTInfo)

Description of AddRefTypeInfo.

#### Parameters

- pTInfo : PyITypeInfo

 Description for pTInfo


<!-- page: PyICreateTypeInfo__AddVarDesc_meth.html -->

## PyICreateTypeInfo.AddVarDesc

 AddVarDesc(index)

Description of AddVarDesc.

#### Parameters

- index : int

 Description for index


<!-- page: PyICreateTypeInfo__DefineFuncAsDllEntry_meth.html -->

## PyICreateTypeInfo.DefineFuncAsDllEntry

 DefineFuncAsDllEntry(index, szDllName, szProcName)

Description of DefineFuncAsDllEntry.

#### Parameters

- index : int

 Description for index

- szDllName : unicode

 Description for szDllName

- szProcName : unicode

 Description for szProcName


<!-- page: PyICreateTypeInfo__LayOut_meth.html -->

## PyICreateTypeInfo.LayOut

 LayOut()

Description of LayOut.


<!-- page: PyICreateTypeInfo__SetAlignment_meth.html -->

## PyICreateTypeInfo.SetAlignment

 SetAlignment(cbAlignment)

Description of SetAlignment.

#### Parameters

- cbAlignment : int

 Description for cbAlignment


<!-- page: PyICreateTypeInfo__SetDocString_meth.html -->

## PyICreateTypeInfo.SetDocString

 SetDocString(pStrDoc)

Description of SetDocString.

#### Parameters

- pStrDoc : unicode

 Description for pStrDoc


<!-- page: PyICreateTypeInfo__SetFuncAndParamNames_meth.html -->

## PyICreateTypeInfo.SetFuncAndParamNames

 SetFuncAndParamNames(index, rgszNames)

Description of SetFuncAndParamNames.

#### Parameters

- index : int

 Index of the item to set.

- rgszNames : (unicode , ...)

 A sequence of unicode or String objects.


<!-- page: PyICreateTypeInfo__SetFuncDocString_meth.html -->

## PyICreateTypeInfo.SetFuncDocString

 SetFuncDocString(index, szDocString)

Description of SetFuncDocString.

#### Parameters

- index : int

 Description for index

- szDocString : unicode

 Description for szDocString


<!-- page: PyICreateTypeInfo__SetFuncHelpContext_meth.html -->

## PyICreateTypeInfo.SetFuncHelpContext

 SetFuncHelpContext(index, dwHelpContext)

Description of SetFuncHelpContext.

#### Parameters

- index : int

 Description for index

- dwHelpContext : int

 Description for dwHelpContext


<!-- page: PyICreateTypeInfo__SetGuid_meth.html -->

## PyICreateTypeInfo.SetGuid

 SetGuid(guid)

Description of SetGuid.

#### Parameters

- guid : PyIID

 Description for guid


<!-- page: PyICreateTypeInfo__SetHelpContext_meth.html -->

## PyICreateTypeInfo.SetHelpContext

 SetHelpContext(dwHelpContext)

Description of SetHelpContext.

#### Parameters

- dwHelpContext : int

 Description for dwHelpContext


<!-- page: PyICreateTypeInfo__SetImplTypeFlags_meth.html -->

## PyICreateTypeInfo.SetImplTypeFlags

 SetImplTypeFlags(index, implTypeFlags)

Description of SetImplTypeFlags.

#### Parameters

- index : int

 Description for index

- implTypeFlags : int

 Description for implTypeFlags


<!-- page: PyICreateTypeInfo__SetMops_meth.html -->

## PyICreateTypeInfo.SetMops

 SetMops(index, bstrMops)

Description of SetMops.

#### Parameters

- index : int

 Description for index

- bstrMops : unicode

 Description for bstrMops


<!-- page: PyICreateTypeInfo__SetSchema_meth.html -->

## PyICreateTypeInfo.SetSchema

 SetSchema(pStrSchema)

Description of SetSchema.

#### Parameters

- pStrSchema : unicode

 Description for pStrSchema


<!-- page: PyICreateTypeInfo__SetTypeDescAlias_meth.html -->

## PyICreateTypeInfo.SetTypeDescAlias

 SetTypeDescAlias()

Description of SetTypeDescAlias.


<!-- page: PyICreateTypeInfo__SetTypeFlags_meth.html -->

## PyICreateTypeInfo.SetTypeFlags

 SetTypeFlags(uTypeFlags)

Description of SetTypeFlags.

#### Parameters

- uTypeFlags : int

 Description for uTypeFlags


<!-- page: PyICreateTypeInfo__SetVarDocString_meth.html -->

## PyICreateTypeInfo.SetVarDocString

 SetVarDocString(index, szDocString)

Description of SetVarDocString.

#### Parameters

- index : int

 Description for index

- szDocString : unicode

 Description for szDocString


<!-- page: PyICreateTypeInfo__SetVarHelpContext_meth.html -->

## PyICreateTypeInfo.SetVarHelpContext

 SetVarHelpContext(index, dwHelpContext)

Description of SetVarHelpContext.

#### Parameters

- index : int

 Description for index

- dwHelpContext : int

 Description for dwHelpContext


<!-- page: PyICreateTypeInfo__SetVarName_meth.html -->

## PyICreateTypeInfo.SetVarName

 SetVarName(index, szName)

Description of SetVarName.

#### Parameters

- index : int

 Description for index

- szName : unicode

 Description for szName


<!-- page: PyICreateTypeInfo__SetVersion_meth.html -->

## PyICreateTypeInfo.SetVersion

 SetVersion(wMajorVerNum, wMinorVerNum)

Description of SetVersion.

#### Parameters

- wMajorVerNum : int

 Description for wMajorVerNum

- wMinorVerNum : int

 Description for wMinorVerNum


---

<!-- object: PyICreateTypeLib -->


<!-- page: PyICreateTypeLib.html -->

---

## PyICreateTypeLib Object

 Description of the interface

#### Methods

- CreateTypeInfo

 Description of CreateTypeInfo

- SetName

 Description of SetName

- SetVersion

 Description of SetVersion

- SetGuid

 Description of SetGuid

- SetDocString

 Description of SetDocString

- SetHelpFileName

 Description of SetHelpFileName

- SetHelpContext

 Description of SetHelpContext

- SetLcid

 Description of SetLcid

- SetLibFlags

 Description of SetLibFlags

- SaveAllChanges

 Description of SaveAllChanges


<!-- page: PyICreateTypeLib__CreateTypeInfo_meth.html -->

## PyICreateTypeLib.CreateTypeInfo

 CreateTypeInfo(szName)

Description of CreateTypeInfo.

#### Parameters

- szName : unicode

 Description for szName


<!-- page: PyICreateTypeLib__SaveAllChanges_meth.html -->

## PyICreateTypeLib.SaveAllChanges

 SaveAllChanges()

Description of SaveAllChanges.


<!-- page: PyICreateTypeLib__SetDocString_meth.html -->

## PyICreateTypeLib.SetDocString

 SetDocString(szDoc)

Description of SetDocString.

#### Parameters

- szDoc : unicode

 Description for szDoc


<!-- page: PyICreateTypeLib__SetGuid_meth.html -->

## PyICreateTypeLib.SetGuid

 SetGuid(guid)

Description of SetGuid.

#### Parameters

- guid : PyIID

 Description for guid


<!-- page: PyICreateTypeLib__SetHelpContext_meth.html -->

## PyICreateTypeLib.SetHelpContext

 SetHelpContext(dwHelpContext)

Description of SetHelpContext.

#### Parameters

- dwHelpContext : int

 Description for dwHelpContext


<!-- page: PyICreateTypeLib__SetHelpFileName_meth.html -->

## PyICreateTypeLib.SetHelpFileName

 SetHelpFileName(szHelpFileName)

Description of SetHelpFileName.

#### Parameters

- szHelpFileName : unicode

 Description for szHelpFileName


<!-- page: PyICreateTypeLib__SetLcid_meth.html -->

## PyICreateTypeLib.SetLcid

 SetLcid()

Description of SetLcid.


<!-- page: PyICreateTypeLib__SetLibFlags_meth.html -->

## PyICreateTypeLib.SetLibFlags

 SetLibFlags(uLibFlags)

Description of SetLibFlags.

#### Parameters

- uLibFlags : int

 Description for uLibFlags


<!-- page: PyICreateTypeLib__SetName_meth.html -->

## PyICreateTypeLib.SetName

 SetName(szName)

Description of SetName.

#### Parameters

- szName : unicode

 Description for szName


<!-- page: PyICreateTypeLib__SetVersion_meth.html -->

## PyICreateTypeLib.SetVersion

 SetVersion(wMajorVerNum, wMinorVerNum)

Description of SetVersion.

#### Parameters

- wMajorVerNum : int

 Description for wMajorVerNum

- wMinorVerNum : int

 Description for wMinorVerNum


---

<!-- object: PyICreateTypeLib2 -->


<!-- page: PyICreateTypeLib2.html -->

---

## PyICreateTypeLib2 Object

 Description of the interface

#### Methods

- CreateTypeInfo

 Description of CreateTypeInfo

- SetName

 Description of SetName

- SetVersion

 Description of SetVersion

- SetGuid

 Description of SetGuid

- SetDocString

 Description of SetDocString

- SetHelpFileName

 Description of SetHelpFileName

- SetHelpContext

 Description of SetHelpContext

- SetLcid

 Description of SetLcid

- SetLibFlags

 Description of SetLibFlags

- SaveAllChanges

 Description of SaveAllChanges


<!-- page: PyICreateTypeLib2__CreateTypeInfo_meth.html -->

## PyICreateTypeLib2.CreateTypeInfo

 CreateTypeInfo(szName)

Description of CreateTypeInfo.

#### Parameters

- szName : unicode

 Description for szName


<!-- page: PyICreateTypeLib2__SaveAllChanges_meth.html -->

## PyICreateTypeLib2.SaveAllChanges

 SaveAllChanges()

Description of SaveAllChanges.


<!-- page: PyICreateTypeLib2__SetDocString_meth.html -->

## PyICreateTypeLib2.SetDocString

 SetDocString(szDoc)

Description of SetDocString.

#### Parameters

- szDoc : unicode

 Description for szDoc


<!-- page: PyICreateTypeLib2__SetGuid_meth.html -->

## PyICreateTypeLib2.SetGuid

 SetGuid(guid)

Description of SetGuid.

#### Parameters

- guid : PyIID

 Description for guid


<!-- page: PyICreateTypeLib2__SetHelpContext_meth.html -->

## PyICreateTypeLib2.SetHelpContext

 SetHelpContext(dwHelpContext)

Description of SetHelpContext.

#### Parameters

- dwHelpContext : int

 Description for dwHelpContext


<!-- page: PyICreateTypeLib2__SetHelpFileName_meth.html -->

## PyICreateTypeLib2.SetHelpFileName

 SetHelpFileName(szHelpFileName)

Description of SetHelpFileName.

#### Parameters

- szHelpFileName : unicode

 Description for szHelpFileName


<!-- page: PyICreateTypeLib2__SetLcid_meth.html -->

## PyICreateTypeLib2.SetLcid

 SetLcid()

Description of SetLcid.


<!-- page: PyICreateTypeLib2__SetLibFlags_meth.html -->

## PyICreateTypeLib2.SetLibFlags

 SetLibFlags(uLibFlags)

Description of SetLibFlags.

#### Parameters

- uLibFlags : int

 Description for uLibFlags


<!-- page: PyICreateTypeLib2__SetName_meth.html -->

## PyICreateTypeLib2.SetName

 SetName(szName)

Description of SetName.

#### Parameters

- szName : unicode

 Description for szName


<!-- page: PyICreateTypeLib2__SetVersion_meth.html -->

## PyICreateTypeLib2.SetVersion

 SetVersion(wMajorVerNum, wMinorVerNum)

Description of SetVersion.

#### Parameters

- wMajorVerNum : int

 Description for wMajorVerNum

- wMinorVerNum : int

 Description for wMinorVerNum


---

<!-- object: PyICurrentItem -->


<!-- page: PyICurrentItem.html -->

---

## PyICurrentItem Object

 Description of the interface

#### Based On

PyIRelatedItem


---

<!-- object: PyICustomDestinationList -->


<!-- page: PyICustomDestinationList.html -->

---

## PyICustomDestinationList Object

 Interface used to customize an application's jump list

#### Methods

- SetAppID

 Specifies the taskbar identifier for the jump list

- BeginList

 Clears the jump list and prepares it to be repopulated

- AppendCategory

 Adds a custom category to the jump list

- AppendKnownCategory

 Adds one of the predefined categories to the custom list

- AddUserTasks

 Sets the entries shown in the Tasks category

- CommitList

 Finalizes changes

- GetRemovedDestinations

 Returns all the items removed from the jump list

- DeleteList

 Removes any customization, leaving only the system-maintained Recent and Frequent lists

- AbortList

 Discards all changes


<!-- page: PyICustomDestinationList__AbortList_meth.html -->

## PyICustomDestinationList.AbortList

 AbortList()

Discards all changes


<!-- page: PyICustomDestinationList__AddUserTasks_meth.html -->

## PyICustomDestinationList.AddUserTasks

 AddUserTasks(Items)

Sets the entries shown in the Tasks category

#### Parameters

- Items : PyIObjectArray

 Collection of PyIShellItem and/or PyIShellLink interfaces


<!-- page: PyICustomDestinationList__AppendCategory_meth.html -->

## PyICustomDestinationList.AppendCategory

 AppendCategory(Category, Items)

Adds a custom category to the jump list

#### Parameters

- Category : str

 Display name of the category, can also be a dll and resource id for localization

- Items : PyIObjectArray

 Collection of IShellItem and/or IShellLink interfaces


<!-- page: PyICustomDestinationList__AppendKnownCategory_meth.html -->

## PyICustomDestinationList.AppendKnownCategory

 AppendKnownCategory(Category)

Adds one of the predefined categories to the custom list

#### Parameters

- Category : int

 shellcon.KDC_RECENT or KDC_FREQUENT


<!-- page: PyICustomDestinationList__BeginList_meth.html -->

## PyICustomDestinationList.BeginList

 int, PyIObjectArray = BeginList(riid)

Clears the jump list and prepares it to be repopulated

#### Parameters

- riid=IID_IObjectArray : PyIID

 The interface to return

#### Return Value

Returns the number of slots and a collection of all destinations removed from the jump list


<!-- page: PyICustomDestinationList__CommitList_meth.html -->

## PyICustomDestinationList.CommitList

 CommitList()

Finalizes changes.


<!-- page: PyICustomDestinationList__DeleteList_meth.html -->

## PyICustomDestinationList.DeleteList

 DeleteList(AppID)

Removes any customization, leaving only the system-maintained Recent and Frequent lists

#### Parameters

- AppID=None : str

 The taskbar identifier of the application


<!-- page: PyICustomDestinationList__GetRemovedDestinations_meth.html -->

## PyICustomDestinationList.GetRemovedDestinations

 PyIObjectArray = GetRemovedDestinations(riid)

Returns all the items removed from the jump list

#### Parameters

- riid=IID_IObjectArray : PyIID

 The interface to return


<!-- page: PyICustomDestinationList__SetAppID_meth.html -->

## PyICustomDestinationList.SetAppID

 SetAppID(AppID)

Specifies the taskbar identifier for the jump list

#### Parameters

- AppID : str

 The taskbar identifier of the application

#### Comments

 Only needed if the calling app doesn't use the system-assigned default


---

<!-- object: PyIDL -->


<!-- page: PyIDL.html -->

---

## PyIDL Object

 A Python representation of an IDL. Implemented as a sequence of Python strings. FALSE*/, UINT *pcb /* = NULL */)


---

<!-- object: PyIDataObject -->


<!-- page: PyIDataObject.html -->

---

## PyIDataObject Object

 Used to transfer data in various formats throughout the shell

#### Comments

 Can be enumerated to return a series of PyFORMATETC describing the formats that the object can render.

#### Methods

- GetData

 Retrieves data from the object in specified format

- GetDataHere

 Returns a copy of the object's data in specified format

- QueryGetData

 Checks if the object supports returning data in a particular format

- GetCanonicalFormatEtc

 Transforms a FORMATECT data description into a general format that the object supports

- SetData

 Sets the data that the object will return.

- EnumFormatEtc

 Returns an enumerator to list the data formats that the object supports.

- DAdvise

 Connects the object to an interface that will receive notifications when its data changes

- DUnadvise

 Disconnects a notification sink.

- EnumDAdvise

 Creates an enumerator to list connected notification sinks.


<!-- page: PyIDataObject__DAdvise_meth.html -->

## PyIDataObject.DAdvise

 int = DAdvise(pformatetc, advf , pAdvSink )

Connects the object to an interface that will receive notifications when its data changes

#### Parameters

- pformatetc : PyFORMATETC

 Defines the type of data for which the sink will receive notifications.

- advf : int

 Combination of values from ADVF enum. (which currently do not appear in any of the constants modules!)

- pAdvSink : PyIAdviseSink

 Currently this interface is not wrapped.

#### Return Value

Returns a unique number that is used to identify the connection


<!-- page: PyIDataObject__DUnadvise_meth.html -->

## PyIDataObject.DUnadvise

 DUnadvise(dwConnection)

Disconnects a notification sink.

#### Parameters

- dwConnection : int

 Identifier of the connection as returned by DAdvise.


<!-- page: PyIDataObject__EnumDAdvise_meth.html -->

## PyIDataObject.EnumDAdvise

 PyIEnumSTATDATA = EnumDAdvise()

Creates an enumerator to list connected notification sinks.


<!-- page: PyIDataObject__EnumFormatEtc_meth.html -->

## PyIDataObject.EnumFormatEtc

 PyIEnumFORMATETC = EnumFormatEtc(dwDirection)

Returns an enumerator to list the data formats that the object supports.

#### Parameters

- dwDirection=DATADIR_GET : int

 Indicates whether to return formats that can be queried or set (pythoncom.DATADIR_GET or DATADIR_SET)


<!-- page: PyIDataObject__GetCanonicalFormatEtc_meth.html -->

## PyIDataObject.GetCanonicalFormatEtc

 PyFORMATETC = GetCanonicalFormatEtc(pformatectIn)

Transforms a FORMATECT data description into a general format that the object supports

#### Parameters

- pformatectIn : PyFORMATETC

 Tuple representing a FORMATETC struct describing how the data should be returned


<!-- page: PyIDataObject__GetDataHere_meth.html -->

## PyIDataObject.GetDataHere

 PySTGMEDIUM = GetDataHere(pformatetcIn)

Retunrs a copy of the object's data in specified format

#### Parameters

- pformatetcIn : PyFORMATETC

 Tuple representing a FORMATETC struct describing how the data should be returned


<!-- page: PyIDataObject__GetData_meth.html -->

## PyIDataObject.GetData

 PySTGMEDIUM = GetData(pformatetcIn)

Retrieves data from the object in specified format

#### Parameters

- pformatetcIn : PyFORMATETC

 Tuple representing a FORMATETC struct describing how the data should be returned


<!-- page: PyIDataObject__QueryGetData_meth.html -->

## PyIDataObject.QueryGetData

 QueryGetData(pformatetc)

Checks if the objects supports returning data in a particular format.

#### Parameters

- pformatetc : PyFORMATETC

 Tuple representing a FORMATETC struct describing how the data should be returned

#### Return Value

Returns None if the object supports the specified format, otherwise an error is raised.


<!-- page: PyIDataObject__SetData_meth.html -->

## PyIDataObject.SetData

 SetData(pformatetc, pmedium, fRelease)

Sets the data that the object will return.

#### Parameters

- pformatetc : PyFORMATETC

 Tuple representing a FORMATETC struct describing the type of data to be set

- pmedium : PySTGMEDIUM

 The data to be placed in the object

- fRelease : boolean

 If True, transfers ownership of the data to the object. If False, caller is responsible for releasing the STGMEDIUM.


---

<!-- object: PyIDebugApplication -->


<!-- page: PyIDebugApplication.html -->

---

## PyIDebugApplication Object

 This interface is an extension of PyIRemoteDebugApplication, exposing non-remotable methods for use by language engines and hosts.

#### Methods

- SetName

 Sets the name of the application.

- StepOutComplete

 Called by language engines, in single step mode, just before they return to their caller.

- DebugOutput

 Causes the given string to be displayed by the debugger IDE.

- StartDebugSession

 Causes a default debugger IDE to be started.

- HandleBreakPoint

 Called by the language engine in the context of a thread that has hit a breakpoint.

- Close

 Causes this application to release all references and enter a zombie state.

- GetBreakFlags

 Returns the current break flags for the application.

- GetCurrentThread

 Returns the application thread object associated with the currently running thread.

- CreateAsyncDebugOperation

 Creates an IDebugAsyncOperation object to wrap a provided PyIDebugSyncOperation object.

- AddStackFrameSniffer

 Adds a stack frame sniffer to this application.

- RemoveStackFrameSniffer

 Removes a stack frame sniffer from this application.

- QueryCurrentThreadIsDebuggerThread

 Determines if the current running thread is the debugger thread.

- SynchronousCallInDebuggerThread

 Provides a mechanism for the caller to run code in the debugger thread.

- CreateApplicationNode

 Creates a new application node which is associated with a specific document provider.

- FireDebuggerEvent

 Fire a generic event to the IApplicationDebugger (if any)

- HandleRuntimeError

 Description of HandleRuntimeError

- FCanJitDebug

 Description of FCanJitDebug

- FIsAutoJitDebugEnabled

 Description of FIsAutoJitDebugEnabled

- AddGlobalExpressionContextProvider

 Description of AddGlobalExpressionContextProvider

- RemoveGlobalExpressionContextProvider

 Description of RemoveGlobalExpressionContextProvider


<!-- page: PyIDebugApplication__AddGlobalExpressionContextProvider_meth.html -->

## PyIDebugApplication.AddGlobalExpressionContextProvider

 AddGlobalExpressionContextProvider(pdsfs)

Description of AddGlobalExpressionContextProvider.

#### Parameters

- pdsfs : PyIProvideExpressionContexts

 Description for pdsfs


<!-- page: PyIDebugApplication__AddStackFrameSniffer_meth.html -->

## PyIDebugApplication.AddStackFrameSniffer

 int = AddStackFrameSniffer(pdsfs)

Adds a stack frame sniffer to this application.

#### Parameters

- pdsfs : PyIDebugStackFrameSniffer

 Description for pdsfs

#### Comments

 Generally called by a language engine to expose its stack frames to the debugger. It is possible for other entities to expose stack frames.

#### Return Value

The result is an integer cookie, to be passed to PyIDebugApplication::RemoveStackFrameSniffer


<!-- page: PyIDebugApplication__Close_meth.html -->

## PyIDebugApplication.Close

 Close()

Causes this application to release all references and enter a zombie state.

#### Comments

 Called by the owner of the application generally on shut down.


<!-- page: PyIDebugApplication__CreateApplicationNode_meth.html -->

## PyIDebugApplication.CreateApplicationNode

 PyIDebugApplicationNode = CreateApplicationNode()

Creates a new application node which is associated with a specific document provider.

#### Comments

 Before it is visible, the new node must be attached to a parent node.


<!-- page: PyIDebugApplication__CreateAsyncDebugOperation_meth.html -->

## PyIDebugApplication.CreateAsyncDebugOperation

 CreateAsyncDebugOperation(psdo)

Creates an IDebugAsyncOperation object to wrap a provided PyIDebugSyncOperation object.

#### Parameters

- psdo : PyIDebugSyncOperation

 Description for psdo

#### Comments

 This provides a mechanism for language engines to implement asynchronous expression and evaluation, etc. without having to know the details of synchronization with the debugger thread. See the descriptions for PyIDebugSyncOperation and PyIDebugAsyncOperation for more details.


<!-- page: PyIDebugApplication__DebugOutput_meth.html -->

## PyIDebugApplication.DebugOutput

 DebugOutput(pstr)

Causes the given string to be displayed by the debugger IDE, normally in an output window.

#### Parameters

- pstr : unicode

 Description for pstr

#### Comments

 This mechanism provides the means for a language engine to implement language specific debugging output support. Example: Debug.writeln("Help") in JavaScript.


<!-- page: PyIDebugApplication__FCanJitDebug_meth.html -->

## PyIDebugApplication.FCanJitDebug

 FCanJitDebug()

Description of FCanJitDebug.


<!-- page: PyIDebugApplication__FIsAutoJitDebugEnabled_meth.html -->

## PyIDebugApplication.FIsAutoJitDebugEnabled

 FIsAutoJitDebugEnabled()

Description of FIsAutoJitDebugEnabled.


<!-- page: PyIDebugApplication__FireDebuggerEvent_meth.html -->

## PyIDebugApplication.FireDebuggerEvent

 FireDebuggerEvent(guid, unknown)

Fire a generic event to the IApplicationDebugger (if any)

#### Parameters

- guid : PyIIID

 A GUID.

- unknown : PyIUnknown

 An unknown object.


<!-- page: PyIDebugApplication__GetBreakFlags_meth.html -->

## PyIDebugApplication.GetBreakFlags

 int = GetBreakFlags()

Returns the current break flags for the application.


<!-- page: PyIDebugApplication__GetCurrentThread_meth.html -->

## PyIDebugApplication.GetCurrentThread

 PyIDebugApplicationThread = GetCurrentThread()

Returns the application thread object associated with the currently running thread.


<!-- page: PyIDebugApplication__HandleBreakPoint_meth.html -->

## PyIDebugApplication.HandleBreakPoint

 int = HandleBreakPoint(br)

Called by the language engine in the context of a thread that has hit a breakpoint.

#### Parameters

- br : int

 Break reason - one of the BREAKREASON_* constants.

#### Comments

 This method causes the current thread to block and a notification of the breakpoint to be sent to the debugger IDE. When the debugger IDE resumes the application this method returns with the action to be taken.

 Note: While in the breakpoint the language engine may be called in this thread to do various things such as enumerating stack frames or evaluating expressions.

#### Return Value

The result is the break resume action - one of the BREAKRESUMEACTION contsants.


<!-- page: PyIDebugApplication__HandleRuntimeError_meth.html -->

## PyIDebugApplication.HandleRuntimeError

 HandleRuntimeError(pErrorDebug, pScriptSite)

Description of HandleRuntimeError.

#### Parameters

- pErrorDebug : PyIActiveScriptErrorDebug

 Description for pErrorDebug

- pScriptSite : PyIActiveScriptSite

 Description for pScriptSite


<!-- page: PyIDebugApplication__QueryCurrentThreadIsDebuggerThread_meth.html -->

## PyIDebugApplication.QueryCurrentThreadIsDebuggerThread

 QueryCurrentThreadIsDebuggerThread()

Determines if the current running thread is the debugger thread.

#### Return Value

Returns S_OK if the current running thread is the debugger thread. Otherwise, returns S_FALSE.


<!-- page: PyIDebugApplication__RemoveGlobalExpressionContextProvider_meth.html -->

## PyIDebugApplication.RemoveGlobalExpressionContextProvider

 RemoveGlobalExpressionContextProvider(dwCookie)

Description of RemoveGlobalExpressionContextProvider.

#### Parameters

- dwCookie : int

 Description for dwCookie


<!-- page: PyIDebugApplication__RemoveStackFrameSniffer_meth.html -->

## PyIDebugApplication.RemoveStackFrameSniffer

 RemoveStackFrameSniffer(dwCookie)

Removes a stack frame sniffer from this application.

#### Parameters

- dwCookie : int

 A cookie obtained from PyIDebugApplication::AddStackFrameSniffer


<!-- page: PyIDebugApplication__SetName_meth.html -->

## PyIDebugApplication.SetName

 SetName(pstrName)

Sets the name of the application.

#### Parameters

- pstrName : unicode

 The name of the application.

#### Comments

 The provided name will be returned in subsequent calls to >om PyIRemoteDebugApplication.GetName>.


<!-- page: PyIDebugApplication__StartDebugSession_meth.html -->

## PyIDebugApplication.StartDebugSession

 StartDebugSession()

Causes a default debugger IDE to be started and a debug session to be attached to this application if one does not already exist.

#### Comments

 This is used to implement just-in-time debugging.


<!-- page: PyIDebugApplication__StepOutComplete_meth.html -->

## PyIDebugApplication.StepOutComplete

 StepOutComplete()

Called by language engines, in single step mode, just before they return to their caller.

#### Comments

 The process debug manager uses this opportunity to notify all other script engines that they should break at the first opportunity. This is how cross language step modes are implemented.


<!-- page: PyIDebugApplication__SynchronousCallInDebuggerThread_meth.html -->

## PyIDebugApplication.SynchronousCallInDebuggerThread

 SynchronousCallInDebuggerThread(pptc, dwParam1, dwParam2, dwParam3)

Provides a mechanism for the caller to run code in the debugger thread.

#### Parameters

- pptc : PyIDebugThreadCall

 Description for pptc

- dwParam1 : int

 Description for dwParam1

- dwParam2 : int

 Description for dwParam2

- dwParam3 : int

 Description for dwParam3

#### Comments

 This is generally used so that language engines and hosts can implement free threaded objects on top of their single threaded implementations.


---

<!-- object: PyIDebugApplicationNode -->


<!-- page: PyIDebugApplicationNode.html -->

---

## PyIDebugApplicationNode Object

 Provides the functionality of IDebugDocumentProvider, plus a context within a project tree. Derived from PyIDebugDocumentProvider

#### Methods

- EnumChildren

 Description of EnumChildren

- GetParent

 Description of GetParent

- SetDocumentProvider

 Description of SetDocumentProvider

- Close

 Description of Close

- Attach

 Attach a node to its parent.

- Detach

 Detach a node from its parent.


<!-- page: PyIDebugApplicationNode__Attach_meth.html -->

## PyIDebugApplicationNode.Attach

 Attach(pdanParent)

Attach a node to its parent.

#### Parameters

- pdanParent : PyIDebugApplicationNode

 The parent node. None is not acceptable.


<!-- page: PyIDebugApplicationNode__Close_meth.html -->

## PyIDebugApplicationNode.Close

 Close()

Description of Close.


<!-- page: PyIDebugApplicationNode__Detach_meth.html -->

## PyIDebugApplicationNode.Detach

 Detach()

Detach a node from its parent.


<!-- page: PyIDebugApplicationNode__EnumChildren_meth.html -->

## PyIDebugApplicationNode.EnumChildren

 EnumChildren()

Description of EnumChildren.


<!-- page: PyIDebugApplicationNode__GetParent_meth.html -->

## PyIDebugApplicationNode.GetParent

 PyIDebugApplicationNode = GetParent()

Returns the parent node.


<!-- page: PyIDebugApplicationNode__SetDocumentProvider_meth.html -->

## PyIDebugApplicationNode.SetDocumentProvider

 SetDocumentProvider(pddp)

Description of SetDocumentProvider.

#### Parameters

- pddp : PyIDebugDocumentProvider

 Description for pddp


---

<!-- object: PyIDebugApplicationNodeEvents -->


<!-- page: PyIDebugApplicationNodeEvents.html -->

---

## PyIDebugApplicationNodeEvents Object

 Description of the interface

#### Methods

- onAddChild

 Description of onAddChild

- onRemoveChild

 Description of onRemoveChild

- onDetach

 Description of onDetach

- onAttach

 Description of onAttach


<!-- page: PyIDebugApplicationNodeEvents__onAddChild_meth.html -->

## PyIDebugApplicationNodeEvents.onAddChild

 onAddChild(prddpChild)

Description of onAddChild.

#### Parameters

- prddpChild : PyIDebugApplicationNode

 Description for prddpChild


<!-- page: PyIDebugApplicationNodeEvents__onAttach_meth.html -->

## PyIDebugApplicationNodeEvents.onAttach

 onAttach(prddpParent)

Description of onAttach.

#### Parameters

- prddpParent : PyIDebugApplicationNode

 Description for prddpParent


<!-- page: PyIDebugApplicationNodeEvents__onDetach_meth.html -->

## PyIDebugApplicationNodeEvents.onDetach

 onDetach()

Description of onDetach.


<!-- page: PyIDebugApplicationNodeEvents__onRemoveChild_meth.html -->

## PyIDebugApplicationNodeEvents.onRemoveChild

 onRemoveChild(prddpChild)

Description of onRemoveChild.

#### Parameters

- prddpChild : PyIDebugApplicationNode

 Description for prddpChild


---

<!-- object: PyIDebugApplicationThread -->


<!-- page: PyIDebugApplicationThread.html -->

---

## PyIDebugApplicationThread Object

 Description of the interface

#### Methods

- SynchronousCallIntoThread

 Description of SynchronousCallIntoThread

- QueryIsCurrentThread

 Description of QueryIsCurrentThread

- QueryIsDebuggerThread

 Description of QueryIsDebuggerThread

- QueryIsDebuggerThread

 Description of SetDescription

- QueryIsDebuggerThread

 Description of SetStateString


<!-- page: PyIDebugApplicationThread__QueryIsCurrentThread_meth.html -->

## PyIDebugApplicationThread.QueryIsCurrentThread

 QueryIsCurrentThread()

Description of QueryIsCurrentThread.


<!-- page: PyIDebugApplicationThread__QueryIsDebuggerThread_meth.html -->

## PyIDebugApplicationThread.QueryIsDebuggerThread

 QueryIsDebuggerThread()

Description of QueryIsDebuggerThread.


<!-- page: PyIDebugApplicationThread__SetDescription_meth.html -->

## PyIDebugApplicationThread.SetDescription

 SetDescription()

Description of SetDescription.


<!-- page: PyIDebugApplicationThread__SetStateString_meth.html -->

## PyIDebugApplicationThread.SetStateString

 SetStateString()

Description of SetStateString.


<!-- page: PyIDebugApplicationThread__SynchronousCallIntoThread_meth.html -->

## PyIDebugApplicationThread.SynchronousCallIntoThread

 SynchronousCallIntoThread(pstcb, dwParam1, dwParam2, dwParam3)

Description of SynchronousCallIntoThread.

#### Parameters

- pstcb : PyIDebugThreadCall

 Description for pstcb

- dwParam1 : int

 Description for dwParam1

- dwParam2 : int

 Description for dwParam2

- dwParam3 : int

 Description for dwParam3


---

<!-- object: PyIDebugCodeContext -->


<!-- page: PyIDebugCodeContext.html -->

---

## PyIDebugCodeContext Object

 Description of the interface

#### Methods

- GetDocumentContext

 Description of GetDocumentContext

- SetBreakPoint

 Description of SetBreakPoint


<!-- page: PyIDebugCodeContext__GetDocumentContext_meth.html -->

## PyIDebugCodeContext.GetDocumentContext

 GetDocumentContext()

Description of GetDocumentContext.


<!-- page: PyIDebugCodeContext__SetBreakPoint_meth.html -->

## PyIDebugCodeContext.SetBreakPoint

 SetBreakPoint(bps)

Description of SetBreakPoint.

#### Parameters

- bps : int

 Description for bps


---

<!-- object: PyIDebugDocument -->


<!-- page: PyIDebugDocument.html -->

---

## PyIDebugDocument Object

 The base interface to all debug documents. Derived from PyIDebugDocumentInfo


---

<!-- object: PyIDebugDocumentContext -->


<!-- page: PyIDebugDocumentContext.html -->

---

## PyIDebugDocumentContext Object

 Description of the interface

#### Methods

- GetDocument

 Description of GetDocument

- EnumCodeContexts

 Description of EnumCodeContexts


<!-- page: PyIDebugDocumentContext__EnumCodeContexts_meth.html -->

## PyIDebugDocumentContext.EnumCodeContexts

 EnumCodeContexts()

Description of EnumCodeContexts.


<!-- page: PyIDebugDocumentContext__GetDocument_meth.html -->

## PyIDebugDocumentContext.GetDocument

 GetDocument()

Description of GetDocument.


---

<!-- object: PyIDebugDocumentHelper -->


<!-- page: PyIDebugDocumentHelper.html -->

---

## PyIDebugDocumentHelper Object

 Description of the interface

#### Methods

- Init

 Description of Init

- Attach

 Add the document to the doc tree

- Detach

 Description of Detach

- AddUnicodeText

 Description of AddUnicodeText

- AddDBCSText

 Description of AddDBCSText

- SetDebugDocumentHost

 Description of SetDebugDocumentHost

- AddDeferredText

 Description of AddDeferredText

- DefineScriptBlock

 Description of DefineScriptBlock

- SetDefaultTextAttr

 Description of SetDefaultTextAttr

- SetTextAttributes

 Description of SetTextAttributes

- SetLongName

 Description of SetLongName

- SetShortName

 Description of SetShortName

- SetDocumentAttr

 Description of SetDocumentAttr

- GetDebugApplicationNode

 Description of GetDebugApplicationNode

- GetScriptBlockInfo

 Description of GetScriptBlockInfo

- CreateDebugDocumentContext

 Description of CreateDebugDocumentContext

- BringDocumentToTop

 Description of BringDocumentToTop

- BringDocumentContextToTop

 Description of BringDocumentContextToTop


<!-- page: PyIDebugDocumentHelper__AddDBCSText_meth.html -->

## PyIDebugDocumentHelper.AddDBCSText

 AddDBCSText()

Description of AddDBCSText.


<!-- page: PyIDebugDocumentHelper__AddDeferredText_meth.html -->

## PyIDebugDocumentHelper.AddDeferredText

 AddDeferredText(cChars, dwTextStartCookie)

Description of AddDeferredText.

#### Parameters

- cChars : int

 Description for cChars

- dwTextStartCookie : int

 Description for dwTextStartCookie


<!-- page: PyIDebugDocumentHelper__AddUnicodeText_meth.html -->

## PyIDebugDocumentHelper.AddUnicodeText

 AddUnicodeText(pszText)

Description of AddUnicodeText.

#### Parameters

- pszText : unicode

 Description for pszText


<!-- page: PyIDebugDocumentHelper__Attach_meth.html -->

## PyIDebugDocumentHelper.Attach

 Attach(pddhParent)

Add the document to the doc tree

#### Parameters

- pddhParent : PyIDebugDocumentHelper

 Parent item. If none, this item is top level.


<!-- page: PyIDebugDocumentHelper__BringDocumentContextToTop_meth.html -->

## PyIDebugDocumentHelper.BringDocumentContextToTop

 BringDocumentContextToTop(pddc)

Description of BringDocumentContextToTop.

#### Parameters

- pddc : PyIDebugDocumentContext

 Description for pddc


<!-- page: PyIDebugDocumentHelper__BringDocumentToTop_meth.html -->

## PyIDebugDocumentHelper.BringDocumentToTop

 BringDocumentToTop()

Description of BringDocumentToTop.


<!-- page: PyIDebugDocumentHelper__CreateDebugDocumentContext_meth.html -->

## PyIDebugDocumentHelper.CreateDebugDocumentContext

 CreateDebugDocumentContext(iCharPos, cChars)

Description of CreateDebugDocumentContext.

#### Parameters

- iCharPos : int

 Description for iCharPos

- cChars : int

 Description for cChars


<!-- page: PyIDebugDocumentHelper__DefineScriptBlock_meth.html -->

## PyIDebugDocumentHelper.DefineScriptBlock

 DefineScriptBlock(ulCharOffset, cChars, pas, fScriptlet)

Description of DefineScriptBlock.

#### Parameters

- ulCharOffset : int

 Description for ulCharOffset

- cChars : int

 Description for cChars

- pas : PyIActiveScript

 Description for pas

- fScriptlet : int

 Description for fScriptlet


<!-- page: PyIDebugDocumentHelper__Detach_meth.html -->

## PyIDebugDocumentHelper.Detach

 Detach()

Description of Detach.


<!-- page: PyIDebugDocumentHelper__GetDebugApplicationNode_meth.html -->

## PyIDebugDocumentHelper.GetDebugApplicationNode

 GetDebugApplicationNode()

Description of GetDebugApplicationNode.


<!-- page: PyIDebugDocumentHelper__GetScriptBlockInfo_meth.html -->

## PyIDebugDocumentHelper.GetScriptBlockInfo

 GetScriptBlockInfo(dwSourceContext)

Description of GetScriptBlockInfo.

#### Parameters

- dwSourceContext : int

 Description for dwSourceContext


<!-- page: PyIDebugDocumentHelper__Init_meth.html -->

## PyIDebugDocumentHelper.Init

 Init(pda, pszShortName, pszLongName, docAttr)

Description of Init.

#### Parameters

- pda : PyIDebugApplication

 Description for pda

- pszShortName : unicode

 Description for pszShortName

- pszLongName : unicode

 Description for pszLongName

- docAttr : int

 Description for docAttr


<!-- page: PyIDebugDocumentHelper__SetDebugDocumentHost_meth.html -->

## PyIDebugDocumentHelper.SetDebugDocumentHost

 SetDebugDocumentHost(pddh)

Description of SetDebugDocumentHost.

#### Parameters

- pddh : PyIDebugDocumentHost

 Description for pddh


<!-- page: PyIDebugDocumentHelper__SetDefaultTextAttr_meth.html -->

## PyIDebugDocumentHelper.SetDefaultTextAttr

 SetDefaultTextAttr(staTextAttr)

Description of SetDefaultTextAttr.

#### Parameters

- staTextAttr : int

 Description for staTextAttr


<!-- page: PyIDebugDocumentHelper__SetDocumentAttr_meth.html -->

## PyIDebugDocumentHelper.SetDocumentAttr

 SetDocumentAttr(pszAttributes)

Description of SetDocumentAttr.

#### Parameters

- pszAttributes : int

 Description for pszAttributes


<!-- page: PyIDebugDocumentHelper__SetLongName_meth.html -->

## PyIDebugDocumentHelper.SetLongName

 SetLongName(pszLongName)

Description of SetLongName.

#### Parameters

- pszLongName : unicode

 Description for pszLongName


<!-- page: PyIDebugDocumentHelper__SetShortName_meth.html -->

## PyIDebugDocumentHelper.SetShortName

 SetShortName(pszShortName)

Description of SetShortName.

#### Parameters

- pszShortName : unicode

 Description for pszShortName


<!-- page: PyIDebugDocumentHelper__SetTextAttributes_meth.html -->

## PyIDebugDocumentHelper.SetTextAttributes

 SetTextAttributes(ulCharOffset, obAttr)

Description of SetTextAttributes.

#### Parameters

- ulCharOffset : int

 Description for ulCharOffset

- obAttr : object

 A sequence of attributes.


---

<!-- object: PyIDebugDocumentHost -->


<!-- page: PyIDebugDocumentHost.html -->

---

## PyIDebugDocumentHost Object

 Description of the interface

#### Methods

- GetDeferredText

 Description of GetDeferredText

- GetScriptTextAttributes

 Description of GetScriptTextAttributes

- OnCreateDocumentContext

 Description of OnCreateDocumentContext

- GetPathName

 Description of GetPathName

- GetFileName

 Description of GetFileName

- NotifyChanged

 Description of NotifyChanged


<!-- page: PyIDebugDocumentHost__GetDeferredText_meth.html -->

## PyIDebugDocumentHost.GetDeferredText

 GetDeferredText(dwTextStartCookie, cMaxChars)

Description of GetDeferredText.

#### Parameters

- dwTextStartCookie : int

 Description for dwTextStartCookie

- cMaxChars : int

 Description for cMaxChars


<!-- page: PyIDebugDocumentHost__GetFileName_meth.html -->

## PyIDebugDocumentHost.GetFileName

 GetFileName()

Description of GetFileName.


<!-- page: PyIDebugDocumentHost__GetPathName_meth.html -->

## PyIDebugDocumentHost.GetPathName

 GetPathName()

Description of GetPathName.


<!-- page: PyIDebugDocumentHost__GetScriptTextAttributes_meth.html -->

## PyIDebugDocumentHost.GetScriptTextAttributes

 GetScriptTextAttributes(pstrCode, pstrDelimiter, dwFlags)

Description of GetScriptTextAttributes.

#### Parameters

- pstrCode : unicode

 Description for pstrCode

- pstrDelimiter : unicode

 Description for pstrDelimiter

- dwFlags : int

 Description for dwFlags


<!-- page: PyIDebugDocumentHost__NotifyChanged_meth.html -->

## PyIDebugDocumentHost.NotifyChanged

 NotifyChanged()

Description of NotifyChanged.


<!-- page: PyIDebugDocumentHost__OnCreateDocumentContext_meth.html -->

## PyIDebugDocumentHost.OnCreateDocumentContext

 OnCreateDocumentContext()

Description of OnCreateDocumentContext.


---

<!-- object: PyIDebugDocumentInfo -->


<!-- page: PyIDebugDocumentInfo.html -->

---

## PyIDebugDocumentInfo Object

 Provides information on a document, which may or may not be instantiated.

#### Methods

- GetName

 Returns the specified name for the document.

- GetDocumentClassId

 Returns a CLSID describing the document type.


<!-- page: PyIDebugDocumentInfo__GetDocumentClassId_meth.html -->

## PyIDebugDocumentInfo.GetDocumentClassId

 PyIID = GetDocumentClassId()

Returns a CLSID describing the document type.


<!-- page: PyIDebugDocumentInfo__GetName_meth.html -->

## PyIDebugDocumentInfo.GetName

 GetName()

Returns the specified name for the document.


---

<!-- object: PyIDebugDocumentProvider -->


<!-- page: PyIDebugDocumentProvider.html -->

---

## PyIDebugDocumentProvider Object

 Provides the means for instanciating a document on demand. Derived from PyIDebugDocumentInfo.

#### Methods

- GetDocument

 Causes the document to be instantiated if it does not already exist.


<!-- page: PyIDebugDocumentProvider__GetDocument_meth.html -->

## PyIDebugDocumentProvider.GetDocument

 PyIDebugDocument = GetDocument()

Causes the document to be instantiated if it does not already exist.


---

<!-- object: PyIDebugDocumentText -->


<!-- page: PyIDebugDocumentText.html -->

---

## PyIDebugDocumentText Object

 The interface to a text only debug document. Derived from PyIDebugDocument

#### Methods

- GetDocumentAttributes

 Description of GetDocumentAttributes

- GetSize

 Description of GetSize

- GetPositionOfLine

 Description of GetPositionOfLine

- GetLineOfPosition

 Description of GetLineOfPosition

- GetText

 Description of GetText

- GetPositionOfContext

 Description of GetPositionOfContext

- GetContextOfPosition

 Description of GetContextOfPosition


<!-- page: PyIDebugDocumentText__GetContextOfPosition_meth.html -->

## PyIDebugDocumentText.GetContextOfPosition

 GetContextOfPosition(cCharacterPosition, cNumChars)

Description of GetContextOfPosition.

#### Parameters

- cCharacterPosition : int

 Description for cCharacterPosition

- cNumChars : int

 Description for cNumChars


<!-- page: PyIDebugDocumentText__GetDocumentAttributes_meth.html -->

## PyIDebugDocumentText.GetDocumentAttributes

 GetDocumentAttributes()

Description of GetDocumentAttributes.


<!-- page: PyIDebugDocumentText__GetLineOfPosition_meth.html -->

## PyIDebugDocumentText.GetLineOfPosition

 GetLineOfPosition(cCharacterPosition)

Description of GetLineOfPosition.

#### Parameters

- cCharacterPosition : int

 Description for cCharacterPosition


<!-- page: PyIDebugDocumentText__GetPositionOfContext_meth.html -->

## PyIDebugDocumentText.GetPositionOfContext

 GetPositionOfContext(psc)

Description of GetPositionOfContext.

#### Parameters

- psc : PyIDebugDocumentContext

 Description for psc


<!-- page: PyIDebugDocumentText__GetPositionOfLine_meth.html -->

## PyIDebugDocumentText.GetPositionOfLine

 GetPositionOfLine(cLineNumber)

Description of GetPositionOfLine.

#### Parameters

- cLineNumber : int

 Description for cLineNumber


<!-- page: PyIDebugDocumentText__GetSize_meth.html -->

## PyIDebugDocumentText.GetSize

 GetSize()

Description of GetSize.


<!-- page: PyIDebugDocumentText__GetText_meth.html -->

## PyIDebugDocumentText.GetText

 GetText(cCharacterPosition, cMaxChars, bWantAttr)

Description of GetText.

#### Parameters

- cCharacterPosition : int

- cMaxChars : int

 Max chars to return

- bWantAttr=1 : int

 Should the attributes be returned?


---

<!-- object: PyIDebugDocumentTextAuthor -->


<!-- page: PyIDebugDocumentTextAuthor.html -->

---

## PyIDebugDocumentTextAuthor Object

 This preliminary interface is provided by text documents that support editing. Derived from PyIDebugDocumentText

#### Methods

- InsertText

 Description of InsertText

- RemoveText

 Description of RemoveText

- ReplaceText

 Description of ReplaceText


<!-- page: PyIDebugDocumentTextAuthor__InsertText_meth.html -->

## PyIDebugDocumentTextAuthor.InsertText

 InsertText(cCharacterPosition, cNumToInsert, pcharText)

Description of InsertText.

#### Parameters

- cCharacterPosition : int

 Description for cCharacterPosition

- cNumToInsert : int

 Description for cNumToInsert

- pcharText : unicode

 Description for pcharText


<!-- page: PyIDebugDocumentTextAuthor__RemoveText_meth.html -->

## PyIDebugDocumentTextAuthor.RemoveText

 RemoveText(cCharacterPosition, cNumToRemove)

Description of RemoveText.

#### Parameters

- cCharacterPosition : int

 Description for cCharacterPosition

- cNumToRemove : int

 Description for cNumToRemove


<!-- page: PyIDebugDocumentTextAuthor__ReplaceText_meth.html -->

## PyIDebugDocumentTextAuthor.ReplaceText

 ReplaceText(cCharacterPosition, cNumToReplace, pcharText)

Description of ReplaceText.

#### Parameters

- cCharacterPosition : int

 Description for cCharacterPosition

- cNumToReplace : int

 Description for cNumToReplace

- pcharText : unicode

 Description for pcharText


---

<!-- object: PyIDebugDocumentTextEvents -->


<!-- page: PyIDebugDocumentTextEvents.html -->

---

## PyIDebugDocumentTextEvents Object

 Description of the interface

#### Methods

- onDestroy

 Description of onDestroy

- onInsertText

 Description of onInsertText

- onRemoveText

 Description of onRemoveText

- onReplaceText

 Description of onReplaceText

- onUpdateTextAttributes

 Description of onUpdateTextAttributes

- onUpdateDocumentAttributes

 Description of onUpdateDocumentAttributes


<!-- page: PyIDebugDocumentTextEvents__onDestroy_meth.html -->

## PyIDebugDocumentTextEvents.onDestroy

 onDestroy()

Description of onDestroy.


<!-- page: PyIDebugDocumentTextEvents__onInsertText_meth.html -->

## PyIDebugDocumentTextEvents.onInsertText

 onInsertText(cCharacterPosition, cNumToInsert)

Description of onInsertText.

#### Parameters

- cCharacterPosition : int

 Description for cCharacterPosition

- cNumToInsert : int

 Description for cNumToInsert


<!-- page: PyIDebugDocumentTextEvents__onRemoveText_meth.html -->

## PyIDebugDocumentTextEvents.onRemoveText

 onRemoveText(cCharacterPosition, cNumToRemove)

Description of onRemoveText.

#### Parameters

- cCharacterPosition : int

 Description for cCharacterPosition

- cNumToRemove : int

 Description for cNumToRemove


<!-- page: PyIDebugDocumentTextEvents__onReplaceText_meth.html -->

## PyIDebugDocumentTextEvents.onReplaceText

 onReplaceText(cCharacterPosition, cNumToReplace)

Description of onReplaceText.

#### Parameters

- cCharacterPosition : int

 Description for cCharacterPosition

- cNumToReplace : int

 Description for cNumToReplace


<!-- page: PyIDebugDocumentTextEvents__onUpdateDocumentAttributes_meth.html -->

## PyIDebugDocumentTextEvents.onUpdateDocumentAttributes

 onUpdateDocumentAttributes(textdocattr)

Description of onUpdateDocumentAttributes.

#### Parameters

- textdocattr : int

 Description for textdocattr


<!-- page: PyIDebugDocumentTextEvents__onUpdateTextAttributes_meth.html -->

## PyIDebugDocumentTextEvents.onUpdateTextAttributes

 onUpdateTextAttributes(cCharacterPosition, cNumToUpdate)

Description of onUpdateTextAttributes.

#### Parameters

- cCharacterPosition : int

 Description for cCharacterPosition

- cNumToUpdate : int

 Description for cNumToUpdate


---

<!-- object: PyIDebugDocumentTextExternalAuthor -->


<!-- page: PyIDebugDocumentTextExternalAuthor.html -->

---

## PyIDebugDocumentTextExternalAuthor Object

 Description of the interface

#### Methods

- GetPathName

 Description of GetPathName

- GetFileName

 Description of GetFileName

- NotifyChanged

 Description of NotifyChanged


<!-- page: PyIDebugDocumentTextExternalAuthor__GetFileName_meth.html -->

## PyIDebugDocumentTextExternalAuthor.GetFileName

 GetFileName()

Description of GetFileName.


<!-- page: PyIDebugDocumentTextExternalAuthor__GetPathName_meth.html -->

## PyIDebugDocumentTextExternalAuthor.GetPathName

 GetPathName()

Description of GetPathName.


<!-- page: PyIDebugDocumentTextExternalAuthor__NotifyChanged_meth.html -->

## PyIDebugDocumentTextExternalAuthor.NotifyChanged

 NotifyChanged()

Description of NotifyChanged.


---

<!-- object: PyIDebugExpression -->


<!-- page: PyIDebugExpression.html -->

---

## PyIDebugExpression Object

 Description of the interface

#### Methods

- Start

 Description of Start

- Abort

 Description of Abort

- QueryIsComplete

 Description of QueryIsComplete

- GetResultAsString

 Description of GetResultAsString

- GetResultAsDebugProperties

 Description of GetResultAsDebugProperties


<!-- page: PyIDebugExpression__Abort_meth.html -->

## PyIDebugExpression.Abort

 Abort()

Description of Abort.


<!-- page: PyIDebugExpression__GetResultAsDebugProperties_meth.html -->

## PyIDebugExpression.GetResultAsDebugProperties

 GetResultAsDebugProperties()

Description of GetResultAsDebugProperty.


<!-- page: PyIDebugExpression__GetResultAsString_meth.html -->

## PyIDebugExpression.GetResultAsString

 GetResultAsString()

Description of GetResultAsString.


<!-- page: PyIDebugExpression__QueryIsComplete_meth.html -->

## PyIDebugExpression.QueryIsComplete

 QueryIsComplete()

Description of QueryIsComplete.


<!-- page: PyIDebugExpression__Start_meth.html -->

## PyIDebugExpression.Start

 Start(pdecb)

Description of Start.

#### Parameters

- pdecb : PyIDebugExpressionCallBack

 Description for pdecb


---

<!-- object: PyIDebugExpressionCallBack -->


<!-- page: PyIDebugExpressionCallBack.html -->

---

## PyIDebugExpressionCallBack Object

 Description of the interface

#### Methods

- onComplete

 Description of onComplete


<!-- page: PyIDebugExpressionCallBack__onComplete_meth.html -->

## PyIDebugExpressionCallBack.onComplete

 onComplete()

Description of onComplete.


---

<!-- object: PyIDebugExpressionContext -->


<!-- page: PyIDebugExpressionContext.html -->

---

## PyIDebugExpressionContext Object

 Description of the interface

#### Methods

- ParseLanguageText

 Description of ParseLanguageText

- GetLanguageInfo

 Description of GetLanguageInfo


<!-- page: PyIDebugExpressionContext__GetLanguageInfo_meth.html -->

## PyIDebugExpressionContext.GetLanguageInfo

 GetLanguageInfo()

Description of GetLanguageInfo.


<!-- page: PyIDebugExpressionContext__ParseLanguageText_meth.html -->

## PyIDebugExpressionContext.ParseLanguageText

 ParseLanguageText(pstrCode, nRadix, pstrDelimiter, dwFlags)

Description of ParseLanguageText.

#### Parameters

- pstrCode : unicode

 Description for pstrCode

- nRadix : int

 Description for nRadix

- pstrDelimiter : unicode

 Description for pstrDelimiter

- dwFlags : int

 Description for dwFlags


---

<!-- object: PyIDebugProperty -->


<!-- page: PyIDebugProperty.html -->

---

## PyIDebugProperty Object

 Description of the interface

#### Methods

- GetPropertyInfo

 Description of GetPropertyInfo

- GetExtendedInfo

 Description of GetExtendedInfo

- SetValueAsString

 Description of SetValueAsString

- EnumMembers

 Description of EnumMembers

- GetParent

 Description of GetParent


<!-- page: PyIDebugProperty__EnumMembers_meth.html -->

## PyIDebugProperty.EnumMembers

 EnumMembers(dwFieldSpec, nRadix, refiid)

Description of EnumMembers.

#### Parameters

- dwFieldSpec : int

 Description for dwFieldSpec

- nRadix : int

 Description for nRadix

- refiid : PyIID

 Description for refiid


<!-- page: PyIDebugProperty__GetExtendedInfo_meth.html -->

## PyIDebugProperty.GetExtendedInfo

 GetExtendedInfo()

Description of GetExtendedInfo.


<!-- page: PyIDebugProperty__GetParent_meth.html -->

## PyIDebugProperty.GetParent

 GetParent()

Description of GetParent.


<!-- page: PyIDebugProperty__GetPropertyInfo_meth.html -->

## PyIDebugProperty.GetPropertyInfo

 GetPropertyInfo(dwFieldSpec, nRadix)

Description of GetPropertyInfo.

#### Parameters

- dwFieldSpec : int

 Description for dwFieldSpec

- nRadix : int

 Description for nRadix


<!-- page: PyIDebugProperty__SetValueAsString_meth.html -->

## PyIDebugProperty.SetValueAsString

 SetValueAsString(pszValue, nRadix)

Description of SetValueAsString.

#### Parameters

- pszValue : unicode

 Description for pszValue

- nRadix : int

 Description for nRadix


---

<!-- object: PyIDebugSessionProvider -->


<!-- page: PyIDebugSessionProvider.html -->

---

## PyIDebugSessionProvider Object

 Description of the interface

#### Methods

- StartDebugSession

 Description of StartDebugSession


<!-- page: PyIDebugSessionProvider__StartDebugSession_meth.html -->

## PyIDebugSessionProvider.StartDebugSession

 StartDebugSession(pda)

Description of StartDebugSession.

#### Parameters

- pda : PyIRemoteDebugApplication

 Description for pda


---

<!-- object: PyIDebugStackFrame -->


<!-- page: PyIDebugStackFrame.html -->

---

## PyIDebugStackFrame Object

 Description of the interface

#### Methods

- GetCodeContext

 Returns the current code context associated with the stack frame.

- GetDescriptionString

 Returns a short or long textual description of the stack frame.

- GetLanguageString

 Returns a short or long textual description of the language.

- GetThread

 Returns the thread associated with this stack frame.

- GetThread

 Returns the debug property object associated with this stack frame.


<!-- page: PyIDebugStackFrame__GetCodeContext_meth.html -->

## PyIDebugStackFrame.GetCodeContext

 GetCodeContext()

Returns the current code context associated with the stack frame.


<!-- page: PyIDebugStackFrame__GetDebugProperty_meth.html -->

## PyIDebugStackFrame.GetDebugProperty

 PyIDebugProperty = GetDebugProperty()

Returns the debug property.


<!-- page: PyIDebugStackFrame__GetDescriptionString_meth.html -->

## PyIDebugStackFrame.GetDescriptionString

 unicode = GetDescriptionString(fLong)

Returns a short or long textual description of the stack frame.

#### Parameters

- fLong : int

 If false, provide only the name of the function associated with the stack frame. When true it may also provide the parameter(s) to the function or whatever else is relevant.


<!-- page: PyIDebugStackFrame__GetLanguageString_meth.html -->

## PyIDebugStackFrame.GetLanguageString

 unicode = GetLanguageString(fLong)

Returns a short or long textual description of the language.

#### Parameters

- fLong : int

 If False, just the language name should be provided, eg, "Python". If True a full product description may be provided (eg, "Python X.X ActiveX Debugging Host")


<!-- page: PyIDebugStackFrame__GetThread_meth.html -->

## PyIDebugStackFrame.GetThread

 PyIDebugApplicationThread = GetThread()

Returns the thread associated with this stack frame.


---

<!-- object: PyIDebugStackFrameSniffer -->


<!-- page: PyIDebugStackFrameSniffer.html -->

---

## PyIDebugStackFrameSniffer Object

 Description of the interface

#### Methods

- EnumStackFrames

 Description of EnumStackFrames


<!-- page: PyIDebugStackFrameSniffer__EnumStackFrames_meth.html -->

## PyIDebugStackFrameSniffer.EnumStackFrames

 EnumStackFrames()

Description of EnumStackFrames.


---

<!-- object: PyIDebugStackFrameSnifferEx -->


<!-- page: PyIDebugStackFrameSnifferEx.html -->

---

## PyIDebugStackFrameSnifferEx Object

 Derived from PyIDebugStackFrameSniffer

#### Methods

- EnumStackFramesEx

 Description of EnumStackFramesEx


<!-- page: PyIDebugStackFrameSnifferEx__EnumStackFramesEx_meth.html -->

## PyIDebugStackFrameSnifferEx.EnumStackFramesEx

 EnumStackFramesEx()

Description of EnumStackFrames.


---

<!-- object: PyIDebugSyncOperation -->


<!-- page: PyIDebugSyncOperation.html -->

---

## PyIDebugSyncOperation Object

 Description of the interface

#### Methods

- GetTargetThread

 Description of GetTargetThread

- Execute

 Description of Execute

- InProgressAbort

 Description of InProgressAbort


<!-- page: PyIDebugSyncOperation__Execute_meth.html -->

## PyIDebugSyncOperation.Execute

 Execute()

Description of Execute.


<!-- page: PyIDebugSyncOperation__GetTargetThread_meth.html -->

## PyIDebugSyncOperation.GetTargetThread

 GetTargetThread()

Description of GetTargetThread.


<!-- page: PyIDebugSyncOperation__InProgressAbort_meth.html -->

## PyIDebugSyncOperation.InProgressAbort

 InProgressAbort()

Description of InProgressAbort.


---

<!-- object: PyIDefaultExtractIconInit -->


<!-- page: PyIDefaultExtractIconInit.html -->

---

## PyIDefaultExtractIconInit Object

 Description of the interface

#### Methods

- SetFlags

 Description of SetFlags

- SetKey

 Description of SetKey

- SetNormalIcon

 Description of SetNormalIcon

- SetOpenIcon

 Description of SetOpenIcon

- SetShortcutIcon

 Description of SetShortcutIcon

- SetDefaultIcon

 Description of SetDefaultIcon


<!-- page: PyIDefaultExtractIconInit__SetDefaultIcon_meth.html -->

## PyIDefaultExtractIconInit.SetDefaultIcon

 SetDefaultIcon(pszFile, iIcon)

Description of SetDefaultIcon.

#### Parameters

- pszFile : unicode

 Description for pszFile

- iIcon : int

 Description for iIcon


<!-- page: PyIDefaultExtractIconInit__SetFlags_meth.html -->

## PyIDefaultExtractIconInit.SetFlags

 SetFlags(uFlags)

Description of SetFlags.

#### Parameters

- uFlags : int

 Description for uFlags


<!-- page: PyIDefaultExtractIconInit__SetKey_meth.html -->

## PyIDefaultExtractIconInit.SetKey

 SetKey(hkey)

Description of SetKey.

#### Parameters

- hkey : PyHKEY

 Description for hkey


<!-- page: PyIDefaultExtractIconInit__SetNormalIcon_meth.html -->

## PyIDefaultExtractIconInit.SetNormalIcon

 SetNormalIcon(pszFile, iIcon)

Description of SetNormalIcon.

#### Parameters

- pszFile : unicode

 Description for pszFile

- iIcon : int

 Description for iIcon


<!-- page: PyIDefaultExtractIconInit__SetOpenIcon_meth.html -->

## PyIDefaultExtractIconInit.SetOpenIcon

 SetOpenIcon(pszFile, iIcon)

Description of SetOpenIcon.

#### Parameters

- pszFile : unicode

 Description for pszFile

- iIcon : int

 Description for iIcon


<!-- page: PyIDefaultExtractIconInit__SetShortcutIcon_meth.html -->

## PyIDefaultExtractIconInit.SetShortcutIcon

 SetShortcutIcon(pszFile, iIcon)

Description of SetShortcutIcon.

#### Parameters

- pszFile : unicode

 Description for pszFile

- iIcon : int

 Description for iIcon


---

<!-- object: PyIDirectSound -->


<!-- page: PyIDirectSound.html -->

---

## PyIDirectSound Object

 Description of the interface

#### Methods

- Initialize

 Description of Initialize.

- SetCooperativeLevel

 Description of SetCooperativeLevel.

- CreateSoundBuffer

 Description of CreateSoundBuffer.

- GetCaps

 Description of GetCaps.

- Compact

 Description of Compact.


<!-- page: PyIDirectSound__Compact_meth.html -->

## PyIDirectSound.Compact

 Compact()

The Compact method moves the unused portions of on-board sound memory, if any, to a contiguous block so that the largest portion of free memory will be available.


<!-- page: PyIDirectSound__CreateSoundBuffer_meth.html -->

## PyIDirectSound.CreateSoundBuffer

 CreateSoundBuffer(lpDSCBufferDesc, unk)

The IDirectSound::CreateSoundBuffer method creates a DirectSoundBuffer object to hold a sequence of audio samples.

#### Parameters

- lpDSCBufferDesc : PyDSCBUFFERDESC

 a DSBUFFERDESC structure containing values for the sound buffer being created.

- unk=None : PyIUknown

 The IUnknown for COM aggregation.


<!-- page: PyIDirectSound__GetCaps_meth.html -->

## PyIDirectSound.GetCaps

 GetCaps()

The GetCaps method retrieves the capabilities of the hardware device that is represented by the DirectSound object. See DSCAPS contants .


<!-- page: PyIDirectSound__GetSpeakerConfig_meth.html -->

## PyIDirectSound.GetSpeakerConfig

 GetSpeakerConfig()

The GetSpeakerConfig method retrieves the speaker configuration.


<!-- page: PyIDirectSound__Initialize_meth.html -->

## PyIDirectSound.Initialize

 Initialize(guid)

Description of Initialize.

#### Parameters

- guid : PyIID

 Globally unique identifier (GUID) specifying the sound driver to which this DirectSound object binds. Pass None to select the primary sound driver.


<!-- page: PyIDirectSound__SetCooperativeLevel_meth.html -->

## PyIDirectSound.SetCooperativeLevel

 SetCooperativeLevel(hwnd, level)

The IDirectSound::SetCooperativeLevel method sets the cooperative level of the application for this sound device.

#### Parameters

- hwnd : int

 Window handle to the application or None.

- level : int

 Requested priority level. Specify one of the following values:

| | Level | Description
| |

---

 |

---

| | DSSCL_NORMAL | Sets the application to a fully cooperative status. Most applications should use this level, because it has the smoothest multitasking and resource-sharing behavior.
| | DSSCL_PRIORITY | Sets the application to the priority level. Applications with this cooperative level can call the DirectSoundBuffer.setFormat and DirectSound.compact methods.
| | DSSCL_EXCLUSIVE | Sets the application to the exclusive level. When it has the input focus, the application will be the only one audible (sounds from applications with the DSBCAPS_GLOBALFOCUS flag set will be muted). With this level, it also has all the privileges of the DSSCL_PRIORITY level. DirectSound will restore the hardware format, as specified by the most recent call to the DirectSoundBuffer.setFormat method, once the application gains the input focus. (Note that DirectSound will always restore the wave format, no matter what priority level is set.)
| | DSSCL_WRITEPRIMARY | This is the highest priority level. The application has write access to the primary sound buffers. No secondary sound buffers in any application can be played.


<!-- page: PyIDirectSound__SetSpeakerConfig_meth.html -->

## PyIDirectSound.SetSpeakerConfig

 SetSpeakerConfig(dwSpeakerConfig)

The SetSpeakerConfig method specifies the speaker configuration of the DirectSound object.

#### Parameters

- dwSpeakerConfig : int

 Speaker configuration of the specified DirectSound object. See the DSSPEAKER constants.


---

<!-- object: PyIDirectSoundBuffer -->


<!-- page: PyIDirectSoundBuffer.html -->

---

## PyIDirectSoundBuffer Object

 Description of the interface

#### Methods

- Initialize

 Description of Initialize.

- SetCooperativeLevel

 Description of SetCooperativeLevel.

- GetStatus

 Description of GetStatus.

- GetCaps

 Description of GetCaps.

- Initialize

 Description of GetCaps.

- Restore

 Description of Restore.

- GetCurrentPosition

 Description of GetCaps.

- Play

 Description of GetCaps.

- SetCurrentPosition

 Description of GetCaps.

- Stop

 Description of GetCaps.

- Unlock

 Description of Unlock.

- GetFrequency

 Description of GetCaps.

- GetPan

 Description of GetCaps.

- GetVolume

 Description of GetCaps.

- SetFrequency

 Description of GetCaps.

- SetPan

 Description of GetCaps.

- SetVolume

 Description of GetCaps.


<!-- page: PyIDirectSoundBuffer__GetCaps_meth.html -->

## PyIDirectSoundBuffer.GetCaps

 GetCaps()

Retrieves the capabilities of the DirectSoundBuffer object as a DSBCAPS object.


<!-- page: PyIDirectSoundBuffer__GetCurrentPosition_meth.html -->

## PyIDirectSoundBuffer.GetCurrentPosition

 GetCurrentPosition()

Description of GetCurrentPosition.


<!-- page: PyIDirectSoundBuffer__GetFormat_meth.html -->

## PyIDirectSoundBuffer.GetFormat

 GetFormat()

Description of GetFormat.


<!-- page: PyIDirectSoundBuffer__GetFrequency_meth.html -->

## PyIDirectSoundBuffer.GetFrequency

 GetFrequency()

Description of GetFrequency.


<!-- page: PyIDirectSoundBuffer__GetPan_meth.html -->

## PyIDirectSoundBuffer.GetPan

 GetPan()

Description of GetPan.


<!-- page: PyIDirectSoundBuffer__GetStatus_meth.html -->

## PyIDirectSoundBuffer.GetStatus

 GetStatus()

Retrieves the current status of the sound buffer.


<!-- page: PyIDirectSoundBuffer__GetVolume_meth.html -->

## PyIDirectSoundBuffer.GetVolume

 GetVolume()

Description of GetVolume.


<!-- page: PyIDirectSoundBuffer__Initialize_meth.html -->

## PyIDirectSoundBuffer.Initialize

 Initialize()

Description of Initialize.


<!-- page: PyIDirectSoundBuffer__Play_meth.html -->

## PyIDirectSoundBuffer.Play

 Play()

Description of Play.


<!-- page: PyIDirectSoundBuffer__Restore_meth.html -->

## PyIDirectSoundBuffer.Restore

 Restore()

Restores the memory allocation for a lost sound buffer for the specified DirectSoundBuffer object.


<!-- page: PyIDirectSoundBuffer__SetCurrentPosition_meth.html -->

## PyIDirectSoundBuffer.SetCurrentPosition

 SetCurrentPosition()

Description of SetCurrentPosition.


<!-- page: PyIDirectSoundBuffer__SetFormat_meth.html -->

## PyIDirectSoundBuffer.SetFormat

 SetFormat(format)

Sets the format of the primary sound buffer for the application. Whenever this application has the input focus, DirectSound will set the primary buffer to the specified format.

#### Parameters

- format : WAVEFORMATEX

 A WAVEFORMATEX object that describes the new format for the primary sound buffer.


<!-- page: PyIDirectSoundBuffer__SetFrequency_meth.html -->

## PyIDirectSoundBuffer.SetFrequency

 SetFrequency()

Description of SetFrequency.


<!-- page: PyIDirectSoundBuffer__SetPan_meth.html -->

## PyIDirectSoundBuffer.SetPan

 SetPan()

Description of SetPan.


<!-- page: PyIDirectSoundBuffer__SetVolume_meth.html -->

## PyIDirectSoundBuffer.SetVolume

 SetVolume()

Description of SetVolume.


<!-- page: PyIDirectSoundBuffer__Stop_meth.html -->

## PyIDirectSoundBuffer.Stop

 Stop()

Description of Stop.


<!-- page: PyIDirectSoundBuffer__Update_meth.html -->

## PyIDirectSoundBuffer.Update

 Update()

Description of Update.


---

<!-- object: PyIDirectSoundCapture -->


<!-- page: PyIDirectSoundCapture.html -->

---

## PyIDirectSoundCapture Object

 The methods of the IDirectSoundCapture interface are used to create sound capture buffers.

#### Methods

- Initialize

 Description of Initialize.

- CreateSoundBuffer

 Description of CreateSoundBuffer.

- GetCaps

 Description of GetCaps.


<!-- page: PyIDirectSoundCapture__CreateCaptureBuffer_meth.html -->

## PyIDirectSoundCapture.CreateCaptureBuffer

 CreateCaptureBuffer(lpDSCBufferDesc, unk)

The IDirectSoundCapture::CreateSoundBuffer method creates a DirectSoundBuffer object to hold a sequence of audio samples.

#### Parameters

- lpDSCBufferDesc : PyDSCBUFFERDESC

 a DSCBUFFERDESC structure containing values for the capture buffer being created.

- unk=None : PyIUknown

 The IUnknown for COM aggregation.


<!-- page: PyIDirectSoundCapture__GetCaps_meth.html -->

## PyIDirectSoundCapture.GetCaps

 GetCaps()

The GetCaps method retrieves the capabilities of the hardware device that is represented by the DirectSound object. See DSCAPS contants .


<!-- page: PyIDirectSoundCapture__Initialize_meth.html -->

## PyIDirectSoundCapture.Initialize

 Initialize()

Not normally called directly. Use DirectSoundCaptureCreate instead.


---

<!-- object: PyIDirectSoundCaptureBuffer -->


<!-- page: PyIDirectSoundCaptureBuffer.html -->

---

## PyIDirectSoundCaptureBuffer Object

 The methods of the IDirectSoundCaptureBuffer interface are used to manipulate sound capture buffers.

#### Methods

- Initialize

 Description of GetCaps.

- SetCooperativeLevel

 Description of GetFormat.

- GetStatus

 Description of GetStatus.

- Initialize

 Description of Initialize.

- GetCurrentPosition

 Description of GetCaps.

- Play

 Description of Start.

- Stop

 Description of Stop.

- Unlock

 Description of Update.


<!-- page: PyIDirectSoundCaptureBuffer__GetCaps_meth.html -->

## PyIDirectSoundCaptureBuffer.GetCaps

 GetCaps()

Returns the capabilities of the DirectSound Capture Buffer.


<!-- page: PyIDirectSoundCaptureBuffer__GetCurrentPosition_meth.html -->

## PyIDirectSoundCaptureBuffer.GetCurrentPosition

 GetCurrentPosition()

Returns a tuple of the current capture and read position in the buffer. The capture position is ahead of the read position. These positions are not always identical due to possible buffering of captured data either on the physical device or in the host. The data after the read position up to and including the capture position is not necessarily valid data.


<!-- page: PyIDirectSoundCaptureBuffer__GetFormat_meth.html -->

## PyIDirectSoundCaptureBuffer.GetFormat

 GetFormat()

Retrieves the current format of the sound capture buffer as a WAVEFORMATEX object.


<!-- page: PyIDirectSoundCaptureBuffer__GetStatus_meth.html -->

## PyIDirectSoundCaptureBuffer.GetStatus

 GetStatus()

Retrieves the current status of the sound capture buffer.


<!-- page: PyIDirectSoundCaptureBuffer__Initialize_meth.html -->

## PyIDirectSoundCaptureBuffer.Initialize

 Initialize()

Not normally used. Used IDirectSoundCapture.CreateCaptureBuffer instead.


<!-- page: PyIDirectSoundCaptureBuffer__Start_meth.html -->

## PyIDirectSoundCaptureBuffer.Start

 Start(dwFlags)

The PyIDirectSoundCaptureBuffer::Start method puts the capture buffer into the capture state and begins capturing data into the buffer. If the capture buffer is already in the capture state then the method has no effect.

#### Parameters

- dwFlags=0 : int

 Flags that specify the behavior for the capture buffer when capturing sound data. Possible values for dwFlags can be one of the following: DSCBSTART_LOOPING


<!-- page: PyIDirectSoundCaptureBuffer__Stop_meth.html -->

## PyIDirectSoundCaptureBuffer.Stop

 Stop()

The IDirectSoundCaptureBuffer::Stop method puts the capture buffer into the "stop" state and stops capturing data. If the capture buffer is already in the stop state then the method has no effect.


<!-- page: PyIDirectSoundCaptureBuffer__Update_meth.html -->

## PyIDirectSoundCaptureBuffer.Update

 Update(dwReadCursor, dwReadBytes, dwFlags)

Retrieve data from the capture buffer.

#### Parameters

- dwReadCursor : int

 Offset, in bytes, from the start of the buffer to where the update begins.

- dwReadBytes : int

 Size, in bytes, of the portion of the buffer to update.

- dwFlags=0 : int

 Flags modifying the update event. This value can be 0 or the following flag: DSCBLOCK_ENTIREBUFFER The dwReadBytes parameter is to be ignored and the entire capture buffer is to be locked.


---

<!-- object: PyIDirectSoundNotify -->


<!-- page: PyIDirectSoundNotify.html -->

---

## PyIDirectSoundNotify Object

 Description of the interface

#### Methods

- Initialize

 Description of SetNotificationPositions.


<!-- page: PyIDirectSoundNotify__SetNotificationPositions_meth.html -->

## PyIDirectSoundNotify.SetNotificationPositions

 SetNotificationPositions()

Description of GetCaps.


---

<!-- object: PyIDirectoryObject -->


<!-- page: PyIDirectoryObject.html -->

---

## PyIDirectoryObject Object

 A COM interface to ADSI's IDirectoryObject interface.
Derived from PyIUnknown

#### Methods

- GetObjectInformation

 Retrieves an PyADS_OBJECT_INFO object that contains information about the identity and location of a directory service object.

- GetObjectAttributes

 Gets one or more specified attributes of the directory service object, as defined in the PyADS_ATTR_INFO structure.

- SetObjectAttributes

 Sets one or more specified attributes of the directory service object, as defined in the PyADS_ATTR_INFO structure.

- CreateDSObject

- DeleteDSObject

 Deletes a leaf object in a directory tree


<!-- page: PyIDirectoryObject__CreateDSObject_meth.html -->

## PyIDirectoryObject.CreateDSObject

 PyIDispatch = CreateDSObject(rdn, attrs )

#### Parameters

- rdn : PyUnicode

 The relative distinguished name (relative path) of the object to be created.

- attrs : (PyADS_ATTR_INFO, ...)

 The attributes to set.


<!-- page: PyIDirectoryObject__DeleteDSObject_meth.html -->

## PyIDirectoryObject.DeleteDSObject

 DeleteDSObject(rdn)

Deletes a leaf object in a directory tree

#### Parameters

- rdn : string

 The relative distinguished name (relative path) of the object to be deleted.


<!-- page: PyIDirectoryObject__GetObjectAttributes_meth.html -->

## PyIDirectoryObject.GetObjectAttributes

 (PyADS_ATTR_INFO, ...) = GetObjectAttributes(names)

Gets one or more specified attributes of the directory service object, as defined in the PyADS_ATTR_INFO structure.

#### Parameters

- names : (PyUnicode , ...)


<!-- page: PyIDirectoryObject__GetObjectInformation_meth.html -->

## PyIDirectoryObject.GetObjectInformation

 PyADS_OBJECT_INFO = GetObjectInformation()

Retrieves an PyADS_OBJECT_INFO object that contains information about the identity and location of a directory service object.


<!-- page: PyIDirectoryObject__SetObjectAttributes_meth.html -->

## PyIDirectoryObject.SetObjectAttributes

 int = SetObjectAttributes(attrs)

Sets one or more specified attributes of the directory service object, as defined in the PyADS_ATTR_INFO structure.

#### Parameters

- attrs : (PyADS_ATTR_INFO, ...)

 The attributes to set


---

<!-- object: PyIDirectorySearch -->


<!-- page: PyIDirectorySearch.html -->

---

## PyIDirectorySearch Object

 A COM interface to ADSI's IDirectorySearch interface.
Derived from PyIUnknown

#### Methods

- SetSearchPreference

- ExecuteSearch

 Executes a search and passes the results to the caller. Some providers, such as LDAP, will defer the actual execution until the caller invokes the PyIDirectorySearch::GetFirstRow method or the PyIDirectorySearch::GetNextRow method.

- GetNextRow

- GetFirstRow

- GetPreviousRow

- CloseSearchHandle

 Closes a previously opened search handle.

- AdandonSearch

- GetColumn

- GetNextColumnName


<!-- page: PyIDirectorySearch__AdandonSearch_meth.html -->

## PyIDirectorySearch.AdandonSearch

 AdandonSearch(handle)

#### Parameters

- handle : int


<!-- page: PyIDirectorySearch__CloseSearchHandle_meth.html -->

## PyIDirectorySearch.CloseSearchHandle

 CloseSearchHandle(handle)

Closes a previously opened search handle.

#### Parameters

- handle : int


<!-- page: PyIDirectorySearch__ExecuteSearch_meth.html -->

## PyIDirectorySearch.ExecuteSearch

 int = ExecuteSearch(filter, attrNames )

Executes a search and passes the results to the caller. Some providers, such as LDAP, will defer the actual execution until the caller invokes the PyIDirectorySearch::GetFirstRow method or the PyIDirectorySearch::GetNextRow method.

#### Parameters

- filter : PyUnicode

- attrNames : [PyUnicode , ...]

#### Return Value

The result is an integer search handle. PyIDirectorySearch::CloseSearchHandle should be called to close the handle.


<!-- page: PyIDirectorySearch__GetColumn_meth.html -->

## PyIDirectorySearch.GetColumn

 (name, type, values) = GetColumn(handle, name )

#### Parameters

- handle : int

 Handle to a search

- name : PyUnicode

 The column name to fetch


<!-- page: PyIDirectorySearch__GetFirstRow_meth.html -->

## PyIDirectorySearch.GetFirstRow

 int = GetFirstRow(handle)

#### Parameters

- handle : int

#### Return Value

The result is the HRESULT from the call - no exceptions are thrown


<!-- page: PyIDirectorySearch__GetNextColumnName_meth.html -->

## PyIDirectorySearch.GetNextColumnName

 GetNextColumnName()

#### Return Value

Returns None when the underlying ADSI function return S_ADS_NOMORE_COLUMNS.


<!-- page: PyIDirectorySearch__GetNextRow_meth.html -->

## PyIDirectorySearch.GetNextRow

 int = GetNextRow(handle)

#### Parameters

- handle : int

#### Return Value

The result is the HRESULT from the call - no exceptions are thrown


<!-- page: PyIDirectorySearch__GetPreviousRow_meth.html -->

## PyIDirectorySearch.GetPreviousRow

 int = GetPreviousRow(handle)

#### Parameters

- handle : int

#### Return Value

The result is the HRESULT from the call - no exceptions are thrown


<!-- page: PyIDirectorySearch__SetSearchPreference_meth.html -->

## PyIDirectorySearch.SetSearchPreference

 int, [int, ...] = SetSearchPreference(prefs)

#### Parameters

- prefs : ADS_SEARCHPREF_INFO

#### Return Value

The result is the hresult of the call, and a list of integer status codes for each of the preferences set.


---

<!-- object: PyIDispatch -->


<!-- page: PyIDispatch.html -->

---

## PyIDispatch Object

 A OLE automation client object.

#### Methods

- Invoke

 Invokes a DISPID, using the passed arguments.

- InvokeTypes

 Invokes a DISPID, using the passed arguments and type descriptions.

- GetIDsOfNames

 Get the DISPID for the passed names.

- GetTypeInfo

 Get type information for the object.

- GetTypeInfoCount

 Retrieves the number of PyITypeInfos the object provides.

#### Based On

PyIUnknown


<!-- page: PyIDispatch__GetIDsOfNames_meth.html -->

## PyIDispatch.GetIDsOfNames

 (int, ...)/int = GetIDsOfNames(name)

Get the DISPID for the passed names.

#### Parameters

- name : string

 A name to query for

#### Alternative Parameters

- [name, ...]

 A sequence of string names to query

#### Comments

 Currently the LCID can not be specified, and LOCALE_SYSTEM_DEFAULT is used.

#### Return Value

If the first parameter is a sequence, the result will be a tuple of integers for each name in the sequence. If the first parameter is a single string, the result is a single integer with the ID of requested item.


<!-- page: PyIDispatch__GetTypeInfoCount_meth.html -->

## PyIDispatch.GetTypeInfoCount

 int = GetTypeInfoCount()

Retrieves the number of PyITypeInfos the object provides.


<!-- page: PyIDispatch__GetTypeInfo_meth.html -->

## PyIDispatch.GetTypeInfo

 PyITypeInfo = GetTypeInfo(locale, index )

Get type information for the object.

#### Parameters

- locale=LOCALE_USER_DEFAULT : int

 The locale to use.

- index=0 : int

 The index of the typelibrary to fetch. Note that these params are reversed from the win32 call.


<!-- page: PyIDispatch__InvokeTypes_meth.html -->

## PyIDispatch.InvokeTypes

 object = InvokeTypes(dispid, lcid , wFlags , resultTypeDesc , typeDescs , args )

Invokes a DISPID, using the passed arguments and type descriptions.

#### Parameters

- dispid : int

 The dispid to use. Please see PyIDispatch::Invoke.

- lcid : int

 The locale ID. Please see PyIDispatch::Invoke.

- wFlags : int

 Flags for the call. Please see PyIDispatch::Invoke.

- resultTypeDesc : tuple

 A tuple describing the type of the result. See the comments for more information.

- typeDescs : (tuple, ...)

 A sequence of tuples describing the types of the parameters for the function. See the comments for more information.

- args : object, ...

 The args to the function.

#### Comments

 The Microsoft documentation for IDispatch should be used for all params except 'resultTypeDesc' and 'typeDescs'. 'resultTypeDesc' describes the return value of the function, and is a tuple of (type_id, flags). 'typeDescs' describes the type of each parameters, and is a list of the same (type_id, flags) tuple.

| | item | Description
| |

---

 |

---

| | type_id | A valid "variant type" constant (eg, VT_I4 | VT_ARRAY, VT_DATE, etc - see VARIANT at MSDN).
| | flags | One of the PARAMFLAG constants (eg, PARAMFLAG_FIN, PARAMFLAG_FOUT etc - see PARAMFLAG at MSDN).

#### Example

An example from the makepy generated file for Word

```
class Cells(DispatchBaseClass):



...



    def SetWidth(self, ColumnWidth=..., RulerStyle=...):



	return self._oleobj_.InvokeTypes(202, LCID, 1, (24, 0), ((4, 1), (3, 1)),...)




```

 The interesting bits are

```
resultTypeDesc: (24, 0) - (VT_VOID, <no flags>)



typeDescs: ((4, 1), (3, 1)) - ((VT_R4, PARAMFLAG_FIN), (VT_I4, PARAMFLAG_FIN))




```

 So, in this example, the function returns no value and takes 2 "in" params - ColumnWidth is a float, and RulerStule is an int.

```





```


<!-- page: PyIDispatch__Invoke_meth.html -->

## PyIDispatch.Invoke

 object = Invoke(dispid, lcid , flags , bResultWanted , params, ... )

Invokes a DISPID, using the passed arguments.

#### Parameters

- dispid : int

 The dispid to use. Typically this value will come from PyIDispatch::GetIDsOfNames or from a type library.

- lcid : int

 The locale id to use.

- flags : int

 The flags for the call. The following flags can be used.

| | Flag | Description
| |

---

 |

---

| | DISPATCH_METHOD | The member is invoked as a method. If a property has the same name, both this and the DISPATCH_PROPERTYGET flag may be set.
| | DISPATCH_PROPERTYGET | The member is retrieved as a property or data member.
| | DISPATCH_PROPERTYPUT | The member is changed as a property or data member.
| | DISPATCH_PROPERTYPUTREF | The member is changed by a reference assignment, rather than a value assignment. This flag is valid only when the property accepts a reference to an object.
- bResultWanted : int

 Indicates if the result of the call should be requested.

- params, ... : object, ...

 The parameters to pass.

#### Return Value

If the bResultWanted parameter is False, then the result will be None. Otherwise, the result is determined by the COM object itself (and may still be None)


---

<!-- object: PyIDispatchEx -->


<!-- page: PyIDispatchEx.html -->

---

## PyIDispatchEx Object

 A OLE automation client object that uses the IDispatchEx scripting interface..

#### Methods

- GetDispID

- InvokeEx

 Provides access to properties and methods exposed by a PyIDispatchEx object.

- DeleteMemberByName

- DeleteMemberByDispID

- GetMemberProperties

- GetMemberName

 Returns the name associated with a member id

- GetNextDispID

 Enumerates member ids.

#### Based On

PyIDispatch


<!-- page: PyIDispatchEx__DeleteMemberByDispID_meth.html -->

## PyIDispatchEx.DeleteMemberByDispID

 DeleteMemberByDispID(dispid)

#### Parameters

- dispid : int


<!-- page: PyIDispatchEx__DeleteMemberByName_meth.html -->

## PyIDispatchEx.DeleteMemberByName

 DeleteMemberByName(name, fdex)

#### Parameters

- name : PyUnicode

 Passed in name to be mapped

- fdex : int

 Determines the options


<!-- page: PyIDispatchEx__GetDispID_meth.html -->

## PyIDispatchEx.GetDispID

 int = GetDispID(name, fdex )

Returns the member id for a name

#### Parameters

- name : PyUnicode

 Passed in name to be mapped

- fdex : int

 Determines the options for obtaining the member identifier. This can be a combination of the fdex* constants:


<!-- page: PyIDispatchEx__GetMemberName_meth.html -->

## PyIDispatchEx.GetMemberName

 str = GetMemberName(dispid)

Returns the name associated with a member id

#### Parameters

- dispid : int

 The member id


<!-- page: PyIDispatchEx__GetMemberProperties_meth.html -->

## PyIDispatchEx.GetMemberProperties

 int = GetMemberProperties(dispid, fdex )

Returns mask of fdex* flags describing a member

#### Parameters

- dispid : int

 The member id

- fdex : int

 fdex* flags specifying which properties to return


<!-- page: PyIDispatchEx__GetNextDispID_meth.html -->

## PyIDispatchEx.GetNextDispID

 int = GetNextDispID(fdex, dispid )

Enumerates member ids.

#### Parameters

- fdex : int

 Determines the options

- dispid : int

 Current member, or DISPID_STARTENUM to begin enumeration. GetNextDispID will retrieve the item in the enumeration after this one.


<!-- page: PyIDispatchEx__InvokeEx_meth.html -->

## PyIDispatchEx.InvokeEx

 object = InvokeEx(dispid, lcid , flags , args , types , returnDesc , serviceProvider )

Provides access to properties and methods exposed by a PyIDispatchEx object.

#### Parameters

- dispid : int

- lcid : int

- flags : int

- args : [object, ...]

 The arguments.

- types=None : [object, ...]

 A tuple of type description object, or None if type descriptions are not available.

- returnDesc=1 : object|int

 If types==None, should be a BOOL indicating if the result is needed. If types is a tuple, then should a be type description.

- serviceProvider=None : PyIServiceProvider

 A service provider object supplied by the caller which allows the object to obtain services from the caller. Can be None.


---

<!-- object: PyIDisplayItem -->


<!-- page: PyIDisplayItem.html -->

---

## PyIDisplayItem Object

 Description of the interface

#### Based On

PyIRelatedItem


---

<!-- object: PyIDocHostUIHandler -->


<!-- page: PyIDocHostUIHandler.html -->

---

## PyIDocHostUIHandler Object

 Description of the interface

#### Methods

- ShowContextMenu

 Description of ShowContextMenu

- GetHostInfo

 Description of GetHostInfo

- ShowUI

 Description of ShowUI

- HideUI

 Description of HideUI

- UpdateUI

 Description of UpdateUI

- EnableModeless

 Description of EnableModeless

- OnDocWindowActivate

 Description of OnDocWindowActivate

- OnFrameWindowActivate

 Description of OnFrameWindowActivate

- ResizeBorder

 Description of ResizeBorder

- TranslateAccelerator

 Description of TranslateAccelerator

- GetOptionKeyPath

 Description of GetOptionKeyPath

- GetDropTarget

 Description of GetDropTarget

- GetExternal

 Description of GetExternal

- TranslateUrl

 Description of TranslateUrl

- FilterDataObject

 Description of FilterDataObject


<!-- page: PyIDocHostUIHandler__EnableModeless_meth.html -->

## PyIDocHostUIHandler.EnableModeless

 EnableModeless(fEnable)

Description of EnableModeless.

#### Parameters

- fEnable : int

 Description for fEnable


<!-- page: PyIDocHostUIHandler__FilterDataObject_meth.html -->

## PyIDocHostUIHandler.FilterDataObject

 FilterDataObject(pDO)

Description of FilterDataObject.

#### Parameters

- pDO : PyIDataObject

 Description for pDO


<!-- page: PyIDocHostUIHandler__GetDropTarget_meth.html -->

## PyIDocHostUIHandler.GetDropTarget

 GetDropTarget(pDropTarget)

Description of GetDropTarget.

#### Parameters

- pDropTarget : PyIDropTarget

 Description for pDropTarget


<!-- page: PyIDocHostUIHandler__GetExternal_meth.html -->

## PyIDocHostUIHandler.GetExternal

 GetExternal()

Description of GetExternal.


<!-- page: PyIDocHostUIHandler__GetHostInfo_meth.html -->

## PyIDocHostUIHandler.GetHostInfo

 GetHostInfo()

Description of GetHostInfo.


<!-- page: PyIDocHostUIHandler__GetOptionKeyPath_meth.html -->

## PyIDocHostUIHandler.GetOptionKeyPath

 GetOptionKeyPath(dw)

Description of GetOptionKeyPath.

#### Parameters

- dw : int

 Description for dw


<!-- page: PyIDocHostUIHandler__HideUI_meth.html -->

## PyIDocHostUIHandler.HideUI

 HideUI()

Description of HideUI.


<!-- page: PyIDocHostUIHandler__OnDocWindowActivate_meth.html -->

## PyIDocHostUIHandler.OnDocWindowActivate

 OnDocWindowActivate(fActivate)

Description of OnDocWindowActivate.

#### Parameters

- fActivate : int

 Description for fActivate


<!-- page: PyIDocHostUIHandler__OnFrameWindowActivate_meth.html -->

## PyIDocHostUIHandler.OnFrameWindowActivate

 OnFrameWindowActivate(fActivate)

Description of OnFrameWindowActivate.

#### Parameters

- fActivate : int

 Description for fActivate


<!-- page: PyIDocHostUIHandler__ResizeBorder_meth.html -->

## PyIDocHostUIHandler.ResizeBorder

 ResizeBorder(prcBorder, pUIWindow, fRameWindow)

Description of ResizeBorder.

#### Parameters

- prcBorder : (int, int, int, int)

 Description for prcBorder

- pUIWindow : PyIOleInPlaceUIWindow

 Description for pUIWindow

- fRameWindow : int

 Description for fRameWindow


<!-- page: PyIDocHostUIHandler__ShowContextMenu_meth.html -->

## PyIDocHostUIHandler.ShowContextMenu

 ShowContextMenu(dwID, pt, pcmdtReserved, pdispReserved)

Description of ShowContextMenu.

#### Parameters

- dwID : int

 Description for dwID

- pt : (int, int)

 Description for ppt

- pcmdtReserved : PyIUnknown

 Description for pcmdtReserved

- pdispReserved : PyIDispatch

 Description for pdispReserved


<!-- page: PyIDocHostUIHandler__ShowUI_meth.html -->

## PyIDocHostUIHandler.ShowUI

 ShowUI(dwID, pActiveObject, pCommandTarget, pFrame, pDoc)

Description of ShowUI.

#### Parameters

- dwID : int

 Description for dwID

- pActiveObject : PyIOleInPlaceActiveObject

 Description for pActiveObject

- pCommandTarget : PyIOleCommandTarget

 Description for pCommandTarget

- pFrame : PyIOleInPlaceFrame

 Description for pFrame

- pDoc : PyIOleInPlaceUIWindow

 Description for pDoc


<!-- page: PyIDocHostUIHandler__TranslateAccelerator_meth.html -->

## PyIDocHostUIHandler.TranslateAccelerator

 TranslateAccelerator(lpMsg, pguidCmdGroup, nCmdID)

Description of TranslateAccelerator.

#### Parameters

- lpMsg : PyLPMSG

 Description for lpMsg

- pguidCmdGroup : PyIID

 Description for pguidCmdGroup

- nCmdID : int

 Description for nCmdID


<!-- page: PyIDocHostUIHandler__TranslateUrl_meth.html -->

## PyIDocHostUIHandler.TranslateUrl

 TranslateUrl(dwTranslate, pchURLIn)

Description of TranslateUrl.

#### Parameters

- dwTranslate : int

 Description for dwTranslate

- pchURLIn : unicode

 Description for pchURLIn


<!-- page: PyIDocHostUIHandler__UpdateUI_meth.html -->

## PyIDocHostUIHandler.UpdateUI

 UpdateUI()

Description of UpdateUI.


---

<!-- object: PyIDropSource -->


<!-- page: PyIDropSource.html -->

---

## PyIDropSource Object

 Description of the interface

#### Methods

- QueryContinueDrag

 Description of QueryContinueDrag

- GiveFeedback

 Description of GiveFeedback


<!-- page: PyIDropSource__GiveFeedback_meth.html -->

## PyIDropSource.GiveFeedback

 GiveFeedback(dwEffect)

Description of GiveFeedback.

#### Parameters

- dwEffect : int

 Description for dwEffect


<!-- page: PyIDropSource__QueryContinueDrag_meth.html -->

## PyIDropSource.QueryContinueDrag

 QueryContinueDrag(fEscapePressed, grfKeyState)

Description of QueryContinueDrag.

#### Parameters

- fEscapePressed : int

 Description for fEscapePressed

- grfKeyState : int

 Description for grfKeyState


---

<!-- object: PyIDropTarget -->


<!-- page: PyIDropTarget.html -->

---

## PyIDropTarget Object

 Interface that acts as a target of OLE drag and drop operations

#### Methods

- DragEnter

 Called when an object is initially dragged into a window

- DragOver

 Called as the dragged object moves over the window

- DragLeave

 Called as the object is dragged back out of the window

- Drop

 Called when the object is dropped onto the window


<!-- page: PyIDropTarget__DragEnter_meth.html -->

## PyIDropTarget.DragEnter

 int = DragEnter(pDataObj, grfKeyState , pt , pdwEffect )

Called when an object is initially dragged into a window

#### Parameters

- pDataObj : PyIDataObject

 IDataObject interface that contains the object being dragged

- grfKeyState : int

 Combination of win32con.MK_* flags containing keyboard modifier state

- pt : (int, int)

 (x,y) Screen coordinates of cursor

- pdwEffect : int

 shellcon.DROPEFFECT_* value

#### Return Value

Your implementation of this function should return a shellcon.DROPEFFECT_* value indicating if the object can be accepted


<!-- page: PyIDropTarget__DragLeave_meth.html -->

## PyIDropTarget.DragLeave

 DragLeave()

Called as the object is dragged back out of the window


<!-- page: PyIDropTarget__DragOver_meth.html -->

## PyIDropTarget.DragOver

 int = DragOver(grfKeyState, pt , pdwEffect )

Called as the dragged object moves over the window

#### Parameters

- grfKeyState : int

 Combination of win32con.MK_* flags containing keyboard modifier state

- pt : (int, int)

 (x,y) Screen coordinates of cursor

- pdwEffect : int

 shellcon.DROPEFFECT_* value

#### Return Value

Your implementation of this function should return a shellcon.DROPEFFECT_* value indicating if the object can be accepted at the current position


<!-- page: PyIDropTarget__Drop_meth.html -->

## PyIDropTarget.Drop

 int = Drop(pDataObj, grfKeyState , pt , dwEffect )

Called when the object is dropped onto the window

#### Parameters

- pDataObj : PyIDataObject

 IDataObject interface containing the dropped object

- grfKeyState : int

 Combination of win32con.MK_* flags containing keyboard modifier state

- pt : (int, int)

 (x,y) Screen coordinates of cursor

- dwEffect : int

 shellcon.DROPEFFECT_* value

#### Return Value

Your implementation of this function should return one of the shellcon.DROPEFFECT_* values


---

<!-- object: PyIDropTargetHelper -->


<!-- page: PyIDropTargetHelper.html -->

---

## PyIDropTargetHelper Object

 Description of the interface

#### Methods

- DragEnter

 Description of DragEnter

- DragOver

 Description of DragOver

- DragLeave

 Description of DragLeave

- Drop

 Description of Drop


<!-- page: PyIDropTargetHelper__DragEnter_meth.html -->

## PyIDropTargetHelper.DragEnter

 DragEnter(hwnd, pDataObj, pt, dwEffect)

Description of DragEnter.

#### Parameters

- hwnd : PyHANDLE

 Handle to target window

- pDataObj : PyIDataObject

 Object that is dragged onto the window

- pt : (int, int)

 Coordinates where drag operation entered the window

- dwEffect : int

 One of shellcon.DROPEFFECT_* values


<!-- page: PyIDropTargetHelper__DragLeave_meth.html -->

## PyIDropTargetHelper.DragLeave

 DragLeave()

Description of DragLeave.


<!-- page: PyIDropTargetHelper__DragOver_meth.html -->

## PyIDropTargetHelper.DragOver

 DragOver(hwnd, pt, pdwEffect)

Description of DragOver.

#### Parameters

- hwnd : int

- pt : (int, int)

 Description for pt

- pdwEffect : int

 Description for pdwEffect


<!-- page: PyIDropTargetHelper__Drop_meth.html -->

## PyIDropTargetHelper.Drop

 Drop(pDataObj, pt, dwEffect)

Description of Drop.

#### Parameters

- pDataObj : PyIDataObject

 Description for pDataObj

- pt : (int, int)

 Description for pt

- dwEffect : int

 Description for dwEffect


---

<!-- object: PyIDsObjectPicker -->


<!-- page: PyIDsObjectPicker.html -->

---

## PyIDsObjectPicker Object

 A COM interface to ADSI's IDsObjectPicker interface.
Derived from PyIUnknown

#### Methods

- Initialize

 Initializes the IDsObjectPicker interface with information about the scopes, filters, and options used by the object picker dialog box.

- InvokeDialog

 Displays a modal object picker dialog box and returns the user's selections.


<!-- page: PyIDsObjectPicker__Initialize_meth.html -->

## PyIDsObjectPicker.Initialize

 Initialize(targetComputer, scopeInfos, options, attrNames)

Initializes the IDsObjectPicker interface with information about the scopes, filters, and options used by the object picker dialog box.

#### Parameters

- targetComputer : PyUnicode

- scopeInfos : PyDSOP_SCOPE_INIT_INFOs

- options=0 : int

- attrNames=None : [PyUnicode , ...]


<!-- page: PyIDsObjectPicker__InvokeDialog_meth.html -->

## PyIDsObjectPicker.InvokeDialog

 PyIDataObject = InvokeDialog(hwnd)

Displays a modal object picker dialog box and returns the user's selections.

#### Parameters

- hwnd : int


---

<!-- object: PyIEmptyVolumeCache -->


<!-- page: PyIEmptyVolumeCache.html -->

---

## PyIEmptyVolumeCache Object

 Used for cleaning up temporary file ("disk cleanup")

#### Comments

 This is a "gateway" object only - you can only implement this interface - see the shell/demos/server/empty_volume_cache.py. The methods described here are the methods you must implement - you can't call them.
Please contribute to these docs!

#### Methods

- PyIEmptyVolumeCache

 Initialize

- PyIEmptyVolumeCache

 GetSpaceUsed

- PyIEmptyVolumeCache

 Purge

- PyIEmptyVolumeCache

 ShowProperties

- PyIEmptyVolumeCache2

 InitializeEx

 Gateway Implementation


<!-- page: PyIEmptyVolumeCache__Deactivate_meth.html -->

## PyIEmptyVolumeCache.Deactivate

 Deactivate()


<!-- page: PyIEmptyVolumeCache__GetSpaceUsed_meth.html -->

## PyIEmptyVolumeCache.GetSpaceUsed

 GetSpaceUsed()


<!-- page: PyIEmptyVolumeCache__Initialize_meth.html -->

## PyIEmptyVolumeCache.Initialize

 Initialize()


<!-- page: PyIEmptyVolumeCache__Purge_meth.html -->

## PyIEmptyVolumeCache.Purge

 Purge()


<!-- page: PyIEmptyVolumeCache__ShowProperties_meth.html -->

## PyIEmptyVolumeCache.ShowProperties

 ShowProperties()


---

<!-- object: PyIEmptyVolumeCache2 -->


<!-- page: PyIEmptyVolumeCache2.html -->

---

## PyIEmptyVolumeCache2 Object

 See also PyIEmptyVolumeCache

#### Methods

- PyIEmptyVolumeCache

 Deactivate


<!-- page: PyIEmptyVolumeCache2__InitializeEx_meth.html -->

## PyIEmptyVolumeCache2.InitializeEx

 InitializeEx()


---

<!-- object: PyIEmptyVolumeCacheCallBack -->


<!-- page: PyIEmptyVolumeCacheCallBack.html -->

---

## PyIEmptyVolumeCacheCallBack Object

 Callback used by PyIEmptyVolumeCacheCallBack

#### Methods

- ScanProgress

 Description of ScanProgress

- PurgeProgress

 Description of PurgeProgress


<!-- page: PyIEmptyVolumeCacheCallBack__PurgeProgress_meth.html -->

## PyIEmptyVolumeCacheCallBack.PurgeProgress

 PurgeProgress(dwlSpaceFreed, spaceFreed, spaceToFree, flags, status)

Description of PurgeProgress.

#### Parameters

- dwlSpaceFreed : PyDWORDLONG

 Description for dwlSpaceFreed

- spaceFreed : long

- spaceToFree : long

- flags : long

- status : unicode


<!-- page: PyIEmptyVolumeCacheCallBack__ScanProgress_meth.html -->

## PyIEmptyVolumeCacheCallBack.ScanProgress

 ScanProgress(dwlSpaceUsed, dwFlags, pcwszStatus)

Description of ScanProgress.

#### Parameters

- dwlSpaceUsed : long

 Description for dwlSpaceUsed

- dwFlags : int

 Description for dwFlags

- pcwszStatus : unicode

 Description for pcwszStatus


---

<!-- object: PyIEnumCATEGORYINFO -->


<!-- page: PyIEnumCATEGORYINFO.html -->

---

## PyIEnumCATEGORYINFO Object

 A Python interface to IEnumCATEGORYINFO

#### Methods

- Next

 Retrieves a specified number of items in the enumeration sequence.

- Skip

 Skips over the next specified elementes.

- Reset

 Resets the enumeration sequence to the beginning.

- Clone

 Creates another enumerator that contains the same enumeration state as the current one.

#### Based On

PyIUnknown


<!-- page: PyIEnumCATEGORYINFO__Clone_meth.html -->

## PyIEnumCATEGORYINFO.Clone

 PyIEnumCATEGORYINFO = Clone()

Creates another enumerator that contains the same enumeration state as the current one


<!-- page: PyIEnumCATEGORYINFO__Next_meth.html -->

## PyIEnumCATEGORYINFO.Next

 ( (PyIID, int, string), ...) = Next(num)

Retrieves a specified number of items in the enumeration sequence.

#### Parameters

- num=1 : int

 Number of items to retrieve.

#### Return Value

The result is a tuple of (IID object, LCID, string description) tuples, one for each element returned.


<!-- page: PyIEnumCATEGORYINFO__Reset_meth.html -->

## PyIEnumCATEGORYINFO.Reset

 Reset()

Resets the enumeration sequence to the beginning.


<!-- page: PyIEnumCATEGORYINFO__Skip_meth.html -->

## PyIEnumCATEGORYINFO.Skip

 Skip(num)

Skips over the next specified elementes.

#### Parameters

- num : int

 The number of elements being requested.


---

<!-- object: PyIEnumConnectionPoints -->


<!-- page: PyIEnumConnectionPoints.html -->

---

## PyIEnumConnectionPoints Object

 A Python interface to IEnumConnectionPoints

#### Methods

- Next

 Retrieves a specified number of items in the enumeration sequence.

- Skip

 Skips over the next specified elementes.

- Reset

 Resets the enumeration sequence to the beginning.

- Clone

 Creates another enumerator that contains the same enumeration state as the current one.

#### Based On

PyIUnknown


<!-- page: PyIEnumConnectionPoints__Clone_meth.html -->

## PyIEnumConnectionPoints.Clone

 PyIEnumConnectionPoints = Clone()

Creates another enumerator that contains the same enumeration state as the current one


<!-- page: PyIEnumConnectionPoints__Next_meth.html -->

## PyIEnumConnectionPoints.Next

 (PyIConnectionPoint, ...) = Next(num)

Retrieves a specified number of items in the enumeration sequence.

#### Parameters

- num=1 : int

 Number of items to retrieve.


<!-- page: PyIEnumConnectionPoints__Reset_meth.html -->

## PyIEnumConnectionPoints.Reset

 Reset()

Resets the enumeration sequence to the beginning.


<!-- page: PyIEnumConnectionPoints__Skip_meth.html -->

## PyIEnumConnectionPoints.Skip

 Skip()

Skips over the next specified elementes.


---

<!-- object: PyIEnumConnections -->


<!-- page: PyIEnumConnections.html -->

---

## PyIEnumConnections Object

 A Python interface to IEnumConnections

#### Methods

- Next

 Retrieves a specified number of items in the enumeration sequence.

- Skip

 Skips over the next specified elementes.

- Reset

 Resets the enumeration sequence to the beginning.

- Clone

 Creates another enumerator that contains the same enumeration state as the current one.

#### Based On

PyIUnknown


<!-- page: PyIEnumConnections__Clone_meth.html -->

## PyIEnumConnections.Clone

 PyIEnumConnections = Clone()

Creates another enumerator that contains the same enumeration state as the current one


<!-- page: PyIEnumConnections__Next_meth.html -->

## PyIEnumConnections.Next

 object = Next(num)

Retrieves a specified number of items in the enumeration sequence.

#### Parameters

- num=1 : int

 Number of items to retrieve.


<!-- page: PyIEnumConnections__Reset_meth.html -->

## PyIEnumConnections.Reset

 Reset()

Resets the enumeration sequence to the beginning.


<!-- page: PyIEnumConnections__Skip_meth.html -->

## PyIEnumConnections.Skip

 Skip()

Skips over the next specified elementes.


---

<!-- object: PyIEnumContextProps -->


<!-- page: PyIEnumContextProps.html -->

---

## PyIEnumContextProps Object

 A Python interface to IEnumContextProps

#### Methods

- Next

 Retrieves a specified number of items in the enumeration sequence.

- Skip

 Skips over the next specified elementes.

- Reset

 Resets the enumeration sequence to the beginning.

- Clone

 Creates another enumerator that contains the same enumeration state as the current one.


<!-- page: PyIEnumContextProps__Clone_meth.html -->

## PyIEnumContextProps.Clone

 PyIEnumContextProps = Clone()

Creates another enumerator that contains the same enumeration state as the current one


<!-- page: PyIEnumContextProps__Next_meth.html -->

## PyIEnumContextProps.Next

 ((PyIID, int, PyIUnknown), ...) = Next(num)

Retrieves a specified number of items in the enumeration sequence.

#### Parameters

- num=1 : int

 Number of items to retrieve.

#### Return Value

Returns a tuple of 3-tuples representing ContextProperty structs:
 First item is GUID identifying the property, second is Flags (reserved), third is the interface set as the property value


<!-- page: PyIEnumContextProps__Reset_meth.html -->

## PyIEnumContextProps.Reset

 Reset()

Resets the enumeration sequence to the beginning.


<!-- page: PyIEnumContextProps__Skip_meth.html -->

## PyIEnumContextProps.Skip

 Skip()

Skips over the next specified elementes.


---

<!-- object: PyIEnumDebugApplicationNodes -->


<!-- page: PyIEnumDebugApplicationNodes.html -->

---

## PyIEnumDebugApplicationNodes Object

 A Python interface to IEnumDebugApplicationNodes

#### Methods

- Next

 Retrieves a specified number of items in the enumeration sequence.

- Skip

 Skips over the next specified elementes.

- Reset

 Resets the enumeration sequence to the beginning.

- Clone

 Creates another enumerator that contains the same enumeration state as the current one.


<!-- page: PyIEnumDebugApplicationNodes__Clone_meth.html -->

## PyIEnumDebugApplicationNodes.Clone

 PyIEnumDebugApplicationNodes = Clone()

Creates another enumerator that contains the same enumeration state as the current one


<!-- page: PyIEnumDebugApplicationNodes__Next_meth.html -->

## PyIEnumDebugApplicationNodes.Next

 object = Next(num)

Retrieves a specified number of items in the enumeration sequence.

#### Parameters

- num=1 : int

 Number of items to retrieve.


<!-- page: PyIEnumDebugApplicationNodes__Reset_meth.html -->

## PyIEnumDebugApplicationNodes.Reset

 Reset()

Resets the enumeration sequence to the beginning.


<!-- page: PyIEnumDebugApplicationNodes__Skip_meth.html -->

## PyIEnumDebugApplicationNodes.Skip

 Skip()

Skips over the next specified elementes.


---

<!-- object: PyIEnumDebugCodeContexts -->


<!-- page: PyIEnumDebugCodeContexts.html -->

---

## PyIEnumDebugCodeContexts Object

 A Python interface to IEnumDebugCodeContexts

#### Methods

- Next

 Retrieves a specified number of items in the enumeration sequence.

- Skip

 Skips over the next specified elementes.

- Reset

 Resets the enumeration sequence to the beginning.

- Clone

 Creates another enumerator that contains the same enumeration state as the current one.


<!-- page: PyIEnumDebugCodeContexts__Clone_meth.html -->

## PyIEnumDebugCodeContexts.Clone

 PyIEnumDebugCodeContexts = Clone()

Creates another enumerator that contains the same enumeration state as the current one


<!-- page: PyIEnumDebugCodeContexts__Next_meth.html -->

## PyIEnumDebugCodeContexts.Next

 object = Next(num)

Retrieves a specified number of items in the enumeration sequence.

#### Parameters

- num=1 : int

 Number of items to retrieve.


<!-- page: PyIEnumDebugCodeContexts__Reset_meth.html -->

## PyIEnumDebugCodeContexts.Reset

 Reset()

Resets the enumeration sequence to the beginning.


<!-- page: PyIEnumDebugCodeContexts__Skip_meth.html -->

## PyIEnumDebugCodeContexts.Skip

 Skip()

Skips over the next specified elementes.


---

<!-- object: PyIEnumDebugExpressionContexts -->


<!-- page: PyIEnumDebugExpressionContexts.html -->

---

## PyIEnumDebugExpressionContexts Object

 A Python interface to IEnumDebugExpressionContexts

#### Methods

- Next

 Retrieves a specified number of items in the enumeration sequence.

- Skip

 Skips over the next specified elementes.

- Reset

 Resets the enumeration sequence to the beginning.

- Clone

 Creates another enumerator that contains the same enumeration state as the current one.


<!-- page: PyIEnumDebugExpressionContexts__Clone_meth.html -->

## PyIEnumDebugExpressionContexts.Clone

 PyIEnumDebugExpressionContexts = Clone()

Creates another enumerator that contains the same enumeration state as the current one


<!-- page: PyIEnumDebugExpressionContexts__Next_meth.html -->

## PyIEnumDebugExpressionContexts.Next

 object = Next(num)

Retrieves a specified number of items in the enumeration sequence.

#### Parameters

- num=1 : int

 Number of items to retrieve.


<!-- page: PyIEnumDebugExpressionContexts__Reset_meth.html -->

## PyIEnumDebugExpressionContexts.Reset

 Reset()

Resets the enumeration sequence to the beginning.


<!-- page: PyIEnumDebugExpressionContexts__Skip_meth.html -->

## PyIEnumDebugExpressionContexts.Skip

 Skip()

Skips over the next specified elementes.


---

<!-- object: PyIEnumDebugPropertyInfo -->


<!-- page: PyIEnumDebugPropertyInfo.html -->

---

## PyIEnumDebugPropertyInfo Object

 A Python interface to IEnumDebugPropertyInfo

#### Methods

- Next

 Retrieves a specified number of items in the enumeration sequence.

- Skip

 Skips over the next specified elementes.

- Reset

 Resets the enumeration sequence to the beginning.

- Clone

 Creates another enumerator that contains the same enumeration state as the current one.

- GetCount

 Obtains the number of items


<!-- page: PyIEnumDebugPropertyInfo__Clone_meth.html -->

## PyIEnumDebugPropertyInfo.Clone

 PyIEnumDebugPropertyInfo = Clone()

Creates another enumerator that contains the same enumeration state as the current one


<!-- page: PyIEnumDebugPropertyInfo__GetCount_meth.html -->

## PyIEnumDebugPropertyInfo.GetCount

 int = GetCount()

Obtains the number of items


<!-- page: PyIEnumDebugPropertyInfo__Next_meth.html -->

## PyIEnumDebugPropertyInfo.Next

 object = Next(num)

Retrieves a specified number of items in the enumeration sequence.

#### Parameters

- num=1 : int

 Number of items to retrieve.


<!-- page: PyIEnumDebugPropertyInfo__Reset_meth.html -->

## PyIEnumDebugPropertyInfo.Reset

 Reset()

Resets the enumeration sequence to the beginning.


<!-- page: PyIEnumDebugPropertyInfo__Skip_meth.html -->

## PyIEnumDebugPropertyInfo.Skip

 Skip()

Skips over the next specified elementes.


---

<!-- object: PyIEnumDebugStackFrames -->


<!-- page: PyIEnumDebugStackFrames.html -->

---

## PyIEnumDebugStackFrames Object

 A Python interface to IEnumDebugStackFrames

#### Methods

- Next

 Retrieves a specified number of items in the enumeration sequence.

- Skip

 Skips over the next specified elementes.

- Reset

 Resets the enumeration sequence to the beginning.

- Clone

 Creates another enumerator that contains the same enumeration state as the current one.


<!-- page: PyIEnumDebugStackFrames__Clone_meth.html -->

## PyIEnumDebugStackFrames.Clone

 PyIEnumDebugStackFrames = Clone()

Creates another enumerator that contains the same enumeration state as the current one


<!-- page: PyIEnumDebugStackFrames__Next_meth.html -->

## PyIEnumDebugStackFrames.Next

 object = Next(num)

Retrieves a specified number of items in the enumeration sequence.

#### Parameters

- num=1 : int

 Number of items to retrieve.


<!-- page: PyIEnumDebugStackFrames__Reset_meth.html -->

## PyIEnumDebugStackFrames.Reset

 Reset()

Resets the enumeration sequence to the beginning.


<!-- page: PyIEnumDebugStackFrames__Skip_meth.html -->

## PyIEnumDebugStackFrames.Skip

 Skip()

Skips over the next specified elementes.


---

<!-- object: PyIEnumExplorerCommand -->


<!-- page: PyIEnumExplorerCommand.html -->

---

## PyIEnumExplorerCommand Object

 A Python interface to IEnumExplorerCommand

#### Methods

- Next

 Retrieves a specified number of items in the enumeration sequence.

- Skip

 Skips over the next specified elementes.

- Reset

 Resets the enumeration sequence to the beginning.

- Clone

 Creates another enumerator that contains the same enumeration state as the current one.


<!-- page: PyIEnumExplorerCommand__Clone_meth.html -->

## PyIEnumExplorerCommand.Clone

 PyIEnumExplorerCommand = Clone()

Creates another enumerator that contains the same enumeration state as the current one


<!-- page: PyIEnumExplorerCommand__Next_meth.html -->

## PyIEnumExplorerCommand.Next

 object = Next(num)

Retrieves a specified number of items in the enumeration sequence.

#### Parameters

- num=1 : int

 Number of items to retrieve.


<!-- page: PyIEnumExplorerCommand__Reset_meth.html -->

## PyIEnumExplorerCommand.Reset

 Reset()

Resets the enumeration sequence to the beginning.


<!-- page: PyIEnumExplorerCommand__Skip_meth.html -->

## PyIEnumExplorerCommand.Skip

 Skip()

Skips over the next specified elementes.


---

<!-- object: PyIEnumFORMATETC -->


<!-- page: PyIEnumFORMATETC.html -->

---

## PyIEnumFORMATETC Object

 A Python interface to IEnumFORMATETC

#### Methods

- Next

 Retrieves a specified number of items in the enumeration sequence.

- Skip

 Skips over the next specified elementes.

- Reset

 Resets the enumeration sequence to the beginning.

- Clone

 Creates another enumerator that contains the same enumeration state as the current one.


<!-- page: PyIEnumFORMATETC__Clone_meth.html -->

## PyIEnumFORMATETC.Clone

 PyIEnumFORMATETC = Clone()

Creates another enumerator that contains the same enumeration state as the current one


<!-- page: PyIEnumFORMATETC__Next_meth.html -->

## PyIEnumFORMATETC.Next

 object = Next(num)

Retrieves a specified number of items in the enumeration sequence.

#### Parameters

- num=1 : int

 Number of items to retrieve.


<!-- page: PyIEnumFORMATETC__Reset_meth.html -->

## PyIEnumFORMATETC.Reset

 Reset()

Resets the enumeration sequence to the beginning.


<!-- page: PyIEnumFORMATETC__Skip_meth.html -->

## PyIEnumFORMATETC.Skip

 Skip()

Skips over the next specified elementes.


---

<!-- object: PyIEnumGUID -->


<!-- page: PyIEnumGUID.html -->

---

## PyIEnumGUID Object

 A Python interface to IEnumGUID

#### Methods

- Next

 Retrieves a specified number of items in the enumeration sequence.

- Skip

 Skips over the next specified elementes.

- Reset

 Resets the enumeration sequence to the beginning.

- Clone

 Creates another enumerator that contains the same enumeration state as the current one.

#### Based On

PyIUnknown


<!-- page: PyIEnumGUID__Clone_meth.html -->

## PyIEnumGUID.Clone

 PyIEnumGUID = Clone()

Creates another enumerator that contains the same enumeration state as the current one


<!-- page: PyIEnumGUID__Next_meth.html -->

## PyIEnumGUID.Next

 (PyIID, ...) = Next(num)

Retrieves a specified number of items in the enumeration sequence.

#### Parameters

- num=1 : int

 Number of items to retrieve.

#### Return Value

The result is a tuple of PyIID objects, one for each element returned. Note that if zero elements are returned, it is not considered an error condition - an empty tuple is simply returned.


<!-- page: PyIEnumGUID__Reset_meth.html -->

## PyIEnumGUID.Reset

 Reset()

Resets the enumeration sequence to the beginning.


<!-- page: PyIEnumGUID__Skip_meth.html -->

## PyIEnumGUID.Skip

 Skip(num)

Skips over the next specified elementes.

#### Parameters

- num : int

 The number of elements being requested.


---

<!-- object: PyIEnumIDList -->


<!-- page: PyIEnumIDList.html -->

---

## PyIEnumIDList Object

 A Python interface to IEnumIDList

#### Methods

- Next

 Retrieves a specified number of items in the enumeration sequence.

- Skip

 Skips over the next specified elementes.

- Reset

 Resets the enumeration sequence to the beginning.

- Clone

 Creates another enumerator that contains the same enumeration state as the current one.


<!-- page: PyIEnumIDList__Clone_meth.html -->

## PyIEnumIDList.Clone

 PyIEnumIDList = Clone()

Creates another enumerator that contains the same enumeration state as the current one


<!-- page: PyIEnumIDList__Next_meth.html -->

## PyIEnumIDList.Next

 object = Next(num)

Retrieves a specified number of items in the enumeration sequence.

#### Parameters

- num=1 : int

 Number of items to retrieve.


<!-- page: PyIEnumIDList__Reset_meth.html -->

## PyIEnumIDList.Reset

 Reset()

Resets the enumeration sequence to the beginning.


<!-- page: PyIEnumIDList__Skip_meth.html -->

## PyIEnumIDList.Skip

 Skip()

Skips over the next specified elementes.


---

<!-- object: PyIEnumMoniker -->


<!-- page: PyIEnumMoniker.html -->

---

## PyIEnumMoniker Object

 A Python interface to IEnumMoniker

#### Methods

- Next

 Retrieves a specified number of items in the enumeration sequence.

- Skip

 Skips over the next specified elementes.

- Reset

 Resets the enumeration sequence to the beginning.

- Clone

 Creates another enumerator that contains the same enumeration state as the current one.

#### Based On

PyIUnknown


<!-- page: PyIEnumMoniker__Clone_meth.html -->

## PyIEnumMoniker.Clone

 PyIEnumMoniker = Clone()

Creates another enumerator that contains the same enumeration state as the current one


<!-- page: PyIEnumMoniker__Next_meth.html -->

## PyIEnumMoniker.Next

 PyIMoniker = Next(num)

Retrieves a specified number of items in the enumeration sequence.

#### Parameters

- num=1 : int

 Number of items to retrieve.

#### Return Value

The result is a tuple of PyIID objects, one for each element returned. Note that if zero elements are returned, it is not considered an error condition - an empty tuple is simply returned.


<!-- page: PyIEnumMoniker__Reset_meth.html -->

## PyIEnumMoniker.Reset

 Reset()

Resets the enumeration sequence to the beginning.


<!-- page: PyIEnumMoniker__Skip_meth.html -->

## PyIEnumMoniker.Skip

 Skip(num)

Skips over the next specified elementes.

#### Parameters

- num : int

 The number of elements being requested.


---

<!-- object: PyIEnumObjects -->


<!-- page: PyIEnumObjects.html -->

---

## PyIEnumObjects Object

 Iterates through a number of arbitrary interfaces

#### Methods

- Next

 Retrieves a specified number of items in the enumeration sequence.

- Skip

 Skips over the next specified elementes.

- Reset

 Resets the enumeration sequence to the beginning.

- Clone

 Creates another enumerator that contains the same enumeration state as the current one.


<!-- page: PyIEnumObjects__Clone_meth.html -->

## PyIEnumObjects.Clone

 PyIEnumObjects = Clone()

Creates another enumerator that contains the same enumeration state as the current one


<!-- page: PyIEnumObjects__Next_meth.html -->

## PyIEnumObjects.Next

 (PyIUnknown,...) = Next(num, riid )

Retrieves a specified number of items in the enumeration sequence.

#### Parameters

- num=1 : int

 Number of items to retrieve.

- riid=IID_IUnknown : PyIID

 The interfaces to return


<!-- page: PyIEnumObjects__Reset_meth.html -->

## PyIEnumObjects.Reset

 Reset()

Resets the enumeration sequence to the beginning.


<!-- page: PyIEnumObjects__Skip_meth.html -->

## PyIEnumObjects.Skip

 Skip()

Skips over the next specified elementes.


---

<!-- object: PyIEnumRemoteDebugApplicationThreads -->


<!-- page: PyIEnumRemoteDebugApplicationThreads.html -->

---

## PyIEnumRemoteDebugApplicationThreads Object

 A Python interface to IEnumRemoteDebugApplicationThreads

#### Methods

- Next

 Retrieves a specified number of items in the enumeration sequence.

- Skip

 Skips over the next specified elementes.

- Reset

 Resets the enumeration sequence to the beginning.

- Clone

 Creates another enumerator that contains the same enumeration state as the current one.


<!-- page: PyIEnumRemoteDebugApplicationThreads__Clone_meth.html -->

## PyIEnumRemoteDebugApplicationThreads.Clone

 PyIEnumRemoteDebugApplicationThreads = Clone()

Creates another enumerator that contains the same enumeration state as the current one


<!-- page: PyIEnumRemoteDebugApplicationThreads__Next_meth.html -->

## PyIEnumRemoteDebugApplicationThreads.Next

 object = Next(num)

Retrieves a specified number of items in the enumeration sequence.

#### Parameters

- num=1 : int

 Number of items to retrieve.


<!-- page: PyIEnumRemoteDebugApplicationThreads__Reset_meth.html -->

## PyIEnumRemoteDebugApplicationThreads.Reset

 Reset()

Resets the enumeration sequence to the beginning.


<!-- page: PyIEnumRemoteDebugApplicationThreads__Skip_meth.html -->

## PyIEnumRemoteDebugApplicationThreads.Skip

 Skip()

Skips over the next specified elementes.


---

<!-- object: PyIEnumRemoteDebugApplications -->


<!-- page: PyIEnumRemoteDebugApplications.html -->

---

## PyIEnumRemoteDebugApplications Object

 A Python interface to IEnumRemoteDebugApplications

#### Methods

- Next

 Retrieves a specified number of items in the enumeration sequence.

- Skip

 Skips over the next specified elementes.

- Reset

 Resets the enumeration sequence to the beginning.

- Clone

 Creates another enumerator that contains the same enumeration state as the current one.


<!-- page: PyIEnumRemoteDebugApplications__Clone_meth.html -->

## PyIEnumRemoteDebugApplications.Clone

 PyIEnumRemoteDebugApplications = Clone()

Creates another enumerator that contains the same enumeration state as the current one


<!-- page: PyIEnumRemoteDebugApplications__Next_meth.html -->

## PyIEnumRemoteDebugApplications.Next

 object = Next(num)

Retrieves a specified number of items in the enumeration sequence.

#### Parameters

- num=1 : int

 Number of items to retrieve.


<!-- page: PyIEnumRemoteDebugApplications__Reset_meth.html -->

## PyIEnumRemoteDebugApplications.Reset

 Reset()

Resets the enumeration sequence to the beginning.


<!-- page: PyIEnumRemoteDebugApplications__Skip_meth.html -->

## PyIEnumRemoteDebugApplications.Skip

 Skip()

Skips over the next specified elementes.


---

<!-- object: PyIEnumResources -->


<!-- page: PyIEnumResources.html -->

---

## PyIEnumResources Object

 A Python interface to IEnumResources

#### Methods

- Next

 Retrieves a specified number of items in the enumeration sequence.

- Skip

 Skips over the next specified elementes.

- Reset

 Resets the enumeration sequence to the beginning.

- Clone

 Creates another enumerator that contains the same enumeration state as the current one.


<!-- page: PyIEnumResources__Clone_meth.html -->

## PyIEnumResources.Clone

 PyIEnumResources = Clone()

Creates another enumerator that contains the same enumeration state as the current one


<!-- page: PyIEnumResources__Next_meth.html -->

## PyIEnumResources.Next

 object = Next(num)

Retrieves a specified number of items in the enumeration sequence.

#### Parameters

- num=1 : int

 Number of items to retrieve.


<!-- page: PyIEnumResources__Reset_meth.html -->

## PyIEnumResources.Reset

 Reset()

Resets the enumeration sequence to the beginning.


<!-- page: PyIEnumResources__Skip_meth.html -->

## PyIEnumResources.Skip

 Skip()

Skips over the next specified elementes.


---

<!-- object: PyIEnumSTATPROPSETSTG -->


<!-- page: PyIEnumSTATPROPSETSTG.html -->

---

## PyIEnumSTATPROPSETSTG Object

 A Python interface to IEnumSTATPROPSETSTG

#### Methods

- Next

 Retrieves a specified number of items in the enumeration sequence.

- Skip

 Skips over the next specified elementes.

- Reset

 Resets the enumeration sequence to the beginning.

- Clone

 Creates another enumerator that contains the same enumeration state as the current one.


<!-- page: PyIEnumSTATPROPSETSTG__Clone_meth.html -->

## PyIEnumSTATPROPSETSTG.Clone

 PyIEnumSTATPROPSETSTG = Clone()

Creates another enumerator that contains the same enumeration state as the current one


<!-- page: PyIEnumSTATPROPSETSTG__Next_meth.html -->

## PyIEnumSTATPROPSETSTG.Next

 object = Next(num)

Retrieves a specified number of items in the enumeration sequence.

#### Parameters

- num=1 : int

 Number of items to retrieve.


<!-- page: PyIEnumSTATPROPSETSTG__Reset_meth.html -->

## PyIEnumSTATPROPSETSTG.Reset

 Reset()

Resets the enumeration sequence to the beginning.


<!-- page: PyIEnumSTATPROPSETSTG__Skip_meth.html -->

## PyIEnumSTATPROPSETSTG.Skip

 Skip()

Skips over the next specified elementes.


---

<!-- object: PyIEnumSTATPROPSTG -->


<!-- page: PyIEnumSTATPROPSTG.html -->

---

## PyIEnumSTATPROPSTG Object

 A Python interface to IEnumSTATPROPSTG

#### Methods

- Next

 Retrieves a specified number of items in the enumeration sequence.

- Skip

 Skips over the next specified elementes.

- Reset

 Resets the enumeration sequence to the beginning.

- Clone

 Creates another enumerator that contains the same enumeration state as the current one.


<!-- page: PyIEnumSTATPROPSTG__Clone_meth.html -->

## PyIEnumSTATPROPSTG.Clone

 PyIEnumSTATPROPSTG = Clone()

Creates another enumerator that contains the same enumeration state as the current one


<!-- page: PyIEnumSTATPROPSTG__Next_meth.html -->

## PyIEnumSTATPROPSTG.Next

 object = Next(num)

Retrieves a specified number of items in the enumeration sequence.

#### Parameters

- num=1 : int

 Number of items to retrieve.


<!-- page: PyIEnumSTATPROPSTG__Reset_meth.html -->

## PyIEnumSTATPROPSTG.Reset

 Reset()

Resets the enumeration sequence to the beginning.


<!-- page: PyIEnumSTATPROPSTG__Skip_meth.html -->

## PyIEnumSTATPROPSTG.Skip

 Skip()

Skips over the next specified elementes.


---

<!-- object: PyIEnumSTATSTG -->


<!-- page: PyIEnumSTATSTG.html -->

---

## PyIEnumSTATSTG Object

 An enumerator for elements contained in a PyIStorage object

#### Methods

- Next

 Retrieves a specified number of items in the enumeration sequence.

- Skip

 Skips over the next specified elementes.

- Reset

 Resets the enumeration sequence to the beginning.

- Clone

 Creates another enumerator that contains the same enumeration state as the current one.

#### Based On

PyIUnknown


<!-- page: PyIEnumSTATSTG__Clone_meth.html -->

## PyIEnumSTATSTG.Clone

 PyIEnumSTATSTG = Clone()

Creates another enumerator that contains the same enumeration state as the current one


<!-- page: PyIEnumSTATSTG__Next_meth.html -->

## PyIEnumSTATSTG.Next

 (STATSTG, ...) = Next(num)

Retrieves a specified number of items in the enumeration sequence.

#### Parameters

- num=1 : int

 Number of items to retrieve.


<!-- page: PyIEnumSTATSTG__Reset_meth.html -->

## PyIEnumSTATSTG.Reset

 Reset()

Resets the enumeration sequence to the beginning.


<!-- page: PyIEnumSTATSTG__Skip_meth.html -->

## PyIEnumSTATSTG.Skip

 Skip()

Skips over the next specified elementes.


---

<!-- object: PyIEnumShellItems -->


<!-- page: PyIEnumShellItems.html -->

---

## PyIEnumShellItems Object

 A Python interface to IEnumShellItems

#### Methods

- Next

 Retrieves a specified number of items in the enumeration sequence.

- Skip

 Skips over the next specified elementes.

- Reset

 Resets the enumeration sequence to the beginning.

- Clone

 Creates another enumerator that contains the same enumeration state as the current one.


<!-- page: PyIEnumShellItems__Clone_meth.html -->

## PyIEnumShellItems.Clone

 PyIEnumShellItems = Clone()

Creates another enumerator that contains the same enumeration state as the current one


<!-- page: PyIEnumShellItems__Next_meth.html -->

## PyIEnumShellItems.Next

 (PyIShellItem,...) = Next(num)

Retrieves a specified number of items in the enumeration sequence.

#### Parameters

- num=1 : int

 Number of items to retrieve.


<!-- page: PyIEnumShellItems__Reset_meth.html -->

## PyIEnumShellItems.Reset

 Reset()

Resets the enumeration sequence to the beginning.


<!-- page: PyIEnumShellItems__Skip_meth.html -->

## PyIEnumShellItems.Skip

 Skip()

Skips over the next specified elementes.


---

<!-- object: PyIEnumString -->


<!-- page: PyIEnumString.html -->

---

## PyIEnumString Object

 An enumerator interface to list strings

#### Methods

- Next

 Retrieves a specified number of items in the enumeration sequence.

- Skip

 Skips over the next specified elementes.

- Reset

 Resets the enumeration sequence to the beginning.

- Clone

 Creates another enumerator that contains the same enumeration state as the current one.

#### Based On

PyIUnknown


<!-- page: PyIEnumString__Clone_meth.html -->

## PyIEnumString.Clone

 PyIEnumString = Clone()

Creates another enumerator that contains the same enumeration state as the current one


<!-- page: PyIEnumString__Next_meth.html -->

## PyIEnumString.Next

 (PyUnicode ,...) = Next(num)

Retrieves a specified number of items in the enumeration sequence.

#### Parameters

- num=1 : int

 Number of items to retrieve.


<!-- page: PyIEnumString__Reset_meth.html -->

## PyIEnumString.Reset

 Reset()

Resets the enumeration sequence to the beginning.


<!-- page: PyIEnumString__Skip_meth.html -->

## PyIEnumString.Skip

 Skip()

Skips over the next specified elementes.


---

<!-- object: PyIErrorLog -->


<!-- page: PyIErrorLog.html -->

---

## PyIErrorLog Object

 A Python wrapper for a COM IErrorLog interface.

#### Comments

 The IErrorLog interface is an abstraction for an error log that is used to communicate detailed error information between a client and an object. The caller of the single interface method, PyIErrorLog::AddError, simply logs an error where the error is an EXCEPINFO structure related to a specific property. The implementer of the interface is responsible for handling the error in whatever way it desires.
IErrorLog is used in the protocol between a client that implements PyIPropertyBag and an object that implements PyIPersistPropertyBag.

#### Methods

- AddError

 Adds an error to the error log.

#### Based On

PyIUnknown


<!-- page: PyIErrorLog__AddError_meth.html -->

## PyIErrorLog.AddError

 AddError(propName, excepInfo)

Adds an error to the error log.

#### Parameters

- propName : string

 The name of the error

- excepInfo=None : exception

 A COM exception. Must be a complete COM exception (ie, pythoncom.com_error, or win32com.server.exceptions.COMException())


---

<!-- object: PyIExplorerBrowser -->


<!-- page: PyIExplorerBrowser.html -->

---

## PyIExplorerBrowser Object

 Description of the interface

#### Methods

- Initialize

 Description of Initialize

- Destroy

 Description of Destroy

- SetRect

 Description of SetRect

- SetPropertyBag

 Description of SetPropertyBag

- SetEmptyText

 Description of SetEmptyText

- SetFolderSettings

 Description of SetFolderSettings

- Advise

 Description of Advise

- Unadvise

 Description of Unadvise

- SetOptions

 Description of SetOptions

- GetOptions

 Description of GetOptions

- BrowseToIDList

 Description of BrowseToIDList

- BrowseToObject

 Description of BrowseToObject

- FillFromObject

 Description of FillFromObject

- RemoveAll

 Description of RemoveAll

- GetCurrentView

 Description of GetCurrentView


<!-- page: PyIExplorerBrowser__Advise_meth.html -->

## PyIExplorerBrowser.Advise

 int = Advise(psbe)

Description of Advise.

#### Parameters

- psbe : PyIExplorerBrowserEvents

 Description for psbe


<!-- page: PyIExplorerBrowser__BrowseToIDList_meth.html -->

## PyIExplorerBrowser.BrowseToIDList

 BrowseToIDList(pidl, uFlags)

Description of BrowseToIDList.

#### Parameters

- pidl : PyPCUIDLIST_RELATIVE

 Description for pidl

- uFlags : int

 Description for uFlags


<!-- page: PyIExplorerBrowser__BrowseToObject_meth.html -->

## PyIExplorerBrowser.BrowseToObject

 BrowseToObject(punk, uFlags)

Description of BrowseToObject.

#### Parameters

- punk : PyIUnknown

 Description for punk

- uFlags : int

 Description for uFlags


<!-- page: PyIExplorerBrowser__Destroy_meth.html -->

## PyIExplorerBrowser.Destroy

 Destroy()

Description of Destroy.


<!-- page: PyIExplorerBrowser__FillFromObject_meth.html -->

## PyIExplorerBrowser.FillFromObject

 FillFromObject(punk, dwFlags)

Description of FillFromObject.

#### Parameters

- punk : PyIUnknown

 Description for punk

- dwFlags : PyEXPLORER_BROWSER_FILL_FLAGS

 Description for dwFlags


<!-- page: PyIExplorerBrowser__GetCurrentView_meth.html -->

## PyIExplorerBrowser.GetCurrentView

 PyIUnknown = GetCurrentView(riid)

Description of GetCurrentView.

#### Parameters

- riid : PyIID

 Description for riid


<!-- page: PyIExplorerBrowser__GetOptions_meth.html -->

## PyIExplorerBrowser.GetOptions

 int = GetOptions()

Description of GetOptions.


<!-- page: PyIExplorerBrowser__Initialize_meth.html -->

## PyIExplorerBrowser.Initialize

 Initialize(hwndParent, prc, pfs)

Description of Initialize.

#### Parameters

- hwndParent : HWND

 Description for hwndParent

- prc : PyRECT

 Description for prc

- pfs : PyFOLDERSETTINGS

 Description for pfs


<!-- page: PyIExplorerBrowser__RemoveAll_meth.html -->

## PyIExplorerBrowser.RemoveAll

 RemoveAll()

Description of RemoveAll.


<!-- page: PyIExplorerBrowser__SetEmptyText_meth.html -->

## PyIExplorerBrowser.SetEmptyText

 SetEmptyText(EmptyText)

Description of SetEmptyText.

#### Parameters

- EmptyText : str

 Description for pszEmptyText


<!-- page: PyIExplorerBrowser__SetFolderSettings_meth.html -->

## PyIExplorerBrowser.SetFolderSettings

 SetFolderSettings(pfs)

Description of SetFolderSettings.

#### Parameters

- pfs : PyFOLDERSETTINGS

 Description for pfs


<!-- page: PyIExplorerBrowser__SetOptions_meth.html -->

## PyIExplorerBrowser.SetOptions

 SetOptions(dwFlag)

Description of SetOptions.

#### Parameters

- dwFlag : PyEXPLORER_BROWSER_OPTIONS

 Description for dwFlag


<!-- page: PyIExplorerBrowser__SetPropertyBag_meth.html -->

## PyIExplorerBrowser.SetPropertyBag

 SetPropertyBag(PropertyBag)

Description of SetPropertyBag.

#### Parameters

- PropertyBag : str

 Description for pszPropertyBag


<!-- page: PyIExplorerBrowser__SetRect_meth.html -->

## PyIExplorerBrowser.SetRect

 PyHANDLE = SetRect(hdwp, rcBrowser )

Description of SetRect.

#### Parameters

- hdwp : PyHDWP

 Description for phdwp

- rcBrowser : PyRECT

 Description for rcBrowser


<!-- page: PyIExplorerBrowser__Unadvise_meth.html -->

## PyIExplorerBrowser.Unadvise

 Unadvise(dwCookie)

Description of Unadvise.

#### Parameters

- dwCookie : int

 Description for dwCookie


---

<!-- object: PyIExplorerBrowserEvents -->


<!-- page: PyIExplorerBrowserEvents.html -->

---

## PyIExplorerBrowserEvents Object

 Description of the interface

#### Methods

- OnNavigationPending

 Description of OnNavigationPending

- OnViewCreated

 Description of OnViewCreated

- OnNavigationComplete

 Description of OnNavigationComplete

- OnNavigationFailed

 Description of OnNavigationFailed


<!-- page: PyIExplorerBrowserEvents__OnNavigationComplete_meth.html -->

## PyIExplorerBrowserEvents.OnNavigationComplete

 OnNavigationComplete(pidlFolder)

Description of OnNavigationComplete.

#### Parameters

- pidlFolder : PyPCIDLIST_ABSOLUTE

 Description for pidlFolder


<!-- page: PyIExplorerBrowserEvents__OnNavigationFailed_meth.html -->

## PyIExplorerBrowserEvents.OnNavigationFailed

 OnNavigationFailed(pidlFolder)

Description of OnNavigationFailed.

#### Parameters

- pidlFolder : PyPCIDLIST_ABSOLUTE

 Description for pidlFolder


<!-- page: PyIExplorerBrowserEvents__OnNavigationPending_meth.html -->

## PyIExplorerBrowserEvents.OnNavigationPending

 OnNavigationPending(pidlFolder)

Description of OnNavigationPending.

#### Parameters

- pidlFolder : PyPCIDLIST_ABSOLUTE

 Description for pidlFolder


<!-- page: PyIExplorerBrowserEvents__OnViewCreated_meth.html -->

## PyIExplorerBrowserEvents.OnViewCreated

 OnViewCreated(psv)

Description of OnViewCreated.

#### Parameters

- psv : PyIShellView

 Description for psv


---

<!-- object: PyIExplorerCommand -->


<!-- page: PyIExplorerCommand.html -->

---

## PyIExplorerCommand Object

 Description of the interface

#### Methods

- GetTitle

 Description of GetTitle

- GetIcon

 Description of GetIcon

- GetToolTip

 Description of GetToolTip

- GetCanonicalName

 Description of GetCanonicalName

- GetState

 Description of GetState

- Invoke

 Description of Invoke

- GetFlags

 Description of GetFlags

- EnumSubCommands

 Description of EnumSubCommands


<!-- page: PyIExplorerCommand__EnumSubCommands_meth.html -->

## PyIExplorerCommand.EnumSubCommands

 PyIEnumExplorerCommand = EnumSubCommands()

Description of EnumSubCommands.


<!-- page: PyIExplorerCommand__GetCanonicalName_meth.html -->

## PyIExplorerCommand.GetCanonicalName

 PyIID = GetCanonicalName()

Description of GetCanonicalName.


<!-- page: PyIExplorerCommand__GetFlags_meth.html -->

## PyIExplorerCommand.GetFlags

 int = GetFlags()

Description of GetFlags.


<!-- page: PyIExplorerCommand__GetIcon_meth.html -->

## PyIExplorerCommand.GetIcon

 unicode = GetIcon(psiItemArray)

Description of GetIcon.

#### Parameters

- psiItemArray : PyIShellItemArray

 Description for psiItemArray


<!-- page: PyIExplorerCommand__GetState_meth.html -->

## PyIExplorerCommand.GetState

 int = GetState(psiItemArray, fOkToBeSlow )

Description of GetState.

#### Parameters

- psiItemArray : PyIShellItemArray

 Description for psiItemArray

- fOkToBeSlow : int

 Description for fOkToBeSlow


<!-- page: PyIExplorerCommand__GetTitle_meth.html -->

## PyIExplorerCommand.GetTitle

 unicode = GetTitle(psiItemArray)

Description of GetTitle.

#### Parameters

- psiItemArray : PyIShellItemArray

 Description for psiItemArray


<!-- page: PyIExplorerCommand__GetToolTip_meth.html -->

## PyIExplorerCommand.GetToolTip

 unicode = GetToolTip(psiItemArray)

Description of GetToolTip.

#### Parameters

- psiItemArray : PyIShellItemArray

 Description for psiItemArray


<!-- page: PyIExplorerCommand__Invoke_meth.html -->

## PyIExplorerCommand.Invoke

 Invoke(psiItemArray, pbc)

Description of Invoke.

#### Parameters

- psiItemArray : PyIShellItemArray

 Description for psiItemArray

- pbc : PyIBindCtx

 Description for pbc


---

<!-- object: PyIExplorerCommandProvider -->


<!-- page: PyIExplorerCommandProvider.html -->

---

## PyIExplorerCommandProvider Object

 This is a gateway only interface.


---

<!-- object: PyIExplorerPaneVisibility -->


<!-- page: PyIExplorerPaneVisibility.html -->

---

## PyIExplorerPaneVisibility Object

 Description of the interface

#### Methods

- Extract

 Description of Extract


<!-- page: PyIExplorerPaneVisibility__GetPaneState_meth.html -->

## PyIExplorerPaneVisibility.GetPaneState

 int = GetPaneState(ep)

Description of Extract.

#### Parameters

- ep : guid

 Description for ep


---

<!-- object: PyIExternalConnection -->


<!-- page: PyIExternalConnection.html -->

---

## PyIExternalConnection Object

 A Python wrapper for a COM IExternalConnection interface.

#### Comments

 The IExternalConnection interface manages a server object's count of marshaled, or external, connections. A server that maintains such a count can detect when it has no external connections and shut itself down in an orderly fashion.

#### Methods

- AddConnection

 Increments an object's count of its strong external connections (links).

- ReleaseConnection

 Decrements an object's count of its strong external connections (references).

#### Based On

PyIUnknown


<!-- page: PyIExternalConnection__AddConnection_meth.html -->

## PyIExternalConnection.AddConnection

 int = AddConnection(extconn, reserved )

Increments an object's count of its strong external connections (links).

#### Parameters

- extconn : int

 Type of external connection to the object. The only type of external connection currently supported by this interface is strong, which means that the object must remain alive as long as this external connection exists. Strong external connections are represented by the value EXTCONN_STRONG = 0x0001, which is defined in the enumeration EXTCON

- reserved=0 : int

 A reserved parameter

#### Return Value

The result is the number of reference counts on the object; used for debugging purposes only.


<!-- page: PyIExternalConnection__ReleaseConnection_meth.html -->

## PyIExternalConnection.ReleaseConnection

 int = ReleaseConnection(extconn, reserved , fLastReleaseCloses )

Decrements an object's count of its strong external connections (references).

#### Parameters

- extconn : int

 Type of external connection

- reserved : int

 A reserved parameter.

- fLastReleaseCloses : int

 TRUE specifies that if the connection being released is the last external lock on the object, the object should close. FALSE specifies that the object should remain open until closed by the user or another process.

#### Return Value

The result is the number of reference counts on the object; used for debugging purposes only.


---

<!-- object: PyIExtractIcon -->


<!-- page: PyIExtractIcon.html -->

---

## PyIExtractIcon Object

 Description of the interface

#### Methods

- Extract

 Description of Extract

- GetIconLocation

 Description of GetIconLocation


<!-- page: PyIExtractIcon__Extract_meth.html -->

## PyIExtractIcon.Extract

 Extract(pszFile, nIconIndex, nIconSize)

Description of Extract.

#### Parameters

- pszFile : unicode

 Description for pszFile

- nIconIndex : int

 Description for nIconIndex

- nIconSize : int

 Description for nIconIndex

#### Return Value

The result is (hicon_large, hicon_small), or (None,None) if the underlying function returns S_FALSE, indicating the calling application should extract it.


<!-- page: PyIExtractIcon__GetIconLocation_meth.html -->

## PyIExtractIcon.GetIconLocation

 GetIconLocation(uFlags, cchMax)

Description of GetIconLocation.

#### Parameters

- uFlags : int

 Description for uFlags

- cchMax=MAX_PATH+MAX_FNAME : int

 Buffer size to allocate for file name


---

<!-- object: PyIExtractIconW -->


<!-- page: PyIExtractIconW.html -->

---

## PyIExtractIconW Object

 Description of the interface

#### Methods

- Extract

 Description of Extract

- GetIconLocation

 Description of GetIconLocation


<!-- page: PyIExtractIconW__Extract_meth.html -->

## PyIExtractIconW.Extract

 Extract(pszFile, nIconIndex, nIconSize)

Description of Extract.

#### Parameters

- pszFile : unicode

 Description for pszFile

- nIconIndex : int

 Description for nIconIndex

- nIconSize : int

 Description for nIconIndex

#### Return Value

The result is (hicon_large, hicon_small), or (None,None) if the underlying function returns S_FALSE, indicating the calling application should extract it.


<!-- page: PyIExtractIconW__GetIconLocation_meth.html -->

## PyIExtractIconW.GetIconLocation

 GetIconLocation(uFlags, cchMax)

Description of GetIconLocation.

#### Parameters

- uFlags : int

 Description for uFlags

- cchMax=MAX_PATH+MAX_FNAME : int

 Buffer size to allocate for file name


---

<!-- object: PyIExtractImage -->


<!-- page: PyIExtractImage.html -->

---

## PyIExtractImage Object

 Description of the interface

#### Methods

- GetLocation

 Description of GetLocation

- Extract

 Description of Extract


<!-- page: PyIExtractImage__Extract_meth.html -->

## PyIExtractImage.Extract

 Extract()

Description of Extract.


<!-- page: PyIExtractImage__GetLocation_meth.html -->

## PyIExtractImage.GetLocation

 GetLocation(dwPriority, size, dwRecClrDepth, pdwFlags)

Description of GetLocation.

#### Parameters

- dwPriority : int

 Description for dwPriority

- size : (int, int)

 Description for prgSize

- dwRecClrDepth : int

 Description for dwRecClrDepth

- pdwFlags : int

 Description for pdwFlags


---

<!-- object: PyIFileOperation -->


<!-- page: PyIFileOperation.html -->

---

## PyIFileOperation Object

 Interface used to build a collection of file system modifications to be performed by the shell as a unit. Serves as a replacement for shell::SHFileOperation.
No changes are actually made until PerformOperations is called.
Progress can be monitored by implementing PyGFileOperationProgressSink.

#### Methods

- Advise

 Connects an event sink to receive updates

- Unadvise

 Disconnects a progress sink

- SetOperationFlags

 Sets option flags

- SetProgressMessage

 Not implemented

- SetProgressDialog

 Provides an interface used to display progress

- SetProperties

 Specifies a set of properties to be changed

- SetOwnerWindow

 Sets the parent window for any UI displayed.

- ApplyPropertiesToItem

 Specifies the item that will receive property changes

- ApplyPropertiesToItems

 Specifies multiple items that will receive property changes

- RenameItem

 Adds a rename to the operation sequence

- RenameItems

 Adds multiple renames to the operation sequence

- MoveItem

 Adds a move operation to the configuration

- MoveItems

 Adds multiple move operations to the configuration

- CopyItem

 Adds a copy operation to the configuration

- CopyItems

 Adds multiple copy operations to the configuration

- DeleteItem

 Adds a delete operation to the configuration

- DeleteItems

 Adds multiple delete operations to the configuration

- NewItem

 Creates a new file as part of the operation

- PerformOperations

 Effects all configured file system modifications

- GetAnyOperationsAborted

 Determines if any operations were terminated


<!-- page: PyIFileOperation__Advise_meth.html -->

## PyIFileOperation.Advise

 int = Advise(Sink)

Connects an event sink to receive updates

#### Parameters

- Sink : PyGFileOperationProgressSink

 Interface that receives progress updates

#### Return Value

Returns a cookie to be passed to PyIFileOperation::Unadvise to disconnect


<!-- page: PyIFileOperation__ApplyPropertiesToItem_meth.html -->

## PyIFileOperation.ApplyPropertiesToItem

 ApplyPropertiesToItem(Item)

Specifies the item that will receive property changes

#### Parameters

- Item : PyIShellItem

 The item to which property changes will be applied


<!-- page: PyIFileOperation__ApplyPropertiesToItems_meth.html -->

## PyIFileOperation.ApplyPropertiesToItems

 ApplyPropertiesToItems(Items)

Specifies multiple items that will receive property changes

#### Parameters

- Items : PyIUnknown

 PyIShellItemArray, PyIDataObject, or PyIEnumShellItems containing the target items


<!-- page: PyIFileOperation__CopyItem_meth.html -->

## PyIFileOperation.CopyItem

 CopyItem(Item, DestinationFolder, CopyName, Sink)

Adds a copy operation to the configuration

#### Parameters

- Item : PyIShellItem

 Item to be copied

- DestinationFolder : PyIShellItem

 Folder into which it will be copied

- CopyName=None : str

 New name for the copied file, use None to keep original name

- Sink=None : PyGFileOperationProgressSink

 Progress sink for just this operation


<!-- page: PyIFileOperation__CopyItems_meth.html -->

## PyIFileOperation.CopyItems

 CopyItems(Items, DestinationFolder)

Adds multiple copy operations to the configuration

#### Parameters

- Items : PyIUnknown

 PyIShellItemArray, PyIDataObject, or PyIEnumShellItems containing items to be copied

- DestinationFolder : PyIShellItem

 Folder into which they will be copied


<!-- page: PyIFileOperation__DeleteItem_meth.html -->

## PyIFileOperation.DeleteItem

 DeleteItem(Item, Sink)

Adds a delete operation to the configuration

#### Parameters

- Item : PyIShellItem

 Description for psiItem

- Sink=None : PyGFileOperationProgressSink

 Progress sink for just this operation


<!-- page: PyIFileOperation__DeleteItems_meth.html -->

## PyIFileOperation.DeleteItems

 DeleteItems(Items)

Adds multiple delete operations to the configuration

#### Parameters

- Items : PyIUnknown

 PyIShellItemArray, PyIDataObject, or PyIEnumShellItems containing the items to be deleted


<!-- page: PyIFileOperation__GetAnyOperationsAborted_meth.html -->

## PyIFileOperation.GetAnyOperationsAborted

 boolean = GetAnyOperationsAborted()

Determines if any operations were terminated


<!-- page: PyIFileOperation__MoveItem_meth.html -->

## PyIFileOperation.MoveItem

 MoveItem(Item, DestinationFolder, pszNewName, Sink)

Adds a move operation to the configuration

#### Parameters

- Item : PyIShellItem

 The item to be moved

- DestinationFolder : PyIShellItem

 The folder into which it will be moved

- pszNewName=None : str

 Name to be given to moved item, use None to keep original name

- Sink=None : PyGFileOperationProgressSink

 Progress sink to receive notification for just this operation


<!-- page: PyIFileOperation__MoveItems_meth.html -->

## PyIFileOperation.MoveItems

 MoveItems(Items, DestinationFolder)

Adds multiple move operations to the configuration

#### Parameters

- Items : PyIUnknown

 PyIShellItemArray, PyIDataObject, or PyIEnumShellItems containing the items to be moved

- DestinationFolder : PyIShellItem

 Folder into which all items will be moved


<!-- page: PyIFileOperation__NewItem_meth.html -->

## PyIFileOperation.NewItem

 NewItem(DestinationFolder, FileAttributes, Name, TemplateName, Sink)

Creates a new file as part of the operation

#### Parameters

- DestinationFolder : PyIShellItem

 Folder in which to create the file

- FileAttributes : int

 Combination of win32con.FILE_ATTRIBUTE_* flags

- Name : str

 Name of the new file

- TemplateName=None : str

 Template file used to initialize the new file

- Sink=None : PyGFileOperationProgressSink

 Progress sink for just this operation


<!-- page: PyIFileOperation__PerformOperations_meth.html -->

## PyIFileOperation.PerformOperations

 PerformOperations()

Effects all configured file system modifications


<!-- page: PyIFileOperation__RenameItem_meth.html -->

## PyIFileOperation.RenameItem

 RenameItem(Item, NewName, Sink)

Adds a rename to the operation sequence

#### Parameters

- Item : PyIShellItem

 The item to be renamed

- NewName : str

 The new name

- Sink=None : PyGFileOperationProgressSink

 Progress sink for this operation only.


<!-- page: PyIFileOperation__RenameItems_meth.html -->

## PyIFileOperation.RenameItems

 RenameItems(pUnkItems, NewName)

Adds multiple renames to the operation sequence

#### Parameters

- pUnkItems : PyIUnknown

 PyIShellItemArray, PyIDataObject, or PyIEnumShellItems containing items to be renamed

- NewName : str

 New name for all items. Collisions handled automatically.


<!-- page: PyIFileOperation__SetOperationFlags_meth.html -->

## PyIFileOperation.SetOperationFlags

 SetOperationFlags(OperationFlags)

Sets option flags for the operation

#### Parameters

- OperationFlags : int

 Combination of shellcon.FOF_* and FOFX_* flags


<!-- page: PyIFileOperation__SetOwnerWindow_meth.html -->

## PyIFileOperation.SetOwnerWindow

 SetOwnerWindow(Owner)

Sets the parent window for any UI displayed.

#### Parameters

- Owner : PyHANDLE

 Handle to parent window


<!-- page: PyIFileOperation__SetProgressDialog_meth.html -->

## PyIFileOperation.SetProgressDialog

 SetProgressDialog(popd)

Provides an interface used to display a progress dialog

#### Parameters

- popd : PyIOperationsProgressDialog

 Progress dialog interface

#### Comments

 IOperationsProgressDialog is not yet supported


<!-- page: PyIFileOperation__SetProgressMessage_meth.html -->

## PyIFileOperation.SetProgressMessage

 SetProgressMessage(Message)

Not implemented.

#### Parameters

- Message : str

 Description for Message


<!-- page: PyIFileOperation__SetProperties_meth.html -->

## PyIFileOperation.SetProperties

 SetProperties(proparray)

Specifies a set of properties to be changed.

#### Parameters

- proparray : PyIPropertyChangeArray

 Sequence of property changes to be performed (see propsys::PSCreatePropertyChangeArray)

#### Comments

 Note that these properties will be set for *any* files created by the operation, not just items passed to ApplyPropertiesToItem(s). New items created as the result of a rename, copy, or move must have a property handler, or the operation fails with the vague
com_error: (-2147467259, 'Unspecified error', None, None) (E_FAIL, or 0x80004005 in hex) even though the given file operation was actually performed.


<!-- page: PyIFileOperation__Unadvise_meth.html -->

## PyIFileOperation.Unadvise

 Unadvise(Cookie)

Disconnects a progress sink

#### Parameters

- Cookie : int

 Identifies the sink to disconnect, as returned by PyIFileOperation::Advise


---

<!-- object: PyIID -->


<!-- page: PyIID.html -->

---

## PyIID Object

 A Python object, representing an IID/CLSID.
All pythoncom functions that return a CLSID/IID will return one of these objects. However, in almost all cases, functions that expect a CLSID/IID as a param will accept either a string object, or a native PyIID object.

#### Methods

- __repr__

 Used whenever a repr() is called for the object tp_repr

- __hash__

 Used when the hash value of an IID object is required tp_hash

- __str__

 Used whenever a string representation of the IID is required. tp_str

#### Comments

 Note that IID objects support the buffer interface. Thus buffer(iid) can be used to obtain the raw bytes. tp_as_buffer


<!-- page: PyIID____hash___meth.html -->

## PyIID.__hash__

 int = __hash__()

Used when the hash value of an IID object is required


<!-- page: PyIID____repr___meth.html -->

## PyIID.__repr__

 string = __repr__()


<!-- page: PyIID____str___meth.html -->

## PyIID.__str__

 string = __str__()

Used whenever a string representation of the IID is required.


---

<!-- object: PyIIdentityName -->


<!-- page: PyIIdentityName.html -->

---

## PyIIdentityName Object

 Description of the interface

#### Based On

PyIRelatedItem


---

<!-- object: PyIInitializeWithFile -->


<!-- page: PyIInitializeWithFile.html -->

---

## PyIInitializeWithFile Object

 Initializes a property handler that requires a file path instead of a stream

#### Methods

- Initialize

 Passes a file path to a property handler on startup


<!-- page: PyIInitializeWithFile__Initialize_meth.html -->

## PyIInitializeWithFile.Initialize

 Initialize(FilePath, Mode)

Passes a file path to a property handler on startup

#### Parameters

- FilePath : str

 Full path to the file whose properties are to be accessed

- Mode : int

 Indicates if properties can be written, STGM_READ or STGM_READWRITE


---

<!-- object: PyIInitializeWithStream -->


<!-- page: PyIInitializeWithStream.html -->

---

## PyIInitializeWithStream Object

 Interface that initializes a handler capable of reading properties from a stream

#### Methods

- Initialize

 Initializes a property handler with a stream


<!-- page: PyIInitializeWithStream__Initialize_meth.html -->

## PyIInitializeWithStream.Initialize

 Initialize(Stream, Mode)

Initializes a property handler with a stream

#### Parameters

- Stream : PyIStream

 Stream containing the contents from which to extract properties

- Mode : int

 Indicates if stream is writable, STGM_READ or STGM_READWRITE


---

<!-- object: PyIInputObject -->


<!-- page: PyIInputObject.html -->

---

## PyIInputObject Object

 Description of the interface

#### Methods

- TranslateAccelerator

 Description of TranslateAccelerator

- UIActivate

 Description of UIActivate

- HasFocusIO

 Description of Refresh


<!-- page: PyIInputObject__HasFocusIO_meth.html -->

## PyIInputObject.HasFocusIO

 HasFocusIO()

Description of Refresh.


<!-- page: PyIInputObject__TranslateAccelerator_meth.html -->

## PyIInputObject.TranslateAccelerator

 TranslateAccelerator(pmsg)

Description of TranslateAccelerator.

#### Parameters

- pmsg : tuple

 Description for pmsg


<!-- page: PyIInputObject__UIActivate_meth.html -->

## PyIInputObject.UIActivate

 UIActivate(uState)

Description of UIActivate.

#### Parameters

- uState : int

 Description for uState


---

<!-- object: PyIInternetBindInfo -->


<!-- page: PyIInternetBindInfo.html -->

---

## PyIInternetBindInfo Object

 Description of the interface

#### Methods

- GetBindInfo

 Description of GetBindInfo

- GetBindString

 Description of GetBindString


<!-- page: PyIInternetBindInfo__GetBindInfo_meth.html -->

## PyIInternetBindInfo.GetBindInfo

 GetBindInfo()

Description of GetBindInfo.


<!-- page: PyIInternetBindInfo__GetBindString_meth.html -->

## PyIInternetBindInfo.GetBindString

 GetBindString()

Description of GetBindString.


---

<!-- object: PyIInternetPriority -->


<!-- page: PyIInternetPriority.html -->

---

## PyIInternetPriority Object

 Description of the interface

#### Methods

- SetPriority

 Description of SetPriority

- GetPriority

 Description of GetPriority


<!-- page: PyIInternetPriority__GetPriority_meth.html -->

## PyIInternetPriority.GetPriority

 GetPriority()

Description of GetPriority.


<!-- page: PyIInternetPriority__SetPriority_meth.html -->

## PyIInternetPriority.SetPriority

 SetPriority(nPriority)

Description of SetPriority.

#### Parameters

- nPriority : int

 Description for nPriority


---

<!-- object: PyIInternetProtocol -->


<!-- page: PyIInternetProtocol.html -->

---

## PyIInternetProtocol Object

 Description of the interface

#### Methods

- Read

 Description of Read

- Seek

 Description of Seek

- LockRequest

 Description of LockRequest

- UnlockRequest

 Description of UnlockRequest


<!-- page: PyIInternetProtocol__LockRequest_meth.html -->

## PyIInternetProtocol.LockRequest

 LockRequest(dwOptions)

Description of LockRequest.

#### Parameters

- dwOptions : int

 Description for dwOptions


<!-- page: PyIInternetProtocol__Read_meth.html -->

## PyIInternetProtocol.Read

 Read(cb)

Description of Read.

#### Parameters

- cb : int

 Description for cb


<!-- page: PyIInternetProtocol__Seek_meth.html -->

## PyIInternetProtocol.Seek

 Seek(dlibMove, dwOrigin)

Description of Seek.

#### Parameters

- dlibMove : LARGE_INTEGER

 Description for dlibMove

- dwOrigin : int

 Description for dwOrigin


<!-- page: PyIInternetProtocol__UnlockRequest_meth.html -->

## PyIInternetProtocol.UnlockRequest

 UnlockRequest()

Description of UnlockRequest.


---

<!-- object: PyIInternetProtocolInfo -->


<!-- page: PyIInternetProtocolInfo.html -->

---

## PyIInternetProtocolInfo Object

 Description of the interface

#### Methods

- ParseUrl

 Description of ParseUrl

- CombineUrl

 Description of CombineUrl

- CompareUrl

 Description of CompareUrl

- QueryInfo

 Description of QueryInfo


<!-- page: PyIInternetProtocolInfo__CombineUrl_meth.html -->

## PyIInternetProtocolInfo.CombineUrl

 CombineUrl(pwzBaseUrl, pwzRelativeUrl, dwCombineFlags, cchResult, dwReserved)

Description of CombineUrl.

#### Parameters

- pwzBaseUrl : unicode

 Description for pwzBaseUrl

- pwzRelativeUrl : unicode

 Description for pwzRelativeUrl

- dwCombineFlags : int

 Description for dwCombineFlags

- cchResult : int

 Description for cchResult

- dwReserved : int

 Description for dwReserved


<!-- page: PyIInternetProtocolInfo__CompareUrl_meth.html -->

## PyIInternetProtocolInfo.CompareUrl

 CompareUrl(pwzUrl1, pwzUrl2, dwCompareFlags)

Description of CompareUrl.

#### Parameters

- pwzUrl1 : unicode

 Description for pwzUrl1

- pwzUrl2 : unicode

 Description for pwzUrl2

- dwCompareFlags : int

 Description for dwCompareFlags


<!-- page: PyIInternetProtocolInfo__ParseUrl_meth.html -->

## PyIInternetProtocolInfo.ParseUrl

 ParseUrl(pwzUrl, ParseAction, dwParseFlags, cchResult, dwReserved)

Description of ParseUrl.

#### Parameters

- pwzUrl : unicode

 Description for pwzUrl

- ParseAction : int

 Description for ParseAction

- dwParseFlags : int

 Description for dwParseFlags

- cchResult : int

 Description for cchResult

- dwReserved : int

 Description for dwReserved


<!-- page: PyIInternetProtocolInfo__QueryInfo_meth.html -->

## PyIInternetProtocolInfo.QueryInfo

 int|string = QueryInfo(pwzUrl, OueryOption , dwQueryFlags , cbBuffer , dwReserved )

Description of QueryInfo.

#### Parameters

- pwzUrl : unicode

 Description for pwzUrl

- OueryOption : int

 Description for OueryOption

- dwQueryFlags : int

 Description for dwQueryFlags

- cbBuffer : int

 Description for cbBuffer

- dwReserved : int

 Description for dwReserved

#### Comments

 If the buffer size is the size of an integer, an integer will be returned, otherwise a string.


---

<!-- object: PyIInternetProtocolRoot -->


<!-- page: PyIInternetProtocolRoot.html -->

---

## PyIInternetProtocolRoot Object

 Description of the interface

#### Methods

- Start

 Description of Start

- Continue

 Description of Continue

- Abort

 Description of Abort

- Terminate

 Description of Terminate

- Suspend

 Description of Suspend

- Resume

 Description of Resume


<!-- page: PyIInternetProtocolRoot__Abort_meth.html -->

## PyIInternetProtocolRoot.Abort

 Abort(hrReason, dwOptions)

Description of Abort.

#### Parameters

- hrReason : int

 Description for hrReason

- dwOptions : int

 Description for dwOptions


<!-- page: PyIInternetProtocolRoot__Continue_meth.html -->

## PyIInternetProtocolRoot.Continue

 Continue()

Description of Continue.


<!-- page: PyIInternetProtocolRoot__Resume_meth.html -->

## PyIInternetProtocolRoot.Resume

 Resume()

Description of Resume.


<!-- page: PyIInternetProtocolRoot__Start_meth.html -->

## PyIInternetProtocolRoot.Start

 Start(szUrl, pOIProtSink, pOIBindInfo, grfPI, dwReserved)

Description of Start.

#### Parameters

- szUrl : unicode

 Description for szUrl

- pOIProtSink : PyIInternetProtocolSink

 Description for pOIProtSink

- pOIBindInfo : PyIInternetBindInfo

 Description for pOIBindInfo

- grfPI : int

 Description for grfPI

- dwReserved : int

 Description for dwReserved


<!-- page: PyIInternetProtocolRoot__Suspend_meth.html -->

## PyIInternetProtocolRoot.Suspend

 Suspend()

Description of Suspend.


<!-- page: PyIInternetProtocolRoot__Terminate_meth.html -->

## PyIInternetProtocolRoot.Terminate

 Terminate(dwOptions)

Description of Terminate.

#### Parameters

- dwOptions : int

 Description for dwOptions


---

<!-- object: PyIInternetProtocolSink -->


<!-- page: PyIInternetProtocolSink.html -->

---

## PyIInternetProtocolSink Object

 Description of the interface

#### Methods

- Switch

 Description of Switch

- ReportProgress

 Description of ReportProgress

- ReportData

 Description of ReportData

- ReportResult

 Description of ReportResult


<!-- page: PyIInternetProtocolSink__ReportData_meth.html -->

## PyIInternetProtocolSink.ReportData

 ReportData(grfBSCF, ulProgress, ulProgressMax)

Description of ReportData.

#### Parameters

- grfBSCF : int

 Description for grfBSCF

- ulProgress : int

 Description for ulProgress

- ulProgressMax : int

 Description for ulProgressMax


<!-- page: PyIInternetProtocolSink__ReportProgress_meth.html -->

## PyIInternetProtocolSink.ReportProgress

 ReportProgress(ulStatusCode, szStatusText)

Description of ReportProgress.

#### Parameters

- ulStatusCode : int

 Description for ulStatusCode

- szStatusText : unicode

 Description for szStatusText


<!-- page: PyIInternetProtocolSink__ReportResult_meth.html -->

## PyIInternetProtocolSink.ReportResult

 ReportResult(hrResult, dwError, szResult)

Description of ReportResult.

#### Parameters

- hrResult : int

 Description for hrResult

- dwError : int

 Description for dwError

- szResult : unicode

 Description for szResult


<!-- page: PyIInternetProtocolSink__Switch_meth.html -->

## PyIInternetProtocolSink.Switch

 Switch()

Description of Switch.


---

<!-- object: PyIInternetSecurityManager -->


<!-- page: PyIInternetSecurityManager.html -->

---

## PyIInternetSecurityManager Object

 Description of the interface

#### Methods

- SetSecuritySite

 Description of SetSecuritySite

- GetSecuritySite

 Description of GetSecuritySite

- MapUrlToZone

 Description of MapUrlToZone

- GetSecurityId

 Description of GetSecurityId

- ProcessUrlAction

 Description of ProcessUrlAction { "QueryCustomPolicy", PyIInternetSecurityManager::QueryCustomPolicy, 1 },

- SetZoneMapping

 Description of SetZoneMapping

- GetZoneMappings

 Description of GetZoneMappings


<!-- page: PyIInternetSecurityManager__GetSecurityId_meth.html -->

## PyIInternetSecurityManager.GetSecurityId

 GetSecurityId(pwszUrl, pcbSecurityId)

Description of GetSecurityId.

#### Parameters

- pwszUrl : unicode

 Description for pwszUrl

- pcbSecurityId : int

 Description for pcbSecurityId


<!-- page: PyIInternetSecurityManager__GetSecuritySite_meth.html -->

## PyIInternetSecurityManager.GetSecuritySite

 GetSecuritySite()

Description of GetSecuritySite.


<!-- page: PyIInternetSecurityManager__GetZoneMappings_meth.html -->

## PyIInternetSecurityManager.GetZoneMappings

 GetZoneMappings(dwZone, dwFlags)

Description of GetZoneMappings.

#### Parameters

- dwZone : int

 Description for dwZone

- dwFlags : int

 Description for dwFlags


<!-- page: PyIInternetSecurityManager__MapUrlToZone_meth.html -->

## PyIInternetSecurityManager.MapUrlToZone

 MapUrlToZone(pwszUrl, dwFlags)

Description of MapUrlToZone.

#### Parameters

- pwszUrl : unicode

 Description for pwszUrl

- dwFlags : int

 Description for dwFlags


<!-- page: PyIInternetSecurityManager__ProcessUrlAction_meth.html -->

## PyIInternetSecurityManager.ProcessUrlAction

 ProcessUrlAction(pwszUrl, dwAction, context, dwFlags)

Description of ProcessUrlAction.

#### Parameters

- pwszUrl : unicode

 Description for pwszUrl

- dwAction : int

 Description for dwAction

- context : bytes

- dwFlags : int

 Description for dwFlags


<!-- page: PyIInternetSecurityManager__SetSecuritySite_meth.html -->

## PyIInternetSecurityManager.SetSecuritySite

 SetSecuritySite(pSite)

Description of SetSecuritySite.

#### Parameters

- pSite : PyIInternetSecurityMgrSite

 Description for pSite


<!-- page: PyIInternetSecurityManager__SetZoneMapping_meth.html -->

## PyIInternetSecurityManager.SetZoneMapping

 SetZoneMapping(dwZone, lpszPattern, dwFlags)

Description of SetZoneMapping.

#### Parameters

- dwZone : int

 Description for dwZone

- lpszPattern : unicode

 Description for lpszPattern

- dwFlags : int

 Description for dwFlags


---

<!-- object: PyIKnownFolder -->


<!-- page: PyIKnownFolder.html -->

---

## PyIKnownFolder Object

 Interface representing a known folder that serves as a replacement for the numeric CSIDL definitions and API functions.

#### Methods

- GetId

 Returns the id of the folder

- GetCategory

 Returns the category for a folder (shellcon.KF_CATEGORY_*)

- GetShellItem

 Returns a shell interface for the folder

- GetPath

 Returns the path to the folder

- SetPath

 Changes the location of the folder

- GetIDList

 Returns the folder's location as an item id list

- GetFolderType

 Returns the type of the folder

- GetRedirectionCapabilities

 Returns flags indicating how the folder can be redirected

- GetFolderDefinition

 Retrieves detailed information about a known folder


<!-- page: PyIKnownFolder__GetCategory_meth.html -->

## PyIKnownFolder.GetCategory

 int = GetCategory()

Returns the category for a folder (shellcon.KF_CATEGORY_*)


<!-- page: PyIKnownFolder__GetFolderDefinition_meth.html -->

## PyIKnownFolder.GetFolderDefinition

 dict = GetFolderDefinition()

Retrieves detailed information about a known folder

#### Return Value

Returns a dict containing info from a KNOWNFOLDER_DEFINITION struct


<!-- page: PyIKnownFolder__GetFolderType_meth.html -->

## PyIKnownFolder.GetFolderType

 PyIID = GetFolderType()

Returns the type of the folder

#### Return Value

Returns a folder type guid (shell.FOLDERTYPEID_*)


<!-- page: PyIKnownFolder__GetIDList_meth.html -->

## PyIKnownFolder.GetIDList

 PyIDL = GetIDList(Flags)

Returns the folder's location as an item id list.

#### Parameters

- Flags : int

 Combination of shellcon.KF_FLAG_* values that affect how the operation is performed


<!-- page: PyIKnownFolder__GetId_meth.html -->

## PyIKnownFolder.GetId

 PyIID = GetId()

Returns the id of the folder


<!-- page: PyIKnownFolder__GetPath_meth.html -->

## PyIKnownFolder.GetPath

 str = GetPath(Flags)

Returns the path to the folder

#### Parameters

- Flags=0 : int

 Combination of shellcon.KF_FLAG_* flags controlling how the path is returned


<!-- page: PyIKnownFolder__GetRedirectionCapabilities_meth.html -->

## PyIKnownFolder.GetRedirectionCapabilities

 int = GetRedirectionCapabilities()

Returns flags indicating how the folder can be redirected

#### Return Value

Combination of shellcon.KF_REDIRECTION_CAPABILITIES_* flags


<!-- page: PyIKnownFolder__GetShellItem_meth.html -->

## PyIKnownFolder.GetShellItem

 PyIShellItem = GetShellItem(Flags, riid )

Returns a shell interface for the folder

#### Parameters

- Flags=0 : int

 Combination of shellcon.KF_FLAG_* values

- riid=IID_IShellItem : PyIID

 The interface to return (IShellItem or IShellItem2)


<!-- page: PyIKnownFolder__SetPath_meth.html -->

## PyIKnownFolder.SetPath

 SetPath(Flags, Path)

Changes the location of the folder

#### Parameters

- Flags : int

 KF_FLAG_DONT_UNEXPAND, or 0

- Path : str

 New path for known folder


---

<!-- object: PyIKnownFolderManager -->


<!-- page: PyIKnownFolderManager.html -->

---

## PyIKnownFolderManager Object

 Interface used to manage known folder definitions.

#### Methods

- FolderIdFromCsidl

 Returns the folder id that corresponds to a CSIDL

- FolderIdToCsidl

 Returns the CSIDL equivalent of a known folder

- GetFolderIds

 Retrieves all known folder ids.

- GetFolder

 Returns a folder by its id

- GetFolderByName

 Returns a folder by its canonical name

- RegisterFolder

 Defines a new known folder

- UnregisterFolder

 Removes the definition of a known folder

- FindFolderFromPath

 Retrieves a known folder by path

- FindFolderFromIDList

 Retrieves a known folder using its item id list.

- Redirect

 Redirects a known folder to an alternate location


<!-- page: PyIKnownFolderManager__FindFolderFromIDList_meth.html -->

## PyIKnownFolderManager.FindFolderFromIDList

 PyIKnownFolder = FindFolderFromIDList(pidl)

Retrieves a known folder using its item id list.

#### Parameters

- pidl : PyIDL

 Item id list of the folder


<!-- page: PyIKnownFolderManager__FindFolderFromPath_meth.html -->

## PyIKnownFolderManager.FindFolderFromPath

 PyIKnownFolder = FindFolderFromPath(Path, Mode )

Retrieves a known folder by path

#### Parameters

- Path : str

 Path of a folder

- Mode : int

 FFFP_EXACTMATCH or FFFP_NEARESTPARENTMATCH


<!-- page: PyIKnownFolderManager__FolderIdFromCsidl_meth.html -->

## PyIKnownFolderManager.FolderIdFromCsidl

 PyIID = FolderIdFromCsidl(Csidl)

Returns the folder id that corresponds to a CSIDL

#### Parameters

- Csidl : int

 The legacy CSIDL identifying a folder


<!-- page: PyIKnownFolderManager__FolderIdToCsidl_meth.html -->

## PyIKnownFolderManager.FolderIdToCsidl

 int = FolderIdToCsidl(id)

Returns the CSIDL equivalent of a known folder

#### Parameters

- id : PyIID

 A known folder id (shell.FOLDERID_*)


<!-- page: PyIKnownFolderManager__GetFolderByName_meth.html -->

## PyIKnownFolderManager.GetFolderByName

 PyIKnownFolder = GetFolderByName(Name)

Returns a folder by canonical name

#### Parameters

- Name : str

 The nonlocalized name of a known folder


<!-- page: PyIKnownFolderManager__GetFolderIds_meth.html -->

## PyIKnownFolderManager.GetFolderIds

 (PyIID,...) = GetFolderIds()

Retrieves all known folder ids.


<!-- page: PyIKnownFolderManager__GetFolder_meth.html -->

## PyIKnownFolderManager.GetFolder

 PyIKnownFolder = GetFolder(id)

Returns a folder by its id.

#### Parameters

- id : PyIID

 A known folder id (shell.FOLDERID_*)


<!-- page: PyIKnownFolderManager__Redirect_meth.html -->

## PyIKnownFolderManager.Redirect

 Redirect(id, hwnd, flags, TargetPath, Exclusion)

Redirects a known folder to an alternate location

#### Parameters

- id : PyIID

 Id of the known folder to be redirected

- hwnd : PyHANDLE

 Handle of window to be used for user interaction

- flags : int

 Combination of KF_REDIRECT_* flags

- TargetPath : str

 Path to which the known folder will be redirected

- Exclusion : (PyIID,...)

 Sequence of known folder ids of subfolders to be excluded from redirection


<!-- page: PyIKnownFolderManager__RegisterFolder_meth.html -->

## PyIKnownFolderManager.RegisterFolder

 RegisterFolder(id, Definition)

Defines a new known folder

#### Parameters

- id : PyIID

 GUID used to identify the new known folder

- Definition : dict

 Dictionary containing info to be placed in a KNOWNFOLDER_DEFINITION struct

#### Comments

 PyIKnownFolder::GetFolderDefinition can be used to get a template dictionary


<!-- page: PyIKnownFolderManager__UnregisterFolder_meth.html -->

## PyIKnownFolderManager.UnregisterFolder

 UnregisterFolder(id)

Removes the definition of a known folder

#### Parameters

- id : PyIID

 GUID of a known folder to be unregistered


---

<!-- object: PyILockBytes -->


<!-- page: PyILockBytes.html -->

---

## PyILockBytes Object

 Description of the interface

#### Methods

- ReadAt

 Reads a specified number of bytes starting at a specified offset from the beginning of the byte array object.

- WriteAt

 Writes the specified number of bytes starting at a specified offset from the beginning of the byte array.

- Flush

 Ensures that any internal buffers maintained by the byte array object are written out to the backing storage.

- SetSize

 Changes the size of the byte array.

- LockRegion

 Restricts access to a specified range of bytes in the byte array.

- UnlockRegion

 Removes the access restriction on a range of bytes previously restricted with PyILockBytes::LockRegion.

- Stat

 Retrieves a STATSTG structure for this byte array object.

#### Based On

PyIUnknown


<!-- page: PyILockBytes__Flush_meth.html -->

## PyILockBytes.Flush

 Flush()

Ensures that any internal buffers maintained by the byte array object are written out to the backing storage.


<!-- page: PyILockBytes__LockRegion_meth.html -->

## PyILockBytes.LockRegion

 LockRegion(libOffset, cb, dwLockType)

Restricts access to a specified range of bytes in the byte array.

#### Parameters

- libOffset : ULARGE_INTEGER

 The beginning of the region to lock.

- cb : ULARGE_INTEGER

 The number of bytes to lock.

- dwLockType : int

 Specifies the restrictions being requested on accessing the range.


<!-- page: PyILockBytes__ReadAt_meth.html -->

## PyILockBytes.ReadAt

 string = ReadAt(ulOffset, cb )

Reads a specified number of bytes starting at a specified offset from the beginning of the byte array object.

#### Parameters

- ulOffset : ULARGE_INTEGER

 Offset to start reading

- cb : int

 Number of bytes to read

#### Comments

 The result is a binary buffer returned in a string.


<!-- page: PyILockBytes__SetSize_meth.html -->

## PyILockBytes.SetSize

 SetSize(cb)

Changes the size of the byte array.

#### Parameters

- cb : ULARGE_INTEGER

 The new size.


<!-- page: PyILockBytes__Stat_meth.html -->

## PyILockBytes.Stat

 STATSTG = Stat(grfStatFlag)

Retrieves a STATSTG structure for this byte array object.

#### Parameters

- grfStatFlag : int

 Specifies that this method does not return some of the fields in the STATSTG structure, thus saving a memory allocation operation. Values are taken from the STATFLAG enumerationg


<!-- page: PyILockBytes__UnlockRegion_meth.html -->

## PyILockBytes.UnlockRegion

 UnlockRegion(libOffset, cb, dwLockType)

Removes the access restriction on a range of bytes previously restricted with PyILockBytes::LockRegion.

#### Parameters

- libOffset : ULARGE_INTEGER

 The beginning of the region to unlock.

- cb : ULARGE_INTEGER

 The number of bytes to lock.

- dwLockType : int

 Specifies the restrictions being requested on accessing the range.


<!-- page: PyILockBytes__WriteAt_meth.html -->

## PyILockBytes.WriteAt

 int = WriteAt(ulOffset, data )

Writes the specified number of bytes starting at a specified offset from the beginning of the byte array.

#### Parameters

- ulOffset : ULARGE_INTEGER

 Offset to write at.

- data : string

 Data to write

#### Return Value

The result is the number of bytes actually written.


---

<!-- object: PyIMAPIContainer -->


<!-- page: PyIMAPIContainer.html -->

---

## PyIMAPIContainer Object

 An COM interface to MAPI's IMAPIContainer interface.
Derived from PyIMAPIProp

#### Methods

- OpenEntry

 Opens an object and returns an interface object for further access.

- GetContentsTable

 Returns an object representing the container's contents table.

- GetHierarchyTable

 Returns an object representing the container's hierarchy table.


<!-- page: PyIMAPIContainer__GetContentsTable_meth.html -->

## PyIMAPIContainer.GetContentsTable

 PyIMAPITable = GetContentsTable(flags)

Returns an object representing the container's contents table.

#### Parameters

- flags : int

 The flags to use.


<!-- page: PyIMAPIContainer__GetHierarchyTable_meth.html -->

## PyIMAPIContainer.GetHierarchyTable

 PyIMAPITable = GetHierarchyTable(flags)

Returns an object representing the container's hierarchy table.

#### Parameters

- flags : int

 The flags to use.


<!-- page: PyIMAPIContainer__OpenEntry_meth.html -->

## PyIMAPIContainer.OpenEntry

 PyIInterface = OpenEntry(entryId, iid , flags )

Opens an object and returns an interface object for further access.

#### Parameters

- entryId : string

 The EntryID to open.

- iid : PyIID

 The IID of the returned interface, or None for the default interface.

- flags : int

 Flags for the call. May include MAPI_BEST_ACCESS, MAPI_DEFERRED_ERRORS, MAPI_MODIFY and possibly others (see the MAPI documentation)


---

<!-- object: PyIMAPIFolder -->


<!-- page: PyIMAPIFolder.html -->

---

## PyIMAPIFolder Object

 An COM interface to MAPI
Derived from PyIMAPIProp

#### Methods

- GetLastError

 Returns the last error code for the object.

- CreateFolder

 Creates a folder object.

- CreateMessage

 Creates a message in a folder

- CopyMessages

 Copies the specified messages

- DeleteFolder

 Deletes a subfolder.

- DeleteMessages

 Deletes the specified messages.

- EmptyFolder

 deletes all messages and subfolders from a folder without deleting the folder itself.

- SetReadFlags

 Sets or clears the MSGFLAG_READ flag in the PR_MESSAGE_FLAGS (PidTagMessageFlags) property of one or more of the folder's messages, and manages the sending of read reports.


<!-- page: PyIMAPIFolder__CopyMessages_meth.html -->

## PyIMAPIFolder.CopyMessages

 int = CopyMessages(msgs, iid , folder , ulUIParam , progress , flags )

Copies the specified messages

#### Parameters

- msgs : PySBinaryArray

- iid : PyIID

 IID representing the interface to be used to access the destination folder. Should usually be None.

- folder : PyIMAPIFolder

 The destination folder

- ulUIParam : long

 Handle of the parent window for any dialog boxes or windows this method displays.

- progress : PyIMAPIProgress

 A progress object, or None

- flags : int

 A bitmask of

| | Mask | Description
| |

---

 |

---

| | MAPI_DECLINE_OK | Informs the message store provider to immediately return MAPI_E_DECLINE_COPY if it implements CopyMessage by calling the support object's IMAPISupport::DoCopyTo or IMAPISupport::DoCopyProps method.
| | MESSAGE_DIALOG | Displays a progress indicator as the operation proceeds.
| | MESSAGE_MOVE | The message or messages are to be moved rather than copied. If MESSAGE_MOVE is not set, the messages are copied.


<!-- page: PyIMAPIFolder__CreateFolder_meth.html -->

## PyIMAPIFolder.CreateFolder

 PyIMAPIFolder = CreateFolder(folderType, folderName , folderComment , iid , flags )

Creates a folder object.

#### Parameters

- folderType : int

 The type of folder to create

- folderName : string

 The name of the folder.

- folderComment=None : string

 A comment for the folder or None

- iid=None : PyIID

 The IID of the object to return. Should usually be None.

- flags=0 : int


<!-- page: PyIMAPIFolder__CreateMessage_meth.html -->

## PyIMAPIFolder.CreateMessage

 PyIMessage = CreateMessage(iid, flags )

Creates a message in a folder

#### Parameters

- iid : PyIID

 The IID of the object to return. Should usually be None.

- flags : int


<!-- page: PyIMAPIFolder__DeleteFolder_meth.html -->

## PyIMAPIFolder.DeleteFolder

 DeleteFolder(entryId, uiParam, progress)

Deletes a subfolder.

#### Parameters

- entryId : string

 The EntryID of the subfolder to delete.

- uiParam : long

 Handle of the parent window of the progress indicator.

- progress : PyIMAPIProgress

 A progress object, or None


<!-- page: PyIMAPIFolder__DeleteMessages_meth.html -->

## PyIMAPIFolder.DeleteMessages

 int = DeleteMessages(msgs, uiParam , progress , flags )

Deletes the specified messages.

#### Parameters

- msgs : PySBinaryArray

- uiParam : int

 A HWND for the progress

- progress : PyIMAPIProgress

 A progress object, or None

- flags : int


<!-- page: PyIMAPIFolder__EmptyFolder_meth.html -->

## PyIMAPIFolder.EmptyFolder

 int = EmptyFolder(uiParam, progress , flags )

deletes all messages and subfolders from a folder without deleting the folder itself.

#### Parameters

- uiParam : int

 A HWND for the progress

- progress : PyIMAPIProgress

 A progress object, or None

- flags : int


<!-- page: PyIMAPIFolder__GetLastError_meth.html -->

## PyIMAPIFolder.GetLastError

 MAPIERROR = GetLastError(hr, flags )

Returns the last error code for the object.

#### Parameters

- hr : int

 Contains the error code generated in the previous method call.

- flags : int

 Indicates for format for the output.


<!-- page: PyIMAPIFolder__SetReadFlags_meth.html -->

## PyIMAPIFolder.SetReadFlags

 SetReadFlags(msgs, uiParam, progress, flag)

Sets or clears the MSGFLAG_READ flag in the PR_MESSAGE_FLAGS (PidTagMessageFlags) property of one or more of the folder's messages, and manages the sending of read reports.

#### Parameters

- msgs : PySBinaryArray

- uiParam : int

 A HWND for the progress

- progress : PyIMAPIProgress

 A progress object, or None

- flag : int

 Bitmask of flags that controls the setting of a message's read flag - that is, the message's MSGFLAG_READ flag in its PR_MESSAGE_FLAGS property and the processing of read reports.


---

<!-- object: PyIMAPIProp -->


<!-- page: PyIMAPIProp.html -->

---

## PyIMAPIProp Object

 An COM interface to MAPI
Derived from PyIUnknown

#### Methods

- GetProps

 Returns a list of property values.

- DeleteProps

 Deletes a set of properties.

- SetProps

 Sets a set of properties.

- CopyTo

 Copies an object to another

- CopyProps

 Copies a set of properties to another object

- OpenProperty

 Returns an interface object to be used to access a property.

- GetIDsFromNames

 Determines property IDs

- GetNamesFromIDs

 Determines property names

- GetLastError

 Returns the last error code for the object.

- SaveChanges

 Saves pending changes to the object

- GetPropList

 Gets a list of properties


<!-- page: PyIMAPIProp__CopyProps_meth.html -->

## PyIMAPIProp.CopyProps

 int, [problems, ] = CopyProps(propTags, uiParam , progress , resultIID , dest , flags , wantProblems )

Copies a set of properties to another object

#### Parameters

- propTags : PySPropTagArray

 The property tags to copy

- uiParam : int

 Handle to the parent window of the progress object

- progress : None

 Reserved - must pass None

- resultIID : PyIID

 IID of the destination object

- dest : PyIMAPIProp

 The destination object

- flags : int

 flags

- wantProblems=False : bool

 Return detailed error information


<!-- page: PyIMAPIProp__CopyTo_meth.html -->

## PyIMAPIProp.CopyTo

 int, [problems, ] = CopyTo(IIDExcludeList, propTags , uiParam , progress , resultIID , dest , flags , wantProblems )

Copies an object to another

#### Parameters

- IIDExcludeList : [PyIID, ]

 A sequence of IIDs to exclude.

- propTags : PySPropTagArray

 The property tags to exclude.

- uiParam : int

 Handle to the parent window of the progress object

- progress : None

 Reserved - must pass None

- resultIID : PyIID

 IID of the destination object

- dest : PyIMAPIProp

 The destination object

- flags : int

 flags

- wantProblems=False : bool

 Return detailed error information


<!-- page: PyIMAPIProp__DeleteProps_meth.html -->

## PyIMAPIProp.DeleteProps

 int, [problems, ] = DeleteProps(propList, wantProblems )

Deletes a set of properties.

#### Parameters

- propList : PySPropTagArray

 The list of properties

- wantProblems=False : bool

 Return detailed error information


<!-- page: PyIMAPIProp__GetIDsFromNames_meth.html -->

## PyIMAPIProp.GetIDsFromNames

 PySPropTagArray = GetIDsFromNames(nameIds, flags )

Determines property IDs

#### Parameters

- nameIds : PyMAPINAMEIDArray

 Sequence of name ids

- flags=0 : int


<!-- page: PyIMAPIProp__GetLastError_meth.html -->

## PyIMAPIProp.GetLastError

 MAPIERROR = GetLastError(hr, flags )

Returns the last error code for the object.

#### Parameters

- hr : int

 Contains the error code generated in the previous method call.

- flags : int

 Indicates for format for the output.


<!-- page: PyIMAPIProp__GetNamesFromIDs_meth.html -->

## PyIMAPIProp.GetNamesFromIDs

 HRESULT, PySPropTagArray, PyMAPINAMEIDArray = GetNamesFromIDs(propTags, propSetGuid , flags )

Determines property names

#### Parameters

- propTags : PySPropTagArray

 Sequence of property tags, or None

- propSetGuid=None : PyIID

 a globally unique identifier, identifying a property set, or None

- flags=0 : int


<!-- page: PyIMAPIProp__GetPropList_meth.html -->

## PyIMAPIProp.GetPropList

 PySPropTagArray = GetPropList(flags)

Gets a list of properties

#### Parameters

- flags : int

 flags


<!-- page: PyIMAPIProp__GetProps_meth.html -->

## PyIMAPIProp.GetProps

 int, [items, ] = GetProps(propList, flags )

Returns a list of property values.

#### Parameters

- propList : PySPropTagArray

 The list of properties

- flags=0 : int


<!-- page: PyIMAPIProp__OpenProperty_meth.html -->

## PyIMAPIProp.OpenProperty

 PyIUnknown = OpenProperty(propTag, iid , interfaceOptions , flags )

Returns an interface object to be used to access a property.

#### Parameters

- propTag : ULONG

 The property tag to open

- iid : PyIID

 The IID of the resulting interface.

- interfaceOptions : int

 Data that relates to the interface identified by the lpiid parameter.

- flags : int

 flags


<!-- page: PyIMAPIProp__SaveChanges_meth.html -->

## PyIMAPIProp.SaveChanges

 SaveChanges(flags)

Saves pending changes to the object

#### Parameters

- flags : int

 flags


<!-- page: PyIMAPIProp__SetProps_meth.html -->

## PyIMAPIProp.SetProps

 int, [problems, ] = SetProps(propList, wantProblems )

Sets a set of properties.

#### Parameters

- propList : [PySPropValue, ]

 The list of properties

- wantProblems=False : bool

 Return detailed error information


---

<!-- object: PyIMAPISession -->


<!-- page: PyIMAPISession.html -->

---

## PyIMAPISession Object

 An COM interface to MAPI's ISession interface.
Derived from PyIUnknown

#### Methods

- OpenEntry

 Opens an object and returns an interface object for further access.

- OpenMsgStore

 Opens a message store.

- QueryIdentity

 Returns the entry identifier of the object that provides the primary identity for the session.

- Advise

- Unadvise

- CompareEntryIDs

 Compares two entry identifiers belonging to a particular address book provider to determine if they refer to the same address book object

- GetLastError

 Returns the last error code for the object.

- GetMsgStoresTable

 Provides access to the message store table - a table with information about all of the message stores in the session profile.

- GetStatusTable

 Provides access to the status table - a table with information about all of the MAPI resources in the session.

- Logoff

 Ends a MAPI session.

- OpenAddressBook

 Opens the integrated address book.

- OpenProfileSection

 Opens a section of the current profile and returns an object for futher access

- AdminServices

 Provides access to a message service administration object for making changes to the message services.


<!-- page: PyIMAPISession__AdminServices_meth.html -->

## PyIMAPISession.AdminServices

 PyIMsgServiceAdmin = AdminServices(flags)

Provides access to a message service administration object for making changes to the message services.

#### Parameters

- flags=0 : int

 reserved; must be zero.


<!-- page: PyIMAPISession__Advise_meth.html -->

## PyIMAPISession.Advise

 int = Advise(entryId, mask , sink )

#### Parameters

- entryId : string

 The entryID of the object

- mask : int

- sink : PyIMAPIAdviseSink

#### Return Value

The result is an integer which should be passed to PyIMAPISession::Unadvise


<!-- page: PyIMAPISession__CompareEntryIDs_meth.html -->

## PyIMAPISession.CompareEntryIDs

 int = CompareEntryIDs(entryId, entryId , flags )

Compares two entry identifiers belonging to a particular address book provider to determine if they refer to the same address book object

#### Parameters

- entryId : string

 The first entry ID to be compared

- entryId : string

 The second entry ID to be compared

- flags=0 : int

 Reserved - must be zero.

#### Return Value

The result is set to TRUE if the two entry identifiers refer to the same object, and FALSE otherwise.


<!-- page: PyIMAPISession__GetLastError_meth.html -->

## PyIMAPISession.GetLastError

 MAPIERROR = GetLastError(hr, flags )

Returns the last error code for the object.

#### Parameters

- hr : int

 Contains the error code generated in the previous method call.

- flags : int

 Indicates for format for the output.


<!-- page: PyIMAPISession__GetMsgStoresTable_meth.html -->

## PyIMAPISession.GetMsgStoresTable

 PyIMAPITable = GetMsgStoresTable(flags)

Provides access to the message store table - a table with information about all of the message stores in the session profile.

#### Parameters

- flags : int

 Flags that control the opening.


<!-- page: PyIMAPISession__GetStatusTable_meth.html -->

## PyIMAPISession.GetStatusTable

 PyIMAPITable = GetStatusTable(flags)

Provides access to the status table - a table with information about all of the MAPI resources in the session.

#### Parameters

- flags : int

 Flags that control the opening.


<!-- page: PyIMAPISession__Logoff_meth.html -->

## PyIMAPISession.Logoff

 Logoff(uiParm, flags, reserved)

Ends a MAPI session.

#### Parameters

- uiParm : int

 hwnd of a dialog is to be displayed.

- flags : int

 Bitmask of flags that control the logoff operation.

- reserved : int

 Reserved; must be zero.


<!-- page: PyIMAPISession__OpenAddressBook_meth.html -->

## PyIMAPISession.OpenAddressBook

 PyIAddrBook = OpenAddressBook(uiParm, iid , flags )

Opens the integrated address book.

#### Parameters

- uiParm : int

 hwnd of a dialog is to be displayed.

- iid : PyIID

 The IID of the interface, or None.

- flags : int

 Flags that control the opening - AB_NO_DIALOG.


<!-- page: PyIMAPISession__OpenEntry_meth.html -->

## PyIMAPISession.OpenEntry

 PyIInterface = OpenEntry(entryId, iid , flags )

Opens an object and returns an interface object for further access.

#### Parameters

- entryId : string

 The EntryID to open.

- iid : PyIID

 The IID of the returned interface, or None for the default interface.

- flags : int

 Flags for the call. May include MAPI_BEST_ACCESS, MAPI_DEFERRED_ERRORS, MAPI_MODIFY and possibly others (see the MAPI documentation)


<!-- page: PyIMAPISession__OpenMsgStore_meth.html -->

## PyIMAPISession.OpenMsgStore

 PyIUnknown = OpenMsgStore(uiParam, entryId , iid , flags )

Opens a message store.

#### Parameters

- uiParam : int

 Handle to the parent window for dialogs.

- entryId : string

 The entry ID of the message store to open.

- iid : PyIID

 The IID of the interface returned, or None

- flags : int

 Options for the call.

#### Comments

 The result is the interface specified by the IID, or IID_IMsgStore if None is used.


<!-- page: PyIMAPISession__OpenProfileSection_meth.html -->

## PyIMAPISession.OpenProfileSection

 PyIProfSection = OpenProfileSection(iidSection, iid , flags )

Opens a section of the current profile and returns an object for futher access

#### Parameters

- iidSection : PyIID

 The MAPIIID of the profile section

- iid : PyIID

 The IID of the interface, or None.

- flags : int

 Flags that control the opening.


<!-- page: PyIMAPISession__QueryIdentity_meth.html -->

## PyIMAPISession.QueryIdentity

 string = QueryIdentity()

Returns the entry identifier of the object that provides the primary identity for the session.


<!-- page: PyIMAPISession__Unadvise_meth.html -->

## PyIMAPISession.Unadvise

 Unadvise(connection)

#### Parameters

- connection : int

 Value returned from PyIMAPISession::Advise


---

<!-- object: PyIMAPIStatus -->


<!-- page: PyIMAPIStatus.html -->

---

## PyIMAPIStatus Object

 Provides status information about the MAPI subsystem, the integrated address book and the MAPI spooler.
Derived from PyIMAPIProp

#### Methods

- ChangePassword

- SettingsDialog

- ValidateState

- FlushQueues

- FlushQueues


<!-- page: PyIMAPIStatus__ChangePassword_meth.html -->

## PyIMAPIStatus.ChangePassword

 ChangePassword(oldPassword, newPassword, ulFlags)

#### Parameters

- oldPassword : unicode

- newPassword : unicode

- ulFlags : int


<!-- page: PyIMAPIStatus__FlushQueues_meth.html -->

## PyIMAPIStatus.FlushQueues

 FlushQueues(ulUIParam, transport, ulFlags)

#### Parameters

- ulUIParam : int

- transport : string

 Blob of data

- ulFlags : int


<!-- page: PyIMAPIStatus__FlushQueues_meth_1.html -->

## PyIMAPIStatus.FlushQueues

 FlushQueues(uiparam, entryID, flags)

#### Parameters

- uiparam : int

- entryID : string

 A blob

- flags : int


<!-- page: PyIMAPIStatus__SettingsDialog_meth.html -->

## PyIMAPIStatus.SettingsDialog

 SettingsDialog(ulUIParam, ulFlags)

#### Parameters

- ulUIParam : int

- ulFlags : int


<!-- page: PyIMAPIStatus__ValidateState_meth.html -->

## PyIMAPIStatus.ValidateState

 ValidateState(ulUIParam, ulFlags)

#### Parameters

- ulUIParam : int

- ulFlags : int


---

<!-- object: PyIMAPITable -->


<!-- page: PyIMAPITable.html -->

---

## PyIMAPITable Object

 An COM interface to MAPI
Derived from PyIUnknown

#### Methods

- GetLastError

 Returns the last error code for the object.

- Advise

 Registers to receive notification of specified events affecting the table.

- SeekRow

 Moves the cursor to a specific position in the table.

- SeekRowApprox

 Moves the cursor to an approximate fractional position in the table.

- GetRowCount

 Returns the total number of rows in the table.

- QueryRows

 Returns one or more rows from a table, beginning at the current cursor position.

- SetColumns

 Defines the particular properties and order of properties to appear as columns in the table.

- GetStatus

 Returns the table's status and type.

- QueryPosition

 Retrieves the current table row position of the cursor, based on a fractional value.

- QueryColumns

 Returns a list of columns for the table.

- Abort

 Stops any asynchronous operations currently in progress for the table.

- FreeBookmark

 Releases the memory associated with a bookmark.

- CreateBookmark

 Marks the table's current position.

- Restrict

 Applies a filter to a table, reducing the row set to only those rows matching the specified criteria.

- FindRow

 Finds the next row in a table that matches specific search criteria.

- SortTable

 Orders the rows of the table based on sort criteria.

- Unadvise

 Cancels the sending of notifications previously set up with a call to the IMAPITable::Advise method.


<!-- page: PyIMAPITable__Abort_meth.html -->

## PyIMAPITable.Abort

 Abort()

Stops any asynchronous operations currently in progress for the table.


<!-- page: PyIMAPITable__Advise_meth.html -->

## PyIMAPITable.Advise

 int = Advise(eventMask, adviseSink )

Registers to receive notification of specified events affecting the table.

#### Parameters

- eventMask : int

- adviseSink : PyIMAPIAdviseSink


<!-- page: PyIMAPITable__CreateBookmark_meth.html -->

## PyIMAPITable.CreateBookmark

 int = CreateBookmark()

Marks the table's current position.


<!-- page: PyIMAPITable__FindRow_meth.html -->

## PyIMAPITable.FindRow

 FindRow(restriction, bookmarkOrigin, flags)

Finds the next row in a table that matches specific search criteria.

#### Parameters

- restriction : PySRestriction

- bookmarkOrigin : int

- flags : int


<!-- page: PyIMAPITable__FreeBookmark_meth.html -->

## PyIMAPITable.FreeBookmark

 FreeBookmark(bookmark)

Releases the memory associated with a bookmark.

#### Parameters

- bookmark : int


<!-- page: PyIMAPITable__GetLastError_meth.html -->

## PyIMAPITable.GetLastError

 MAPIERROR = GetLastError(hr, flags )

Returns the last error code for the object.

#### Parameters

- hr : int

 Contains the error code generated in the previous method call.

- flags : int

 Indicates for format for the output.


<!-- page: PyIMAPITable__GetRowCount_meth.html -->

## PyIMAPITable.GetRowCount

 int = GetRowCount(flags)

Returns the total number of rows in the table.

#### Parameters

- flags : int

 Reserved - must be zero


<!-- page: PyIMAPITable__GetStatus_meth.html -->

## PyIMAPITable.GetStatus

 GetStatus()

Returns the table's status and type.

#### Return Value

Result is a tuple of (tableStatus, tableType)


<!-- page: PyIMAPITable__QueryColumns_meth.html -->

## PyIMAPITable.QueryColumns

 SPropTagArray = QueryColumns(flags)

Returns a list of columns for the table.

#### Parameters

- flags : int


<!-- page: PyIMAPITable__QueryPosition_meth.html -->

## PyIMAPITable.QueryPosition

 QueryPosition()

Retrieves the current table row position of the cursor, based on a fractional value.

#### Return Value

Result is a tuple of (row, numerator, denominator)


<!-- page: PyIMAPITable__QueryRows_meth.html -->

## PyIMAPITable.QueryRows

 SRowSet = QueryRows(rowCount, flags )

Returns one or more rows from a table, beginning at the current cursor position.

#### Parameters

- rowCount : int

 Number of rows to retrieve

- flags : int

 Flags.


<!-- page: PyIMAPITable__Restrict_meth.html -->

## PyIMAPITable.Restrict

 Restrict(restriction, flags)

Applies a filter to a table, reducing the row set to only those rows matching the specified criteria.

#### Parameters

- restriction : PySRestriction

- flags : int


<!-- page: PyIMAPITable__SeekRowApprox_meth.html -->

## PyIMAPITable.SeekRowApprox

 SeekRowApprox(numerator, denominator)

Moves the cursor to an approximate fractional position in the table.

#### Parameters

- numerator : int

 The numerator of the fraction representing the table position

- denominator : int

 The denominator of the fraction representing the table position. This must not be zero.


<!-- page: PyIMAPITable__SeekRow_meth.html -->

## PyIMAPITable.SeekRow

 int = SeekRow(bookmark, rowCount )

Moves the cursor to a specific position in the table.

#### Parameters

- bookmark : int

 The bookmark.

- rowCount : int

#### Return Value

The result is the number of rows processed.


<!-- page: PyIMAPITable__SetColumns_meth.html -->

## PyIMAPITable.SetColumns

 SetColumns(propTags, flags)

Defines the particular properties and order of properties to appear as columns in the table.

#### Parameters

- propTags : SPropTagArray

 Sequence of property tags identifying properties to be included as columns in the table.

- flags : int


<!-- page: PyIMAPITable__SortTable_meth.html -->

## PyIMAPITable.SortTable

 SortTable(sortOrderSet, flags)

Orders the rows of the table based on sort criteria.

#### Parameters

- sortOrderSet : PySSortOrderSet

- flags : int


<!-- page: PyIMAPITable__Unadvise_meth.html -->

## PyIMAPITable.Unadvise

 Unadvise(handle)

Cancels the sending of notifications previously set up with a call to the IMAPITable::Advise method.

#### Parameters

- handle : int

 Handle returned from PyIMAPITable::Advise


---

<!-- object: PyIMachineDebugManager -->


<!-- page: PyIMachineDebugManager.html -->

---

## PyIMachineDebugManager Object

 Description of the interface

#### Methods

- AddApplication

 Description of AddApplication

- RemoveApplication

 Description of RemoveApplication

- EnumApplications

 Description of EnumApplications


<!-- page: PyIMachineDebugManager__AddApplication_meth.html -->

## PyIMachineDebugManager.AddApplication

 AddApplication(pda)

Description of AddApplication.

#### Parameters

- pda : PyIRemoteDebugApplication

 Description for pda


<!-- page: PyIMachineDebugManager__EnumApplications_meth.html -->

## PyIMachineDebugManager.EnumApplications

 EnumApplications()

Description of EnumApplications.


<!-- page: PyIMachineDebugManager__RemoveApplication_meth.html -->

## PyIMachineDebugManager.RemoveApplication

 RemoveApplication(dwAppCookie)

Description of RemoveApplication.

#### Parameters

- dwAppCookie : int

 Description for dwAppCookie


---

<!-- object: PyIMachineDebugManagerEvents -->


<!-- page: PyIMachineDebugManagerEvents.html -->

---

## PyIMachineDebugManagerEvents Object

 Description of the interface

#### Methods

- onAddApplication

 Description of onAddApplication

- onRemoveApplication

 Description of onRemoveApplication


<!-- page: PyIMachineDebugManagerEvents__onAddApplication_meth.html -->

## PyIMachineDebugManagerEvents.onAddApplication

 onAddApplication(pda, dwAppCookie)

Description of onAddApplication.

#### Parameters

- pda : PyIRemoteDebugApplication

 Description for pda

- dwAppCookie : int

 Description for dwAppCookie


<!-- page: PyIMachineDebugManagerEvents__onRemoveApplication_meth.html -->

## PyIMachineDebugManagerEvents.onRemoveApplication

 onRemoveApplication(pda, dwAppCookie)

Description of onRemoveApplication.

#### Parameters

- pda : PyIRemoteDebugApplication

 Description for pda

- dwAppCookie : int

 Description for dwAppCookie


---

<!-- object: PyIMessage -->


<!-- page: PyIMessage.html -->

---

## PyIMessage Object

 An COM interface to MAPI
Derived from PyIMAPIProp

#### Methods

- SetReadFlag

 Sets the read flags for a message

- GetAttachmentTable

 Returns the message's attachment table.

- OpenAttach

 Opens an attachment

- CreateAttach

 Creates an attachment

- DeleteAttach

 Deletes an attachment

- ModifyRecipients

 adds, deletes, or modifies message recipients.

- GetRecipientTable

 Returns the message's recipient table.

- SubmitMessage

 Saves all of the message's properties and marks the message as ready to be sent.


<!-- page: PyIMessage__CreateAttach_meth.html -->

## PyIMessage.CreateAttach

 int, PyIAttach = CreateAttach(interface, flags )

Creates an attachment

#### Parameters

- interface : PyIID

 The interface to use, or None

- flags : int

 Bitmask of flags that controls how the attachment is created.

#### Return Value

The result is a tuple of (attachmentNum, attachmentObject)


<!-- page: PyIMessage__DeleteAttach_meth.html -->

## PyIMessage.DeleteAttach

 DeleteAttach(attachmentNum, ulUIParam, interface, flags)

Deletes an attachment

#### Parameters

- attachmentNum : int

- ulUIParam : int

- interface : PyIMAPIProgress

 The interface to use, or None

- flags : int

 Bitmask of flags that controls the display of a user interface.


<!-- page: PyIMessage__GetAttachmentTable_meth.html -->

## PyIMessage.GetAttachmentTable

 PyIMAPITable = GetAttachmentTable(flags)

Returns the message's attachment table.

#### Parameters

- flags : int

 Bitmask of flags that relate to the creation of the table.


<!-- page: PyIMessage__GetRecipientTable_meth.html -->

## PyIMessage.GetRecipientTable

 PyIMAPITable = GetRecipientTable(flags)

Returns the message's recipient table.

#### Parameters

- flags : int

 Bitmask of flags that relate to the creation of the table.


<!-- page: PyIMessage__ModifyRecipients_meth.html -->

## PyIMessage.ModifyRecipients

 ModifyRecipients(flags, mods)

adds, deletes, or modifies message recipients.

#### Parameters

- flags : int

 Bitmask of flags that controls the recipient changes. If zero is passed for the ulFlags parameter, ModifyRecipients replaces all existing recipients with the recipient list in the mods parameter.

- mods : object

 The list of recipients.


<!-- page: PyIMessage__OpenAttach_meth.html -->

## PyIMessage.OpenAttach

 PyIAttach = OpenAttach(attachmentNum, interface , flags )

Opens an attachment

#### Parameters

- attachmentNum : int

- interface : PyIID

 The interface to use, or None

- flags : int

 Bitmask of flags that controls how the attachment is opened.


<!-- page: PyIMessage__SetReadFlag_meth.html -->

## PyIMessage.SetReadFlag

 SetReadFlag(flag)

Sets the read flags for a message

#### Parameters

- flag : int

 Bitmask of flags that controls the setting of a message's read flag - that is, the message's MSGFLAG_READ flag in its PR_MESSAGE_FLAGS property and the processing of read reports.


<!-- page: PyIMessage__SubmitMessage_meth.html -->

## PyIMessage.SubmitMessage

 SubmitMessage(flags)

Saves all of the message's properties and marks the message as ready to be sent.

#### Parameters

- flags : int

 Flags which specify how the message is submitted.


---

<!-- object: PyIMoniker -->


<!-- page: PyIMoniker.html -->

---

## PyIMoniker Object

 A Python interface to IMoniker

#### Methods

- BindToObject

 Uses the moniker to bind to the object it identifies.

- BindToStorage

 Retrieves an interface object to the storage that contains the object identified by the moniker.

- GetDisplayName

 Gets the display name , which is a user-readable representation of this moniker.

- ComposeWith

 Combines the current moniker with another moniker, creating a new composite moniker.

- Enum

 Supplies an enumerator that can enumerate the components of a composite moniker.

- IsEqual

 Compares this moniker with a specified moniker and indicates whether they are identical.

- IsSystemMoniker

 Indicates whether this moniker is of one of the system-supplied moniker classes.

- Hash

 Calculates a 32-bit integer using the internal state of the moniker.

#### Based On

PyIPersistStream


<!-- page: PyIMoniker__BindToObject_meth.html -->

## PyIMoniker.BindToObject

 PyIUnknown = BindToObject(bindCtx, moniker , iidResult )

Uses the moniker to bind to the object it identifies.

#### Parameters

- bindCtx : PyIBindCtx

 bind context object to be used.

- moniker : PyIMoniker

 If the moniker is part of a composite moniker, otherwise None

- iidResult : IID

 IID of the result object.


<!-- page: PyIMoniker__BindToStorage_meth.html -->

## PyIMoniker.BindToStorage

 PyIUnknown = BindToStorage(bindCtx, moniker , iidResult )

Retrieves an interface object to the storage that contains the object identified by the moniker.

#### Parameters

- bindCtx : PyIBindCtx

 bind context object to be used.

- moniker : PyIMoniker

 If the moniker is part of a composite moniker, otherwise None

- iidResult : IID

 IID of the result object.


<!-- page: PyIMoniker__ComposeWith_meth.html -->

## PyIMoniker.ComposeWith

 PyIMoniker = ComposeWith(mkRight, fOnlyIfNotGeneric )

Combines the current moniker with another moniker, creating a new composite moniker.

#### Parameters

- mkRight : PyIMoniker

 The IMoniker interface on the moniker to compose onto the end of this moniker.

- fOnlyIfNotGeneric : int

 If TRUE, the caller requires a non-generic composition, so the operation should proceed only if pmkRight is a moniker class that this moniker can compose with in some way other than forming a generic composite. If FALSE, the method can create a generic composite if necessary.


<!-- page: PyIMoniker__Enum_meth.html -->

## PyIMoniker.Enum

 PyIEnumMoniker = Enum(fForward)

Supplies an enumerator that can enumerate the components of a composite moniker.

#### Parameters

- fForward=True : int

 If TRUE, enumerates the monikers from left to right. If FALSE, enumerates from right to left.


<!-- page: PyIMoniker__GetDisplayName_meth.html -->

## PyIMoniker.GetDisplayName

 string = GetDisplayName(bindCtx, moniker )

Gets the display name , which is a user-readable representation of this moniker.

#### Parameters

- bindCtx : PyIBindCtx

 bind context object to be used.

- moniker : PyIMoniker

 If the moniker is part of a composite moniker, otherwise None


<!-- page: PyIMoniker__Hash_meth.html -->

## PyIMoniker.Hash

 int = Hash()

Calculates a 32-bit integer using the internal state of the moniker.


<!-- page: PyIMoniker__IsEqual_meth.html -->

## PyIMoniker.IsEqual

 int = IsEqual(other)

Compares this moniker with a specified moniker and indicates whether they are identical.

#### Parameters

- other : PyIMoniker

 The moniker to compare


<!-- page: PyIMoniker__IsSystemMoniker_meth.html -->

## PyIMoniker.IsSystemMoniker

 int = IsSystemMoniker()

Indicates whether this moniker is of one of the system-supplied moniker classes.


---

<!-- object: PyIMsgServiceAdmin -->


<!-- page: PyIMsgServiceAdmin.html -->

---

## PyIMsgServiceAdmin Object

 An COM interface to MAPI's IMsgServiceAdmin interface.
Derived from PyIUnknown

#### Methods

- GetLastError

 Returns the last error code for the object.

- CreateMsgService

 Creates a message service.

- ConfigureMsgService

 Reconfigures a message service.

- GetMsgServiceTable

 Retrieves a table of services.

- GetProviderTable

 Retrieves a table of service providers.

- DeleteMsgService

 Deletes the specified service

- RenameMsgService

 Renames the specified service

- OpenProfileSection

 Opens a profile section

- AdminProviders

 Returns an object providing access to a provider administration object.


<!-- page: PyIMsgServiceAdmin__AdminProviders_meth.html -->

## PyIMsgServiceAdmin.AdminProviders

 PyIProfSect = AdminProviders(uuid, flags )

Returns an object providing access to a provider administration object.

#### Parameters

- uuid : PyIID

 The ID of the service

- flags : int


<!-- page: PyIMsgServiceAdmin__ConfigureMsgService_meth.html -->

## PyIMsgServiceAdmin.ConfigureMsgService

 ConfigureMsgService(iid, ulUIParam, ulFlags, [SPropValue, ...])

Reconfigures a message service.

#### Parameters

- iid : PyIID

 The unique identifier for the message service to configure.

- ulUIParam : int

 Handle of the parent window for the configuration property sheet.

- ulFlags : int

 Bitmask of flags that controls the display of the property sheet.

- [SPropValue, ...] : [values, ...]

 Property values describing the properties to display in the property sheet. Should not be None if the service is to be configured without a message service.


<!-- page: PyIMsgServiceAdmin__CreateMsgService_meth.html -->

## PyIMsgServiceAdmin.CreateMsgService

 CreateMsgService(serviceName, displayName, uiParam, flags)

Creates a message service.

#### Parameters

- serviceName : string

 The name of the service.

- displayName : string

 Display name of the service, or None

- uiParam=0 : int

 A handle of the parent window for any dialog boxes or windows that this method displays.

- flags : int

 A bitmask of flags that controls how the message service is installed.


<!-- page: PyIMsgServiceAdmin__DeleteMsgService_meth.html -->

## PyIMsgServiceAdmin.DeleteMsgService

 DeleteMsgService(uuid)

Deletes the specified service

#### Parameters

- uuid : PyIID

 The ID of the service


<!-- page: PyIMsgServiceAdmin__GetLastError_meth.html -->

## PyIMsgServiceAdmin.GetLastError

 MAPIERROR = GetLastError(hr, flags )

Returns the last error code for the object.

#### Parameters

- hr : int

 Contains the error code generated in the previous method call.

- flags : int

 Indicates for format for the output.


<!-- page: PyIMsgServiceAdmin__GetMsgServiceTable_meth.html -->

## PyIMsgServiceAdmin.GetMsgServiceTable

 PyIMAPITable = GetMsgServiceTable(flags)

Retrieves a table of services.

#### Parameters

- flags : int


<!-- page: PyIMsgServiceAdmin__GetProviderTable_meth.html -->

## PyIMsgServiceAdmin.GetProviderTable

 PyIMAPITable = GetProviderTable(flags)

Retrieves a table of service providers.

#### Parameters

- flags : int


<!-- page: PyIMsgServiceAdmin__OpenProfileSection_meth.html -->

## PyIMsgServiceAdmin.OpenProfileSection

 PyIProfSect = OpenProfileSection(uuid, iid , flags )

Opens a profile section

#### Parameters

- uuid : PyIID

 The ID of the service

- iid : PyIID

 The IID of the resulting object, or None for the default

- flags : int


<!-- page: PyIMsgServiceAdmin__RenameMsgService_meth.html -->

## PyIMsgServiceAdmin.RenameMsgService

 RenameMsgService(uuid, flags, newName)

Renames the specified service

#### Parameters

- uuid : PyIID

 The ID of the service

- flags : int

- newName : string

 The new name for the service.

#### Comments

 This is deprecated, and there is no replacement referenced to use instead.


---

<!-- object: PyIMsgStore -->


<!-- page: PyIMsgStore.html -->

---

## PyIMsgStore Object

 An COM interface to MAPI
Derived from PyIMAPIProp

#### Methods

- OpenEntry

 Opens a folder or message and returns an interface object for further access.

- StoreLogoff

 Enables the orderly logoff of the message store.

- GetReceiveFolder

 Obtains the folder that was established as the destination for incoming messages of a specified message class or the default receive folder for the message store.

- GetReceiveFolderTable

 provides access to the receive folder table, a table that includes information about all of the receive folders for the message store.

- CompareEntryIDs

 Compares two entry identifiers belonging to a particular address book provider to determine if they refer to the same address book object

- GetLastError

 Returns the last error code for the object.

- AbortSubmit

 Attempts to remove a message from the outgoing queue.

- Advise

 Registers to receive notification of specified events that affect the message store.

- Unadvise

 Cancels the sending of notifications previously set up with a call to the IMsgStore::Advise method.


<!-- page: PyIMsgStore__AbortSubmit_meth.html -->

## PyIMsgStore.AbortSubmit

 int = AbortSubmit(entryId, flags )

Attempts to remove a message from the outgoing queue.

#### Parameters

- entryId : string

 The entry ID of the item to be aborted.

- flags=0 : int

 Reserved - must be zero.


<!-- page: PyIMsgStore__Advise_meth.html -->

## PyIMsgStore.Advise

 Advise(entryId, eventMask, adviseSink)

Registers to receive notification of specified events that affect the message store.

#### Parameters

- entryId : string

 entry identifier of the folder or message about which notifications should be generated, or None

- eventMask : int

 A mask of values that indicate the types of notification events.

- adviseSink : PyIMAPIAdviseSink

 An advise sink.


<!-- page: PyIMsgStore__CompareEntryIDs_meth.html -->

## PyIMsgStore.CompareEntryIDs

 int = CompareEntryIDs(entryId, entryId , flags )

Compares two entry identifiers belonging to a particular address book provider to determine if they refer to the same address book object

#### Parameters

- entryId : string

 The first entry ID to be compared

- entryId : string

 The second entry ID to be compared

- flags=0 : int

 Reserved - must be zero.

#### Return Value

The result is set to TRUE if the two entry identifiers refer to the same object, and FALSE otherwise.


<!-- page: PyIMsgStore__GetLastError_meth.html -->

## PyIMsgStore.GetLastError

 MAPIERROR = GetLastError(hr, flags )

Returns the last error code for the object.

#### Parameters

- hr : int

 Contains the error code generated in the previous method call.

- flags : int

 Indicates for format for the output.


<!-- page: PyIMsgStore__GetReceiveFolderTable_meth.html -->

## PyIMsgStore.GetReceiveFolderTable

 PyIMAPITable = GetReceiveFolderTable(flags)

provides access to the receive folder table, a table that includes information about all of the receive folders for the message store.

#### Parameters

- flags : int

 Bitmask of flags that controls table access


<!-- page: PyIMsgStore__GetReceiveFolder_meth.html -->

## PyIMsgStore.GetReceiveFolder

 PyIID, string = GetReceiveFolder(messageClass, flags )

Obtains the folder that was established as the destination for incoming messages of a specified message class or the default receive folder for the message store.

#### Parameters

- messageClass=None : string

 Message class that is associated with a receive folder. If this parameter is set to None or an empty string, GetReceiveFolder returns the default receive folder for the message store.

- flags=0 : int


<!-- page: PyIMsgStore__OpenEntry_meth.html -->

## PyIMsgStore.OpenEntry

 PyIInterface = OpenEntry(entryId, iid , flags )

Opens a folder or message and returns an interface object for further access.

#### Parameters

- entryId : string

 The entryID of the object

- iid : PyIID

 The IID of the object to return, or None for the default IID

- flags : int

 Bitmask of flags that controls how the object is opened.


<!-- page: PyIMsgStore__StoreLogoff_meth.html -->

## PyIMsgStore.StoreLogoff

 PyIInterface = StoreLogoff(flags)

Enables the orderly logoff of the message store.

#### Parameters

- flags : int

 Bitmask of flags that controls how the message store is closed.


<!-- page: PyIMsgStore__Unadvise_meth.html -->

## PyIMsgStore.Unadvise

 Unadvise(connection)

Cancels the sending of notifications previously set up with a call to the IMsgStore::Advise method.

#### Parameters

- connection : int

 Connection number returned from PyIMsgStore::Advise


---

<!-- object: PyINPUT_RECORD -->


<!-- page: PyINPUT_RECORD.html -->

---

## PyINPUT_RECORD Object

 Interface to the INPUT_RECORD struct used with console IO functions. Create using PyINPUT_RECORDType(EventType)

#### Comments

 Only attributes that apply to each particular EventType can be accessed:
 KEY_EVENT: KeyDown, RepeatCount, VirtualKeyCode, VirtualScanCode, ControlKeyState
 MOUSE_EVENT: MousePosition, ButtonState, ControlKeyState, EventFlags
 WINDOW_BUFFER_SIZE_EVENT: Size
 FOCUS_EVENT: SetFocus
 MENU_EVENT: CommandId

#### Properties

- int EventType
 One of KEY_EVENT, MOUSE_EVENT, WINDOW_BUFFER_SIZE_EVENT, MENU_EVENT, FOCUS_EVENT. Cannot be changed after object is created

- boolean KeyDown
 True for a key press, False for key release

- int RepeatCount
 Nbr of repeats generated (key was held down if >1)

- int VirtualKeyCode
 Device-independent key code, win32con.VK_*

- int VirtualScanCode
 Device-dependent scan code generated by keyboard

- PyUnicode Char
 Single unicode character generated by the keypress

- int ControlKeyState
 State of modifier keys, combination of CAPSLOCK_ON, ENHANCED_KEY, LEFT_ALT_PRESSED, LEFT_CTRL_PRESSED, NUMLOCK_ON, RIGHT_ALT_PRESSED, RIGHT_CTRL_PRESSED, SCROLLLOCK_ON, SHIFT_PRESSED

- int ButtonState
 Bitmask representing which mouse buttons were pressed.

- int EventFlags
 DOUBLE_CLICK, MOUSE_MOVED or MOUSE_WHEELED, or 0. If 0, indicates a mouse button press

- PyCOORD MousePosition
 Position in character coordinates

- PyCOORD Size
 New size of screen buffer in character rows/columns

- boolean SetFocus
 Reserved - Used only with type FOCUS_EVENT. This event is Reserved, and should be ignored.

- int CommandId
 Used only with event type MENU_EVENT, which is reserved and should not be used


---

<!-- object: PyINameSpaceTreeControl -->


<!-- page: PyINameSpaceTreeControl.html -->

---

## PyINameSpaceTreeControl Object

 Description of the interface

#### Methods

- Initialize

 Description of Initialize

- TreeAdvise

 Description of TreeAdvise

- TreeUnadvise

 Description of TreeUnadvise

- AppendRoot

 Description of AppendRoot

- InsertRoot

 Description of InsertRoot

- RemoveRoot

 Description of RemoveRoot

- RemoveAllRoots

 Description of RemoveAllRoots

- GetRootItems

 Description of GetRootItems

- SetItemState

 Description of SetItemState

- GetItemState

 Description of GetItemState

- GetSelectedItems

 Description of GetSelectedItems

- GetItemCustomState

 Description of GetItemCustomState

- SetItemCustomState

 Description of SetItemCustomState

- EnsureItemVisible

 Description of EnsureItemVisible

- SetTheme

 Description of SetTheme

- GetNextItem

 Description of GetNextItem

- HitTest

 Description of HitTest

- GetItemRect

 Description of GetItemRect

- CollapseAll

 Description of CollapseAll


<!-- page: PyINameSpaceTreeControl__AppendRoot_meth.html -->

## PyINameSpaceTreeControl.AppendRoot

 AppendRoot(psiRoot, grfEnumFlags, grfRootStyle, pif)

Description of AppendRoot.

#### Parameters

- psiRoot : PyIShellItem

 Description for psiRoot

- grfEnumFlags : int

 Description for grfEnumFlags

- grfRootStyle : int

 Description for grfRootStyle

- pif : PyIShellItemFilter

 Description for pif


<!-- page: PyINameSpaceTreeControl__CollapseAll_meth.html -->

## PyINameSpaceTreeControl.CollapseAll

 CollapseAll()

Description of CollapseAll.


<!-- page: PyINameSpaceTreeControl__EnsureItemVisible_meth.html -->

## PyINameSpaceTreeControl.EnsureItemVisible

 EnsureItemVisible(psi)

Description of EnsureItemVisible.

#### Parameters

- psi : PyIShellItem

 Description for psi


<!-- page: PyINameSpaceTreeControl__GetItemCustomState_meth.html -->

## PyINameSpaceTreeControl.GetItemCustomState

 GetItemCustomState(psi)

Description of GetItemCustomState.

#### Parameters

- psi : PyIShellItem

 Description for psi


<!-- page: PyINameSpaceTreeControl__GetItemRect_meth.html -->

## PyINameSpaceTreeControl.GetItemRect

 GetItemRect()

Description of GetItemRect.


<!-- page: PyINameSpaceTreeControl__GetItemState_meth.html -->

## PyINameSpaceTreeControl.GetItemState

 GetItemState(psi, nstcisMask)

Description of GetItemState.

#### Parameters

- psi : PyIShellItem

 Description for psi

- nstcisMask : int

 Description for nstcisMask


<!-- page: PyINameSpaceTreeControl__GetNextItem_meth.html -->

## PyINameSpaceTreeControl.GetNextItem

 GetNextItem(psi, nstcgi)

Description of GetNextItem.

#### Parameters

- psi : PyIShellItem

 Description for psi

- nstcgi : int

 Description for nstcgi


<!-- page: PyINameSpaceTreeControl__GetRootItems_meth.html -->

## PyINameSpaceTreeControl.GetRootItems

 GetRootItems()

Description of GetRootItems.


<!-- page: PyINameSpaceTreeControl__GetSelectedItems_meth.html -->

## PyINameSpaceTreeControl.GetSelectedItems

 GetSelectedItems()

Description of GetSelectedItems.


<!-- page: PyINameSpaceTreeControl__HitTest_meth.html -->

## PyINameSpaceTreeControl.HitTest

 HitTest(pt)

Description of HitTest.

#### Parameters

- pt : (int, int)

 Description for ppt


<!-- page: PyINameSpaceTreeControl__Initialize_meth.html -->

## PyINameSpaceTreeControl.Initialize

 Initialize(hwndParent, prc, nsctsFlags)

Description of Initialize.

#### Parameters

- hwndParent : int/long

 Description for hwndParent

- prc : (int, int, int, int)

 Description for prc

- nsctsFlags : int

 Description for nsctsFlags


<!-- page: PyINameSpaceTreeControl__InsertRoot_meth.html -->

## PyINameSpaceTreeControl.InsertRoot

 InsertRoot(iIndex, psiRoot, grfEnumFlags, grfRootStyle, pif)

Description of InsertRoot.

#### Parameters

- iIndex : int

 Description for iIndex

- psiRoot : PyIShellItem

 Description for psiRoot

- grfEnumFlags : int

 Description for grfEnumFlags

- grfRootStyle : int

 Description for grfRootStyle

- pif : PyIShellItemFilter

 Description for pif


<!-- page: PyINameSpaceTreeControl__RemoveAllRoots_meth.html -->

## PyINameSpaceTreeControl.RemoveAllRoots

 RemoveAllRoots()

Description of RemoveAllRoots.


<!-- page: PyINameSpaceTreeControl__RemoveRoot_meth.html -->

## PyINameSpaceTreeControl.RemoveRoot

 RemoveRoot(psiRoot)

Description of RemoveRoot.

#### Parameters

- psiRoot : PyIShellItem

 Description for psiRoot


<!-- page: PyINameSpaceTreeControl__SetItemCustomState_meth.html -->

## PyINameSpaceTreeControl.SetItemCustomState

 SetItemCustomState(psi, iStateNumber)

Description of SetItemCustomState.

#### Parameters

- psi : PyIShellItem

 Description for psi

- iStateNumber : int

 Description for iStateNumber


<!-- page: PyINameSpaceTreeControl__SetItemState_meth.html -->

## PyINameSpaceTreeControl.SetItemState

 SetItemState(psi, nstcisMask, nstcisFlags)

Description of SetItemState.

#### Parameters

- psi : PyIShellItem

 Description for psi

- nstcisMask : int

 Description for nstcisMask

- nstcisFlags : int

 Description for nstcisFlags


<!-- page: PyINameSpaceTreeControl__SetTheme_meth.html -->

## PyINameSpaceTreeControl.SetTheme

 SetTheme(pszTheme)

Description of SetTheme.

#### Parameters

- pszTheme : unicode

 Description for pszTheme


<!-- page: PyINameSpaceTreeControl__TreeAdvise_meth.html -->

## PyINameSpaceTreeControl.TreeAdvise

 TreeAdvise(punk)

Description of TreeAdvise.

#### Parameters

- punk : PyIUnknown

 Description for punk


<!-- page: PyINameSpaceTreeControl__TreeUnadvise_meth.html -->

## PyINameSpaceTreeControl.TreeUnadvise

 TreeUnadvise(dwCookie)

Description of TreeUnadvise.

#### Parameters

- dwCookie : int

 Description for dwCookie


---

<!-- object: PyINamedPropertyStore -->


<!-- page: PyINamedPropertyStore.html -->

---

## PyINamedPropertyStore Object

 Contains a collection of properties indentified by name

#### Methods

- GetNamedValue

 Retrieves a property value by name

- SetNamedValue

 Sets the value of a property

- GetNameCount

 Retrieves the number of named properties in the store

- GetNameAt

 Retrieves a property name by zero-based index


<!-- page: PyINamedPropertyStore__GetNameAt_meth.html -->

## PyINamedPropertyStore.GetNameAt

 str = GetNameAt(Index)

Retrieves a property name by zero-based index

#### Parameters

- Index : int

 Index of the property name


<!-- page: PyINamedPropertyStore__GetNameCount_meth.html -->

## PyINamedPropertyStore.GetNameCount

 int = GetNameCount()

Retrieves the number of named properties in the store


<!-- page: PyINamedPropertyStore__GetNamedValue_meth.html -->

## PyINamedPropertyStore.GetNamedValue

 PyPROPVARIANT = GetNamedValue(Name)

Retrieves a property value by name

#### Parameters

- Name : str

 Name of the property


<!-- page: PyINamedPropertyStore__SetNamedValue_meth.html -->

## PyINamedPropertyStore.SetNamedValue

 SetNamedValue(propvar)

Sets the value of a property

#### Parameters

- propvar : Py__RPC__in REFPROPVARIANT

 Description for propvar


---

<!-- object: PyIObjectArray -->


<!-- page: PyIObjectArray.html -->

---

## PyIObjectArray Object

 Holds a collection of interface objects

#### Methods

- GetCount

 Returns number of objects in collection

- GetAt

 Retrieves an item by zero-based index


<!-- page: PyIObjectArray__GetAt_meth.html -->

## PyIObjectArray.GetAt

 PyIUnknown = GetAt(Index, riid )

Retrieves an item by zero-based index

#### Parameters

- Index : int

 Index of item to retrieve

- riid=IID_IUnknown : PyIID

 The interface to return


<!-- page: PyIObjectArray__GetCount_meth.html -->

## PyIObjectArray.GetCount

 int = GetCount()

Returns number of objects in collection


---

<!-- object: PyIObjectCollection -->


<!-- page: PyIObjectCollection.html -->

---

## PyIObjectCollection Object

 Modifiable container for a number of IUnknown objects

#### Methods

- AddObject

 Adds a single object to the collection

- AddFromArray

 Adds a number of objects contained in an PyIObjectArray collection

- RemoveObjectAt

 Removes a single object from the collection

- Clear

 Empties the container

#### Based On

PyIObjectArray


<!-- page: PyIObjectCollection__AddFromArray_meth.html -->

## PyIObjectCollection.AddFromArray

 AddFromArray(Source)

Adds a number of objects contained in an PyIObjectArray collection

#### Parameters

- Source : PyIObjectArray

 Objects to be added to the collection


<!-- page: PyIObjectCollection__AddObject_meth.html -->

## PyIObjectCollection.AddObject

 AddObject(punk)

Adds a single object to the collection

#### Parameters

- punk : PyIUnknown

 Object to be added


<!-- page: PyIObjectCollection__Clear_meth.html -->

## PyIObjectCollection.Clear

 Clear()

Empties the container.


<!-- page: PyIObjectCollection__RemoveObjectAt_meth.html -->

## PyIObjectCollection.RemoveObjectAt

 RemoveObjectAt(Index)

Removes a single object from the collection

#### Parameters

- Index : int

 Zero-based index of item to remove


---

<!-- object: PyIObjectWithPropertyKey -->


<!-- page: PyIObjectWithPropertyKey.html -->

---

## PyIObjectWithPropertyKey Object

 Interface implemented by objects that have an associated property id

#### Methods

- SetPropertyKey

 Sets the property id

- GetPropertyKey

 Returns the property id


<!-- page: PyIObjectWithPropertyKey__GetPropertyKey_meth.html -->

## PyIObjectWithPropertyKey.GetPropertyKey

 PyPROPERTYKEY = GetPropertyKey()

Returns the property id


<!-- page: PyIObjectWithPropertyKey__SetPropertyKey_meth.html -->

## PyIObjectWithPropertyKey.SetPropertyKey

 SetPropertyKey(key)

Sets the property id

#### Parameters

- key : PyPROPERTYKEY

 The identifier of the property


---

<!-- object: PyIObjectWithSite -->


<!-- page: PyIObjectWithSite.html -->

---

## PyIObjectWithSite Object

 Description of the interface

#### Methods

- SetSite

 Description of SetSite

- GetSite

 Description of GetSite


<!-- page: PyIObjectWithSite__GetSite_meth.html -->

## PyIObjectWithSite.GetSite

 GetSite(riid)

Description of GetSite.

#### Parameters

- riid : PyIID

 Description for riid


<!-- page: PyIObjectWithSite__SetSite_meth.html -->

## PyIObjectWithSite.SetSite

 SetSite(pUnkSite)

Description of SetSite.

#### Parameters

- pUnkSite : PyIUnknown *

 Description for pUnkSite


---

<!-- object: PyIOleClientSite -->


<!-- page: PyIOleClientSite.html -->

---

## PyIOleClientSite Object

 Description of the interface

#### Methods

- SaveObject

 Description of SaveObject

- GetMoniker

 Description of GetMoniker

- GetContainer

 Description of GetContainer

- ShowObject

 Description of ShowObject

- OnShowWindow

 Description of OnShowWindow

- RequestNewObjectLayout

 Description of RequestNewObjectLayout


<!-- page: PyIOleClientSite__GetContainer_meth.html -->

## PyIOleClientSite.GetContainer

 GetContainer()

Description of GetContainer.


<!-- page: PyIOleClientSite__GetMoniker_meth.html -->

## PyIOleClientSite.GetMoniker

 GetMoniker(dwAssign, dwWhichMoniker)

Description of GetMoniker.

#### Parameters

- dwAssign : int

 Description for dwAssign

- dwWhichMoniker : int

 Description for dwWhichMoniker


<!-- page: PyIOleClientSite__OnShowWindow_meth.html -->

## PyIOleClientSite.OnShowWindow

 OnShowWindow(fShow)

Description of OnShowWindow.

#### Parameters

- fShow : int

 Description for fShow


<!-- page: PyIOleClientSite__RequestNewObjectLayout_meth.html -->

## PyIOleClientSite.RequestNewObjectLayout

 RequestNewObjectLayout()

Description of RequestNewObjectLayout.


<!-- page: PyIOleClientSite__SaveObject_meth.html -->

## PyIOleClientSite.SaveObject

 SaveObject()

Description of SaveObject.


<!-- page: PyIOleClientSite__ShowObject_meth.html -->

## PyIOleClientSite.ShowObject

 ShowObject()

Description of ShowObject.


---

<!-- object: PyIOleCommandTarget -->


<!-- page: PyIOleCommandTarget.html -->

---

## PyIOleCommandTarget Object

 Description of the interface

#### Methods

- QueryStatus

 Description of QueryStatus

- Exec

 Description of Exec


<!-- page: PyIOleCommandTarget__Exec_meth.html -->

## PyIOleCommandTarget.Exec

 Exec()

Description of Exec.


<!-- page: PyIOleCommandTarget__QueryStatus_meth.html -->

## PyIOleCommandTarget.QueryStatus

 QueryStatus()

Description of QueryStatus.


---

<!-- object: PyIOleControl -->


<!-- page: PyIOleControl.html -->

---

## PyIOleControl Object

 Description of the interface

#### Methods

- GetControlInfo

 Description of GetControlInfo

- OnMnemonic

 Description of OnMnemonic

- OnAmbientPropertyChange

 Description of OnAmbientPropertyChange

- FreezeEvents

 Description of FreezeEvents


<!-- page: PyIOleControl__FreezeEvents_meth.html -->

## PyIOleControl.FreezeEvents

 FreezeEvents(bFreeze)

Description of FreezeEvents.

#### Parameters

- bFreeze : int

 Description for bFreeze


<!-- page: PyIOleControl__GetControlInfo_meth.html -->

## PyIOleControl.GetControlInfo

 GetControlInfo()

Description of GetControlInfo.


<!-- page: PyIOleControl__OnAmbientPropertyChange_meth.html -->

## PyIOleControl.OnAmbientPropertyChange

 OnAmbientPropertyChange(dispID)

Description of OnAmbientPropertyChange.

#### Parameters

- dispID : long

 Description for dispID


<!-- page: PyIOleControl__OnMnemonic_meth.html -->

## PyIOleControl.OnMnemonic

 OnMnemonic(msg)

Description of OnMnemonic.

#### Parameters

- msg : iiiii(ii)

 A tuple representing a MSG structure.


---

<!-- object: PyIOleControlSite -->


<!-- page: PyIOleControlSite.html -->

---

## PyIOleControlSite Object

 Description of the interface

#### Methods

- OnControlInfoChanged

 Description of OnControlInfoChanged

- LockInPlaceActive

 Description of LockInPlaceActive

- GetExtendedControl

 Description of GetExtendedControl

- TransformCoords

 Description of TransformCoords

- TranslateAccelerator

 Description of TranslateAccelerator

- OnFocus

 Description of OnFocus

- ShowPropertyFrame

 Description of ShowPropertyFrame


<!-- page: PyIOleControlSite__GetExtendedControl_meth.html -->

## PyIOleControlSite.GetExtendedControl

 GetExtendedControl()

Description of GetExtendedControl.


<!-- page: PyIOleControlSite__LockInPlaceActive_meth.html -->

## PyIOleControlSite.LockInPlaceActive

 LockInPlaceActive(fLock)

Description of LockInPlaceActive.

#### Parameters

- fLock : int

 Description for fLock


<!-- page: PyIOleControlSite__OnControlInfoChanged_meth.html -->

## PyIOleControlSite.OnControlInfoChanged

 OnControlInfoChanged()

Description of OnControlInfoChanged.


<!-- page: PyIOleControlSite__OnFocus_meth.html -->

## PyIOleControlSite.OnFocus

 OnFocus(fGotFocus)

Description of OnFocus.

#### Parameters

- fGotFocus : int

 Description for fGotFocus


<!-- page: PyIOleControlSite__ShowPropertyFrame_meth.html -->

## PyIOleControlSite.ShowPropertyFrame

 ShowPropertyFrame()

Description of ShowPropertyFrame.


<!-- page: PyIOleControlSite__TransformCoords_meth.html -->

## PyIOleControlSite.TransformCoords

 TransformCoords(PtlHimetric, pPtfContainer, dwFlags)

Description of TransformCoords.

#### Parameters

- PtlHimetric : (int, int)

 Description for pPtlHimetric

- pPtfContainer : (float, float))

 Description for pPtfContainer

- dwFlags : int

 Description for dwFlags

#### Return Value

The result is a tuple of the transformed input points - ie, a tuple of ((int, int), (float, float))


<!-- page: PyIOleControlSite__TranslateAccelerator_meth.html -->

## PyIOleControlSite.TranslateAccelerator

 TranslateAccelerator(pMsg, grfModifiers)

Description of TranslateAccelerator.

#### Parameters

- pMsg : PyMSG

 Description for pMsg

- grfModifiers : int

 Description for grfModifiers


---

<!-- object: PyIOleInPlaceActiveObject -->


<!-- page: PyIOleInPlaceActiveObject.html -->

---

## PyIOleInPlaceActiveObject Object

 Description of the interface

#### Methods

- TranslateAccelerator

 Description of TranslateAccelerator

- OnFrameWindowActivate

 Description of OnFrameWindowActivate

- OnDocWindowActivate

 Description of OnDocWindowActivate

- ResizeBorder

 Description of ResizeBorder

- EnableModeless

 Description of EnableModeless


<!-- page: PyIOleInPlaceActiveObject__EnableModeless_meth.html -->

## PyIOleInPlaceActiveObject.EnableModeless

 EnableModeless(fEnable)

Description of EnableModeless.

#### Parameters

- fEnable : int

 Description for fEnable


<!-- page: PyIOleInPlaceActiveObject__OnDocWindowActivate_meth.html -->

## PyIOleInPlaceActiveObject.OnDocWindowActivate

 OnDocWindowActivate(fActivate)

Description of OnDocWindowActivate.

#### Parameters

- fActivate : int

 Description for fActivate


<!-- page: PyIOleInPlaceActiveObject__OnFrameWindowActivate_meth.html -->

## PyIOleInPlaceActiveObject.OnFrameWindowActivate

 OnFrameWindowActivate(fActivate)

Description of OnFrameWindowActivate.

#### Parameters

- fActivate : int

 Description for fActivate


<!-- page: PyIOleInPlaceActiveObject__ResizeBorder_meth.html -->

## PyIOleInPlaceActiveObject.ResizeBorder

 ResizeBorder(rcBorder, pUIWindow, fFrameWindow)

Description of ResizeBorder.

#### Parameters

- rcBorder : (int, int, int, int)

 Description for prcBorder

- pUIWindow : PyIOleInPlaceUIWindow

 Description for pUIWindow

- fFrameWindow : int

 Description for fFrameWindow


<!-- page: PyIOleInPlaceActiveObject__TranslateAccelerator_meth.html -->

## PyIOleInPlaceActiveObject.TranslateAccelerator

 TranslateAccelerator(lpmsg)

Description of TranslateAccelerator.

#### Parameters

- lpmsg : PyMSG

 Description for lpmsg


---

<!-- object: PyIOleInPlaceFrame -->


<!-- page: PyIOleInPlaceFrame.html -->

---

## PyIOleInPlaceFrame Object

 Description of the interface

#### Methods

- InsertMenus

 Description of InsertMenus

- SetMenu

 Description of SetMenu

- RemoveMenus

 Description of RemoveMenus

- SetStatusText

 Description of SetStatusText

- EnableModeless

 Description of EnableModeless

- TranslateAccelerator

 Description of TranslateAccelerator


<!-- page: PyIOleInPlaceFrame__EnableModeless_meth.html -->

## PyIOleInPlaceFrame.EnableModeless

 EnableModeless(fEnable)

Description of EnableModeless.

#### Parameters

- fEnable : int

 Description for fEnable


<!-- page: PyIOleInPlaceFrame__InsertMenus_meth.html -->

## PyIOleInPlaceFrame.InsertMenus

 InsertMenus(hmenuShared, menuWidths)

Description of InsertMenus.

#### Parameters

- hmenuShared : int/long

 Description for hmenuShared

- menuWidths : PyOLEMENUGROUPWIDTHS


<!-- page: PyIOleInPlaceFrame__RemoveMenus_meth.html -->

## PyIOleInPlaceFrame.RemoveMenus

 RemoveMenus(hmenuShared)

Description of RemoveMenus.

#### Parameters

- hmenuShared : int/long

 Description for hmenuShared


<!-- page: PyIOleInPlaceFrame__SetMenu_meth.html -->

## PyIOleInPlaceFrame.SetMenu

 SetMenu(hmenuShared, holemenu, hwndActiveObject)

Description of SetMenu.

#### Parameters

- hmenuShared : int/long

 Description for hmenuShared

- holemenu : int/long

 Description for holemenu

- hwndActiveObject : int/long

 Description for hwndActiveObject


<!-- page: PyIOleInPlaceFrame__SetStatusText_meth.html -->

## PyIOleInPlaceFrame.SetStatusText

 SetStatusText(pszStatusText)

Description of SetStatusText.

#### Parameters

- pszStatusText : unicode

 Description for pszStatusText


<!-- page: PyIOleInPlaceFrame__TranslateAccelerator_meth.html -->

## PyIOleInPlaceFrame.TranslateAccelerator

 TranslateAccelerator(lpmsg, wID)

Description of TranslateAccelerator.

#### Parameters

- lpmsg : PyMSG

 Description for lpmsg

- wID : int

 Description for wID


---

<!-- object: PyIOleInPlaceObject -->


<!-- page: PyIOleInPlaceObject.html -->

---

## PyIOleInPlaceObject Object

 Description of the interface

#### Methods

- InPlaceDeactivate

 Description of InPlaceDeactivate

- UIDeactivate

 Description of UIDeactivate

- SetObjectRects

 Description of SetObjectRects

- ReactivateAndUndo

 Description of ReactivateAndUndo


<!-- page: PyIOleInPlaceObject__InPlaceDeactivate_meth.html -->

## PyIOleInPlaceObject.InPlaceDeactivate

 InPlaceDeactivate()

Description of InPlaceDeactivate.


<!-- page: PyIOleInPlaceObject__ReactivateAndUndo_meth.html -->

## PyIOleInPlaceObject.ReactivateAndUndo

 ReactivateAndUndo()

Description of ReactivateAndUndo.


<!-- page: PyIOleInPlaceObject__SetObjectRects_meth.html -->

## PyIOleInPlaceObject.SetObjectRects

 SetObjectRects()

Description of SetObjectRects.


<!-- page: PyIOleInPlaceObject__UIDeactivate_meth.html -->

## PyIOleInPlaceObject.UIDeactivate

 UIDeactivate()

Description of UIDeactivate.


---

<!-- object: PyIOleInPlaceSite -->


<!-- page: PyIOleInPlaceSite.html -->

---

## PyIOleInPlaceSite Object

 Description of the interface

#### Methods

- CanInPlaceActivate

 Description of CanInPlaceActivate

- OnInPlaceActivate

 Description of OnInPlaceActivate

- OnUIActivate

 Description of OnUIActivate

- GetWindowContext

 Description of GetWindowContext

- Scroll

 Description of Scroll

- OnUIDeactivate

 Description of OnUIDeactivate

- OnInPlaceDeactivate

 Description of OnInPlaceDeactivate

- DiscardUndoState

 Description of DiscardUndoState

- DeactivateAndUndo

 Description of DeactivateAndUndo

- OnPosRectChange

 Description of OnPosRectChange


<!-- page: PyIOleInPlaceSite__CanInPlaceActivate_meth.html -->

## PyIOleInPlaceSite.CanInPlaceActivate

 CanInPlaceActivate()

Description of CanInPlaceActivate.


<!-- page: PyIOleInPlaceSite__DeactivateAndUndo_meth.html -->

## PyIOleInPlaceSite.DeactivateAndUndo

 DeactivateAndUndo()

Description of DeactivateAndUndo.


<!-- page: PyIOleInPlaceSite__DiscardUndoState_meth.html -->

## PyIOleInPlaceSite.DiscardUndoState

 DiscardUndoState()

Description of DiscardUndoState.


<!-- page: PyIOleInPlaceSite__GetWindowContext_meth.html -->

## PyIOleInPlaceSite.GetWindowContext

 GetWindowContext()

Description of GetWindowContext.


<!-- page: PyIOleInPlaceSite__OnInPlaceActivate_meth.html -->

## PyIOleInPlaceSite.OnInPlaceActivate

 OnInPlaceActivate()

Description of OnInPlaceActivate.


<!-- page: PyIOleInPlaceSite__OnInPlaceDeactivate_meth.html -->

## PyIOleInPlaceSite.OnInPlaceDeactivate

 OnInPlaceDeactivate()

Description of OnInPlaceDeactivate.


<!-- page: PyIOleInPlaceSite__OnPosRectChange_meth.html -->

## PyIOleInPlaceSite.OnPosRectChange

 OnPosRectChange()

Description of OnPosRectChange.


<!-- page: PyIOleInPlaceSite__OnUIActivate_meth.html -->

## PyIOleInPlaceSite.OnUIActivate

 OnUIActivate()

Description of OnUIActivate.


<!-- page: PyIOleInPlaceSite__OnUIDeactivate_meth.html -->

## PyIOleInPlaceSite.OnUIDeactivate

 OnUIDeactivate(fUndoable)

Description of OnUIDeactivate.

#### Parameters

- fUndoable : int

 Description for fUndoable


<!-- page: PyIOleInPlaceSite__Scroll_meth.html -->

## PyIOleInPlaceSite.Scroll

 Scroll()

Description of Scroll.


---

<!-- object: PyIOleInPlaceSiteEx -->


<!-- page: PyIOleInPlaceSiteEx.html -->

---

## PyIOleInPlaceSiteEx Object

 Description of the interface

#### Methods

- OnInPlaceActivateEx

 Description of OnInPlaceActivateEx

- OnInPlaceDeactivateEx

 Description of OnInPlaceDeactivateEx

- RequestUIActivate

 Description of RequestUIActivate


<!-- page: PyIOleInPlaceSiteEx__OnInPlaceActivateEx_meth.html -->

## PyIOleInPlaceSiteEx.OnInPlaceActivateEx

 OnInPlaceActivateEx(dwFlags)

Description of OnInPlaceActivateEx.

#### Parameters

- dwFlags : int

 Description for dwFlags


<!-- page: PyIOleInPlaceSiteEx__OnInPlaceDeactivateEx_meth.html -->

## PyIOleInPlaceSiteEx.OnInPlaceDeactivateEx

 OnInPlaceDeactivateEx(fNoRedraw)

Description of OnInPlaceDeactivateEx.

#### Parameters

- fNoRedraw : int

 Description for fNoRedraw


<!-- page: PyIOleInPlaceSiteEx__RequestUIActivate_meth.html -->

## PyIOleInPlaceSiteEx.RequestUIActivate

 RequestUIActivate()

Description of RequestUIActivate.


---

<!-- object: PyIOleInPlaceSiteWindowless -->


<!-- page: PyIOleInPlaceSiteWindowless.html -->

---

## PyIOleInPlaceSiteWindowless Object

 Description of the interface

#### Methods

- CanWindowlessActivate

 Description of CanWindowlessActivate

- GetCapture

 Description of GetCapture

- SetCapture

 Description of SetCapture

- GetFocus

 Description of GetFocus

- SetFocus

 Description of SetFocus

- GetDC

 Description of GetDC

- ReleaseDC

 Description of ReleaseDC

- InvalidateRect

 Description of InvalidateRect

- InvalidateRgn

 Description of InvalidateRgn

- ScrollRect

 Description of ScrollRect

- AdjustRect

 Description of AdjustRect

- OnDefWindowMessage

 Description of OnDefWindowMessage


<!-- page: PyIOleInPlaceSiteWindowless__AdjustRect_meth.html -->

## PyIOleInPlaceSiteWindowless.AdjustRect

 AdjustRect()

Description of AdjustRect.


<!-- page: PyIOleInPlaceSiteWindowless__CanWindowlessActivate_meth.html -->

## PyIOleInPlaceSiteWindowless.CanWindowlessActivate

 CanWindowlessActivate()

Description of CanWindowlessActivate.


<!-- page: PyIOleInPlaceSiteWindowless__GetCapture_meth.html -->

## PyIOleInPlaceSiteWindowless.GetCapture

 GetCapture()

Description of GetCapture.


<!-- page: PyIOleInPlaceSiteWindowless__GetDC_meth.html -->

## PyIOleInPlaceSiteWindowless.GetDC

 GetDC(grfFlags, rect)

Description of GetDC.

#### Parameters

- grfFlags : int

 Description for grfFlags

- rect : (int, int, int, int)


<!-- page: PyIOleInPlaceSiteWindowless__GetFocus_meth.html -->

## PyIOleInPlaceSiteWindowless.GetFocus

 GetFocus()

Description of GetFocus.


<!-- page: PyIOleInPlaceSiteWindowless__InvalidateRect_meth.html -->

## PyIOleInPlaceSiteWindowless.InvalidateRect

 InvalidateRect(rect, fErase)

Description of InvalidateRect.

#### Parameters

- rect : (int, int, int, int)

- fErase : int

 Description for fErase


<!-- page: PyIOleInPlaceSiteWindowless__InvalidateRgn_meth.html -->

## PyIOleInPlaceSiteWindowless.InvalidateRgn

 InvalidateRgn(hRgn, fErase)

Description of InvalidateRgn.

#### Parameters

- hRgn : int

 Handle to a region

- fErase : int

 Description for fErase


<!-- page: PyIOleInPlaceSiteWindowless__OnDefWindowMessage_meth.html -->

## PyIOleInPlaceSiteWindowless.OnDefWindowMessage

 OnDefWindowMessage(msg, wParam, lParam)

Description of OnDefWindowMessage.

#### Parameters

- msg : int

 Description for msg

- wParam : int

 Description for wParam

- lParam : long

 Description for lParam


<!-- page: PyIOleInPlaceSiteWindowless__ReleaseDC_meth.html -->

## PyIOleInPlaceSiteWindowless.ReleaseDC

 ReleaseDC(hDC)

Description of ReleaseDC.

#### Parameters

- hDC : HDC

 Description for hDC


<!-- page: PyIOleInPlaceSiteWindowless__ScrollRect_meth.html -->

## PyIOleInPlaceSiteWindowless.ScrollRect

 ScrollRect(dx, dy)

Description of ScrollRect.

#### Parameters

- dx : int

 Description for dx

- dy : int

 Description for dy


<!-- page: PyIOleInPlaceSiteWindowless__SetCapture_meth.html -->

## PyIOleInPlaceSiteWindowless.SetCapture

 SetCapture(fCapture)

Description of SetCapture.

#### Parameters

- fCapture : int

 Description for fCapture


<!-- page: PyIOleInPlaceSiteWindowless__SetFocus_meth.html -->

## PyIOleInPlaceSiteWindowless.SetFocus

 SetFocus(fFocus)

Description of SetFocus.

#### Parameters

- fFocus : int

 Description for fFocus


---

<!-- object: PyIOleInPlaceUIWindow -->


<!-- page: PyIOleInPlaceUIWindow.html -->

---

## PyIOleInPlaceUIWindow Object

 Description of the interface

#### Methods

- GetBorder

 Description of GetBorder

- RequestBorderSpace

 Description of RequestBorderSpace

- SetBorderSpace

 Description of SetBorderSpace

- SetActiveObject

 Description of SetActiveObject


<!-- page: PyIOleInPlaceUIWindow__GetBorder_meth.html -->

## PyIOleInPlaceUIWindow.GetBorder

 GetBorder()

Description of GetBorder.


<!-- page: PyIOleInPlaceUIWindow__RequestBorderSpace_meth.html -->

## PyIOleInPlaceUIWindow.RequestBorderSpace

 RequestBorderSpace(borderwidths)

Description of RequestBorderSpace.

#### Parameters

- borderwidths : (int, int, int, int)

 Description for pborderwidths


<!-- page: PyIOleInPlaceUIWindow__SetActiveObject_meth.html -->

## PyIOleInPlaceUIWindow.SetActiveObject

 SetActiveObject(pActiveObject, pszObjName)

Description of SetActiveObject.

#### Parameters

- pActiveObject : PyIOleInPlaceActiveObject

 Description for pActiveObject

- pszObjName : unicode

 Description for pszObjName


<!-- page: PyIOleInPlaceUIWindow__SetBorderSpace_meth.html -->

## PyIOleInPlaceUIWindow.SetBorderSpace

 SetBorderSpace(borderwidths)

Description of SetBorderSpace.

#### Parameters

- borderwidths : (int, int, int, int)

 Description for pborderwidths


---

<!-- object: PyIOleObject -->


<!-- page: PyIOleObject.html -->

---

## PyIOleObject Object

 Description of the interface

#### Methods

- SetClientSite

 Description of SetClientSite

- GetClientSite

 Description of GetClientSite

- SetHostNames

 Description of SetHostNames

- Close

 Description of Close

- SetMoniker

 Description of SetMoniker

- GetMoniker

 Description of GetMoniker

- InitFromData

 Description of InitFromData

- GetClipboardData

 Description of GetClipboardData

- DoVerb

 Description of DoVerb

- EnumVerbs

 Description of EnumVerbs

- Update

 Description of Update

- IsUpToDate

 Description of IsUpToDate

- GetUserClassID

 Description of GetUserClassID

- GetUserType

 Description of GetUserType

- SetExtent

 Description of SetExtent

- GetExtent

 Description of GetExtent

- Advise

 Description of Advise

- Unadvise

 Description of Unadvise

- EnumAdvise

 Description of EnumAdvise

- GetMiscStatus

 Description of GetMiscStatus

- SetColorScheme

 Description of SetColorScheme


<!-- page: PyIOleObject__Advise_meth.html -->

## PyIOleObject.Advise

 Advise(pAdvSink)

Description of Advise.

#### Parameters

- pAdvSink : PyIAdviseSink

 Description for pAdvSink


<!-- page: PyIOleObject__Close_meth.html -->

## PyIOleObject.Close

 Close(dwSaveOption)

Description of Close.

#### Parameters

- dwSaveOption : int

 Description for dwSaveOption


<!-- page: PyIOleObject__DoVerb_meth.html -->

## PyIOleObject.DoVerb

 DoVerb(iVerb, msg, pActiveSite, lindex, hwndParent, rect)

Description of DoVerb.

#### Parameters

- iVerb : int

 Description for iVerb

- msg : PyMSG

 MSG tuple, a-la win32gui etc.

- pActiveSite : PyIOleClientSite

 Description for pActiveSite

- lindex : int

 Description for lindex

- hwndParent : HWND

 Description for hwndParent

- rect : (int, int, int, int)


<!-- page: PyIOleObject__EnumAdvise_meth.html -->

## PyIOleObject.EnumAdvise

 EnumAdvise()

Description of EnumAdvise.


<!-- page: PyIOleObject__EnumVerbs_meth.html -->

## PyIOleObject.EnumVerbs

 EnumVerbs()

Description of EnumVerbs.


<!-- page: PyIOleObject__GetClientSite_meth.html -->

## PyIOleObject.GetClientSite

 GetClientSite()

Description of GetClientSite.


<!-- page: PyIOleObject__GetClipboardData_meth.html -->

## PyIOleObject.GetClipboardData

 GetClipboardData(dwReserved)

Description of GetClipboardData.

#### Parameters

- dwReserved : int

 Description for dwReserved


<!-- page: PyIOleObject__GetExtent_meth.html -->

## PyIOleObject.GetExtent

 GetExtent(dwDrawAspect, size)

Description of GetExtent.

#### Parameters

- dwDrawAspect : int

 Description for dwDrawAspect

- size : (int, int)

 Size limit for the object.


<!-- page: PyIOleObject__GetMiscStatus_meth.html -->

## PyIOleObject.GetMiscStatus

 GetMiscStatus(dwAspect)

Description of GetMiscStatus.

#### Parameters

- dwAspect : int

 Description for dwAspect


<!-- page: PyIOleObject__GetMoniker_meth.html -->

## PyIOleObject.GetMoniker

 GetMoniker(dwAssign, dwWhichMoniker)

Description of GetMoniker.

#### Parameters

- dwAssign : int

 Description for dwAssign

- dwWhichMoniker : int

 Description for dwWhichMoniker


<!-- page: PyIOleObject__GetUserClassID_meth.html -->

## PyIOleObject.GetUserClassID

 GetUserClassID()

Description of GetUserClassID.


<!-- page: PyIOleObject__GetUserType_meth.html -->

## PyIOleObject.GetUserType

 GetUserType(dwFormOfType)

Description of GetUserType.

#### Parameters

- dwFormOfType : int

 Description for dwFormOfType


<!-- page: PyIOleObject__InitFromData_meth.html -->

## PyIOleObject.InitFromData

 InitFromData(pDataObject, fCreation, dwReserved)

Description of InitFromData.

#### Parameters

- pDataObject : PyIDataObject

 Description for pDataObject

- fCreation : int

 Description for fCreation

- dwReserved : int

 Description for dwReserved


<!-- page: PyIOleObject__IsUpToDate_meth.html -->

## PyIOleObject.IsUpToDate

 IsUpToDate()

Description of IsUpToDate.


<!-- page: PyIOleObject__SetClientSite_meth.html -->

## PyIOleObject.SetClientSite

 SetClientSite(pClientSite)

Description of SetClientSite.

#### Parameters

- pClientSite : PyIOleClientSite

 Description for pClientSite


<!-- page: PyIOleObject__SetColorScheme_meth.html -->

## PyIOleObject.SetColorScheme

 SetColorScheme()

Description of SetColorScheme.


<!-- page: PyIOleObject__SetExtent_meth.html -->

## PyIOleObject.SetExtent

 SetExtent(dwDrawAspect, size)

Description of SetExtent.

#### Parameters

- dwDrawAspect : int

 Description for dwDrawAspect

- size : (int, int)

 Size limit for the object.


<!-- page: PyIOleObject__SetHostNames_meth.html -->

## PyIOleObject.SetHostNames

 SetHostNames(szContainerApp, szContainerObj)

Description of SetHostNames.

#### Parameters

- szContainerApp : unicode

 Description for szContainerApp

- szContainerObj : unicode

 Description for szContainerObj


<!-- page: PyIOleObject__SetMoniker_meth.html -->

## PyIOleObject.SetMoniker

 SetMoniker(dwWhichMoniker, pmk)

Description of SetMoniker.

#### Parameters

- dwWhichMoniker : int

 Description for dwWhichMoniker

- pmk : PyIMoniker

 Description for pmk


<!-- page: PyIOleObject__Unadvise_meth.html -->

## PyIOleObject.Unadvise

 Unadvise(dwConnection)

Description of Unadvise.

#### Parameters

- dwConnection : int

 Description for dwConnection


<!-- page: PyIOleObject__Update_meth.html -->

## PyIOleObject.Update

 Update()

Description of Update.


---

<!-- object: PyIOleWindow -->


<!-- page: PyIOleWindow.html -->

---

## PyIOleWindow Object

 Description of the interface

#### Methods

- GetWindow

 Description of GetWindow

- ContextSensitiveHelp

 Description of ContextSensitiveHelp


<!-- page: PyIOleWindow__ContextSensitiveHelp_meth.html -->

## PyIOleWindow.ContextSensitiveHelp

 ContextSensitiveHelp(fEnterMode)

Description of ContextSensitiveHelp.

#### Parameters

- fEnterMode : int

 Description for fEnterMode


<!-- page: PyIOleWindow__GetWindow_meth.html -->

## PyIOleWindow.GetWindow

 GetWindow()

Description of GetWindow.


---

<!-- object: PyIPersist -->


<!-- page: PyIPersist.html -->

---

## PyIPersist Object

 A Python interface to IPersist

#### Methods

- GetClassID

 Returns the class identifier (CLSID) for the component object.

#### Based On

PyIUnknown


<!-- page: PyIPersist__GetClassID_meth.html -->

## PyIPersist.GetClassID

 PyIID = GetClassID()

Returns the class identifier (CLSID) for the component object.


---

<!-- object: PyIPersistFile -->


<!-- page: PyIPersistFile.html -->

---

## PyIPersistFile Object

 Description of the interface

#### Methods

- IsDirty

 Checks an object for changes since it was last saved to its current file.

- Load

 Opens the specified file and initializes an object from the file contents.

- Save

 Saves the object into the specified file.

- SaveCompleted

 Notifies the object that it can revert from NoScribble mode to Normal mode.

- GetCurFile

 Gets the current name of the file associated with the object.


<!-- page: PyIPersistFile__GetCurFile_meth.html -->

## PyIPersistFile.GetCurFile

 str = GetCurFile()

Gets the current name of the file associated with the object.


<!-- page: PyIPersistFile__IsDirty_meth.html -->

## PyIPersistFile.IsDirty

 IsDirty()

Checks an object for changes since it was last saved to its current file.

#### Return Value

This method returns the raw COM error code without raising the normal COM exception. You should treat any error return codes as an indication that the object has changed. Unless this method explicitly returns S_FALSE, assume that the object must be saved.


<!-- page: PyIPersistFile__Load_meth.html -->

## PyIPersistFile.Load

 Load(FileName, Mode)

Opens the specified file and initializes an object from the file contents.

#### Parameters

- FileName : str

 Absolute path of the file to open

- Mode=STGM_READ : int

 Specifies the access mode from the STGM enumeration.


<!-- page: PyIPersistFile__SaveCompleted_meth.html -->

## PyIPersistFile.SaveCompleted

 SaveCompleted(FileName)

Notifies the object that it can revert from NoScribble mode to Normal mode.

#### Parameters

- FileName : str

 Absolute path of the file where the object was saved.


<!-- page: PyIPersistFile__Save_meth.html -->

## PyIPersistFile.Save

 Save(FileName, fRemember)

Saves the object into the specified file.

#### Parameters

- FileName : str

 absolute path of the file where the object is saved.

- fRemember : int

 Specifies whether the file is to be the current working file or not.


---

<!-- object: PyIPersistFolder -->


<!-- page: PyIPersistFolder.html -->

---

## PyIPersistFolder Object

 Description of the interface

#### Methods

- Initialize

 Description of Initialize


<!-- page: PyIPersistFolder__Initialize_meth.html -->

## PyIPersistFolder.Initialize

 Initialize(pidl)

Description of Initialize.

#### Parameters

- pidl : PyIDL

 Description for pidl


---

<!-- object: PyIPersistFolder2 -->


<!-- page: PyIPersistFolder2.html -->

---

## PyIPersistFolder2 Object

 Description of the interface

#### Methods

- GetCurFolder

 Description of GetCurFolder


<!-- page: PyIPersistFolder2__GetCurFolder_meth.html -->

## PyIPersistFolder2.GetCurFolder

 GetCurFolder()

Description of GetCurFolder.


---

<!-- object: PyIPersistPropertyBag -->


<!-- page: PyIPersistPropertyBag.html -->

---

## PyIPersistPropertyBag Object

 A Python wrapper for a COM IPersistPropertyBag interface.

#### Methods

- InitNew

 Called by the container when the control is initialized to initialize the property bag.

- Load

 Called by the container to load the control's properties.

- Save

 Called by the container to save the object's properties.

#### Based On

PyIPersist


<!-- page: PyIPersistPropertyBag__InitNew_meth.html -->

## PyIPersistPropertyBag.InitNew

 InitNew()

Called by the container when the control is initialized to initialize the property bag.


<!-- page: PyIPersistPropertyBag__Load_meth.html -->

## PyIPersistPropertyBag.Load

 Load(bag, log)

Called by the container to load the control's properties.

#### Parameters

- bag : PyIPropertyBag

 the caller's property bag.

- log=None : PyIErrorLog

 the caller's error log, or None


<!-- page: PyIPersistPropertyBag__Save_meth.html -->

## PyIPersistPropertyBag.Save

 Save(bag, clearDirty, saveProperties)

Called by the container to save the object's properties.

#### Parameters

- bag : PyIPropertyBag

 the caller's property bag.

- clearDirty : int

 Specifies whether to clear the dirty flag.

- saveProperties : int

 Specifies whether to save all properties or just those that have changed


---

<!-- object: PyIPersistSerializedPropStorage -->


<!-- page: PyIPersistSerializedPropStorage.html -->

---

## PyIPersistSerializedPropStorage Object

 Allows a property store to be marshalled into a single buffer. Primarily used with property stores created using propsys::PSCreateMemoryPropertyStore.

#### Methods

- SetFlags

 Sets flags for the store

- SetPropertyStorage

 Initializes the store with a serialized buffer

- GetPropertyStorage

 Retrieves the current contents of the property store


<!-- page: PyIPersistSerializedPropStorage__GetPropertyStorage_meth.html -->

## PyIPersistSerializedPropStorage.GetPropertyStorage

 buffer = GetPropertyStorage()

Retrieves the current contents of the property store


<!-- page: PyIPersistSerializedPropStorage__SetFlags_meth.html -->

## PyIPersistSerializedPropStorage.SetFlags

 SetFlags(flags)

Sets flags for the store

#### Parameters

- flags : int

 Combination of pscon.FPSPS_* values


<!-- page: PyIPersistSerializedPropStorage__SetPropertyStorage_meth.html -->

## PyIPersistSerializedPropStorage.SetPropertyStorage

 SetPropertyStorage(ps)

Initializes the store with a serialized buffer

#### Parameters

- ps : buffer

 Bytes or buffer object containing a serialized property store


---

<!-- object: PyIPersistStorage -->


<!-- page: PyIPersistStorage.html -->

---

## PyIPersistStorage Object

 A Python wrapper of a COM IPersistStorage interface.

#### Comments

 The IPersistStorage interface defines methods that enable a container application to pass a storage object to one of its contained objects and to load and save the storage object. This interface supports the structured storage model, in which each contained object has its own storage that is nested within the container's storage.

#### Methods

- IsDirty

 Checks the object for changes since it was last saved.

- InitNew

 Initializes a new object, providing a storage object to be used for the object.

- Load

 Loads an object from its existing storage.

- Save

 Saves an object, and any nested objects that it contains, into the specified storage.

- SaveCompleted

 Notifies the object that it can revert from NoScribble or HandsOff mode.

- HandsOffStorage

 Instructs the object to release all storage objects that have been passed to it by its container and to enter HandsOff mode.

#### Based On

PyIUnknown


<!-- page: PyIPersistStorage__HandsOffStorage_meth.html -->

## PyIPersistStorage.HandsOffStorage

 HandsOffStorage()

Instructs the object to release all storage objects that have been passed to it by its container and to enter HandsOff mode, in which the object cannot do anything and the only operation that works is a close operation.


<!-- page: PyIPersistStorage__InitNew_meth.html -->

## PyIPersistStorage.InitNew

 InitNew(PyIStorage)

Initializes a new object, providing a storage object to be used for the object.

#### Parameters

- PyIStorage : PyIStorage

 PyIStorage for the new storage object to be initialized. The container creates a nested storage object in its storage object (see PyIStorage::CreateStorage). Then, the container calls the PyIPersistStorage::WriteClassStg function to initialize the new storage object with the object class identifier (CLSID).


<!-- page: PyIPersistStorage__IsDirty_meth.html -->

## PyIPersistStorage.IsDirty

 int = IsDirty()

Checks the object for changes since it was last saved.

| | Return Value | Description
| | S_OK (ie, 0) | The object has changed since it was last saved.
| | S_FALSE (ie, 1) | The object has not changed since the last save.


<!-- page: PyIPersistStorage__Load_meth.html -->

## PyIPersistStorage.Load

 Load(storage)

Loads an object from its existing storage.

#### Parameters

- storage : PyIStorage

 Existing storage for the object.


<!-- page: PyIPersistStorage__SaveCompleted_meth.html -->

## PyIPersistStorage.SaveCompleted

 SaveCompleted(PyIStorage)

Notifies the object that it can revert from NoScribble or HandsOff mode, in which it must not write to its storage object, to Normal mode, in which it can. The object enters NoScribble mode when it receives an PyIPersistStorage::Save call.

#### Parameters

- PyIStorage : PyIStorage

 The current storage object


<!-- page: PyIPersistStorage__Save_meth.html -->

## PyIPersistStorage.Save

 Save(PyIStorage, int)

Saves an object, and any nested objects that it contains, into the specified storage. The object is placed in NoScribble mode, and it must not write to the specified storage until it receives a call to its PyIPersistStorage::SaveCompleted method.

#### Parameters

- PyIStorage : PyIStorage

 Storage for the object

- int : fSameAsLoad

 Indicates whether the specified storage object is the current one.
 This parameter is set to FALSE when performing a Save As or Save A Copy To operation or when performing a full save. In the latter case, this method saves to a temporary file, deletes the original file, and renames the temporary file.
 This parameter is set to TRUE to perform a full save in a low-memory situation or to perform a fast incremental save in which only the dirty components are saved.


---

<!-- object: PyIPersistStream -->


<!-- page: PyIPersistStream.html -->

---

## PyIPersistStream Object

 A Python interface to IPersistStream

#### Methods

- IsDirty

 Checks the object for changes since it was last saved.

- Load

 Initializes an object from the stream where it was previously saved.

- Save

 Saves an object to the specified stream.

- GetSizeMax

 Returns the size in bytes of the stream needed to save the object.

#### Based On

PyIPersist


<!-- page: PyIPersistStream__GetSizeMax_meth.html -->

## PyIPersistStream.GetSizeMax

 ULARGE_INTEGER = GetSizeMax()

Returns the size in bytes of the stream needed to save the object.


<!-- page: PyIPersistStream__IsDirty_meth.html -->

## PyIPersistStream.IsDirty

 int = IsDirty()

Checks the object for changes since it was last saved.

| | Return Value | Description
| | S_OK (ie, 0) | The object has changed since it was last saved.
| | S_FALSE (ie, 1) | The object has not changed since the last save.


<!-- page: PyIPersistStream__Load_meth.html -->

## PyIPersistStream.Load

 Load(stream)

Initializes an object from the stream where it was previously saved.

#### Parameters

- stream : PyIStream

 Stream object to load from.

#### Comments

 This method loads an object from its associated stream. The seek pointer is set as it was in the most recent PyIPersistStream::Save method. This method can seek and read from the stream, but cannot write to it.

 On exit, the seek pointer must be in the same position it was in on entry, immediately past the end of the data.


<!-- page: PyIPersistStream__Save_meth.html -->

## PyIPersistStream.Save

 Save(stream, bClearDirty)

Saves an object to the specified stream.

#### Parameters

- stream : PyIStream

 The stream to save to.

- bClearDirty : int

 Indicates whether to clear the dirty flag after the save is complete


---

<!-- object: PyIPersistStreamInit -->


<!-- page: PyIPersistStreamInit.html -->

---

## PyIPersistStreamInit Object

 A Python interface to IPersistStreamInit

#### Methods

- InitNew

 Initializes the object to a default state.

#### Based On

PyIPersistStream


<!-- page: PyIPersistStreamInit__InitNew_meth.html -->

## PyIPersistStreamInit.InitNew

 InitNew()

Initializes the object to a default state.


---

<!-- object: PyIProcessDebugManager -->


<!-- page: PyIProcessDebugManager.html -->

---

## PyIProcessDebugManager Object

 Description of the interface

#### Methods

- CreateApplication

 Description of CreateApplication

- GetDefaultApplication

 Description of GetDefaultApplication

- AddApplication

 Description of AddApplication

- RemoveApplication

 Description of RemoveApplication

- CreateDebugDocumentHelper

 Description of CreateDebugDocumentHelper.


<!-- page: PyIProcessDebugManager__AddApplication_meth.html -->

## PyIProcessDebugManager.AddApplication

 AddApplication(pda)

Description of AddApplication.

#### Parameters

- pda : PyIDebugApplication

 Description for pda


<!-- page: PyIProcessDebugManager__CreateApplication_meth.html -->

## PyIProcessDebugManager.CreateApplication

 CreateApplication()

Description of CreateApplication.


<!-- page: PyIProcessDebugManager__CreateDebugDocumentHelper_meth.html -->

## PyIProcessDebugManager.CreateDebugDocumentHelper

 CreateDebugDocumentHelper(unkOuter)

Description of CreateDebugDocumentHelper.

#### Parameters

- unkOuter : PyIIUnknown

 The outer object for aggregation, or (usually!) None


<!-- page: PyIProcessDebugManager__GetDefaultApplication_meth.html -->

## PyIProcessDebugManager.GetDefaultApplication

 GetDefaultApplication()

Description of GetDefaultApplication.


<!-- page: PyIProcessDebugManager__RemoveApplication_meth.html -->

## PyIProcessDebugManager.RemoveApplication

 RemoveApplication(dwAppCookie)

Description of RemoveApplication.

#### Parameters

- dwAppCookie : int

 Description for dwAppCookie


---

<!-- object: PyIProfAdmin -->


<!-- page: PyIProfAdmin.html -->

---

## PyIProfAdmin Object

 An COM interface to MAPI
Derived from PyIUnknown

#### Methods

- GetLastError

 Returns the last error code for the object.

- CreateProfile

 Creates a new profile.

- DeleteProfile

 Deletes a profile.

- CopyProfile

 Copies a profile.

- RenameProfile

 Assigns a new name to a profile.

- SetDefaultProfile

 Sets or clears a client's default profile.

- AdminServices

 Provides access to a message service administration object for making changes to the message services in a profile.


<!-- page: PyIProfAdmin__AdminServices_meth.html -->

## PyIProfAdmin.AdminServices

 PyIProfAdmin = AdminServices(profileName, Password , uiParam , flags )

Provides access to a message service administration object for making changes to the message services in a profile.

#### Parameters

- profileName : string

 The name of the profile to be modified.

- Password=None : string

- uiParam=0 : int

 A handle of the parent window for any dialog boxes or windows that this method displays.

- flags=0 : int


<!-- page: PyIProfAdmin__CopyProfile_meth.html -->

## PyIProfAdmin.CopyProfile

 CopyProfile(oldProfileName, Password, newProfileName, uiParam, flags)

Copies a profile.

#### Parameters

- oldProfileName : string

 The name of the profile to copy.

- Password : string

 Must be None

- newProfileName : string

 The new name of the copied profile.

- uiParam=0 : int

 A handle of the parent window for any dialog boxes or windows that this method displays.

- flags=0 : int


<!-- page: PyIProfAdmin__CreateProfile_meth.html -->

## PyIProfAdmin.CreateProfile

 CreateProfile(oldProfileName, Password, uiParam, flags)

Creates a new profile.

#### Parameters

- oldProfileName : string

 The name of the new profile.

- Password : string

 Must be None

- uiParam=0 : int

 A handle of the parent window for any dialog boxes or windows that this method displays.

- flags=0 : int


<!-- page: PyIProfAdmin__DeleteProfile_meth.html -->

## PyIProfAdmin.DeleteProfile

 DeleteProfile(oldProfileName, flags)

Deletes a profile.

#### Parameters

- oldProfileName : string

 The name of the profile to be deleted.

- flags=0 : int


<!-- page: PyIProfAdmin__GetLastError_meth.html -->

## PyIProfAdmin.GetLastError

 MAPIERROR = GetLastError(hr, flags )

Returns the last error code for the object.

#### Parameters

- hr : int

 Contains the error code generated in the previous method call.

- flags : int

 Indicates for format for the output.


<!-- page: PyIProfAdmin__RenameProfile_meth.html -->

## PyIProfAdmin.RenameProfile

 RenameProfile(oldProfileName, Password, newProfileName, uiParam, flags)

Assigns a new name to a profile.

#### Parameters

- oldProfileName : string

 The current name of the profile to rename.

- Password : string

 Must be None

- newProfileName : string

 The new name of the profile to rename.

- uiParam=0 : int

 A handle of the parent window for any dialog boxes or windows that this method displays.

- flags=0 : int


<!-- page: PyIProfAdmin__SetDefaultProfile_meth.html -->

## PyIProfAdmin.SetDefaultProfile

 SetDefaultProfile(profileName, flags)

Sets or clears a client's default profile.

#### Parameters

- profileName : string

 The name of the profile that will become the default, or None. Setting profileName to None indicates that SetDefaultProfile should remove the existing default profile, leaving the client without a default.

- flags=0 : int


---

<!-- object: PyIPropertyBag -->


<!-- page: PyIPropertyBag.html -->

---

## PyIPropertyBag Object

 A Python wrapper for a COM IPropertyBag interface.

#### Comments

 The IPropertyBag interface provides an object with a property bag in which the object can persistently save its properties.
 When a client wishes to have exact control over how individually named properties of an object are saved, it would attempt to use an object's IPersistPropertyBag interface as a persistence mechanism. In that case the client supplies a property bag to the object in the form of an IPropertyBag interface.

#### Methods

- Read

 Called by the control to read a property from the storage provided by the container.

- Write

 Called by the control to write each property in turn to the storage provided by the container.

#### Based On

PyIUnknown


<!-- page: PyIPropertyBag__Read_meth.html -->

## PyIPropertyBag.Read

 object = Read(propName, propType , errorLog )

Called by the control to read a property from the storage provided by the container.

#### Parameters

- propName : str

 Name of the property to read.

- propType : int

 The type of the object to read. Must be a VT_* Variant Type constant.

- errorLog=None : PyIErrorLog

 The caller's PyIErrorLog object in which the property bag stores any errors that occur during reads. Can be None in which case the caller is not interested in errors.

#### Comments

 The result is a Python object, mapped from a COM VARIANT of type as specified in the propType parameter.


<!-- page: PyIPropertyBag__Write_meth.html -->

## PyIPropertyBag.Write

 Write(propName, value)

Called by the control to write each property in turn to the storage provided by the container.

#### Parameters

- propName : str

 Name of the property to read.

- value : object

 The value for the property. The value must be able to be converted to a COM VARIANT.


---

<!-- object: PyIPropertyChange -->


<!-- page: PyIPropertyChange.html -->

---

## PyIPropertyChange Object

 Interface used to specify a change to a property

#### Methods

- ApplyToPropVariant

 Applies the change to a variant value

#### Based On

PyIObjectWithPropertyKey


<!-- page: PyIPropertyChange__ApplyToPropVariant_meth.html -->

## PyIPropertyChange.ApplyToPropVariant

 PyPROPVARIANT = ApplyToPropVariant(OrigVal)

Applies the change to a variant value

#### Parameters

- OrigVal : PyPROPVARIANT

 The value to be modified


---

<!-- object: PyIPropertyChangeArray -->


<!-- page: PyIPropertyChangeArray.html -->

---

## PyIPropertyChangeArray Object

 Container for a sequence of PyIPropertyChange interfaces, as used with PyIFileOperation.
Create using propsys.PSCreatePropertyChangeArray(...)

#### Methods

- GetCount

 Returns the number of changes in the array

- GetAt

 Returns a change by zero-based index

- InsertAt

 Inserts a change at a specific position

- Append

 Adds a change to the end of the array

- AppendOrReplace

 Adds a change, or replaces an identical property key

- RemoveAt

 Removes a change from the array

- IsKeyInArray

 Checks if array contains a change to a property


<!-- page: PyIPropertyChangeArray__AppendOrReplace_meth.html -->

## PyIPropertyChangeArray.AppendOrReplace

 AppendOrReplace(PropChange)

Adds a change, or replaces if an identical property key is already in container

#### Parameters

- PropChange : PyIPropertyChange

 The change to be added or replaced


<!-- page: PyIPropertyChangeArray__Append_meth.html -->

## PyIPropertyChangeArray.Append

 Append(PropChange)

Adds a change to the end of the array

#### Parameters

- PropChange : PyIPropertyChange

 The change to be added


<!-- page: PyIPropertyChangeArray__GetAt_meth.html -->

## PyIPropertyChangeArray.GetAt

 PyIPropertyChange = GetAt(Index, riid )

Retrieves a change by zero-based index

#### Parameters

- Index : int

 Index of the change to retrieve

- riid=IID_IPropertyChange : PyIID

 The interface to return


<!-- page: PyIPropertyChangeArray__GetCount_meth.html -->

## PyIPropertyChangeArray.GetCount

 int = GetCount()

Returns the number of changes in the array


<!-- page: PyIPropertyChangeArray__InsertAt_meth.html -->

## PyIPropertyChangeArray.InsertAt

 InsertAt(Index, PropChange)

Inserts a change at a specific position

#### Parameters

- Index : int

 Position at which to place the change

- PropChange : PyIPropertyChange

 The change to be added


<!-- page: PyIPropertyChangeArray__IsKeyInArray_meth.html -->

## PyIPropertyChangeArray.IsKeyInArray

 boolean = IsKeyInArray(key)

Checks if array contains a change to a property

#### Parameters

- key : PyPROPERTYKEY

 Property key to look for


<!-- page: PyIPropertyChangeArray__RemoveAt_meth.html -->

## PyIPropertyChangeArray.RemoveAt

 RemoveAt(Index)

Removes a change from the array

#### Parameters

- Index : int

 Index of change to be removed


---

<!-- object: PyIPropertyDescription -->


<!-- page: PyIPropertyDescription.html -->

---

## PyIPropertyDescription Object

 Gives access to the details of a property definition

#### Methods

- GetPropertyKey

 Returns the unique identifier for a property

- GetCanonicalName

 Returns the name of the property

- GetPropertyType

 Returns the variant type of the property (VT_*)

- GetDisplayName

 Returns the property name as shown in the UI

- GetEditInvitation

 Returns the input prompt used in edit controls

- GetTypeFlags

 Returns type flags for the property

- GetViewFlags

 Returns the view flags that control how the property is displayed (PDVF_*)

- GetDefaultColumnWidth

 Returns the default width in characters

- GetDisplayType

 Returns the display type (PDDT_*)

- GetColumnState

 Returns flags that control how property is displayed in column (SHCOLSTATE_*)

- GetGroupingRange

 Returns property's grouping attributes (PDGR_*)

- GetRelativeDescriptionType

 Returns the relative description type (PDRDT_*)

- GetRelativeDescription

 Compares two values

- GetSortDescription

 Returns value that determines how sorting options are displayed (PDSD_*)

- GetSortDescriptionLabel

 Returns description of current sort order

- GetAggregationType

 Describes how properties for multiple items are displayed (PDAT_*)

- GetConditionType

 Returns options that determine how the property is used to build a search query

- GetEnumTypeList

 Returns an interface used for querying valid property range

- CoerceToCanonicalValue

 Converts a variant value to the exact type expected by the property

- FormatForDisplay

 Converts a value to its string representation

- IsValueCanonical

 Determines if a value exactly matches the specification for the property


<!-- page: PyIPropertyDescription__CoerceToCanonicalValue_meth.html -->

## PyIPropertyDescription.CoerceToCanonicalValue

 int = CoerceToCanonicalValue(Value)

Converts a variant value to the exact type expected by the property

#### Parameters

- Value : PyPROPVARIANT

 The property value to be converted

#### Comments

 This method mutates the PyPROPVARIANT in place. It may be cleared on failure.

#### Return Value

Returns the HRESULT from the operation on success.


<!-- page: PyIPropertyDescription__FormatForDisplay_meth.html -->

## PyIPropertyDescription.FormatForDisplay

 str = FormatForDisplay(Value, Flags )

Converts a value to its string representation

#### Parameters

- Value : PyPROPVARIANT

 The value to be formatted

- Flags=PDFF_DEFAULT : int

 Combination of PROPDESC_FORMAT_FLAGS (PDFF_*)


<!-- page: PyIPropertyDescription__GetAggregationType_meth.html -->

## PyIPropertyDescription.GetAggregationType

 int = GetAggregationType()

Describes how properties for multiple items are displayed (PDAT_*)


<!-- page: PyIPropertyDescription__GetCanonicalName_meth.html -->

## PyIPropertyDescription.GetCanonicalName

 str = GetCanonicalName()

Returns the name of the property


<!-- page: PyIPropertyDescription__GetColumnState_meth.html -->

## PyIPropertyDescription.GetColumnState

 int = GetColumnState()

Returns flags that control how property is displayed in column (SHCOLSTATE_*)


<!-- page: PyIPropertyDescription__GetConditionType_meth.html -->

## PyIPropertyDescription.GetConditionType

 (int, int) = GetConditionType()

Returns options that determine how the property is used to build a search query

#### Return Value

Returns the condition type (PDCOT_*) and default operation (COP_*)


<!-- page: PyIPropertyDescription__GetDefaultColumnWidth_meth.html -->

## PyIPropertyDescription.GetDefaultColumnWidth

 int = GetDefaultColumnWidth()

Returns the default width in characters


<!-- page: PyIPropertyDescription__GetDisplayName_meth.html -->

## PyIPropertyDescription.GetDisplayName

 str = GetDisplayName()

Returns the property name as shown in the UI


<!-- page: PyIPropertyDescription__GetDisplayType_meth.html -->

## PyIPropertyDescription.GetDisplayType

 int = GetDisplayType()

Returns the display type (PDDT_*)


<!-- page: PyIPropertyDescription__GetEditInvitation_meth.html -->

## PyIPropertyDescription.GetEditInvitation

 str = GetEditInvitation()

Returns the input prompt used in edit controls


<!-- page: PyIPropertyDescription__GetEnumTypeList_meth.html -->

## PyIPropertyDescription.GetEnumTypeList

 PyIPropertyEnumTypeList = GetEnumTypeList(riid)

Returns an interface used for querying valid property range

#### Parameters

- riid=IID_IPropertyEnumTypeList : PyIID

 IID of the requested interface


<!-- page: PyIPropertyDescription__GetGroupingRange_meth.html -->

## PyIPropertyDescription.GetGroupingRange

 int = GetGroupingRange()

Returns property's grouping attributes (PDGR_*)


<!-- page: PyIPropertyDescription__GetPropertyKey_meth.html -->

## PyIPropertyDescription.GetPropertyKey

 PyPROPERTYKEY = GetPropertyKey()

Returns the unique identifier for a property


<!-- page: PyIPropertyDescription__GetPropertyType_meth.html -->

## PyIPropertyDescription.GetPropertyType

 int = GetPropertyType()

Returns the variant type of the property (VT_*)


<!-- page: PyIPropertyDescription__GetRelativeDescriptionType_meth.html -->

## PyIPropertyDescription.GetRelativeDescriptionType

 int = GetRelativeDescriptionType()

Returns the relative description type (PDRDT_*)


<!-- page: PyIPropertyDescription__GetRelativeDescription_meth.html -->

## PyIPropertyDescription.GetRelativeDescription

 (str, str) = GetRelativeDescription(var1, var2 )

Compares two values

#### Parameters

- var1 : PyPROPVARIANT

 The first value

- var2 : PyPROPVARIANT

 The second value


<!-- page: PyIPropertyDescription__GetSortDescriptionLabel_meth.html -->

## PyIPropertyDescription.GetSortDescriptionLabel

 str = GetSortDescriptionLabel(Descending)

Returns description of current sort order

#### Parameters

- Descending : bool

 Indicates if order is reversed


<!-- page: PyIPropertyDescription__GetSortDescription_meth.html -->

## PyIPropertyDescription.GetSortDescription

 int = GetSortDescription()

Returns value that determines how sorting options are displayed (PDSD_*)


<!-- page: PyIPropertyDescription__GetTypeFlags_meth.html -->

## PyIPropertyDescription.GetTypeFlags

 int = GetTypeFlags(mask)

Returns type flags for the property

#### Parameters

- mask=PDTF_MASK_ALL : int

 Specifies which flags to retrieve (PDTF_*)


<!-- page: PyIPropertyDescription__GetViewFlags_meth.html -->

## PyIPropertyDescription.GetViewFlags

 int = GetViewFlags()

Returns the view flags that control how the property is displayed (PDVF_*)


<!-- page: PyIPropertyDescription__IsValueCanonical_meth.html -->

## PyIPropertyDescription.IsValueCanonical

 bool = IsValueCanonical(Value)

Determines if a value exactly matches the specification for the property

#### Parameters

- Value : PROPVARIANT

 The value to check


---

<!-- object: PyIPropertyDescriptionAliasInfo -->


<!-- page: PyIPropertyDescriptionAliasInfo.html -->

---

## PyIPropertyDescriptionAliasInfo Object

 Interface that gives access to the sorting columns for a property

#### Methods

- GetSortByAlias

 Returns the primary column used for sorting

- GetAdditionalSortByAliases

 Returns secondary sorting columns


<!-- page: PyIPropertyDescriptionAliasInfo__GetAdditionalSortByAliases_meth.html -->

## PyIPropertyDescriptionAliasInfo.GetAdditionalSortByAliases

 PyIPropertyDescriptionList = GetAdditionalSortByAliases(riid)

Returns secondary sorting columns

#### Parameters

- riid=IID_IPropertyDescriptionList : PyIID

 The interface to return


<!-- page: PyIPropertyDescriptionAliasInfo__GetSortByAlias_meth.html -->

## PyIPropertyDescriptionAliasInfo.GetSortByAlias

 PyIPropertyDescription = GetSortByAlias(riid)

Returns the primary column used for sorting

#### Parameters

- riid=IID_IPropertyDescription : PyIID

 The interface to return


---

<!-- object: PyIPropertyDescriptionList -->


<!-- page: PyIPropertyDescriptionList.html -->

---

## PyIPropertyDescriptionList Object

 Container for a number of property descriptions

#### Methods

- GetCount

 Gets the number of properties in the list

- GetAt

 Retrieves a description from the list


<!-- page: PyIPropertyDescriptionList__GetAt_meth.html -->

## PyIPropertyDescriptionList.GetAt

 PyIPropertyDescription = GetAt(Elem, riid )

Retrieves a description from the list

#### Parameters

- Elem : int

 Index of the element to return

- riid=IID_IPropertyDescription : PyIID

 The interface to return


<!-- page: PyIPropertyDescriptionList__GetCount_meth.html -->

## PyIPropertyDescriptionList.GetCount

 int = GetCount()

Gets the number of properties in the list


---

<!-- object: PyIPropertyDescriptionSearchInfo -->


<!-- page: PyIPropertyDescriptionSearchInfo.html -->

---

## PyIPropertyDescriptionSearchInfo Object

 Interface that retrieves indexing options defined in a property's searchinfo XML element Inhererits all methods of PyIPropertyDescription

#### Methods

- GetSearchInfoFlags

 Returns flags controlling how property is indexed

- GetColumnIndexType

 Returns flags indicating type of property

- GetProjectionString

 Returns the canonical name of the property

- GetMaxSize

 Returns the maximum size specified in search options


<!-- page: PyIPropertyDescriptionSearchInfo__GetColumnIndexType_meth.html -->

## PyIPropertyDescriptionSearchInfo.GetColumnIndexType

 int = GetColumnIndexType()

Returns flags indicating type of property

#### Return Value

Returns a value from the PROPDESC_COLUMNINDEX_TYPE enum


<!-- page: PyIPropertyDescriptionSearchInfo__GetMaxSize_meth.html -->

## PyIPropertyDescriptionSearchInfo.GetMaxSize

 int = GetMaxSize()

Returns the maximum size specified in search options


<!-- page: PyIPropertyDescriptionSearchInfo__GetProjectionString_meth.html -->

## PyIPropertyDescriptionSearchInfo.GetProjectionString

 str = GetProjectionString()

Returns the canonical name of the property


<!-- page: PyIPropertyDescriptionSearchInfo__GetSearchInfoFlags_meth.html -->

## PyIPropertyDescriptionSearchInfo.GetSearchInfoFlags

 int = GetSearchInfoFlags()

Returns flags controlling how property is indexed

#### Return Value

Returns a combination of PROPDESC_SEARCHINFO_FLAGS values


---

<!-- object: PyIPropertyEnumType -->


<!-- page: PyIPropertyEnumType.html -->

---

## PyIPropertyEnumType Object

 Contains information about an allowable value or range for a property

#### Methods

- GetEnumType

 Retrieves the type (PROPENUMTYPE)

- GetValue

 Retrieves the defined value

- GetRangeMinValue

 Returns the minimum allowed value for the property

- GetRangeSetValue

 Returns a fixed value defined for the property

- GetDisplayText

 Returns the display text for the enumerated type


<!-- page: PyIPropertyEnumType__GetDisplayText_meth.html -->

## PyIPropertyEnumType.GetDisplayText

 GetDisplayText()

Returns the display text for the enumerated type


<!-- page: PyIPropertyEnumType__GetEnumType_meth.html -->

## PyIPropertyEnumType.GetEnumType

 int = GetEnumType()

Retrieves the type (PROPENUMTYPE)

#### Return Value

pscon.PET_*


<!-- page: PyIPropertyEnumType__GetRangeMinValue_meth.html -->

## PyIPropertyEnumType.GetRangeMinValue

 PyPROPVARIANT = GetRangeMinValue()

Returns the minimum allowed value for the property


<!-- page: PyIPropertyEnumType__GetRangeSetValue_meth.html -->

## PyIPropertyEnumType.GetRangeSetValue

 PyPROPVARIANT = GetRangeSetValue()

Returns a fixed value defined for the property


<!-- page: PyIPropertyEnumType__GetValue_meth.html -->

## PyIPropertyEnumType.GetValue

 PyPROPVARIANT = GetValue()

Retrieves the defined value


---

<!-- object: PyIPropertyEnumTypeList -->


<!-- page: PyIPropertyEnumTypeList.html -->

---

## PyIPropertyEnumTypeList Object

 Contains a collection of PyIPropertyEnumType objects that define the allowable values for a property

#### Methods

- GetCount

 Returns the number of objects in the list

- GetAt

 Retrieves an item by index

- FindMatchingIndex

 Attempts to match the specified value to one of the allowable values for the property


<!-- page: PyIPropertyEnumTypeList__FindMatchingIndex_meth.html -->

## PyIPropertyEnumTypeList.FindMatchingIndex

 int = FindMatchingIndex(Cmp)

Attempts to match the specified value to one of the allowable values for the property

#### Parameters

- Cmp : PyPROPVARIANT

 A value to match against the defined values of the property


<!-- page: PyIPropertyEnumTypeList__GetAt_meth.html -->

## PyIPropertyEnumTypeList.GetAt

 PyIPropertyEnumType = GetAt(itype, riid )

Retrieves an item by index

#### Parameters

- itype : int

 Zero based index of type to return

- riid=IID_IPropertyEnumType : PyIID

 The interface to return


<!-- page: PyIPropertyEnumTypeList__GetCount_meth.html -->

## PyIPropertyEnumTypeList.GetCount

 int = GetCount()

Returns the number of objects in the list


---

<!-- object: PyIPropertySetStorage -->


<!-- page: PyIPropertySetStorage.html -->

---

## PyIPropertySetStorage Object

 Container for a collection of property sets. Can be iterated over to enumerate property sets.

#### Methods

- Create

 Creates a new property set in the storage object

- Open

 Opens an existing property set

- Delete

 Removes a property set from this storage object

- Enum

 Creates an iterator to enumerate contained property sets


<!-- page: PyIPropertySetStorage__Create_meth.html -->

## PyIPropertySetStorage.Create

 PyIPropertyStorage = Create(fmtid, clsid , Flags , Mode )

Creates a new property set in the storage object

#### Parameters

- fmtid : PyIID

 GUID identifying a property set, pythoncom.FMTID_*

- clsid : PyIID

 CLSID of property set handler, usually same as fmtid

- Flags : int

 Specifies behaviour of property set, storagecon.PROPSETFLAG_*

- Mode : int

 Access mode, combination of storagecon.STGM_* flags


<!-- page: PyIPropertySetStorage__Delete_meth.html -->

## PyIPropertySetStorage.Delete

 Delete(fmtid)

Removes a property set from this storage object

#### Parameters

- fmtid : PyIID

 GUID of a property set, pythoncom.FMTID_*


<!-- page: PyIPropertySetStorage__Enum_meth.html -->

## PyIPropertySetStorage.Enum

 PyIEnumSTATPROPSETSTG = Enum()

Creates an iterator to enumerate contained property sets


<!-- page: PyIPropertySetStorage__Open_meth.html -->

## PyIPropertySetStorage.Open

 PyIPropertyStorage = Open(fmtid, Mode )

Opens an existing property set

#### Parameters

- fmtid : PyIID

 GUID of a property set, pythoncom.FMTID_*

- Mode=STGM_READ | STGM_SHARE_EXCLUSIVE : int

 Access mode, combination of storagecon.STGM_* flags


---

<!-- object: PyIPropertyStorage -->


<!-- page: PyIPropertyStorage.html -->

---

## PyIPropertyStorage Object

 Structured storage object that contains a set of properties. Supports iteration to list properties.

#### Methods

- ReadMultiple

 Reads specified properties from the current property set.

- WriteMultiple

 Creates or modifies properties in the property set

- DeleteMultiple

 Deletes properties from the property set

- ReadPropertyNames

 Retrieves any existing string names for the specified property identifiers.

- WritePropertyNames

 Assigns string names to a specified array of property IDs in the current property set.

- DeletePropertyNames

 Removes property names from specified properties.

- Commit

 Persists the property set to its base storage

- Revert

 Discards any changes that have been made

- Enum

 Creates an enumerator for properties in the property set

- SetTimes

 Sets the creation, last access, and modification time

- SetClass

 Sets the GUID for the property set

- Stat

 Returns various infomation about the property set


<!-- page: PyIPropertyStorage__Commit_meth.html -->

## PyIPropertyStorage.Commit

 Commit(CommitFlags)

Persists the property set to its base storage

#### Parameters

- CommitFlags : int

 Combination of storagecon.STGC_* flags


<!-- page: PyIPropertyStorage__DeleteMultiple_meth.html -->

## PyIPropertyStorage.DeleteMultiple

 DeleteMultiple(props)

Deletes properties from the property set

#### Parameters

- props : (PROPSPEC, ...)

 Sequence containing names or IDs of properties to be deleted


<!-- page: PyIPropertyStorage__DeletePropertyNames_meth.html -->

## PyIPropertyStorage.DeletePropertyNames

 DeletePropertyNames(props)

Removes property names from specified properties.

#### Parameters

- props : (int, ...)

 Sequence of ints containing property IDs.


<!-- page: PyIPropertyStorage__Enum_meth.html -->

## PyIPropertyStorage.Enum

 PyIEnumSTATPROPSTG = Enum()

Creates an enumerator for properties in the property set


<!-- page: PyIPropertyStorage__ReadMultiple_meth.html -->

## PyIPropertyStorage.ReadMultiple

 (object, ...) = ReadMultiple(props)

Reads specified properties from the current property set.

#### Parameters

- props : (PROPSPEC, ...)

 Sequence of property IDs or names.

#### Return Value

Returned values are automatically converted to an appropriate python type


<!-- page: PyIPropertyStorage__ReadPropertyNames_meth.html -->

## PyIPropertyStorage.ReadPropertyNames

 (str,...) = ReadPropertyNames(props)

Retrieves any existing string names for the specified property identifiers.

#### Parameters

- props : (int, ...)

 Sequence of ints containing property IDs.


<!-- page: PyIPropertyStorage__Revert_meth.html -->

## PyIPropertyStorage.Revert

 Revert()

Discards any changes that have been made


<!-- page: PyIPropertyStorage__SetClass_meth.html -->

## PyIPropertyStorage.SetClass

 SetClass(clsid)

Sets the GUID for the property set

#### Parameters

- clsid : PyIID

 Description for clsid


<!-- page: PyIPropertyStorage__SetTimes_meth.html -->

## PyIPropertyStorage.SetTimes

 SetTimes(ctime, atime, mtime)

Sets the creation, last access, and modification time

#### Parameters

- ctime : PyDateTime

 Creation time, or None for no change

- atime : PyDateTime

 Last access time, or None for no change

- mtime : PyDateTime

 Modification time, or None for no change

#### Comments

 Some property sets do not support these times.


<!-- page: PyIPropertyStorage__Stat_meth.html -->

## PyIPropertyStorage.Stat

 tuple = Stat()

Returns various infomation about the property set

#### Return Value

Returns a tuple representing a STATPROPSETSTG struct.


<!-- page: PyIPropertyStorage__WriteMultiple_meth.html -->

## PyIPropertyStorage.WriteMultiple

 WriteMultiple(props, values, propidNameFirst)

Creates or modifies properties in the property set

#### Parameters

- props : (PROPSPEC, ...)

 Sequence containing names or integer ids of properties to write

- values : (PROPVARIANT , ...)

 The values for the properties.

- propidNameFirst=2 : int

 Minimum property id to be assigned to new properties specified by name


<!-- page: PyIPropertyStorage__WritePropertyNames_meth.html -->

## PyIPropertyStorage.WritePropertyNames

 WritePropertyNames(props, names)

Assigns string names to a specified array of property IDs in the current property set.

#### Parameters

- props : (int, ...)

 Sequence containing the property IDs.

- names : (string, ...)

 Equal length sequence of property names.


---

<!-- object: PyIPropertyStore -->


<!-- page: PyIPropertyStore.html -->

---

## PyIPropertyStore Object

 Contains a collection of properties

#### Methods

- GetCount

 Returns the number of properties in the store

- GetAt

 Returns the property key for the specified property

- GetValue

 Retrieves the value of a property

- SetValue

 Sets the value of a property

- Commit

 Commits property changes


<!-- page: PyIPropertyStore__Commit_meth.html -->

## PyIPropertyStore.Commit

 Commit()

Commits property changes


<!-- page: PyIPropertyStore__GetAt_meth.html -->

## PyIPropertyStore.GetAt

 PyPROPERTYKEY = GetAt(iProp)

Returns the property key for the specified property

#### Parameters

- iProp : int

 Zero-based index of property


<!-- page: PyIPropertyStore__GetCount_meth.html -->

## PyIPropertyStore.GetCount

 int = GetCount()

Returns the number of properties in the store


<!-- page: PyIPropertyStore__GetValue_meth.html -->

## PyIPropertyStore.GetValue

 PyPROPVARIANT = GetValue(Key)

Retrieves the value of a property

#### Parameters

- Key : PyPROPERTYKEY

 Property key as returned by PyIPropertyStore::GetAt


<!-- page: PyIPropertyStore__SetValue_meth.html -->

## PyIPropertyStore.SetValue

 SetValue(Key, Value)

Sets the value of a property

#### Parameters

- Key : PyPROPERTYKEY

 Property key (see PyIPropertyStore::GetAt)

- Value : PyPROPVARIANT

 Variant value which can be converted to the appropriate variant type for the property Pass a VT_EMPTY variant to indicate that the property should be removed.


---

<!-- object: PyIPropertyStoreCache -->


<!-- page: PyIPropertyStoreCache.html -->

---

## PyIPropertyStoreCache Object

 Property store that allows tracking of modification state. Inherits all methods of PyIPropertyStore.

#### Methods

- GetState

 Retrieves the current state of a property

- GetValueAndState

 Retrieves the current value and state of a property

- SetState

 Sets the state of a property

- SetValueAndState

 Sets the value and state of a property


<!-- page: PyIPropertyStoreCache__GetState_meth.html -->

## PyIPropertyStoreCache.GetState

 int = GetState(key)

Retrieves the current state of a property

#### Parameters

- key : PyPROPERTYKEY

 Property identifier

#### Return Value

A value from the PSC_STATE enum (PSC_NORMAL, PSC_NOTINSOURCE. PSC_DIRTY)


<!-- page: PyIPropertyStoreCache__GetValueAndState_meth.html -->

## PyIPropertyStoreCache.GetValueAndState

 (PyPROPVARIANT, int) = GetValueAndState(key)

Retrieves the current value and state of a property

#### Parameters

- key : PyPROPERTYKEY

 Property identifier


<!-- page: PyIPropertyStoreCache__SetState_meth.html -->

## PyIPropertyStoreCache.SetState

 SetState(key, state)

Sets the state of a property

#### Parameters

- key : PyPROPERTYKEY

 Property identifier

- state : int

 Value from the PSC_STATE enum (pscon.PSC_*)


<!-- page: PyIPropertyStoreCache__SetValueAndState_meth.html -->

## PyIPropertyStoreCache.SetValueAndState

 SetValueAndState(key, value, state)

Sets the value and state of a property

#### Parameters

- key : PyPROPERTYKEY

 Property identifier

- value : PyPROPVARIANT

 The new value

- state : int

 The new state (pscon.PSC_*)


---

<!-- object: PyIPropertyStoreCapabilities -->


<!-- page: PyIPropertyStoreCapabilities.html -->

---

## PyIPropertyStoreCapabilities Object

 Property providers use this interface to indicate whether properties are writeable.

#### Methods

- IsPropertyWritable

 Asks provider if a property can be editted.


<!-- page: PyIPropertyStoreCapabilities__IsPropertyWritable_meth.html -->

## PyIPropertyStoreCapabilities.IsPropertyWritable

 boolean = IsPropertyWritable(key)

Asks provider if a property can be editted.

#### Parameters

- key : PyPROPERTYKEY

 Property identifier


---

<!-- object: PyIPropertySystem -->


<!-- page: PyIPropertySystem.html -->

---

## PyIPropertySystem Object

 Wraps the IPropertySystem interface

#### Methods

- GetPropertyDescription

 Returns an interface used to describe a property

- GetPropertyDescriptionByName

 Returns an interface used to describe a property

- GetPropertyDescriptionListFromString

 Retrieves property descriptions from a string of property names

- EnumeratePropertyDescriptions

 Returns an interface used to list defined properties

- FormatForDisplay

 Formats a property into a string

- RegisterPropertySchema

 Registers a set of properties defined in a .propdesc file

- UnregisterPropertySchema

 Removes a set of registered properties

- RefreshPropertySchema

 Not currently implemented by the OS


<!-- page: PyIPropertySystem__EnumeratePropertyDescriptions_meth.html -->

## PyIPropertySystem.EnumeratePropertyDescriptions

 PyIPropertyDescriptionList = EnumeratePropertyDescriptions(Filter, riid )

Returns an interface used to list defined properties

#### Parameters

- Filter=PDEF_ALL : int

 Value from PROPDESC_ENUMFILTER (pscon.PDEF_*) that limits what types of properties are listed

- riid=IID_IPropertyDescriptionList : PyIID

 The interface to return


<!-- page: PyIPropertySystem__FormatForDisplay_meth.html -->

## PyIPropertySystem.FormatForDisplay

 str = FormatForDisplay(Key, Value , Flags )

Formats a property into a string

#### Parameters

- Key : PyPROPERTYKEY

 Fmtid and property id that identifies the property

- Value : PyPROPVARIANT

 The value to format

- Flags=PDFF_DEFAULT : int

 Combination of PROPDESC_FORMAT_FLAGS (pscon.PDFF_*) indicating formatting options


<!-- page: PyIPropertySystem__GetPropertyDescriptionByName_meth.html -->

## PyIPropertySystem.GetPropertyDescriptionByName

 PyIPropertyDescription = GetPropertyDescriptionByName(CanonicalName, riid )

Returns an interface used to describe a property

#### Parameters

- CanonicalName : str

 Registered name of the property

- riid=IID_IPropertyDescription : PyIID

 The interface to return


<!-- page: PyIPropertySystem__GetPropertyDescriptionListFromString_meth.html -->

## PyIPropertySystem.GetPropertyDescriptionListFromString

 PyIPropertyDescriptionList = GetPropertyDescriptionListFromString(PropList, riid )

Retrieves property descriptions from a string of property names

#### Parameters

- PropList : str

 String containing a list of properties and flags

- riid=IPropertyDescriptionList : PyIID

 The interface to return


<!-- page: PyIPropertySystem__GetPropertyDescription_meth.html -->

## PyIPropertySystem.GetPropertyDescription

 PyIPropertyDescription = GetPropertyDescription(Key, riid )

Returns an interface used to describe a property

#### Parameters

- Key : PyPROPERTYKEY

 Fmtid and propertyid that uniquely identifies a property

- riid=IID_IPropertyDescription : PyIID

 The interface to return


<!-- page: PyIPropertySystem__RefreshPropertySchema_meth.html -->

## PyIPropertySystem.RefreshPropertySchema

 RefreshPropertySchema()

Not currently implemented by the OS

#### Comments

 Not currently implemented, according to MSDN


<!-- page: PyIPropertySystem__RegisterPropertySchema_meth.html -->

## PyIPropertySystem.RegisterPropertySchema

 RegisterPropertySchema(Path)

Registers a set of properties defined in a .propdesc file

#### Parameters

- Path : str

 Path to a property schema XML file (.propdesc)


<!-- page: PyIPropertySystem__UnregisterPropertySchema_meth.html -->

## PyIPropertySystem.UnregisterPropertySchema

 UnregisterPropertySchema(Path)

Removes a set of registered properties

#### Parameters

- Path : str

 Path to a property schema XML file (.propdesc)


---

<!-- object: PyIProvideClassInfo -->


<!-- page: PyIProvideClassInfo.html -->

---

## PyIProvideClassInfo Object

 A Python interface to IProvideClassInfo

#### Methods

- GetClassInfo

 Gets information about the CO_CLASS.

#### Based On

PyIUnknown


<!-- page: PyIProvideClassInfo__GetClassInfo_meth.html -->

## PyIProvideClassInfo.GetClassInfo

 PyITypeInfo = GetClassInfo()

Gets information about the CO_CLASS.


---

<!-- object: PyIProvideClassInfo2 -->


<!-- page: PyIProvideClassInfo2.html -->

---

## PyIProvideClassInfo2 Object

#### Methods

- GetGUID

 Gets the default event sink IID for the object (if any).

#### Based On

PyIProvideClassInfo


<!-- page: PyIProvideClassInfo2__GetGUID_meth.html -->

## PyIProvideClassInfo2.GetGUID

 PyIID = GetGUID(flags)

Gets the GUID for the object.

#### Parameters

- flags : int

 The flags for the GUID.


---

<!-- object: PyIProvideExpressionContexts -->


<!-- page: PyIProvideExpressionContexts.html -->

---

## PyIProvideExpressionContexts Object

 Description of the interface

#### Methods

- EnumExpressionContexts

 Description of EnumExpressionContexts


<!-- page: PyIProvideExpressionContexts__EnumExpressionContexts_meth.html -->

## PyIProvideExpressionContexts.EnumExpressionContexts

 EnumExpressionContexts()

Description of EnumStackFrames.


---

<!-- object: PyIProvideTaskPage -->


<!-- page: PyIProvideTaskPage.html -->

---

## PyIProvideTaskPage Object

 Description of the interface

#### Methods

- GetPage

 Return a property sheet page handle for the spedified type (TASKPAGE_TASK,TASKPAGE_SCHEDULE,TASKPAGE_SETTINGS)


<!-- page: PyIProvideTaskPage__GetPage_meth.html -->

## PyIProvideTaskPage.GetPage

 GetPage(tpType, PersistChanges)

Return a property sheet page handle for the spedified type (TASKPAGE_TASK,TASKPAGE_SCHEDULE,TASKPAGE_SETTINGS)

#### Parameters

- tpType : int

 Type of page to retreive (TASKPAGE_TASK,TASKPAGE_SCHEDULE,TASKPAGE_SETTINGS)

- PersistChanges : bool

 Indicates if changes should be saved automatically

#### Comments

 There's not yet anything useful that can be done with this handle - return type subject to change


---

<!-- object: PyIQueryAssociations -->


<!-- page: PyIQueryAssociations.html -->

---

## PyIQueryAssociations Object

 Description of the interface

#### Methods

- Init

 Initializes the IQueryAssociations interface and sets the root key to the appropriate ProgID.

- GetKey

 Searches for and retrieves a file association-related key from the registry.

- GetString

 Searches for and retrieves a file association-related string from the registry.


<!-- page: PyIQueryAssociations__GetKey_meth.html -->

## PyIQueryAssociations.GetKey

 int = GetKey(flags, assocKey , )

Searches for and retrieves a file association-related key from the registry.

#### Parameters

- flags : int

 Used to control the search.

- assocKey : int

 Specifies the type of key that is to be returned.

- =extra : string

 Optional string with information about the location of the key. It is normally set to a shell verb such as 'open'. Set this parameter to None if it is not used.


<!-- page: PyIQueryAssociations__GetString_meth.html -->

## PyIQueryAssociations.GetString

 int = GetString(flags, assocStr , )

Searches for and retrieves a file association-related string from the registry.

#### Parameters

- flags : int

 Used to control the search.

- assocStr : int

 Specifies the type of string that is to be returned.

- =extra : string

 Optional string with information about the location of the key. It is normally set to a shell verb such as 'open'. Set this parameter to None if it is not used.

#### Comments

 Note that ASSOCF_NOTRUNCATE semantics are currently not supported - the buffer passed is 2048 bytes long, and will be truncated by the shell if too small.


<!-- page: PyIQueryAssociations__Init_meth.html -->

## PyIQueryAssociations.Init

 Init(flags, assoc, hkeyProgId, hwnd)

Initializes the IQueryAssociations interface and sets the root key to the appropriate ProgID.

#### Parameters

- flags : int

 One of shellcon.ASSOCF_* flags

- assoc : string

 The string data (ie, extension, prog-id, etc)

- hkeyProgId=None : PyHKEY

 Root registry key, can be None

- hwnd=None : PyHANDLE

 Reserved, must be 0 or None


---

<!-- object: PyIRelatedItem -->


<!-- page: PyIRelatedItem.html -->

---

## PyIRelatedItem Object

 Interface used as the base for objects that have a related shell item (eg ITransferMediumItem, IDisplayItem, etc). Should not be used directly.

#### Methods

- GetItemIDList

 Returns the ID list of the related item

- GetItem

 Returns the related item


<!-- page: PyIRelatedItem__GetItemIDList_meth.html -->

## PyIRelatedItem.GetItemIDList

 PyIDL = GetItemIDList()

Returns the ID list of the related item


<!-- page: PyIRelatedItem__GetItem_meth.html -->

## PyIRelatedItem.GetItem

 PyIShellItem = GetItem()

Returns the related item


---

<!-- object: PyIRemoteDebugApplication -->


<!-- page: PyIRemoteDebugApplication.html -->

---

## PyIRemoteDebugApplication Object

 Description of the interface

#### Methods

- ResumeFromBreakPoint

 Continue an application which is currently in a breakpoint.

- CauseBreak

 Causes the application to break into the debugger at the earliest opportunity.

- ConnectDebugger

 Connects a debugger to the application.

- DisconnectDebugger

 Disconnects the current debugger from the application.

- GetDebugger

 Returns the current debugger connected to the application.

- CreateInstanceAtApplication

 Create objects in the application process address space.

- QueryAlive

 Indicates if the application is alive.

- EnumThreads

 Enumerates all threads known to be associated with the application.

- GetName

 Description of GetName

- GetRootNode

 Returns the application node under which all nodes associated with the application are added.

- EnumGlobalExpressionContexts

 Enumerates all global expression contexts.


<!-- page: PyIRemoteDebugApplication__CauseBreak_meth.html -->

## PyIRemoteDebugApplication.CauseBreak

 CauseBreak()

Causes the application to break into the debugger at the earliest opportunity.

#### Comments

 Note that a long time may elapse before the application actually breaks, particularly if the application is not currently executing script code.


<!-- page: PyIRemoteDebugApplication__ConnectDebugger_meth.html -->

## PyIRemoteDebugApplication.ConnectDebugger

 ConnectDebugger(pad)

Connects a debugger to the application.

#### Parameters

- pad : PyIApplicationDebugger

 Description for pad

#### Comments

 Only one debugger may be connected at a time; this method fails if there is already a debugger connected.


<!-- page: PyIRemoteDebugApplication__CreateInstanceAtApplication_meth.html -->

## PyIRemoteDebugApplication.CreateInstanceAtApplication

 PyIUnknown = CreateInstanceAtApplication(rclsid, pUnkOuter , dwClsContext , riid )

Create objects in the application process address space.

#### Parameters

- rclsid : PyIID

 Description for rclsid

- pUnkOuter : PyIUnknown

 Description for pUnkOuter

- dwClsContext : int

 Description for dwClsContext

- riid : PyIID

 Description for riid

#### Comments

 Provides a mechanism for the debugger IDE, running out-of-process to the application, to create objects in the application process. This method simply delegates to CoCreateInstance.


<!-- page: PyIRemoteDebugApplication__DisconnectDebugger_meth.html -->

## PyIRemoteDebugApplication.DisconnectDebugger

 DisconnectDebugger()

Disconnects the current debugger from the application.


<!-- page: PyIRemoteDebugApplication__EnumGlobalExpressionContexts_meth.html -->

## PyIRemoteDebugApplication.EnumGlobalExpressionContexts

 IEnumDebugExpressionContexts = EnumGlobalExpressionContexts()

Enumerates all global expression contexts


<!-- page: PyIRemoteDebugApplication__EnumThreads_meth.html -->

## PyIRemoteDebugApplication.EnumThreads

 PyIEnumRemoteDebugApplicationThreads = EnumThreads()

Enumerates all threads known to be associated with the application.

#### Comments

 New threads may be added at any time.


<!-- page: PyIRemoteDebugApplication__GetDebugger_meth.html -->

## PyIRemoteDebugApplication.GetDebugger

 PyIApplicationDebugger = GetDebugger()

Returns the current debugger connected to the application.


<!-- page: PyIRemoteDebugApplication__GetName_meth.html -->

## PyIRemoteDebugApplication.GetName

 GetName()

Description of GetName.


<!-- page: PyIRemoteDebugApplication__GetRootNode_meth.html -->

## PyIRemoteDebugApplication.GetRootNode

 PyIDebugApplicationNode = GetRootNode()

Returns the application node under which all nodes associated with the application are added.


<!-- page: PyIRemoteDebugApplication__QueryAlive_meth.html -->

## PyIRemoteDebugApplication.QueryAlive

 QueryAlive()

Returns True if alive, else False.


<!-- page: PyIRemoteDebugApplication__ResumeFromBreakPoint_meth.html -->

## PyIRemoteDebugApplication.ResumeFromBreakPoint

 ResumeFromBreakPoint(prptFocus, bra, era)

Continue an application which is currently in a breakpoint.

#### Parameters

- prptFocus : PyIRemoteDebugApplicationThread

 Description for prptFocus

- bra : int

 Break resume action

- era : int

 Error resume action


---

<!-- object: PyIRemoteDebugApplicationEvents -->


<!-- page: PyIRemoteDebugApplicationEvents.html -->

---

## PyIRemoteDebugApplicationEvents Object

 Description of the interface

#### Methods

- OnConnectDebugger

 Description of OnConnectDebugger

- OnDisconnectDebugger

 Description of OnDisconnectDebugger

- OnSetName

 Description of OnSetName

- OnDebugOutput

 Description of OnDebugOutput

- OnClose

 Description of OnClose

- OnEnterBreakPoint

 Description of OnEnterBreakPoint

- OnLeaveBreakPoint

 Description of OnLeaveBreakPoint

- OnCreateThread

 Description of OnCreateThread

- OnDestroyThread

 Description of OnDestroyThread

- OnBreakFlagChange

 Description of OnBreakFlagChange


<!-- page: PyIRemoteDebugApplicationEvents__OnBreakFlagChange_meth.html -->

## PyIRemoteDebugApplicationEvents.OnBreakFlagChange

 OnBreakFlagChange(abf, prdatSteppingThread)

Description of OnBreakFlagChange.

#### Parameters

- abf : int

 Description for abf

- prdatSteppingThread : PyIRemoteDebugApplicationThread

 Description for prdatSteppingThread


<!-- page: PyIRemoteDebugApplicationEvents__OnClose_meth.html -->

## PyIRemoteDebugApplicationEvents.OnClose

 OnClose()

Description of OnClose.


<!-- page: PyIRemoteDebugApplicationEvents__OnConnectDebugger_meth.html -->

## PyIRemoteDebugApplicationEvents.OnConnectDebugger

 OnConnectDebugger(pad)

Description of OnConnectDebugger.

#### Parameters

- pad : PyIApplicationDebugger

 Description for pad


<!-- page: PyIRemoteDebugApplicationEvents__OnCreateThread_meth.html -->

## PyIRemoteDebugApplicationEvents.OnCreateThread

 OnCreateThread(prdat)

Description of OnCreateThread.

#### Parameters

- prdat : PyIRemoteDebugApplicationThread

 Description for prdat


<!-- page: PyIRemoteDebugApplicationEvents__OnDebugOutput_meth.html -->

## PyIRemoteDebugApplicationEvents.OnDebugOutput

 OnDebugOutput(pstr)

Description of OnDebugOutput.

#### Parameters

- pstr : unicode

 Description for pstr


<!-- page: PyIRemoteDebugApplicationEvents__OnDestroyThread_meth.html -->

## PyIRemoteDebugApplicationEvents.OnDestroyThread

 OnDestroyThread(prdat)

Description of OnDestroyThread.

#### Parameters

- prdat : PyIRemoteDebugApplicationThread

 Description for prdat


<!-- page: PyIRemoteDebugApplicationEvents__OnDisconnectDebugger_meth.html -->

## PyIRemoteDebugApplicationEvents.OnDisconnectDebugger

 OnDisconnectDebugger()

Description of OnDisconnectDebugger.


<!-- page: PyIRemoteDebugApplicationEvents__OnEnterBreakPoint_meth.html -->

## PyIRemoteDebugApplicationEvents.OnEnterBreakPoint

 OnEnterBreakPoint(prdat)

Description of OnEnterBreakPoint.

#### Parameters

- prdat : PyIRemoteDebugApplicationThread

 Description for prdat


<!-- page: PyIRemoteDebugApplicationEvents__OnLeaveBreakPoint_meth.html -->

## PyIRemoteDebugApplicationEvents.OnLeaveBreakPoint

 OnLeaveBreakPoint(prdat)

Description of OnLeaveBreakPoint.

#### Parameters

- prdat : PyIRemoteDebugApplicationThread

 Description for prdat


<!-- page: PyIRemoteDebugApplicationEvents__OnSetName_meth.html -->

## PyIRemoteDebugApplicationEvents.OnSetName

 OnSetName(pstrName)

Description of OnSetName.

#### Parameters

- pstrName : unicode

 Description for pstrName


---

<!-- object: PyIRemoteDebugApplicationThread -->


<!-- page: PyIRemoteDebugApplicationThread.html -->

---

## PyIRemoteDebugApplicationThread Object

 Description of the interface

#### Methods

- GetSystemThreadId

 Description of GetSystemThreadId

- GetApplication

 Description of GetApplication

- EnumStackFrames

 Description of EnumStackFrames

- GetDescription

 Description of GetDescription

- SetNextStatement

 Description of SetNextStatement

- GetState

 Description of GetState

- Suspend

 Description of Suspend

- Resume

 Description of Resume

- GetSuspendCount

 Description of GetSuspendCount


<!-- page: PyIRemoteDebugApplicationThread__EnumStackFrames_meth.html -->

## PyIRemoteDebugApplicationThread.EnumStackFrames

 EnumStackFrames()

Description of EnumStackFrames.


<!-- page: PyIRemoteDebugApplicationThread__GetApplication_meth.html -->

## PyIRemoteDebugApplicationThread.GetApplication

 GetApplication()

Description of GetApplication.


<!-- page: PyIRemoteDebugApplicationThread__GetDescription_meth.html -->

## PyIRemoteDebugApplicationThread.GetDescription

 GetDescription()

Description of GetDescription.


<!-- page: PyIRemoteDebugApplicationThread__GetState_meth.html -->

## PyIRemoteDebugApplicationThread.GetState

 GetState()

Description of GetState.


<!-- page: PyIRemoteDebugApplicationThread__GetSuspendCount_meth.html -->

## PyIRemoteDebugApplicationThread.GetSuspendCount

 GetSuspendCount()

Description of GetSuspendCount.


<!-- page: PyIRemoteDebugApplicationThread__GetSystemThreadId_meth.html -->

## PyIRemoteDebugApplicationThread.GetSystemThreadId

 GetSystemThreadId()

Description of GetSystemThreadId.


<!-- page: PyIRemoteDebugApplicationThread__Resume_meth.html -->

## PyIRemoteDebugApplicationThread.Resume

 Resume()

Description of Resume.


<!-- page: PyIRemoteDebugApplicationThread__SetNextStatement_meth.html -->

## PyIRemoteDebugApplicationThread.SetNextStatement

 SetNextStatement(pStackFrame, pCodeContext)

Description of SetNextStatement.

#### Parameters

- pStackFrame : PyIDebugStackFrame

 Description for pStackFrame

- pCodeContext : PyIDebugCodeContext

 Description for pCodeContext


<!-- page: PyIRemoteDebugApplicationThread__Suspend_meth.html -->

## PyIRemoteDebugApplicationThread.Suspend

 Suspend()

Description of Suspend.


---

<!-- object: PyIRunningObjectTable -->


<!-- page: PyIRunningObjectTable.html -->

---

## PyIRunningObjectTable Object

 A Python interface to IRunningObjectTable

#### Methods

- Register

 Registers an object in the ROT

- Revoke

 Revokes a previously registered object

- IsRunning

 Checks whether an object is running.

- GetObject

 Checks whether an object is running.

- EnumRunning

 Creates an enumerator that can list the monikers of all the objects currently registered in the Running Object Table (ROT).

#### Based On

PyIUnknown


<!-- page: PyIRunningObjectTable__EnumRunning_meth.html -->

## PyIRunningObjectTable.EnumRunning

 PyIEnumMoniker = EnumRunning()

Creates an enumerator that can list the monikers of all the objects currently registered in the Running Object Table (ROT).


<!-- page: PyIRunningObjectTable__GetObject_meth.html -->

## PyIRunningObjectTable.GetObject

 PyIUnknown = GetObject(objectName)

Checks whether an object is running.

#### Parameters

- objectName : PyIMoniker

 The PyIMoniker interface on the moniker to search for in the Running Object Table.


<!-- page: PyIRunningObjectTable__IsRunning_meth.html -->

## PyIRunningObjectTable.IsRunning

 int = IsRunning(objectName)

Checks whether an object is running.

#### Parameters

- objectName : PyIMoniker

 The PyIMoniker interface on the moniker to search for in the Running Object Table.

| | Return Value | Description
| | S_OK (ie, 0) | The object identified by objectName is running.
| | S_FALSE (ie, 1) | There is no entry for objectName in the ROT, or that the object it identifies is no longer running (in which case, the entry is revoked).


<!-- page: PyIRunningObjectTable__Register_meth.html -->

## PyIRunningObjectTable.Register

 int = Register()

Registers an object and its identifying moniker in the Running Object Table (ROT).


<!-- page: PyIRunningObjectTable__Revoke_meth.html -->

## PyIRunningObjectTable.Revoke

 int = Revoke()

Removes from the Running Object Table (ROT) an entry that was previously registered by a call to PyIRunningObjectTable::Register.


---

<!-- object: PyIScheduledWorkItem -->


<!-- page: PyIScheduledWorkItem.html -->

---

## PyIScheduledWorkItem Object

 Python object that encapsulates the IScheduledWorkItem interface

#### Methods

- CreateTrigger

 Creates a new trigger for a task, returns index and new ITaskTrigger interface

- DeleteTrigger

 Deletes specified trigger

- GetTriggerCount

 Returns number of triggers defined for the task

- GetTrigger

 Retrieves ITaskTrigger interface for specified trigger index

- GetTriggerString

 Creates a human-readable summary of specified trigger

- GetRunTimes

 Return specified number of run times within given time frame

- GetNextRunTime

 Returns next time that task is scheduled to run

- SetIdleWait

 Sets idle parms for task with trigger of type TASK_EVENT_TRIGGER_ON_IDLE

- GetIdleWait

 Gets idle parms for task with trigger of type TASK_EVENT_TRIGGER_ON_IDLE

- Run

 Starts task

- Terminate

 Terminate process if task is running

- EditWorkItem

 Brings up standard Scheduled Task dialog

- GetMostRecentRunTime

 Returns last time task ran

- GetStatus

 Returns status (SCHED_S_TASK... constants)

- GetExitCode

 Returns tuple of task's exit code and error returned to Task Scheduler if process could not start

- SetComment

 Set comment string for task

- GetComment

 Return comment string associated with task.

- SetCreator

 Specify who (or what) created task, can be any string

- GetCreator

 Returns creator info, can be any string data

- SetWorkItemData

 Set data associated with task (treated as uninterpreted bytes)

- GetWorkItemData

 Retrieve data associated with task

- SetErrorRetryCount

 Specify nbr of times to attempt to run task if it can't start (not currently implemented)

- GetErrorRetryCount

 Return nbr of times Task scheduler should try to run task (not currently implemented)

- SetErrorRetryInterval

 Interval in minutes between attempts to run task. Not implemented according to SDK

- GetErrorRetryInterval

 Returns nbr of minutes between attempts to run task. Not implemented according to SDK

- SetFlags

 Set flags for task

- GetFlags

 Returns flags for task (TASK_FLAG_* constants)

- SetAccountInformation

 Set username and password under which task will run

- GetAccountInformation

 Returns username that task will run under


<!-- page: PyIScheduledWorkItem__CreateTrigger_meth.html -->

## PyIScheduledWorkItem.CreateTrigger

 int,PyITaskTrigger = CreateTrigger()

Creates a new trigger for a task, returns index and new ITaskTrigger interface


<!-- page: PyIScheduledWorkItem__DeleteTrigger_meth.html -->

## PyIScheduledWorkItem.DeleteTrigger

 DeleteTrigger(Trigger)

Deletes specified trigger

#### Parameters

- Trigger : int

 Index of trigger to delete


<!-- page: PyIScheduledWorkItem__EditWorkItem_meth.html -->

## PyIScheduledWorkItem.EditWorkItem

 EditWorkItem(hParent, dwReserved)

Brings up standard Scheduled Task dialog

#### Parameters

- hParent : PyHANDLE

 Reserved, use 0 or None if passed

- dwReserved : int

 Reserved, use 0 if passed


<!-- page: PyIScheduledWorkItem__GetAccountInformation_meth.html -->

## PyIScheduledWorkItem.GetAccountInformation

 PyUNICODE = GetAccountInformation()

Returns username that task will run under


<!-- page: PyIScheduledWorkItem__GetComment_meth.html -->

## PyIScheduledWorkItem.GetComment

 PyUnicode = GetComment()

Return comment string associated with task.


<!-- page: PyIScheduledWorkItem__GetCreator_meth.html -->

## PyIScheduledWorkItem.GetCreator

 GetCreator()

Returns creator info, can be any string data


<!-- page: PyIScheduledWorkItem__GetErrorRetryCount_meth.html -->

## PyIScheduledWorkItem.GetErrorRetryCount

 GetErrorRetryCount()

Return nbr of times Task scheduler should try to run task (not currently implemented)


<!-- page: PyIScheduledWorkItem__GetErrorRetryInterval_meth.html -->

## PyIScheduledWorkItem.GetErrorRetryInterval

 GetErrorRetryInterval()

Returns nbr of minutes between attempts to run task. Not implemented according to SDK


<!-- page: PyIScheduledWorkItem__GetExitCode_meth.html -->

## PyIScheduledWorkItem.GetExitCode

 (int,int) = GetExitCode()

Returns tuple of task's exit code and error returned to Task Scheduler if process could not start


<!-- page: PyIScheduledWorkItem__GetFlags_meth.html -->

## PyIScheduledWorkItem.GetFlags

 int = GetFlags()

Returns flags for task (TASK_FLAG_* constants)


<!-- page: PyIScheduledWorkItem__GetIdleWait_meth.html -->

## PyIScheduledWorkItem.GetIdleWait

 int,int = GetIdleWait()

Gets IdleMinutes and DeadlineMinutes parms for task with trigger of type TASK_EVENT_TRIGGER_ON_IDLE


<!-- page: PyIScheduledWorkItem__GetMostRecentRunTime_meth.html -->

## PyIScheduledWorkItem.GetMostRecentRunTime

 PyDateTime = GetMostRecentRunTime()

Returns last time task ran


<!-- page: PyIScheduledWorkItem__GetNextRunTime_meth.html -->

## PyIScheduledWorkItem.GetNextRunTime

 PyDateTime = GetNextRunTime()

Returns next time that task is scheduled to run


<!-- page: PyIScheduledWorkItem__GetRunTimes_meth.html -->

## PyIScheduledWorkItem.GetRunTimes

 (PyDateTime,,,) = GetRunTimes(Count, Begin , End )

Return specified number of run times within given time frame

#### Parameters

- Count : int

 Number of run times to retrieve

- Begin : PyDateTime

 Start time, defaults to current time if not passed or None

- End : PyDateTime

 End time, defaults to unlimited if not passed or None


<!-- page: PyIScheduledWorkItem__GetStatus_meth.html -->

## PyIScheduledWorkItem.GetStatus

 int = GetStatus()

Returns status (SCHED_S_TASK... constants)


<!-- page: PyIScheduledWorkItem__GetTriggerCount_meth.html -->

## PyIScheduledWorkItem.GetTriggerCount

 int = GetTriggerCount()

Returns number of triggers defined for the task


<!-- page: PyIScheduledWorkItem__GetTriggerString_meth.html -->

## PyIScheduledWorkItem.GetTriggerString

 PyUNICODE = GetTriggerString()

Creates a human-readable summary of specified trigger


<!-- page: PyIScheduledWorkItem__GetTrigger_meth.html -->

## PyIScheduledWorkItem.GetTrigger

 PyITaskTrigger = GetTrigger(iTrigger)

Retrieves ITaskTrigger interface for specified trigger index

#### Parameters

- iTrigger : int

 Index of trigger to retrieve


<!-- page: PyIScheduledWorkItem__GetWorkItemData_meth.html -->

## PyIScheduledWorkItem.GetWorkItemData

 string = GetWorkItemData()

Retrieve data associated with task


<!-- page: PyIScheduledWorkItem__Run_meth.html -->

## PyIScheduledWorkItem.Run

 Run()

Starts task


<!-- page: PyIScheduledWorkItem__SetAccountInformation_meth.html -->

## PyIScheduledWorkItem.SetAccountInformation

 SetAccountInformation(AccountName, Password)

Set username and password under which task will run

#### Parameters

- AccountName : unicode

 AccountName, use "" for local system account (can only be used by Administrators)

- Password : unicode

 Password - Can be None for local System account, or if TASK_FLAG_RUN_ONLY_IF_LOGGED_ON is set

#### Comments

 On some systems, username and password are verified at the time the task is saved, on others when the task tries to run


<!-- page: PyIScheduledWorkItem__SetComment_meth.html -->

## PyIScheduledWorkItem.SetComment

 SetComment(Comment)

Set comment string for task

#### Parameters

- Comment : unicode

 Freeform comment string


<!-- page: PyIScheduledWorkItem__SetCreator_meth.html -->

## PyIScheduledWorkItem.SetCreator

 SetCreator(Creator)

Specify who (or what) created task, can be any string

#### Parameters

- Creator : unicode

 Originator of task, does not have to be valid username


<!-- page: PyIScheduledWorkItem__SetErrorRetryCount_meth.html -->

## PyIScheduledWorkItem.SetErrorRetryCount

 SetErrorRetryCount(wRetryCount)

Specify nbr of times to attempt to run task if it can't start (not currently implemented)

#### Parameters

- wRetryCount : int

 Nbr of attemps to start task


<!-- page: PyIScheduledWorkItem__SetErrorRetryInterval_meth.html -->

## PyIScheduledWorkItem.SetErrorRetryInterval

 SetErrorRetryInterval(RetryInterval)

Interval in minutes between attempts to run task. Not implemented according to SDK

#### Parameters

- RetryInterval : int

 Interval in minutes


<!-- page: PyIScheduledWorkItem__SetFlags_meth.html -->

## PyIScheduledWorkItem.SetFlags

 SetFlags(dwFlags)

Set flags for task

#### Parameters

- dwFlags : int

 Combination of TASK_FLAG_* constants


<!-- page: PyIScheduledWorkItem__SetIdleWait_meth.html -->

## PyIScheduledWorkItem.SetIdleWait

 SetIdleWait(wIdleMinutes, wDeadlineMinutes)

Sets idle parms for task with trigger of type TASK_EVENT_TRIGGER_ON_IDLE

#### Parameters

- wIdleMinutes : int

 Nbr of minutes computer must be idle before task fires

- wDeadlineMinutes : int

 Maximum nbr of minutes task will wait for computer to become idle


<!-- page: PyIScheduledWorkItem__SetWorkItemData_meth.html -->

## PyIScheduledWorkItem.SetWorkItemData

 SetWorkItemData(Data)

Set data associated with task (treated as uninterpreted bytes)

#### Parameters

- Data : string

 Character data, treated as uninterpreted bytes


<!-- page: PyIScheduledWorkItem__Terminate_meth.html -->

## PyIScheduledWorkItem.Terminate

 Terminate()

Terminate process if task is running


---

<!-- object: PyIServerSecurity -->


<!-- page: PyIServerSecurity.html -->

---

## PyIServerSecurity Object

 Interface used to access client security settings and perform impersonation

#### Comments

 Can be created using pythoncom::CoGetCallContext

#### Methods

- QueryBlanket

 Retrieves security settings specified by the client

- ImpersonateClient

 Initiates impersonation of client

- RevertToSelf

 Ends impersonation of client

- IsImpersonating

 Determines if server is currently impersonating a client


<!-- page: PyIServerSecurity__ImpersonateClient_meth.html -->

## PyIServerSecurity.ImpersonateClient

 ImpersonateClient()

Initiates impersonation of client


<!-- page: PyIServerSecurity__IsImpersonating_meth.html -->

## PyIServerSecurity.IsImpersonating

 bool = IsImpersonating()

Determines if server is currently impersonating a client


<!-- page: PyIServerSecurity__QueryBlanket_meth.html -->

## PyIServerSecurity.QueryBlanket

 dict = QueryBlanket(Capabilities)

Retrieves security settings specified by the client

#### Parameters

- Capabilities=0 : int

 Can be EOAC_MAKE_FULLSIC for SChannel provider


<!-- page: PyIServerSecurity__RevertToSelf_meth.html -->

## PyIServerSecurity.RevertToSelf

 RevertToSelf()

Ends impersonation of client


---

<!-- object: PyIServiceProvider -->


<!-- page: PyIServiceProvider.html -->

---

## PyIServiceProvider Object

 A Python interface to IServiceProvider

#### Methods

- QueryService

 Creates or accesses the specified service and returns an interface object to the specified interface for the service.

#### Based On

PyIUnknown


<!-- page: PyIServiceProvider__QueryService_meth.html -->

## PyIServiceProvider.QueryService

 PyIUnknown = QueryService(clsid, iid )

Creates or accesses the specified service and returns an interface object to the specified interface for the service.

#### Parameters

- clsid : PyIID

 Unique identifier for the requested service.

- iid : PyIID

 Unique identifier for the requested interface on the service.


---

<!-- object: PyIShellBrowser -->


<!-- page: PyIShellBrowser.html -->

---

## PyIShellBrowser Object

 Exposed by Windows Explorer and the Open File common dialog box to provide services for namespace extensions.

#### Methods

- InsertMenusSB

 Updates a composite menu with container's options

- SetMenuSB

 Attaches a shared menu to a shell view window

- RemoveMenusSB

 Asks container to remove any items it added to a composite menu

- SetStatusTextSB

 Sets the status text in view's status bar

- EnableModelessSB

 Enables or disables modeless dialogs

- TranslateAcceleratorSB

 Translates keystrokes used as menu item activators

- BrowseObject

 Navigates to a different location

- GetViewStateStream

 Returns a stream that can be used to access view state information

- GetControlWindow

 Returns a handle to one of the browser's control elements

- SendControlMsg

 Sends a control msg to browser's toolbar or status bar

- QueryActiveShellView

 Returns the currently displayed view

- OnViewWindowActive

 Callback triggered when a view window is activated

- SetToolbarItems

 Adds toolbar buttons to the browser's toolbar


<!-- page: PyIShellBrowser__BrowseObject_meth.html -->

## PyIShellBrowser.BrowseObject

 BrowseObject(pidl, wFlags)

Navigates to a different location

#### Parameters

- pidl : PyIDL

 Item id list that specifies the new browse location, can be None

- wFlags : int

 Combination of shellcon.SBSP_* flags


<!-- page: PyIShellBrowser__EnableModelessSB_meth.html -->

## PyIShellBrowser.EnableModelessSB

 EnableModelessSB(fEnable)

Enables or disables modeless dialogs

#### Parameters

- fEnable : boolean

 Use True to enable or False to disable modeless dialog boxes


<!-- page: PyIShellBrowser__GetControlWindow_meth.html -->

## PyIShellBrowser.GetControlWindow

 GetControlWindow(id)

Returns a handle to one of the browser's control elements

#### Parameters

- id : int

 One of shellcon.FCW_* values


<!-- page: PyIShellBrowser__GetViewStateStream_meth.html -->

## PyIShellBrowser.GetViewStateStream

 PyIStream = GetViewStateStream(grfMode)

Returns a stream that can be used to access view state information

#### Parameters

- grfMode : int

 Read/write mode, one of STGM_READ,STGM_WRITE,STGM_READWRITE


<!-- page: PyIShellBrowser__InsertMenusSB_meth.html -->

## PyIShellBrowser.InsertMenusSB

 PyOLEMENUGROUPWIDTHS = InsertMenusSB(hmenuShared, lpMenuWidths )

Updates a composite menu with container's options

#### Parameters

- hmenuShared : PyHANDLE

 Newly created menu that contains no items

- lpMenuWidths : PyOLEMENUGROUPWIDTHS

 Tuple of 6 ints. Items 0,2,and 4 are updated when the tuple is returned.


<!-- page: PyIShellBrowser__OnViewWindowActive_meth.html -->

## PyIShellBrowser.OnViewWindowActive

 OnViewWindowActive(pshv)

Callback triggered when a view window is activated

#### Parameters

- pshv : PyIShellView

 The activated view object


<!-- page: PyIShellBrowser__QueryActiveShellView_meth.html -->

## PyIShellBrowser.QueryActiveShellView

 PyIShellView = QueryActiveShellView()

Returns the currently displayed view


<!-- page: PyIShellBrowser__RemoveMenusSB_meth.html -->

## PyIShellBrowser.RemoveMenusSB

 RemoveMenusSB(hmenuShared)

Asks container to remove any items it added to a composite menu

#### Parameters

- hmenuShared : PyHANDLE

 Handle to the composite menu


<!-- page: PyIShellBrowser__SendControlMsg_meth.html -->

## PyIShellBrowser.SendControlMsg

 int = SendControlMsg(id, uMsg , wParam , lParam )

Sends a control msg to browser's toolbar or status bar

#### Parameters

- id : int

 shellcon.FCW_TOOLBAR or FCW_STATUS

- uMsg : int

 The message to send

- wParam : int

 Value is dependent on the message

- lParam : long

 Value is dependent on the message


<!-- page: PyIShellBrowser__SetMenuSB_meth.html -->

## PyIShellBrowser.SetMenuSB

 SetMenuSB(hmenuShared, holemenuRes, hwndActiveObject)

Attaches a shared menu to a shell view window

#### Parameters

- hmenuShared : PyHANDLE

 Handle to the shared menu

- holemenuRes : PyHANDLE

 Reserved, use only None (or 0)

- hwndActiveObject : PyHANDLE

 Handle to the shell window


<!-- page: PyIShellBrowser__SetStatusTextSB_meth.html -->

## PyIShellBrowser.SetStatusTextSB

 SetStatusTextSB(pszStatusText)

Sets the status text in view's status bar

#### Parameters

- pszStatusText : str

 New status to be displayed


<!-- page: PyIShellBrowser__SetToolbarItems_meth.html -->

## PyIShellBrowser.SetToolbarItems

 SetToolbarItems(lpButtons, uFlags)

Adds toolbar buttons to the browser's toolbar

#### Parameters

- lpButtons : PyLPTBBUTTONSB

 Sequence of tuples describing the buttons to be added

- uFlags : int

 Indicates button positions, combination of shellcon.FCT_*


<!-- page: PyIShellBrowser__TranslateAcceleratorSB_meth.html -->

## PyIShellBrowser.TranslateAcceleratorSB

 TranslateAcceleratorSB(pmsg, wID)

Translates keystrokes used as menu item activators

#### Parameters

- pmsg : PyMSG

 Keystroke message to be translated

- wID : int

 Menu command id for the keystroke


---

<!-- object: PyIShellExtInit -->


<!-- page: PyIShellExtInit.html -->

---

## PyIShellExtInit Object

 Description of the interface

#### Methods

- Initialize

 Description of Initialize


<!-- page: PyIShellExtInit__Initialize_meth.html -->

## PyIShellExtInit.Initialize

 Initialize(pFolder, pDataObject, hkey)

Description of Initialize.

#### Parameters

- pFolder : PyIDL

 Description for pFolder

- pDataObject : PyIDataObject

 Description for pDataObject

- hkey : PyHANDLE

 Description for hkey


---

<!-- object: PyIShellFolder -->


<!-- page: PyIShellFolder.html -->

---

## PyIShellFolder Object

 Interface that represents an Explorer folder

#### Methods

- ParseDisplayName

 Returns the PIDL of an item in a shell folder

- EnumObjects

 Creates an enumerator to list the contents of the shell folder

- BindToObject

 Returns an IShellFolder interface for a subfolder

- BindToStorage

 Returns an interface to a storage object in a shell folder

- CompareIDs

 Determines the sorting order of 2 items in shell folder

- CreateViewObject

 Creates a view object for a shell folder.

- GetAttributesOf

 Queries attributes of items within the shell folder

- GetUIObjectOf

 Creates an interface to one or more items in a shell folder

- GetDisplayNameOf

 Returns the display name of an item within this shell folder

- SetNameOf

 Sets the display name of an item and changes its PIDL

- __iter__

 Enumerates all objects in this folder.


<!-- page: PyIShellFolder__BindToObject_meth.html -->

## PyIShellFolder.BindToObject

 PyIShellFolder = BindToObject(pidl, pbc , riid )

Returns an IShellFolder interface for a subfolder

#### Parameters

- pidl : PyIDL

 Relative item id list that identifies the subfolder, can be multi-level

- pbc : PyIBindCtx

 Bind context to be used, can be None

- riid : PyIID

 IID of the desired interface, usually IID_IShellFolder


<!-- page: PyIShellFolder__BindToStorage_meth.html -->

## PyIShellFolder.BindToStorage

 interface = BindToStorage(pidl, pbc , riid )

Returns an interface to a storage object in a shell folder

#### Parameters

- pidl : PyIDL

 Relative pidl for the folder item, must be a single item id

- pbc : PyIBindCtx

 Bind context that affects how binding is performed, can be None

- riid : PyIID

 IID of the desired interface, one of IID_IStream, IID_IStorage, IID_IPropertySetStorage

#### Return Value

Returns PyIStream, PyIStorage or PyIPropertySetStorage depending on the riid passed in


<!-- page: PyIShellFolder__CompareIDs_meth.html -->

## PyIShellFolder.CompareIDs

 int = CompareIDs(lparam, pidl1 , pidl2 )

Determines the sorting order of 2 items in shell folder

#### Parameters

- lparam : int

 Lower 16 bits specify folder-dependent sorting rules, 0 means to sort by display name. System folder view uses these as a column number.
 Upper sixteen bits is used for flags SHCIDS_ALLFIELDS or SHCIDS_CANONICALONLY

- pidl1 : PyIDL

 Item id list that idenfies an object relative to the folder

- pidl2 : PyIDL

 Item id list that idenfies an object relative to the folder

#### Return Value

Returns 0 if items compare equal, -1 if the pidl1 comes first, or 1 if pidl2 comes first


<!-- page: PyIShellFolder__CreateViewObject_meth.html -->

## PyIShellFolder.CreateViewObject

 PyIShellView = CreateViewObject(hwndOwner, riid )

Creates a view object for a shell folder.

#### Parameters

- hwndOwner : HWND

 Parent window for a custom folder view, or 0

- riid : PyIID

 IID of the desired interface, usually IID_IShellView


<!-- page: PyIShellFolder__EnumObjects_meth.html -->

## PyIShellFolder.EnumObjects

 PyIEnumIDList = EnumObjects(hwndOwner, grfFlags )

Creates an enumerator to list the contents of the shell folder

#### Parameters

- hwndOwner=None : PyHANDLE

 Window to use if any user interaction is required

- grfFlags=SHCONTF_FOLDERS|SHCONTF_NONFOLDERS|SHCONTF_INCLUDEHIDDEN : int

 Combination of shellcon.SHCONTF_* constants


<!-- page: PyIShellFolder__GetAttributesOf_meth.html -->

## PyIShellFolder.GetAttributesOf

 int = GetAttributesOf(pidl, rgfInOut )

Queries attributes of items within the shell folder

#### Parameters

- pidl : (PyIDL,...)

 A sequence of single-level pidls identifying items directly contained by the folder

- rgfInOut : int

 Combination of shellcon.SFGAO_* constants

#### Return Value

The requested attributes are only returned if they are common to all of the specified items


<!-- page: PyIShellFolder__GetDisplayNameOf_meth.html -->

## PyIShellFolder.GetDisplayNameOf

 str = GetDisplayNameOf(pidl, uFlags )

Returns the display name of an item within this shell folder

#### Parameters

- pidl : PyIDL

 PIDL that identifies the item relative to the parent folder

- uFlags : int

 Combination of shellcon.SHGDN_* flags


<!-- page: PyIShellFolder__GetUIObjectOf_meth.html -->

## PyIShellFolder.GetUIObjectOf

 int, PyIUnknown = GetUIObjectOf(hwndOwner, pidl , riid , Reserved , iidout )

Creates an interface to one or more items in a shell folder

#### Parameters

- hwndOwner : PyHANDLE

 Specifies a window in which to display any required dialogs or errors, can be 0

- pidl : (PyIDL,...)

 A sequence of single-level pidls identifying items in the folder

- riid : PyIID

 The interface to create, one of IID_IContextMenu, IID_IContextMenu2, IID_IDataObject, IID_IDropTarget, IID_IExtractIcon, IID_IQueryInfo

- Reserved=0 : int

 Reserved, use 0 if passed in

- iidout=riid : PyIID

 The interface to return. Can be used in the case where there is not a python wrapper for the desired interface. You must make certain that the interface identified by riid actually supports the iidout interface, or Bad Things Will Happen. It should always be safe to return PyIUnknown, which is the base for all interfaces.

#### Return Value

Returns the Reserved parameter and the requested interface


<!-- page: PyIShellFolder__ParseDisplayName_meth.html -->

## PyIShellFolder.ParseDisplayName

 tuple = ParseDisplayName(hwndOwner, pbc , DisplayName , Attributes )

Returns the PIDL of an item in a shell folder

#### Parameters

- hwndOwner : PyHANDLE

 Window in which to display any dialogs or message boxes, can be 0

- pbc : PyIBindCtx

 Bind context that affects how parsing is performed, can be None

- DisplayName : str

 Display name to parse, format is dependent on the shell folder. Desktop folder will accept a file path, as well as guids of the form ::{guid} Example: '::%s\\::%s' %(shell.CLSID_MyComputer,shell.CLSID_ControlPanel)

- Attributes=0 : int

 Combination of shellcon.SFGAO_* constants specifying which attributes should be returned

#### Return Value

The result is a tuple of cchEaten, pidl, attr

#### Items

- [0] int : cchEaten

 the number of characters of the input name that were parsed

- [1] PyIDL : pidl

 specifies the relative path from the parsing folder to the object

- [2] int : Attributes

 returns any requested attributes


<!-- page: PyIShellFolder__SetNameOf_meth.html -->

## PyIShellFolder.SetNameOf

 PyIDL = SetNameOf(hwndOwner, pidl , Name , Flags )

Sets the display name of an item and changes its PIDL

#### Parameters

- hwndOwner : HWND

 Window in which to display any message boxes or dialogs, can be 0

- pidl : PyIDL

 PIDL that identifies the item relative to the parent folder

- Name : str

 New name for the item

- Flags : int

 Combination of shellcon.SHGDM_* values

#### Return Value

Returns the new PIDL for item


---

<!-- object: PyIShellFolder2 -->


<!-- page: PyIShellFolder2.html -->

---

## PyIShellFolder2 Object

 Represents an explorer folder, giving access to details of items in the folder. Inherits all methods of PyIShellFolder.

#### Methods

- GetDefaultSearchGUID

 Retrieves the default search for the folder

- EnumSearches

 Returns an interface that lists searches defined for the folder

- GetDefaultColumn

 Returns the columns used for sorting and display

- GetDefaultColumnState

 Returns flags indicating the default behaviour of the column

- GetDetailsEx

 Returns the details of an item by Column ID

- GetDetailsOf

 Returns the value or title of a column in the folder's Details view.

- MapColumnToSCID

 Returns the unique identifier (FMTID, pid) of a column

- __iter__

 Enumerates all objects in this folder.


<!-- page: PyIShellFolder2__EnumSearches_meth.html -->

## PyIShellFolder2.EnumSearches

 PyIEnumExtraSearch = EnumSearches()

Returns an interface that lists searches defined for the folder

#### Comments

 IEnumExtraSearch is not yet wrapped by Pywin32


<!-- page: PyIShellFolder2__GetDefaultColumnState_meth.html -->

## PyIShellFolder2.GetDefaultColumnState

 int = GetDefaultColumnState(iColumn)

Returns flags indicating the default behaviour of the column

#### Parameters

- iColumn : int

 Zero-based index of the column

#### Return Value

Returns a combination of shellcon.SHCOLSTATE_* flags


<!-- page: PyIShellFolder2__GetDefaultColumn_meth.html -->

## PyIShellFolder2.GetDefaultColumn

 (int, int) = GetDefaultColumn()

Returns the columns used for sorting and display


<!-- page: PyIShellFolder2__GetDefaultSearchGUID_meth.html -->

## PyIShellFolder2.GetDefaultSearchGUID

 PyIID = GetDefaultSearchGUID(pguid)

Retrieves the default search for the folder

#### Parameters

- pguid : PyIID

 Description for pguid


<!-- page: PyIShellFolder2__GetDetailsEx_meth.html -->

## PyIShellFolder2.GetDetailsEx

 object = GetDetailsEx(pidl, pscid )

Returns the details of an item by Column ID

#### Parameters

- pidl : PyIDL

 Relative id list of an item in the folder

- pscid : SHCOLUMNID

 The Column id/property key of a column in the folder's Details view

#### Return Value

The type of returned object is determined by the variant type of the requested column


<!-- page: PyIShellFolder2__GetDetailsOf_meth.html -->

## PyIShellFolder2.GetDetailsOf

 (int, int, str) = GetDetailsOf(pidl, iColumn )

Returns the value or title of a column in the folder's Details view.

#### Parameters

- pidl : PyIDL

 The relative idl of an item in the folder. Use None to retrieve column title.

- iColumn : int

 Zero based index of column

#### Return Value

Returns a tuple representing a SHELLDETAILS struct, containing the formst (LVCFMT_*), column width in characters, and string representation of the requested value


<!-- page: PyIShellFolder2__MapColumnToSCID_meth.html -->

## PyIShellFolder2.MapColumnToSCID

 SHCOLUMNID = MapColumnToSCID(Column)

Returns the unique identifier (FMTID, pid) of a column

#### Parameters

- Column : int

 The zero-based index of the column as presented by the folder's Details view

#### Return Value

This is the Property Key used with the property system interfaces.


---

<!-- object: PyIShellIcon -->


<!-- page: PyIShellIcon.html -->

---

## PyIShellIcon Object

 Description of the interface

#### Methods

- GetIconOf

 Description of GetIconOf


<!-- page: PyIShellIcon__GetIconOf_meth.html -->

## PyIShellIcon.GetIconOf

 GetIconOf(pidl)

Description of GetIconOf.

#### Parameters

- pidl : PyIDL

 Description for pidl


---

<!-- object: PyIShellIconOverlay -->


<!-- page: PyIShellIconOverlay.html -->

---

## PyIShellIconOverlay Object

 Description of the interface

#### Methods

- GetOverlayIndex

 Description of GetOverlayIndex

- GetOverlayIconIndex

 Description of GetOverlayIconIndex


<!-- page: PyIShellIconOverlay__GetOverlayIconIndex_meth.html -->

## PyIShellIconOverlay.GetOverlayIconIndex

 GetOverlayIconIndex(pidl)

Description of GetOverlayIconIndex.

#### Parameters

- pidl : PyIDL

 Description for pidl


<!-- page: PyIShellIconOverlay__GetOverlayIndex_meth.html -->

## PyIShellIconOverlay.GetOverlayIndex

 GetOverlayIndex(pidl)

Description of GetOverlayIndex.

#### Parameters

- pidl : PyIDL

 Description for pidl


---

<!-- object: PyIShellIconOverlayIdentifier -->


<!-- page: PyIShellIconOverlayIdentifier.html -->

---

## PyIShellIconOverlayIdentifier Object

 Interface that supplies icon overlay information to the shell

#### Methods

- IsMemberOf

 Determines if a shell object should have an icon overlay

- GetOverlayInfo

 Retrieves the path to the overlay icon

- GetPriority

 Retrieves the relative priority of the overlay


<!-- page: PyIShellIconOverlayIdentifier__GetOverlayInfo_meth.html -->

## PyIShellIconOverlayIdentifier.GetOverlayInfo

 (PyUnicode , int, int) = GetOverlayInfo()

Retrieves the path to the overlay icon

#### Return Value

Returns the path to the icon file, the index of icon within the file, and Flags containing combination of shellcon.ISIOI_ICON* flags


<!-- page: PyIShellIconOverlayIdentifier__GetPriority_meth.html -->

## PyIShellIconOverlayIdentifier.GetPriority

 int = GetPriority()

Retrieves the relative priority of the overlay

#### Return Value

Implementation of this function should return a number in the range 0-100 (0 is highest priority)


<!-- page: PyIShellIconOverlayIdentifier__IsMemberOf_meth.html -->

## PyIShellIconOverlayIdentifier.IsMemberOf

 int = IsMemberOf(path, attrib )

Determines if a shell object should have an icon overlay

#### Parameters

- path : PyUnicode

 Fully qualified path of the shell object

- attrib : int

 Shell attributes, combination of shellcon.SFGAO_* flags

#### Return Value

The gateway implementation of this function should return winerror.S_OK to display the overlay, S_FALSE if not, or throw a COM exception with E_FAIL on error.
The client implementation of this function returns the same values - ie, Python's True and False should not be used, as S_OK==0==False.


---

<!-- object: PyIShellIconOverlayManager -->


<!-- page: PyIShellIconOverlayManager.html -->

---

## PyIShellIconOverlayManager Object

 Description of the interface

#### Methods

- GetFileOverlayInfo

 Description of GetFileOverlayInfo

- GetReservedOverlayInfo

 Description of GetReservedOverlayInfo

- RefreshOverlayImages

 Description of RefreshOverlayImages

- LoadNonloadedOverlayIdentifiers

 Description of LoadNonloadedOverlayIdentifiers

- OverlayIndexFromImageIndex

 Description of OverlayIndexFromImageIndex


<!-- page: PyIShellIconOverlayManager__GetFileOverlayInfo_meth.html -->

## PyIShellIconOverlayManager.GetFileOverlayInfo

 int = GetFileOverlayInfo(path, attrib , flags )

Returns an index into the system image list for the icon image or overlay image

#### Parameters

- path : str

 Full path to the file

- attrib : int

 File attributes (win32com.FILE_ATTRIBUTE_*)

- flags : int

 SIOM_OVERLAYINDEX (1) or SIOM_ICONINDEX (2)


<!-- page: PyIShellIconOverlayManager__GetReservedOverlayInfo_meth.html -->

## PyIShellIconOverlayManager.GetReservedOverlayInfo

 GetReservedOverlayInfo(path, attrib, flags, ireservedID)

Description of GetReservedOverlayInfo.

#### Parameters

- path : str

 Description for path

- attrib : int

 Description for attrib

- flags : int

 Description for flags

- ireservedID : int

 Description for ireservedID


<!-- page: PyIShellIconOverlayManager__LoadNonloadedOverlayIdentifiers_meth.html -->

## PyIShellIconOverlayManager.LoadNonloadedOverlayIdentifiers

 LoadNonloadedOverlayIdentifiers()

Description of LoadNonloadedOverlayIdentifiers.


<!-- page: PyIShellIconOverlayManager__OverlayIndexFromImageIndex_meth.html -->

## PyIShellIconOverlayManager.OverlayIndexFromImageIndex

 OverlayIndexFromImageIndex(iImage, fAdd)

Description of OverlayIndexFromImageIndex.

#### Parameters

- iImage : int

 Description for iImage

- fAdd : int

 Description for fAdd


<!-- page: PyIShellIconOverlayManager__RefreshOverlayImages_meth.html -->

## PyIShellIconOverlayManager.RefreshOverlayImages

 RefreshOverlayImages(flags)

Description of RefreshOverlayImages.

#### Parameters

- flags : int

 Description for flags


---

<!-- object: PyIShellItem -->


<!-- page: PyIShellItem.html -->

---

## PyIShellItem Object

 Interface that represents an item in the Explorer shell

#### Methods

- BindToHandler

 Creates an instance of one of the item's handlers

- GetParent

 Retrieves the parent of this item

- GetDisplayName

 Returns the display name of the item in the specified format

- GetAttributes

 Returns shell attributes of the item

- Compare

 Compares another shell item with this item


<!-- page: PyIShellItem__BindToHandler_meth.html -->

## PyIShellItem.BindToHandler

 interface = BindToHandler(pbc, bhid , riid )

Creates an instance of one of the item's handlers

#### Parameters

- pbc : PyIBindCtx

 Used to pass parameters that influence the binding operation, can be None

- bhid : PyIID

 GUID that identifies a handler (shell.BHID_*)

- riid : PyIID

 The interface to return


<!-- page: PyIShellItem__Compare_meth.html -->

## PyIShellItem.Compare

 int = Compare(psi, hint )

Compares another shell item with this item

#### Parameters

- psi : PyIShellItem

 A shell item to be compared with this item

- hint : int

 shellcon.SICHINT_* value indicating how the comparison is to be performed

#### Return Value

Returns 0 if items compare as equal, nonzero otherwise


<!-- page: PyIShellItem__GetAttributes_meth.html -->

## PyIShellItem.GetAttributes

 int = GetAttributes(Mask)

Returns shell attributes of the item

#### Parameters

- Mask : int

 Combination of shellcon.SFGAO_* values indicating the flags to return

#### Return Value

Returns a combination of shellcon.SFGAO_* values


<!-- page: PyIShellItem__GetDisplayName_meth.html -->

## PyIShellItem.GetDisplayName

 str = GetDisplayName(sigdnName)

Returns the display name of the item in the specified format

#### Parameters

- sigdnName : int

 Format of name to return, shellcon.SIGDN_*


<!-- page: PyIShellItem__GetParent_meth.html -->

## PyIShellItem.GetParent

 PyIShellItem = GetParent()

Retrieves the parent of this item


---

<!-- object: PyIShellItem2 -->


<!-- page: PyIShellItem2.html -->

---

## PyIShellItem2 Object

 Extends the IShellItem interface, giving access to an item's properties

#### Methods

- GetPropertyStore

 Returns a collection of the item's properties

- GetPropertyStoreForKeys

 Creates a property store containing just the specified properties of the item

- GetPropertyStoreWithCreateObject

 Returns the property store for the item, with alternate handler instantiation

- GetPropertyDescriptionList

 Retrieves descriptions of properties in a particular group

- Update

 Refreshes properties that have been modified since interface was created

- GetProperty

 DRetrieves the value of a property, converted to an appropriate python type

- GetCLSID

 Retrieves the value of a property as a GUID

- GetFileTime

 Retrieves the value of a property as a file time.

- GetInt32

 Retrieves the value of a property as a 32 bit int.

- GetString

 Retrieves the value of a property as a string

- GetUInt32

 Returns the value of a property as a 32 bit unsigned int

- GetUInt64

 Returns the value of a property as an unsigned 64-bit int

- GetBool

 Returns the value of a property as a boolean


<!-- page: PyIShellItem2__GetBool_meth.html -->

## PyIShellItem2.GetBool

 boolean = GetBool(key)

Returns the value of a property as a boolean

#### Parameters

- key : PyPROPERTYKEY

 The id of the property to retrieve


<!-- page: PyIShellItem2__GetCLSID_meth.html -->

## PyIShellItem2.GetCLSID

 PyIID = GetCLSID(key)

Retrieves the value of a property as a CLSID (VT_CLSID)

#### Parameters

- key : PyPROPERTYKEY

 The id of the property to retrieve


<!-- page: PyIShellItem2__GetFileTime_meth.html -->

## PyIShellItem2.GetFileTime

 PyDateTime = GetFileTime(key)

Retrieves the value of a property as a FILETIME

#### Parameters

- key : PyPROPERTYKEY

 The id of the property to retrieve


<!-- page: PyIShellItem2__GetInt32_meth.html -->

## PyIShellItem2.GetInt32

 int = GetInt32(key)

Retrieves the value of a property as a 32 bit int.

#### Parameters

- key : PyPROPERTYKEY

 The id of the property to retrieve


<!-- page: PyIShellItem2__GetPropertyDescriptionList_meth.html -->

## PyIShellItem2.GetPropertyDescriptionList

 PyIPropertyDescriptionList = GetPropertyDescriptionList(Type, riid )

Retrieves descriptions of properties in a particular group

#### Parameters

- Type : PyPROPERTYKEY

 Property list identifier (pscon.PKEY_PropList_*)

- riid=IID_IPropertyDescriptionList : PyIID

 The interface to return


<!-- page: PyIShellItem2__GetPropertyStoreForKeys_meth.html -->

## PyIShellItem2.GetPropertyStoreForKeys

 PyIPropertyStore = GetPropertyStoreForKeys(Keys, Flags , riid )

Creates a property store containing just the specified properties of the item

#### Parameters

- Keys : (SHCOLUMNID ,...))

 A sequence of property identifiers

- Flags=GPS_DEFAULT : int

 Combination of GETPROPERTYSTOREFLAGS values (shellcon.GPS_*)

- riid=IID_IPropertyStore : PyIID

 The interface to return


<!-- page: PyIShellItem2__GetPropertyStoreWithCreateObject_meth.html -->

## PyIShellItem2.GetPropertyStoreWithCreateObject

 PyIPropertyStore = GetPropertyStoreWithCreateObject(Flags, CreateObject , riid )

Returns the property store for the item, with alternate handler instantiation

#### Parameters

- Flags : int

 Combination of GETPROPERTYSTOREFLAGS values (shellcon.GPS_*)

- CreateObject : PyIUnknown

 An interface that implements ICreateObject, used to create the property handler

- riid=IID_IPropertyStore : PyIID

 The interface to be created

#### Comments

 Primarily used to create a handler in a separate process with reduced privileges


<!-- page: PyIShellItem2__GetPropertyStore_meth.html -->

## PyIShellItem2.GetPropertyStore

 PyIPropertyStore = GetPropertyStore(Flags, riid )

Returns a collection of the item's properties

#### Parameters

- Flags=GPS_DEFAULT : int

 Combination of GETPROPERTYSTOREFLAGS values (shellcon.GPS_*)

- riid=IID_IPropertyStore : PyIID

 The interface to return


<!-- page: PyIShellItem2__GetProperty_meth.html -->

## PyIShellItem2.GetProperty

 object = GetProperty(key)

Retrieves the value of a property, converted to an appropriate python type

#### Parameters

- key : PyPROPERTYKEY

 The id of the property to retrieve

#### Return Value

Type of returned object is determined by the variant type of the property


<!-- page: PyIShellItem2__GetString_meth.html -->

## PyIShellItem2.GetString

 str = GetString(key)

Retrieves the value of a property as a string

#### Parameters

- key : PyPROPERTYKEY

 The id of the property to retrieve


<!-- page: PyIShellItem2__GetUInt32_meth.html -->

## PyIShellItem2.GetUInt32

 int = GetUInt32(key)

Returns the value of a property as a 32 bit unsigned int

#### Parameters

- key : PyPROPERTYKEY

 The id of the property to retrieve


<!-- page: PyIShellItem2__GetUInt64_meth.html -->

## PyIShellItem2.GetUInt64

 int = GetUInt64(key)

Returns the value of a property as an unsigned 64-bit int

#### Parameters

- key : PyPROPERTYKEY

 The id of the property to retrieve


<!-- page: PyIShellItem2__Update_meth.html -->

## PyIShellItem2.Update

 Update(BindCtx)

Refreshes properties that have been modified since interface was created

#### Parameters

- BindCtx=None : PyIBindCxt

 Bind context used when requesting the interface, or None


---

<!-- object: PyIShellItemArray -->


<!-- page: PyIShellItemArray.html -->

---

## PyIShellItemArray Object

 Container for a number of shell items

#### Comments

 Can be used as an iterator to enumerate the contained items

#### Methods

- BindToHandler

 Creates an instance of a handler for the items in the container

- GetPropertyStore

 Retrieves a store containing consolidated properties of items in container

- GetPropertyDescriptionList

 Retrieves descriptions for a defined group of properties

- GetAttributes

 Retrieves shell attributes of contained items

- GetCount

 Returns the number of items in the container

- GetItemAt

 Retrieves an item by index

- EnumItems

 Returns an enumeration interface to list contained items


<!-- page: PyIShellItemArray__BindToHandler_meth.html -->

## PyIShellItemArray.BindToHandler

 interface = BindToHandler(pbc, rbhid , riid )

Creates an instance of a handler for the items in the container

#### Parameters

- pbc : PyIBindCtx

 Bind context, can be None

- rbhid : PyIID

 Bind handler GUID (shell.BHID_*)

- riid : PyIID

 The interface to return


<!-- page: PyIShellItemArray__EnumItems_meth.html -->

## PyIShellItemArray.EnumItems

 PyIEnumShellItems = EnumItems()

Returns an enumeration interface to list contained items


<!-- page: PyIShellItemArray__GetAttributes_meth.html -->

## PyIShellItemArray.GetAttributes

 int = GetAttributes(AttribFlags, Mask )

Retrieves shell attributes of contained items

#### Parameters

- AttribFlags : int

 SIATTRIBFLAGS value (shellcon.SIATTRIBFLAGS_*) specifying how to combine attributes of multiple items

- Mask : int

 Combination of SFGAOF flags (shellcon.SFGAO_*) specifying which attributes to return


<!-- page: PyIShellItemArray__GetCount_meth.html -->

## PyIShellItemArray.GetCount

 int = GetCount()

Returns the number of items in the container


<!-- page: PyIShellItemArray__GetItemAt_meth.html -->

## PyIShellItemArray.GetItemAt

 PyIShellItem = GetItemAt(dwIndex)

Retrieves an item by index

#### Parameters

- dwIndex : int

 Zero-based index of item to retrieve


<!-- page: PyIShellItemArray__GetPropertyDescriptionList_meth.html -->

## PyIShellItemArray.GetPropertyDescriptionList

 PyIPropertyDescriptionList = GetPropertyDescriptionList(Type, riid )

Retrieves descriptions for a defined group of properties

#### Parameters

- Type : PyPROPERTYKEY

 Property list identifier (pscon.PKEY_PropList_*)

- riid=IID_IPropertyDescriptionList : PyIID

 The interface to return


<!-- page: PyIShellItemArray__GetPropertyStore_meth.html -->

## PyIShellItemArray.GetPropertyStore

 PyIPropertyStore = GetPropertyStore(flags, riid )

Retrieves a store containing consolidated properties of items in container

#### Parameters

- flags=GPS_DEFAULT : int

 Flags indicating how the properties are retrieved (shellcon.GPS_*)

- riid=IID__IPropertyStore : PyIID

 The interface to return, IID_IPropertyStore or related interface


---

<!-- object: PyIShellItemResources -->


<!-- page: PyIShellItemResources.html -->

---

## PyIShellItemResources Object

 Description of the interface

#### Methods

- GetAttributes

 Description of GetAttributes

- GetSize

 Description of GetSize

- GetTimes

 Description of GetTimes

- SetTimes

 Description of SetTimes

- GetResourceDescription

 Description of GetResourceDescription

- EnumResources

 Description of EnumResources

- SupportsResource

 Description of SupportsResource

- OpenResource

 Description of OpenResource

- CreateResource

 Description of CreateResource

- MarkForDelete

 Description of MarkForDelete


<!-- page: PyIShellItemResources__CreateResource_meth.html -->

## PyIShellItemResources.CreateResource

 interface = CreateResource(sir, riid )

Description of CreateResource.

#### Parameters

- sir : PySHELL_ITEM_RESOURCE

 Resource identifier

- riid : PyIID

 The interface to return


<!-- page: PyIShellItemResources__EnumResources_meth.html -->

## PyIShellItemResources.EnumResources

 PyIEnumResources = EnumResources()

Description of EnumResources.


<!-- page: PyIShellItemResources__GetAttributes_meth.html -->

## PyIShellItemResources.GetAttributes

 GetAttributes()

Description of GetAttributes.


<!-- page: PyIShellItemResources__GetResourceDescription_meth.html -->

## PyIShellItemResources.GetResourceDescription

 GetResourceDescription(pcsir)

Description of GetResourceDescription.

#### Parameters

- pcsir : PySHELL_ITEM_RESOURCE

 Description for pcsir


<!-- page: PyIShellItemResources__GetSize_meth.html -->

## PyIShellItemResources.GetSize

 int = GetSize()

Description of GetSize.


<!-- page: PyIShellItemResources__GetTimes_meth.html -->

## PyIShellItemResources.GetTimes

 GetTimes()

Description of GetTimes.


<!-- page: PyIShellItemResources__MarkForDelete_meth.html -->

## PyIShellItemResources.MarkForDelete

 MarkForDelete()

Description of MarkForDelete.


<!-- page: PyIShellItemResources__OpenResource_meth.html -->

## PyIShellItemResources.OpenResource

 PyIUnknown = OpenResource(pcsir, riid )

Description of OpenResource.

#### Parameters

- pcsir : PySHELL_ITEM_RESOURCE

 Description for pcsir

- riid : PyIID

 The interface to return


<!-- page: PyIShellItemResources__SetTimes_meth.html -->

## PyIShellItemResources.SetTimes

 SetTimes(pftCreation, pftWrite, pftAccess)

Description of SetTimes.

#### Parameters

- pftCreation : PyDateTime

 Description for pftCreation

- pftWrite : PyDateTime

 Description for pftWrite

- pftAccess : PyDateTime

 Description for pftAccess


<!-- page: PyIShellItemResources__SupportsResource_meth.html -->

## PyIShellItemResources.SupportsResource

 boolean = SupportsResource(pcsir)

Description of SupportsResource.

#### Parameters

- pcsir : PySHELL_ITEM_RESOURCE

 Description for pcsir


---

<!-- object: PyIShellLibrary -->


<!-- page: PyIShellLibrary.html -->

---

## PyIShellLibrary Object

 Interface used to access Libraries

#### Methods

- LoadLibraryFromItem

 Loads an existing library file

- LoadLibraryFromKnownFolder

 Initializes library from a known folder

- AddFolder

 Includes a folder in the library

- RemoveFolder

 Removes a folder

- GetFolders

 Retrieves a collection of folders in the library

- ResolveFolder

 Attempts to locate a folder that has been moved or renamed

- GetDefaultSaveFolder

 Returns the default folder in which new items are saved

- SetDefaultSaveFolder

 Sets the default save location

- GetOptions

 Retrieves library option flags

- SetOptions

 Sets library option flags

- GetFolderType

 Retrieves the folder type of the library

- SetFolderType

 Sets the folder type of the library

- GetIcon

 Returns the location of the library's icon

- SetIcon

 Sets the library icon

- Commit

 Saves changes (only if loaded from an existing library)

- Save

 Saves the library to a specific location

- SaveInKnownFolder

 Saves the library in a known folder


<!-- page: PyIShellLibrary__AddFolder_meth.html -->

## PyIShellLibrary.AddFolder

 AddFolder(Location)

Includes a folder

#### Parameters

- Location : PyIShellItem

 Shell item interface representing the folder


<!-- page: PyIShellLibrary__Commit_meth.html -->

## PyIShellLibrary.Commit

 Commit()

Saves changes (only if loaded from an existing library)


<!-- page: PyIShellLibrary__GetDefaultSaveFolder_meth.html -->

## PyIShellLibrary.GetDefaultSaveFolder

 PyIShellItem = GetDefaultSaveFolder(Type, riid )

Returns the default folder in which new items are saved

#### Parameters

- Type=DSFT_DETECT : int

 Specifies whether to return public or private save location, shellcon.DSFT_*

- riid=IID_IShellItem : PyIID

 The interface to return


<!-- page: PyIShellLibrary__GetFolderType_meth.html -->

## PyIShellLibrary.GetFolderType

 PyIID = GetFolderType()

Returns the library type, shell.FOLDERTYPEID_*


<!-- page: PyIShellLibrary__GetFolders_meth.html -->

## PyIShellLibrary.GetFolders

 PyIShellItemArray = GetFolders(Filter, riid )

Retrieves a collection of folders in the library

#### Parameters

- Filter=LFF_ALLITEMS : int

 Specifies what types of folder to return (shellcon.LFF_*)

- riid=IID_IShellItemArray : PyIID

 The interface to return, IObjectCollection and IObjectArray also accepted.


<!-- page: PyIShellLibrary__GetIcon_meth.html -->

## PyIShellLibrary.GetIcon

 str = GetIcon()

Returns the location of the library's icon

#### Return Value

Uses "module,resource" format


<!-- page: PyIShellLibrary__GetOptions_meth.html -->

## PyIShellLibrary.GetOptions

 int = GetOptions()

Retrieves library option flags

#### Return Value

Returns a combination of shellcon.LOF_* flags


<!-- page: PyIShellLibrary__LoadLibraryFromItem_meth.html -->

## PyIShellLibrary.LoadLibraryFromItem

 LoadLibraryFromItem(Library, Mode)

Loads an existing library file

#### Parameters

- Library : PyIShellItem

 Shell item interface representing the library file

- Mode : int

 Access mode, combination of storagecon.STGM_* flags


<!-- page: PyIShellLibrary__LoadLibraryFromKnownFolder_meth.html -->

## PyIShellLibrary.LoadLibraryFromKnownFolder

 LoadLibraryFromKnownFolder(Library, Mode)

Initializes library from a known folder

#### Parameters

- Library : PyIID

 Known folder id, shell.FOLDERID_*

- Mode : int

 Access mode, combination of storagecon.STGM_* flags


<!-- page: PyIShellLibrary__RemoveFolder_meth.html -->

## PyIShellLibrary.RemoveFolder

 RemoveFolder(Location)

Removes a folder

#### Parameters

- Location : PyIShellItem

 Shell item interface representing the folder


<!-- page: PyIShellLibrary__ResolveFolder_meth.html -->

## PyIShellLibrary.ResolveFolder

 PyIShellItem = ResolveFolder(FolderToResolve, Timeout , riid )

Attempts to locate a folder that has been moved or renamed

#### Parameters

- FolderToResolve : PyIShellItem

 Library item whose location has changed

- Timeout : int

 Max search time, specified in milliseconds

- riid=IID_IShellItem : PyIID

 The interface to return


<!-- page: PyIShellLibrary__SaveInKnownFolder_meth.html -->

## PyIShellLibrary.SaveInKnownFolder

 PyIShellItem = SaveInKnownFolder(FolderToSaveIn, LibraryName , Flags )

Saves the library in a known folder

#### Parameters

- FolderToSaveIn : PyIID

 The destination folder, shell.FOLDERID_*

- LibraryName : str

 Filename for the new library, without file extension

- Flags : int

 Determines behaviour if file already exists, shellcon.LSF_*


<!-- page: PyIShellLibrary__Save_meth.html -->

## PyIShellLibrary.Save

 PyIShellItem = Save(FolderToSaveIn, LibraryName , Flags )

Saves the library to a specific location

#### Parameters

- FolderToSaveIn : PyIShellItem

 The destination folder, use None to save in current user's Libraries folder

- LibraryName : str

 Filename for the new library, without file extension

- Flags : int

 Determines behaviour if file already exists, shellcon.LSF_*

#### Return Value

Returns a shell item for the saved file.


<!-- page: PyIShellLibrary__SetDefaultSaveFolder_meth.html -->

## PyIShellLibrary.SetDefaultSaveFolder

 SetDefaultSaveFolder(Type, SaveFolder)

Sets the default save location

#### Parameters

- Type : int

 Specifies public or private save location, shellcon.DSFT_*

- SaveFolder : PyIShellItem

 New default location, must be in the library


<!-- page: PyIShellLibrary__SetFolderType_meth.html -->

## PyIShellLibrary.SetFolderType

 SetFolderType(Type)

Sets the folder type for the library

#### Parameters

- Type : PyIID

 New type, shell.FOLDERTYPEID_*


<!-- page: PyIShellLibrary__SetIcon_meth.html -->

## PyIShellLibrary.SetIcon

 SetIcon(Icon)

Sets the library icon

#### Parameters

- Icon : str

 Icon location in "module,resource" syntax


<!-- page: PyIShellLibrary__SetOptions_meth.html -->

## PyIShellLibrary.SetOptions

 SetOptions(Mask, Options)

Sets library option flags

#### Parameters

- Mask : int

 Bitmask of flags to be changed, combination of shellcon.LOF_* values

- Options : int

 New options, combination of shellcon.LOF_* values


---

<!-- object: PyIShellLink -->


<!-- page: PyIShellLink.html -->

---

## PyIShellLink Object

 Interface used to access the properties of a shell link file (*.lnk)

#### Methods

- GetPath

 Retrieves the path and file name of a shell link object.

- GetIDList

 Retrieves the item id list that identifies the target of the shell link.

- SetIDList

 Sets the target of the link using an item id list

- GetDescription

 Retrieves the description of the link (displays as Comment in the UI)

- SetDescription

 Sets the description of the link (displays as Comment in the UI)

- GetWorkingDirectory

 Retrieves the working directory for the link

- SetWorkingDirectory

 Sets the working directory for the link

- GetArguments

 Retrieves the command-line arguments associated with a shell link object.

- SetArguments

 Sets the command-line arguments associated with a shell link object.

- GetHotkey

 Retrieves the hot key for a shell link object.

- SetHotkey

 Sets the hot key for a shell link object.

- GetShowCmd

 Retrieves the show (SW_) command for a shell link object.

- SetShowCmd

 Sets the show (SW_) command for a shell link object.

- GetIconLocation

 Retrieves the location (path and index) of the icon for a shell link object.

- SetIconLocation

 Sets the location (path and index) of the icon for a shell link object.

- SetRelativePath

 Sets the relative path for a shell link object.

- Resolve

 Resolves a shell link

- SetPath

 Sets the path and file name of a shell link object.


<!-- page: PyIShellLink__GetArguments_meth.html -->

## PyIShellLink.GetArguments

 str = GetArguments(cchMaxName)

Retrieves the command-line arguments associated with a shell link object.

#### Parameters

- cchMaxName=1024 : int

 Number of characters to fetch.


<!-- page: PyIShellLink__GetDescription_meth.html -->

## PyIShellLink.GetDescription

 str = GetDescription(cchMaxName)

Retrieves the description of the link (displays as Comment in the UI)

#### Parameters

- cchMaxName=1024 : int

 Number of character to allocate for the retrieved text


<!-- page: PyIShellLink__GetHotkey_meth.html -->

## PyIShellLink.GetHotkey

 int = GetHotkey()

Retrieves the hot key for a shell link object.

#### Comments

 Note: My tests do not seem to be working. at least, the values returned seem not to match what the documentation says should be returned. I would expect with a Hotkey of CTRL-ALT-T, to get an integer where integer & 256 == ord('T'), i.e. 116 or 84, instead I get 1620


<!-- page: PyIShellLink__GetIDList_meth.html -->

## PyIShellLink.GetIDList

 PyIDL = GetIDList()

Retrieves the item id list that identifies the target of the shell link.


<!-- page: PyIShellLink__GetIconLocation_meth.html -->

## PyIShellLink.GetIconLocation

 str = GetIconLocation(cchMaxPath)

Retrieves the location (path and index) of the icon for a shell link object.

#### Parameters

- cchMaxPath=_MAX_PATH : int

 Number of characters to allocate for the result string.


<!-- page: PyIShellLink__GetPath_meth.html -->

## PyIShellLink.GetPath

 str, WIN32_FIND_DATA = GetPath(fFlags, cchMaxPath )

Retrieves the target path and file name of a shell link object

#### Parameters

- fFlags : int

 One of the following values:

| | Value | Description
| |

---

 |

---

| | SLGP_SHORTPATH | Retrieves the standard short (8.3 format) file name.
| | SLGP_UNCPRIORITY | Retrieves the Universal Naming Convention (UNC) path name of the file.
| | SLGP_RAWPATH | Retrieves the raw path name. A raw path is something that might not exist and may include environment variables that need to be expanded.
- cchMaxPath=_MAX_PATH : int

 Number of characters to allocate for returned filename

#### Comments

 The AlternateFileName (8.3) member of WIN32_FIND_DATA does not return information


<!-- page: PyIShellLink__GetShowCmd_meth.html -->

## PyIShellLink.GetShowCmd

 int = GetShowCmd()

Retrieves the show (SW_) command for a shell link object.


<!-- page: PyIShellLink__GetWorkingDirectory_meth.html -->

## PyIShellLink.GetWorkingDirectory

 str = GetWorkingDirectory(cchMaxName)

Retrieves the working directory for the link

#### Parameters

- cchMaxName=1024 : int

 Number of characters to allocate for returned text


<!-- page: PyIShellLink__Resolve_meth.html -->

## PyIShellLink.Resolve

 Resolve(hwnd, fFlags)

Resolves a shell link by searching for the shell link object and updating the shell link path and its list of identifiers (if necessary)

#### Parameters

- hwnd : HWND

 The parent window of a dialog which will pop up if resolution fails.

- fFlags : int

 One of the following constants:

| | Value | Description
| |

---

 |

---

| | SLR_INVOKE_MSI | Call the Microsoft Windows Installer.
| | SLR_NOLINKINFO | Disable distributed link tracking. By default, distributed link tracking tracks removable media across multiple devices based on the volume name. It also uses the UNC path to track remote file systems whose drive letter has changed. Setting SLR_NOLINKINFO disables both types of tracking.
| | SLR_NO_UI | Do not display a dialog box if the link cannot be resolved. When SLR_NO_UI is set, the high-order word of fFlags can be set to a time-out value that specifies the maximum amount of time to be spent resolving the link. The function returns if the link cannot be resolved within the time-out duration. If the high-order word is set to zero, the time-out duration will be set to the default value of 3,000 milliseconds (3 seconds). To specify a value, set the high word of fFlags to the desired time-out duration, in milliseconds.
| | SLR_NOUPDATE | Do not update the link information.
| | SLR_NOSEARCH | Do not execute the search heuristics.
| | SLR_NOTRACK | Do not use distributed link tracking.
| | SLR_UPDATE | If the link object has changed, update its path and list of identifiers. If SLR_UPDATE is set, you do not need to call IPersistFile::IsDirty to determine whether or not the link object has changed.


<!-- page: PyIShellLink__SetArguments_meth.html -->

## PyIShellLink.SetArguments

 SetArguments(args)

Sets the command-line arguments associated with a shell link object.

#### Parameters

- args : str

 The new arguments.


<!-- page: PyIShellLink__SetDescription_meth.html -->

## PyIShellLink.SetDescription

 SetDescription(Name)

Sets the description of the link (displays as Comment in the UI)

#### Parameters

- Name : str

 The description for the link


<!-- page: PyIShellLink__SetHotkey_meth.html -->

## PyIShellLink.SetHotkey

 SetHotkey(wHotkey)

Sets the hot key for a shell link object.

#### Parameters

- wHotkey : int

 The virtual key code is in the low-order byte, and the modifier flags are in the high-order byte. The modifier flags can be a combination of the values specified in the description of the PyIShellLink::GetHotkey method.


<!-- page: PyIShellLink__SetIDList_meth.html -->

## PyIShellLink.SetIDList

 SetIDList(pidl)

Sets the target of the link using an item id list

#### Parameters

- pidl : PyIDL

 Absolute item id list that identifies the target


<!-- page: PyIShellLink__SetIconLocation_meth.html -->

## PyIShellLink.SetIconLocation

 SetIconLocation(iconPath, iIcon)

Sets the location (path and index) of the icon for a shell link object.

#### Parameters

- iconPath : string

 Path to the file with the icon.

- iIcon : int

 Index of the icon.


<!-- page: PyIShellLink__SetPath_meth.html -->

## PyIShellLink.SetPath

 SetPath(path)

Sets the path and file name of a shell link object.

#### Parameters

- path : string

 The path and filename of the link.


<!-- page: PyIShellLink__SetRelativePath_meth.html -->

## PyIShellLink.SetRelativePath

 SetRelativePath(relPath, reserved)

Sets the relative path for a shell link object.

#### Parameters

- relPath : string

 The relative path.

- reserved=0 : int

 Reserved - must be zero.

#### Comments

 This mechanism allows for moved link files to reestablish connection with relative files through similar-prefix comparisons


<!-- page: PyIShellLink__SetShowCmd_meth.html -->

## PyIShellLink.SetShowCmd

 SetShowCmd(iShowCmd)

Sets the show (SW_) command for a shell link object.

#### Parameters

- iShowCmd : int

 The new show command value.


<!-- page: PyIShellLink__SetWorkingDirectory_meth.html -->

## PyIShellLink.SetWorkingDirectory

 SetWorkingDirectory(Dir)

Sets the working directory for the link.

#### Parameters

- Dir : str

 The working directory for the link


---

<!-- object: PyIShellLinkDataList -->


<!-- page: PyIShellLinkDataList.html -->

---

## PyIShellLinkDataList Object

 Interface to a link's extra data blocks. Can be obtained from PyIShellLink by calling QueryInterface with IID_IShellLinkDataList

#### Methods

- AddDataBlock

 Inserts a data block into the link

- CopyDataBlock

 Retrieves the specified data block from the link

- GetFlags

 Retrieves the link's flags

- RemoveDataBlock

 Deletes one of the link's data blocks

- SetFlags

 Sets the flags indicating which data blocks are present


<!-- page: PyIShellLinkDataList__AddDataBlock_meth.html -->

## PyIShellLinkDataList.AddDataBlock

 AddDataBlock(DataBlock)

Inserts a data block into the link

#### Parameters

- DataBlock : dict

 Contents are dependent on type of data block being added

#### Comments

 Input should be one of NT_CONSOLE_PROPS, NT_FE_CONSOLE_PROPS, EXP_SPECIAL_FOLDER, EXP_DARWIN_LINK, or EXP_SZ_LINK. Expected form is indicated by the Signature member.


<!-- page: PyIShellLinkDataList__CopyDataBlock_meth.html -->

## PyIShellLinkDataList.CopyDataBlock

 dict = CopyDataBlock(Sig)

Retrieves the specified data block from the link

#### Parameters

- Sig : int

 The type of data block to retrieve, one of the shellcon.*_SIG constants

#### Return Value

The returned dictionary will contain different information depending on the value passed in


<!-- page: PyIShellLinkDataList__GetFlags_meth.html -->

## PyIShellLinkDataList.GetFlags

 int = GetFlags()

Retrieves the link's flags

#### Return Value

Returns combination of shellcon.SLDF_* flags


<!-- page: PyIShellLinkDataList__RemoveDataBlock_meth.html -->

## PyIShellLinkDataList.RemoveDataBlock

 RemoveDataBlock(Sig)

Deletes one of the link's data blocks

#### Parameters

- Sig : int

 Identifies which block is to be removed, one of shellcon.*_SIG constants


<!-- page: PyIShellLinkDataList__SetFlags_meth.html -->

## PyIShellLinkDataList.SetFlags

 SetFlags(Flags)

Sets the flags indicating which data blocks are present

#### Parameters

- Flags : int

 Combination of shellcon.SLDF_* flags


---

<!-- object: PyIShellView -->


<!-- page: PyIShellView.html -->

---

## PyIShellView Object

 Description of the interface

#### Methods

- TranslateAccelerator

 Description of TranslateAccelerator

- EnableModeless

 Description of EnableModeless

- UIActivate

 Description of UIActivate

- Refresh

 Description of Refresh

- CreateViewWindow

 Description of CreateViewWindow

- DestroyViewWindow

 Description of DestroyViewWindow

- GetCurrentInfo

 Description of GetCurrentInfo

- SaveViewState

 Description of SaveViewState

- SelectItem

 Description of SelectItem

- GetItemObject

 Description of GetItemObject


<!-- page: PyIShellView__CreateViewWindow_meth.html -->

## PyIShellView.CreateViewWindow

 int = CreateViewWindow(psvPrevious, pfs , psb , prcView )

Description of CreateViewWindow.

#### Parameters

- psvPrevious : PyIShellView

 Description for psvPrevious

- pfs : (int, int)

 Description for pfs

- psb : PyIShellBrowser

 Description for psb

- prcView : (int, int, int, int)

 Description for prcView

#### Return Value

The result is an integer handle to the new window.


<!-- page: PyIShellView__DestroyViewWindow_meth.html -->

## PyIShellView.DestroyViewWindow

 DestroyViewWindow()

Description of DestroyViewWindow.


<!-- page: PyIShellView__EnableModeless_meth.html -->

## PyIShellView.EnableModeless

 EnableModeless(fEnable)

Description of EnableModeless.

#### Parameters

- fEnable : int

 Description for fEnable


<!-- page: PyIShellView__GetCurrentInfo_meth.html -->

## PyIShellView.GetCurrentInfo

 PyFOLDERSETTINGS = GetCurrentInfo()

Description of GetCurrentInfo.


<!-- page: PyIShellView__GetItemObject_meth.html -->

## PyIShellView.GetItemObject

 PyIUnknown = GetItemObject(uItem, riid )

Description of GetItemObject.

#### Parameters

- uItem : int

 Description for uItem

- riid : PyIID

 Description for riid


<!-- page: PyIShellView__Refresh_meth.html -->

## PyIShellView.Refresh

 Refresh()

Description of Refresh.


<!-- page: PyIShellView__SaveViewState_meth.html -->

## PyIShellView.SaveViewState

 SaveViewState()

Description of SaveViewState.


<!-- page: PyIShellView__SelectItem_meth.html -->

## PyIShellView.SelectItem

 SelectItem(pidlItem, uFlags)

Description of SelectItem.

#### Parameters

- pidlItem : PyIDL

 Description for pidlItem

- uFlags : int

 Description for uFlags


<!-- page: PyIShellView__TranslateAccelerator_meth.html -->

## PyIShellView.TranslateAccelerator

 int = TranslateAccelerator(pmsg)

Description of TranslateAccelerator.

#### Parameters

- pmsg : tuple

 Description for pmsg

#### Return Value

The result is the HRESULT from the underlying TranslateAccelerator call


<!-- page: PyIShellView__UIActivate_meth.html -->

## PyIShellView.UIActivate

 UIActivate(uState)

Description of UIActivate.

#### Parameters

- uState : int

 Description for uState


---

<!-- object: PyISpecifyPropertyPages -->


<!-- page: PyISpecifyPropertyPages.html -->

---

## PyISpecifyPropertyPages Object

 Description of the interface

#### Methods

- GetPages

 Description of GetPages


<!-- page: PyISpecifyPropertyPages__GetPages_meth.html -->

## PyISpecifyPropertyPages.GetPages

 GetPages()

Description of GetPages.


---

<!-- object: PyIStorage -->


<!-- page: PyIStorage.html -->

---

## PyIStorage Object

 Structured storage compound storage object

#### Comments

 This object acts as an iterator through PyIStorage::EnumElements

#### Methods

- CreateStream

 Creates and opens a stream object with the specified name contained in this storage object.

- OpenStream

 Opens an existing stream object.

- CreateStorage

 Creates and opens a new storage object nested within this storage object.

- OpenStorage

 Opens an existing storage object with the specified name in the specified access mode.

- CopyTo

 Copies the entire contents of an open storage object to another storage object.

- MoveElementTo

 Copies or moves a substorage or stream from this storage object to another storage object.

- Commit

 Ensures that any changes made to a storage object open in transacted mode are reflected in the parent storage.

- Revert

 Discards all changes that have been made to the storage object since the last commit.

- EnumElements

 Retrieves an enumerator object that can be used to enumerate the storage and stream objects contained within this storage object.

- DestroyElement

 Removes the specified storage or stream from this storage object.

- RenameElement

 Renames the specified substorage or stream in this storage object.

- SetElementTimes

 Sets the modification, access, and creation times of the specified storage element, if supported by the underlying file system.

- SetClass

 Assigns the specified CLSID to this storage object.

- SetStateBits

 Stores up to 32 bits of state information in this storage object.

- Stat

 Retrieves the STATSTG structure for this open storage object.

#### Based On

PyIUnknown


<!-- page: PyIStorage__Commit_meth.html -->

## PyIStorage.Commit

 Commit(grfCommitFlags)

Ensures that any changes made to a storage object open in transacted mode are reflected in the parent storage; for a root storage, reflects the changes in the actual device, for example, a file on disk. For a root storage object opened in direct mode, this method has no effect except to flush all memory buffers to the disk. For non-root storage objects in direct mode, this method has no effect.

#### Parameters

- grfCommitFlags : int

 Controls how the changes are committed to the storage object. See the STGC enumeration for a definition of these values.


<!-- page: PyIStorage__CopyTo_meth.html -->

## PyIStorage.CopyTo

 CopyTo(rgiidExclude, snbExclude, stgDest)

Copies the entire contents of an open storage object to another storage object.

#### Parameters

- rgiidExclude : [PyIID,]

 List of IID's to be excluded. Use empty seq to exclude all objects, or None to indicate no excludes.

- snbExclude : SNB

 Reserved for later - Must be None

- stgDest : PyIStorage

 The open storage object into which this storage object is to be copied. The destination storage object can be a different implementation of the PyIStorage interface from the source storage object. Thus, IStorage::CopyTo can only use publicly available methods of the destination storage object. If stgDest is open in transacted mode, it can be reverted by calling its PyIStorage::Revert method.


<!-- page: PyIStorage__CreateStorage_meth.html -->

## PyIStorage.CreateStorage

 PyIStorage = CreateStorage(Name, Mode , StgFmt , reserved2 )

Creates and opens a new storage object nested within this storage object.

#### Parameters

- Name : str

 The name of the newly created stream.

- Mode : int

 Access mode - combination of storagecon.STGM_* flags

- StgFmt : int

 Documented as "reserved"!

- reserved2=0 : int

 Description for reserved2


<!-- page: PyIStorage__CreateStream_meth.html -->

## PyIStorage.CreateStream

 PyIStream = CreateStream(Name, Mode , reserved1 , reserved2 )

Creates and opens a stream object with the specified name contained in this storage object. All elements within a storage object, both streams and other storage objects, are kept in the same name space.

#### Parameters

- Name : str

 Name of the new stream

- Mode : int

 Access mode, storagecon.STGM_*

- reserved1=0 : int

 Reserved - must be zero.

- reserved2=0 : int

 Reserved - must be zero.


<!-- page: PyIStorage__DestroyElement_meth.html -->

## PyIStorage.DestroyElement

 DestroyElement(name)

Removes the specified storage or stream from this storage object.

#### Parameters

- name : string

 The name of the element to be removed.


<!-- page: PyIStorage__EnumElements_meth.html -->

## PyIStorage.EnumElements

 PyIEnumSTATSTG = EnumElements(reserved1, reserved2 , reserved3 )

Retrieves an enumerator object that can be used to enumerate the storage and stream objects contained within this storage object.

#### Parameters

- reserved1=0 : int

 Reserved - must be zero.

- reserved2=None : object

 A reserved param. Always pass None. NULL is always passed to the COM function

- reserved3=0 : int

 Reserved - must be zero.


<!-- page: PyIStorage__MoveElementTo_meth.html -->

## PyIStorage.MoveElementTo

 MoveElementTo(Name, stgDest, NewName, Flags)

Copies or moves a substorage or stream from this storage object to another storage object.

#### Parameters

- Name : str

 A string that contains the name of the element in this storage object to be moved or copied.

- stgDest : PyIStorage

 PyIStorage for the destination storage object.

- NewName : str

 A string that contains the new name for the element in its new storage object.

- Flags : int

 Specifies whether to move or copy (storagecon.STGMOVE_MOVE or STGMOVE_COPY)


<!-- page: PyIStorage__OpenStorage_meth.html -->

## PyIStorage.OpenStorage

 PyIStorage = OpenStorage(Name, Priority , Mode , snbExclude , reserved )

Opens an existing storage object with the specified name in the specified access mode.

#### Parameters

- Name : str

 Name of the storage, or None.

- Priority : PyIStorage

 If the pstgPriority parameter is not None, it is a PyIStorage object to a previous opening of an element of the storage object, usually one that was opened in priority mode. The storage object should be closed and re-opened according to grfMode. When the PyIStorage::OpenStorage method returns, pstgPriority is no longer valid - use the result value. If the pstgPriority parameter is None, it is ignored.

- Mode : int

 Access mode - combination of storagecon.STGM_* flags (must include STGM_SHARE_EXCLUSIVE)

- snbExclude : SNB

 Reserved for later - Must be None

- reserved=0 : int

 Reserved integer param.


<!-- page: PyIStorage__OpenStream_meth.html -->

## PyIStorage.OpenStream

 PyIStream = OpenStream(Name, reserved1 , Mode , reserved2 )

Opens an existing stream object within this storage object in the specified access mode.

#### Parameters

- Name : str

 Name of stream to be opened

- reserved1 : object

 A reserved param. Always pass None. NULL is always passed to the COM function

- Mode : int

 Access mode, storagecon.STGM_*

- reserved2=0 : int

 Reserved - must be zero.


<!-- page: PyIStorage__RenameElement_meth.html -->

## PyIStorage.RenameElement

 RenameElement(OldName, NewName)

Renames the specified substorage or stream in this storage object.

#### Parameters

- OldName : str

 The name of the substorage or stream to be changed.

- NewName : str

 The new name for the specified sustorage or stream.


<!-- page: PyIStorage__Revert_meth.html -->

## PyIStorage.Revert

 Revert()

Discards all changes that have been made to the storage object since the last commit.


<!-- page: PyIStorage__SetClass_meth.html -->

## PyIStorage.SetClass

 SetClass(clsid)

Assigns the specified CLSID to this storage object.

#### Parameters

- clsid : PyIID

 The class identifier (CLSID) that is to be associated with the storage object.


<!-- page: PyIStorage__SetElementTimes_meth.html -->

## PyIStorage.SetElementTimes

 SetElementTimes(name, ctime, atime, mtime)

Sets the modification, access, and creation times of the specified storage element, if supported by the underlying file system.

#### Parameters

- name : str

 The name of the storage object element whose times are to be modified. If NULL, the time is set on the root storage rather than one of its elements.

- ctime : PyDateTime

 Either the new creation time for the element or None if the creation time is not to be modified.

- atime : PyDateTime

 Either the new access time for the element or None if the access time is not to be modified.

- mtime : PyDateTime

 Either the new modification time for the element or None if the modification time is not to be modified.


<!-- page: PyIStorage__SetStateBits_meth.html -->

## PyIStorage.SetStateBits

 SetStateBits(grfStateBits, grfMask)

Stores up to 32 bits of state information in this storage object.

#### Parameters

- grfStateBits : int

 Specifies the new values of the bits to set. No legal values are defined for these bits; they are all reserved for future use and must not be used by applications.

- grfMask : int

 A binary mask indicating which bits in grfStateBits are significant in this call.


<!-- page: PyIStorage__Stat_meth.html -->

## PyIStorage.Stat

 STATSTG = Stat(grfStatFlag)

Retrieves the STATSTG structure for this open storage object.

#### Parameters

- grfStatFlag : int

 Specifies that some of the fields in the STATSTG structure are not returned, thus saving a memory allocation operation. Values are taken from the STATFLAG enumeration.


---

<!-- object: PyIStream -->


<!-- page: PyIStream.html -->

---

## PyIStream Object

 A Python interface to IStream

#### Methods

- Read

 Read the specified number of bytes from the string.

- read

 Alias for PyIStream::Read

- Write

 Write data from a stream.

- write

 Alias for PyIStream::Write

- Seek

 Changes the seek pointer to a new location.

- SetSize

 Changes the size of the stream object.

- CopyTo

 Copies a specified number of bytes from the current seek pointer in the stream to the current seek pointer in another stream.

- Commit

 Ensures that any changes made to a stream object open in transacted mode are reflected in the parent storage.

- Revert

 Discards all changes that have been made to a transacted stream since the last PyIStream::Commit call.

- LockRegion

 Restricts access to a specified range of bytes in the stream.

- UnLockRegion

 Removes the access restriction on a range of bytes previously restricted with PyIStream::LockRegion.

- Clone

 Creates a new stream object with its own seek pointer that references the same bytes as the original stream.

- Stat

 Returns information about a stream

#### Based On

PyIUnknown


<!-- page: PyIStream__Clone_meth.html -->

## PyIStream.Clone

 PyIStream = Clone()

Creates a new stream object with its own seek pointer that references the same bytes as the original stream.


<!-- page: PyIStream__Commit_meth.html -->

## PyIStream.Commit

 Commit(flags)

Ensures that any changes made to a stream object open in transacted mode are reflected in the parent storage.

#### Parameters

- flags=STGC_DEFAULT : int

 Controls how changes are performed.


<!-- page: PyIStream__CopyTo_meth.html -->

## PyIStream.CopyTo

 ULARGE_INTEGER = CopyTo(stream, cb )

Copies a specified number of bytes from the current seek pointer in the stream to the current seek pointer in another stream.

#### Parameters

- stream : PyIStream

 The stream to write to.

- cb : ULARGE_INTEGER

 The number of bytes to write.

#### Return Value

The return value is the number of bytes actually written.


<!-- page: PyIStream__LockRegion_meth.html -->

## PyIStream.LockRegion

 LockRegion(offset, cb, lockType)

Restricts access to a specified range of bytes in the stream.

#### Parameters

- offset : ULARGE_INTEGER

 Integer that specifies the byte offset for the beginning of the range.

- cb : ULARGE_INTEGER

 The number of bytes to restrict.

- lockType : int

 Restrictions requested.


<!-- page: PyIStream__Read_meth.html -->

## PyIStream.Read

 string = Read(numBytes)

Read the specified number of bytes from the string.

#### Parameters

- numBytes : int

 The number of bytes to read from the stream. Must not be zero.

#### Return Value

The result is a string containing binary data.


<!-- page: PyIStream__Revert_meth.html -->

## PyIStream.Revert

 Revert()

Discards all changes that have been made to a transacted stream since the last PyIStream::Commit call.


<!-- page: PyIStream__Seek_meth.html -->

## PyIStream.Seek

 ULARGE_INTEGER = Seek(offset, origin )

Changes the seek pointer to a new location.

#### Parameters

- offset : int

 The new location

- origin : int

 Relative to where?


<!-- page: PyIStream__SetSize_meth.html -->

## PyIStream.SetSize

 SetSize(newSize)

Changes the size of the stream object.

#### Parameters

- newSize : ULARGE_INTEGER

 The new size


<!-- page: PyIStream__Stat_meth.html -->

## PyIStream.Stat

 STATSTG = Stat(grfStatFlag)

Returns information about the stream

#### Parameters

- grfStatFlag=0 : int

 Flags.


<!-- page: PyIStream__UnlockRegion_meth.html -->

## PyIStream.UnlockRegion

 UnlockRegion(offset, cb, lockType)

Removes the access restriction on a range of bytes previously restricted with PyIStream::LockRegion.

#### Parameters

- offset : ULARGE_INTEGER

 Integer that specifies the byte offset for the beginning of the range.

- cb : ULARGE_INTEGER

 The number of bytes to restrict.

- lockType : int

 Restrictions requested.


<!-- page: PyIStream__Write_meth.html -->

## PyIStream.Write

 Write(data)

Write data to a stream

#### Parameters

- data : string

 The binary data to write.


---

<!-- object: PyITask -->


<!-- page: PyITask.html -->

---

## PyITask Object

 Python object that encapsulates the ITask interface, inherits all the methods of PyIScheduledWorkItem

#### Methods

- SetApplicationName

 Specify which program the task will run

- GetApplicationName

 Retrieve name of program that task will run

- SetParameters

 Sets command line parameters

- GetParameters

 Returns command line parameters for task

- SetWorkingDirectory

 Sets initial working directory for task

- GetWorkingDirectory

 Return working directory that the task will start out in

- SetPriority

 Sets priority for task

- GetPriority

 Gets priority that will be assigned to process when task starts

- SetTaskFlags

 Sets flag for task

- GetTaskFlags

 Retrieve task flags (None currently defined)

- SetMaxRunTime

 Sets maximun run time for task, use -1 to disable

- GetMaxRunTime

 Returns maximun run time for task

#### Based On

PyIScheduledWorkItem


<!-- page: PyITask__GetApplicationName_meth.html -->

## PyITask.GetApplicationName

 PyUNICODE = GetApplicationName()

Retrieve name of program that task will run


<!-- page: PyITask__GetMaxRunTime_meth.html -->

## PyITask.GetMaxRunTime

 int = GetMaxRunTime()

Returns maximun run time for task


<!-- page: PyITask__GetParameters_meth.html -->

## PyITask.GetParameters

 PyUNICODE = GetParameters()

Returns command line parameters for task


<!-- page: PyITask__GetPriority_meth.html -->

## PyITask.GetPriority

 int = GetPriority()

Gets priority that will be assigned to process when task starts


<!-- page: PyITask__GetTaskFlags_meth.html -->

## PyITask.GetTaskFlags

 int = GetTaskFlags()

Retrieve task flags (None currently defined)


<!-- page: PyITask__GetWorkingDirectory_meth.html -->

## PyITask.GetWorkingDirectory

 PyUNICODE = GetWorkingDirectory()

Return working directory that the task will start out in


<!-- page: PyITask__SetApplicationName_meth.html -->

## PyITask.SetApplicationName

 SetApplicationName(ApplicationName)

Specify which program the task will run

#### Parameters

- ApplicationName : unicode

 Program to execute


<!-- page: PyITask__SetMaxRunTime_meth.html -->

## PyITask.SetMaxRunTime

 SetMaxRunTime(MaxRunTimeMS)

Sets maximun run time for task, use -1 to disable

#### Parameters

- MaxRunTimeMS : int

 Specified in milliseconds (use -1 to disable, not 0)


<!-- page: PyITask__SetParameters_meth.html -->

## PyITask.SetParameters

 SetParameters(Parameters)

Sets command line parameters

#### Parameters

- Parameters : unicode

 String containing command line parameters


<!-- page: PyITask__SetPriority_meth.html -->

## PyITask.SetPriority

 SetPriority(Priority)

Sets priority for task

#### Parameters

- Priority : int

 One of REALTIME_PRIORITY_CLASS, HIGH_PRIORITY_CLASS, NORMAL_PRIORITY_CLASS, IDLE_PRIORITY_CLASS


<!-- page: PyITask__SetTaskFlags_meth.html -->

## PyITask.SetTaskFlags

 SetTaskFlags(dwFlags)

Sets flag for task.

#### Parameters

- dwFlags : int

 None currently defined


<!-- page: PyITask__SetWorkingDirectory_meth.html -->

## PyITask.SetWorkingDirectory

 SetWorkingDirectory(WorkingDirectory)

Sets initial working directory for task

#### Parameters

- WorkingDirectory : unicode

 Initial working directory


---

<!-- object: PyITaskScheduler -->


<!-- page: PyITaskScheduler.html -->

---

## PyITaskScheduler Object

 Interface to the Windows Task Scheduler

#### Methods

- SetTargetComputer

 Connect to another machine to manage its tasks

- GetTargetComputer

 Returns name of computer that the Task Scheduler is connected to

- Enum

 Retrieve list of task names

- Activate

 Opens the specified task and returns an ITask interface for it

- Delete

 Delete task by name

- NewWorkItem

 Creates a new task

- AddWorkItem

 Create a new scheduled task from PyITask object

- IsOfType

 Check if named task supports specified interface


<!-- page: PyITaskScheduler__Activate_meth.html -->

## PyITaskScheduler.Activate

 PyITask = Activate(Name, riid )

Opens the specified task and returns an ITask interface for it

#### Parameters

- Name : unicode

 Name of task to retreive

- riid=IID_ITask : PyIID

 IID to return, currently only IID_ITask accepted


<!-- page: PyITaskScheduler__AddWorkItem_meth.html -->

## PyITaskScheduler.AddWorkItem

 AddWorkItem(TaskName, WorkItem)

Create a new scheduled task from PyITask object

#### Parameters

- TaskName : unicode

 Name of task to be created

- WorkItem : PyITask

 Existing PyITask object

#### Comments

 The PyItask passed in is modified in place and on success is associated with the new task, not the old one


<!-- page: PyITaskScheduler__Delete_meth.html -->

## PyITaskScheduler.Delete

 Delete(TaskName)

Delete task by name

#### Parameters

- TaskName : unicode

 Name of task to delete


<!-- page: PyITaskScheduler__Enum_meth.html -->

## PyITaskScheduler.Enum

 PyUnicode ,... = Enum()

Retrieve list of task names


<!-- page: PyITaskScheduler__GetTargetComputer_meth.html -->

## PyITaskScheduler.GetTargetComputer

 unicode = GetTargetComputer()

Returns name of computer that the Task Scheduler is connected to


<!-- page: PyITaskScheduler__IsOfType_meth.html -->

## PyITaskScheduler.IsOfType

 IsOfType(Name, riid)

Check if named object supports specified interface

#### Parameters

- Name : unicode

 Name of object

- riid : PyIID

 Named object is checked that it supports the interface of this IID


<!-- page: PyITaskScheduler__NewWorkItem_meth.html -->

## PyITaskScheduler.NewWorkItem

 PyITask = NewWorkItem(TaskName, rclsid , riid )

Creates a new task

#### Parameters

- TaskName : unicode

 Name of new task

- rclsid=CLSID_CTask : PyIID

 Class id of work item, currently only CLSID_CTask (defaults if not passed in)

- riid=IID_ITask : PyIID

 Interface IID to return, currently only IID_ITask (defaults if not passed in)


<!-- page: PyITaskScheduler__SetTargetComputer_meth.html -->

## PyITaskScheduler.SetTargetComputer

 SetTargetComputer(Computer)

Connect to another machine to manage its tasks

#### Parameters

- Computer : unicode

 Name of system to connect to

#### Comments

 Leading backslashes are required. Call will succeed without them, but no other methods will work.


---

<!-- object: PyITaskTrigger -->


<!-- page: PyITaskTrigger.html -->

---

## PyITaskTrigger Object

 Python object that encapsulates the ITaskTrigger interface

#### Methods

- SetTrigger

 Set trigger parameters from a PyTASK_TRIGGER object

- GetTrigger

 Retrieves trigger parms as a PyTASK_TRIGGER object

- GetTriggerString

 Build text summary of trigger


<!-- page: PyITaskTrigger__GetTriggerString_meth.html -->

## PyITaskTrigger.GetTriggerString

 PyUnicode = GetTriggerString()

Build text summary of trigger


<!-- page: PyITaskTrigger__GetTrigger_meth.html -->

## PyITaskTrigger.GetTrigger

 PyTASK_TRIGGER = GetTrigger()

Retrieves trigger parms as a PyTASK_TRIGGER object


<!-- page: PyITaskTrigger__SetTrigger_meth.html -->

## PyITaskTrigger.SetTrigger

 SetTrigger(Trigger)

Set trigger parameters from a PyTASK_TRIGGER object

#### Parameters

- Trigger : PyTASK_TRIGGER

 Python object representing a TASK_TRIGGER struct


---

<!-- object: PyITaskbarList -->


<!-- page: PyITaskbarList.html -->

---

## PyITaskbarList Object

 Description of the interface

#### Methods

- HrInit

 Intializes the interface before use

- AddTab

 Places a window on the taskbar

- DeleteTab

 Removes a window from the taskbar

- ActivateTab

 Marks a window as the active tab on the taskbar

- SetActiveAlt

 Sets the window as the active tab, without displaying it as pressed on the taskbar


<!-- page: PyITaskbarList__ActivateTab_meth.html -->

## PyITaskbarList.ActivateTab

 ActivateTab(hwnd)

Marks a window as the active tab on the taskbar

#### Parameters

- hwnd : PyHANDLE

 Handle to window, should have WS_CAPTION style


<!-- page: PyITaskbarList__AddTab_meth.html -->

## PyITaskbarList.AddTab

 AddTab(hwnd)

Places a window on the taskbar

#### Parameters

- hwnd : PyHANDLE

 Handle to window, should have WS_CAPTION style


<!-- page: PyITaskbarList__DeleteTab_meth.html -->

## PyITaskbarList.DeleteTab

 DeleteTab(hwnd)

Removes a window from the taskbar

#### Parameters

- hwnd : PyHANDLE

 Handle to window, should have WS_CAPTION style


<!-- page: PyITaskbarList__HrInit_meth.html -->

## PyITaskbarList.HrInit

 HrInit()

Intializes the interface before use


<!-- page: PyITaskbarList__SetActiveAlt_meth.html -->

## PyITaskbarList.SetActiveAlt

 SetActiveAlt(hwnd)

Sets the window as the active tab, without displaying it as pressed on the taskbar

#### Parameters

- hwnd : PyHANDLE

 Handle to window, should have WS_CAPTION style


---

<!-- object: PyITransferAdviseSink -->


<!-- page: PyITransferAdviseSink.html -->

---

## PyITransferAdviseSink Object

 Interface that receives notifications from PyITransferSource or PyITransferDestination

#### Methods

- UpdateProgress

 Gives an estimate of amount of work completed

- UpdateTransferState

 Notifies client of current operation state

- ConfirmOverwrite

 Asks user for permission to overwrite an existing item

- ConfirmEncryptionLoss

 Notifies user when an item can't be encrypted at destination

- FileFailure

 Notifies user of failure, and queries how to proceed

- SubStreamFailure

 Notifies user of failure on a substream, and queries how to proceed

- PropertyFailure

 Notifies user of failure to set an item's properties


<!-- page: PyITransferAdviseSink__ConfirmEncryptionLoss_meth.html -->

## PyITransferAdviseSink.ConfirmEncryptionLoss

 int = ConfirmEncryptionLoss(Source)

Notifies user when an item can't be encrypted at destination

#### Parameters

- Source : PyIShellItem

 Item that failed to be encrypted


<!-- page: PyITransferAdviseSink__ConfirmOverwrite_meth.html -->

## PyITransferAdviseSink.ConfirmOverwrite

 int = ConfirmOverwrite(Source, DestParent , Name )

Asks user for permission to overwrite an existing item

#### Parameters

- Source : PyIShellItem

 The item that will replace existing item

- DestParent : PyIShellItem

 Folder into which item will be placed

- Name : str

 New name for item, or None if item is to keep original name


<!-- page: PyITransferAdviseSink__FileFailure_meth.html -->

## PyITransferAdviseSink.FileFailure

 (int,str) = FileFailure(Item, ItemName , Error )

Notifies user of failure, and queries how to proceed

#### Parameters

- Item : PyIShellItem

 The shell item that caused the failure

- ItemName : str

 Name of item if different than above, can be None

- Error : int

 HRESULT error code from operation

#### Return Value

Returns the HRESULT and new file name if renaming resolved the failure


<!-- page: PyITransferAdviseSink__PropertyFailure_meth.html -->

## PyITransferAdviseSink.PropertyFailure

 int = PropertyFailure(Item, key , Error )

Notifies user of failure to set an item's properties

#### Parameters

- Item : PyIShellItem

 The item whose property could not be set

- key : PyPROPERTYKEY

 Identifies the property that caused the error, or None if all properties failed

- Error : int

 HRESULT error code returned by the operation

#### Return Value

Returns COPYENGINE_S_* to indicate that the failure was handled, or COPYENGINE_E_USERCANCELLED to cancel pending operations


<!-- page: PyITransferAdviseSink__SubStreamFailure_meth.html -->

## PyITransferAdviseSink.SubStreamFailure

 int = SubStreamFailure(Item, StreamName , Error )

Notifies user of failure on a substream, and queries how to proceed

#### Parameters

- Item : PyIShellItem

 The item whose stream couldn't be created

- StreamName : str

 Name of the failed stream

- Error : int

 HRESULT failure code from operation

#### Return Value

Returns COPYENGINE_S_* if operation is to continue, or COPYENGINE_E_* HRESULT if cancelled


<!-- page: PyITransferAdviseSink__UpdateProgress_meth.html -->

## PyITransferAdviseSink.UpdateProgress

 UpdateProgress(SizeCurrent, SizeTotal, FilesCurrent, FilesTotal, FoldersCurrent, FoldersTotal)

Gives an estimate of amount of work completed

#### Parameters

- SizeCurrent : int

 Bytes transferred so far

- SizeTotal : int

 Total number of bytes

- FilesCurrent : int

 Number of files processed already

- FilesTotal : int

 Total number of files

- FoldersCurrent : int

 Number of folders processed already

- FoldersTotal : int

 Total number of folder


<!-- page: PyITransferAdviseSink__UpdateTransferState_meth.html -->

## PyITransferAdviseSink.UpdateTransferState

 UpdateTransferState(State)

Notifies client of current operation state

#### Parameters

- State : int

 A TRANSFER_ADVISE_STATE value (shellcon.TS_*)


---

<!-- object: PyITransferDestination -->


<!-- page: PyITransferDestination.html -->

---

## PyITransferDestination Object

 Implemented by shell extensions that act as targets for item copy or move operations

#### Methods

- Advise

 Connects an advise sink

- Unadvise

 Disconnects an advise sink

- CreateItem

 Requests that a new item be created


<!-- page: PyITransferDestination__Advise_meth.html -->

## PyITransferDestination.Advise

 int = Advise(Sink)

Connects an advise sink

#### Parameters

- Sink : PyITransferAdviseSink

 Event sink to receive notifications

#### Return Value

Returns an id for the connection, to be passed to PyITransferDestination::Unadvise


<!-- page: PyITransferDestination__CreateItem_meth.html -->

## PyITransferDestination.CreateItem

 (int, interface, interface) = CreateItem(Name, Attributes , Size , Flags , riidItem , riidResources )

Requests that a new item be created

#### Parameters

- Name : str

 Filename to be created

- Attributes : int

 File attributes

- Size : int

 Size of file

- Flags : int

 Combination of shellcon.TSF_* flags

- riidItem=IID_IShellItem : PyIID

 Item interface to return

- riidResources=IID_IShellItemResources : PyIID

 Resource interface to return

#### Return Value

Returns the HRESULT and requested interfaces. Interfaces may be None if function returns one of the informational codes (shellcon.COPYENGINE_S_*)


<!-- page: PyITransferDestination__Unadvise_meth.html -->

## PyITransferDestination.Unadvise

 Unadvise(Cookie)

Disconnects an advise sink

#### Parameters

- Cookie : int

 Connection identifier as returned by PyITransferDestination::Advise


---

<!-- object: PyITransferMediumItem -->


<!-- page: PyITransferMediumItem.html -->

---

## PyITransferMediumItem Object

 Description of the interface

#### Based On

PyIRelatedItem


---

<!-- object: PyITransferSource -->


<!-- page: PyITransferSource.html -->

---

## PyITransferSource Object

 Implemented by shell folders that can act as the source of shell item operations

#### Methods

- Advise

 Connects an advise sink to receive notifications

- Unadvise

 Disconnects an event sink

- SetProperties

 Specifies changes to be applied to items' properties

- OpenItem

 Initiates the copying of an item

- MoveItem

 Moves a shell item into another folder

- RecycleItem

 Moves an item to the recycle bin

- RemoveItem

 Deletes an item without recycling

- RenameItem

 Renames a shell item

- LinkItem

 Not implemented, according to MSDN

- ApplyPropertiesToItem

 Changes an item's properties as specified by PyITransferSource::SetProperties

- GetDefaultDestinationName

 Determines the name of an item as it would appear in a given folder

- EnterFolder

 Informs the copy engine that a folder will be the target of a file operation

- LeaveFolder

 Informs the copy engine that the operation on a destination folder is finished


<!-- page: PyITransferSource__Advise_meth.html -->

## PyITransferSource.Advise

 int = Advise(Sink)

Connects an advise sink to receive notifications

#### Parameters

- Sink : PyITransferAdviseSink

 Event sink to respond to notifications


<!-- page: PyITransferSource__ApplyPropertiesToItem_meth.html -->

## PyITransferSource.ApplyPropertiesToItem

 PyIShellItem = ApplyPropertiesToItem(Source)

Changes an item's properties as specified by PyITransferSource::SetProperties

#### Parameters

- Source : PyIShellItem

 Item whose properties are to be changed


<!-- page: PyITransferSource__EnterFolder_meth.html -->

## PyITransferSource.EnterFolder

 int = EnterFolder(ChildFolderDest)

Informs the copy engine that a folder will be the target of a file operation

#### Parameters

- ChildFolderDest : PyIShellItem

 The destination folder for the operation


<!-- page: PyITransferSource__GetDefaultDestinationName_meth.html -->

## PyITransferSource.GetDefaultDestinationName

 str = GetDefaultDestinationName(Source, ParentDest )

Determines the name of an item as it would appear in a given folder

#### Parameters

- Source : PyIShellItem

 The item whose name is wanted

- ParentDest : PyIShellItem

 The destination folder


<!-- page: PyITransferSource__LeaveFolder_meth.html -->

## PyITransferSource.LeaveFolder

 int = LeaveFolder(ChildFolderDest)

Informs the copy engine that the operation on a destination folder is finished

#### Parameters

- ChildFolderDest : PyIShellItem

 Destination folder


<!-- page: PyITransferSource__LinkItem_meth.html -->

## PyITransferSource.LinkItem

 (int, PyIShellItem = LinkItem(Source, ParentDest , NewName , flags )

Not implemented, according to MSDN

#### Parameters

- Source : PyIShellItem

 Description for psiSource

- ParentDest : PyIShellItem

 Description for psiParentDest

- NewName : str

 Description for NewName

- flags : int

 Combination of shellcon.TSF_* flags


<!-- page: PyITransferSource__MoveItem_meth.html -->

## PyITransferSource.MoveItem

 (int, PyIShellItem = MoveItem(Item, ParentDst , NameDst , flags )

Moves a shell item into another folder

#### Parameters

- Item : PyIShellItem

 Item to be moved

- ParentDst : PyIShellItem

 The folder into which it will be moved

- NameDst : unicode

 New name for item after move, None to keep same name

- flags : int

 Combination of shellcon.TSF_* flags

#### Return Value

Returns the HRESULT from the operation and the new shell item, which may be None when the code in one of the informational COPYENGINE_S_* values. See MSDN for descriptions of expected actions for specific error codes.


<!-- page: PyITransferSource__OpenItem_meth.html -->

## PyITransferSource.OpenItem

 (int, PyIShellItemResources) = OpenItem(Item, flags , riid )

Initiates the copying of an item

#### Parameters

- Item : PyIShellItem

 The item to be copied.

- flags : int

 Combination of shellcon.TSF_* flags

- riid=IID_IShellItemResources : PyIID

 The interface to return


<!-- page: PyITransferSource__RecycleItem_meth.html -->

## PyITransferSource.RecycleItem

 (int, PyIShellItem = RecycleItem(Source, ParentDest , flags )

Moves an item to the recycle bin

#### Parameters

- Source : PyIShellItem

 The item to be recycled

- ParentDest : PyIShellItem

 Shell item representing the recycle bin

- flags : int

 Combination of shellcon.TSF_* flags


<!-- page: PyITransferSource__RemoveItem_meth.html -->

## PyITransferSource.RemoveItem

 int = RemoveItem(Source, flags )

Deletes an item without recycling

#### Parameters

- Source : PyIShellItem

 The item to be deleted

- flags : int

 Combination of shellcon.TSF_* flags

#### Return Value

Returns the HRESULT of the operation


<!-- page: PyITransferSource__RenameItem_meth.html -->

## PyITransferSource.RenameItem

 (int, PyIShellItem) = RenameItem(Source, NewName , flags )

Renames a shell item

#### Parameters

- Source : PyIShellItem

 Item to be renamed

- NewName : str

 The name to be given to the item

- flags : int

 Combination of shellcon.TSF_* flags


<!-- page: PyITransferSource__SetProperties_meth.html -->

## PyITransferSource.SetProperties

 SetProperties(proparray)

Specifies changes to be applied to items' properties

#### Parameters

- proparray : PyIPropertyChangeArray

 Property changes to be applied by PyITransferSource::ApplyPropertiesToItem


<!-- page: PyITransferSource__Unadvise_meth.html -->

## PyITransferSource.Unadvise

 Unadvise(Cookie)

Disconnects an event sink

#### Parameters

- Cookie : int

 Connection id as returned by PyITransferSource::Advise


---

<!-- object: PyITypeComp -->


<!-- page: PyITypeComp.html -->

---

## PyITypeComp Object

 An object that implements the ITypeComp interface.

#### Methods

- Bind

 Retrieves specified binding description.

- BindType

 Retrieves specified binding description for a type sentinel

#### Based On

PyIUnknown


<!-- page: PyITypeComp__BindType_meth.html -->

## PyITypeComp.BindType

 DESCKIND = BindType(szName)

binds to a type

#### Parameters

- szName : string

 The name to bind to


<!-- page: PyITypeComp__Bind_meth.html -->

## PyITypeComp.Bind

 DESCKIND = Bind(szName, wflags )

binds to a variable/type

#### Parameters

- szName : string

 The name to bind to

- wflags=0 : int

 the bind flags


---

<!-- object: PyITypeInfo -->


<!-- page: PyITypeInfo.html -->

---

## PyITypeInfo Object

 An OLE automation type info object. Derived from PyIUnknown

#### Methods

- GetContainingTypeLib

 Retrieves the containing type library and the index of the type description within that type library.

- GetDocumentation

 Retrieves the documentation string, the complete Help file name and path, and the context ID for the Help topic for a specified type description.

- GetFuncDesc

 Retrieves the FUNCDESC object that contains information about a specified function.

- GetImplTypeFlags

 Retrieves the IMPLTYPEFLAGS enumeration for one implemented interface or base interface in a type description.

- GetIDsOfNames

 Maps between member names and member IDs, and parameter names and parameter IDs.

- GetNames

 Retrieves the variable with the specified member ID (or the name of the property or method and its parameters) that correspond to the specified function ID.

- GetTypeAttr

 Retrieves a TYPEATTR object that contains the attributes of the type description.

- GetRefTypeInfo

 If a type description references other type descriptions, it retrieves the referenced type descriptions.

- GetRefTypeOfImplType

 Retrieves the type description of the implemented interface types.

- GetVarDesc

 Retrieves a VARDESC object that describes the specified variable.

- GetTypeComp

 Retrieves a ITypeComp object for Name to VARDESC/FUNCDESC mapping.

#### Based On

PyIUnknown


<!-- page: PyITypeInfo__GetContainingTypeLib_meth.html -->

## PyITypeInfo.GetContainingTypeLib

 PyITypeLib, int = GetContainingTypeLib()

Retrieves the containing type library and the index of the type description within that type library.


<!-- page: PyITypeInfo__GetDocumentation_meth.html -->

## PyITypeInfo.GetDocumentation

 (name, docstring, helpContext, helpFile) = GetDocumentation(memberId)

Retrieves the documentation string, the complete Help file name and path, and the context ID for the Help topic for a specified type description.

#### Parameters

- memberId : int


<!-- page: PyITypeInfo__GetFuncDesc_meth.html -->

## PyITypeInfo.GetFuncDesc

 FUNCDESC = GetFuncDesc(memberId)

Retrieves the FUNCDESC object that contains information about a specified function.

#### Parameters

- memberId : int


<!-- page: PyITypeInfo__GetIDsOfNames_meth.html -->

## PyITypeInfo.GetIDsOfNames

 int = GetIDsOfNames()

Maps between member names and member IDs, and parameter names and parameter IDs.


<!-- page: PyITypeInfo__GetImplTypeFlags_meth.html -->

## PyITypeInfo.GetImplTypeFlags

 int = GetImplTypeFlags(index)

Retrieves the IMPLTYPEFLAGS enumeration for one implemented interface or base interface in a type description.

#### Parameters

- index : int


<!-- page: PyITypeInfo__GetNames_meth.html -->

## PyITypeInfo.GetNames

 (tuple of strings) = GetNames(memberId)

Retrieves the variable with the specified member ID (or the name of the property or method and its parameters) that correspond to the specified function ID.

#### Parameters

- memberId : int


<!-- page: PyITypeInfo__GetRefTypeInfo_meth.html -->

## PyITypeInfo.GetRefTypeInfo

 PyITypeInfo = GetRefTypeInfo(hRefType)

If a type description references other type descriptions, it retrieves the referenced type descriptions.

#### Parameters

- hRefType : int


<!-- page: PyITypeInfo__GetRefTypeOfImplType_meth.html -->

## PyITypeInfo.GetRefTypeOfImplType

 int = GetRefTypeOfImplType(hRefType)

Retrieves the type description of the implemented interface types.

#### Parameters

- hRefType : int

#### Comments

 If a type description describes a COM class, it retrieves the type description of the implemented interface types. For an interface, GetRefTypeOfImplType returns the type information for inherited interfaces, if any exist.


<!-- page: PyITypeInfo__GetTypeAttr_meth.html -->

## PyITypeInfo.GetTypeAttr

 TYPEATTR = GetTypeAttr()

Retrieves a TYPEATTR object that contains the attributes of the type description.


<!-- page: PyITypeInfo__GetTypeComp_meth.html -->

## PyITypeInfo.GetTypeComp

 PyITypeComp = GetTypeComp()

Retrieves a ITypeComp object for Name to VARDESC/FUNCDESC mapping.


<!-- page: PyITypeInfo__GetVarDesc_meth.html -->

## PyITypeInfo.GetVarDesc

 VARDESC = GetVarDesc(memberId)

Retrieves a VARDESC object that describes the specified variable.

#### Parameters

- memberId : int


---

<!-- object: PyITypeLib -->


<!-- page: PyITypeLib.html -->

---

## PyITypeLib Object

 An object that implements the ITypeLib interface.

#### Methods

- GetDocumentation

 Retrieves documentation information about the library.

- GetLibAttr

 Retrieves the libraries attributes

- GetTypeComp

 Retrieves a ITypeComp object for Name to VARDESC/FUNCDESC mapping.

- GetTypeInfo

 Retrieves the specified type description in the library.

- GetTypeInfoCount

 Retrieves the number of PyITypeInfos in the type library.

- GetTypeInfoOfGuid

 Retrieves the type info of the specified GUID.

- GetTypeInfoType

 Retrieves the type of a type description. sentinel

#### Based On

PyIUnknown


<!-- page: PyITypeLib__GetDocumentation_meth.html -->

## PyITypeLib.GetDocumentation

 tuple = GetDocumentation(index)

Retrieves documentation information about the library.

#### Parameters

- index : int

 The index of the type description within the library

#### Return Value

The return type is a tuple of (name of item, documentation string, help context integer, help file name)


<!-- page: PyITypeLib__GetLibAttr_meth.html -->

## PyITypeLib.GetLibAttr

 TLIBATTR = GetLibAttr()

Retrieves the libraries attributes


<!-- page: PyITypeLib__GetTypeComp_meth.html -->

## PyITypeLib.GetTypeComp

 PyITypeComp = GetTypeComp()

Retrieves a ITypeComp object for Name to VARDESC/FUNCDESC mapping.


<!-- page: PyITypeLib__GetTypeInfoCount_meth.html -->

## PyITypeLib.GetTypeInfoCount

 int = GetTypeInfoCount()

Retrieves the number of PyITypeInfos in the type library.


<!-- page: PyITypeLib__GetTypeInfoOfGuid_meth.html -->

## PyITypeLib.GetTypeInfoOfGuid

 PyITypeInfo = GetTypeInfoOfGuid(iid)

Retrieves the type info of the specified GUID.

#### Parameters

- iid : PyIID

 GUID of the type description.


<!-- page: PyITypeLib__GetTypeInfoType_meth.html -->

## PyITypeLib.GetTypeInfoType

 TYPEKIND = GetTypeInfoType(index)

Retrieves the type of a type description.

#### Parameters

- index : int

 The index of the type description within the library


<!-- page: PyITypeLib__GetTypeInfo_meth.html -->

## PyITypeLib.GetTypeInfo

 PyITypeInfo = GetTypeInfo(index)

Retrieves the specified type description in the library.

#### Parameters

- index : int

 The index of the type description within the library


---

<!-- object: PyIUniformResourceLocator -->


<!-- page: PyIUniformResourceLocator.html -->

---

## PyIUniformResourceLocator Object

 Interface to an internet shortcut

#### Methods

- GetURL

 Returns the URL for the shortcut

- SetURL

 Sets the URL for the shortcut

- InvokeCommand

 Performs one of the object's predefined actions


<!-- page: PyIUniformResourceLocator__GetURL_meth.html -->

## PyIUniformResourceLocator.GetURL

 str = GetURL()

Returns the URL for the shortcut


<!-- page: PyIUniformResourceLocator__InvokeCommand_meth.html -->

## PyIUniformResourceLocator.InvokeCommand

 int = InvokeCommand(Verb, Flags , hwndParent )

Performs one of the object's predefined actions

#### Parameters

- Verb : str

 The verb to be invoked

- Flags=0 : int

 Combination of shellcon.IURL_INVOKECOMMAND_* flags

- hwndParent=0 : PyHANDLE

 Handle to parent window


<!-- page: PyIUniformResourceLocator__SetURL_meth.html -->

## PyIUniformResourceLocator.SetURL

 SetURL(URL, InFlags)

Sets the URL for the shortcut

#### Parameters

- URL : str

 The url to be set

- InFlags=0 : int

 One of the shellcon.IURL_SETURL* flags


---

<!-- object: PyIUnknown -->


<!-- page: PyIUnknown.html -->

---

## PyIUnknown Object

 The base object for all PythonCOM objects. Wraps a COM IUnknown object.

#### Methods

- QueryInterface

 Queries the object for an interface.

#### Comments

 Note that there are no reference counting functions that are typically exposed via COM. This is because COM reference counts are automatically handled by PythonCOM - each interface object keeps exactly one COM reference, regardless of how many Python references. When the Python object destructs due to its reference count hitting zero, the COM reference is then released. It is not possible for force the closure of a PythonCOM object - the only way to ensure cleanup is to remove all Python references.


<!-- page: PyIUnknown__QueryInterface_meth.html -->

## PyIUnknown.QueryInterface

 PyIUnknown = QueryInterface(iid, useIID )

Queries an object for a specific interface.

#### Parameters

- iid : IID

 The IID requested.

- useIID=None : IID

 If provided and not None, will return an interface for the specified IID if (and only if) a native interface can not be supported. If the interface specified by iid is natively supported, this option is ignored.

#### Comments

 The useIID parameter is a very dangerous option, and should only be used when you are sure you need it! By specifying this parameter, you are telling the COM framework that regardless of the true type of the result (as specified by iid), a Python wrapper of type useIID will be created. If iid does not derive from useIID, then it is almost certain that using the object will cause an Access Violation.
For example, this option can be used to obtain a PyIUnknown object if pythoncom does not natively support the interface. Another example might be to return an unsupported persistence interface as a PyIPersist instance.
 For backwards compatibility: the integer 0 implies None, and the integer 1 implies IID_IUnknown.

#### Return Value

The result is always an object derived from PyIUnknown. Any error (including E_NOINTERFACE) will generate a com_error exception.


<!-- page: PyIUnknown____cmp___meth.html -->

## PyIUnknown.__cmp__

 int = __cmp__()

Implements COM rules for object identity.

#### Comments

 As per the COM rules for object identity, both objects are queried for IUnknown, and these values compared. The only meaningful test is for equality - the result of other comparisons is undefined (ie, determined by the object's relative addresses in memory.


<!-- page: PyIUnknown____repr___meth.html -->

---

## PyIUnknown::__repr__ method

 string __repr__()

 Called to create a representation of a PyIUnknown object

 Defined in: D:/A/PYWIN32/PYWIN32/COM/WIN32COM/SRC/PYIUNKNOWN.CPP

#### Comments

 The repr of this object displays both the object's address, and its attached IUnknown's address


---

<!-- object: PyIViewObject -->


<!-- page: PyIViewObject.html -->

---

## PyIViewObject Object

 Description of the interface

#### Methods

- Draw

 Description of Draw

- GetColorSet

 Description of GetColorSet

- Freeze

 Description of Freeze

- Unfreeze

 Description of Unfreeze

- SetAdvise

 Description of SetAdvise

- GetAdvise

 Description of GetAdvise


<!-- page: PyIViewObject__Draw_meth.html -->

## PyIViewObject.Draw

 Draw(dwDrawAspect, lindex, aspectFlags, hdcTargetDev, hdcDraw, left, top, right, bottom, left, top, right, bottom, funcContinue, obContinue)

Description of Draw.

#### Parameters

- dwDrawAspect : int

 Description for dwDrawAspect

- lindex : int

 Description for lindex

- aspectFlags : int

 Integer value for the dwFlags item of the DVASPECTINFO structure.

- hdcTargetDev : HDC

 Description for hdcTargetDev

- hdcDraw : HDC

 Description for hdcDraw

- left, top, right, bottom : int, int, int, int

 Bounds rectangle.

- left, top, right, bottom : int, int, int, int

 WBounds rectangle.

- funcContinue : object

 A continue function.

- obContinue : object

 Value passed to the function.


<!-- page: PyIViewObject__Freeze_meth.html -->

## PyIViewObject.Freeze

 Freeze(dwDrawAspect, lindex, aspectFlags)

Description of Freeze.

#### Parameters

- dwDrawAspect : int

 Description for dwDrawAspect

- lindex : int

 Description for lindex

- aspectFlags : int

 Integer value for the dwFlags item of the DVASPECTINFO structure.


<!-- page: PyIViewObject__GetAdvise_meth.html -->

## PyIViewObject.GetAdvise

 GetAdvise()

Description of GetAdvise.


<!-- page: PyIViewObject__GetColorSet_meth.html -->

## PyIViewObject.GetColorSet

 GetColorSet(dwDrawAspect, lindex, aspectFlags, hicTargetDev)

Description of GetColorSet.

#### Parameters

- dwDrawAspect : int

 Description for dwDrawAspect

- lindex : int

 Description for lindex

- aspectFlags : int

 Integer value for the dwFlags item of the DVASPECTINFO structure.

- hicTargetDev : HDC

 Description for hicTargetDev


<!-- page: PyIViewObject__SetAdvise_meth.html -->

## PyIViewObject.SetAdvise

 SetAdvise(aspects, advf, pAdvSink)

Description of SetAdvise.

#### Parameters

- aspects : int

 Description for aspects

- advf : int

 Description for advf

- pAdvSink : PyIAdviseSink

 Description for pAdvSink


<!-- page: PyIViewObject__Unfreeze_meth.html -->

## PyIViewObject.Unfreeze

 Unfreeze(dwFreeze)

Description of Unfreeze.

#### Parameters

- dwFreeze : int

 Description for dwFreeze


---

<!-- object: PyIViewObject2 -->


<!-- page: PyIViewObject2.html -->

---

## PyIViewObject2 Object

 Description of the interface

#### Methods

- GetExtent

 Description of GetExtent


<!-- page: PyIViewObject2__GetExtent_meth.html -->

## PyIViewObject2.GetExtent

 GetExtent(dwDrawAspect, lindex, targetDevice)

Description of GetExtent.

#### Parameters

- dwDrawAspect : int

 Description for dwDrawAspect

- lindex : int

 Description for lindex

- targetDevice : PyDVTARGETDEVICE

 Description for lindex
