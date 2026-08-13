# pywin32 对象文档 · 分卷 Py

> 共 298 个对象，来源 https://mhammond.github.io/pywin32/<Object>.html


---

<!-- object: PyACL -->


<!-- page: PyACL.html -->

---

## PyACL Object

 A Python object, representing a ACL structure

#### Methods

- Initialize

 Initialize the ACL.

- IsValid

 Validate the ACL.

- AddAccessAllowedAce

 Adds an access-allowed ACE to an ACL object.

- AddAccessAllowedAceEx

 Same as AddAccessAllowedAce, with addition of ace flags

- AddAccessAllowedObjectAce

 Adds an ACCESS_ALLOWED_OBJECT_ACE to the ACL

- AddAccessDeniedAce

 Adds an access-denied ACE to an ACL object.

- AddAccessDeniedAceEx

 Adds an access-denied ACE to an ACL object

- AddMandatoryAce

 Adds a mandatory integrity level ACE to a SACL

- AddAccessAllowedObjectAce

 Adds an ACCESS_DENIED_OBJECT_ACE to the ACL

- AddAuditAccessAce

 Adds an audit entry to a system access control list (SACL)

- AddAuditAccessAceEx

 Adds an audit ACE to an SACL with inheritance flags

- AddAuditAccessObjectAce

 Adds an audit ACE for an object type identified by GUID

- GetAclSize

 Returns the storage size of the ACL.

- GetAclRevision

 Returns the revision nbr of the ACL.

- GetAceCount

 Returns the number of ACEs in the ACL.

- GetAce

 Returns an ACE from the ACL.

- DeleteAce

 Delete an access-control entry (ACE) from an ACL

- GetExplicitEntriesFromAcl

 Retrieve list of EXPLICIT_ACCESSs from the ACL

- SetEntriesInAcl

 Adds a list of EXPLICIT_ACCESSs to an ACL

- GetEffectiveRightsFromAcl

 Return access rights (ACCESS_MASK) that the ACL grants to specified trustee

- GetAuditedPermissionsFromAcl

 Return types of access for which ACL will generate an audit event for specified trustee


<!-- page: PyACL__AddAccessAllowedAceEx_meth.html -->

## PyACL.AddAccessAllowedAceEx

 AddAccessAllowedAceEx(revision, aceflags, access, sid)

Add access allowed ACE to an ACL with ACE flags (Requires Win2k or higher)

#### Parameters

- revision : int

 Must be at least ACL_REVISION_DS

- aceflags : int

 Combination of ACE inheritance flags (CONTAINER_INHERIT_ACE,INHERIT_ONLY_ACE,INHERITED_ACE,NO_PROPAGATE_INHERIT_ACE, and OBJECT_INHERIT_ACE)

- access : int

 Specifies the mask of access rights to be granted to the specified SID.

- sid : PySID

 A SID object representing a user, group, or logon account being granted access.


<!-- page: PyACL__AddAccessAllowedAce_meth.html -->

## PyACL.AddAccessAllowedAce

 AddAccessAllowedAce(revision, access, sid)

Adds an access-allowed ACE to an DACL object. The access is granted to a specified SID.

#### Parameters

- revision : int

 Pre-win2k, must be ACL_REVISION, otherwise also may be ACL_REVISION_DS.

- access : int

 Specifies the mask of access rights to be denied to the specified SID.

- sid : PySID

 A SID object representing a user, group, or logon account being denied access.

#### Alternative Parameters

- access

 Specifies the mask of access rights to be denied to the specified SID.

- sid

 A SID object representing a user, group, or logon account being denied access.

#### Comments

 Note that early versions of this function supported only two arguments. This has been deprecated in preference of the three argument version, which reflects the win32 API and the new functions in this module.


<!-- page: PyACL__AddAccessAllowedObjectAce_meth.html -->

## PyACL.AddAccessAllowedObjectAce

 AddAccessAllowedObjectAce(AceRevision, AceFlags, AccessMask, ObjectTypeGuid, InheritedObjectTypeGuid, sid)

Adds an ACCESS_ALLOWED_OBJECT_ACE to the ACL

#### Parameters

- AceRevision : int

 Must be at least ACL_REVISION_DS

- AceFlags : int

 Combination of ACE inheritance flags (CONTAINER_INHERIT_ACE,INHERIT_ONLY_ACE,INHERITED_ACE,NO_PROPAGATE_INHERIT_ACE, and OBJECT_INHERIT_ACE)

- AccessMask : int

 Specifies the mask of access rights to be granted to the specified SID

- ObjectTypeGuid : PyIID

 GUID of object type or property set to which ace applies, can be None

- InheritedObjectTypeGuid : PyIID

 GUID of object type or property that will inherit ACE, can be None

- sid : PySID

 A SID object representing a user, group, or logon account being granted access.


<!-- page: PyACL__AddAccessDeniedAceEx_meth.html -->

## PyACL.AddAccessDeniedAceEx

 AddAccessDeniedAceEx(revision, aceflags, access, sid)

Add access denied ACE to an ACL with ACE flags (Requires Win2k or higher)

#### Parameters

- revision : int

 Must be at least ACL_REVISION_DS

- aceflags : int

 Combination of ACE inheritance flags (CONTAINER_INHERIT_ACE,INHERIT_ONLY_ACE,INHERITED_ACE,NO_PROPAGATE_INHERIT_ACE, and OBJECT_INHERIT_ACE)

- access : int

 Specifies the mask of access rights to be denied to the specified SID.

- sid : PySID

 A SID object representing a user, group, or logon account being denied access.


<!-- page: PyACL__AddAccessDeniedAce_meth.html -->

## PyACL.AddAccessDeniedAce

 AddAccessDeniedAce(revision, access, sid)

Adds an access-denied ACE to an ACL object. The access is denied to a specified SID.

#### Parameters

- revision : int

 Pre-win2k, must be ACL_REVISION, otherwise also may be ACL_REVISION_DS.

- access : int

 Specifies the mask of access rights to be denied to the specified SID.

- sid : PySID

 A SID object representing a user, group, or logon account being denied access.

#### Alternative Parameters

- access

 Specifies the mask of access rights to be denied to the specified SID.

- sid

 A SID object representing a user, group, or logon account being denied access.

#### Comments

 Note that early versions of this function supported only two arguments. This has been deprecated in preference of the three argument version, which reflects the win32 API and the new functions in this module.


<!-- page: PyACL__AddAccessDeniedObjectAce_meth.html -->

## PyACL.AddAccessDeniedObjectAce

 AddAccessDeniedObjectAce(AceRevision, AceFlags, AccessMask, ObjectTypeGuid, InheritedObjectTypeGuid, sid)

Adds an ACCESS_DENIED_OBJECT_ACE to the ACL

#### Parameters

- AceRevision : int

 Must be at least ACL_REVISION_DS

- AceFlags : int

 Combination of ACE inheritance flags (CONTAINER_INHERIT_ACE,INHERIT_ONLY_ACE,INHERITED_ACE,NO_PROPAGATE_INHERIT_ACE, and OBJECT_INHERIT_ACE)

- AccessMask : int

 Specifies the mask of access rights to be granted to the specified SID

- ObjectTypeGuid : PyIID

 GUID of object type or property set to which ace applies, can be None

- InheritedObjectTypeGuid : PyIID

 GUID of object type or property that will inherit ACE, can be None

- sid : PySID

 A SID object representing a user, group, or logon account that will be denied access.


<!-- page: PyACL__AddAuditAccessAceEx_meth.html -->

## PyACL.AddAuditAccessAceEx

 AddAuditAccessAceEx(dwAceRevision, AceFlags, dwAccessMask, sid, bAuditSuccess, bAuditFailure)

Adds an audit ACE to an Sacl, includes ace flags

#### Parameters

- dwAceRevision : int

 Revision of ACL: Must be at least ACL_REVISION_DS

- AceFlags : int

 Combination of FAILED_ACCESS_ACE_FLAG,SUCCESSFUL_ACCESS_ACE_FLAG,CONTAINER_INHERIT_ACE,INHERIT_ONLY_ACE,INHERITED_ACE,NO_PROPAGATE_INHERIT_ACE and OBJECT_INHERIT_ACE

- dwAccessMask : int

 Bitmask of access types to be audited

- sid : PySID

 SID for whom system audit messages will be generated

- bAuditSuccess : int

 Set to 1 if access success should be audited, else 0

- bAuditFailure : int

 Set to 1 if access failure should be audited, else 0


<!-- page: PyACL__AddAuditAccessAce_meth.html -->

## PyACL.AddAuditAccessAce

 AddAuditAccessAce(dwAceRevision, dwAccessMask, sid, bAuditSuccess, bAuditFailure)

Adds an audit ACE to a Sacl

#### Parameters

- dwAceRevision : int

 Revision of ACL: Pre-Win2k, must be ACL_REVISION. Win2K on up, can also be ACL_REVISION_DS

- dwAccessMask : int

 Bitmask of access types to be audited

- sid : PySID

 SID for whom system audit messages will be generated

- bAuditSuccess : int

 Set to 1 if access success should be audited, else 0

- bAuditFailure : int

 Set to 1 if access failure should be audited, else 0


<!-- page: PyACL__AddAuditAccessObjectAce_meth.html -->

## PyACL.AddAuditAccessObjectAce

 AddAuditAccessObjectAce(dwAceRevision, AceFlags, dwAccessMask, ObjectTypeGuid, InheritedObjectTypeGuid, sid, bAuditSuccess, bAuditFailure)

Adds an audit ACE for an object type identified by GUID

#### Parameters

- dwAceRevision : int

 Revision of ACL: Must be at least ACL_REVISION_DS

- AceFlags : int

 Combination of FAILED_ACCESS_ACE_FLAG,SUCCESSFUL_ACCESS_ACE_FLAG,CONTAINER_INHERIT_ACE,INHERIT_ONLY_ACE,INHERITED_ACE,NO_PROPAGATE_INHERIT_ACE and OBJECT_INHERIT_ACE

- dwAccessMask : int

 Bitmask of access types to be audited

- ObjectTypeGuid : PyIID

 GUID of object type or property set to which ace applies, can be None

- InheritedObjectTypeGuid : PyIID

 GUID of object type or property that will inherit ACE, can be None

- sid : PySID

 SID for whom system audit messages will be generated

- bAuditSuccess : int

 Set to 1 if access success should be audited, else 0

- bAuditFailure : int

 Set to 1 if access failure should be audited, else 0


<!-- page: PyACL__AddMandatoryAce_meth.html -->

## PyACL.AddMandatoryAce

 AddMandatoryAce(AceRevision, AceFlags, MandatoryPolicy, LabelSid)

Adds a mandatory integrity level ACE to a SACL

#### Parameters

- AceRevision : int

 ACL_REVISION or ACL_REVISION_DS

- AceFlags : int

 Combination of ACE inheritance flags (CONTAINER_INHERIT_ACE,INHERIT_ONLY_ACE,INHERITED_ACE,NO_PROPAGATE_INHERIT_ACE, and OBJECT_INHERIT_ACE)

- MandatoryPolicy : int

 Access policy for processes with lower integrity level, combination of SYSTEM_MANDATORY_LABEL_* flags

- LabelSid : PySID

 Integrity level SID. This can be created using CreateWellKnownSid with Win*LabelSid.
Also can be constructed manually using SECURITY_MANDATORY_LABEL_AUTHORITY and a SECURITY_MANDATORY_*_RID


<!-- page: PyACL__DeleteAce_meth.html -->

## PyACL.DeleteAce

 DeleteAce(index)

Deletes specified Ace from an ACL.

#### Parameters

- index : int

 Zero-based index of the ACE to delete.


<!-- page: PyACL__GetAceCount_meth.html -->

## PyACL.GetAceCount

 int = GetAceCount()

Returns the number of ACEs in the ACL.


<!-- page: PyACL__GetAce_meth.html -->

## PyACL.GetAce

 tuple = GetAce(index)

Gets an Ace from the ACL

#### Parameters

- index : int

 Zero-based index of the ACE to retrieve.

#### Return Value

Conventional ACE's (types ACCESS_ALLOWED_ACE, ACCESS_DENIED_ACE, SYSTEM_AUDIT_ACE) are returned as a tuple of:

#### Items

- [0] (int, int) : aceType, AceFlags

- [1] int : Mask

- [2] PySID : sid

Object ACE's (types ACCESS_ALLOWED_OBJECT_ACE, ACCESS_DENIED_OBJECT_ACE, SYSTEM_AUDIT_OBJECT_ACE) are returned as a tuple:

- [0] (int, int) : aceType, AceFlags

- [1] int : mask

- [2] PyIID : ObjectType

- [3] PyIID : InheritedObjectType

- [4] PySID : sid

For details see the API documentation.


<!-- page: PyACL__GetAclRevision_meth.html -->

## PyACL.GetAclRevision

 int = GetAclRevision()

Returns revision of the ACL.


<!-- page: PyACL__GetAclSize_meth.html -->

## PyACL.GetAclSize

 int = GetAclSize()

Returns the storage size of the ACL.


<!-- page: PyACL__GetAuditedPermissionsFromAcl_meth.html -->

## PyACL.GetAuditedPermissionsFromAcl

 (SuccessfulAuditedRights,FailedAuditRights) = GetAuditedPermissionsFromAcl(trustee)

Return types of access for which ACL will generate an audit event for specified trustee

#### Parameters

- trustee : PyTRUSTEE

 Dictionary representing a TRUSTEE structure


<!-- page: PyACL__GetEffectiveRightsFromAcl_meth.html -->

## PyACL.GetEffectiveRightsFromAcl

 ACCESS_MASK = GetEffectiveRightsFromAcl(trustee)

Return access rights (ACCESS_MASK) that the ACL grants to specified trustee

#### Parameters

- trustee : PyTRUSTEE

 Dictionary representing a TRUSTEE structure


<!-- page: PyACL__Initialize_meth.html -->

## PyACL.Initialize

 Initialize()

Initialize the ACL.

#### Comments

 It should not be necessary to call this, as the ACL object is initialised by Python. This method gives you a chance to trap any errors that may occur.


<!-- page: PyACL__IsValid_meth.html -->

## PyACL.IsValid

 IsValid()

Determines if the ACL is valid (IsValidAcl)


---

<!-- object: PyADSVALUE -->


<!-- page: PyADSVALUE.html -->

---

## PyADSVALUE Object

 A tuple:

#### Items

- [0] object : value

 The value as a Python object.

- [1] int : type

 The AD type of the value.


---

<!-- object: PyADS_ATTR_INFO -->


<!-- page: PyADS_ATTR_INFO.html -->

---

## PyADS_ATTR_INFO Object

 Represents a ADS_ATTR_INFO structure.

#### Properties

- unicode AttrName
 The name

- integer ControlCode

- integer ADsType

- [PyADSVALUE, ...] Values


---

<!-- object: PyADS_OBJECT_INFO -->


<!-- page: PyADS_OBJECT_INFO.html -->

---

## PyADS_OBJECT_INFO Object

 Represents a ADS_OBJECT_INFO structure.

#### Properties

- unicode RDN
 The name

- unicode ObjectDN

- unicode ParentDN

- unicode ClassName


---

<!-- object: PyADS_SEARCHPREF_INFO -->


<!-- page: PyADS_SEARCHPREF_INFO.html -->

---

## PyADS_SEARCHPREF_INFO Object

 A tuple of:

#### Items

- [0] int : attr_id

- [1] PyADSVALUE : value


---

<!-- object: PyAssocCObject -->


<!-- page: PyAssocCObject.html -->

---

## PyAssocCObject Object

 An internal class.


---

<!-- object: PyAssocObject -->


<!-- page: PyAssocObject.html -->

---

## PyAssocObject Object

 An internal class.

#### Methods

- AttachObject

 Attaches a Python object for lookup of "virtual" functions.

- GetAttachedObject

 Returned the attached Python object, or None.


<!-- page: PyAssocObject__AttachObject_meth.html -->

## PyAssocObject.AttachObject

 AttachObject()

Attaches a Python object for lookup of "virtual" functions.


<!-- page: PyAssocObject__GetAttachedObject_meth.html -->

## PyAssocObject.GetAttachedObject

 object = GetAttachedObject()

Returned the attached Python object, or None.


---

<!-- object: PyBIND_OPTS -->


<!-- page: PyBIND_OPTS.html -->

---

## PyBIND_OPTS Object

 Dictionary representation of a BIND_OPTS struct May eventually be extended to include BIND_OPTS2 members

#### Properties

- int Flags
 Value from BIND_FLAGS enum: BIND_MAYBOTHERUSER, BIND_JUSTTESTEXISTENCE or 0

- int Mode
 Combination of storagecon.STGM_* values

- int TickCountDeadline
 Operation timeout in milliseconds

- int cbStruct
 Size of struct, ignored on input


---

<!-- object: PyBITMAP -->


<!-- page: PyBITMAP.html -->

---

## PyBITMAP Object

 A Python object, representing an PyBITMAP structure

#### Comments

 Typically you get one of these from GetObject. Note that currently the bitmap bits are not exposed via this type - but the value of the pointer is. You can use the struct and win32gui functions to unpack these bits manually if you really need them. Note that you are still responsible for the life of the win32 bitmap object. The object can then be passed to any function which takes an BITMAP object

#### Properties

- integer bmType

- integer bmWidth

- integer bmHeight

- integer bmWidthBytes

- integer bmPlanes

- integer


---

<!-- object: PyBLENDFUNCTION -->


<!-- page: PyBLENDFUNCTION.html -->

---

## PyBLENDFUNCTION Object

 Tuple of four small ints used to fill a BLENDFUNCTION struct Each int must fit in a byte (0-255).

#### Win32 API References

- Search for BLENDFUNCTION at [msdn](https://learn.microsoft.com/en-ca/search/?terms=BLENDFUNCTION), [google](https://www.google.com/search?q=BLENDFUNCTION) or [google groups](https://groups.google.com/groups?q=BLENDFUNCTION).

#### Items

- [0] int : BlendOp

 Only defined value is AC_SRC_OVER (0)

- [1] int : BlendFlags

 None currently defined, must be 0

- [2] int : SourceConstantAlpha

 Transparency to be applied to entire source. (255 is opaque)

- [3] int : AlphaFormat

 Only defined flag is AC_SRC_ALPHA, used when src bitmap contains per-pixel alpha


---

<!-- object: PyCBitmap -->


<!-- page: PyCBitmap.html -->

---

## PyCBitmap Object

 A bitmap class, derived from a PyCGdiObject.

#### Methods

- CreateCompatibleBitmap

 Creates a bitmap compatible with the specified device context.

- GetSize

 Gets the size of the bitmap object, in pixels.

- GetHandle

 Returns the HBITMAP for a bitmap.

- LoadBitmap

 Loads a bitmap from a DLL object.

- LoadBitmapFile

 Loads a bitmap from a file object.

- LoadPPMFile

 Loads a bitmap from a file object containing a PPM format bitmap.

- Paint

 Paints a bitmap to a windows DC.

- GetInfo

 Returns the BITMAP structure info.

- GetBitmapBits

 Returns the bitmap bits.

- SaveBitmapFile

 Saves a bitmap to a file. sentinel


<!-- page: PyCBitmap__CreateCompatibleBitmap_meth.html -->

## PyCBitmap.CreateCompatibleBitmap

 CreateCompatibleBitmap(dc, width, height)

Creates a bitmap compatible with the specified device context.

#### Parameters

- dc : PyCDC

 Specifies the device context.

- width : int

 The width (in bits) of the bitmap

- height : int

 The height (in bits) of the bitmap.


<!-- page: PyCBitmap__GetBitmapBits_meth.html -->

## PyCBitmap.GetBitmapBits

 tuple/string = GetBitmapBits(asString)

Returns the bitmap bits.

#### Parameters

- asString=0 : int

 If False, the result is a tuple of integers, if True, the result is a Python string


<!-- page: PyCBitmap__GetHandle_meth.html -->

## PyCBitmap.GetHandle

 int = GetHandle()

Returns the HBITMAP for a bitmap object


<!-- page: PyCBitmap__GetInfo_meth.html -->

## PyCBitmap.GetInfo

 dict = GetInfo()

Returns the BITMAP structure info

#### Return Value

A dictionary of integers, keyed by the following strings:
 bmType
 bmWidth
 bmHeight
 bmWidthBytes
 bmPlanes
 bmBitsPixel


<!-- page: PyCBitmap__GetSize_meth.html -->

## PyCBitmap.GetSize

 (cx,cy) = GetSize()

Returns the size of the bitmap object.


<!-- page: PyCBitmap__LoadBitmapFile_meth.html -->

## PyCBitmap.LoadBitmapFile

 LoadBitmapFile(fileObject)

Loads a bitmap (.BMP) format from a file object.

#### Parameters

- fileObject : file[.read]

 The file object to load the .BMP format file from.


<!-- page: PyCBitmap__LoadBitmap_meth.html -->

## PyCBitmap.LoadBitmap

 LoadBitmap(idRes, obDLL)

Loads a bitmap from a DLL object.

#### Parameters

- idRes : int

 The resource ID of the bitmap

- obDLL=None : PyDLL

 The DLL object to load from.


<!-- page: PyCBitmap__LoadPPMFile_meth.html -->

## PyCBitmap.LoadPPMFile

 LoadPPMFile(fileObject, cols, rows)

Loads a bitmap in Portable Pix Map (PPM) format from a file object.

#### Parameters

- fileObject : file[.read]

 The file object to load the PPM format file from.

- cols : int

 The number of columns in the bitmap.

- rows : int

 The number of rows in the bitmap.


<!-- page: PyCBitmap__Paint_meth.html -->

## PyCBitmap.Paint

 Paint(dcObject, rectDest, rectSrc)

Paint a bitmap.

#### Parameters

- dcObject : PyCDC

 The DC object to paint the bitmap to.

- rectDest=(0,0,0,0) : (left,top,right,bottom)

 The destination rectangle to paint to.

- rectSrc=(0,0,0,0) : (left,top,right,bottom)

 The source rectangle to paint from.


<!-- page: PyCBitmap__SaveBitmapFile_meth.html -->

## PyCBitmap.SaveBitmapFile

 None = SaveBitmapFile(dcObject, Filename )

Saves a bitmap to a file.

#### Parameters

- dcObject : PyCDC

 The DC object that has rendered the bitmap.

- Filename : string

 The file to save the bitmap to


---

<!-- object: PyCBrush -->


<!-- page: PyCBrush.html -->

---

## PyCBrush Object

 An object encapsulating an MFC PyCBrush class.

#### Methods

- CreateSolidBrush

 Initializes a brush with a specified solid color.

- GetSafeHandle

 Retrieves the HBRUSH for the brush as an integer


<!-- page: PyCBrush__CreateSolidBrush_meth.html -->

## PyCBrush.CreateSolidBrush

 CreateSolidBrush()

Initializes a brush with a specified solid color.


<!-- page: PyCBrush__GetSafeHandle_meth.html -->

## PyCBrush.GetSafeHandle

 int = GetSafeHandle()

Retrieves the HBRUSH for the brush as an integer


---

<!-- object: PyCButton -->


<!-- page: PyCButton.html -->

---

## PyCButton Object

 A windows button. Encapsulates an MFC CButton class. Derived from PyCControl.

#### Methods

- CreateWindow

 Creates the window for a new button object.

- GetBitmap

 Retrieves the bitmap associated with the button.

- SetBitmap

 Sets the bitmap of a button.

- GetCheck

 Retrieves the check state of a radio button or check box.

- SetCheck

 Sets the check state of a radio button or check box.

- GetState

 Retrieves the state of a radio button or check box.

- SetState

 Sets the state of a radio button or check box.

- GetButtonStyle

 Retrieves the style of a radio button or check box.

- SetButtonStyle

 Sets the state of a radio button or check box.


<!-- page: PyCButton__CreateWindow_meth.html -->

## PyCButton.CreateWindow

 CreateWindow(caption, style, rect, parent, id)

Creates the window for a new button object.

#### Parameters

- caption : string

 The caption (text) for the button.

- style : int

 The style for the button. Use any of the win32con.BS_* constants.

- rect : (left, top, right, bottom)

 The size and position of the button.

- parent : PyCWnd

 The parent window of the button. Usually a PyCDialog.

- id : int

 The buttons control ID.


<!-- page: PyCButton__GetBitmap_meth.html -->

## PyCButton.GetBitmap

 int = GetBitmap()

Get the button's bitmap


<!-- page: PyCButton__GetButtonStyle_meth.html -->

## PyCButton.GetButtonStyle

 int = GetButtonStyle()

Gets the style of the button.


<!-- page: PyCButton__GetCheck_meth.html -->

## PyCButton.GetCheck

 int = GetCheck()

Retrieves the check state of a radio button or check box.


<!-- page: PyCButton__GetState_meth.html -->

## PyCButton.GetState

 int = GetState()

Returns the state of the button.


<!-- page: PyCButton__SetBitmap_meth.html -->

## PyCButton.SetBitmap

 int = SetBitmap(hBitmap)

Set the button's bitmap

#### Parameters

- hBitmap=1 : int

 Handle of the new bitmap


<!-- page: PyCButton__SetButtonStyle_meth.html -->

## PyCButton.SetButtonStyle

 int = SetButtonStyle(style, bRedraw )

Sets the style of the button.

#### Parameters

- style : int

 The new style for the button.

- bRedraw=1 : int

 Should the button be redrawn?


<!-- page: PyCButton__SetCheck_meth.html -->

## PyCButton.SetCheck

 SetCheck(idCheck)

Sets or resets the state of a radio button or check box.

#### Parameters

- idCheck : int

 The ID of the button.


<!-- page: PyCButton__SetState_meth.html -->

## PyCButton.SetState

 int = SetState(bHighlight)

Sets the state of the button.

#### Parameters

- bHighlight : int

 The new state for the button.

#### Comments

 Highlighting affects the exterior of a button control. It has no effect on the check state of a radio button or check box.


---

<!-- object: PyCCmdTarget -->


<!-- page: PyCCmdTarget.html -->

---

## PyCCmdTarget Object

 An abstract command target class. Encapsulates an MFC CCmdTarget class

#### Methods

- BeginWaitCursor

 Displays the cursor as an hourglass.

- EndWaitCursor

 End a wait cursor.

- HookCommand

 Hook a command handler.

- HookCommandUpdate

 Hook a windows command update handler.

- HookOleEvent

 Hooks an OLE event.

- HookNotify

 Hook a control notification handler.

- RestoreWaitCursor

 Restores the appropriate hourglass cursor after the system cursor has changed.


<!-- page: PyCCmdTarget__BeginWaitCursor_meth.html -->

## PyCCmdTarget.BeginWaitCursor

 BeginWaitCursor()

Displays the cursor as an hourglass. This can be used when you expect a command to take a noticeable time to execute (eg, when a document loads or saves itself to a file.).
The actions of BeginWaitCursor are not always effective outside of a single message handler as other actions, such as OnSetCursor handling, could change the cursor.
Call EndWaitCursor to restore the previous cursor.

#### MFC References

- CWnd::BeginWaitCursor


<!-- page: PyCCmdTarget__EndWaitCursor_meth.html -->

## PyCCmdTarget.EndWaitCursor

 EndWaitCursor()

Ends a wait cursor. Should only be called after PyCWnd::BeginWaitCursor .


<!-- page: PyCCmdTarget__HookCommandUpdate_meth.html -->

## PyCCmdTarget.HookCommandUpdate

 object = HookCommandUpdate(obHandler, id )

Hook a windows command update handler.

#### Parameters

- obHandler : object

 The handler for the command message. This must be a callable object.

- id : int

 The ID of the command to be handled.

#### Comments

 The handler object passed will be called as the application updates user interface elements with the specified ID. See PyCCmdTarget::HookCommand for a description of the rules used to determine command routing and updating.

#### Return Value

The return value is the previous handler, or None.


<!-- page: PyCCmdTarget__HookCommand_meth.html -->

## PyCCmdTarget.HookCommand

 object = HookCommand(obHandler, id )

Hook a windows command handler.

#### Parameters

- obHandler : object

 The handler for the command message. This must be a callable object.

- id : int

 The ID of the command to be handled, or zero to handle all command messages.

#### Comments

 obHandler will be called as the application receives command notification messages with the specified ID. Command notification messages are usually sent in response to menu or toolbar commands.
When updating a user interface element, Pythonwin will first check if a handler has been installed via PyCCmdTarget::HookCommandUpdate. If so, this alone determines the state of the interface object. If no Update handler exists, PythonWin will automatically enable a menu/toolbar item if a command handler exists The handler will be called with 2 arguments
* The command id being handled.
* The command notification code.
If the handler returns TRUE, then the command will be passed on to the default handler, otherwise the message will be consumed.
This method is best suited to handling messages from user interface elements, such as menus, toolbars, etc. To handle notification messages from a control, you should use PyCCmdTarget::HookNotify

#### Return Value

The return value is the previous handler, or None.


<!-- page: PyCCmdTarget__HookNotify_meth.html -->

## PyCCmdTarget.HookNotify

 object = HookNotify(obHandler, id )

Hook a windows command handler.

#### Parameters

- obHandler : object

 The handler for the command message. This must be a callable object.

- id : int

 The ID of the command to be handled, or zero to handle all command messages.

#### Comments

 obHandler will be called as the application receives control notification messages. These may also be handled via PyCCmdTarget::HookCommand, but this method is specific to control notifications, and therefore provides more information.

 The handler will be called with 2 arguments
 A tuple describing standard notification information.
 A tuple describing extra notification params, or an integer containing the address of the first byte of the extended information.
 If the handler returns TRUE, then the command will be passed on to the default handler, otherwise the message will be consumed.

 Certain notification codes are recognised internally, and these are converted to a Python tuple. If the extra information is not recognised, the address is passed. These addresses could be extracted using win32ui::GetBytes and the struct module, or using Sam Rushing's calldll/dynwin module. (It would be possible to extend Pythonwin so a program can install certain knowledge about handlers, but this has not been implemented.)

#### Return Value

The return value is the previous handler, or None.


<!-- page: PyCCmdTarget__HookOleEvent_meth.html -->

## PyCCmdTarget.HookOleEvent

 object = HookOleEvent()

Hook an OLE Event.

#### Return Value

The return value is the previous handler, or None.


<!-- page: PyCCmdTarget__RestoreWaitCursor_meth.html -->

## PyCCmdTarget.RestoreWaitCursor

 RestoreWaitCursor()

Restores the appropriate hourglass cursor after the system cursor has changed.

#### Comments

 Call this function to restore the appropriate hourglass cursor after the system cursor has changed (for example, after a message box has opened and then closed while in the middle of a lengthy operation).


---

<!-- object: PyCCmdUI -->


<!-- page: PyCCmdUI.html -->

---

## PyCCmdUI Object

 A class for manipulating user-interface elements. Encapsulates an MFC CCmdUI class

#### Methods

- Enable

 Enables or disables the user-interface item for this command.

- SetCheck

 Sets the check state of the user-interface item for this command.

- SetRadio

 Like the SetCheck member function, but operates on radio groups.

- SetText

 Sets the text for the user-interface item for this command.

- ContinueRouting

 Tells the command-routing mechanism to continue routing the current message down the chain of handlers.

#### Properties

- int m_nIndex

- int m_nID

- PyCMenu m_pMenu

- PyCMenu m_pSubMenu


<!-- page: PyCCmdUI__ContinueRouting_meth.html -->

## PyCCmdUI.ContinueRouting

 ContinueRouting()

Tells the command-routing mechanism to continue routing the current message down the chain of handlers.


<!-- page: PyCCmdUI__Enable_meth.html -->

## PyCCmdUI.Enable

 Enable(bEnable)

Enables or disables the user-interface item for this command.

#### Parameters

- bEnable=1 : int

 TRUE if the item should be enabled, false otherwise.


<!-- page: PyCCmdUI__SetCheck_meth.html -->

## PyCCmdUI.SetCheck

 SetCheck(state)

Sets the check state of the user-interface item for this command.

#### Parameters

- state=1 : int

 0 for unchecked, 1 for checked, or 2 for indeterminate.


<!-- page: PyCCmdUI__SetRadio_meth.html -->

## PyCCmdUI.SetRadio

 SetRadio(bOn)

Like the SetCheck member function, but operates on radio groups.

#### Parameters

- bOn=1 : int

 TRUE if the item should be enabled, false otherwise.


<!-- page: PyCCmdUI__SetText_meth.html -->

## PyCCmdUI.SetText

 SetText(text)

Sets the text for the user-interface item for this command.

#### Parameters

- text : string

 The text for the interface element.


---

<!-- object: PyCColorDialog -->


<!-- page: PyCColorDialog.html -->

---

## PyCColorDialog Object

 A class which encapsulates an MFC CColorDialog object. Derived from a PyCDialog object.

#### Methods

- GetColor

 Determines the selected color.

- DoModal

 Displays a dialog and allows the user to make a selection.

- GetSavedCustomColors

 Returns the saved custom colors.

- SetCurrentColor

 Sets the currently selected color.

- SetCustomColors

 Sets one or more custom colors

- GetCustomColors

 Gets the currently defined custom colors.

#### Based On

PyCCommonDialog


<!-- page: PyCColorDialog__DoModal_meth.html -->

## PyCColorDialog.DoModal

 int = DoModal()

Displays a dialog and allows the user to make a selection.

#### MFC References

- CColorDialog::DoModal


<!-- page: PyCColorDialog__GetColor_meth.html -->

## PyCColorDialog.GetColor

 int = GetColor()

Determines the selected color.

#### MFC References

- CColorDialog::GetColor


<!-- page: PyCColorDialog__GetCustomColors_meth.html -->

## PyCColorDialog.GetCustomColors

 (int,...) = GetCustomColors()

Gets the 16 currently defined custom colors


<!-- page: PyCColorDialog__GetSavedCustomColors_meth.html -->

## PyCColorDialog.GetSavedCustomColors

 int = GetSavedCustomColors()

Returns the saved custom colors.

#### MFC References

- CColorDialog::GetSavedCustomColors


<!-- page: PyCColorDialog__SetCurrentColor_meth.html -->

## PyCColorDialog.SetCurrentColor

 SetCurrentColor(color)

Sets the currently selected color.

#### Parameters

- color : int

 The color to set.

#### MFC References

- CColorDialog::SetCurrentColor


<!-- page: PyCColorDialog__SetCustomColors_meth.html -->

## PyCColorDialog.SetCustomColors

 SetCustomColors()

Sets one or more custom colors


---

<!-- object: PyCComboBox -->


<!-- page: PyCComboBox.html -->

---

## PyCComboBox Object

 A windows combo control. Encapsulates an MFC CComboBox class. Derived from a PyCControl object.

#### Methods

- AddString

 Add a string to the listbox portion of a combo box.

- DeleteString

 Delete a string to the listbox portion of a combo box.

- Dir

 Fill the listbox portion of a combo with a file specification.

- GetCount

 Get the count of items in the listbox portion of a combo box.

- GetCurSel

 Get the current selection in the listbox portion of a combo box.

- GetEditSel

 Gets the edit control selection from a combo box.

- GetExtendedUI

 Gets the ExtendedUI flag for a combo box.

- GetItemData

 Retrieves the application-specific object associated with a combobox entry

- GetItemValue

 Retrieves the application-specific value associated with a combobox entry

- GetLBText

 Gets the text from the edit control in a combo box.

- GetLBTextLen

 Gets the length of the text in the edit control of a combo box.

- InsertString

 Inserts a string into the listbox portion of a combo box.

- LimitText

 Limit the length of text in the edit control portion of a combo box.

- ResetContent

 Remove all items from the listbox portion of a combo box.

- SelectString

 Select a string in the listbox portion of a combo box.

- SetCurSel

 Sets the current selection in the listbox portion of a combo box.

- SetEditSel

 Sets the current selection in the edit control portion of a combo box.

- SetExtendedUI

 Sets the ExtendedUI flag for a combo box.

- SetItemData

 Sets the application-specific object associated with a combobox entry

- SetItemValue

 Sets the application-specific value associated with a combobox entry

- ShowDropDown

 Shows the listbox portion of a combo box.


<!-- page: PyCComboBox__AddString_meth.html -->

## PyCComboBox.AddString

 int = AddString(object)

Adds a string to a combobox.

#### Parameters

- object : any

 Any object. If not a string, __str__, __repr__ or a default repr() will be used

#### MFC References

- CComboBox::AddString

#### Return Value

The zero based index of the new string.


<!-- page: PyCComboBox__DeleteString_meth.html -->

## PyCComboBox.DeleteString

 int = DeleteString(pos)

Deletes an item from a combobox.

#### Parameters

- pos : int

 The zero based index of the item to delete.

#### MFC References

- CComboBox::DeleteString

#### Return Value

The count of the items remaining in the list.


<!-- page: PyCComboBox__Dir_meth.html -->

## PyCComboBox.Dir

 int = Dir(attr, wild )

Fills the list portion of a combobox with a directory listing.

#### Parameters

- attr : int

 The attributes of the files to locate

- wild : string

 A file specification string - eg, *.*

#### MFC References

- CComboBox::Dir

#### Return Value

The index of the last file name added to the list.


<!-- page: PyCComboBox__GetCount_meth.html -->

## PyCComboBox.GetCount

 int = GetCount()

Returns the count of items in the combobox.

#### MFC References

- CListBox::GetCount

#### Return Value

Returns the number of items currently in the combobox.


<!-- page: PyCComboBox__GetCurSel_meth.html -->

## PyCComboBox.GetCurSel

 int = GetCurSel()

Returns the index of the currently selected item.

#### Comments

 Should not be called for a multiple selection listbox.

#### MFC References

- CComboBox::GetCurSel


<!-- page: PyCComboBox__GetEditSel_meth.html -->

## PyCComboBox.GetEditSel

 int = GetEditSel()

Returns the selection of the edit control portion of a combo box.

#### MFC References

- CComboBox::GetEditSel

#### Return Value

A 32-bit value that contains the starting position in the low-order word and the position of the first nonselected character after the end of the selection in the high-order word. If this function is used on a combo box without an edit control, an exception is raised.


<!-- page: PyCComboBox__GetExtendedUI_meth.html -->

## PyCComboBox.GetExtendedUI

 int = GetExtendedUI()

Indicates if the combo has the extended interface.

#### MFC References

- CComboBox::GetExtendedUI

#### Return Value

Nonzero if the combo box has the extended user interface; otherwise 0.


<!-- page: PyCComboBox__GetItemData_meth.html -->

## PyCComboBox.GetItemData

 object = GetItemData(item)

Retrieves the application-specific object associated with an item.

#### Parameters

- item : int

 The index of the item whose data is to be retrieved.


<!-- page: PyCComboBox__GetItemValue_meth.html -->

## PyCComboBox.GetItemValue

 int = GetItemValue(item)

Retrieves the application-specific value associated with an item.

#### Parameters

- item : int

 The index of the item whose data is to be retrieved.


<!-- page: PyCComboBox__GetLBTextLen_meth.html -->

## PyCComboBox.GetLBTextLen

 int = GetLBTextLen(index)

Returns the length of a string in the list of a combobox.

#### Parameters

- index : int

 The index of the item to return the length of.

#### MFC References

- CComboBox::GetLBTextLen rdesc Returns the length of the string (in bytes), or raises an exception on error.


<!-- page: PyCComboBox__GetLBText_meth.html -->

## PyCComboBox.GetLBText

 string = GetLBText(index)

Gets the string from the list of a combo box.

#### Parameters

- index : int

 The index of the item to return the string for.

#### Return Value

The requested string. If index does not specify a valid index, no exception is raised.


<!-- page: PyCComboBox__InsertString_meth.html -->

## PyCComboBox.InsertString

 int = InsertString(pos, object )

Insert a string into a combobox.

#### Parameters

- pos : int

 The zero based index in the combobox to insert the new string

- object : any

 The object to be added to the combobox

#### MFC References

- CComboBox::InsertString

#### Return Value

The zero based index of the new string added.


<!-- page: PyCComboBox__LimitText_meth.html -->

## PyCComboBox.LimitText

 int = LimitText(max)

Limits the amount of text the edit portion of a combo box can hold.

#### Parameters

- max : int

 The maximum number of characters the user can enter. If zero, the size is set to (virtually) unlimited.

#### MFC References

- CComboBox::LimitText


<!-- page: PyCComboBox__ResetContent_meth.html -->

## PyCComboBox.ResetContent

 ResetContent()

Clear all the items from a combobox.

#### MFC References

- CComboBox::ResetContent


<!-- page: PyCComboBox__SelectString_meth.html -->

## PyCComboBox.SelectString

 SelectString(after, string)

Searches for a combobox item that matches the specified string, and selects it.

#### Parameters

- after : int

 Contains the zero-based index of the item before the first item to be searched, or -1 for the entire combobox.

- string : string

 The string to search for.

#### MFC References

- CComboBoxBox::SelectString

#### Return Value

The return value is always None - an exception is raised if the string can not be located.


<!-- page: PyCComboBox__SetCurSel_meth.html -->

## PyCComboBox.SetCurSel

 SetCurSel(index)

Selects an item in a combobox.

#### Parameters

- index : int

 The zero based index of the item to select.

#### MFC References

- CComboBox::SetCurSel


<!-- page: PyCComboBox__SetEditSel_meth.html -->

## PyCComboBox.SetEditSel

 SetEditSel(start, end)

Sets the selection in the edit control portion of a combo box.

#### Parameters

- start : int

 Specifies the starting position. If the starting position is set to -1, then any existing selection is removed.

- end : int

 Specifies the ending position. If the ending position is set to -1, then all text from the starting position to the last character in the edit control is selected.

#### MFC References

- PyCComboBox::SetEditSel

#### Return Value

The return value is always None - an exception is raised if the combo is a dropdown style, or does not have an edit control.


<!-- page: PyCComboBox__SetExtendedUI_meth.html -->

## PyCComboBox.SetExtendedUI

 SetExtendedUI(bExtended)

Selects the Extended UI mode for a combo box.

#### Parameters

- bExtended=1 : int

 Indicates if the combo should have the extended user interface.

#### Comments

 A combo box with the Extended UI flag set can be identified in the following ways:~ Clicking the static control displays the list box only for combo boxes with the CBS_DROPDOWNLIST style.~ Pressing the DOWN ARROW key displays the list box (F4 is disabled).~ Scrolling in the static control is disabled when the item list is not visible (the arrow keys are disabled).

#### MFC References

- CListBox::SetExtendedUI


<!-- page: PyCComboBox__SetItemData_meth.html -->

## PyCComboBox.SetItemData

 int = SetItemData(item, Data )

Sets the item's application-specific object value.

#### Parameters

- item : int

 Index of the item whose Data is to be set.

- Data : object

 New value for the data.

#### Comments

 Note that a reference count is not added to the object. This it is your responsibility to make sure the object remains alive while in the list.


<!-- page: PyCComboBox__SetItemValue_meth.html -->

## PyCComboBox.SetItemValue

 int = SetItemValue(item, data )

Sets the item's application-specific value.

#### Parameters

- item : int

 Index of the item whose Data is to be set.

- data : int

 New value for the data.


<!-- page: PyCComboBox__ShowDropDown_meth.html -->

## PyCComboBox.ShowDropDown

 ShowDropDown(bShowIt)

Shows or hides the listbox portion of a combo box.

#### Parameters

- bShowIt=1 : int

 Indicates if the listbox should be shown or hidden.


---

<!-- object: PyCCommonDialog -->


<!-- page: PyCCommonDialog.html -->

---

## PyCCommonDialog Object

 An abstract class which encapsulates an MFC CCommonDialog object. Derived from a PyCDialog object.


---

<!-- object: PyCControl -->


<!-- page: PyCControl.html -->

---

## PyCControl Object

 A windows abstract control. Derived from a PyCWnd object.


---

<!-- object: PyCControlBar -->


<!-- page: PyCControlBar.html -->

---

## PyCControlBar Object

 A class which encapsulates an MFC CControlBar . Derived from a PyCWnd object.

#### Methods

- CalcDynamicLayout

 The framework calls this member function to calculate the dimensions of a dynamic toolbar.

- CalcFixedLayout

 Calculates the horizontal size of a control bar

- EnableDocking

 Specifies whether the control bar supports docking and the sides of its parent window.

- EraseNonClient

- GetBarStyle

 Retrieves the control bar style settings.

- GetCount

 Returns the number of non-HWND elements in the control bar.

- GetDockingFrame

 Returns the frame window to which a control bar is docked.

- IsFloating

 Returns a nonzero value if the control bar in question is a floating control bar.

- SetBarStyle

 Modifies the control bar style settings.

- ShowWindow

 Shows the window, and recalculates the toolbar layout.

#### Properties

- PyCFrameWnd dockSite
 Current dock site, if dockable

- PyCWnd dockBar
 Current dock bar, if dockable

- PyCDockContext dockContext
 Used during dragging

- int dwStyle
 creation style (used for layout)

- int dwDockStyle
 indicates how bar can be docked


<!-- page: PyCControlBar__CalcDynamicLayout_meth.html -->

## PyCControlBar.CalcDynamicLayout

 int = CalcDynamicLayout(length, dwMode )

The framework calls this member function to calculate the dimensions of a dynamic toolbar.

#### Parameters

- length : int

 The requested dimension of the control bar, either horizontal or vertical, depending on dwMode.

- dwMode : int

 A combination of flags.


<!-- page: PyCControlBar__CalcDynamicLayout_virtual.html -->

## PyCControlBar.CalcDynamicLayout Virtual

 CalcDynamicLayout()

Override to augment control-bar size calculations.

#### Comments

 The base implementation is not called if a handler exists. This can be done via CPythonControlBar::CalcDynamicLayout .

#### See Also

- CPythonControlBar::CalcDynamicLayout


<!-- page: PyCControlBar__CalcFixedLayout_meth.html -->

## PyCControlBar.CalcFixedLayout

 int = CalcFixedLayout(bStretch, bHorz )

Calculates the horizontal size of a control bar

#### Parameters

- bStretch : int

 Indicates whether the bar should be stretched to the size of the frame. The bStretch parameter is nonzero when the bar is not a docking bar (not available for docking) and is 0 when it is docked or floating (available for docking).

- bHorz : int

 Indicates that the bar is horizontally or vertically oriented.


<!-- page: PyCControlBar__CalcFixedLayout_virtual.html -->

## PyCControlBar.CalcFixedLayout Virtual

 CalcFixedLayout()

Override to augment control-bar size calculations.

#### Comments

 The base implementation is not called if a handler exists. This can be done via CPythonControlBar::CalcFixedLayout .

#### See Also

- CPythonControlBar::CalcFixedLayout


<!-- page: PyCControlBar__EnableDocking_meth.html -->

## PyCControlBar.EnableDocking

 EnableDocking(style)

pecifies whether the control bar supports docking and the sides of its parent window.

#### Parameters

- style : int

 Enables a control bar to be docked.


<!-- page: PyCControlBar__EraseNonClient_meth.html -->

## PyCControlBar.EraseNonClient

 EraseNonClient()


<!-- page: PyCControlBar__GetBarStyle_meth.html -->

## PyCControlBar.GetBarStyle

 int = GetBarStyle()

Retrieves the control bar style settings.


<!-- page: PyCControlBar__GetCount_meth.html -->

## PyCControlBar.GetCount

 int = GetCount()

Returns the number of non-HWND elements in the control bar.


<!-- page: PyCControlBar__GetDockingFrame_meth.html -->

## PyCControlBar.GetDockingFrame

 PyCFrameWnd = GetDockingFrame()

Returns the frame window to which a control bar is docked.


<!-- page: PyCControlBar__IsFloating_meth.html -->

## PyCControlBar.IsFloating

 int = IsFloating()

Returns a nonzero value if the control bar in question is a floating control bar.


<!-- page: PyCControlBar__OnBarStyleChange_virtual.html -->

## PyCControlBar.OnBarStyleChange Virtual

 OnBarStyleChange()

Override to augment control-bar size calculations.

#### Comments

 The base implementation is not called if a handler exists. This can be done via CPythonControlBar::OnBarStyleChange .


<!-- page: PyCControlBar__OnUpdateCmdUI_virtual.html -->

## PyCControlBar.OnUpdateCmdUI Virtual

 OnUpdateCmdUI(frame, bDisableIsNoHandler )

#### Parameters

- frame : PyCFrameWnd

- bDisableIsNoHandler : int


<!-- page: PyCControlBar__SetBarStyle_meth.html -->

## PyCControlBar.SetBarStyle

 SetBarStyle(style)

Modifies the control bar style settings.

#### Parameters

- style : int

 The new style


<!-- page: PyCControlBar__ShowWindow_meth.html -->

## PyCControlBar.ShowWindow

 int = ShowWindow()

Shows the toolbar, and recalculates the button layout.

#### Comments

 This method is provided for convenience. For further details, see PyCWnd::ShowWindow and PyCFrameWnd::RecalcLayout

#### Return Value

The return value is that returned from PyCWnd::ShowWindow


---

<!-- object: PyCCtrlView -->


<!-- page: PyCCtrlView.html -->

---

## PyCCtrlView Object

 A class which implements a CCtrlView (ie, a view based on a dialog resource.

#### Methods

- OnCommand

 Calls the standard Python framework OnCommand handler

#### Based On

PyCView


<!-- page: PyCCtrlView__OnCommand_meth.html -->

## PyCCtrlView.OnCommand

 OnCommand(wparam, lparam)

Calls the standard Python framework OnCommand handler

#### Parameters

- wparam : int

- lparam : int

#### See Also

- PyCWnd.OnCommand virtual method


---

<!-- object: PyCDC -->


<!-- page: PyCDC.html -->

---

## PyCDC Object

 A Device Context. Encapsulates an MFC CDC class.

#### Methods

- AbortDoc

 Aborts a print job

- Arc

 Draws an arc.

- BeginPath

 Opens a path bracket in the device context

- BitBlt

 Copies a bitmap

- Chord

 Draws a chord.

- CreateCompatibleDC

 Creates a memory DC compatible with this DC.

- CreatePrinterDC

 Creates a device context for a specific printer

- DeleteDC

 Deletes all resources associated with a device context.

- DPtoLP

 Convert from device points to logical points.

- Draw3dRect

 Draws a three-dimensional rectangle.

- DrawFocusRect

 Draws a rectangle in the style used to indicate the rectangle has focus

- DrawFrameControl

 Draws a frame control of the specified type and style.

- DrawIcon

 Draws an icon on the DC.

- DrawText

 Formats text in the given rectangle

- Ellipse

 Draws an Ellipse.

- EndDoc

 Finishes spooling the document and starts printing it

- EndPage

 Finishes a page on a printer DC

- EndPath

 Closes a path bracket and selects the path defined by the bracket into the specified device context

- ExtTextOut

 Writes text to the DC.

- FillPath

 Closes any open figures in the current path and fills the path's interior by using the current brush and polygon-filling mode.

- FillRect

 Fills a given rectangle with the specified brush

- FillSolidRect

 Fills the given rectangle with the specified solid color.

- FrameRect

 Draws a border around the rectangle specified by rect

- GetBrushOrg

 Retrieves the origin (in device units) of the brush currently selected for the device context.

- GetClipBox

 Retrives the current clipping region.

- GetCurrentPosition

 Retrieves the current position (in logical coordinates).

- GetDeviceCaps

 Retrieves current device capabilities.

- GetHandleAttrib

 Retrieves the handle of the attribute device context.

- GetHandleOutput

 Retrieves the handle of the output device context.

- GetMapMode

 Gets the mapping mode for the device context.

- GetNearestColor

 Returns the closest color a device can map.

- GetPixel

 Returns the value of a pixel at a location

- GetSafeHdc

 Returns the underlying windows handle for the DC object.

- GetTextExtent

 Calculates the size of the string.

- GetTextExtentPoint

 Alias for GetTextExtent - Calculates the size of the string.

- GetTextFace

 Retrieves the name of the current font.

- GetTextMetrics

 Retrieves the metrics for the current font.

- GetViewportExt

 Gets the viewport extent of the device context

- GetViewportOrg

 Gets the viewport origin of the device context

- GetWindowExt

 Gets the window extent of the device context

- GetWindowOrg

 Retrieves the x- and y-coordinates of the origin of the window associated with the device context.

- IntersectClipRect

 Creates a new clipping region by forming the intersection of the current region and the rectangle specified

- IsPrinting

 Returns 1 if the DC is currently printing, else 0

- LineTo

 Draws a line to a specified point.

- LPtoDP

 Convert from logical points to device points

- MoveTo

 Moves the current position to a specifed point.

- OffsetWindowOrg

 Modifies the coordinates of the window origin relative to the coordinates of the current window origin.

- OffsetViewportOrg

 Modifies the coordinates of the viewport origin relative to the coordinates of the current viewport origin

- PatBlt

 Creates a bit pattern on the device.

- Pie

 Draws a pie shape with specific starting and ending points in a rectangle

- PolyBezier

 Draws one or more Bezier splines.

- Polygon

 Draws an Polygon.

- Polyline

 Draws a Polyline.

- RealizePalette

 Maps palette entries in the current logical palette to the system palette.

- Rectangle

 Draws a rectangle using the current pen. The interior of the rectangle is filled using the current brush.

- RectVisible

 Determines if a rectangle is currently visisble in the viewport.

- RestoreDC

 Restores a saved DC.

- SaveDC

 Saves a DC.

- ScaleWindowExt

 Modifies the window extents relative to the current values.

- ScaleViewportExt

 Modifies the viewport extents relative to the current values.

- SelectClipRgn

 Selects the given region as the current clipping region for the device context

- SelectObject

 Selects an object into the DC.

- SelectObject

 Selects the logical palette.

- SetBkColor

 Sets the background color.

- SetBkMode

 Sets the background mode.

- SetBrushOrg

 Specifies the origin that GDI will assign to the next brush that the application selects into the device context.

- SetGraphicsMode

 Sets the graphics mode for the specified device context

- SetMapMode

 Sets the device mapping mode.

- SetPixel

 Set a pixel to a color

- SetPolyFillMode

 Sets the polygon-filling mode.

- SetROP2

 Sets the current drawing mode.

- SetTextAlign

 Sets the text alignment.

- SetTextColor

 Sets the text foreground color.

- SetWindowExt

 Sets the extents of the window.

- SetWindowOrg

 Sets the window origin of the device context

- SetViewportExt

 Sets the extents of the window's viewport.

- SetViewportOrg

 Sets the viewport origin of the device context

- SetWorldTransform

 sets a two-dimensional linear transformation between world space and page space for the specified device context.

- StartDoc

 Starts spooling a document to a printer DC

- StartPage

 Starts a new page on a printer DC

- StretchBlt

 Copies a bitmap from the source device context to this device context.

- StrokeAndFillPath

 Closes any open figures in a path, strokes the outline of the path by using the current pen, and fills its interior by using the current brush. The device context must contain a closed path.

- StrokePath

 Renders the specified path by using the current pen.

- TextOut

 Writes text to the DC.


<!-- page: PyCDC__AbortDoc_meth.html -->

## PyCDC.AbortDoc

 AbortDoc()

Aborts a print job


<!-- page: PyCDC__Arc_meth.html -->

## PyCDC.Arc

 Arc(rect, pointStart, pointEnd)

Draws an eliptical arc.

#### Parameters

- rect : (left, top, right, bottom)

 Specifies the ellipse's bounding rectangle

- pointStart : (x,y)

 Specifies the x- and y-coordinates of the point that defines the arc's starting point (in logical units). This point does not have to lie exactly on the arc.

- pointEnd : (x,y)

 Specifies the x- and y-coordinates of the point that defines the arc's ending point (in logical units). This point does not have to lie exactly on the arc.

#### Comments

 The arc drawn by using the function is a segment of the ellipse defined by the specified bounding rectangle. The actual starting point of the arc is the point at which a ray drawn from the center of the bounding rectangle through the specified starting point intersects the ellipse. The actual ending point of the arc is the point at which a ray drawn from the center of the bounding rectangle through the specified ending point intersects the ellipse. The arc is drawn in a counterclockwise direction. Since an arc is not a closed figure, it is not filled. Both the width and height of the rectangle must be greater than 2 units and less than 32,767 units.

#### MFC References

- CDC::Arc

#### Return Value

Always none. If the function fails, an exception is raised.


<!-- page: PyCDC__BeginPath_meth.html -->

## PyCDC.BeginPath

 BeginPath()

Opens a path bracket in the device context


<!-- page: PyCDC__BitBlt_meth.html -->

## PyCDC.BitBlt

 BitBlt(destPos, size, dc, srcPos, rop)

Copies a bitmap from the source device context to this device context.

#### Parameters

- destPos : (x,y)-ints

 The logical x,y coordinates of the upper-left corner of the destination rectangle.

- size : (width, height)-ints

 Specifies the width and height (in logical units) of the destination rectangle and source bitmap.

- dc : PyCDC

 Specifies the PyCDC object from which the bitmap will be copied. It must be None if rop specifies a raster operation that does not include a source.

- srcPos : (xSrc, ySrc)-ints

 Specifies the logical x,y coordinates of the upper-left corner of the source bitmap.

- rop : int

 Specifies the raster operation to be performed. See the win32 api documentation for details.

#### MFC References

- CDC::BitBlt


<!-- page: PyCDC__Chord_meth.html -->

## PyCDC.Chord

 Chord(rect, pointStart, pointEnd)

Draws a chord.

#### Parameters

- rect : (left, top, right, bottom)

 Specifies the ellipse's bounding rectangle

- pointStart : (x,y)

 Specifies the x- and y-coordinates of the point that defines the arc's starting point (in logical units). This point does not have to lie exactly on the arc.

- pointEnd : (x,y)

 Specifies the x- and y-coordinates of the point that defines the arc's ending point (in logical units). This point does not have to lie exactly on the arc.

#### Comments

 Draws a chord (a closed figure bounded by the intersection of an ellipse and a line segment). The rect parameter specify the upper-left and lower-right corners, respectively, of a rectangle bounding the ellipse that is part of the chord. The pointStart and pointEnd parameters specify the endpoints of a line that intersects the ellipse. The chord is drawn by using the selected pen and filled by using the selected brush.

#### MFC References

- CDC::Chord

#### Return Value

Always none. If the function fails, an exception is raised.


<!-- page: PyCDC__CreateCompatibleDC_meth.html -->

## PyCDC.CreateCompatibleDC

 CreateCompatibleDC(dcFrom)

Creates a memory device context that is compatible with this DC.

#### Parameters

- dcFrom=None : PyCDC

 The source DC, or None to make a screen compatible DC.

#### Comments

 Note that unlike the MFC version, this function calls the global CreateCompatibleDC function and returns a new PyCDC object.

#### MFC References

- CDC::CreateCompatibleDC


<!-- page: PyCDC__CreatePrinterDC_meth.html -->

## PyCDC.CreatePrinterDC

 CreatePrinterDC(printerName)

Creates a device context for a specific printer

#### Parameters

- printerName=None : string

 The printer name, or None for the default printer

#### MFC References

- CDC::CreateDC


<!-- page: PyCDC__DPtoLP_meth.html -->

## PyCDC.DPtoLP

 (x,y) = DPtoLP(point)

Converts device units into logical units.

#### Parameters

- point : (x,y)

 The point to convert

#### Alternative Parameters

- x

 The x coordinate to convert.

- y

 The y coordinate to convert.

#### MFC References

- CDC::DPtoLP

#### To Do

 Should really handle list of (x,y) points

#### Return Value

The converted coordinates.


<!-- page: PyCDC__DeleteDC_meth.html -->

## PyCDC.DeleteDC

 DeleteDC()

Deletes all resources associated with a device context.

#### Comments

 In general, do not call this function; the destructor will do it for you.
An application should not call DeleteDC if objects have been selected into the device context. Objects must first be selected out of the device context before it it is deleted.
An application must not delete a device context whose handle was obtained by calling CWnd::GetDC. Instead, it must call CWnd::ReleaseDC to free the device context.
The DeleteDC function is generally used to delete device contexts created with CreateDC, CreateIC, or CreateCompatibleDC.


<!-- page: PyCDC__Draw3dRect_meth.html -->

## PyCDC.Draw3dRect

 Draw3dRect(rect, colorTopLeft, colorBotRight)

Draws a three-dimensional rectangle.

#### Parameters

- rect : (left, top, right, bottom

 Specifies the bounding rectangle, in logical units.

- colorTopLeft : int

 Specifies the color of the top and left sides of the three-dimensional rectangle.

- colorBotRight : int

 Specifies the color of the bottom and right sides of the three-dimensional rectangle.

#### MFC References

- CDC::Draw3dRect


<!-- page: PyCDC__DrawFocusRect_meth.html -->

## PyCDC.DrawFocusRect

 DrawFocusRect(rect)

Draws a rectangle in the style used to indicate the rectangle has focus

#### Parameters

- rect : (left, top, right, bottom)

 The coordinates of the rectangle

#### MFC References

- CDC::DrawFocusRect


<!-- page: PyCDC__DrawFrameControl_meth.html -->

## PyCDC.DrawFrameControl

 DrawFrameControl(rect, typ, state)

Draws a frame control of the specified type and style.

#### Parameters

- rect : (left, top, right, bottom)

 Specifies the bounding rectangle, in logical units.

- typ : int

- state : int

#### MFC References

- CDC::DrawFrameControl


<!-- page: PyCDC__DrawIcon_meth.html -->

## PyCDC.DrawIcon

 DrawIcon(point, hIcon)

Draws an icon on the DC.

#### Parameters

- point : (x,y)

 The point coordinate to draw to.

- hIcon : PyHANDLE

 The handle of the icon to draw.

#### MFC References

- CDC::DrawIcon


<!-- page: PyCDC__DrawText_meth.html -->

## PyCDC.DrawText

 s,rc,forat = DrawText(s, tuple , format )

Formats text in the given rectangle

#### Parameters

- s : string

 The desired output string

- tuple : (int, int, int, int)

 The bounding rectangle in the form: (left, top, right, bottom) expressed in logical units (depending on selected coordinate system - see PyCDC::SetMapMode)

- format : int

 Specifies one or more bit-or'd format values, such as DT_BOTTOM, DT_CENTERDT_RIGHT, DT_VCENTER. For a complete list, see the Microsoft Win32 API documentation.

#### Example

Example

```
import win32ui<nl>



 import win32con<nl>



 INCH = 1440   # twips - 1440 per inch allows fine res<nl>



 def drawtext_test():<nl>



     dc = win32ui.CreateDC()<nl>



     dc.CreatePrinterDC()                # ties to default printer<nl>



     dc.StartDoc('My Python Document')<nl>



     dc.StartPage()<nl>



 <nl>



     # note: upper left is 0,0 with x increasing to the right,<nl>



     #       and y decreasing (negative) moving down<nl>



     dc.SetMapMode(win32con.MM_TWIPS)<nl>



 <nl>



     # Centers "TEST" about an inch down on page<nl>



     dc.DrawText('TEST', (0,INCH*-1,INCH*8,INCH*-2), win32con.DT_CENTER )<nl>



     dc.EndPage()<nl>



     dc.EndDoc()<nl>



     del dc<nl>




```

#### Return Value

Height of text in pixels

 The return value is the height of the text, in logical units. If DT_VCENTER or DT_BOTTOM is specified, the return value is the offset from rect.top to the bottom of the drawn text. If the function fails, the return value is zero (no Python exception is thrown)


<!-- page: PyCDC__Ellipse_meth.html -->

## PyCDC.Ellipse

 Ellipse(rect)

Draws an Ellipse.

#### Parameters

- rect : (left, top, right, bottom)

 Specifies the ellipse's bounding rectangle

#### Comments

 The center of the ellipse is the center of the bounding rectangle specified by rect. The ellipse is drawn with the current pen, and its interior is filled with the current brush.

#### MFC References

- CDC::Ellipse

#### Return Value

Always none. If the function fails, an exception is raised.


<!-- page: PyCDC__EndDoc_meth.html -->

## PyCDC.EndDoc

 EndDoc()

Finishes spooling the document and starts printing it


<!-- page: PyCDC__EndPage_meth.html -->

## PyCDC.EndPage

 EndPage()

Finishes a page on a printer DC


<!-- page: PyCDC__EndPath_meth.html -->

## PyCDC.EndPath

 EndPath()

Closes a path bracket and selects the path defined by the bracket into the specified device context


<!-- page: PyCDC__ExtTextOut_meth.html -->

## PyCDC.ExtTextOut

 ExtTextOut(int, int, int, rect, string, tuple)

Writes text to the DC.

#### Parameters

- int : x

 The x coordinate to write the text to.

- int : y

 The y coordinate to write the text to.

- int : nOptions

 Specifies the rectangle type. This parameter can be one, both, or neither of ETO_CLIPPED and ETO_OPAQUE

- rect : (left, top, right, bottom)

 Specifies the text's bounding rectangle. (Can be None.)

- string : text

 The text to write.

- tuple : (width1, width2, ...)

 Optional array of values that indicate distance between origins of character cells.

#### MFC References

- CDC::ExtTextOut

#### Return Value

Always none. If the function fails, an exception is raised.


<!-- page: PyCDC__FillPath_meth.html -->

## PyCDC.FillPath

 FillPath()

Closes any open figures in the current path and fills the path's interior by using the current brush and polygon-filling mode. After its interior is filled, the path is discarded from the device context.


<!-- page: PyCDC__FillRect_meth.html -->

## PyCDC.FillRect

 FillRect(rect, brush)

Fills a given rectangle with the specified brush

#### Parameters

- rect : (left, top, right, bottom

 Specifies the bounding rectangle, in logical units.

- brush : PyCBrush

 Specifies the brush to use.

#### MFC References

- CDC::FillRect


<!-- page: PyCDC__FillSolidRect_meth.html -->

## PyCDC.FillSolidRect

 FillSolidRect(rect, color)

Fills the given rectangle with the specified solid color.

#### Parameters

- rect : (left, top, right, bottom

 Specifies the bounding rectangle, in logical units.

- color : int

 Specifies the color to use.

#### MFC References

- CDC::FillSolidRect


<!-- page: PyCDC__FrameRect_meth.html -->

## PyCDC.FrameRect

 FrameRect(rect, brush)

Draws a border around the rectangle specified by rect

#### Parameters

- rect : (left, top, right, bottom

 Specifies the bounding rectangle, in logical units.

- brush : PyCBrush

 Specifies the brush to use.

#### MFC References

- CDC::FrameRect


<!-- page: PyCDC__GetBrushOrg_meth.html -->

## PyCDC.GetBrushOrg

 (int,int) = GetBrushOrg()

Retrieves the origin (in device units) of the brush currently selected for the device context.

#### MFC References

- CDC::GetBrushOrg


<!-- page: PyCDC__GetClipBox_meth.html -->

## PyCDC.GetClipBox

 (left, top, right, bottom) = GetClipBox()

Retrieves the dimensions of the smallest bounding rectangle around the current clipping boundary.

#### MFC References

- CDC::GetClipBox

#### Return Value

A tuple of integers specifying the rectangle.


<!-- page: PyCDC__GetCurrentPosition_meth.html -->

## PyCDC.GetCurrentPosition

 (x, y) = GetCurrentPosition()

Retrieves the current position (in logical coordinates).


<!-- page: PyCDC__GetDeviceCaps_meth.html -->

## PyCDC.GetDeviceCaps

 int = GetDeviceCaps(index)

Retrieves a capability of the device context.

#### Parameters

- index : int

 The information requested. See the win32api documentation for details.

#### MFC References

- CDC::GetDeviceCaps

#### Return Value

The value of the requested capability


<!-- page: PyCDC__GetHandleAttrib_meth.html -->

## PyCDC.GetHandleAttrib

 int = GetHandleAttrib()

Retrieves the handle of the attribute device context.


<!-- page: PyCDC__GetHandleOutput_meth.html -->

## PyCDC.GetHandleOutput

 int = GetHandleOutput()

Retrieves the handle of the output device context.


<!-- page: PyCDC__GetMapMode_meth.html -->

## PyCDC.GetMapMode

 int = GetMapMode()

Gets the mapping mode for the device context.

#### MFC References

- CDC::GetMapMode


<!-- page: PyCDC__GetNearestColor_meth.html -->

## PyCDC.GetNearestColor

 int = GetNearestColor(color)

Returns the closest color a device can map.

#### Parameters

- color : int

 Specifies the color to be matched.


<!-- page: PyCDC__GetPixel_meth.html -->

## PyCDC.GetPixel

 GetPixel(x, y)

Gets a pixel at a local in a device context

#### Parameters

- x : int

 Horizontal coordinate.

- y : int

 Vertical coordinate.


<!-- page: PyCDC__GetSafeHdc_meth.html -->

## PyCDC.GetSafeHdc

 int = GetSafeHdc()

Returns the HDC of this DC object.

#### MFC References

- CDC::GetSafeHdc


<!-- page: PyCDC__GetTextExtentPoint_meth.html -->

## PyCDC.GetTextExtentPoint

 (x,y) = GetTextExtentPoint(text)

An alias for PyCDC::GetTextExtent. GetTextExtentPoint is the preferred win32api name, but GetTextExtent is the MFC name.
 Calculates the width and height of a line of text using the current font to determine the dimensions.

#### Parameters

- text : string

 The text to calculate for.

#### Return Value

A tuple of integers with the size of the string, in logical units.


<!-- page: PyCDC__GetTextExtent_meth.html -->

## PyCDC.GetTextExtent

 (x,y) = GetTextExtent(text)

Calculates the width and height of a line of text using the current font to determine the dimensions.

#### Parameters

- text : string

 The text to calculate for.

#### MFC References

- CFC::GetTextExtent

#### Return Value

A tuple of integers with the size of the string, in logical units.


<!-- page: PyCDC__GetTextFace_meth.html -->

## PyCDC.GetTextFace

 string = GetTextFace()

Returns typeface name of the current font.

#### MFC References

- CDC::GetTextFace


<!-- page: PyCDC__GetTextMetrics_meth.html -->

## PyCDC.GetTextMetrics

 dict = GetTextMetrics()

Retrieves the metrics for the current font in this device context.

#### MFC References

- CDC::GetTextMetrics

#### Return Value

A dictionary of integers, keyed by the following strings:
 tmHeight
 tmAscent
 tmDescent
 tmInternalLeading
 tmExternalLeading
 tmAveCharWidth
 tmMaxCharWidth
 tmWeight
 tmItalic
 tmUnderlined
 tmStruckOut
 tmFirstChar
 tmLastChar
 tmDefaultChar
 tmBreakChar
 tmPitchAndFamily
 tmCharSet
 tmOverhang
 tmDigitizedAspectX
 tmDigitizedAspectY


<!-- page: PyCDC__GetViewportExt_meth.html -->

## PyCDC.GetViewportExt

 x, y = GetViewportExt()

Gets the viewport extent of the device context


<!-- page: PyCDC__GetViewportOrg_meth.html -->

## PyCDC.GetViewportOrg

 x, y = GetViewportOrg()

Gets the viewport origin of the device context


<!-- page: PyCDC__GetWindowExt_meth.html -->

## PyCDC.GetWindowExt

 x, y = GetWindowExt()

Gets the window extent of the device context


<!-- page: PyCDC__GetWindowOrg_meth.html -->

## PyCDC.GetWindowOrg

 x, y = GetWindowOrg()

Retrieves the x- and y-coordinates of the origin of the window associated with the device context.


<!-- page: PyCDC__IntersectClipRect_meth.html -->

## PyCDC.IntersectClipRect

 IntersectClipRect(rect)

Creates a new clipping region by forming the intersection of the current region and the rectangle specified

#### Parameters

- rect : (left, top, right, bottom)

 Specifies the bounding rectangle, in logical units.

#### MFC References

- CDC::IntersectClipRect

#### Return Value

region type as integer


<!-- page: PyCDC__IsPrinting_meth.html -->

## PyCDC.IsPrinting

 int = IsPrinting()

Returns 1 if the DC is currently printing, else 0


<!-- page: PyCDC__LPtoDP_meth.html -->

## PyCDC.LPtoDP

 (x,y) = LPtoDP(point)

Converts logical units into device units.

#### Parameters

- point : (x,y)

 The point coordinate to convert.

#### Alternative Parameters

- x

 The x coordinate to convert.

- y

 The y coordinate to convert.

#### MFC References

- CDC::LPtoDP

#### Return Value

The converted coordinates.


<!-- page: PyCDC__LineTo_meth.html -->

## PyCDC.LineTo

 LineTo(point)

Draws a line to a specified point, using the currently selected pen.

#### Parameters

- point : (x,y)

 The point coordinate to draw to.

#### Alternative Parameters

- x

 The x coordinate to draw to.

- y

 The y coordinate to draw to.

#### MFC References

- CDC::LineTo


<!-- page: PyCDC__MoveTo_meth.html -->

## PyCDC.MoveTo

 (x,y) = MoveTo(point)

Moves the current position to a specified point.

#### Parameters

- point : (x,y)

 The point coordinate to move to.

#### Alternative Parameters

- x

 The x coordinate to move to.

- y

 The y coordinate to move to.

#### MFC References

- CDC::MoveTo

#### Return Value

The previous position.


<!-- page: PyCDC__OffsetViewportOrg_meth.html -->

## PyCDC.OffsetViewportOrg

 x, y = OffsetViewportOrg(x,y)

Modifies the coordinates of the viewport origin relative to the coordinates of the current viewport origin

#### Parameters

- x,y : int, int

 The new origin offset.

#### Return Value

The previous viewport origin as a tuple (x,y)


<!-- page: PyCDC__OffsetWindowOrg_meth.html -->

## PyCDC.OffsetWindowOrg

 x, y = OffsetWindowOrg(x,y)

Modifies the coordinates of the window origin relative to the coordinates of the current window origin.

#### Parameters

- x,y : int, int

 The new origin offset.

#### Return Value

The previous origin as a tuple (x,y)


<!-- page: PyCDC__PatBlt_meth.html -->

## PyCDC.PatBlt

 PatBlt(destPos, size, rop)

Creates a bit pattern on the device.

#### Parameters

- destPos : (x,y)-ints

 The logical x,y coordinates of the upper-left corner of the destination rectangle.

- size : (width, height)-ints

 Specifies the width and height (in logical units) of the destination rectangle and source bitmap.

- rop : int

 Specifies the raster operation to be performed. See the win32 api documentation for details.

#### MFC References

- CDC::BitBlt


<!-- page: PyCDC__Pie_meth.html -->

## PyCDC.Pie

 Pie(x1, y1, x2, y2, x3, y3, x4, y4)

Draws a pie slice in a device context

#### Parameters

- x1 : int

 X coordinate of upper left corner

- y1 : int

 Y coordinate of upper left corner

- x2 : int

 X coordinate of lower right corner

- y2 : int

 Y coordinate of lower right corner

- x3 : int

 X coordinate of starting point of arc

- y3 : int

 Y coordinate of starting point of arc

- x4 : int

 X coordinate of ending point of arc

- y4 : int

 Y coordinate of ending point of arc


<!-- page: PyCDC__PolyBezier_meth.html -->

## PyCDC.PolyBezier

 PolyBezier()

Draws one or more Bezier splines.


<!-- page: PyCDC__Polygon_meth.html -->

## PyCDC.Polygon

 Polygon(points)

Draws an Polygon.

#### Parameters

- points : [(x, y), ...]

 A sequence of points


<!-- page: PyCDC__Polyline_meth.html -->

## PyCDC.Polyline

 Polyline(points)

Draws a Polyline.

#### Parameters

- points : [(x, y), ...]

 A sequence of points


<!-- page: PyCDC__RealizePalette_meth.html -->

## PyCDC.RealizePalette

 int = RealizePalette()

Maps palette entries in the current logical palette to the system palette.

#### Return Value

Indicates how many entries in the logical palette were mapped to different entries in the system palette. This represents the number of entries that this function remapped to accommodate changes in the system palette since the logical palette was last realized.


<!-- page: PyCDC__RectVisible_meth.html -->

## PyCDC.RectVisible

 int = RectVisible(rect)

Determines whether any part of the given rectangle lies within the clipping region of the display context.

#### Parameters

- rect : (left, top, right, bottom)

 The coordinates of the reactangle to be checked.

#### MFC References

- CDC::RectVisible

#### Return Value

Non zero if any part of the rectangle lies within the clipping region, else zero.


<!-- page: PyCDC__Rectangle_meth.html -->

## PyCDC.Rectangle

 rc = Rectangle()

Draws a rectangle using the current pen. The interior of the rectangle is filled using the current brush.


<!-- page: PyCDC__RestoreDC_meth.html -->

## PyCDC.RestoreDC

 RestoreDC(saved)

Restores the state of the device context.

#### Parameters

- saved : int

 The id of a previously saved device context. See PyCDC::SaveDC

#### MFC References

- CDC::RestoreDC


<!-- page: PyCDC__SaveDC_meth.html -->

## PyCDC.SaveDC

 int = SaveDC()

Saves the current state of the device context. Windows manages a stack of state information. The saved device context can later be restored by using CDC::RestoreDC

#### MFC References

- CDC::SaveDC

#### Return Value

An integer identifying the context, which can be used by PyCDC::RestoreDC. An exception is raised if this function fails.


<!-- page: PyCDC__ScaleViewportExt_meth.html -->

## PyCDC.ScaleViewportExt

 x, y = ScaleViewportExt()

Modifies the viewport extents relative to the current values.


<!-- page: PyCDC__ScaleWindowExt_meth.html -->

## PyCDC.ScaleWindowExt

 x, y = ScaleWindowExt()

Modifies the window extents relative to the current values.


<!-- page: PyCDC__SelectClipRgn_meth.html -->

## PyCDC.SelectClipRgn

 obRgn = SelectClipRgn()

Selects the given region as the current clipping region for the device context

#### Return Value

The return value specifies the region's complexity (integer)


<!-- page: PyCDC__SelectObject_meth.html -->

## PyCDC.SelectObject

 object = SelectObject(ob)

Selects an object into the device context.
 Currently, only PyCFont, PyCBitMap, PyCBrush and PyCPen objects are supported.

#### Parameters

- ob : object

 The object to select.

#### MFC References

- CDC::SelectObject

#### Return Value

The previously selected object. This will be the same type as the object parameter.


<!-- page: PyCDC__SelectPalette_meth.html -->

## PyCDC.SelectPalette

 int = SelectPalette(hPalette, forceBackground )

Sets the logical palette.

#### Parameters

- hPalette : int

 The handle to the palette

- forceBackground : int

 Specifies whether the logical palette is forced to be a background palette.

#### MFC References

- CDC::SelectePalette

#### Return Value

The previous palette handle.


<!-- page: PyCDC__SetBkColor_meth.html -->

## PyCDC.SetBkColor

 int = SetBkColor(color)

Sets the current background color to the specified color.

#### Parameters

- color : int

 A windows color specification. See the win32api documentation for details.

#### Comments

 If the background mode is OPAQUE, the system uses the background color to fill the gaps in styled lines, the gaps between hatched lines in brushes, and the background in character cells. The system also uses the background color when converting bitmaps between color and monochrome device contexts.

#### MFC References

- CDC::SetBkColor

#### Return Value

The return value is the previous background color.


<!-- page: PyCDC__SetBkMode_meth.html -->

## PyCDC.SetBkMode

 int = SetBkMode(mode)

Sets the current background mode to the specified mode.

#### Parameters

- mode : int

 A background mode. May be either TRANSPARENT or OPAQUE.

#### Comments

 Specifies the mode to be set. This parameter can be either OPAQUE or TRANSPARENT

#### MFC References

- CDC::SetBkMode

#### Return Value

The return value is the previous background mode.


<!-- page: PyCDC__SetBrushOrg_meth.html -->

## PyCDC.SetBrushOrg

 (int, int) = SetBrushOrg(point)

Specifies the origin that GDI will assign to the next brush that the application selects into the device context.

#### Parameters

- point : (x,y)

 The new origin in device units.

#### MFC References

- CDC::SetBrushOrg

#### Return Value

The previous origin in device units.


<!-- page: PyCDC__SetGraphicsMode_meth.html -->

## PyCDC.SetGraphicsMode

 int = SetGraphicsMode(mode)

Sets the graphics mode for the specified device context

#### Parameters

- mode : int

 The new mode.


<!-- page: PyCDC__SetMapMode_meth.html -->

## PyCDC.SetMapMode

 int = SetMapMode(newMode)

Sets the mapping mode for the device context.

#### Parameters

- newMode : int

 The new mode. Can be one of MM_ANISOTROPIC, MM_HIENGLISH, MM_HIMETRIC, MM_ISOTROPIC, MM_LOENGLISH, MM_LOMETRIC, MM_TEXT, MM_TWIPS

#### MFC References

- CDC::SetMapMode

#### Return Value

The previous mapping mode.


<!-- page: PyCDC__SetPixel_meth.html -->

## PyCDC.SetPixel

 SetPixel(x, y, color)

Sets a pixel in a device context

#### Parameters

- x : int

 Horizontal coordinate.

- y : int

 Vertical coordinate.

- color : int

 The brush color.


<!-- page: PyCDC__SetPolyFillMode_meth.html -->

## PyCDC.SetPolyFillMode

 (int) = SetPolyFillMode(int)

Sets the polygon-filling mode.

#### Parameters

- int=1 : i

 The new mode, ALTERNATE (1) or WINDING (2).

#### MFC References

- CDC::SetPolyFillMode

#### Return Value

The previous PolyFillMode as integer

 The previous PolyFillMode.


<!-- page: PyCDC__SetROP2_meth.html -->

## PyCDC.SetROP2

 dict = SetROP2(mode)

Sets the current drawing mode.

#### Parameters

- mode : int

 The new drawing mode.

#### MFC References

- CDC::SetROP2


<!-- page: PyCDC__SetTextAlign_meth.html -->

## PyCDC.SetTextAlign

 int = SetTextAlign(newFlags)

Sets the text-alignment flags.

#### Parameters

- newFlags : int

 The new alignment flags. Can be a combination of (TA_CENTER, TA_LEFT, TA_RIGHT), (TA_BASELINE, TA_BOTTOM, TA_TOP) and (TA_NOUPDATECP, TA_UPDATECP)
 The default is TA_LEFT|TA_TOP|TA_NOUPDATECP

#### MFC References

- CDC::SetTextAlign

#### Return Value

The old alignment flags.


<!-- page: PyCDC__SetTextColor_meth.html -->

## PyCDC.SetTextColor

 int = SetTextColor(color)

Sets the text color to the specified color.

#### Parameters

- color : int

 A windows color specification. See the win32api documentation for details.

#### Comments

 This text color is used when writing text to this device context and also when converting bitmaps between color and monochrome device contexts. If the device cannot represent the specified color, the system sets the text color to the nearest physical color. The background color for a character is specified by the SetBkColor and SetBkMode member functions.

#### MFC References

- CDC::SetTextColor

#### Return Value

The return value is the previous text color.


<!-- page: PyCDC__SetViewportExt_meth.html -->

## PyCDC.SetViewportExt

 (x,y) = SetViewportExt(size)

Sets the x,y extents of the viewport of the device context.

#### Parameters

- size : (x,y)

 The new size.

#### MFC References

- CDC::SetViewportExt

#### Return Value

The previous extents of the viewport (in logical units).


<!-- page: PyCDC__SetViewportOrg_meth.html -->

## PyCDC.SetViewportOrg

 x, y = SetViewportOrg(x,y)

Sets the viewport origin of the device context

#### Parameters

- x,y : int, int

 The new origin.


<!-- page: PyCDC__SetWindowExt_meth.html -->

## PyCDC.SetWindowExt

 (x,y) = SetWindowExt(size)

Sets the x,y extents of the window associated with the device context.

#### Parameters

- size : (x,y)

 The new size.

#### MFC References

- CDC::SetWindowExt

#### Return Value

The previous extents of the window (in logical units).


<!-- page: PyCDC__SetWindowOrg_meth.html -->

## PyCDC.SetWindowOrg

 x, y = SetWindowOrg(x,y)

Sets the window origin of the device context

#### Parameters

- x,y : int, int

 The new origin.


<!-- page: PyCDC__SetWorldTransform_meth.html -->

## PyCDC.SetWorldTransform

 int = SetWorldTransform()

sets a two-dimensional linear transformation between world space and page space for the specified device context. This transformation can be used to scale, rotate, shear, or translate graphics output.


<!-- page: PyCDC__StartDoc_meth.html -->

## PyCDC.StartDoc

 StartDoc(docName, outputFile)

Starts spooling a document to a printer DC

#### Parameters

- docName : string

 The document name

- outputFile : string

 The output file name. Use this to spool to a file. Omit to send to the printer.


<!-- page: PyCDC__StartPage_meth.html -->

## PyCDC.StartPage

 StartPage()

Starts a new page on a printer DC


<!-- page: PyCDC__StretchBlt_meth.html -->

## PyCDC.StretchBlt

 StretchBlt(destPos, size, dc, srcPos, size, rop)

Copies a bitmap from the source device context to this device context.

#### Parameters

- destPos : (x,y)-ints

 The logical x,y coordinates of the upper-left corner of the destination rectangle.

- size : (width, height)-ints

 Specifies the width and height (in logical units) of the destination rectangle and source bitmap.

- dc : PyCDC

 Specifies the PyCDC object from which the bitmap will be copied. It must be None if rop specifies a raster operation that does not include a source.

- srcPos : (xSrc, ySrc)-ints

 Specifies the logical x,y coordinates of the upper-left corner of the source bitmap.

- size : (widthsrc, heightsrc)-ints

 Specifies the width and height (in logical units) of the destination rectangle and source bitmap.

- rop : int

 Specifies the raster operation to be performed. See the win32 api documentation for details.

#### MFC References

- CDC::StretchBlt


<!-- page: PyCDC__StrokeAndFillPath_meth.html -->

## PyCDC.StrokeAndFillPath

 StrokeAndFillPath()

Closes any open figures in a path, strokes the outline of the path by using the current pen, and fills its interior by using the current brush. The device context must contain a closed path.


<!-- page: PyCDC__StrokePath_meth.html -->

## PyCDC.StrokePath

 StrokePath()

Renders the specified path by using the current pen.


<!-- page: PyCDC__TextOut_meth.html -->

## PyCDC.TextOut

 TextOut(int, int, string)

Outputs text to the display context, using the currently selected font.

#### Parameters

- int : x

 The x coordinate to write the text to.

- int : y

 The y coordinate to write the text to.

- string : text

 The text to write.

#### MFC References

- CDC::TextOut

#### Return Value

Always none. If the function fails, an exception is raised.


---

<!-- object: PyCDialog -->


<!-- page: PyCDialog.html -->

---

## PyCDialog Object

 A class which encapsulates an MFC CDialog object. Derived from a PyCWnd object.

#### Methods

- CreateWindow

 Creates a modless window for the dialog.

- DoModal

 Creates a modal window for the dialog.

- EndDialog

 Closes a modal dialog.

- GotoDlgCtrl

 Sets focus to a specific control.

- MapDialogRect

 Converts the dialog-box units of a rectangle to screen units.

- OnCancel

 Calls the default MFC OnCancel handler.

- OnOK

 Calls the default MFC OnOK handler.

- OnInitDialog

 Calls the default MFC OnInitDialog handler. sentinel

#### Based On

PyCWnd


<!-- page: PyCDialog__CreateWindow_meth.html -->

## PyCDialog.CreateWindow

 CreateWindow(obParent)

Create a modeless window for the dialog box.

#### Parameters

- obParent=None : PyCWnd

 The parent window for the new window

#### MFC References

- CDialog::CreateIndirect


<!-- page: PyCDialog__DoModal_meth.html -->

## PyCDialog.DoModal

 int = DoModal()

Create a modal window for the dialog box.

#### MFC References

- CDialog::DoModal

#### Return Value

The return value from the dialog. This is the value passed to PyCDialog::EndDialog.


<!-- page: PyCDialog__EndDialog_meth.html -->

## PyCDialog.EndDialog

 EndDialog(result)

Ends a modal dialog box.

#### Parameters

- result : int

 The value to be returned by the PyCDialog::DoModal method.

#### MFC References

- CDialog::EndDialog


<!-- page: PyCDialog__GotoDlgCtrl_meth.html -->

## PyCDialog.GotoDlgCtrl

 GotoDlgCtrl(control)

Moves the focus to the specified control in the dialog box.

#### Parameters

- control : PyCWnd

 The control to get the focus.


<!-- page: PyCDialog__MapDialogRect_meth.html -->

## PyCDialog.MapDialogRect

 (left, top, right, bottom) = MapDialogRect(rect)

Converts the dialog-box units of a rectangle to screen units.

#### Parameters

- rect : (left, top, right, bottom)

 The rect to be converted


<!-- page: PyCDialog__OnCancel_meth.html -->

## PyCDialog.OnCancel

 OnCancel()

Calls the default MFC OnCancel handler.

#### See Also

- PyCDialog.OnCancel virtual method


<!-- page: PyCDialog__OnCancel_virtual.html -->

## PyCDialog.OnCancel Virtual

 OnCancel()

Called by the MFC architecture when the user selects the Cancel button.

#### Comments

 The procedure is expected to dismiss the window with the PyCDialog::EndDialog method. The base implementation (which dismisses the dialog) is not called if a handler exists. This can be done via PyCDialog::OnCancel.

#### See Also

- PyCDialog::OnCancel


<!-- page: PyCDialog__OnInitDialog_meth.html -->

## PyCDialog.OnInitDialog

 int = OnInitDialog()

Calls the default MFC OnInitDialog handler.

#### See Also

- PyCDialog.OnInitDialog virtual method


<!-- page: PyCDialog__OnInitDialog_virtual.html -->

## PyCDialog.OnInitDialog Virtual

 OnInitDialog()

Override to augment dialog-box initialization.

#### Comments

 The base implementation is not called if a handler exists. This can be done via PyCDialog::OnInitDialog.

#### See Also

- PyCDialog::OnInitDialog

#### Return Value

Specifies whether the application has set the input focus to one of the controls in the dialog box. If OnInitDialog returns nonzero, Windows sets the input focus to the first control in the dialog box. The application can return 0/None only if it has explicitly set the input focus to one of the controls in the dialog box.


<!-- page: PyCDialog__OnOK_meth.html -->

## PyCDialog.OnOK

 OnOK()

Calls the default MFC OnOK handler.

#### See Also

- PyCDialog.OnOK virtual method


<!-- page: PyCDialog__OnOK_virtual.html -->

## PyCDialog.OnOK Virtual

 OnOK()

Called by the MFC architecture when the user selects the OK button.

#### Comments

 The procedure is expected to dismiss the window with the PyCDialog::EndDialog method. The base implementation (which dismisses the dialog) is not called if a handler exists. This can be done via PyCDialog::OnOK.

#### See Also

- PyCDialog::OnOK


---

<!-- object: PyCDialogBar -->


<!-- page: PyCDialogBar.html -->

---

## PyCDialogBar Object

 A class which encapsulates an MFC CDialogBar . Derived from a PyCControlBar object.

#### Methods

- CreateWindow

 Creates the window for the PyCDialogBar object.


<!-- page: PyCDialogBar__CreateWindow_meth.html -->

## PyCDialogBar.CreateWindow

 CreateWindow(parent, template, style, id)

Creates the window for the PyCDialogBar object.

#### Parameters

- parent : PyCWnd

 The parent window

- template : PyResourceId

 Template name or integer resource id

- style : int

 The style for the window

- id : int

 The ID of the window


---

<!-- object: PyCDocTemplate -->


<!-- page: PyCDocTemplate.html -->

---

## PyCDocTemplate Object

 A document template class. Encapsulates an MFC CDocTemplate class

#### Methods

- DoCreateDoc

 Creates an underlying document object.

- FindOpenDocument

 Returns an existing document with the specified file name.

- GetDocString

 Retrieves a specific substring describing the document type.

- GetDocumentList

 Return a list of all open documents.

- GetResourceID

 Returns the resource ID in use.

- GetSharedMenu

 Returns the shared menu object for all frames using this template.

- InitialUpdateFrame

 Calls the default OnInitialFrame handler.

- SetContainerInfo

 Sets the resources to be used when an OLE 2 object is in-place activated.

- SetDocStrings

 Assigns the document strings for the template.

- OpenDocumentFile

 Opens a document file, creating a view and frame.


<!-- page: PyCDocTemplate__CreateNewDocument_virtual.html -->

## PyCDocTemplate.CreateNewDocument Virtual

 CreateNewDocument()

Called to create a new document object.


<!-- page: PyCDocTemplate__CreateNewFrame_virtual.html -->

## PyCDocTemplate.CreateNewFrame Virtual

 CreateNewFrame()

Called to create a new frame window.


<!-- page: PyCDocTemplate__DoCreateDoc_meth.html -->

## PyCDocTemplate.DoCreateDoc

 PyCDocument = DoCreateDoc(fileName)

Creates an underlying document object.

#### Parameters

- fileName=None : string

 The name of the file to load.


<!-- page: PyCDocTemplate__FindOpenDocument_meth.html -->

## PyCDocTemplate.FindOpenDocument

 PyCDocument = FindOpenDocument(fileName)

Returns an existing document with the specified file name.

#### Parameters

- fileName : string

 The fully qualified filename to search for.


<!-- page: PyCDocTemplate__GetDocString_meth.html -->

## PyCDocTemplate.GetDocString

 string = GetDocString(docIndex)

Retrieves a specific substring describing the document type.

#### Parameters

- docIndex : int

 The document index. Must be one of the win32ui.CDocTemplate_* constants.

#### Comments

 For more information on the doc strings, please see PyCDocTemplate::SetDocStrings


<!-- page: PyCDocTemplate__GetDocumentList_meth.html -->

## PyCDocTemplate.GetDocumentList

 list = GetDocumentList()

Return a list of all open documents.


<!-- page: PyCDocTemplate__GetResourceID_meth.html -->

## PyCDocTemplate.GetResourceID

 GetResourceID()

Returns the resource ID in use.


<!-- page: PyCDocTemplate__GetSharedMenu_meth.html -->

## PyCDocTemplate.GetSharedMenu

 PyCMenu = GetSharedMenu()

Returns the shared menu object for all frames using this template.

#### MFC References

- CWnd::m_hMenuShared


<!-- page: PyCDocTemplate__InitialUpdateFrame_meth.html -->

## PyCDocTemplate.InitialUpdateFrame

 InitialUpdateFrame(frame, doc, bMakeVisible)

Calls the default OnInitialFrame handler.

#### Parameters

- frame=None : PyCFrameWnd

 The frame window.

- doc=None : PyCDocument

 A document for the frame.

- bMakeVisible=1 : int

 Indicates of the frame should be shown.

#### See Also

- PyCDocTemplate.InitialUpdateFrame virtual method


<!-- page: PyCDocTemplate__InitialUpdateFrame_virtual.html -->

## PyCDocTemplate.InitialUpdateFrame Virtual

 InitialUpdateFrame(frame, frame , bMakeVisible )

Called to perform the initial frame update. The default behaviour is to call OnInitialUpdate on all views.

#### Parameters

- frame : PyCFrameWnd

 The frame window.

- frame : PyCDocument

 The document attached to the frame.

- bMakeVisible : int

 Indicates if the frame should be made visible.


<!-- page: PyCDocTemplate__MatchDocType_virtual.html -->

## PyCDocTemplate.MatchDocType Virtual

 MatchDocType(fileName, fileType )

Queries if the template can open the specified file name.

#### Parameters

- fileName : string

 The name of the file to open.

- fileType : int

 Only used on the mac.

#### Comments

 This method should call PyCDocTemplate.FindOpenDocument to return an already open document if one exists, else it should return one of the win32ui.CDocTemplate_Confidence_* constants.


<!-- page: PyCDocTemplate__OpenDocumentFile_meth.html -->

## PyCDocTemplate.OpenDocumentFile

 OpenDocumentFile(filename, bMakeVisible)

Opens a document file, creating a view and frame.

#### Parameters

- filename : string

 Name of file to open, or None

- bMakeVisible=1 : int

 Indicates if the document should be created visible.


<!-- page: PyCDocTemplate__OpenDocumentFile_virtual.html -->

## PyCDocTemplate.OpenDocumentFile Virtual

 OpenDocumentFile()

Called when a document file is to be opened.


<!-- page: PyCDocTemplate__SetContainerInfo_meth.html -->

## PyCDocTemplate.SetContainerInfo

 SetContainerInfo(id)

Sets the resources to be used when an OLE 2 object is in-place activated.

#### Parameters

- id : int

 The resource ID.


<!-- page: PyCDocTemplate__SetDocStrings_meth.html -->

## PyCDocTemplate.SetDocStrings

 SetDocStrings(docStrings)

Assigns the document strings for the template.

#### Parameters

- docStrings : string

 The document strings.

#### Comments

 The string must be a \\n separated list of docstrings. The elements are:

| | elementName | Description
| |

---

 |

---

| | windowTitle | Title used for the window (only for SDI applications)
| | docName | Root for the default document name.
| | fileNewName | Name of the document type, as displayed in the "File/New" dialog
| | filterName | Description of the document type and a wildcard spec for the file open dialog.
| | filterExt | Extension for documents of this file type.
| | regFileTypeId | Internal Id of the document as registered in the registry. Used to associate the extension with the file type.
| | regFileTypeName | Name of the document, as stored in the registry. This is the name presented to the user.


---

<!-- object: PyCDockContext -->


<!-- page: PyCDockContext.html -->

---

## PyCDockContext Object

 A class which encapsulates an MFC CDockContext object

#### Methods

- EndDrag

- StartDrag

- EndResize

- StartResize

- ToggleDocking

#### Properties

- x,y ptLast

- left, top, right, bottom rectLast

- cx, cy sizeLast

- int bDitherLast

- left, top, right, bottom rectDragHorz

- left, top, right, bottom rectDragVert

- left, top, right, bottom rectFrameDragHorz

- left, top, right, bottom rectFrameDragVert

- int dwDockStyle
 allowable dock styles for bar

- int dwOverDockStyle
 style of dock that rect is over

- int dwStyle
 style of control bar

- int bFlip
 if shift key is down

- int bForceFrame
 if ctrl key is down CDC* m_pDC; // where to draw during drag

- int bDragging

- int nHitTest

- int uMRUDockID

- left, top, right, bottom rectMRUDockPos

- int dwMRUFloatStyle

- x,y ptMRUFloatPos
 Sentinel


<!-- page: PyCDockContext__EndDrag_meth.html -->

## PyCDockContext.EndDrag

 int = EndDrag()


<!-- page: PyCDockContext__EndResize_meth.html -->

## PyCDockContext.EndResize

 int = EndResize()


<!-- page: PyCDockContext__StartDrag_meth.html -->

## PyCDockContext.StartDrag

 int = StartDrag(pt)

#### Parameters

- pt : int, int


<!-- page: PyCDockContext__StartResize_meth.html -->

## PyCDockContext.StartResize

 int = StartResize(hittest, pt )

#### Parameters

- hittest : int

- pt : int, int


<!-- page: PyCDockContext__ToggleDocking_meth.html -->

## PyCDockContext.ToggleDocking

 int = ToggleDocking()


---

<!-- object: PyCDocument -->


<!-- page: PyCDocument.html -->

---

## PyCDocument Object

 A document class. Encapsulates an MFC CDocument class

#### Methods

- DeleteContents

 Call the MFC DeleteContents method.

- DoSave

 Save the file. If necessary, prompt for file name.

- DoFileSave

 Check file attributes, and save the file.

- GetDocTemplate

 Returns the PyCDocTemplate for the document.

- GetAllViews

 Returns a list of all views for the current document.

- GetFirstView

 Returns the first view object attached to this document.

- GetPathName

 Returns the full path name of the current document.

- GetTitle

 Returns the title of the current document.

- IsModified

 Return a flag indicating if the document has been modified.

- OnChangedViewList

 Informs the document when a view is added or removed.

- OnCloseDocument

 Call the MFC OnCloseDocument handler.

- OnNewDocument

 Call the MFC OnNewDocument handler.

- OnOpenDocument

 Call the MFC OnOpenDocument handler.

- OnSaveDocument

 Call the MFC OnSaveDocument handler.

- SetModifiedFlag

 Set the "dirty" flag for the document.

- SaveModified

 Call the underlying MFC method.

- SetPathName

 Set the full path name for the document.

- SetTitle

 Set the title of the document.

- UpdateAllViews

 Informs each view when a document changes. sentinel

#### Based On

PyCCmdTarget


<!-- page: PyCDocument__DeleteContents_meth.html -->

## PyCDocument.DeleteContents

 DeleteContents()

Call the MFC DeleteContents method. This routine is provided so a document object which overrides this method can call the original MFC version if required.

#### See Also

- PyCDocument.DeleteContents virtual method

#### MFC References

- CDocument::DeleteContents


<!-- page: PyCDocument__DeleteContents_virtual.html -->

## PyCDocument.DeleteContents Virtual

 DeleteContents()

Called by the MFC architecture when a document is newly created or closed.

#### Comments

 If a handler is defined for this function, the base (MFC) function will not be called. If necessary, the handler must call this function explicitly.

#### See Also

- PyCDocument::DeleteContents


<!-- page: PyCDocument__DoFileSave_meth.html -->

## PyCDocument.DoFileSave

 DoFileSave()

Checks the file attributes. If the file is read only, a new name is prompted, else the file is saved (by calling DoSave)

#### See Also

- PyCDocument.DoFileSave virtual method

#### Undocumented MFC References

- CDocument::DoFileSave


<!-- page: PyCDocument__DoFileSave_virtual.html -->

## PyCDocument.DoFileSave Virtual

 DoFileSave()

Called by the MFC architecture.

#### Comments

 If a handler is defined for this function, it must call the base class PyCDocument::DoFileSave method.

#### See Also

- PyCDocument::DoFileSave

#### Return Value

TRUE if the document could be saved, else FALSE.


<!-- page: PyCDocument__DoSave_meth.html -->

## PyCDocument.DoSave

 DoSave(fileName, bReplace)

Calls the underlying MFC DoSave method.

#### Parameters

- fileName : string

 The name of the file to save to.

- bReplace=1 : int

 Should an existing file be silently replaced?.

#### Comments

 If invalid or no filename, will prompt for a name, else will perform the actual saving of the document.

#### See Also

- PyCDocument.DoSave virtual method

#### Undocumented MFC References

- CDocument::DoSave


<!-- page: PyCDocument__DoSave_virtual.html -->

## PyCDocument.DoSave Virtual

 DoSave(fileName, bReplace )

Called by the MFC architecture to save a document.

#### Parameters

- fileName : string

 The name of the file being saved.

- bReplace : int

 TRUE if the file should be replaced.

#### Comments

 If a handler is defined for this function, it must call the base class PyCDocument::DoSave method.

#### See Also

- PyCDocument::DoSave

#### Return Value

TRUE if the document could be saved, else FALSE.


<!-- page: PyCDocument__GetAllViews_meth.html -->

## PyCDocument.GetAllViews

 [PyCView,...] = GetAllViews()

Returns a list of all views for the current document.

#### MFC References

- CDocument::GetFirstViewPosition

- CDocument::GetNextView


<!-- page: PyCDocument__GetDocTemplate_meth.html -->

## PyCDocument.GetDocTemplate

 PyCDocTemplate = GetDocTemplate()

Returns the template for the document.

#### MFC References

- CDocument::GetDocTemplate


<!-- page: PyCDocument__GetFirstView_meth.html -->

## PyCDocument.GetFirstView

 PyCView = GetFirstView()

Returns the first view object attached to this document.

#### Comments

 For more info, see PyCDocument::GetAllViews shouldn't be possible.

#### MFC References

- CDocument::GetFirstViewPosition

- CDocument::GetNextView


<!-- page: PyCDocument__GetPathName_meth.html -->

## PyCDocument.GetPathName

 string = GetPathName()

Returns the full path name of the current document. The string will be empty if no path name has been set.

#### MFC References

- CDocument::GetPathName


<!-- page: PyCDocument__GetTitle_meth.html -->

## PyCDocument.GetTitle

 string = GetTitle()

Returns the title of the current document. This will often be the file name portion of the path name.

#### MFC References

- CDocument::GetTitle


<!-- page: PyCDocument__IsModified_meth.html -->

## PyCDocument.IsModified

 int = IsModified()

Return a flag indicating if the document has been modified.

#### MFC References

- CDocument::IsModified


<!-- page: PyCDocument__OnChangedViewList_meth.html -->

## PyCDocument.OnChangedViewList

 OnChangedViewList()

Informs the document when a view is added or removed.


<!-- page: PyCDocument__OnChangedViewList_virtual.html -->

## PyCDocument.OnChangedViewList Virtual

 OnChangedViewList()

Called by the MFC architecture when after a view is attached.

#### Comments

 If a handler is defined for this function, the base (MFC) function will not be called. If necessary, the handler must call this function explicitly.

#### See Also

- PyCDocument::OnChangedViewList


<!-- page: PyCDocument__OnCloseDocument_meth.html -->

## PyCDocument.OnCloseDocument

 OnCloseDocument()

Call the MFC OnCloseDocument handler. This routine is provided so a document object which overrides this method can call the original MFC version if required.

#### See Also

- PyCDocument.OnCloseDocument virtual method

#### MFC References

- CDocument::OnCloseDocument


<!-- page: PyCDocument__OnCloseDocument_virtual.html -->

## PyCDocument.OnCloseDocument Virtual

 OnCloseDocument()

Called by the MFC architecture.

#### Comments

 If a handler is defined for this function, the base (MFC) function will not be called. If necessary, the handler must call this function explicitly.

#### See Also

- PyCDocument::OnCloseDocument


<!-- page: PyCDocument__OnNewDocument_meth.html -->

## PyCDocument.OnNewDocument

 OnNewDocument()

Call the MFC OnNewDocument handler. This routine is provided so a document object which overrides this method can call the original MFC version if required.

#### See Also

- PyCDocument.OnNewDocument virtual method

#### MFC References

- CDocument::OnNewDocument


<!-- page: PyCDocument__OnNewDocument_virtual.html -->

## PyCDocument.OnNewDocument Virtual

 OnNewDocument()

Called by the MFC architecture.

#### Comments

 If a handler is defined for this function, the base (MFC) function will not be called. If necessary, the handler must call this function explicitly.

#### See Also

- PyCDocument::OnNewDocument

#### Return Value

TRUE if a new document could be created, else FALSE.


<!-- page: PyCDocument__OnOpenDocument_meth.html -->

## PyCDocument.OnOpenDocument

 OnOpenDocument(pathName)

Call the MFC OnOpenDocument handler. This routine is provided so a document object which overrides this method can call the original MFC version if required.

#### Parameters

- pathName : string

 The full path of the file to open.

#### MFC References

- CDocument::OnOpenDocument


<!-- page: PyCDocument__OnOpenDocument_virtual.html -->

## PyCDocument.OnOpenDocument Virtual

 OnOpenDocument(fileName)

Called by the MFC architecture.

#### Parameters

- fileName : string

 The name of the file being opened.

#### Comments

 If a handler is defined for this function, the base (MFC) function will not be called. If necessary, the handler must call this function explicitly.

#### See Also

- PyCDocument::OnOpenDocument

#### Return Value

TRUE if the document could be opened, else FALSE.


<!-- page: PyCDocument__OnSaveDocument_meth.html -->

## PyCDocument.OnSaveDocument

 OnSaveDocument(pathName)

Call the MFC OnSaveDocument handler. This routine is provided so a document object which overrides this method can call the original MFC version if required.

#### Parameters

- pathName : string

 The full path of the file to save.

#### MFC References

- CDocument::OnSaveDocument


<!-- page: PyCDocument__OnSaveDocument_virtual.html -->

## PyCDocument.OnSaveDocument Virtual

 OnSaveDocument(fileName)

Called by the MFC architecture.

#### Parameters

- fileName : string

 The name of the file being saved.

#### Comments

 If a handler is defined for this function, the base (MFC) function will not be called. If necessary, the handler must call this function explicitly.

#### See Also

- PyCDocument::OnSaveDocument

#### Return Value

TRUE if the document could be saved, else FALSE.


<!-- page: PyCDocument__PreCloseFrame_virtual.html -->

## PyCDocument.PreCloseFrame Virtual

 PreCloseFrame()

Called before the frame window is closed.

#### Comments

 The MFC base implementation is always called after the Python handler returns.


<!-- page: PyCDocument__SaveModified_meth.html -->

## PyCDocument.SaveModified

 int = SaveModified()

Call the underlying MFC method.

#### See Also

- PyCDocument.SaveModified virtual method

#### MFC References

- CDocument::SaveModified

#### Return Value

Nonzero if it is safe to continue and close the document; 0 if the document should not be closed.


<!-- page: PyCDocument__SaveModified_virtual.html -->

## PyCDocument.SaveModified Virtual

 SaveModified()

Called by the MFC architecture when a document is closed.

#### Comments

 If a handler is defined for this function, the base (MFC) function will not be called. If necessary, the handler must call this function explicitly.

#### See Also

- PyCDocument::SaveModified

#### Return Value

The handler should return TRUE if it is safe to continue and close the document; 0 if the document should not be closed.


<!-- page: PyCDocument__SetModifiedFlag_meth.html -->

## PyCDocument.SetModifiedFlag

 SetModifiedFlag(bModified)

Set the "dirty" flag for the document.

#### Parameters

- bModified=1 : int

 Set dirty flag

#### MFC References

- CDocument::SetModifiedFlag


<!-- page: PyCDocument__SetPathName_meth.html -->

## PyCDocument.SetPathName

 SetPathName(path)

Set the full path name for the document.

#### Parameters

- path : string

 The full path of the file.

#### MFC References

- CDocument::SetPathName


<!-- page: PyCDocument__SetTitle_meth.html -->

## PyCDocument.SetTitle

 SetTitle(title)

Set the title of the document (ie, the name to appear in the window caption for the document.

#### Parameters

- title : string

 The new title.

#### MFC References

- CDocument::SetTitle


<!-- page: PyCDocument__UpdateAllViews_meth.html -->

## PyCDocument.UpdateAllViews

 UpdateAllViews(sender, hint)

Informs each view when a document changes.

#### Parameters

- sender : PyCView

 The view who initiated the update

- hint=None : object

 A hint for the update.

#### MFC References

- CDocument::UpdateAllViews


---

<!-- object: PyCERTSTORE -->


<!-- page: PyCERTSTORE.html -->

---

## PyCERTSTORE Object

 Handle to a certificate store

#### Methods

- CertCloseStore

 Closes the certificate store

- CertControlStore

 Controls synchronization of the certificate store

- CertEnumCertificatesInStore

 Lists all certificates in the store

- CertEnumCTLsInStore

 Finds all Certificate Trust Lists in store.

- CertSaveStore

 Serializes the store to memory or a file

- CertAddEncodedCertificateToStore

 Imports an encoded certificate into the store

- CertAddCertificateContextToStore

 Adds a certificate context to the store

- CertAddCertificateLinkToStore

 Adds a link to a cert in another store

- CertAddCTLContextToStore

 Adds a certificate trust list to the store

- CertAddCTLLinkToStore

 Adds a link to a CTL in another store

- CertAddStoreToCollection

 Adds a sibling store to a store collection

- CertRemoveStoreFromCollection

 Removes a sibling store from a store collection

- PFXExportCertStoreEx

 Exports certificates and associated private keys in PKCS#12 format

#### Properties

- int HCERTSTORE
 Integer handle


<!-- page: PyCERTSTORE__CertAddCTLContextToStore_meth.html -->

## PyCERTSTORE.CertAddCTLContextToStore

 PyCTL_CONTEXT = CertAddCTLContextToStore(CtlContext, AddDisposition )

Adds a certificate trust list to the store

#### Parameters

- CtlContext : PyCTL_CONTEXT

 CTL to be added

- AddDisposition : int

 CERT_STORE_ADD_* constant


<!-- page: PyCERTSTORE__CertAddCTLLinkToStore_meth.html -->

## PyCERTSTORE.CertAddCTLLinkToStore

 PyCTL_CONTEXT = CertAddCTLLinkToStore(CtlContext, AddDisposition )

Adds a link to a CTL in another store

#### Parameters

- CtlContext : PyCTL_CONTEXT

 CTL to be linked

- AddDisposition : int

 One of the CERT_STORE_ADD_* values


<!-- page: PyCERTSTORE__CertAddCertificateContextToStore_meth.html -->

## PyCERTSTORE.CertAddCertificateContextToStore

 PyCERT_CONTEXT = CertAddCertificateContextToStore(CertContext, AddDisposition )

Adds a certificate context to the store

#### Parameters

- CertContext : PyCERT_CONTEXT

 Certificate context to be added

- AddDisposition : int

 CERT_STORE_ADD_* constant


<!-- page: PyCERTSTORE__CertAddCertificateLinkToStore_meth.html -->

## PyCERTSTORE.CertAddCertificateLinkToStore

 PyCERT_CONTEXT = CertAddCertificateLinkToStore(CertContext, AddDisposition )

Adds a link to a cert in another store

#### Parameters

- CertContext : PyCERT_CONTEXT

 Certificate context to be linked

- AddDisposition : int

 One of the CERT_STORE_ADD_* values


<!-- page: PyCERTSTORE__CertAddEncodedCertificateToStore_meth.html -->

## PyCERTSTORE.CertAddEncodedCertificateToStore

 PyCERT_CONTEXT = CertAddEncodedCertificateToStore(CertEncodingType, CertEncoded , AddDisposition )

Imports an encoded certificate into the store

#### Parameters

- CertEncodingType : int

 Usually X509_ASN_ENCODING combined with PKCS_7_ASN_ENCODING

- CertEncoded : buffer

 Data containing a serialized certificate

- AddDisposition : int

 Combination of CERT_STORE_ADD_* flags


<!-- page: PyCERTSTORE__CertAddStoreToCollection_meth.html -->

## PyCERTSTORE.CertAddStoreToCollection

 CertAddStoreToCollection(SiblingStore, UpdateFlag, Priority)

Adds a sibling store to a store collection

#### Parameters

- SiblingStore : PyCERTSTORE

 Store to be added to the collection

- UpdateFlag=0 : int

 Can be CERT_PHYSICAL_STORE_ADD_ENABLE_FLAG to enable changes to persist

- Priority=0 : int

 Determines order in which store are searched and updated

#### Comments

 A collection store is created by using cryptoapi::CertOpenStore with CERT_STORE_PROV_COLLECTION


<!-- page: PyCERTSTORE__CertCloseStore_meth.html -->

## PyCERTSTORE.CertCloseStore

 CertCloseStore()

Closes the certificate store

#### Comments

 Note that in general, it should not be necessary to call this - it will be called automatically when the Python object dies.

 Note that the Flags param is not supported - if you attempt to force-close the store and Python certificate objects remain alive, the program will crash as those objects are closed. The underlying Windows function is always called with CERT_CLOSE_STORE_CHECK_FLAG. This means that this function is likely to fail with CRYPT_E_PENDING_CLOSE if any such Python objects remain alive (in which case, this function would certainly have crashed the process if CERT_CLOSE_STORE_FORCE_FLAG was able to be specified)


<!-- page: PyCERTSTORE__CertControlStore_meth.html -->

## PyCERTSTORE.CertControlStore

 CertControlStore(Flags, CtrlType, CtrlPara)

Controls synchronization of the certificate store

#### Parameters

- Flags : int

 One of the CERT_STORE_CTRL_*_FLAG flags

- CtrlType : int

 One of the CERT_STORE_CTRL_* flags

- CtrlPara : PyHANDLE

 Event handle, can be None (not used with CERT_STORE_CTRL_COMMIT)


<!-- page: PyCERTSTORE__CertEnumCTLsInStore_meth.html -->

## PyCERTSTORE.CertEnumCTLsInStore

 [PyCTL_CONTEXT,...] = CertEnumCTLsInStore()

Finds all Certificate Trust Lists in store


<!-- page: PyCERTSTORE__CertEnumCertificatesInStore_meth.html -->

## PyCERTSTORE.CertEnumCertificatesInStore

 [PyCERT_CONTEXT,...] = CertEnumCertificatesInStore()

Lists all certificates in the store


<!-- page: PyCERTSTORE__CertRemoveStoreFromCollection_meth.html -->

## PyCERTSTORE.CertRemoveStoreFromCollection

 CertRemoveStoreFromCollection(SiblingStore)

Removes a sibling store from a collection

#### Parameters

- SiblingStore : PyCERTSTORE

 Store to be removed from the collection


<!-- page: PyCERTSTORE__CertSaveStore_meth.html -->

## PyCERTSTORE.CertSaveStore

 CertSaveStore(MsgAndCertEncodingType, SaveAs, SaveTo, SaveToPara, Flags)

Serializes the store to memory or a file

#### Parameters

- MsgAndCertEncodingType : int

 Only used when saveas is CERT_STORE_SAVE_AS_PKCS7 - usually X509_ASN_ENCODING combined with PKCS_7_ASN_ENCODING

- SaveAs : int

 One of the CERT_STORE_SAVE_AS_* constants

- SaveTo : int

 One of the CERT_STORE_SAVE_TO_* constants (CERT_STORE_SAVE_TO_MEMORY not supported yet)

- SaveToPara : PyHANDLE/string

 File name or open file handle depending on SaveTo parm

- Flags=0 : int

 Reserved, use 0


<!-- page: PyCERTSTORE__PFXExportCertStoreEx_meth.html -->

## PyCERTSTORE.PFXExportCertStoreEx

 bytes = PFXExportCertStoreEx(Password, Flags )

Exports certificates and associated private keys in PKCS#12 format

#### Parameters

- Password=None : str

 Passphrase to be used to encrypt the output

- Flags=EXPORT_PRIVATE_KEYS|REPORT_NO_PRIVATE_KEY|REPORT_NOT_ABLE_TO_EXPORT_PRIVATE_KEY : int

 Options to be used while exporting


---

<!-- object: PyCERT_ALT_NAME_ENTRY -->


<!-- page: PyCERT_ALT_NAME_ENTRY.html -->

---

## PyCERT_ALT_NAME_ENTRY Object

 Represented as a 2-tuple

#### Comments

 First item is one of the CERT_ALT_NAME_* constants indicating the type.
Second item is either a string, or for CERT_ALT_NAME_OTHER_NAME a PyCERT_OTHER_NAME


---

<!-- object: PyCERT_ALT_NAME_INFO -->


<!-- page: PyCERT_ALT_NAME_INFO.html -->

---

## PyCERT_ALT_NAME_INFO Object

 Sequence of PyCERT_ALT_NAME_ENTRY objects


---

<!-- object: PyCERT_AUTHORITY_KEY_ID_INFO -->


<!-- page: PyCERT_AUTHORITY_KEY_ID_INFO.html -->

---

## PyCERT_AUTHORITY_KEY_ID_INFO Object

 Dict containing the identity of a CA

#### Properties

- str KeyId
 Unique identifier of private key, usually a hash

- str CertIssuer
 Encoded DN of the Certificate Authority. Decode using X509_UNICODE_NAME

- int CertSerialNumber
 Serial nbr of the CA's signing certificate


---

<!-- object: PyCERT_BASIC_CONSTRAINTS2_INFO -->


<!-- page: PyCERT_BASIC_CONSTRAINTS2_INFO.html -->

---

## PyCERT_BASIC_CONSTRAINTS2_INFO Object

 Dict representing a CERT_BASIC_CONSTRAINTS2_INFO struct

#### Properties

- boolean fCA
 Indicates if cert represents a certificate authority

- boolean fPathLenConstraint
 Indicates if PathLenConstraint member is used

- int PathLenConstraint
 Limits number of intermediate CA's between root CA and end user


---

<!-- object: PyCERT_BASIC_CONSTRAINTS_INFO -->


<!-- page: PyCERT_BASIC_CONSTRAINTS_INFO.html -->

---

## PyCERT_BASIC_CONSTRAINTS_INFO Object

 Dict representing a CERT_BASIC_CONSTRAINTS_INFO struct

#### Properties

- PyCRYPT_BIT_BLOB SubjectType
 Contains a combination of CERT_CA_SUBJECT_FLAG,CERT_END_ENTITY_SUBJECT_FLAG

- boolean fPathLenConstraint
 Indicates if PathLenConstraint member is used

- int PathLenConstraint
 Limits number of intermediate CA's between root CA and end user

- tuple SubtreesConstraint
 Sequence of encoded name blobs


---

<!-- object: PyCERT_CONTEXT -->


<!-- page: PyCERT_CONTEXT.html -->

---

## PyCERT_CONTEXT Object

 Handle to a certificate context

#### Methods

- CertFreeCertificateContext

 Frees the context handle

- CertEnumCertificateContextProperties

 Lists property ids for the certificate

- CryptAcquireCertificatePrivateKey

 Retrieves the private key associated with the certificate

- CertGetIntendedKeyUsage

 Returns the intended key usage from the certificate extensions

- CertGetEnhancedKeyUsage

 Finds the enhanced key usage property and/or extension for the certificate

- CertSerializeCertificateStoreElement

 Serializes the certificate and its properties

- CertVerifySubjectCertificateContext

 Checks the validity of the certificate

- CertDeleteCertificateFromStore

 Removes the certificate from its store

- CertGetCertificateContextProperty

 Retrieves the specified property from the certificate

- CertSetCertificateContextProperty

 Sets a property for a certificate

#### Properties

- int HANDLE
 Pointer to CERT_CONTEXT struct

- PyCERTSTORE CertStore
 Handle to the certificate store that contains this certificate

- str CertEncoded
 Content of the certificate as encoded bytes

- int CertEncodingType
 Method used to encode the certifcate, usually X509_ASN_ENCODING or PKCS_7_ASN_ENCODING

- int Version
 One of the CERT_V* values

- PyUnicode Subject
 Encoded CERT_NAME_INFO struct containing the subject name. Can be decoded using cryptoapi::CryptDecodeObjectEx with X509_UNICODE_NAME, or formatted using cryptoapi::CertNameToStr

- PyUnicode Issuer
 Certificate Authority that issued certificate as encoded CERT_NAME_INFO. Use cryptoapi::CryptDecodeObjectEx to decode into individual components, or cryptoapi::CertNameToStr to return a single formatted string

- PyDateTime NotBefore
 Beginning of certificate's period of validity

- PyDateTime NotAfter
 End of certificate's period of validity

- str SignatureAlgorithm
 Object id of the certifcate's signature algorithm

- (PyCERT_EXTENSION,...) Extension
 Sequence of CERT_EXTENSION dicts containing certificate's extensions

- PyCERT_PUBLIC_KEY_INFO SubjectPublicKeyInfo
 Encoded public key of certificate

- int SerialNumber
 Serial number assigned by the issuer


<!-- page: PyCERT_CONTEXT__CertDeleteCertificateFromStore_meth.html -->

## PyCERT_CONTEXT.CertDeleteCertificateFromStore

 CertDeleteCertificateFromStore()

Removes the certificate from its store


<!-- page: PyCERT_CONTEXT__CertEnumCertificateContextProperties_meth.html -->

## PyCERT_CONTEXT.CertEnumCertificateContextProperties

 [int,...] = CertEnumCertificateContextProperties()

Lists property ids for the certificate


<!-- page: PyCERT_CONTEXT__CertFreeCertificateContext_meth.html -->

## PyCERT_CONTEXT.CertFreeCertificateContext

 CertFreeCertificateContext()

Frees the certificate context


<!-- page: PyCERT_CONTEXT__CertGetCertificateContextProperty_meth.html -->

## PyCERT_CONTEXT.CertGetCertificateContextProperty

 object = CertGetCertificateContextProperty(PropId)

Retrieves the specified property from the certificate

#### Parameters

- PropId : int

 One of the CERT_*_PROP_ID constants

| | PropId | Returned value
| |

---

 |

---

| | CERT_ARCHIVED_PROP_ID | Boolean
| | CERT_DATE_STAMP_PROP_ID | PyDateTime
| | CERT_ACCESS_STATE_PROP_ID | int
| | CERT_KEY_SPEC_PROP_ID | int
| | CERT_DESCRIPTION_PROP_ID | Unicode
| | CERT_FRIENDLY_NAME_PROP_ID | Unicode
| | CERT_PVK_FILE_PROP_ID | Unicode
| | CERT_AUTO_ENROLL_PROP_ID | Unicode
| | CERT_HASH_PROP_ID | String containing a hash
| | CERT_SHA1_HASH_PROP_ID | String containing a hash
| | CERT_MD5_HASH_PROP_ID | String containing a hash
| | CERT_SIGNATURE_HASH_PROP_ID | String containing a hash
| | CERT_KEY_IDENTIFIER_PROP_ID | String containing a hash
| | CERT_SUBJECT_NAME_MD5_HASH_PROP_ID | String containing a hash
| | CERT_KEY_PROV_HANDLE_PROP_ID | PyCRYPTPROV
| | CERT_SUBJECT_PUBLIC_KEY_MD5_HASH_PROP_ID | String containing a hash
| | CERT_ISSUER_PUBLIC_KEY_MD5_HASH_PROP_ID | String containing a hash
| | CERT_CTL_USAGE_PROP_ID | Encoded CTL_USAGE, decode as X509_ENHANCED_KEY_USAGE (CTL_USAGE and CERT_ENHKEY_USAGE are identical)
| | CERT_ENHKEY_USAGE_PROP_ID | Encoded CTL_USAGE. Can be decoded using cryptoapi::CryptDecodeObjectEx with X509_ENHANCED_KEY_USAGE
| | CERT_KEY_PROV_INFO_PROP_ID | CRYPT_KEY_PROV_INFO dict
| | CERT_KEY_CONTEXT_PROP_ID | Dict representing CERT_KEY_CONTEXT struct
| | CERT_NEXT_UPDATE_LOCATION_PROP_ID | Encoded CERT_ALT_NAME_INFO, decode using cryptoapi::CryptDecodeObjectEx with szOID_NEXT_UPDATE_LOCATION

#### Return Value

Type of object returned is dependent on the property id requested.


<!-- page: PyCERT_CONTEXT__CertGetEnhancedKeyUsage_meth.html -->

## PyCERT_CONTEXT.CertGetEnhancedKeyUsage

 tuple = CertGetEnhancedKeyUsage(Flags)

Finds the enhanced key usage property and/or extension for the certificate

#### Parameters

- Flags=0 : int

 CERT_FIND_EXT_ONLY_ENHKEY_USAGE_FLAG, CERT_FIND_PROP_ONLY_ENHKEY_USAGE_FLAG, or 0

#### Return Value

Returns a sequence of usage OIDs


<!-- page: PyCERT_CONTEXT__CertGetIntendedKeyUsage_meth.html -->

## PyCERT_CONTEXT.CertGetIntendedKeyUsage

 int = CertGetIntendedKeyUsage()

Returns the intended key usage from the certificate extensions (szOID_KEY_USAGE or szOID_KEY_ATTRIBUTES)

#### Return Value

Returns a combination of CERT_*_KEY_USAGE values


<!-- page: PyCERT_CONTEXT__CertSerializeCertificateStoreElement_meth.html -->

## PyCERT_CONTEXT.CertSerializeCertificateStoreElement

 string = CertSerializeCertificateStoreElement(Flags)

Serializes the certificate and its properties

#### Parameters

- Flags=0 : int

 Reserved, use only 0 if passed in


<!-- page: PyCERT_CONTEXT__CertSetCertificateContextProperty_meth.html -->

## PyCERT_CONTEXT.CertSetCertificateContextProperty

 CertSetCertificateContextProperty(PropId, Data, Flags)

Sets a property for a certificate

#### Parameters

- PropId : int

 Id of property to be set, CERT_*_PROP_ID

- Data : object

 The value to be set for the property. Type is dependent on PropId. Use None to delete a property.

- Flags=0 : int

 Combination of CERT_SET_* flags

| | PropId | Type of input
| |

---

 |

---

| | CERT_ARCHIVED_PROP_ID | None causes Archived flag to be cleared, any other causes it to be set no actual data, non-NULL pvData indicates presence of flag
| | CERT_DATE_STAMP_PROP_ID | PyDateTime specifying when cert was added to store
| | CERT_DESCRIPTION_PROP_ID | Unicode string
| | CERT_FRIENDLY_NAME_PROP_ID | Unicode string
| | CERT_PVK_FILE_PROP_ID | Unicode string
| | CERT_AUTO_ENROLL_PROP_ID | Unicode string
| | CERT_KEY_SPEC_PROP_ID | Int, usually AT_KEYEXCHANGE or AT_SIGNATURE
| | CERT_HASH_PROP_ID | String containing the hash
| | CERT_SHA1_HASH_PROP_ID | String containing the hash
| | CERT_MD5_HASH_PROP_ID | String containingg the hash
| | CERT_SIGNATURE_HASH_PROP_ID | String containing the hash
| | CERT_KEY_IDENTIFIER_PROP_ID | String containing the key id
| | CERT_SUBJECT_PUBLIC_KEY_MD5_HASH_PROP_ID | String containing the hash
| | CERT_ISSUER_PUBLIC_KEY_MD5_HASH_PROP_ID | String containing the hash
| | CERT_SUBJECT_NAME_MD5_HASH_PROP_ID | String containing the hash
| | CERT_RENEWAL_PROP_ID | String containing the hash
| | CERT_ENHKEY_USAGE_PROP_ID | String containing an encoded PyCTL_USAGE. Use cryptoapi::CryptEncodeObjectEx with X509_ENHANCED_KEY_USAGE.
| | CERT_CTL_USAGE_PROP_ID | Same as CERT_ENHKEY_USAGE_PROP_ID


<!-- page: PyCERT_CONTEXT__CertVerifySubjectCertificateContext_meth.html -->

## PyCERT_CONTEXT.CertVerifySubjectCertificateContext

 int = CertVerifySubjectCertificateContext(Issuer, Flags )

Checks the validity of the certificate

#### Parameters

- Issuer : PyCERT_CONTEXT

 Certificate of authority that issued the certificate

- Flags : int

 Combination of CERT_STORE_REVOCATION_FLAG,CERT_STORE_SIGNATURE_FLAG and CERT_STORE_TIME_VALIDITY_FLAG indicating which checks should be performed

#### Return Value

Returns flags indicating which validity checks failed, or 0 if all were successful.


<!-- page: PyCERT_CONTEXT__CryptAcquireCertificatePrivateKey_meth.html -->

## PyCERT_CONTEXT.CryptAcquireCertificatePrivateKey

 (int,PyCRYPTPROV) = CryptAcquireCertificatePrivateKey(Flags)

Retrieves the private key associated with the certificate

#### Parameters

- Flags=0 : int

 Combination of CRYPT_ACQUIRE_*_FLAG constants

#### Comments

 Only the owner of the certificate can use this method

#### Return Value

Returns the KeySpec (AT_KEYEXCHANGE or AT_SIGNATURE) and a CSP handle to the key


---

<!-- object: PyCERT_EXTENSION -->


<!-- page: PyCERT_EXTENSION.html -->

---

## PyCERT_EXTENSION Object

 Dict containing a certificate extension

#### Properties

- str ObjId
 The OID identifying the type of extension

- boolean Critical
 If true, any contraints or limits contained in the extension should be considered absolute

- str Value
 Binary string containing ASN encoded data. To interpret or display extension data, see cryptoapi::CryptDecodeObjectEx and cryptoapi::CryptFormatObject .

#### Comments

 These extensions are not yet handled by CryptDecodeObjectEx, but can be formatted with CryptFormatObject.
szOID_PRIVATEKEY_USAGE_PERIOD -- ???? CERT_PRIVATE_KEY_VALIDITY ????
szOID_KEY_USAGE_RESTRICTION - CERT_KEY_USAGE_RESTRICTION_INFO


---

<!-- object: PyCERT_KEY_ATTRIBUTES_INFO -->


<!-- page: PyCERT_KEY_ATTRIBUTES_INFO.html -->

---

## PyCERT_KEY_ATTRIBUTES_INFO Object

 Dict representing a CERT_KEY_ATTRIBUTES_INFO struct

#### Properties

- str KeyId
 Usually a hash that uniquely identifies the key

- PyCRYPT_BIT_BLOB IntendedKeyUsage
 Contains a byte with CERT_*_KEY_USAGE flags

- dict PrivateKeyUsagePeriod
 Private key's begin and end effective dates, may be None


---

<!-- object: PyCERT_NAME_INFO -->


<!-- page: PyCERT_NAME_INFO.html -->

---

## PyCERT_NAME_INFO Object

 Sequence of CERT_RDN's


---

<!-- object: PyCERT_NAME_VALUE -->


<!-- page: PyCERT_NAME_VALUE.html -->

---

## PyCERT_NAME_VALUE Object

 Dict containing type (CERT_RDN_*) and a unicode string


---

<!-- object: PyCERT_OTHER_NAME -->


<!-- page: PyCERT_OTHER_NAME.html -->

---

## PyCERT_OTHER_NAME Object

 Dict containing {ObjId, Value}. ObjId is one of the string object id's identifying the type of name. Value is a binary string containing an encoded CERT_NAME_VALUE that can be decoded using X509_UNICODE_NAME_VALUE to return the actual unicode string


---

<!-- object: PyCERT_POLICY_INFO -->


<!-- page: PyCERT_POLICY_INFO.html -->

---

## PyCERT_POLICY_INFO Object

 Dict containing a certificate policy

#### Properties

- str PolicyIdentifier
 OID identifying the policy

- tuple PolicyQualifier
 Sequence of CERT_POLICY_QUALIFIER dicts


---

<!-- object: PyCERT_PUBLIC_KEY_INFO -->


<!-- page: PyCERT_PUBLIC_KEY_INFO.html -->

---

## PyCERT_PUBLIC_KEY_INFO Object

 Dict containing an exported public key

#### Properties

- PyCRYPT_ALGORITHM_IDENTIFIER Algorithm
 Dict containing OID of the public key algorithm

- PyCRYPT_BIT_BLOB PublicKey
 Dict containing the encoded public key


---

<!-- object: PyCEdit -->


<!-- page: PyCEdit.html -->

---

## PyCEdit Object

 A windows edit control. Encapsulates an MFC CEdit class. Derived from a PyCControl object.

#### Methods

- CreateWindow

 Creates the window for a new edit object.

- Clear

 Clears all text from an edit control.

- Copy

 Copy the selection to the clipboard.

- Cut

 Cut the selection, and place it in the clipboard.

- FmtLines

 Change the formatting options for the edit control

- GetFirstVisibleLine

 Returns zero-based index of the topmost visible line.

- GetSel

 Returns the selection.

- GetLine

 Returns a specified line.

- GetLineCount

 Returns the number of lines in an edit control.

- LimitText

 Sets max length of text that user can enter

- LineFromChar

 Returns the line number of a given character.

- LineIndex

 Returns the line index

- LineScroll

 Scroll the control vertically and horizontally

- Paste

 Pastes the contents of the clipboard into the edit control.

- ReplaceSel

 Replace the selection with the specified text.

- SetReadOnly

 Set the read only status of an edit control.

- SetSel

 Changes the selection in an edit control. sentinel


<!-- page: PyCEdit__Clear_meth.html -->

## PyCEdit.Clear

 int = Clear()

Clears all text in an edit control.

#### MFC References

- CEdit::Clear


<!-- page: PyCEdit__Copy_meth.html -->

## PyCEdit.Copy

 Copy()

Copys the current selection to the clipboard.

#### MFC References

- CEdit::Copy


<!-- page: PyCEdit__CreateWindow_meth.html -->

## PyCEdit.CreateWindow

 CreateWindow(style, rect, parent, id)

Creates the window for a new Edit object.

#### Parameters

- style : int

 The style for the Edit. Use any of the win32con.BS_* constants.

- rect : (left, top, right, bottom)

 The size and position of the Edit.

- parent : PyCWnd

 The parent window of the Edit. Usually a PyCDialog.

- id : int

 The Edits control ID.


<!-- page: PyCEdit__Cut_meth.html -->

## PyCEdit.Cut

 Cut()

Cuts the current selection to the clipboard.

#### MFC References

- CEdit::Cut


<!-- page: PyCEdit__FmtLines_meth.html -->

## PyCEdit.FmtLines

 int = FmtLines(bAddEOL)

Sets the formatting options for the control.

#### Parameters

- bAddEOL : int

 Specifies whether soft line-break characters are to be inserted. A value of TRUE inserts the characters; a value of FALSE removes them.

#### MFC References

- CEdit::FmtLines

#### Return Value

Nonzero if any formatting occurs; otherwise 0.


<!-- page: PyCEdit__GetFirstVisibleLine_meth.html -->

## PyCEdit.GetFirstVisibleLine

 int = GetFirstVisibleLine()

Returns zero-based index of the topmost visible line.

#### MFC References

- CEdit::GetFirstVisibleLine

#### Return Value

The zero-based index of the topmost visible line. For single-line edit controls, the return value is 0.


<!-- page: PyCEdit__GetLineCount_meth.html -->

## PyCEdit.GetLineCount

 int = GetLineCount()

Gets the number of lines in an edit control.

#### MFC References

- CEdit::GetLineCount

#### Return Value

The number of lines in the buffer. If the control is empty, the return value is 1.


<!-- page: PyCEdit__GetLine_meth.html -->

## PyCEdit.GetLine

 int = GetLine(lineNo)

Returns the text in a specified line.

#### Parameters

- lineNo=current : int

 Contains the zero-based index value for the desired line.

#### Comments

 This function is not an MFC wrapper.


<!-- page: PyCEdit__GetSel_meth.html -->

## PyCEdit.GetSel

 (start, end) = GetSel()

Returns the start and end of the current selection.

#### MFC References

- CEdit::GetSel

#### Return Value

The return tuple is (the first character in the current selection, first nonselected character past the end of the current selection)


<!-- page: PyCEdit__LimitText_meth.html -->

## PyCEdit.LimitText

 LimitText(nChars)

Sets max length of text that user can enter

#### Parameters

- nChars=0 : int

 Specifies the length (in bytes) of the text that the user can enter. If this parameter is 0, the text length is set to UINT_MAX bytes. This is the default behavior.

#### MFC References

- CEdit::LimitText


<!-- page: PyCEdit__LineFromChar_meth.html -->

## PyCEdit.LineFromChar

 int = LineFromChar(charNo)

Returns the line number of the specified character.

#### Parameters

- charNo=-1 : int

 Contains the zero-based index value for the desired character in the text of the edit control, or -1. If -1, then it specifies the current line.

#### MFC References

- CEdit::LineFromChar

#### Return Value

The zero-based line number of the line containing the character index specified by charNo. If charNo is -1, the number of the line that contains the first character of the selection is returned. If there is no selection, the current line number is returned.


<!-- page: PyCEdit__LineIndex_meth.html -->

## PyCEdit.LineIndex

 int = LineIndex(lineNo)

Retrieves the character index of a line within a multiple-line edit control.

#### Parameters

- lineNo=-1 : int

 Contains the index value for the desired line in the text of the edit control, or contains -1. If -1, then it specifies the current line.

#### Comments

 This method only works on multi-linr edit controls.

#### MFC References

- CEdit::LineIndex

#### Return Value

The character index of the line specified in lineNo, or -1 if the specified line number is greater then the number of lines in the edit control.


<!-- page: PyCEdit__LineScroll_meth.html -->

## PyCEdit.LineScroll

 int = LineScroll(nLines, nChars )

Scroll the control vertically and horizontally

#### Parameters

- nLines : int

 Specifies the number of lines to scroll vertically.

- nChars=0 : int

 Specifies the number of character positions to scroll horizontally. This value is ignored if the edit control has either the ES_RIGHT or ES_CENTER style.

#### Comments

 This method only works on multi-linr edit controls.

#### MFC References

- CEdit::LineScroll


<!-- page: PyCEdit__Paste_meth.html -->

## PyCEdit.Paste

 Paste()

Pastes the contents of the clipboard into the control.

#### MFC References

- CEdit::Paste


<!-- page: PyCEdit__ReplaceSel_meth.html -->

## PyCEdit.ReplaceSel

 ReplaceSel(text)

Replaces the selection with the specified text.

#### Parameters

- text : string

 The text to replace the selection with.

#### MFC References

- CEdit::ReplaceSel


<!-- page: PyCEdit__SetReadOnly_meth.html -->

## PyCEdit.SetReadOnly

 SetReadOnly(bReadOnly)

Sets or clears the read-only status of the listbox.

#### Parameters

- bReadOnly=1 : int

 The read-only state to set.

#### MFC References

- CEdit::SetReadOnly


<!-- page: PyCEdit__SetSel_meth.html -->

## PyCEdit.SetSel

 SetSel(start, end, bNoScroll)

Sets the selection in the edit control.

#### Parameters

- start : int

 Specifies the starting position. If start is 0 and end is -1, all the text in the edit control is selected. If start is -1, any current selection is removed.

- end=start : int

 Specifies the ending position.

- bNoScroll=0 : int

 Indicates whether the caret should be scrolled into view. If 0, the caret is scrolled into view. If 1, the caret is not scrolled into view.

#### Alternative Parameters

- start,end)

 As for normal start, end args.

- bNoScroll

 Indicates whether the caret should be scrolled into view. If 0, the caret is scrolled into view. If 1, the caret is not scrolled into view.

#### MFC References

- CEdit::SetSel


---

<!-- object: PyCEditView -->


<!-- page: PyCEditView.html -->

---

## PyCEditView Object

 A class which implements a CView of a text file. Derived from PyCView and PyCEdit objects.

#### Methods

- IsModified

 Indicates if the view's document is modified.

- LoadFile

 Loads a named file into the view.

- SetModifiedFlag

 Sets the view's document modified flag.

- GetEditCtrl

 Returns the underlying PyCEdit object

- PreCreateWindow

 Calls the underlying MFC PreCreateWindow method.

- SaveFile

 Saves the view to a named file.

- OnCommand

 Calls the standard Python framework OnCommand handler

#### Based On

PyCCtrlView


<!-- page: PyCEditView__GetEditCtrl_meth.html -->

## PyCEditView.GetEditCtrl

 PyCEditCtrl = GetEditCtrl()

returns the underlying edit control object.


<!-- page: PyCEditView__IsModified_meth.html -->

## PyCEditView.IsModified

 int = IsModified()

Indicates if the view's document has the modified flag set.


<!-- page: PyCEditView__LoadFile_meth.html -->

## PyCEditView.LoadFile

 LoadFile(fileName)

Loads a file into the view.

#### Parameters

- fileName : string

 The name of the file to be loaded.


<!-- page: PyCEditView__OnCommand_meth.html -->

## PyCEditView.OnCommand

 OnCommand(wparam, lparam)

Calls the standard Python framework OnCommand handler

#### Parameters

- wparam : int

- lparam : int

#### See Also

- PyCWnd.OnCommand virtual method


<!-- page: PyCEditView__PreCreateWindow_meth.html -->

## PyCEditView.PreCreateWindow

 tuple = PreCreateWindow(createStruct)

Calls the underlying MFC PreCreateWindow method.

#### Parameters

- createStruct : tuple

 A tuple representing a CREATESTRUCT structure.


<!-- page: PyCEditView__SaveFile_meth.html -->

## PyCEditView.SaveFile

 SaveFile(fileName)

Saves the view to a file.

#### Parameters

- fileName : string

 The name of the file to be written.


<!-- page: PyCEditView__SetModifiedFlag_meth.html -->

## PyCEditView.SetModifiedFlag

 SetModifiedFlag(bModified)

Sets the modified flag for the view's document.

#### Parameters

- bModified=1 : int

 The modified state to set.


---

<!-- object: PyCFileDialog -->


<!-- page: PyCFileDialog.html -->

---

## PyCFileDialog Object

 A class which encapsulates an MFC CFileDialog object. Derived from a PyCDialog object.

#### Methods

- GetPathName

 Retrieves the path name.

- GetFileName

 Retrieves the file name.

- GetFileExt

 Retrieves the file extension.

- GetFileTitle

 Retrieves the file title.

- GetPathNames

 Retrieves the list of path names from the file dialog.

- GetReadOnlyPref

 Retrieves the read-only preference.

- SetOFNTitle

 Sets the title for the dialog.

- SetOFNInitialDir

 Sets the initial directory for the dialog.

#### Based On

PyCCommonDialog


<!-- page: PyCFileDialog__GetFileExt_meth.html -->

## PyCFileDialog.GetFileExt

 string = GetFileExt()

Retrives the file extension from the file dialog.

#### MFC References

- CFileDialog::GetFileExt


<!-- page: PyCFileDialog__GetFileName_meth.html -->

## PyCFileDialog.GetFileName

 string = GetFileName()

Retrives the file name from the file dialog.

#### MFC References

- CFileDialog::GetFileName


<!-- page: PyCFileDialog__GetFileTitle_meth.html -->

## PyCFileDialog.GetFileTitle

 string = GetFileTitle()

Retrives the file title from the file dialog.

#### MFC References

- CFileDialog::GetFileTitle


<!-- page: PyCFileDialog__GetPathName_meth.html -->

## PyCFileDialog.GetPathName

 string = GetPathName()

Retrives the path name from the file dialog.

#### MFC References

- CFileDialog::GetPathName


<!-- page: PyCFileDialog__GetPathNames_meth.html -->

## PyCFileDialog.GetPathNames

 string = GetPathNames()

Retrieves the list of path names from the file dialog.

#### Comments

 This method is useful when a multi-select dialog is used.

#### MFC References

- CFileDialog::GetPathNames


<!-- page: PyCFileDialog__GetReadOnlyPref_meth.html -->

## PyCFileDialog.GetReadOnlyPref

 int = GetReadOnlyPref()

Retrives the value of the "Read Only" checkbox on the file dialog.

#### MFC References

- CFileDialog::GetReadOnlyPref


<!-- page: PyCFileDialog__SetOFNInitialDir_meth.html -->

## PyCFileDialog.SetOFNInitialDir

 SetOFNInitialDir(title)

Sets the initial directory for the dialog.

#### Parameters

- title : string

 The initial directory for the dialog box. May be None.


<!-- page: PyCFileDialog__SetOFNTitle_meth.html -->

## PyCFileDialog.SetOFNTitle

 SetOFNTitle(title)

Sets the Title for the dialog.

#### Parameters

- title : string

 The title for the dialog box. May be None.


---

<!-- object: PyCFont -->


<!-- page: PyCFont.html -->

---

## PyCFont Object

 A windows font object. Encapsulates an MFC CFont class. Derived from a PyCGDIObject.

#### Methods

- GetSafeHandle

 Retrieves the HFONT for the font as an integer sentinel


<!-- page: PyCFont__GetSafeHandle_meth.html -->

## PyCFont.GetSafeHandle

 int = GetSafeHandle()

Retrieves the HFONT for the font as an integer


---

<!-- object: PyCFontDialog -->


<!-- page: PyCFontDialog.html -->

---

## PyCFontDialog Object

 A class which encapsulates an MFC CFontDialog object. Derived from a PyCDialog object.

#### Methods

- DoModal

 Displays a dialog and allows the user to make a selection.

- GetCurrentFont

 Returns a dictionary describing the current font.

- GetCharFormat

 Returns the font selection in a CHARFORMAT tuple.

- GetColor

 Determines the color of the selected font.

- GetFaceName

 Returns the face name of the selected font.

- GetStyleName

 Returns the style name of the selected font.

- GetSize

 Returns he font's size, in tenths of a point.

- GetWeight

 Returns the font's weight.

- IsStrikeOut

 Determines whether the font is displayed with strikeout.

- IsUnderline

 Determines whether the font is displayed with underline.

- IsBold

 Determines whether the font is displayed bold.

- IsItalic

 Determines whether the font is displayed with italic.

#### Based On

PyCCommonDialog


<!-- page: PyCFontDialog__DoModal_meth.html -->

## PyCFontDialog.DoModal

 int = DoModal()

Displays a dialog and allows the user to make a selection.

#### MFC References

- CFontDialog::DoModal


<!-- page: PyCFontDialog__GetCharFormat_meth.html -->

## PyCFontDialog.GetCharFormat

 tuple = GetCharFormat()

Returns the font selection in a CHARFORMAT tuple.

#### MFC References

- CFontDialog::GetCharFormat


<!-- page: PyCFontDialog__GetColor_meth.html -->

## PyCFontDialog.GetColor

 int = GetColor()

Determines the color of the selected font.

#### MFC References

- CFontDialog::GetColor


<!-- page: PyCFontDialog__GetCurrentFont_meth.html -->

## PyCFontDialog.GetCurrentFont

 dict = GetCurrentFont()

Returns a dictionary describing the current font.

#### MFC References

- CFontDialog::GetCurrentFont


<!-- page: PyCFontDialog__GetFaceName_meth.html -->

## PyCFontDialog.GetFaceName

 string = GetFaceName()

Returns the face name of the selected font.

#### MFC References

- CFontDialog::GetFaceName


<!-- page: PyCFontDialog__GetSize_meth.html -->

## PyCFontDialog.GetSize

 int = GetSize()

Returns he font's size, in tenths of a point.

#### MFC References

- CFontDialog::GetSize


<!-- page: PyCFontDialog__GetStyleName_meth.html -->

## PyCFontDialog.GetStyleName

 string = GetStyleName()

Returns the style name of the selected font.

#### MFC References

- CFontDialog::GetStyleName


<!-- page: PyCFontDialog__GetWeight_meth.html -->

## PyCFontDialog.GetWeight

 int = GetWeight()

Returns the font's weight.

#### MFC References

- CFontDialog::GetWeight


<!-- page: PyCFontDialog__IsBold_meth.html -->

## PyCFontDialog.IsBold

 int = IsBold()

Determines whether the font is displayed bold.

#### MFC References

- CFontDialog::IsBold


<!-- page: PyCFontDialog__IsItalic_meth.html -->

## PyCFontDialog.IsItalic

 int = IsItalic()

Determines whether the font is displayed with italic.

#### MFC References

- CFontDialog::IsItalic


<!-- page: PyCFontDialog__IsStrikeOut_meth.html -->

## PyCFontDialog.IsStrikeOut

 int = IsStrikeOut()

Determines whether the font is displayed with strikeout.

#### MFC References

- CFontDialog::IsStrikeOut


<!-- page: PyCFontDialog__IsUnderline_meth.html -->

## PyCFontDialog.IsUnderline

 int = IsUnderline()

Determines whether the font is displayed with underline.

#### MFC References

- CFontDialog::IsUnderline


---

<!-- object: PyCFormView -->


<!-- page: PyCFormView.html -->

---

## PyCFormView Object

 A class which implements a CFormView (ie, a view based on a dialog resource.

#### Methods

- OnCommand

 Calls the standard Python framework OnCommand handler

#### Based On

PyCView


<!-- page: PyCFormView__OnCommand_meth.html -->

## PyCFormView.OnCommand

 OnCommand(wparam, lparam)

Calls the standard Python framework OnCommand handler

#### Parameters

- wparam : int

- lparam : int

#### See Also

- PyCWnd.OnCommand virtual method


---

<!-- object: PyCFrameWnd -->


<!-- page: PyCFrameWnd.html -->

---

## PyCFrameWnd Object

 A windows frame window. Encapsulates an MFC CFrameWnd class. Derived from a PyCWnd object.

#### Methods

- BeginModalState

 Sets the frame window to modal.

- CreateWindow

 Creates the underlying window for the object.

- EndModalState

 Ends the frame window's modal state. Enables all of the windows disabled by PyCFrameWnd::BeginModalState.

- DockControlBar

 Docks a control bar.

- EnableDocking

 Enable dockable control bars in a frame window

- FloatControlBar

 Floats a control bar.

- GetActiveDocument

 Returns the currently active document

- GetControlBar

 Retrieves the specified control bar.

- GetMessageString

 Retrieves message corresponding to a command ID.

- GetMessageBar

 Retrieves the message bar for the frame.

- IsTracking

 Determines if splitter bar is currently being moved.

- InModalState

 Returns a value indicating whether or not a frame window is in a modal state.

- LoadAccelTable

 Loads an accelerator table.

- LoadFrame

 Creates the MDI Window's frame

- LoadBarState

 Loads a control bars settings

- PreCreateWindow

 Calls the underlying MFC PreCreateWindow method.

- SaveBarState

 Saves a control bars settings

- ShowControlBar

 Shows a control bar.

- RecalcLayout

 Called by the framework when the standard control bars are toggled on or off or when the frame window is resized.

- GetActiveView

 Retrieves the active view.

- OnBarCheck

 Changes the state of the specified controlbar.

- OnUpdateControlBarMenu

 Checks the state of a menu item

- SetActiveView

 Sets the active view for a frame.

#### Based On

PyCWnd


<!-- page: PyCFrameWnd__BeginModalState_meth.html -->

## PyCFrameWnd.BeginModalState

 BeginModalState()

Sets the frame window to modal.


<!-- page: PyCFrameWnd__CreateWindow_meth.html -->

## PyCFrameWnd.CreateWindow

 tuple = CreateWindow(wndClass, title , style , rect , PyCWnd , createContext , menuId , styleEx )

Creates the actual window for the PyCFrameWnd object.

#### Parameters

- wndClass : string

 The window class name, or None

- title : string

 The window title

- style=WS_VISIBLE | WS_OVERLAPPEDWINDOW : int

 The window style

- rect=None : int, int, int, int

 The default rectangle

- PyCWnd=None : parent

 The parent window

- createContext=None : tuple

 A tuple representing a CREATECONTEXT structure.

- menuId : string or int

 The string or integer id for the menu.

- styleEx : int

 The extended style of the window being created.

#### MFC References

- CFrameWnd::Create


<!-- page: PyCFrameWnd__DockControlBar_meth.html -->

## PyCFrameWnd.DockControlBar

 DockControlBar(controlBar, dockBarId, int, int, int, int)

Docks a control bar.

#### Parameters

- controlBar : PyCControlBar

 The control bar to dock.

- dockBarId=0 : int

 Determines which sides of the frame window to consider for docking.

- int, int, int, int=0,0,0,0 : left, top, right, bottom

 Determines, in screen coordinates, where the control bar will be docked in the nonclient area of the destination frame window.

#### MFC References

- CFrameWnd::DockControlBar


<!-- page: PyCFrameWnd__EnableDocking_meth.html -->

## PyCFrameWnd.EnableDocking

 EnableDocking(style)

Enable dockable control bars in a frame window

#### Parameters

- style : int

 Specifies which sides of the frame window can serve as docking sites for control bars.

#### Comments

 By default, control bars will be docked to a side of the frame window in the following order: top, bottom, left, right.


<!-- page: PyCFrameWnd__EndModalState_meth.html -->

## PyCFrameWnd.EndModalState

 EndModalState()

Ends the frame window's modal state. Enables all of the windows disabled by PyCFrameWnd::BeginModalState.


<!-- page: PyCFrameWnd__FloatControlBar_meth.html -->

## PyCFrameWnd.FloatControlBar

 FloatControlBar(controlBar, int, int, style)

Floats a control bar.

#### Parameters

- controlBar : PyCControlBar

 The control bar to dock.

- int, int : x,y

 The location, in screen coordinates, where the top left corner of the control bar will be placed.

- style=CBRS_ALIGN_TOP : int

 Determines which sides of the frame window to consider for docking.

#### MFC References

- CFrameWnd::FloatControlBar


<!-- page: PyCFrameWnd__GetActiveDocument_meth.html -->

## PyCFrameWnd.GetActiveDocument

 PyCDocument = GetActiveDocument()

Gets the currently active document, else None

#### MFC References

- CFrameWnd::GetActiveDocument


<!-- page: PyCFrameWnd__GetActiveView_meth.html -->

## PyCFrameWnd.GetActiveView

 PyCView = GetActiveView()

Retrieves the active view.


<!-- page: PyCFrameWnd__GetControlBar_meth.html -->

## PyCFrameWnd.GetControlBar

 PyCControlBar = GetControlBar(id)

Retrieves the specified control bar.

#### Parameters

- id : int

 The ID of the toolbar to be retrieved


<!-- page: PyCFrameWnd__GetMessageBar_meth.html -->

## PyCFrameWnd.GetMessageBar

 PyCWnd = GetMessageBar()

Retrieves the message bar for the frame.


<!-- page: PyCFrameWnd__GetMessageString_meth.html -->

## PyCFrameWnd.GetMessageString

 string = GetMessageString(id)

Retrieves message corresponding to a command ID.

#### Parameters

- id : int

 The ID to be retrieved

#### See Also

- PyCMDIChildWnd.GetMessageString virtual method


<!-- page: PyCFrameWnd__InModalState_meth.html -->

## PyCFrameWnd.InModalState

 int = InModalState()

Returns a value indicating whether or not a frame window is in a modal state.


<!-- page: PyCFrameWnd__IsTracking_meth.html -->

## PyCFrameWnd.IsTracking

 int = IsTracking()

Determines if splitter bar is currently being moved.


<!-- page: PyCFrameWnd__LoadAccelTable_meth.html -->

## PyCFrameWnd.LoadAccelTable

 LoadAccelTable(id)

Loads an accelerator table.

#### Parameters

- id : PyResourceId

 Name or id of the resource that contains the table


<!-- page: PyCFrameWnd__LoadBarState_meth.html -->

## PyCFrameWnd.LoadBarState

 LoadBarState(profileName)

Loads a control bars settings

#### Parameters

- profileName : string

 Name of a section in the initialization file or a key in the Windows registry where state information is stored.

#### MFC References

- CFrameWnd::LoadBarState


<!-- page: PyCFrameWnd__LoadFrame_meth.html -->

## PyCFrameWnd.LoadFrame

 LoadFrame(idResource, style, wndParent, context)

Loads a Windows frame window and associated resources

#### Parameters

- idResource=IDR_PYTHONTYPE : int

 The Id of the resources (menu, icon, etc) for this window

- style=-1 : long

 The window style. Note -1 implies win32con.WS_OVERLAPPEDWINDOW|win32con.FWS_ADDTOTITLE

- wndParent=None : PyCWnd

 The parent of the window, or None.

- context=None : object

 An object passed to the OnCreateClient for the frame,

#### MFC References

- CFrameWnd::LoadFrame


<!-- page: PyCFrameWnd__OnBarCheck_meth.html -->

## PyCFrameWnd.OnBarCheck

 int = OnBarCheck(id)

Changes the state of the specified controlbar.

#### Parameters

- id : int

 The control ID of the control bar.


<!-- page: PyCFrameWnd__OnUpdateControlBarMenu_meth.html -->

## PyCFrameWnd.OnUpdateControlBarMenu

 int = OnUpdateControlBarMenu(cmdUI)

Checks the state of a menu item

#### Parameters

- cmdUI : PyCCmdUI

 A cmdui object


<!-- page: PyCFrameWnd__PreCreateWindow_meth.html -->

## PyCFrameWnd.PreCreateWindow

 tuple = PreCreateWindow(createStruct)

Calls the underlying MFC PreCreateWindow method.

#### Parameters

- createStruct : tuple

 A tuple representing a CREATESTRUCT structure.

#### See Also

- PyCWnd.PreCreateWindow virtual method


<!-- page: PyCFrameWnd__RecalcLayout_meth.html -->

## PyCFrameWnd.RecalcLayout

 RecalcLayout(bNotify)

Called by the framework when the standard control bars are toggled on or off or when the frame window is resized.

#### Parameters

- bNotify=1 : int

 Notify flag

#### MFC References

- CFrameWnd::RecalcLayout


<!-- page: PyCFrameWnd__SaveBarState_meth.html -->

## PyCFrameWnd.SaveBarState

 SaveBarState(profileName)

Saves a control bars settings

#### Parameters

- profileName : string

 Name of a section in the initialization file or a key in the Windows registry where state information is stored.

#### MFC References

- CFrameWnd::SaveBarState


<!-- page: PyCFrameWnd__SetActiveView_meth.html -->

## PyCFrameWnd.SetActiveView

 SetActiveView(view, bNotify)

Sets the active view for a frame.

#### Parameters

- view : PyCView

 The view to set active.

- bNotify=1 : int

 Specifies whether the view is to be notified of activation. If TRUE, OnActivateView is called for the new view; if FALSE, it is not.


<!-- page: PyCFrameWnd__ShowControlBar_meth.html -->

## PyCFrameWnd.ShowControlBar

 ShowControlBar(controlBar, bShow, bDelay)

Shows a control bar.

#### Parameters

- controlBar : PyCControlBar

 The control bar to dock.

- bShow : int

 Show or hide flag.

- bDelay : int

 If TRUE, delay showing the control bar. If FALSE, show the control bar immediately.

#### MFC References

- CFrameWnd::ShowControlBar


<!-- page: PyCFrameWnd__ShowOwnedWindows_meth.html -->

## PyCFrameWnd.ShowOwnedWindows

 string = ShowOwnedWindows(bShow)

Shows all windows that are descendants of the PyCFrameWnd object.

#### Parameters

- bShow=1 : int

 Flag


---

<!-- object: PyCGdiObject -->


<!-- page: PyCGdiObject.html -->

---

## PyCGdiObject Object

 A class which encapsulates an MFC CGdiObject.


---

<!-- object: PyCImageList -->


<!-- page: PyCImageList.html -->

---

## PyCImageList Object

 A Python type encapsulating an MFC CImageList class.

#### Methods

- Add

 Adds an icon to the image list.

- Destroy

 Destroys the underlying MFC imagelist object.

- DeleteImageList

 Deletes an image list.

- GetBkColor

 Retrieves the background color of an Image List.

- GetSafeHandle

 Retrieves the HIMAGELIST for the object

- GetImageCount

 Retrieves the number of images in an image list.

- GetImageInfo

 Retrieves information about an image.

- SetBkColor

 Sets the background color for an Image List.


<!-- page: PyCImageList__Add_meth.html -->

## PyCImageList.Add

 int = Add(bitmap, bitmapMask)

Adds an image to the list.

#### Parameters

- bitmap, bitmapMask : (int,int)

 2 Bitmaps to use (primary and mask)

#### Alternative Parameters

- bitmap

 Bitmap to use

- color

 Color to use for the mask.

#### Alternative Parameters

- hIcon

 Handle of an icon to add.

#### Return Value

Zero-based index of the first new image.


<!-- page: PyCImageList__DeleteImageList_meth.html -->

## PyCImageList.DeleteImageList

 DeleteImageList()

Deletes an image list.

#### Comments

 This frees all resources associated with an image list. No further operations on the object will be allowed.


<!-- page: PyCImageList__Destroy_meth.html -->

## PyCImageList.Destroy

 Destroy()

Destroys the underlying CImageList

#### Comments

 This method actually calls delete() on the CImageList - you should ensure that no controls still require access to this list.


<!-- page: PyCImageList__GetBkColor_meth.html -->

## PyCImageList.GetBkColor

 int = GetBkColor()

Retrieves the background color of an Image List.


<!-- page: PyCImageList__GetImageCount_meth.html -->

## PyCImageList.GetImageCount

 int = GetImageCount()

Retrieves the number of images in an image list.


<!-- page: PyCImageList__GetImageInfo_meth.html -->

## PyCImageList.GetImageInfo

 iiii(iiii) = GetImageInfo(index)

Retrieves information about an image.

#### Parameters

- index : int

 Index of image.

#### Return Value

The return info is a tuple describing an IMAGELIST structure.


<!-- page: PyCImageList__GetSafeHandle_meth.html -->

## PyCImageList.GetSafeHandle

 int = GetSafeHandle()

Retrieves the HIMAGELIST for the object


<!-- page: PyCImageList__SetBkColor_meth.html -->

## PyCImageList.SetBkColor

 SetBkColor(color)

Sets the background color for an Image List.

#### Parameters

- color : int

 The new background color.


---

<!-- object: PyCListBox -->


<!-- page: PyCListBox.html -->

---

## PyCListBox Object

 A windows listbox control. Encapsulates an MFC CListBox class. Derived from a PyCControl object.

#### Methods

- AddString

 Add a string to the listbox.

- DeleteString

 Delete a string from the listbox.

- Dir

 Fill a listbox with a file specification.

- GetCaretIndex

 Get the index of the item with the focus rectangle.

- GetCount

 Get the count of items in the listbox.

- GetCurSel

 Get the current selection in a single selection listbox.

- GetItemData

 Retrieves the application-specific object associated with a listbox entry

- GetItemValue

 Retrieves the application-specific value associated with a listbox entry

- GetSel

 Get the selected items in a multiple selection listbox.

- GetSelCount

 Get the number of selected items in a multtiple selection listbox.

- GetSelItems

 Get the index of the selected items in a multiple selection listbox.

- GetSelTextItems

 Get the text of the selected items in a multiple selection listbox.

- GetTopIndex

 Get the index of the topmost item.

- GetText

 Get the text associated with an item.

- GetTextLen

 Get the length of an item

- InsertString

 Insert a string into the listbox.

- ResetContent

 Remove all items from a listbox.

- SetCaretIndex

 Set the focus rectange to a specified item.

- SelectString

 Select an item, based on a string.

- SelItemRange

 Select a range of items in a multiple selection listbox.

- SetCurSel

 Set the current selection in a single selection listbox.

- SetItemData

 Sets the application-specific object associated with a listbox entry

- SetItemValue

 Sets the application-specific value associated with a listbox entry

- SetSel

 Set the selection.

- SetTabStops

 Set the tab stops for a listbox.

- SetTopIndex

 Set the top most visible item in a listbox.


<!-- page: PyCListBox__AddString_meth.html -->

## PyCListBox.AddString

 int = AddString(object)

Adds a string to a listbox.

#### Parameters

- object : any

 Any object. If not a string, __str__, __repr__ or a default repr() will be used

#### MFC References

- CListBox::AddString

#### Return Value

The zero based index of the new string.


<!-- page: PyCListBox__DeleteString_meth.html -->

## PyCListBox.DeleteString

 int = DeleteString(pos)

Deletes an item from a listbox.

#### Parameters

- pos : int

 The zero based index of the item to delete.

#### MFC References

- CListBox::DeleteString

#### Return Value

The count of the items remaining in the list.


<!-- page: PyCListBox__Dir_meth.html -->

## PyCListBox.Dir

 int = Dir(attr, wild )

Fills a listbox with a directory listing.

#### Parameters

- attr : int

 The attributes of the files to locate

- wild : string

 A file specification string - eg, *.*

#### MFC References

- CListBox::Dir

#### Return Value

The index of the last file name added to the list.


<!-- page: PyCListBox__GetCaretIndex_meth.html -->

## PyCListBox.GetCaretIndex

 int = GetCaretIndex()

Returns the index of the item which has focus.

#### Return Value

The zero-based index of the item that has the focus rectangle in a list box. If the list box is a single-selection list box, the return value is the index of the item that is selected, if any.


<!-- page: PyCListBox__GetCount_meth.html -->

## PyCListBox.GetCount

 int = GetCount()

Returns the count of items in the listbox.

#### MFC References

- CListBox::GetCount

#### Return Value

Returns the number of items currently in the listbox.


<!-- page: PyCListBox__GetCurSel_meth.html -->

## PyCListBox.GetCurSel

 int = GetCurSel()

Returns the index of the currently selected item.

#### Comments

 Should not be called for a multiple selection listbox.

#### MFC References

- CListBox::GetCurSel


<!-- page: PyCListBox__GetItemData_meth.html -->

## PyCListBox.GetItemData

 object = GetItemData(item)

Retrieves the application-specific object associated with an item.

#### Parameters

- item : int

 The index of the item whose data is to be retrieved.


<!-- page: PyCListBox__GetItemValue_meth.html -->

## PyCListBox.GetItemValue

 int = GetItemValue(item)

Retrieves the application-specific value associated with an item.

#### Parameters

- item : int

 The index of the item whose data is to be retrieved.


<!-- page: PyCListBox__GetSelCount_meth.html -->

## PyCListBox.GetSelCount

 int = GetSelCount()

Returns the number of selected items in a multiple selection listbox.

#### MFC References

- CListBox::GetSelCount


<!-- page: PyCListBox__GetSelItems_meth.html -->

## PyCListBox.GetSelItems

 list = GetSelItems()

Returns a list of the indexes of the currently selected items in a multiple selection listbox.

#### MFC References

- CListBox::GetSelCount

- CListBox::GetSelItems


<!-- page: PyCListBox__GetSelTextItems_meth.html -->

## PyCListBox.GetSelTextItems

 list = GetSelTextItems()

Returns a list of the strings of the currently selected items in a multiple selection listbox.

#### MFC References

- CListBox::GetSelCount

- CListBox::GetSelItems

- CListBox::GetText


<!-- page: PyCListBox__GetSel_meth.html -->

## PyCListBox.GetSel

 int = GetSel(index)

Returns the selection state of a specified item.

#### Parameters

- index : int

 The index of the item to return the state for.

#### MFC References

- CListBox::GetSel

#### Return Value

A +ve number if the item is selected, else zero.


<!-- page: PyCListBox__GetTextLen_meth.html -->

## PyCListBox.GetTextLen

 int = GetTextLen(index)

Returns the length of the string for a specified item.

#### Parameters

- index : int

 The index of the item to retrieve the length of the text.

#### MFC References

- CListBox::GetTextLen


<!-- page: PyCListBox__GetText_meth.html -->

## PyCListBox.GetText

 string = GetText(index)

Returns the string for a specified item.

#### Parameters

- index : int

 The index of the item to retrieve the text of


<!-- page: PyCListBox__GetTopIndex_meth.html -->

## PyCListBox.GetTopIndex

 int = GetTopIndex()

Returns the index of the top most visible item.

#### MFC References

- CListBox::GetTopIndex

#### Return Value

The zero based index of the top most visible item.


<!-- page: PyCListBox__InsertString_meth.html -->

## PyCListBox.InsertString

 int = InsertString(pos, object )

Insert a string into a listbox.

#### Parameters

- pos : int

 The zero based index in the listbox to insert the new string

- object : any

 The object to be added to the listbox

#### MFC References

- CListBox::InsertString

#### Return Value

The zero based index of the new string added.


<!-- page: PyCListBox__ResetContent_meth.html -->

## PyCListBox.ResetContent

 ResetContent()

Clear all the items from a listbox.

#### MFC References

- CListBox::ResetContent


<!-- page: PyCListBox__SelItemRange_meth.html -->

## PyCListBox.SelItemRange

 SelItemRange(bSel, start, end)

Selects an item range.

#### Parameters

- bSel : int

 Should the selection specified be set or cleared?

- start : int

 The zero based index of the first item to select.

- end : int

 The zero based index of the last item to select.


<!-- page: PyCListBox__SelectString_meth.html -->

## PyCListBox.SelectString

 SelectString(after, string)

Searches for a list-box item that matches the specified string, and selects it.

#### Parameters

- after : int

 Contains the zero-based index of the item before the first item to be searched, or -1 for the entire listbox.

- string : string

 The string to search for.

#### MFC References

- CListBox::SelectString

#### Return Value

The return value is always None - an exception is raised if the string can not be located.


<!-- page: PyCListBox__SetCaretIndex_meth.html -->

## PyCListBox.SetCaretIndex

 SetCaretIndex(index, bScroll)

Sets the focus rectange to a specified item.

#### Parameters

- index : int

 The zero based index of the item.

- bScroll=1 : int

 Should the listbox scroll to the item?

#### MFC References

- CListBox::SetCaretIndex


<!-- page: PyCListBox__SetCurSel_meth.html -->

## PyCListBox.SetCurSel

 SetCurSel(index)

Selects an item in a single selection listbox.

#### Parameters

- index : int

 The zero based index of the item to select.

#### MFC References

- CListBox::SetCurSel


<!-- page: PyCListBox__SetItemData_meth.html -->

## PyCListBox.SetItemData

 int = SetItemData(item, Data )

Sets the item's application-specific object value.

#### Parameters

- item : int

 Index of the item whose Data is to be set.

- Data : object

 New value for the data.

#### Comments

 Note that a reference count is not added to the object. This it is your responsibility to make sure the object remains alive while in the list.


<!-- page: PyCListBox__SetItemValue_meth.html -->

## PyCListBox.SetItemValue

 int = SetItemValue(item, data )

Sets the item's application-specific value.

#### Parameters

- item : int

 Index of the item whose Data is to be set.

- data : int

 New value for the data.


<!-- page: PyCListBox__SetSel_meth.html -->

## PyCListBox.SetSel

 SetSel(index, bSel)

Selects an item in a multiple selection listbox.

#### Parameters

- index : int

 The zero based index of the item to select.

- bSel=1 : int

 Should the item be selected or deselected?

#### MFC References

- CListBox::SetSel


<!-- page: PyCListBox__SetTabStops_meth.html -->

## PyCListBox.SetTabStops

 SetTabStops(eachTabStop)

Sets the tab stops for a listbox.

#### Parameters

- eachTabStop : int

 The position for each tab stop.

#### Alternative Parameters

- tabStops

 Each individual tab stop.


<!-- page: PyCListBox__SetTopIndex_meth.html -->

## PyCListBox.SetTopIndex

 SetTopIndex(index)

Sets the top index (top most visible item) of the listbox.

#### Parameters

- index : int

 The zero based index of the item to place at the top of the list.

#### MFC References

- CListBox::SetTopIndex


---

<!-- object: PyCListCtrl -->


<!-- page: PyCListCtrl.html -->

---

## PyCListCtrl Object

 A class which encapsulates an MFC CListCtrl object. Derived from a PyCWnd object.

#### Methods

- Arrange

 Aligns items on a grid.

- CreateWindow

 Creates the actual window for the object.

- DeleteAllItems

 Deletes all items from the list.

- DeleteItem

 Deletes the specified item.

- GetTextColor

 Retrieves the text color of a list view control.

- SetTextColor

 Sets the text color of a list view control.

- GetBkColor

 Retrieves the background color of the control.

- SetBkColor

 Sets the background color of the control.

- GetItem

 Retrieves the details of an items attributes.

- GetItemCount

 Retrieves the number of items in a list view control.

- GetItemRect

 Retrieves the bounding rectangle of a list view item.

- GetEditControl

 Retrieves the handle of the edit control used to edit the specified list view item.

- EditLabel

 Edits a specified list view item in-place.

- EnsureVisible

 Ensures that a list view item is visible in its list view control.

- CreateDragImage

 Creates a dragging bitmap for the specified list view item.

- GetImageList

 Retrieves the current image list.

- GetNextItem

 Searches for a list view item with specified properties and with specified relationship to a given item.

- InsertColumn

 Inserts a column into a list control when in report view.

- InsertItem

 Inserts an item into the list.

- SetImageList

 Assigns an image list to a list view control.

- GetColumn

 Retrieves the details of a column in the control.

- GetTextBkColor

 Retrieves the text background color of a list view control.

- SetTextBkColor

 Sets the text background color of a list view control.

- GetTopIndex

 Retrieves the index of the topmost visible item.

- GetCountPerPage

 Calculates the number of items that can fit vertically in a list view control.

- GetSelectedCount

 Retrieves the number of selected items in the list view control.

- SetItem

 Sets some of all of an items attributes.

- SetItemState

 Changes the state of an item in a list view control.

- GetItemState

 Retrieves the state of a list view item.

- SetItemData

 Sets the item's application-specific value.

- GetItemData

 Retrieves the application-specific value associated with an item.

- SetItemCount

 Prepares a list view control for adding a large number of items.

- GetItemCount

 Retrieves the number of items in a list view control.

- SetItemText

 Changes the text of a list view item or subitem.

- GetItemText

 Retrieves the text of a list view item or subitem.

- RedrawItems

 Redraws a range of items

- Update

 Forces the control to repaint a specified item.

- SetColumn

 Sets the state of a column in a list control when in report view.

- DeleteColumn

 Deletes the specified column from the list control.

- GetColumnWidth

 Gets the width of the specified column in the list control.

- SetColumnWidth

 Sets the width of the specified column in the list control.

- GetStringWidth

 Gets the necessary column width to fully display this text in a column.

- HitTest

 Determines which list view item, if any, is at a specified position.

- GetItemPosition

 Determines the position of the specified item.


<!-- page: PyCListCtrl__Arrange_meth.html -->

## PyCListCtrl.Arrange

 Arrange(code)

Aligns items on a grid.

#### Parameters

- code : int

 Specifies the alignment style for the items


<!-- page: PyCListCtrl__CreateDragImage_meth.html -->

## PyCListCtrl.CreateDragImage

 PyCImageList,(x,y) = CreateDragImage(item)

Creates a dragging bitmap for the specified list view item.

#### Parameters

- item : int

 The index of the item to edit.


<!-- page: PyCListCtrl__CreateWindow_meth.html -->

## PyCListCtrl.CreateWindow

 CreateWindow(style, rect, PyCWnd, id)

Creates the actual window for the object.

#### Parameters

- style : int

 The window style

- rect : int, int, int, int

 The default rectangle

- PyCWnd : parent

 The parent window

- id : int

 The control ID

#### MFC References

- CListCtrl::Create


<!-- page: PyCListCtrl__DeleteAllItems_meth.html -->

## PyCListCtrl.DeleteAllItems

 DeleteAllItems()

Deletes all items from the list.


<!-- page: PyCListCtrl__DeleteColumn_meth.html -->

## PyCListCtrl.DeleteColumn

 int = DeleteColumn(first)

Deletes the specified column from the list control.

#### Parameters

- first : int

 Index of the column to be removed.


<!-- page: PyCListCtrl__DeleteItem_meth.html -->

## PyCListCtrl.DeleteItem

 DeleteItem(item)

Deletes the specified item.

#### Parameters

- item : int

 The item to delete.


<!-- page: PyCListCtrl__EditLabel_meth.html -->

## PyCListCtrl.EditLabel

 PyCEdit = EditLabel(item)

Edits a specified list view item in-place.

#### Parameters

- item : int

 The index of item to edit.


<!-- page: PyCListCtrl__EnsureVisible_meth.html -->

## PyCListCtrl.EnsureVisible

 int = EnsureVisible(item, bPartialOK )

Ensures that a list view item is visible in its list view control.

#### Parameters

- item : int

 The index of item to edit.

- bPartialOK : int

 Specifies whether partial visibility is acceptable.


<!-- page: PyCListCtrl__GetBkColor_meth.html -->

## PyCListCtrl.GetBkColor

 int = GetBkColor()

Retrieves the background color of the control.


<!-- page: PyCListCtrl__GetColumnWidth_meth.html -->

## PyCListCtrl.GetColumnWidth

 int = GetColumnWidth(first)

Gets the width of the specified column in the list control.

#### Parameters

- first : int

 Index of the column whose width is to be retrieved.


<!-- page: PyCListCtrl__GetColumn_meth.html -->

## PyCListCtrl.GetColumn

 LV_COLUMN = GetColumn(column)

Retrieves the details of a column in the control.

#### Parameters

- column : int

 The index of the column whose attributes are to be retrieved.


<!-- page: PyCListCtrl__GetCountPerPage_meth.html -->

## PyCListCtrl.GetCountPerPage

 int = GetCountPerPage()

Calculates the number of items that can fit vertically in a list view control.


<!-- page: PyCListCtrl__GetEditControl_meth.html -->

## PyCListCtrl.GetEditControl

 PyCEdit = GetEditControl()

Retrieves the handle of the edit control used to edit the specified list view item.


<!-- page: PyCListCtrl__GetImageList_meth.html -->

## PyCListCtrl.GetImageList

 PyCImageList = GetImageList(nImageList)

Retrieves the current image list.

#### Parameters

- nImageList : int

 Value specifying which image list to retrieve. It can be one of:
- commctrl.LVSIL_NORMAL Image list with large icons.
- commctrl.LVSIL_SMALL Image list with small icons.
- commctrl.LVSIL_STATE Image list with state images.


<!-- page: PyCListCtrl__GetItemCount_meth.html -->

## PyCListCtrl.GetItemCount

 int = GetItemCount()

Retrieves the number of items in a list view control.


<!-- page: PyCListCtrl__GetItemData_meth.html -->

## PyCListCtrl.GetItemData

 object = GetItemData(item)

Retrieves the application-specific value associated with an item.

#### Parameters

- item : int

 The index of the item whose data is to be retrieved.


<!-- page: PyCListCtrl__GetItemPosition_meth.html -->

## PyCListCtrl.GetItemPosition

 (int, int) = GetItemPosition(item)

Determines the position of the specified item.

#### Parameters

- item : int

 The item to determine the position for.


<!-- page: PyCListCtrl__GetItemRect_meth.html -->

## PyCListCtrl.GetItemRect

 (int, int, int, int) = GetItemRect(item, bTextOnly )

Retrieves the bounding rectangle of a list view item.

#### Parameters

- item : int

 Index of the item whose Data is to be set.

- bTextOnly : int

 f this parameter is nonzero, the bounding rectangle includes only the text of the item. Otherwise it includes the entire line that the item occupies in the list view control.


<!-- page: PyCListCtrl__GetItemState_meth.html -->

## PyCListCtrl.GetItemState

 int = GetItemState(item, mask )

Retrieves the state of a list view item.

#### Parameters

- item : int

 The index of the item whose position is to be retrieved.

- mask : int

 Mask specifying which of the item's state flags to return.


<!-- page: PyCListCtrl__GetItemText_meth.html -->

## PyCListCtrl.GetItemText

 int = GetItemText(item, sub )

Retrieves the text of a list view item or subitem.

#### Parameters

- item : int

 The index of the item whose text is to be retrieved.

- sub : int

 Specifies the subitem whose text is to be retrieved.


<!-- page: PyCListCtrl__GetItem_meth.html -->

## PyCListCtrl.GetItem

 LV_ITEM = GetItem(item, sub )

Retrieves the details of an items attributes.

#### Parameters

- item : int

 The index of the item whose attributes are to be retrieved.

- sub : int

 Specifies the subitem whose text is to be retrieved.


<!-- page: PyCListCtrl__GetNextItem_meth.html -->

## PyCListCtrl.GetNextItem

 int = GetNextItem(item, flags )

Searches for a list view item with specified properties and with specified relationship to a given item.

#### Parameters

- item : int

 Index of the item to begin the searching with, or -1 to find the first item that matches the specified flags. The specified item itself is excluded from the search.

- flags : int

 Geometric relation of the requested item to the specified item, and the state of the requested item. The geometric relation can be one of these values:
LVNI_ABOVE
LVNI_ALL
LVNI_BELOW
LVNI_TOLEFT
LVNI_TORIGHT
 The state can be zero, or it can be one or more of these values:
LVNI_DROPHILITED
LVNI_FOCUSED
LVNI_HIDDEN
LVNI_MARKED
LVNI_SELECTED
 If an item does not have all of the specified state flags set, the search continues with the next item.

#### Return Value

Returns an integer index, or raises a win32ui.error exception if not item can be found.


<!-- page: PyCListCtrl__GetSelectedCount_meth.html -->

## PyCListCtrl.GetSelectedCount

 int = GetSelectedCount()

Retrieves the number of selected items in the list view control.


<!-- page: PyCListCtrl__GetStringWidth_meth.html -->

## PyCListCtrl.GetStringWidth

 int = GetStringWidth(first)

Gets the necessary column width to fully display this text in a column.

#### Parameters

- first : int

 String that contains the text whose width is to be determined.

#### Comments

 Doesn't take the size of an included Image in account, only the size of the text is determined.


<!-- page: PyCListCtrl__GetTextBkColor_meth.html -->

## PyCListCtrl.GetTextBkColor

 int = GetTextBkColor()

Retrieves the text background color of a list view control.


<!-- page: PyCListCtrl__GetTextColor_meth.html -->

## PyCListCtrl.GetTextColor

 int = GetTextColor()

Retrieves the text color of a list view control.


<!-- page: PyCListCtrl__GetTopIndex_meth.html -->

## PyCListCtrl.GetTopIndex

 int = GetTopIndex()

Retrieves the index of the topmost visible item.


<!-- page: PyCListCtrl__HitTest_meth.html -->

## PyCListCtrl.HitTest

 (int, int, int) = HitTest(x,y)

Determines which list view item, if any, is at a specified position.

#### Parameters

- x,y : point

 The point to test.

#### Return Value

The result is a tuple of (flags, item, subItem). flags may be a combination of the following values:

| | Value | Description
| |

---

 |

---

| | commctrl.LVHT_ABOVE | The position is above the control's client area.
| | commctrl.LVHT_BELOW | The position is below the control's client area.
| | commctrl.LVHT_NOWHERE | The position is inside the list view control's client window, but it is not over a list item.
| | commctrl.LVHT_ONITEMICON | The position is over a list view item's icon.
| | commctrl.LVHT_ONITEMLABEL | The position is over a list view item's text.
| | commctrl.LVHT_ONITEMSTATEICON | The position is over the state image of a list view item.
| | commctrl.LVHT_TOLEFT | The position is to the left of the list view control's client area.
| | commctrl.LVHT_TORIGHT | The position is to the right of the list view control's client area.


<!-- page: PyCListCtrl__InsertColumn_meth.html -->

## PyCListCtrl.InsertColumn

 int = InsertColumn(colNo, item )

Inserts a column into a list control when in report view.

#### Parameters

- colNo : int

 The new column number

- item : LV_COLUMN

 A tuple describing the new column.


<!-- page: PyCListCtrl__InsertItem_meth.html -->

## PyCListCtrl.InsertItem

 int = InsertItem(item)

Inserts an item into the list.

#### Parameters

- item : LV_ITEM

 A tuple describing the new item.

#### Alternative Parameters

- item

 The index of the item.

- text

 The text of the item.

- image

 The index of the image to use.

#### Alternative Parameters

- item

 The index of the item.

- text

 The text of the item.


<!-- page: PyCListCtrl__RedrawItems_meth.html -->

## PyCListCtrl.RedrawItems

 int = RedrawItems(first, first )

Forces a listview to repaint a range of items.

#### Parameters

- first : int

 Index of the first item to be repainted.

- first : int

 Index of the last item to be repainted.

#### Comments

 The specified items are not actually repainted until the list view window receives a WM_PAINT message. To repaint immediately, call the Windows UpdateWindow function after using this function.


<!-- page: PyCListCtrl__SetBkColor_meth.html -->

## PyCListCtrl.SetBkColor

 SetBkColor(color)

Sets the background color of the control.

#### Parameters

- color : int

 The new background color.


<!-- page: PyCListCtrl__SetColumnWidth_meth.html -->

## PyCListCtrl.SetColumnWidth

 int = SetColumnWidth(first, first )

Sets the width of the specified column in the list control.

#### Parameters

- first : int

 Index of the column to be changed.

- first : int

 New width of the column.


<!-- page: PyCListCtrl__SetColumn_meth.html -->

## PyCListCtrl.SetColumn

 int = SetColumn(colNo, item )

Changes column state in a list control when in report view.

#### Parameters

- colNo : int

 The to be modified column number

- item : LV_COLUMN

 A tuple describing the modified column.


<!-- page: PyCListCtrl__SetImageList_meth.html -->

## PyCListCtrl.SetImageList

 int = SetImageList(imageList, imageType )

Assigns an image list to a list view control.

#### Parameters

- imageList : PyCImageList

 The Image List to use.

- imageType : int

 Type of image list. It can be one of (COMMCTRL.) LVSIL_NORMAL, LVSIL_SMALL or LVSIL_STATE


<!-- page: PyCListCtrl__SetItemCount_meth.html -->

## PyCListCtrl.SetItemCount

 SetItemCount(count)

Prepares a list view control for adding a large number of items.

#### Parameters

- count : int

 Number of items that the control will ultimately contain.

#### Comments

 By calling this function before adding a large number of items, you enable a list view control to reallocate its internal data structures only once rather than every time you add an item.


<!-- page: PyCListCtrl__SetItemData_meth.html -->

## PyCListCtrl.SetItemData

 int = SetItemData(item, Data )

Sets the item's application-specific value.

#### Parameters

- item : int

 Index of the item whose Data is to be set.

- Data : object

 New value for the data.

#### Comments

 Note that a reference count is not added to the object. This it is your responsibility to make sure the object remains alive while in the list.


<!-- page: PyCListCtrl__SetItemState_meth.html -->

## PyCListCtrl.SetItemState

 int = SetItemState(item, state , mask )

Changes the state of an item in a list view control.

#### Parameters

- item : int

 Index of the item whose state is to be set.

- state : int

 New values for the state bits.

- mask : int

 Mask specifying which state bits to change.


<!-- page: PyCListCtrl__SetItemText_meth.html -->

## PyCListCtrl.SetItemText

 int = SetItemText(item, sub , text )

Changes the text of a list view item or subitem.

#### Parameters

- item : int

 Index of the item whose text is to be set.

- sub : int

 Index of the subitem, or zero to set the item label.

- text : string

 String that contains the new item text.


<!-- page: PyCListCtrl__SetItem_meth.html -->

## PyCListCtrl.SetItem

 int = SetItem(item)

Sets some of all of an items attributes.

#### Parameters

- item : LV_ITEM

 A tuple describing the new item.


<!-- page: PyCListCtrl__SetTextBkColor_meth.html -->

## PyCListCtrl.SetTextBkColor

 SetTextBkColor(color)

Sets the text background color of a list view control.

#### Parameters

- color : int

 The new background color.


<!-- page: PyCListCtrl__SetTextColor_meth.html -->

## PyCListCtrl.SetTextColor

 SetTextColor(color)

Sets the text color of a list view control.

#### Parameters

- color : int

 The new color.


<!-- page: PyCListCtrl__Update_meth.html -->

## PyCListCtrl.Update

 Update(item)

Forces the control to repaint a specified item.

#### Parameters

- item : int

 The new color.


---

<!-- object: PyCListView -->


<!-- page: PyCListView.html -->

---

## PyCListView Object

 A class which implements a CListView. Derived from PyCView and PyCListCtrl objects.

#### Methods

- PreCreateWindow

 Calls the underlying MFC PreCreateWindow method.

- GetListCtrl

 Returns the underlying list control object.

- OnCommand

 Calls the standard Python framework OnCommand handler

#### Based On

PyCCtrlView


<!-- page: PyCListView__GetListCtrl_meth.html -->

## PyCListView.GetListCtrl

 PyCListCtrl = GetListCtrl()

Returns the underlying list control object.


<!-- page: PyCListView__OnCommand_meth.html -->

## PyCListView.OnCommand

 OnCommand(wparam, lparam)

Calls the standard Python framework OnCommand handler

#### Parameters

- wparam : int

- lparam : int

#### See Also

- PyCWnd.OnCommand virtual method


<!-- page: PyCListView__PreCreateWindow_meth.html -->

## PyCListView.PreCreateWindow

 tuple = PreCreateWindow(createStruct)

Calls the underlying MFC PreCreateWindow method.

#### Parameters

- createStruct : tuple

 A tuple representing a CREATESTRUCT structure.


---

<!-- object: PyCMDIChildWnd -->


<!-- page: PyCMDIChildWnd.html -->

---

## PyCMDIChildWnd Object

 A windows frame window. Encapsulates an MFC CMDIChildWindow class

#### Methods

- ActivateFrame

 Calls the underlying MFC ActivateFrame method.

- CreateWindow

 Creates the actual window for the PyCWnd object.

- GetMDIFrame

 Returns the MDI parent frame

- MDIActivate

 Activates the MDI frame independent of the main frame.

- PreCreateWindow

 Calls the underlying MFC PreCreateWindow method.

- PreTranslateMessage

 Calls the underlying MFC PreTranslateMessage method.

- OnCommand

 Calls the standard Python framework OnCommand handler

- OnClose

 Calls the standard Python framework OnClose handler

#### Based On

PyCFrameWnd


<!-- page: PyCMDIChildWnd__ActivateFrame_meth.html -->

## PyCMDIChildWnd.ActivateFrame

 ActivateFrame(cmdShow)

Calls the underlying MFC ActivateFrame method.

#### Parameters

- cmdShow=-1 : int

 The status of the window.

#### See Also

- PyCMDIChildWnd.ActivateFrame virtual method


<!-- page: PyCMDIChildWnd__ActivateFrame_virtual.html -->

## PyCMDIChildWnd.ActivateFrame Virtual

 ActivateFrame(cmdShow)

Called to activate the frame window.

#### Parameters

- cmdShow : int

 The parameter to be passed to PyCWnd::ShowWindow

#### Comments

 If a handler for this function exists, then the base MFC implementation will not be called. If you wish to use the default functionality, PyCMDIFrameWnd::ActivateFrame can be called.
If there is no handler, the base MFC implementation will be called.

#### See Also

- PyCMDIChildWnd::ActivateFrame


<!-- page: PyCMDIChildWnd__CreateWindow_meth.html -->

## PyCMDIChildWnd.CreateWindow

 tuple = CreateWindow(wndClass, title , style , rect , PyCWnd , createContext )

Creates the actual window for the PyCWnd object.

#### Parameters

- wndClass : string

 The window class name, or None

- title : string

 The window title

- style=WS_CHILD | WS_VISIBLE | WS_OVERLAPPEDWINDOW : int

 The window style

- rect=None : int, int, int, int

 The default rectangle

- PyCWnd=None : parent

 The parent window

- createContext=None : tuple

 A tuple representing a CREATECONTEXT structure.

#### Comments

 You do not need to call this method if you use the MFC Document/View framework.


<!-- page: PyCMDIChildWnd__GetMDIFrame_meth.html -->

## PyCMDIChildWnd.GetMDIFrame

 GetMDIFrame()

Returns the MDI parent frame


<!-- page: PyCMDIChildWnd__GetMessageString_virtual.html -->

## PyCMDIChildWnd.GetMessageString Virtual

 GetMessageString(id)

Gets the message string to use for a control specific ID.

#### Parameters

- id : int

 The command ID to retrieve the string for.

#### See Also

- PyCMDIChildWnd::GetMessageString


<!-- page: PyCMDIChildWnd__MDIActivate_meth.html -->

## PyCMDIChildWnd.MDIActivate

 MDIActivate(cmdShow)

Activates the MDI frame independent of the main frame.

#### Parameters

- cmdShow=-1 : int

 The status of the window.

#### See Also

- PyCWnd.OnMDIActivate virtual method


<!-- page: PyCMDIChildWnd__OnClose_meth.html -->

## PyCMDIChildWnd.OnClose

 OnClose()

Calls the standard Python framework OnClose handler

#### See Also

- PyCWnd.OnClose virtual method


<!-- page: PyCMDIChildWnd__OnCommand_meth.html -->

## PyCMDIChildWnd.OnCommand

 OnCommand(wparam, lparam)

Calls the standard Python framework OnCommand handler

#### Parameters

- wparam : int

- lparam : int

#### See Also

- PyCWnd.OnCommand virtual method


<!-- page: PyCMDIChildWnd__OnCreateClient_virtual.html -->

## PyCMDIChildWnd.OnCreateClient Virtual

 OnCreateClient(CREATESTRUCT, object )

Called by the framework during the execution of OnCreate.

#### Parameters

- CREATESTRUCT : tuple

 A tuple describing a CREATESTRUCT structure.

- object : object

 A Python object initially passed to LoadFrame

#### Return Value

The return value from this method is ignored, but an exception will prevent window creation.


<!-- page: PyCMDIChildWnd__PreCreateWindow_meth.html -->

## PyCMDIChildWnd.PreCreateWindow

 tuple = PreCreateWindow(createStruct)

Calls the underlying MFC PreCreateWindow method.

#### Parameters

- createStruct : tuple

 A tuple representing a CREATESTRUCT structure.

#### See Also

- PyCWnd.PreCreateWindow virtual method


<!-- page: PyCMDIChildWnd__PreTranslateMessage_meth.html -->

## PyCMDIChildWnd.PreTranslateMessage

 PreTranslateMessage()

Calls the base PreTranslateMessage handler

#### See Also

- PyCWnd.PreTranslateMessage virtual method


---

<!-- object: PyCMDIFrameWnd -->


<!-- page: PyCMDIFrameWnd.html -->

---

## PyCMDIFrameWnd Object

 A main application frame window. Encapsulates an MFC CMDIFrameWnd class

#### Methods

- GetMDIClient

 Returns the MDI client window

- MDIGetActive

 Retrieves the current active MDI child window, along with a flag indicating whether the child window is maximized.

- MDIActivate

 Activate an MDI child window

- MDINext

 Activates the next MDI window

- PreCreateWindow

 Calls the underlying MFC PreCreateWindow method.

- PreTranslateMessage

 Calls the underlying MFC PreTranslateMessage method.

- OnCommand

 Calls the standard Python framework OnCommand handler

- OnContextHelp

 Calls the underlying MFC OnContextHelp method.

- OnClose

 Calls the standard Python framework OnClose handler

#### Based On

PyCFrameWnd


<!-- page: PyCMDIFrameWnd__GetMDIClient_meth.html -->

## PyCMDIFrameWnd.GetMDIClient

 PyCMDIFrameWnd = GetMDIClient()

Returns the MDI client window


<!-- page: PyCMDIFrameWnd__MDIActivate_meth.html -->

## PyCMDIFrameWnd.MDIActivate

 PyCMDIFrameWnd = MDIActivate(window)

Activate an MDI child window

#### Parameters

- window : PyCWnd

 The window to activate.


<!-- page: PyCMDIFrameWnd__MDIGetActive_meth.html -->

## PyCMDIFrameWnd.MDIGetActive

 (PyCMDIChildWnd, int) = MDIGetActive()

Retrieves the current active MDI child window, along with a flag indicating whether the child window is maximized.


<!-- page: PyCMDIFrameWnd__MDINext_meth.html -->

## PyCMDIFrameWnd.MDINext

 MDINext(fNext)

Activates the next MDI window

#### Parameters

- fNext=0 : int

 Indicates if the next (0) or previous (non-zero) window is requested.

#### Comments

 Unlike MFC, this version supports the fNext param in the WM_MDINEXT message.


<!-- page: PyCMDIFrameWnd__OnClose_meth.html -->

## PyCMDIFrameWnd.OnClose

 OnClose()

Calls the standard Python framework OnClose handler


<!-- page: PyCMDIFrameWnd__OnCommand_meth.html -->

## PyCMDIFrameWnd.OnCommand

 OnCommand(wparam, lparam)

Calls the standard Python framework OnCommand handler

#### Parameters

- wparam : int

- lparam : int

#### See Also

- PyCWnd.OnCommand virtual method


<!-- page: PyCMDIFrameWnd__OnContextHelp_meth.html -->

## PyCMDIFrameWnd.OnContextHelp

 None = OnContextHelp()

Calls the underlying MFC OnContextHelp method.


<!-- page: PyCMDIFrameWnd__PreCreateWindow_meth.html -->

## PyCMDIFrameWnd.PreCreateWindow

 tuple = PreCreateWindow(createStruct)

Calls the underlying MFC PreCreateWindow method.

#### Parameters

- createStruct : tuple

 A tuple representing a CREATESTRUCT structure.

#### See Also

- PyCWnd.PreCreateWindow virtual method


<!-- page: PyCMDIFrameWnd__PreTranslateMessage_meth.html -->

## PyCMDIFrameWnd.PreTranslateMessage

 PreTranslateMessage()

Calls the base PreTranslateMessage handler

#### See Also

- PyCWnd.PreTranslateMessage virtual method


---

<!-- object: PyCMINVOKECOMMANDINFO -->


<!-- page: PyCMINVOKECOMMANDINFO.html -->

---

## PyCMINVOKECOMMANDINFO Object

 A tuple of parameters to be converted to a CMINVOKECOMMANDINFO struct

#### Items

- [0] int : Mask

 Combination of shellcon.CMIC_MASK_* constants, can be 0

- [1] PyHANDLE : hwnd

 Window that owns the shortcut menu

- [2] int or str : Verb

 Action to be carried out, specified as a string command or integer menu item id

- [3] str : Parameters

 Extra parameters to be passed to the command line for the action, can be None

- [4] str : Directory

 Working directory, can be None

- [5] int : Show

 Combination of win32con.SW_* constants for any windows that may be created

- [6] int : HotKey

 Hot key for any application that may be started

- [7] PyHANDLE : Icon

 Handle to icon to use for application, can be None


---

<!-- object: PyCMenu -->


<!-- page: PyCMenu.html -->

---

## PyCMenu Object

 A windows menu. Encapsulates an MFC CMenu class

#### Methods

- AppendMenu

 Appends a new item to the end of a menu. Python can specify the state of the menu item by setting values in nFlags.

- DeleteMenu

 Deletes the specified menu item.

- EnableMenuItem

 Enables, disables, or dims a menu item.

- GetHandle

 Returns the menu object's underlying hMenu.

- GetMenuItemCount

 Determines the number of items in a menu.

- GetMenuItemID

 Returns the item ID for the specified item in a pop-up menu.

- GetMenuString

 Returns the string for a specified menu item.

- GetSubMenu

 Returns a submenu.

- InsertMenu

 Inserts an item into a menu.

- ModifyMenu

 Modify an item in a menu.

- TrackPopupMenu

 Creates a popup menu anywhere on the screen.


<!-- page: PyCMenu__AppendMenu_meth.html -->

## PyCMenu.AppendMenu

 AppendMenu(flags, id, value)

Appends a new item to the end of a menu. Python can specify the state of the menu item by setting values in nFlags.

#### Parameters

- flags : int

 Specifies information about the state of the new menu item when it is added to the menu. May be a combination of the win32con.MF_* values.

- id=0 : int

 Specifies either the command ID of the new menu item.

- value=None : string/None

 Specifies the content of the new menu item. If used, flags must contain win32con.MF_STRING.


<!-- page: PyCMenu__DeleteMenu_meth.html -->

## PyCMenu.DeleteMenu

 string = DeleteMenu(id, flags )

Deletes the specified menu item.

#### Parameters

- id : int

 The id of the item being deleted.

- flags : int

 Specifies how the id parameter is interpreted. It must be one of win32con.MF_BYCOMMAND or win32con.MF_BYPOSITION.


<!-- page: PyCMenu__EnableMenuItem_meth.html -->

## PyCMenu.EnableMenuItem

 int = EnableMenuItem(id, flags )

Enables, disables, or dims a menu item.

#### Parameters

- id : int

 Specifies the command ID of the menu item. This parameter can specify pop-up menu items as well as standard menu items.

- flags : int

 Specifies the action to take. It can be a combination of MF_DISABLED, MF_ENABLED, or MF_GRAYED, with MF_BYCOMMAND or MF_BYPOSITION

#### Comments

 The PyCMenu::CreateMenu , PyCMenu::InsertMenu, PyCMenu::ModifyMenu, and PyCMenu::LoadMenuIndirect member functions can also set the state (enabled, disabled, or dimmed) of a menu item.


<!-- page: PyCMenu__GetHandle_meth.html -->

## PyCMenu.GetHandle

 int = GetHandle()

Returns the menu object's underlying hMenu.


<!-- page: PyCMenu__GetMenuItemCount_meth.html -->

## PyCMenu.GetMenuItemCount

 int = GetMenuItemCount()

Determines the number of items in a menu.

#### Return Value

The number of items in the menu if the function is successful; otherwise -1.


<!-- page: PyCMenu__GetMenuItemID_meth.html -->

## PyCMenu.GetMenuItemID

 int = GetMenuItemID(pos)

Returns the item ID for the specified item in a pop-up menu.

#### Parameters

- pos : int

 The position (zero-based) of the menu item whose ID is being retrieved.

#### Comments

 If the specified item is a pop-up menu (as opposed to an item within the pop-up menu), the return value is -1. If nPos corresponds to a SEPARATOR menu item, the return value is 0.


<!-- page: PyCMenu__GetMenuString_meth.html -->

## PyCMenu.GetMenuString

 string = GetMenuString(id, flags )

Returns the string for a specified menu item.

#### Parameters

- id : int

 The id of the item being requested.

- flags=win32con.MF_BYCOMMAND : int

 Specifies how the id parameter is interpreted. It must be one of win32con.MF_BYCOMMAND or win32con.MF_BYPOSITION.


<!-- page: PyCMenu__GetSubMenu_meth.html -->

## PyCMenu.GetSubMenu

 PyCMenu = GetSubMenu(pos)

Returns a submenu.

#### Parameters

- pos : int

 The position (zero-based) of the menu item being retrieved.


<!-- page: PyCMenu__InsertMenu_meth.html -->

## PyCMenu.InsertMenu

 InsertMenu(pos, flags, id, value)

Inserts an item into a menu.

#### Parameters

- pos : int

 The position (zero-based) the item should be inserted.

- flags : int

 Flags for the new item.

- id=0 : int/PyCMenu

 The ID for a new menu item, or handle to a submenu

- value=None : string/None

 A string for the menu item.


<!-- page: PyCMenu__ModifyMenu_meth.html -->

## PyCMenu.ModifyMenu

 ModifyMenu(pos, flags, id, value)

Modify an item in a menu.

#### Parameters

- pos : int

 The position (zero-based) the item to be changed.

- flags : int

 Flags for the item.

- id=0 : int

 The ID for the item.

- value=None : string/None

 A string for the menu item.


<!-- page: PyCMenu__TrackPopupMenu_meth.html -->

## PyCMenu.TrackPopupMenu

 TrackPopupMenu((x,y), flags, owner)

Creates a popup menu anywhere on the screen.

#### Parameters

- (x,y) : (int, int)

 The position for the menu..

- flags=win32con.TPM_LEFTALIGN|win32con.TPM_LEFTBUTTON|win32con.TPM_RIGHTBUTTON : int

 Flags for the menu.

- owner=(main application frame) : PyCWnd

 The owner of the menu.

#### Comments

 The TrackPopupMenu function displays a floating pop-up menu at the specified location and tracks the selection of items on the pop-up menu. The floating pop-up menu can appear anywhere on the screen.

#### Return Value

If the underlying MFC function fails, but TPM_RETURNCMD is set in the flags parameter, then None is returned instead of the normal exception.


---

<!-- object: PyCOMSTAT -->


<!-- page: PyCOMSTAT.html -->

---

## PyCOMSTAT Object

 A Python object, representing an COMSTAT structure

#### Properties

- integer cbInQue
 Specifies the number of bytes received by the serial provider but not yet read by a win32file::ReadFile operation

- integer cbOutQue
 Specifies the number of bytes of user data remaining to be transmitted for all write operations. This value will be zero for a nonoverlapped write.

- integer fCtsHold
 Specifies whether transmission is waiting for the CTS (clear-to-send) signal to be sent. If this member is TRUE, transmission is waiting.

- integer fDsrHold
 Specifies whether transmission is waiting for the DSR (data-set-ready) signal to be sent. If this member is TRUE, transmission is waiting.

- integer fRlsdHold
 Specifies whether transmission is waiting for the RLSD (receive-line-signal-detect) signal to be sent. If this member is TRUE, transmission is waiting.

- integer fXoffHold
 Specifies whether transmission is waiting because the XOFF character was received. If this member is TRUE, transmission is waiting.

- integer fXoffSent
 Specifies whether transmission is waiting because the XOFF character was transmitted. If this member is TRUE, transmission is waiting. Transmission halts when the XOFF character is transmitted to a system that takes the next character as XON, regardless of the actual character.

- integer fEof
 Specifies whether the end-of-file (EOF) character has been received. If this member is TRUE, the EOF character has been received.

- integer fTxim
 If this member is TRUE, there is a character queued for transmission that has come to the communications device by way of the TransmitCommChar function. The communications device transmits such a character ahead of other characters in the device's output buffer.

- integer fReserved
 Reserved; do not use.


---

<!-- object: PyCOORD -->


<!-- page: PyCOORD.html -->

---

## PyCOORD Object

 Wrapper for a COORD struct. Create using PyCOORDType(X,Y)

#### Properties

- int X
 Horizontal coordinate

- int Y
 Vertical coordinate


---

<!-- object: PyCOleClientItem -->


<!-- page: PyCOleClientItem.html -->

---

## PyCOleClientItem Object

 An OLE client item class. Encapsulates an MFC COleClientItem class

#### Methods

- CreateNewItem

 Creates an embedded item.

- Close

 Closes the item.

- DoVerb

 Executes the specified verb.

- Draw

 Draws the OLE item into the specified bounding rectangle using the specified device context.

- GetActiveView

 Obtains the active view for the item

- GetDocument

 Obtains the current document for the item

- GetInPlaceWindow

 Obtains the window in which the item has been opened for in-place editing.

- GetItemState

 Obtains the OLE item's current state

- GetObject

 Returns the COM object to the item. This is the m_lpObject variable in MFC.

- GetStorage

 Returns the COM object used for storage

- OnActivate

 Calls the underlying MFC handler.

- OnChange

 Calls the underlying MFC handler.

- OnChangeItemPosition

 Calls the underlying MFC method.

- OnDeactivateUI

 Calls the underlying MFC method.

- Run

 Runs the application associated with this item.

- SetItemRects

 Sets the bounding rectangle or the visible rectangle of the OLE item.


<!-- page: PyCOleClientItem__Close_meth.html -->

## PyCOleClientItem.Close

 Close()

Closes the item


<!-- page: PyCOleClientItem__CreateNewItem_meth.html -->

## PyCOleClientItem.CreateNewItem

 CreateNewItem()

Creates an embedded item.


<!-- page: PyCOleClientItem__DoVerb_meth.html -->

## PyCOleClientItem.DoVerb

 DoVerb()

Executes the specified verb.


<!-- page: PyCOleClientItem__Draw_meth.html -->

## PyCOleClientItem.Draw

 Draw()

Draws the OLE item into the specified bounding rectangle using the specified device context.


<!-- page: PyCOleClientItem__GetActiveView_meth.html -->

## PyCOleClientItem.GetActiveView

 PyCView = GetActiveView()

Obtains the active view for the item


<!-- page: PyCOleClientItem__GetDocument_meth.html -->

## PyCOleClientItem.GetDocument

 PyCDocument = GetDocument()

Obtains the current document for the item


<!-- page: PyCOleClientItem__GetInPlaceWindow_meth.html -->

## PyCOleClientItem.GetInPlaceWindow

 PyCWnd = GetInPlaceWindow()

Obtains the window in which the item has been opened for in-place editing.


<!-- page: PyCOleClientItem__GetItemState_meth.html -->

## PyCOleClientItem.GetItemState

 GetItemState()

Obtains the OLE item's current state


<!-- page: PyCOleClientItem__GetObject_meth.html -->

## PyCOleClientItem.GetObject

 PyIUnknown = GetObject()

Returns the COM object to the item. This is the m_lpObject variable in MFC.


<!-- page: PyCOleClientItem__GetStorage_meth.html -->

## PyCOleClientItem.GetStorage

 GetStorage()

Returns the COM object used for storage


<!-- page: PyCOleClientItem__OnActivate_meth.html -->

## PyCOleClientItem.OnActivate

 OnActivate()

Calls the underlying MFC method.


<!-- page: PyCOleClientItem__OnActivate_virtual.html -->

## PyCOleClientItem.OnActivate Virtual

 OnActivate()


<!-- page: PyCOleClientItem__OnChangeItemPosition_meth.html -->

## PyCOleClientItem.OnChangeItemPosition

 int = OnChangeItemPosition()

Calls the underlying MFC method.

#### Return Value

The result is a BOOL indicating if the function succeeded. No exception is thrown.


<!-- page: PyCOleClientItem__OnChangeItemPosition_virtual.html -->

## PyCOleClientItem.OnChangeItemPosition Virtual

 OnChangeItemPosition((left, top, right, bottom))

#### Parameters

- (left, top, right, bottom) : (int, int, int, int)

 The new position


<!-- page: PyCOleClientItem__OnChange_meth.html -->

## PyCOleClientItem.OnChange

 OnChange()

Calls the underlying MFC method.


<!-- page: PyCOleClientItem__OnChange_virtual.html -->

## PyCOleClientItem.OnChange Virtual

 OnChange(wNotification, dwParam )

#### Parameters

- wNotification : int

- dwParam : int


<!-- page: PyCOleClientItem__OnDeactivateUI_meth.html -->

## PyCOleClientItem.OnDeactivateUI

 int = OnDeactivateUI()

Calls the underlying MFC method.


<!-- page: PyCOleClientItem__OnDeactivateUI_virtual.html -->

## PyCOleClientItem.OnDeactivateUI Virtual

 OnDeactivateUI(bUndoable)

#### Parameters

- bUndoable : int


<!-- page: PyCOleClientItem__OnGetItemPosition_virtual.html -->

## PyCOleClientItem.OnGetItemPosition Virtual

 OnGetItemPosition()


<!-- page: PyCOleClientItem__Run_meth.html -->

## PyCOleClientItem.Run

 Run()

Runs the application associated with this item.


<!-- page: PyCOleClientItem__SetItemRects_meth.html -->

## PyCOleClientItem.SetItemRects

 SetItemRects()

Sets the bounding rectangle or the visible rectangle of the OLE item.


---

<!-- object: PyCOleDialog -->


<!-- page: PyCOleDialog.html -->

---

## PyCOleDialog Object

 An abstract class which encapsulates an MFC COleDialog object. Derived from a PyCCommonDialog object.


---

<!-- object: PyCOleDocument -->


<!-- page: PyCOleDocument.html -->

---

## PyCOleDocument Object

 An OLE document class. Encapsulates an MFC COleDocument class

#### Methods

- EnableCompoundFile

 Call this function if you want to store the document using the compound-file format

- GetStartPosition

 Obtains the position of the first item in the document.

- GetNextItem

 Call this function repeatedly to access each of the items in your document.

- GetInPlaceActiveItem

 Obtains the OLE item that is currently activated in place in the frame window containing the view identified by obWnd. sentinel


<!-- page: PyCOleDocument__EnableCompoundFile_meth.html -->

## PyCOleDocument.EnableCompoundFile

 EnableCompoundFile(bEnable)

Call this function if you want to store the document using the compound-file format.

#### Parameters

- bEnable=1 : int

 Specifies whether compound file support is enabled or disabled.


<!-- page: PyCOleDocument__GetInPlaceActiveItem_meth.html -->

## PyCOleDocument.GetInPlaceActiveItem

 PyCOleClientItem = GetInPlaceActiveItem(wnd)

Obtains the OLE item that is currently activated in place in the frame window containing the view identified by obWnd.

#### Parameters

- wnd : PyCWnd

 The window.


<!-- page: PyCOleDocument__GetNextItem_meth.html -->

## PyCOleDocument.GetNextItem

 (POSITION, PyCOleClientItem) = GetNextItem(pos)

Call this function repeatedly to access each of the items in your document.

#### Parameters

- pos : POSITION

 The position to iterate from.


<!-- page: PyCOleDocument__GetStartPosition_meth.html -->

## PyCOleDocument.GetStartPosition

 POSITION = GetStartPosition()

Obtains the position of the first item in the document.


---

<!-- object: PyCOleInsertDialog -->


<!-- page: PyCOleInsertDialog.html -->

---

## PyCOleInsertDialog Object

 An OLE 'Insert Object' dialog. Encapsulates an MFC COleInsertDialog class

#### Methods

- GetClassID

 Returns the CLSID associated with the selected item

- GetSelectionType

 Returns the type of selection made

- GetPathName

 Returns the full path to the file selected in the dialog box


<!-- page: PyCOleInsertDialog__GetClassID_meth.html -->

## PyCOleInsertDialog.GetClassID

 CLSID = GetClassID()

Returns the CLSID associated with the selected item


<!-- page: PyCOleInsertDialog__GetPathName_meth.html -->

## PyCOleInsertDialog.GetPathName

 CLSID = GetPathName()

Returns the full path to the file selected in the dialog box

#### Comments

 Do not call this if the selection type is createNewItem,


<!-- page: PyCOleInsertDialog__GetSelectionType_meth.html -->

## PyCOleInsertDialog.GetSelectionType

 CLSID = GetSelectionType()

Returns the type of selection made


---

<!-- object: PyCPrintDialog -->


<!-- page: PyCPrintDialog.html -->

---

## PyCPrintDialog Object

 An object which encapsulates an MFC CPrintDialog object.

#### Based On

PyCCommonDialogPyCCommonDialog


<!-- page: PyCPrintDialog__OnCancel_virtual.html -->

## PyCPrintDialog.OnCancel Virtual

 OnCancel()

Called by the MFC architecture when the user selects the Cancel button.

#### Comments

 The procedure is expected to dismiss the window with the PyCPrintDialog::EndDialog method. The base implementation (which dismisses the dialog) is not called if a handler exists. This can be done via PyCPrintDialog::OnCancel .

#### See Also

- PyCDialog::OnCancel


<!-- page: PyCPrintDialog__OnOK_virtual.html -->

## PyCPrintDialog.OnOK Virtual

 OnOK()

Called by the MFC architecture when the user selects the OK button.

#### Comments

 The procedure is expected to dismiss the window with the PyCPrintDialog::EndDialog method. The base implementation (which dismisses the dialog) is not called if a handler exists. This can be done via PyCPrintDialog::OnOK .

#### See Also

- PyCDialogDialog::OnOK


---

<!-- object: PyCPrintInfo -->


<!-- page: PyCPrintInfo.html -->

---

## PyCPrintInfo Object

 Encapsulates an MFC CPrintInfo class, its member CPrintDialog class, and the PRINTDLG structure member of the CPrintDialog.

#### Methods

- DocObject

 A flag indicating whether the document being printed is a DocObject.

- GetDwFlags

 A flags specifying DocObject printing operations. Valid only if data member m_bDocObject is TRUE.

- SetDwFlags

 Set a flag specifying DocObject printing operations. Valid only if data member m_bDocObject is TRUE.

- GetDocOffsetPage

 Get the number of pages preceding the first page of a particular DocObject in a combined DocObject print job.

- SetDocOffsetPage

 Set the number of pages preceding the first page of a particular DocObject in a combined DocObject print job.

- SetPrintDialog

 Set a pointer to the CPrintDialog object used to display the Print dialog box for the print job.

- GetDirect

 TRUE if the Print dialog box will be bypassed for direct printing; FALSE otherwise.

- SetDirect

 Sets to TRUE if the Print dialog box will be bypassed for direct printing; FALSE otherwise.

- GetPreview

 A flag indicating whether the document is being previewed.

- SetPreview

 Set whether the document is being previewed.

- GetContinuePrinting

 A flag indicating whether the framework should continue the print loop.

- SetContinuePrinting

 Set whether the framework should continue the print loop.

- GetCurPage

 Get the number of the current page.

- SetCurPage

 Set the number of the current page.

- GetNumPreviewPages

 Get the number of pages displayed in preview mode.

- SetNumPreviewPages

 Set the number of pages displayed in preview mode.

- GetUserData

 Get a user-created structure.

- SetUserData

 Set a user-created structure.

- GetDraw

 Get the usable drawing area of the page in logical coordinates.

- SetDraw

 Set the usable drawing area of the page in logical coordinates.

- GetPageDesc

 Get the format string used to display the page numbers during print preview

- SetPageDesc

 Set the format string used to display the page numbers during print preview

- GetMinPage

 Get the number of the first page of the document.

- SetMinPage

 Set the number of the first page of the document.

- GetMaxPage

 Get the number of the last page of the document.

- SetMaxPage

 Set the number of the last page of the document.

- GetOffsetPage

 Get the number of pages preceding the first page of a DocObject item being printed in a combined DocObject print job.

- GetFromPage

 The number of the first page to be printed.

- GetToPage

 The number of the last page to be printed.

- SetHDC

 Sets the printer DC compatible with the users choices, call after the print dialog DoModal finishes.

- CreatePrinterDC

 Handle to the newly created printer device context, call only after DoModal finishes.

- DoModal

 Call DoModal on the dialog.

- GetCopies

 The number of copies requested, call only after DoModal finishes.

- GetDefaults

 Retrieves device defaults without displaying a dialog box.

- FreeDefaults

 After a call to GetDefaults, and you are through with the CPrintDialog object, this call deletes the printer DC and calls GlobalFree function on the handles.

- GetDeviceName

 The name of the currently selected printer, call only after DoModal finishes.

- GetDriverName

 The name of the currently selected printer device driver, call only after DoModal finishes.

- GetDlgFromPage

 Retrieves the starting page of the print range.

- GetDlgToPage

 Retrieves the ending page of the print range.

- GetPortName

 The name of the currently selected printer port, call only after DoModal finishes.

- GetPrinterDC

 A handle to the printer device context if successful; otherwise NULL. If the bPrintSetupOnly parameter of the CPrintDialog constructor was FALSE (indicating that the Print dialog box is displayed), then GetPrinterDC returns a handle to the printer device context. You must call the WindowsDeleteDC function to delete the device context when you are done using it.

- PrintAll

 Nonzero if all pages in the document are to be printed; otherwise 0, call only after DoModal finishes.

- PrintCollate

 Nonzero if the user selects the collate check box in the dialog box; otherwise 0, call only after DoModal finishes.

- PrintRange

 Nonzero if only a range of pages in the document are to be printed; otherwise 0, call only after DoModal finishes.

- PrintSelection

 Nonzero if only the selected items are to be printed; otherwise 0., call only after DoModal finishes

- GetHDC

 Identifies a device context or an information context, depending on whether the Flags member specifies the PD_RETURNDC or PC_RETURNIC flag. If neither flag is specified, the value of this member is undefined. If both flags are specified, PD_RETURNDC has priority.

- GetFlags

 A set of bit flags that you can use to initialize the Print common dialog box. When the dialog box returns, it sets these flags to indicate the user's input.

- SetFlags

 A set of bit flags that you can use to initialize the Print common dialog box. When the dialog box returns, it sets these flags to indicate the user's input.

- SetFromPage

 The number of the first page to be printed.

- SetToPage

 The number of the first page to be printed.

- GetPRINTDLGMinPage

 Get the minimum value for the page range specified in the From and To page edit controls. If nMinPage equals nMaxPage, the Pages radio button and the starting and ending page edit controls are disabled.

- SetPRINTDLGMinPage

 Set the minimum value for the page range specified in the From and To page edit controls. If nMinPage equals nMaxPage, the Pages radio button and the starting and ending page edit controls are disabled.

- GetPRINTDLGCopies

 Gets the initial number of copies for the Copies edit control if hDevMode is NULL; otherwise, the dmCopies member of the DEVMODE structure contains the initial value.

- SetPRINTDLGCopies

 Sets the initial number of copies for the Copies edit control if hDevMode is NULL; otherwise, the dmCopies member of the DEVMODE structure contains the initial value.


<!-- page: PyCPrintInfo__CreatePrinterDC_meth.html -->

## PyCPrintInfo.CreatePrinterDC

 CreatePrinterDC()

Handle to the newly created printer device context, call only after DoModal finishes.

#### MFC References

- CPrintDialog::CreatePrinterDC


<!-- page: PyCPrintInfo__DoModal_meth.html -->

## PyCPrintInfo.DoModal

 DoModal()

Call DoModal on the dialog.

#### MFC References

- CPrintDialog::DoModal


<!-- page: PyCPrintInfo__DocObject_meth.html -->

## PyCPrintInfo.DocObject

 DocObject()

Return true if the document being printed is a DocObject.

#### MFC References

- CPrintInfo::m_bDocObject


<!-- page: PyCPrintInfo__FreeDefaults_meth.html -->

## PyCPrintInfo.FreeDefaults

 FreeDefaults()

After a call to GetDefaults, and you are through with the CPrintDialog object, this call deletes the printer DC and calls GlobalFree function on the handles.

#### MFC References

- CPrintDialog::GetDefaults


<!-- page: PyCPrintInfo__GetContinuePrinting_meth.html -->

## PyCPrintInfo.GetContinuePrinting

 GetContinuePrinting()

A flag indicating whether the framework should continue the print loop.

#### MFC References

- CPrintInfo::m_bContinuePrinting


<!-- page: PyCPrintInfo__GetCopies_meth.html -->

## PyCPrintInfo.GetCopies

 GetCopies()

The number of copies requested, call only after DoModal finishes.

#### MFC References

- CPrintDialog::GetCopies


<!-- page: PyCPrintInfo__GetCurPage_meth.html -->

## PyCPrintInfo.GetCurPage

 GetCurPage()

Get the number of the current page.

#### MFC References

- CPrintInfo::m_nCurPage


<!-- page: PyCPrintInfo__GetDefaults_meth.html -->

## PyCPrintInfo.GetDefaults

 GetDefaults()

Nonzero if the function was successful; otherwise 0. Call this function to retrieve the device defaults of the default printer without displaying a dialog box. The retrieved values are placed in the m_pd structure. In some cases, a call to this function will call the constructor for CPrintDialog with bPrintSetupOnly set to FALSE. In these cases, a printer DC and hDevNames and hDevMode (two handles located in the m_pd data member) are automatically allocated. If the constructor for CPrintDialog was called with bPrintSetupOnly set to FALSE, this function will not only return hDevNames and hDevMode (located in m_pd.hDevNames and m_pd.hDevMode) to the caller, but will also return a printer DC in m_pd.hDC. It is the responsibility of the caller to delete the printer DC and call the WindowsGlobalFree function on the handles when you are finished with the CPrintDialog object.

#### MFC References

- CPrintDialog::GetDefaults


<!-- page: PyCPrintInfo__GetDeviceName_meth.html -->

## PyCPrintInfo.GetDeviceName

 GetDeviceName()

The name of the currently selected printer, call only after DoModal finishes.

#### MFC References

- CPrintDialog::GetDeviceName


<!-- page: PyCPrintInfo__GetDirect_meth.html -->

## PyCPrintInfo.GetDirect

 GetDirect()

TRUE if the Print dialog box will be bypassed for direct printing; FALSE otherwise.

#### MFC References

- CPrintInfo::m_bDirect


<!-- page: PyCPrintInfo__GetDlgFromPage_meth.html -->

## PyCPrintInfo.GetDlgFromPage

 GetDlgFromPage()

Retrieves the starting page of the print range.

#### MFC References

- CPrintDialog::GetDlgFromPage


<!-- page: PyCPrintInfo__GetDlgToPage_meth.html -->

## PyCPrintInfo.GetDlgToPage

 GetDlgToPage()

Retrieves the ending page of the print range.

#### MFC References

- CPrintDialog::GetDlgToPage


<!-- page: PyCPrintInfo__GetDocOffsetPage_meth.html -->

## PyCPrintInfo.GetDocOffsetPage

 GetDocOffsetPage()

Get the number of pages preceding the first page of a particular DocObject in a combined DocObject print job.

#### MFC References

- CPrintInfo::m_nOffsetPage


<!-- page: PyCPrintInfo__GetDraw_meth.html -->

## PyCPrintInfo.GetDraw

 GetDraw()

Get the usable drawing area of the page in logical coordinates.

#### MFC References

- CPrintInfo::m_rectDraw


<!-- page: PyCPrintInfo__GetDriverName_meth.html -->

## PyCPrintInfo.GetDriverName

 GetDriverName()

The name of the currently selected printer device driver, call only after DoModal finishes.

#### MFC References

- CPrintDialog::GetDriverName


<!-- page: PyCPrintInfo__GetDwFlags_meth.html -->

## PyCPrintInfo.GetDwFlags

 GetDwFlags()

A flags specifying DocObject printing operations. Valid only if data member m_bDocObject is TRUE.

#### MFC References

- CPrintInfo::m_dwFlags


<!-- page: PyCPrintInfo__GetFlags_meth.html -->

## PyCPrintInfo.GetFlags

 GetFlags()

A set of bit flags that you can use to initialize the Print common dialog box. When the dialog box returns, it sets these flags to indicate the user's input. This member can be a combination of the following flags: PD_ALLPAGES, PD_COLLATE, PD_DISABLEPRINTTOFILE, PD_ENABLEPRINTHOOK, PD_ENABLEPRINTTEMPLATE, PD_ENABLEPRINTTEMPLATEHANDLE, PD_ENABLESETUPHOOK, PD_ENABLESETUPTEMPLATE, PD_ENABLESETUPTEMPLATEHANDLE, PD_HIDEPRINTTOFILE, PD_NONETWORKBUTTON, PD_NOPAGENUMS, PD_NOSELECTION, PD_NOWARNING, PD_PAGENUMS, PD_PRINTSETUP, PD_PRINTTOFILE, PD_RETURNDC, PD_RETURNDEFAULT, PD_RETURNIC, PD_SELECTION, PD_SHOWHELP, PD_USEDEVMODECOPIES, PD_USEDEVMODECOPIESANDCOLLATE.

#### MFC References

- PRINTDLG::Flags


<!-- page: PyCPrintInfo__GetFromPage_meth.html -->

## PyCPrintInfo.GetFromPage

 GetFromPage()

The number of the first page to be printed.

#### MFC References

- CPrintInfo::GetFromPage


<!-- page: PyCPrintInfo__GetHDC_meth.html -->

## PyCPrintInfo.GetHDC

 GetHDC()

Identifies a device context or an information context, depending on whether the Flags member specifies the PD_RETURNDC or PC_RETURNIC flag. If neither flag is specified, the value of this member is undefined. If both flags are specified, PD_RETURNDC has priority.

#### MFC References

- PRINTDLG::hDC


<!-- page: PyCPrintInfo__GetMaxPage_meth.html -->

## PyCPrintInfo.GetMaxPage

 GetMaxPage()

Get the number of the last page of the document.

#### MFC References

- CPrintInfo::GetMaxPage


<!-- page: PyCPrintInfo__GetMinPage_meth.html -->

## PyCPrintInfo.GetMinPage

 GetMinPage()

Get the number of the first page of the document.

#### MFC References

- CPrintInfo::GetMinPage


<!-- page: PyCPrintInfo__GetNumPreviewPages_meth.html -->

## PyCPrintInfo.GetNumPreviewPages

 GetNumPreviewPages()

Get the number of pages displayed in preview mode.

#### MFC References

- CPrintInfo::m_nNumPreviewPages


<!-- page: PyCPrintInfo__GetOffsetPage_meth.html -->

## PyCPrintInfo.GetOffsetPage

 GetOffsetPage()

Get the number of pages preceding the first page of a DocObject item being printed in a combined DocObject print job. This currently does NOT work, as, if I include the symbol pInfo->GetOffsetPage(), the link fails to find its definition. Allways returns 0.

#### MFC References

- CPrintInfo::GetOffsetPage


<!-- page: PyCPrintInfo__GetPRINTDLGCopies_meth.html -->

## PyCPrintInfo.GetPRINTDLGCopies

 GetPRINTDLGCopies()

Get the initial number of copies for the Copies edit control if hDevMode is NULL; otherwise, the dmCopies member of theDEVMODE structure contains the initial value. When PrintDlg returns, nCopies contains the actual number of copies to print. This value depends on whether the application or the printer driver is responsible for printing multiple copies. If the PD_USEDEVMODECOPIESANDCOLLATE flag is set in the Flags member, nCopies is always 1 on return, and the printer driver is responsible for printing multiple copies. If the flag is not set, the application is responsible for printing the number of copies specified by nCopies. For more information, see the description of the PD_USEDEVMODECOPIESANDCOLLATE flag.

#### MFC References

- PRINTDLG::nCopies


<!-- page: PyCPrintInfo__GetPRINTDLGMinPage_meth.html -->

## PyCPrintInfo.GetPRINTDLGMinPage

 GetPRINTDLGMinPage()

Get the minimum value for the page range specified in the From and To page edit controls. If nMinPage equals nMaxPage, the Pages radio button and the starting and ending page edit controls are disabled.

#### MFC References

- PRINTDLG::nMinPage


<!-- page: PyCPrintInfo__GetPageDesc_meth.html -->

## PyCPrintInfo.GetPageDesc

 GetPageDesc()

Get the format string used to display the page numbers during print preview

#### MFC References

- CPrintInfo::m_strPageDesc


<!-- page: PyCPrintInfo__GetPortName_meth.html -->

## PyCPrintInfo.GetPortName

 GetPortName()

The name of the currently selected printer port, call only after DoModal finishes.

#### MFC References

- CPrintDialog::GetPortName


<!-- page: PyCPrintInfo__GetPreview_meth.html -->

## PyCPrintInfo.GetPreview

 GetPreview()

A flag indicating whether the document is being previewed.

#### MFC References

- CPrintInfo::m_bPreview


<!-- page: PyCPrintInfo__GetPrinterDC_meth.html -->

## PyCPrintInfo.GetPrinterDC

 GetPrinterDC()

A handle to the printer device context if successful; otherwise NULL. If the bPrintSetupOnly parameter of the CPrintDialog constructor was FALSE (indicating that the Print dialog box is displayed), then GetPrinterDC returns a handle to the printer device context. You must call the WindowsDeleteDC function to delete the device context when you are done using it.

#### MFC References

- CPrintDialog::GetPrinterDC


<!-- page: PyCPrintInfo__GetToPage_meth.html -->

## PyCPrintInfo.GetToPage

 GetToPage()

The number of the last page to be printed.

#### MFC References

- CPrintInfo::GetToPage


<!-- page: PyCPrintInfo__GetUserData_meth.html -->

## PyCPrintInfo.GetUserData

 GetUserData()

Get a user-created structure.

#### MFC References

- CPrintInfo::m_lpUserData


<!-- page: PyCPrintInfo__PrintAll_meth.html -->

## PyCPrintInfo.PrintAll

 PrintAll()

Nonzero if all pages in the document are to be printed; otherwise 0, call only after DoModal finishes.

#### MFC References

- CPrintDialog::PrintAll


<!-- page: PyCPrintInfo__PrintCollate_meth.html -->

## PyCPrintInfo.PrintCollate

 PrintCollate()

Nonzero if the user selects the collate check box in the dialog box; otherwise 0, call only after DoModal finishes.

#### MFC References

- CPrintDialog::PrintCollate


<!-- page: PyCPrintInfo__PrintRange_meth.html -->

## PyCPrintInfo.PrintRange

 PrintRange()

Nonzero if only a range of pages in the document are to be printed; otherwise 0, call only after DoModal finishes.

#### MFC References

- CPrintDialog::PrintRange


<!-- page: PyCPrintInfo__PrintSelection_meth.html -->

## PyCPrintInfo.PrintSelection

 PrintSelection()

Nonzero if only the selected items are to be printed; otherwise 0., call only after DoModal finishes

#### MFC References

- CPrintDialog::PrintSelection


<!-- page: PyCPrintInfo__SetContinuePrinting_meth.html -->

## PyCPrintInfo.SetContinuePrinting

 SetContinuePrinting()

Set whether the framework should continue the print loop.

#### MFC References

- CPrintInfo::m_bContinuePrinting


<!-- page: PyCPrintInfo__SetCurPage_meth.html -->

## PyCPrintInfo.SetCurPage

 SetCurPage()

Set the number of the current page.

#### MFC References

- CPrintInfo::m_nCurPage


<!-- page: PyCPrintInfo__SetDirect_meth.html -->

## PyCPrintInfo.SetDirect

 SetDirect()

Sets to TRUE if the Print dialog box will be bypassed for direct printing; FALSE otherwise.

#### MFC References

- CPrintInfo::m_bDirect


<!-- page: PyCPrintInfo__SetDocOffsetPage_meth.html -->

## PyCPrintInfo.SetDocOffsetPage

 SetDocOffsetPage()

Set the number of pages preceding the first page of a particular DocObject in a combined DocObject print job.

#### MFC References

- CPrintInfo::m_nOffsetPage


<!-- page: PyCPrintInfo__SetDraw_meth.html -->

## PyCPrintInfo.SetDraw

 SetDraw()

Set the usable drawing area of the page in logical coordinates.

#### MFC References

- CPrintInfo::m_rectDraw


<!-- page: PyCPrintInfo__SetDwFlags_meth.html -->

## PyCPrintInfo.SetDwFlags

 SetDwFlags()

Set a flag specifying DocObject printing operations. Valid only if data member m_bDocObject is TRUE.

#### MFC References

- CPrintInfo::m_dwFlags


<!-- page: PyCPrintInfo__SetFlags_meth.html -->

## PyCPrintInfo.SetFlags

 SetFlags()

A set of bit flags that you can use to initialize the Print common dialog box. When the dialog box returns, it sets these flags to indicate the user's input. This member can be a combination of the following flags: PD_ALLPAGES, PD_COLLATE, PD_DISABLEPRINTTOFILE, PD_ENABLEPRINTHOOK, PD_ENABLEPRINTTEMPLATE, PD_ENABLEPRINTTEMPLATEHANDLE, PD_ENABLESETUPHOOK, PD_ENABLESETUPTEMPLATE, PD_ENABLESETUPTEMPLATEHANDLE, PD_HIDEPRINTTOFILE, PD_NONETWORKBUTTON, PD_NOPAGENUMS, PD_NOSELECTION, PD_NOWARNING, PD_PAGENUMS, PD_PRINTSETUP, PD_PRINTTOFILE, PD_RETURNDC, PD_RETURNDEFAULT, PD_RETURNIC, PD_SELECTION, PD_SHOWHELP, PD_USEDEVMODECOPIES, PD_USEDEVMODECOPIESANDCOLLATE.

#### MFC References

- PRINTDLG::Flags


<!-- page: PyCPrintInfo__SetFromPage_meth.html -->

## PyCPrintInfo.SetFromPage

 SetFromPage()

The number of the first page to be printed.

#### MFC References

- PRINTDLG::nFromPage


<!-- page: PyCPrintInfo__SetHDC_meth.html -->

## PyCPrintInfo.SetHDC

 SetHDC(hdc)

Sets the printer DC compatible with the users choices, call after the print dialog DoModal finishes.

#### Parameters

- hdc : int

 The DC.

#### MFC References

- CPrintInfo::m_pPD

- CPrintDialog::m_pd.hDC


<!-- page: PyCPrintInfo__SetMaxPage_meth.html -->

## PyCPrintInfo.SetMaxPage

 SetMaxPage()

Set the number of the last page of the document.

#### MFC References

- CPrintInfo::SetMaxPage


<!-- page: PyCPrintInfo__SetMinPage_meth.html -->

## PyCPrintInfo.SetMinPage

 SetMinPage()

Set the number of the first page of the document.

#### MFC References

- CPrintInfo::SetMinPage


<!-- page: PyCPrintInfo__SetNumPreviewPages_meth.html -->

## PyCPrintInfo.SetNumPreviewPages

 SetNumPreviewPages()

Set the number of pages displayed in preview mode.

#### MFC References

- CPrintInfo::m_nNumPreviewPages


<!-- page: PyCPrintInfo__SetPRINTDLGCopies_meth.html -->

## PyCPrintInfo.SetPRINTDLGCopies

 SetPRINTDLGCopies()

Set the initial number of copies for the Copies edit control if hDevMode is NULL; otherwise, the dmCopies member of theDEVMODE structure contains the initial value. When PrintDlg returns, nCopies contains the actual number of copies to print. This value depends on whether the application or the printer driver is responsible for printing multiple copies. If the PD_USEDEVMODECOPIESANDCOLLATE flag is set in the Flags member, nCopies is always 1 on return, and the printer driver is responsible for printing multiple copies. If the flag is not set, the application is responsible for printing the number of copies specified by nCopies. For more information, see the description of the PD_USEDEVMODECOPIESANDCOLLATE flag.

#### MFC References

- PRINTDLG::nCopies


<!-- page: PyCPrintInfo__SetPRINTDLGMinPage_meth.html -->

## PyCPrintInfo.SetPRINTDLGMinPage

 SetPRINTDLGMinPage()

Set the minimum value for the page range specified in the From and To page edit controls. If nMinPage equals nMaxPage, the Pages radio button and the starting and ending page edit controls are disabled.

#### MFC References

- PRINTDLG::nMinPage


<!-- page: PyCPrintInfo__SetPageDesc_meth.html -->

## PyCPrintInfo.SetPageDesc

 SetPageDesc()

Set the format string used to display the page numbers during print preview

#### MFC References

- CPrintInfo::m_strPageDesc


<!-- page: PyCPrintInfo__SetPreview_meth.html -->

## PyCPrintInfo.SetPreview

 SetPreview()

Set whether the document is being previewed.

#### MFC References

- CPrintInfo::m_bPreview


<!-- page: PyCPrintInfo__SetPrintDialog_meth.html -->

## PyCPrintInfo.SetPrintDialog

 SetPrintDialog()

Set a pointer to the CPrintDialog object used to display the Print dialog box for the print job.

#### MFC References

- CPrintInfo::m_pPD


<!-- page: PyCPrintInfo__SetToPage_meth.html -->

## PyCPrintInfo.SetToPage

 SetToPage()

The number of the last page to be printed.

#### MFC References

- PRINTDLG::nToPage


<!-- page: PyCPrintInfo__SetUserData_meth.html -->

## PyCPrintInfo.SetUserData

 SetUserData()

Set a user-created structure.

#### MFC References

- CPrintInfo::m_lpUserData


---

<!-- object: PyCProgressCtrl -->


<!-- page: PyCProgressCtrl.html -->

---

## PyCProgressCtrl Object

 A windows progress bar control. Encapsulates an MFC CProgressCtrl class. Derived from PyCControl.

#### Methods

- CreateWindow

 Creates the window for a new progress bar object.

- SetRange

 Sets the lower and upper bounds for the progress bar.

- SetPos

 Set the control's position

- OffsetPos

 Advances the progress bar control's current position by the increment specified.

- SetStep

 Specifies the step increment for a progress bar control.

- StepIt

 Advances the current position for a progress bar control by the step increment. Returns previous position.


<!-- page: PyCProgressCtrl__CreateWindow_meth.html -->

## PyCProgressCtrl.CreateWindow

 CreateWindow(style, rect, parent, id)

Creates the actual control.

#### Parameters

- style : int

 The style for the control.

- rect : (left, top, right, bottom)

 The size and position of the control.

- parent : PyCWnd

 The parent window of the control. Usually a PyCDialog.

- id : int

 The control's ID.


<!-- page: PyCProgressCtrl__OffsetPos_meth.html -->

## PyCProgressCtrl.OffsetPos

 int = OffsetPos(nPos)

Advances the progress bar control's current position by the increment specified

#### Parameters

- nPos=1 : int

 Amount to advance the position.


<!-- page: PyCProgressCtrl__SetPos_meth.html -->

## PyCProgressCtrl.SetPos

 int = SetPos(nPos)

Set the control's position

#### Parameters

- nPos=1 : int

 New position of the progress bar control.


<!-- page: PyCProgressCtrl__SetRange_meth.html -->

## PyCProgressCtrl.SetRange

 SetRange(nLower, nUpper)

Set the control's bounds

#### Parameters

- nLower=1 : int

 Specifies the lower limit of the range (default is zero).

- nUpper=1 : int

 Specifies the upper limit of the range (default is 100).


<!-- page: PyCProgressCtrl__SetStep_meth.html -->

## PyCProgressCtrl.SetStep

 int = SetStep(nStep)

Specifies the step increment for a progress bar control.

#### Parameters

- nStep=1 : int

 New step increment.


<!-- page: PyCProgressCtrl__StepIt_meth.html -->

## PyCProgressCtrl.StepIt

 int = StepIt()

Advances the current position for a progress bar control by the step increment. Returns previous position.


---

<!-- object: PyCPropertyPage -->


<!-- page: PyCPropertyPage.html -->

---

## PyCPropertyPage Object

 A class which encapsulates an MFC CPropertyPage object. Derived from a PyCDialog object.

#### Methods

- CancelToClose

 Changes the Cancel button to Close.

- OnCancel

 Calls the default MFC OnCancel handler.

- OnOK

 Calls the default MFC OnOK handler.

- OnApply

 Calls the default MFC OnApply handler.

- OnReset

 Calls the default MFC OnReset handler.

- OnQueryCancel

 Calls the default MFC OnQueryCancel handler.

- OnWizardBack

 Calls the default MFC OnWizardBack handler.

- OnWizardNext

 Calls the default MFC OnWizardNext handler.

- OnWizardFinish

 Calls the default MFC OnWizardFinish handler.

- OnSetActive

 Calls the default MFC OnSetActive handler.

- OnKillActive

 Calls the default MFC OnKillActive handler.

- SetModified

 Sets the modified flag (for the Apply button).

- SetPSPBit

 Sets (or clears) a bit in m_psp.dwFlags.


<!-- page: PyCPropertyPage__CancelToClose_meth.html -->

## PyCPropertyPage.CancelToClose

 CancelToClose()

Changes the Cancel button to Close.


<!-- page: PyCPropertyPage__OnApply_meth.html -->

## PyCPropertyPage.OnApply

 OnApply()

Calls the default MFC OnApply handler.

#### See Also

- PyCPropertyPage.OnApply virtual method


<!-- page: PyCPropertyPage__OnApply_virtual.html -->

## PyCPropertyPage.OnApply Virtual

 OnApply()

Called by the framework when the user chooses the OK or the Apply Now button.

#### Comments

 Note - If you provide a handler, you must call the underlying MFC method (PyCPropertyPage::OnApply) yourself

#### See Also

- PyCPropertyPage::OnApply

#### Return Value

Return Nonzero if the changes are accepted; otherwise 0.


<!-- page: PyCPropertyPage__OnCancel_meth.html -->

## PyCPropertyPage.OnCancel

 OnCancel()

Calls the default MFC OnCancel handler.

#### See Also

- PyCDialog.OnCancel virtual method


<!-- page: PyCPropertyPage__OnKillActive_meth.html -->

## PyCPropertyPage.OnKillActive

 int = OnKillActive()

Calls the default MFC OnKillActive handler.

#### See Also

- PyCPropertyPage.OnKillActive virtual method

- PyCPropertyPage.OnKillActive virtual method

#### Return Value

The result is true if the page should be deselected. Typically this result should be passed to the original OnSetActive handler.


<!-- page: PyCPropertyPage__OnKillActive_virtual.html -->

## PyCPropertyPage.OnKillActive Virtual

 OnKillActive()

Called when the page loses focus.

#### Comments

 Note - If you provide a handler, you must call the underlying MFC method (PyCPropertyPage::OnKillActive) yourself

#### See Also

- PyCPropertyPage::OnKillActive

#### Return Value

The method should return TRUE if the page can be de-activated.


<!-- page: PyCPropertyPage__OnOK_meth.html -->

## PyCPropertyPage.OnOK

 OnOK()

Calls the default MFC OnOK handler.

#### See Also

- PyCDialog.OnOK virtual method


<!-- page: PyCPropertyPage__OnQueryCancel_meth.html -->

## PyCPropertyPage.OnQueryCancel

 OnQueryCancel()

Calls the default MFC OnQueryCancel handler.

#### See Also

- PyCPropertyPage.OnQueryCancel virtual method


<!-- page: PyCPropertyPage__OnQueryCancel_virtual.html -->

## PyCPropertyPage.OnQueryCancel Virtual

 OnQueryCancel()

Called by the framework when the user clicks the Cancel button and before the cancel action has taken place.

#### Comments

 Note - If you provide a handler, you must call the underlying MFC method (PyCPropertyPage::OnQueryCancel) yourself

#### See Also

- PyCPropertyPage::OnQueryCancel

#### Return Value

Return FALSE to prevent the cancel operation or TRUE to allow it.


<!-- page: PyCPropertyPage__OnReset_meth.html -->

## PyCPropertyPage.OnReset

 OnReset()

Calls the default MFC OnReset handler.

#### See Also

- PyCPropertyPage.OnReset virtual method


<!-- page: PyCPropertyPage__OnReset_virtual.html -->

## PyCPropertyPage.OnReset Virtual

 OnReset()

Called by the framework when the user chooses the Cancel button.

#### Comments

 Note - If you provide a handler, you must call the underlying MFC method (PyCPropertyPage::OnReset) yourself

#### See Also

- PyCPropertyPage::OnReset


<!-- page: PyCPropertyPage__OnSetActive_meth.html -->

## PyCPropertyPage.OnSetActive

 int = OnSetActive()

Calls the default MFC OnSetActive handler.

#### See Also

- PyCPropertyPage.OnSetActive virtual method

- PyCPropertyPage.OnSetActive virtual method

#### Return Value

The result is true if the page should be made active. Typically this result should be passed to the original OnSetActive handler.


<!-- page: PyCPropertyPage__OnSetActive_virtual.html -->

## PyCPropertyPage.OnSetActive Virtual

 OnSetActive()

Called when the page becomes active.

#### Comments

 Note - If you provide a handler, you must call the underlying MFC method (PyCPropertyPage::OnSetActive) yourself

#### See Also

- PyCPropertyPage::OnSetActive

#### Return Value

The method should return TRUE if the page can be activated.


<!-- page: PyCPropertyPage__OnWizardBack_meth.html -->

## PyCPropertyPage.OnWizardBack

 OnWizardBack()

Calls the default MFC OnWizardBack handler.

#### See Also

- PyCPropertyPage.OnWizardBack virtual method


<!-- page: PyCPropertyPage__OnWizardBack_virtual.html -->

## PyCPropertyPage.OnWizardBack Virtual

 OnWizardBack()

Called by the framework when the user clicks on the Back button in a wizard.

#### Comments

 Note - If you provide a handler, you must call the underlying MFC method (PyCPropertyPage::OnWizardBack) yourself

#### See Also

- PyCPropertyPage::OnWizardBack

#### Return Value

Return 0 to automatically advance to the next page; -1 to prevent the page from changing. To jump to a page other than the next one, return the identifier of the dialog to be displayed.


<!-- page: PyCPropertyPage__OnWizardFinish_meth.html -->

## PyCPropertyPage.OnWizardFinish

 OnWizardFinish()

Calls the default MFC OnWizardFinish handler.

#### See Also

- PyCPropertyPage.OnWizardFinish virtual method


<!-- page: PyCPropertyPage__OnWizardFinish_virtual.html -->

## PyCPropertyPage.OnWizardFinish Virtual

 OnWizardFinish()

Called by the framework when the user clicks on the Finish button in a wizard.

#### Comments

 Note - If you provide a handler, you must call the underlying MFC method (PyCPropertyPage::OnWizardFinish) yourself

#### See Also

- PyCPropertyPage::OnWizardFinish

#### Return Value

Return nonzero if the property sheet is destroyed when the wizard finishes; otherwise zero.


<!-- page: PyCPropertyPage__OnWizardNext_meth.html -->

## PyCPropertyPage.OnWizardNext

 OnWizardNext()

Calls the default MFC OnWizardNext handler.

#### See Also

- PyCPropertyPage.OnWizardNext virtual method


<!-- page: PyCPropertyPage__OnWizardNext_virtual.html -->

## PyCPropertyPage.OnWizardNext Virtual

 OnWizardNext()

Called by the framework when the user clicks on the Next button in a wizard.

#### Comments

 Note - If you provide a handler, you must call the underlying MFC method (PyCPropertyPage::OnWizardNext) yourself

#### See Also

- PyCPropertyPage::OnWizardNext

#### Return Value

Return 0 to automatically advance to the next page; -1 to prevent the page from changing. To jump to a page other than the next one, return the identifier of the dialog to be displayed.


<!-- page: PyCPropertyPage__SetModified_meth.html -->

## PyCPropertyPage.SetModified

 SetModified(bChanged)

Sets the modified flag.

#### Parameters

- bChanged=1 : int

 A flag to indicate the new modified state.


<!-- page: PyCPropertyPage__SetPSPBit_meth.html -->

## PyCPropertyPage.SetPSPBit

 SetPSPBit(bitMask, bitValue)

Sets or clears a bit in m_psp.dwFlags

#### Parameters

- bitMask : int

 The PSP_* bit mask constant

- bitValue : int

 1 to set, 0 to clear


---

<!-- object: PyCPropertySheet -->


<!-- page: PyCPropertySheet.html -->

---

## PyCPropertySheet Object

 A class which encapsulates an MFC CPropertySheet object. Derived from a PyCWnd object.

#### Methods

- AddPage

 Adds the supplied page with the rightmost tab in the property sheet.

- CreateWindow

 Displays the property sheet as a modeless dialog.

- DoModal

 Displays the property sheet as a modal dialog.

- EnableStackedTabs

 Enables or disables stacked tabs.

- EndDialog

 Closes the dialog, with the specified result.

- GetActiveIndex

 Retrieves the index of the active page of the property sheet.

- GetActivePage

 Returns the currently active property page.

- GetPage

 Returns the specified property page.

- GetPageIndex

 Retrieves the index of the specified page of the property sheet.

- GetPageCount

 Returns the number of pages.

- GetTabCtrl

 Returns the tab control used by the sheet.

- OnInitDialog

 Calls the default MFC OnInitDialog handler.

- PressButton

 Simulates the choice of the specified button in a property sheet.

- RemovePage

 Removes the specified page from the sheet.

- SetActivePage

 Programmatically sets the active page object.

- SetTitle

 Sets the caption for the property sheet.

- SetFinishText

 Sets the text for the Finish button

- SetWizardMode

 Enables the wizard mode

- SetWizardButtons

 Enables the wizard buttons

- SetPSHBit

 Sets (or clears) a bit in m_psh.dwFlags.


<!-- page: PyCPropertySheet__AddPage_meth.html -->

## PyCPropertySheet.AddPage

 AddPage(page)

Adds the supplied page with the rightmost tab in the property sheet.

#### Parameters

- page : PyCPropertyPage

 The page to be added.

#### Comments

 Add pages to the property sheet in the left-to-right order you want them to appear.

#### MFC References

- PyCPropertySheet::AddPage


<!-- page: PyCPropertySheet__CreateWindow_meth.html -->

## PyCPropertySheet.CreateWindow

 CreateWindow(parent, style, exStyle)

Displays the property sheet as a modeless dialog.

#### Parameters

- parent=None : PyCWnd

 The parent of the dialog.

- style=WS_SYSMENU|WS_POPUP|WS_CAPTION|DS_MODALFRAME|WS_VISIBLE : int

 The style for the window.

- exStyle=WS_EX_DLGMODALFRAME : int

 The extended style for the window.


<!-- page: PyCPropertySheet__DoModal_meth.html -->

## PyCPropertySheet.DoModal

 int = DoModal()

Displays the property sheet as a modal dialog.


<!-- page: PyCPropertySheet__EnableStackedTabs_meth.html -->

## PyCPropertySheet.EnableStackedTabs

 PyCPropertyPage = EnableStackedTabs(stacked)

Enables or disables stacked tabs.

#### Parameters

- stacked : int

 A boolean flag


<!-- page: PyCPropertySheet__EndDialog_meth.html -->

## PyCPropertySheet.EndDialog

 EndDialog(result)

Closes the dialog, with the specified result.

#### Parameters

- result : int

 The result to be returned by DoModal.


<!-- page: PyCPropertySheet__GetActiveIndex_meth.html -->

## PyCPropertySheet.GetActiveIndex

 int = GetActiveIndex()

Retrieves the index of the active page of the property sheet.


<!-- page: PyCPropertySheet__GetActivePage_meth.html -->

## PyCPropertySheet.GetActivePage

 PyCPropertyPage = GetActivePage()

Returns the currently active property page.

#### MFC References

- PyCPropertySheet::GetActivePage


<!-- page: PyCPropertySheet__GetPageCount_meth.html -->

## PyCPropertySheet.GetPageCount

 int = GetPageCount()

Returns the number of pages.


<!-- page: PyCPropertySheet__GetPageIndex_meth.html -->

## PyCPropertySheet.GetPageIndex

 int = GetPageIndex(page)

Retrieves the index of the specified page of the property sheet.

#### Parameters

- page : PyCPropertyPage

 The page.


<!-- page: PyCPropertySheet__GetPage_meth.html -->

## PyCPropertySheet.GetPage

 PyCPropertyPage = GetPage(pageNo)

Returns the specified property page.

#### Parameters

- pageNo : int

 The index of the page toretrieve.

#### MFC References

- PyCPropertySheet::GetPage


<!-- page: PyCPropertySheet__GetTabCtrl_meth.html -->

## PyCPropertySheet.GetTabCtrl

 PyCTabCtrl = GetTabCtrl()

Returns the tab control used by the sheet.


<!-- page: PyCPropertySheet__OnInitDialog_meth.html -->

## PyCPropertySheet.OnInitDialog

 int = OnInitDialog()

Calls the default MFC OnInitDialog handler.

#### See Also

- PyCPropertySheet.OnInitDialog virtual method


<!-- page: PyCPropertySheet__OnInitDialog_virtual.html -->

## PyCPropertySheet.OnInitDialog Virtual

 OnInitDialog()

Override to augment dialog-box initialization.

#### Comments

 The base implementation is not called if a handler exists. This can be done via PyCDialog::OnInitDialog.

#### See Also

- PyCDialog::OnInitDialog

#### Return Value

Specifies whether the application has set the input focus to one of the controls in the dialog box. If OnInitDialog returns nonzero, Windows sets the input focus to the first control in the dialog box. The application can return 0/None only if it has explicitly set the input focus to one of the controls in the dialog box.


<!-- page: PyCPropertySheet__OnInitDialog_virtual_1.html -->

## PyCPropertySheet.OnInitDialog Virtual

 OnInitDialog()

Override to augment dialog-box initialization.

#### Comments

 The base implementation is not called if a handler exists. This can be done via PyCPropertySheet::OnInitDialog.

#### See Also

- PyCPropertySheet::OnInitDialog

#### Return Value

Specifies whether the application has set the input focus to one of the controls in the dialog box. If OnInitDialog returns nonzero, Windows sets the input focus to the first control in the dialog box. The application can return 0/None only if it has explicitly set the input focus to one of the controls in the dialog box.


<!-- page: PyCPropertySheet__PressButton_meth.html -->

## PyCPropertySheet.PressButton

 PressButton(button)

Simulates the choice of the specified button in a property sheet.

#### Parameters

- button : int

 The button to press


<!-- page: PyCPropertySheet__RemovePage_meth.html -->

## PyCPropertySheet.RemovePage

 RemovePage(offset)

Removes the specified page from the sheet.

#### Parameters

- offset : int

 The page number to remove

#### Alternative Parameters

- page

 The page to remove


<!-- page: PyCPropertySheet__SetActivePage_meth.html -->

## PyCPropertySheet.SetActivePage

 SetActivePage(page)

Programmatically sets the active page object.

#### Parameters

- page : PyCPropertyPage

 The page.


<!-- page: PyCPropertySheet__SetFinishText_meth.html -->

## PyCPropertySheet.SetFinishText

 SetFinishText(text)

Sets the text for the Finish button

#### Parameters

- text : string

 The next for the button


<!-- page: PyCPropertySheet__SetPSHBit_meth.html -->

## PyCPropertySheet.SetPSHBit

 SetPSHBit(bitMask, bitValue)

Sets or clears a bit in m_psh.dwFlags

#### Parameters

- bitMask : int

 The PSH_* bit mask constant

- bitValue : int

 1 to set, 0 to clear


<!-- page: PyCPropertySheet__SetTitle_meth.html -->

## PyCPropertySheet.SetTitle

 SetTitle(title)

Sets the caption for the property sheet.

#### Parameters

- title : string

 The new caption


<!-- page: PyCPropertySheet__SetWizardButtons_meth.html -->

## PyCPropertySheet.SetWizardButtons

 SetWizardButtons(flags)

Enables the wizard buttons

#### Parameters

- flags : int

 The wizard flags


<!-- page: PyCPropertySheet__SetWizardMode_meth.html -->

## PyCPropertySheet.SetWizardMode

 SetWizardMode()

Enables the wizard mode


<!-- page: PyCPropertySheet__WindowProc_virtual.html -->

## PyCPropertySheet.WindowProc Virtual

 WindowProc()

Default message handler.


---

<!-- object: PyCREDENTIAL -->


<!-- page: PyCREDENTIAL.html -->

---

## PyCREDENTIAL Object

 A dictionary containing information for a CREDENTIAL struct

#### Win32 API References

- Search for CREDENTIAL struct at [msdn](https://learn.microsoft.com/en-ca/search/?terms=CREDENTIAL struct), [google](https://www.google.com/search?q=CREDENTIAL struct) or [google groups](https://groups.google.com/groups?q=CREDENTIAL struct).

#### Properties

- int Flags
 Combination of CRED_FLAGS_PROMPT_NOW, CRED_FLAGS_USERNAME_TARGET

- int Type
 Type of credential, one of CRED_TYPE_* values

- PyUnicode TargetName
 Target of credential, can end with * for wildcard matching

- PyUnicode Comment
 Descriptive text

- PyDateTime LastWritten
 Modification time, ignored on input

- PyUnicode CredentialBlob
 Contains password for username credential, or PIN for certificate credential. This member is write-only.

- int Persist
 Specifies scope of persistence, one of CRED_PERSIST_* values

- tuple Attributes
 Tuple of PyCREDENTIAL_ATTRIBUTE dicts containing application-specific data, can be None

- PyUnicode TargetAlias
 Alias for TargetName, only valid with CRED_TYPE_GENERIC

- PyUnicode UserName
 User to be authenticated by target. Can be of the form username@domain or domain\\username. For CRED_TYPE_DOMAIN_CERTIFICATE, use win32cred::CredMarshalCredential to marshal the SHA1 hash of user's certficate


---

<!-- object: PyCREDENTIAL_ATTRIBUTE -->


<!-- page: PyCREDENTIAL_ATTRIBUTE.html -->

---

## PyCREDENTIAL_ATTRIBUTE Object

 A dictionary containing information for a CREDENTIAL_ATTRIBUTE struct

#### Win32 API References

- Search for CREDENTIAL_ATTRIBUTE at [msdn](https://learn.microsoft.com/en-ca/search/?terms=CREDENTIAL_ATTRIBUTE), [google](https://www.google.com/search?q=CREDENTIAL_ATTRIBUTE) or [google groups](https://groups.google.com/groups?q=CREDENTIAL_ATTRIBUTE).

#### Properties

- PyUnicode Keyword
 Attribute name, at most CRED_MAX_STRING_LENGTH chars

- int Flags
 Reserved, use only 0

- str Value
 Attribute value, at most CRED_MAX_VALUE_SIZE bytes. Unicode objects are treated as raw bytes.


---

<!-- object: PyCREDENTIAL_TARGET_INFORMATION -->


<!-- page: PyCREDENTIAL_TARGET_INFORMATION.html -->

---

## PyCREDENTIAL_TARGET_INFORMATION Object

 A dictionary representing a CREDENTIAL_TARGET_INFORMATION struct

#### Win32 API References

- Search for CREDENTIAL_TARGET_INFORMATION at [msdn](https://learn.microsoft.com/en-ca/search/?terms=CREDENTIAL_TARGET_INFORMATION), [google](https://www.google.com/search?q=CREDENTIAL_TARGET_INFORMATION) or [google groups](https://groups.google.com/groups?q=CREDENTIAL_TARGET_INFORMATION).

#### Properties

- PyUnicode TargetName
 Target of credentials

- PyUnicode NetbiosServerName

- PyUnicode DnsServerName

- PyUnicode NetbiosDomainName

- PyUnicode DnsDomainName

- PyUnicode DnsTreeName

- PyUnicode PackageName
 Name of security package which mapped TargetName

- int Flags
 CRED_TI_* flags

- (int,...) CredTypes
 Tuple of CRED_TYPE_* values indicating which types of credentials are acceptable to target


---

<!-- object: PyCREDUI_INFO -->


<!-- page: PyCREDUI_INFO.html -->

---

## PyCREDUI_INFO Object

 A dictionary representing a CREDUI_INFO structure, used with win32cred::CredUIPromptForCredentials

#### Comments

 All members are optional

#### Win32 API References

- Search for CREDUI_INFO at [msdn](https://learn.microsoft.com/en-ca/search/?terms=CREDUI_INFO), [google](https://www.google.com/search?q=CREDUI_INFO) or [google groups](https://groups.google.com/groups?q=CREDUI_INFO).

#### Properties

- PyHANDLE Parent
 Handle to parent window, can be None

- PyUnicode MessageText
 Message to appear in dialog

- PyUnicode CaptionText
 Title of the dialog window

- PyHANDLE Banner
 Handle to a bitmap to be displayed


---

<!-- object: PyCRYPTHASH -->


<!-- page: PyCRYPTHASH.html -->

---

## PyCRYPTHASH Object

 Handle to a cryptographic hash

#### Methods

- CryptDestroyHash

 Frees the hash object

- CryptDuplicateHash

 Clones the hash object

- CryptHashData

 Adds data to the hash

- CryptHashSessionKey

 Hashes a session key

- CryptSignHash

 Signs the hash

- CryptVerifySignature

 Verifies that a signature matches hashed data

- CryptGetHashParam

 Retrieves the specified attribute of the hash


<!-- page: PyCRYPTHASH__CryptDestroyHash_meth.html -->

## PyCRYPTHASH.CryptDestroyHash

 CryptDestroyHash()

Frees the hash object


<!-- page: PyCRYPTHASH__CryptDuplicateHash_meth.html -->

## PyCRYPTHASH.CryptDuplicateHash

 PyCRYPTHASH = CryptDuplicateHash(Flags)

Clones the hash object

#### Parameters

- Flags=0 : int

 Reserved, use 0 if passed


<!-- page: PyCRYPTHASH__CryptGetHashParam_meth.html -->

## PyCRYPTHASH.CryptGetHashParam

 int/str = CryptGetHashParam(Param, Flags )

Retrieves the specified attribute of the hash

#### Parameters

- Param : int

 The parameter to retrieve: HP_ALGID, HP_HASHSIZE, or HP_HASHVAL

- Flags=0 : int

 Reserved, use 0 if passed in

#### Comments

 After this method has been called, no more data can be hashed

#### Return Value

Type of returned object is dependent on the Param passed in


<!-- page: PyCRYPTHASH__CryptHashData_meth.html -->

## PyCRYPTHASH.CryptHashData

 CryptHashData(Data, Flags)

Adds data to the hash

#### Parameters

- Data : string

 Data to be hashed

- Flags=0 : int

 CRYPT_USERDATA or 0

#### Comments

 If Flags is CRYPT_USERDATA, provider is expected to prompt user to enter data. MSDN says that MS CSPs ignore this flag


<!-- page: PyCRYPTHASH__CryptHashSessionKey_meth.html -->

## PyCRYPTHASH.CryptHashSessionKey

 CryptHashSessionKey(Key, Flags)

Hashes a session key

#### Parameters

- Key : PyCRYPTKEY

 The session key to be hashed

- Flags=0 : int

 CRYPT_LITTLE_ENDIAN or 0


<!-- page: PyCRYPTHASH__CryptSignHash_meth.html -->

## PyCRYPTHASH.CryptSignHash

 string = CryptSignHash(KeySpec, Flags )

Signs the hash

#### Parameters

- KeySpec : int

 The key to be used to sign the hash, AT_KEYEXCHANGE,AT_SIGNATURE

- Flags=0 : int

 CRYPT_NOHASHOID,CRYPT_X931_FORMAT or 0

#### Comments

 This methods signs only the hash, not the data that the hash represents


<!-- page: PyCRYPTHASH__CryptVerifySignature_meth.html -->

## PyCRYPTHASH.CryptVerifySignature

 CryptVerifySignature(Signature, PubKey, Flags)

Verifies that a signature matches hashed data

#### Parameters

- Signature : string

 Signature data to verify

- PubKey : PyCRYPTKEY

 Public key of signer

- Flags=0 : int

 CRYPT_NOHASHOID,CRYPT_X931_FORMAT or 0


---

<!-- object: PyCRYPTKEY -->


<!-- page: PyCRYPTKEY.html -->

---

## PyCRYPTKEY Object

 Handle to a cryptographic key

#### Methods

- CryptDestroyKey

 Releases the handle to the key

- CryptExportKey

 Securely exports key or key pair

- CryptGetKeyParam

 Retrieves key parameters

- CryptDuplicateKey

 Creates an independent copy of the key

- CryptEncrypt

 Encrypts data

- CryptDecrypt

 Decrypts data

#### Properties

- int HCRYPTPROV
 CSP used by the key

- int HCRYPTKEY
 Plain integer handle to the key


<!-- page: PyCRYPTKEY__CryptDecrypt_meth.html -->

## PyCRYPTKEY.CryptDecrypt

 str = CryptDecrypt(Final, Data , Hash , Flags )

Decrypts data

#### Parameters

- Final : int

 Boolean, use True is this is last (or only) operation

- Data : buffer

 Data to be decrypted

- Hash=None : PyCRYPTHASH

 Hash to be used in signature verification, can be None

- Flags=0 : int

 Reserved, use only 0


<!-- page: PyCRYPTKEY__CryptDestroyKey_meth.html -->

## PyCRYPTKEY.CryptDestroyKey

 CryptDestroyKey()

Releases the handle to the key (does not delete permanent keys)


<!-- page: PyCRYPTKEY__CryptDuplicateKey_meth.html -->

## PyCRYPTKEY.CryptDuplicateKey

 PyCRYPTKEY = CryptDuplicateKey(Reserved, Flags )

Creates an independent copy of the key

#### Parameters

- Reserved=0 : int

 Use 0 if passed in

- Flags=0 : int

 Also reserved, use 0


<!-- page: PyCRYPTKEY__CryptEncrypt_meth.html -->

## PyCRYPTKEY.CryptEncrypt

 str = CryptEncrypt(Final, Data , Hash , Flags )

Encrypts and optionally hashes data

#### Parameters

- Final : int

 Boolean, use True if this is final encryption operation

- Data : buffer

 Data to be encrypted

- Hash=None : PyCRYPTHASH

 Hash to be updated with data passed in, can be None

- Flags=0 : int

 Reserved, use 0 if passed in


<!-- page: PyCRYPTKEY__CryptExportKey_meth.html -->

## PyCRYPTKEY.CryptExportKey

 str = CryptExportKey(ExpKey, BlobType , Flags )

Exports key or key pair as an encrypted blob

#### Parameters

- ExpKey : PyCRYPTKEY

 Public key or session key of destination user. Use None if exporting a PUBLICKEYBLOB

- BlobType : int

 One of OPAQUEKEYBLOB,PRIVATEKEYBLOB,PUBLICKEYBLOB,SIMPLEBLOB,PLAINTEXTKEYBLOB,SYMMETRICWRAPKEYBLOB

- Flags=0 : int

 Combination of CRYPT_DESTROYKEY,CRYPT_SSL2_FALLBACK,CRYPT_OAEP or 0

#### Return Value

Returns a binary blob that can be imported via PyCRYPTPROV::CryptImportKey


<!-- page: PyCRYPTKEY__CryptGetKeyParam_meth.html -->

## PyCRYPTKEY.CryptGetKeyParam

 object = CryptGetKeyParam(Param, Flags )

Retrieves key parameters

#### Parameters

- Param : int

 One of the KP_* constants

- Flags=0 : int

 Reserved, use only 0

#### Return Value

Type of returned object is dependent on the requested attribute


---

<!-- object: PyCRYPTMSG -->


<!-- page: PyCRYPTMSG.html -->

---

## PyCRYPTMSG Object

 Wrapper for a cryptographic message handle

#### Methods

- CryptMsgClose

 Closes the message handle

#### Properties

- int HCRYPTMSG
 Raw message handle


<!-- page: PyCRYPTMSG__CryptMsgClose_meth.html -->

## PyCRYPTMSG.CryptMsgClose

 CryptMsgClose()

Closes the message handle


---

<!-- object: PyCRYPTPROTECT_PROMPTSTRUCT -->


<!-- page: PyCRYPTPROTECT_PROMPTSTRUCT.html -->

---

## PyCRYPTPROTECT_PROMPTSTRUCT Object

 A tuple representing a CRYPTPROTECT_PROMPTSTRUCT structure

#### Items

- [0] int : flags

 Combination of CRYPTPROTECT_PROMPT_* flags

- [1] int : hwndApp

 parent hwnd (default is 0)

- [2] PyUnicode : prompt

 A prompt string (default is None)


---

<!-- object: PyCRYPTPROV -->


<!-- page: PyCRYPTPROV.html -->

---

## PyCRYPTPROV Object

 Handle to a cryptographic provider, created using cryptoapi::CryptAcquireContext

#### Methods

- CryptReleaseContext

 Releases the CSP handle

- CryptGenKey

 Generates a key pair or a session key

- CryptGetProvParam

 Retrieves specified attribute of provider

- CryptGetUserKey

 Returns a handle to one of user's key pairs

- CryptGenRandom

 Generates random data of specified length

- CryptCreateHash

 Creates a hash object for hashing large amounts of data

- CryptImportKey

 Imports a key exported by PyCRYPTKEY::CryptExportKey

- CryptExportPublicKeyInfo

 Exports a public key to send to other users

- CryptImportPublicKeyInfo

 Imports another user's public key


<!-- page: PyCRYPTPROV__CryptCreateHash_meth.html -->

## PyCRYPTPROV.CryptCreateHash

 PyCRYPTHASH = CryptCreateHash(Algid, Key , Flags )

Creates a hash object for hashing large amounts of data

#### Parameters

- Algid : int

 An algorithm identifier, CALG_*.

- Key=None : PyCRYPTKEY

 Used only for keyed hashes (MAC or HMAC), use None otherwise

- Flags=0 : int

 Reserved, use 0 if passed in


<!-- page: PyCRYPTPROV__CryptExportPublicKeyInfo_meth.html -->

## PyCRYPTPROV.CryptExportPublicKeyInfo

 PyCERT_PUBLIC_KEY_INFO = CryptExportPublicKeyInfo(KeySpec, CertEncodingType )

Exports a public key to send to other users Returned dict can be serialized for sending to another python application using pickle.dump

#### Parameters

- KeySpec : int

 AT_KEYEXCHANGE or AT_SIGNATURE

- CertEncodingType=X509_ASN_ENCODING combined with PKCS_7_ASN_ENCODING : int

 Specifies encoding for exported key info


<!-- page: PyCRYPTPROV__CryptGenKey_meth.html -->

## PyCRYPTPROV.CryptGenKey

 PyCRYPTKEY = CryptGenKey(Algid, Flags , KeyLen )

Generates a key pair or a session key

#### Parameters

- Algid : int

 Algorithm identifier, one of the CALG_* values, or AT_KEYEXCHANGE/AT_SIGNATURE

- Flags : int

 Combination of CRYPT_CREATE_SALT,CRYPT_EXPORTABLE,CRYPT_NO_SALT,CRYPT_PREGEN,CRYPT_USER_PROTECTED,CRYPT_ARCHIVABLE

- KeyLen=0 : int

 Length of key to generate, can be 0 to use provider's default key length

#### Comments

 Differs from Api call in that the length is passed in separately


<!-- page: PyCRYPTPROV__CryptGenRandom_meth.html -->

## PyCRYPTPROV.CryptGenRandom

 string = CryptGenRandom(Len, SeedData )

Generates random data of specified length

#### Parameters

- Len : int

 Number of bytes to generate

- SeedData=None : string

 Random seed data


<!-- page: PyCRYPTPROV__CryptGetProvParam_meth.html -->

## PyCRYPTPROV.CryptGetProvParam

 CryptGetProvParam(Param, Flags)

Retrieves specified attribute of provider

#### Parameters

- Param : int

 One of the PP_* values

- Flags=0 : int

 If param if PP_KEYSET_SEC_DESCR, can be a combination of OWNER_SECURITY_INFORMATION,GROUP_SECURITY_INFORMATION,DACL_SECURITY_INFORMATION,SACL_SECURITY_INFORMATION

#### Return Value

Type of returned object is dependent on the attribute requested


<!-- page: PyCRYPTPROV__CryptGetUserKey_meth.html -->

## PyCRYPTPROV.CryptGetUserKey

 PyCRYPTKEY = CryptGetUserKey(KeySpec)

Returns a handle to one of user's key pairs

#### Parameters

- KeySpec : int

 AT_KEYEXCHANGE or AT_SIGNATURE (some providers may implement extra key specs)


<!-- page: PyCRYPTPROV__CryptImportKey_meth.html -->

## PyCRYPTPROV.CryptImportKey

 PyCRYPTKEY = CryptImportKey(Data, PubKey , Flags )

Imports a key exported by PyCRYPTKEY::CryptExportKey

#### Parameters

- Data : buffer

 The key blob to be imported

- PubKey=None : PyCRYPTKEY

 Key to be used to decrypt the blob, not used for importing public keys

- Flags=0 : int

 Combination of CRYPT_EXPORTABLE, CRYPT_OAEP, CRYPT_NO_SALT, CRYPT_USER_PROTECTED


<!-- page: PyCRYPTPROV__CryptImportPublicKeyInfo_meth.html -->

## PyCRYPTPROV.CryptImportPublicKeyInfo

 PyCRYPTKEY = CryptImportPublicKeyInfo(Info, CertEncodingType )

Imports another user's public key

#### Parameters

- Info : dict

 PyCERT_PUBLIC_KEY_INFO dictionary as returned by PyCRYPTPROV::CryptExportPublicKeyInfo

- CertEncodingType=X509_ASN_ENCODING combined with PKCS_7_ASN_ENCODING : int

 Specifies encoding for exported key info


<!-- page: PyCRYPTPROV__CryptReleaseContext_meth.html -->

## PyCRYPTPROV.CryptReleaseContext

 CryptReleaseContext(Flags)

Releases the CSP handle

#### Parameters

- Flags=0 : int

 Reserved, use 0 if passed in


---

<!-- object: PyCRYPT_ALGORITHM_IDENTIFIER -->


<!-- page: PyCRYPT_ALGORITHM_IDENTIFIER.html -->

---

## PyCRYPT_ALGORITHM_IDENTIFIER Object

 Dictionary containing information that identifies an encryption algorithm and any extra parameters it requires

#### Properties

- str ObjId
 An szOID_* string identifying the algorithm

- str Parameters
 Blob of binary data containing encoded parameters


---

<!-- object: PyCRYPT_ATTRIBUTE -->


<!-- page: PyCRYPT_ATTRIBUTE.html -->

---

## PyCRYPT_ATTRIBUTE Object

 Dict representing a CRYPT_ATTRIBUTE struct

#### Properties

- str ObjId
 An szOID_* string identifying the attribute

- (buffer,...) Value
 A sequence of buffers containing the attribute values


---

<!-- object: PyCRYPT_BIT_BLOB -->


<!-- page: PyCRYPT_BIT_BLOB.html -->

---

## PyCRYPT_BIT_BLOB Object

 Dict containing raw data of a certain bit length

#### Properties

- buffer Data
 Binary data

- int UnusedBits
 Nbr of bits of last byte that are unused


---

<!-- object: PyCRYPT_DECRYPT_MESSAGE_PARA -->


<!-- page: PyCRYPT_DECRYPT_MESSAGE_PARA.html -->

---

## PyCRYPT_DECRYPT_MESSAGE_PARA Object

 Dict containing message decryption parameters, used with cryptoapi::CryptDecodeMessage and cryptoapi::CryptDecryptMessage

#### Properties

- (PyCERT_STORE ,...) CertStores
 Sequence of certificate stores to be searched for a certificate with a private key that can be used to decrypt the message

- int MsgAndCertEncodingType
 Encoding types, optional. Defaults to X509_ASN_ENCODING combined with PKCS_7_ASN_ENCODING

- int Flags
 Optional. CRYPT_MESSAGE_SILENT_KEYSET_FLAG can be used to suppress any dialogs that might be triggered by accessing a key container, such as a request for a PIN.


---

<!-- object: PyCRYPT_ENCRYPT_MESSAGE_PARA -->


<!-- page: PyCRYPT_ENCRYPT_MESSAGE_PARA.html -->

---

## PyCRYPT_ENCRYPT_MESSAGE_PARA Object

 Dictionary of encryption parameters used with cryptoapi::CryptEncryptMessage

#### Properties

- PyCRYPT_ALGORITHM_IDENTIFIER ContentEncryptionAlgorithm
 Identifies the algorithm to be used

- PyCRYPTPROV CryptProv
 Optional. Handle to provider that will perform encryption, can be None for default provider

- object EncryptionAuxInfo
 Optional. Extra info required by some CSP's. Not supported yet, use only None

- int Flags
 Optional. Combination of CRYPT_MESSAGE_*_FLAG constants

- int InnerContentType
 Optional. Only used if message to be encrypted is already encoded

- int MsgEncodingType
 Optional. Defaults to X509_ASN_ENCODING combined with PKCS_7_ASN_ENCODING


---

<!-- object: PyCRYPT_SIGN_MESSAGE_PARA -->


<!-- page: PyCRYPT_SIGN_MESSAGE_PARA.html -->

---

## PyCRYPT_SIGN_MESSAGE_PARA Object

 Dict of parms defining how a message will be signed

#### Properties

- PyCERT_CONTEXT SigningCert
 Certficate to be used to sign message

- PyCRYPT_ALGORITHM_IDENTIFIER HashAlgorithm
 Algorithm to be used for signed hash

- None HashAuxInfo
 Optional. Param is reserved, use only None.

- (PyCERT_CONTEXT,...) MsgCert
 Optional sequence of certificate to be included in the message.

- (CRL_CONTEXT,...) MsgCrl
 Optional. Sequence of certificate revocation lists. Not yet supported, use only None.

- (PyCRYPT_ATTRIBUTE,...) AuthAttr
 Sequence of canonical attributes to be added to the message

- (PyCRYPT_ATTRIBUTE,...) UnauthAttr
 Sequence of arbitrary attributes

- int Flags
 Optional CRYPT_MESSAGE_*_FLAG that indicates content type if output is to be further encoded.

- int InnerContentType
 Optional, one of the CMSG_* content types if message is already encoded, .

- int MsgEncodingType
 Encoding types, optional. Defaults to X509_ASN_ENCODING combined with PKCS_7_ASN_ENCODING


---

<!-- object: PyCRYPT_VERIFY_MESSAGE_PARA -->


<!-- page: PyCRYPT_VERIFY_MESSAGE_PARA.html -->

---

## PyCRYPT_VERIFY_MESSAGE_PARA Object

 Dict of verification parameters to be used with cryptoapi::CryptDecodeMessage or cryptoapi::CryptVerifyMessageSignature . All parameters are optional. Can be either an empty dict or None to use all defaults.

#### Properties

- int MsgAndCertEncodingType
 Encoding types, defaults to X509_ASN_ENCODING combined with PKCS_7_ASN_ENCODING

- PyCRYPTPROV CryptProv
 CSP to be used to verify signature. Use None for default provider.

- function PyGetSignerCertificate
 Callback function that locates signer's certificate.

- object GetArg
 Argument to be passed to above function, can be any object.


---

<!-- object: PyCRect -->


<!-- page: PyCRect.html -->

---

## PyCRect Object

 A Python interface the the MFC CRect class.

#### Items

- [0] int : left

- [1] int : top

- [2] int : right

- [3] int : bottom


---

<!-- object: PyCRgn -->


<!-- page: PyCRgn.html -->

---

## PyCRgn Object

 An object encapsulating an MFC PyCRgn class.


<!-- page: PyCRgn__CombineRgn_meth.html -->

## PyCRgn.CombineRgn

 int = CombineRgn()

Creates a new GDI region by combining two existing regions. The regions are combined as specified by nCombineMode Return Values: success or failure flag (BOOL)


<!-- page: PyCRgn__CopyRgn_meth.html -->

## PyCRgn.CopyRgn

 int = CopyRgn()

Copies the region defined by pRgnSrc into the CRgn object Return Values: success or failure flag (BOOL)


<!-- page: PyCRgn__CreateEllipticRgn_meth.html -->

## PyCRgn.CreateEllipticRgn

 int = CreateEllipticRgn()

Initializes a region to an ellipse Return Values: success or failure flag (BOOL)


<!-- page: PyCRgn__CreateRectRgn_meth.html -->

## PyCRgn.CreateRectRgn

 int = CreateRectRgn()

Initializes a region to a rectangle Return Values: success or failure flag (BOOL)


<!-- page: PyCRgn__DeleteObject_meth.html -->

## PyCRgn.DeleteObject

 int = DeleteObject()

Deletes the attached Windows GDI Rgn object from memory by freeing all system storage associated with the Windows GDI object Return Values: None


<!-- page: PyCRgn__GetRgnBox_meth.html -->

## PyCRgn.GetRgnBox

 int = GetRgnBox()

Retrieves the coordinates of the bounding rectangle of the CRgn object Return Values: the bounding rectangle as a tuple (l,t,r,b)


<!-- page: PyCRgn__GetSafeHandle_meth.html -->

## PyCRgn.GetSafeHandle

 int = GetSafeHandle()

A HANDLE to the attached Windows GDI object; otherwise NULL if no object is attached Return Values: the handle of the CRgn object


---

<!-- object: PyCRichEditCtrl -->


<!-- page: PyCRichEditCtrl.html -->

---

## PyCRichEditCtrl Object

 A windows Rich Text edit control. Encapsulates an MFC CRichEditCtrl class. Derived from a PyCControl object.

#### Methods

- Clear

 Clears all text from an edit control.

- Copy

 Copy the selection to the clipboard.

- CreateWindow

 Creates a rich edit control.

- Cut

 Cut the selection, and place it in the clipboard.

- FindText

 Finds text in the control

- GetCharPos

 Returns te location of the top-left corner of the specified character.

- GetDefaultCharFormat

 Returns the current default character formatting attributes in this PyCRichEditCtrl object.

- GetEventMask

 Returns the current event mask.

- GetSelectionCharFormat

 Returns the character formatting attributes of the current selection in this PyCRichEditCtrl object.

- GetFirstVisibleLine

 Returns zero-based index of the topmost visible line.

- GetParaFormat

 Returns the formatting of the current paragraph.

- GetSel

 Returns the selection.

- GetSelText

 Returns the currently selected text

- GetTextLength

 Returns the length of the text in the control.

- GetLine

 Returns a specified line.

- GetModify

 Determines if the control has been modified.

- GetLineCount

 Returns the number of lines in an edit control.

- LimitText

 Sets max length of text that user can enter

- LineFromChar

 Returns the line number of a given character.

- LineIndex

 Returns the line index

- LineScroll

 Scroll the control vertically and horizontally

- Paste

 Pastes the contents of the clipboard into the edit control.

- ReplaceSel

 Replace the selection with the specified text.

- SetBackgroundColor

 Sets the background color for the control.

- SetDefaultCharFormat

 Sets the current default character formatting attributes in this PyCRichEditCtrl object.

- SetEventMask

 Sets the event motification mask.

- SetSelectionCharFormat

 Sets the character formatting attributes for the selection in this PyCRichEditCtrl object.

- SetModify

 Sets the modified flag.

- SetOptions

 Sets options for the control.

- SetParaFormat

 Sets the paragraph formatting.

- SetReadOnly

 Set the read only status of an edit control.

- SetSel

 Changes the selection in an edit control.

- SetSelAndCharFormat

 Sets the selection and the char format.

- SetTargetDevice

 Sets the target device for the control

- StreamIn

 Invokes a callback to stream data into the control.

- StreamOut

 Invokes a callback to stream data out of the control.


<!-- page: PyCRichEditCtrl__Clear_meth.html -->

## PyCRichEditCtrl.Clear

 int = Clear()

Clears all text in an edit control.

#### MFC References

- CRichEditCtrl::Clear


<!-- page: PyCRichEditCtrl__Copy_meth.html -->

## PyCRichEditCtrl.Copy

 Copy()

Copys the current selection to the clipboard.

#### MFC References

- CRichEditCtrl::Copy


<!-- page: PyCRichEditCtrl__CreateWindow_meth.html -->

## PyCRichEditCtrl.CreateWindow

 CreateWindow(style, rect, parent, id)

Creates a rich edit control window.

#### Parameters

- style : int

 The control style

- rect : int,int,int,int

 The position of the control

- parent : PyCWnd

 The parent window. Must not be None

- id : int

 The control ID


<!-- page: PyCRichEditCtrl__Cut_meth.html -->

## PyCRichEditCtrl.Cut

 Cut()

Cuts the current selection to the clipboard.

#### MFC References

- CRichEditCtrl::Cut


<!-- page: PyCRichEditCtrl__FindText_meth.html -->

## PyCRichEditCtrl.FindText

 int, (start, end) = FindText(charPos)

Finds text in the control

#### Parameters

- charPos : int

 The character position


<!-- page: PyCRichEditCtrl__GetCharPos_meth.html -->

## PyCRichEditCtrl.GetCharPos

 (tuple) = GetCharPos(charPos)

Returns the location of the top-left corner of the character specified by charPos.

#### Parameters

- charPos : int

 The character position

#### Return Value

The return value is a win32ui::CHARFORMAT tuple


<!-- page: PyCRichEditCtrl__GetDefaultCharFormat_meth.html -->

## PyCRichEditCtrl.GetDefaultCharFormat

 (tuple) = GetDefaultCharFormat()

Returns the current default character formatting attributes in this PyCRichEditCtrl object.

#### MFC References

- CRichEditCtrl::GetDefaultCharFormat

#### Return Value

The return value is a win32ui::CHARFORMAT tuple


<!-- page: PyCRichEditCtrl__GetEventMask_meth.html -->

## PyCRichEditCtrl.GetEventMask

 int = GetEventMask()

Returns the current event mask.

#### MFC References

- CRichEditCtrl::GetEventMask


<!-- page: PyCRichEditCtrl__GetFirstVisibleLine_meth.html -->

## PyCRichEditCtrl.GetFirstVisibleLine

 int = GetFirstVisibleLine()

Returns zero-based index of the topmost visible line.

#### MFC References

- CRichEditCtrl::GetFirstVisibleLine

#### Return Value

The zero-based index of the topmost visible line. For single-line edit controls, the return value is 0.


<!-- page: PyCRichEditCtrl__GetLineCount_meth.html -->

## PyCRichEditCtrl.GetLineCount

 int = GetLineCount()

Gets the number of lines in an edit control.

#### MFC References

- CRichEditCtrl::GetLineCount

#### Return Value

The number of lines in the buffer. If the control is empty, the return value is 1.


<!-- page: PyCRichEditCtrl__GetLine_meth.html -->

## PyCRichEditCtrl.GetLine

 int = GetLine(lineNo)

Returns the text in a specified line.

#### Parameters

- lineNo=current : int

 Contains the zero-based index value for the desired line.

#### Comments

 This function is not an MFC wrapper.


<!-- page: PyCRichEditCtrl__GetModify_meth.html -->

## PyCRichEditCtrl.GetModify

 int = GetModify()

Nonzero if the text in this control has been modified; otherwise 0.

#### MFC References

- CRichEditCtrl::GetModify


<!-- page: PyCRichEditCtrl__GetParaFormat_meth.html -->

## PyCRichEditCtrl.GetParaFormat

 (tuple) = GetParaFormat()

Returns the current paragraph formatting attributes.

#### MFC References

- CRichEditCtrl::GetParaFormat

#### Return Value

The return value is a win32ui::PARAFORMAT tuple


<!-- page: PyCRichEditCtrl__GetSelText_meth.html -->

## PyCRichEditCtrl.GetSelText

 string = GetSelText()

Returns the currently selected text


<!-- page: PyCRichEditCtrl__GetSel_meth.html -->

## PyCRichEditCtrl.GetSel

 (start, end) = GetSel()

Returns the start and end of the current selection.

#### MFC References

- CRichEditCtrl::GetSel

#### Return Value

The return tuple is (the first character in the current selection, first nonselected character past the end of the current selection)


<!-- page: PyCRichEditCtrl__GetSelectionCharFormat_meth.html -->

## PyCRichEditCtrl.GetSelectionCharFormat

 (tuple) = GetSelectionCharFormat()

Returns the character formatting of the selection.

#### MFC References

- CRichEditCtrl::GetSelectionCharFormat


<!-- page: PyCRichEditCtrl__GetTextLength_meth.html -->

## PyCRichEditCtrl.GetTextLength

 int = GetTextLength()

Returns the length of the text in the control.

#### MFC References

- CRichEditCtrl::GetTextLength


<!-- page: PyCRichEditCtrl__LimitText_meth.html -->

## PyCRichEditCtrl.LimitText

 LimitText(nChars)

Sets max length of text that user can enter

#### Parameters

- nChars=0 : int

 Specifies the length (in bytes) of the text that the user can enter. If this parameter is 0, the text length is set to UINT_MAX bytes. This is the default behavior.

#### MFC References

- CRichEditCtrl::LimitText


<!-- page: PyCRichEditCtrl__LineFromChar_meth.html -->

## PyCRichEditCtrl.LineFromChar

 int = LineFromChar(charNo)

Returns the line number of the specified character.

#### Parameters

- charNo=-1 : int

 Contains the zero-based index value for the desired character in the text of the edit control, or -1. If -1, then it specifies the current line.

#### MFC References

- CRichEditCtrl::LineFromChar

#### Return Value

The zero-based line number of the line containing the character index specified by charNo. If charNo is -1, the number of the line that contains the first character of the selection is returned. If there is no selection, the current line number is returned.


<!-- page: PyCRichEditCtrl__LineIndex_meth.html -->

## PyCRichEditCtrl.LineIndex

 int = LineIndex(lineNo)

Retrieves the character index of a line within a multiple-line edit control.

#### Parameters

- lineNo=-1 : int

 Contains the index value for the desired line in the text of the edit control, or contains -1. If -1, then it specifies the current line.

#### Comments

 This method only works on multi-linr edit controls.

#### MFC References

- CRichEditCtrl::LineIndex

#### Return Value

The character index of the line specified in lineNo, or -1 if the specified line number is greater then the number of lines in the edit control.


<!-- page: PyCRichEditCtrl__LineScroll_meth.html -->

## PyCRichEditCtrl.LineScroll

 int = LineScroll(nLines, nChars )

Scroll the control vertically and horizontally

#### Parameters

- nLines : int

 Specifies the number of lines to scroll vertically.

- nChars=0 : int

 Specifies the number of character positions to scroll horizontally. This value is ignored if the edit control has either the ES_RIGHT or ES_CENTER style.

#### Comments

 This method only works on multi-linr edit controls.

#### MFC References

- CRichEditCtrl::LineScroll


<!-- page: PyCRichEditCtrl__Paste_meth.html -->

## PyCRichEditCtrl.Paste

 Paste()

Pastes the contents of the clipboard into the control.

#### MFC References

- CRichEditCtrl::Paste


<!-- page: PyCRichEditCtrl__ReplaceSel_meth.html -->

## PyCRichEditCtrl.ReplaceSel

 ReplaceSel(text)

Replaces the selection with the specified text.

#### Parameters

- text : string

 The text to replace the selection with.

#### MFC References

- CRichEditCtrl::ReplaceSel


<!-- page: PyCRichEditCtrl__SetBackgroundColor_meth.html -->

## PyCRichEditCtrl.SetBackgroundColor

 int = SetBackgroundColor(bSysColor, cr )

Sets the background color for the control.

#### Parameters

- bSysColor : int

 Indicates if the background color should be set to the system value. If this value is TRUE, cr is ignored.

- cr=0 : int

 The requested background color. Used only if bSysColor is FALSE.

#### MFC References

- CRichEditCtrl::SetEventMask

#### Return Value

The return value is the previous background color.


<!-- page: PyCRichEditCtrl__SetDefaultCharFormat_meth.html -->

## PyCRichEditCtrl.SetDefaultCharFormat

 SetDefaultCharFormat(charFormat)

Sets the current default character formatting attributes in this PyCRichEditCtrl object.

#### Parameters

- charFormat : tuple

 A charformat tuple. See win32ui::CHARFORMAT tuple for details.

#### MFC References

- CRichEditCtrl::SetDefaultCharFornmat


<!-- page: PyCRichEditCtrl__SetEventMask_meth.html -->

## PyCRichEditCtrl.SetEventMask

 int = SetEventMask(eventMask)

Sets the event motification mask.

#### Parameters

- eventMask : int

 The new event mask. Must be one of the win32con.ENM_* flags.

#### MFC References

- CRichEditCtrl::SetEventMask

#### Return Value

The return value is the previous event mask.


<!-- page: PyCRichEditCtrl__SetModify_meth.html -->

## PyCRichEditCtrl.SetModify

 SetModify(modified)

Sets the modified flag for this control

#### Parameters

- modified=1 : int

 Indicates the new value for the modified flag.

#### MFC References

- CRichEditCtrl::SetModify


<!-- page: PyCRichEditCtrl__SetOptions_meth.html -->

## PyCRichEditCtrl.SetOptions

 SetOptions(op, flags)

Sets options for the control.

#### Parameters

- op : int

 Indicates the operation. Must be one of the win32con.ECOOP_* flags.

- flags : int

 Indicates the options. Must be one a combination of win32con.ECO_* flags.

#### MFC References

- CRichEditCtrl::SetOptions


<!-- page: PyCRichEditCtrl__SetParaFormat_meth.html -->

## PyCRichEditCtrl.SetParaFormat

 int = SetParaFormat(paraFormat)

Sets the paragraph formatting

#### Parameters

- paraFormat : tuple

 A charformat tuple. See win32ui::PARAFORMAT tuple for details.

#### MFC References

- CRichEditCtrl::SetParaFormat

#### Return Value

This function seems to return occasionally return failure, but the formatting is applied. Therefore an exception is not raised on failure, but the BOOL return code is passed back.


<!-- page: PyCRichEditCtrl__SetReadOnly_meth.html -->

## PyCRichEditCtrl.SetReadOnly

 SetReadOnly(bReadOnly)

Sets or clears the read-only status of the listbox.

#### Parameters

- bReadOnly=1 : int

 The read-only state to set.

#### MFC References

- CRichEditCtrl::SetReadOnly


<!-- page: PyCRichEditCtrl__SetSelAndCharFormat_meth.html -->

## PyCRichEditCtrl.SetSelAndCharFormat

 SetSelAndCharFormat(charFormat)

Sets the selection and char format.

#### Parameters

- charFormat : tuple

 A charformat tuple. See win32ui::CHARFORMAT tuple for details.

#### Comments

 Highly optimised for speed for color editors.

#### MFC References

- CRichEditCtrl::SetSelectionCharFormat

- CRichEditCtrl::SetSel


<!-- page: PyCRichEditCtrl__SetSel_meth.html -->

## PyCRichEditCtrl.SetSel

 SetSel(start, end)

Sets the selection in the edit control.

#### Parameters

- start : int

 Specifies the starting position. If start is 0 and end is -1, all the text in the edit control is selected. If start is -1, any current selection is removed.

- end=start : int

 Specifies the ending position.

#### Alternative Parameters

- start,end)

 As for normal start, end args.

#### MFC References

- CRichEditCtrl::SetSel


<!-- page: PyCRichEditCtrl__SetSelectionCharFormat_meth.html -->

## PyCRichEditCtrl.SetSelectionCharFormat

 SetSelectionCharFormat(charFormat)

Sets the current selections character formatting attributes.

#### Parameters

- charFormat : tuple

 A charformat tuple. See win32ui::CHARFORMAT tuple for details.

#### MFC References

- CRichEditCtrl::SetSelectionCharFormat


<!-- page: PyCRichEditCtrl__SetTargetDevice_meth.html -->

## PyCRichEditCtrl.SetTargetDevice

 SetTargetDevice(dc, lineWidth)

Sets the target device for the control

#### Parameters

- dc : PyCDC

 The new DC - may be None

- lineWidth : int

 Line width to use for formatting.

#### MFC References

- CRichEditCtrl::SetTargetDevice


<!-- page: PyCRichEditCtrl__SetWordCharFormat_meth.html -->

## PyCRichEditCtrl.SetWordCharFormat

 SetWordCharFormat(charFormat)

Sets the currently selected word's character formatting attributes.

#### Parameters

- charFormat : tuple

 A charformat tuple. See win32ui::CHARFORMAT tuple for details.

#### MFC References

- CRichEditCtrl::SetWordCharFormat


<!-- page: PyCRichEditCtrl__StreamIn_meth.html -->

## PyCRichEditCtrl.StreamIn

 (int,int) = StreamIn(format, method )

Invokes a callback to stream data into the control.

#### Parameters

- format : int

 The format. One of the win32con.SF_* flags (SF_TEXT,SF_RTF)

- method : object

 A callable object (eg, a method or function) This method is called with a single integer param, which is the maximum number of bytes to fetch. The method should return a zero length string, or None to finish the operation, and a string otherwise.

#### MFC References

- CRichEditCtrl::StreamIn

#### Return Value

The return value is a tuple of (no bytes written, error code)


<!-- page: PyCRichEditCtrl__StreamOut_meth.html -->

## PyCRichEditCtrl.StreamOut

 (int, int) = StreamOut(format, method )

Invokes a callback to stream data into the control.

#### Parameters

- format : int

 The format. One of the win32con.SF_* flags (SF_TEXT,SF_RTF) and may also combine SFF_SELECTION.

- method : object

 A callable object (eg, a method or function) This method is called with a string parameter. It should return an integer, zero to abort, non zero otherwise.

#### MFC References

- CRichEditCtrl::StreamOut

#### Return Value

The return value is a tuple of (no bytes written, error code)


---

<!-- object: PyCRichEditDoc -->


<!-- page: PyCRichEditDoc.html -->

---

## PyCRichEditDoc Object

 A class which implements a CRichEditView object. Derived from PyCDocument.

#### Methods

- OnCloseDocument

 Call the MFC OnCloseDocument handler.


<!-- page: PyCRichEditDoc__OnCloseDocument_meth.html -->

## PyCRichEditDoc.OnCloseDocument

 OnCloseDocument()

Call the MFC OnCloseDocument handler. This routine is provided so a document object which overrides this method can call the original MFC version if required.

#### See Also

- PyCDocument.OnCloseDocument virtual method

#### MFC References

- CRichEditDoc::OnCloseDocument


---

<!-- object: PyCRichEditDocTemplate -->


<!-- page: PyCRichEditDocTemplate.html -->

---

## PyCRichEditDocTemplate Object

 A document template class for OLE functionality. Encapsulates an MFC CDocTemplate class

#### Methods

- DoCreateRichEditDoc

 Creates an underlying document object.


<!-- page: PyCRichEditDocTemplate__DoCreateRichEditDoc_meth.html -->

## PyCRichEditDocTemplate.DoCreateRichEditDoc

 PyCRichEditDoc = DoCreateRichEditDoc(fileName)

Creates an underlying document object.

#### Parameters

- fileName=None : string

 The name of the file to load.


---

<!-- object: PyCRichEditView -->


<!-- page: PyCRichEditView.html -->

---

## PyCRichEditView Object

 A class which implements a CRichEditView. Derived from PyCRichEditView and PyCRichEditCtrl.

#### Methods

- GetRichEditCtrl

 Returns the underlying rich edit control object.

- SetWordWrap

 Sets the wordwrap state for the control.

- WrapChanged

 Calls the underlying WrapChanged method.

- SaveTextFile

 Saves the control to a text file


<!-- page: PyCRichEditView__GetRichEditCtrl_meth.html -->

## PyCRichEditView.GetRichEditCtrl

 PyCRichEditCtrl = GetRichEditCtrl()

Returns the underlying rich edit control object.


<!-- page: PyCRichEditView__SaveTextFile_meth.html -->

## PyCRichEditView.SaveTextFile

 None = SaveTextFile(FileName)

Saves the contents of the control as a test file

#### Parameters

- FileName : str

 Name of file to save

#### Comments

 There is no equivalent MFC method. This is implemented in this module for performance reasons.


<!-- page: PyCRichEditView__SetWordWrap_meth.html -->

## PyCRichEditView.SetWordWrap

 None = SetWordWrap(wordWrap)

Sets the wordwrap state for the control.

#### Parameters

- wordWrap : int

 The new word-wrap state.

#### MFC References

- CRichEditCtrl::m_nWordWrap


<!-- page: PyCRichEditView__WrapChanged_meth.html -->

## PyCRichEditView.WrapChanged

 None = WrapChanged()

Calls the underlying WrapChanged method.

#### MFC References

- CRichEditCtrl::WrapChanged


---

<!-- object: PyCScrollView -->


<!-- page: PyCScrollView.html -->

---

## PyCScrollView Object

 A class which implements a generic CScrollView. Derived from a PyCView object.

#### Methods

- GetDeviceScrollPosition

 Return the position of the scroll bars (device units).

- GetDC

 Get the views current PyCDC

- GetScrollPosition

 Return the position of the scroll bars (logical units).

- GetTotalSize

 Return the total size of the views.

- OnCommand

 Calls the standard Python framework OnCommand handler

- ResizeParentToFit

 Call ResizeParentToFit to let the size of your view dictate the size of its frame window.

- SetScaleToFitSize

 Scales the viewport size to the current window size automatically.

- ScrollToPosition

 Scroll to a specified point.

- SetScrollSizes

 Set the scrolling sizes.

- UpdateBars

 Update the scroll bar state.

#### Based On

PyCView


<!-- page: PyCScrollView__GetDC_meth.html -->

## PyCScrollView.GetDC

 PyCDC = GetDC()

Gets the view's current DC.


<!-- page: PyCScrollView__GetDeviceScrollPosition_meth.html -->

## PyCScrollView.GetDeviceScrollPosition

 (x,y) = GetDeviceScrollPosition()

Returns the positon of the scroll bars in device units.


<!-- page: PyCScrollView__GetScrollPosition_meth.html -->

## PyCScrollView.GetScrollPosition

 (x,y) = GetScrollPosition()

Returns the current position of the scroll bars (in logical units).


<!-- page: PyCScrollView__GetTotalSize_meth.html -->

## PyCScrollView.GetTotalSize

 (x,y) = GetTotalSize()

Returns the total size of the view in logical units.


<!-- page: PyCScrollView__OnCommand_meth.html -->

## PyCScrollView.OnCommand

 OnCommand(wparam, lparam)

Calls the standard Python framework OnCommand handler

#### Parameters

- wparam : int

- lparam : int

#### See Also

- PyCWnd.OnCommand virtual method


<!-- page: PyCScrollView__OnPrepareDC_virtual.html -->

## PyCScrollView.OnPrepareDC Virtual

 OnPrepareDC(dc)

Called to prepare the device context for a view.

#### Parameters

- dc : PyCDC

 The DC object.

#### See Also

- PyCView::OnPrepareDC


<!-- page: PyCScrollView__ResizeParentToFit_meth.html -->

## PyCScrollView.ResizeParentToFit

 tuple = ResizeParentToFit(bShrinkOnly)

Lets the size of a view dictate the size of its frame window.

#### Parameters

- bShrinkOnly=1 : int

 The kind of resizing to perform. The default value, TRUE, shrinks the frame window if appropriate.

#### Comments

 This is recommended only for views in MDI child frame windows.
Use ResizeParentToFit in the OnInitialUpdate handler function of your View class.
You must ensure the parent's PyCFrameWnd::RecalcLayout is called before using this method.


<!-- page: PyCScrollView__ScrollToPosition_meth.html -->

## PyCScrollView.ScrollToPosition

 ScrollToPosition(position)

Scrolls to a given point in the view.

#### Parameters

- position : (x,y)

 The position to scroll to.


<!-- page: PyCScrollView__SetScaleToFitSize_meth.html -->

## PyCScrollView.SetScaleToFitSize

 SetScaleToFitSize(size)

Scales the viewport size to the current window size automatically.

#### Parameters

- size : (x,y)

 The horizontal and vertical sizes to which the view is to be scaled. The scroll view's size is measured in logical units.


<!-- page: PyCScrollView__SetScrollSizes_meth.html -->

## PyCScrollView.SetScrollSizes

 SetScrollSizes(mapMode, sizeTotal, sizePage, sizePage)

Sets the sizes of the scroll bars

#### Parameters

- mapMode : int

 The mapping mode for this view.

- sizeTotal : (x,y)

 The total size of the view. Sizes are in logical units. Both x and y must be greater than zero.

- sizePage=win32ui.rectDefault : (x,y)

 The number of units to scroll in response to a page-down command.

- sizePage=win32ui.rectDefault : (x,y)

 The number of units to scroll in response to a line-down command.


<!-- page: PyCScrollView__UpdateBars_meth.html -->

## PyCScrollView.UpdateBars

 UpdateBars()

Update the scroll bars state


---

<!-- object: PyCSliderCtrl -->


<!-- page: PyCSliderCtrl.html -->

---

## PyCSliderCtrl Object

 A windows Slider bar control. Encapsulates an MFC CSliderCtrl class. Derived from PyCControl.

#### Methods

- CreateWindow

 Creates the window for a new Slider bar object.

- GetLineSize

 Get the control's line size

- SetLineSize

 Set the control's line size

- GetPageSize

 Get the control's Page size

- SetPageSize

 Set the control's Page size

- GetRangeMax

 Get the control's maximum

- GetRangeMin

 Get the control's minimum

- GetRange

 Get the control's minimum and maximum

- GetRangeMax

 Set the control's maximum

- GetRangeMin

 Set the control's minimum

- SetRange

 Set the control's minimum and maximum

- GetSelection

 Get the selection start and end positions

- SetSelection

 Set the selection start and end positions

- GetChannelRect

 Get the control's channel rect

- GetThumbRect

 Get the control's thumb rect

- GetPos

 Get the control's position

- SetPos

 Set the control's position

- GetNumTics

 Get the number of tics in the control

- GetTicArray

 Get the array of tic positions

- GetTic

 Get the position of the specified tic

- GetTicPos

 Get the position of the specified tic in client coordinates

- SetTic

 Set a tick at the position

- SetTicFreq

 Set the tic mark frequency

- ClearSel

 Clear any control selection

- ClearTics

 Clear any tic marks from the control


<!-- page: PyCSliderCtrl__ClearSel_meth.html -->

## PyCSliderCtrl.ClearSel

 int = ClearSel(bRedraw)

Clear the selection

#### Parameters

- bRedraw=1 : int

 Redraw the control?


<!-- page: PyCSliderCtrl__ClearTics_meth.html -->

## PyCSliderCtrl.ClearTics

 int = ClearTics(bRedraw)

Clear the control's tic marks

#### Parameters

- bRedraw=1 : int

 Redraw the control?


<!-- page: PyCSliderCtrl__CreateWindow_meth.html -->

## PyCSliderCtrl.CreateWindow

 CreateWindow(style, rect, parent, id)

Creates the actual control.

#### Parameters

- style : int

 The style for the control.

- rect : (left, top, right, bottom)

 The size and position of the control.

- parent : PyCWnd

 The parent window of the control. Usually a PyCDialog.

- id : int

 The control's ID.


<!-- page: PyCSliderCtrl__GetChannelRect_meth.html -->

## PyCSliderCtrl.GetChannelRect

 int = GetChannelRect()

Get the control's channel rectangle


<!-- page: PyCSliderCtrl__GetLineSize_meth.html -->

## PyCSliderCtrl.GetLineSize

 int = GetLineSize()

Get the control's position


<!-- page: PyCSliderCtrl__GetNumTics_meth.html -->

## PyCSliderCtrl.GetNumTics

 int = GetNumTics()

Get number of tics in the slider


<!-- page: PyCSliderCtrl__GetPageSize_meth.html -->

## PyCSliderCtrl.GetPageSize

 int = GetPageSize()

Get the control's position


<!-- page: PyCSliderCtrl__GetPos_meth.html -->

## PyCSliderCtrl.GetPos

 int = GetPos()

Get the control's position


<!-- page: PyCSliderCtrl__GetRangeMax_meth.html -->

## PyCSliderCtrl.GetRangeMax

 int = GetRangeMax()

Get the control's Maximum


<!-- page: PyCSliderCtrl__GetRangeMin_meth.html -->

## PyCSliderCtrl.GetRangeMin

 int = GetRangeMin()

Get the control's Minimum


<!-- page: PyCSliderCtrl__GetRange_meth.html -->

## PyCSliderCtrl.GetRange

 int = GetRange()

Get the control's min and max


<!-- page: PyCSliderCtrl__GetSelection_meth.html -->

## PyCSliderCtrl.GetSelection

 int = GetSelection()

Get the control's selection start and end positions


<!-- page: PyCSliderCtrl__GetThumbRect_meth.html -->

## PyCSliderCtrl.GetThumbRect

 int = GetThumbRect()

Get the control's thumb rectangle


<!-- page: PyCSliderCtrl__GetTicArray_meth.html -->

## PyCSliderCtrl.GetTicArray

 int = GetTicArray()

Get a tuple of slider tic positions


<!-- page: PyCSliderCtrl__GetTicPos_meth.html -->

## PyCSliderCtrl.GetTicPos

 int = GetTicPos(nTic)

Get the position of the specified tic number in client coordinates

#### Parameters

- nTic=1 : int

 Zero based index of the tic mark


<!-- page: PyCSliderCtrl__GetTic_meth.html -->

## PyCSliderCtrl.GetTic

 int = GetTic(nTic)

Get the position of the specified tic number

#### Parameters

- nTic=1 : int

 Zero based index of the tic mark


<!-- page: PyCSliderCtrl__SetLineSize_meth.html -->

## PyCSliderCtrl.SetLineSize

 int = SetLineSize(nLineSize)

Set the control's line size. Returns the previous line size.

#### Parameters

- nLineSize=1 : int

 New line size of the Slider bar control


<!-- page: PyCSliderCtrl__SetPageSize_meth.html -->

## PyCSliderCtrl.SetPageSize

 int = SetPageSize(nPageSize)

Set the control's page size Returns the previous page size.

#### Parameters

- nPageSize=1 : int

 New page size of the Slider bar control.


<!-- page: PyCSliderCtrl__SetPos_meth.html -->

## PyCSliderCtrl.SetPos

 int = SetPos(nPos)

Set the control's position

#### Parameters

- nPos=1 : int

 New position of the Slider bar control.


<!-- page: PyCSliderCtrl__SetRangeMax_meth.html -->

## PyCSliderCtrl.SetRangeMax

 int = SetRangeMax(nRangeMax, bRedraw )

Set the control's maximum

#### Parameters

- nRangeMax=1 : int

 New maximum of the Slider bar control.

- bRedraw=1 : int

 Should slider be redrawn?


<!-- page: PyCSliderCtrl__SetRangeMin_meth.html -->

## PyCSliderCtrl.SetRangeMin

 int = SetRangeMin(nRangeMin, bRedraw )

Set the control's minimum

#### Parameters

- nRangeMin=1 : int

 New minimum of the Slider bar control.

- bRedraw=1 : int

 Should slider be redrawn?


<!-- page: PyCSliderCtrl__SetRange_meth.html -->

## PyCSliderCtrl.SetRange

 int = SetRange(nRangeMin, nRangeMax , bRedraw )

Set the control's min and max

#### Parameters

- nRangeMin=1 : int

 New minimum of the Slider bar control.

- nRangeMax=1 : int

 New maximum of the Slider bar control.

- bRedraw=1 : int

 Should slider be redrawn?


<!-- page: PyCSliderCtrl__SetSelection_meth.html -->

## PyCSliderCtrl.SetSelection

 int = SetSelection(nRangeMin, nRangeMax )

Set the control's selection start and end positions

#### Parameters

- nRangeMin=1 : int

 New start of the Slider's selection.

- nRangeMax=1 : int

 New end of the Slider's selection.


<!-- page: PyCSliderCtrl__SetTicFreq_meth.html -->

## PyCSliderCtrl.SetTicFreq

 int = SetTicFreq(nFreq)

Set the tic frequency

#### Parameters

- nFreq=1 : int

 Frequency of tic marks


<!-- page: PyCSliderCtrl__SetTic_meth.html -->

## PyCSliderCtrl.SetTic

 int = SetTic(nTic)

Set a tic at the specified position

#### Parameters

- nTic=1 : int

 Position of the desired tic mark


---

<!-- object: PyCSpinButtonCtrl -->


<!-- page: PyCSpinButtonCtrl.html -->

---

## PyCSpinButtonCtrl Object

 A windows spin button control. Encapsulates an MFC CSpinButtonCtrl object.

#### Methods

- GetPos

 Obtains the current position for a spin button control.

- SetPos

 Sets the current position for a spin button control.

- SetRange

 Sets the upper and lower limits (range) for a spin button control.

- SetRange32

 Sets the upper and lower limits (range) for a spin button control.


<!-- page: PyCSpinButtonCtrl__GetPos_meth.html -->

## PyCSpinButtonCtrl.GetPos

 int = GetPos()

Obtains the current position for a spin button control.


<!-- page: PyCSpinButtonCtrl__SetPos_meth.html -->

## PyCSpinButtonCtrl.SetPos

 int = SetPos(pos)

Sets the current position for a spin button control.

#### Parameters

- pos : int

 The new position.

#### Return Value

The result is the previous position.


<!-- page: PyCSpinButtonCtrl__SetRange32_meth.html -->

## PyCSpinButtonCtrl.SetRange32

 int = SetRange32()

Sets the 32 bit upper and lower limits (range) for a spin button control.


<!-- page: PyCSpinButtonCtrl__SetRange_meth.html -->

## PyCSpinButtonCtrl.SetRange

 int = SetRange()

Sets the upper and lower limits (range) for a spin button control.


---

<!-- object: PyCSplitterWnd -->


<!-- page: PyCSplitterWnd.html -->

---

## PyCSplitterWnd Object

 A class which encapsulates an MFC CSplitterWnd . Derived from a PyCWnd object.

#### Methods

- GetPane

 Returns the PyCWnd object associated with a splitter window pane.

- CreateView

 Creates a view in a splitter window

- CreateStatic

 Creates a static splitter window.

- SetColumnInfo

 Sets a new minimum height and ideal height for a column

- SetRowInfo

 Sets a new minimum height and ideal height for a row.

- IdFromRowCol

 Gets the child window ID for the specified child.

- DoKeyboardSplit


<!-- page: PyCSplitterWnd__CreateStatic_meth.html -->

## PyCSplitterWnd.CreateStatic

 CreateStatic(parent, rows, cols, style, id)

Creates a static splitter window.

#### Parameters

- parent : PyCFrameWnd or PyCSplitter

 The parent window.

- rows : int

 The number of rows in the splitter.

- cols : int

 The number of columns in the splitter.

- style=WS_CHILD | WS_VISIBLE : int

 Specifies the window style

- id=AFX_IDW_PANE_FIRST : int

 The child window ID of the window. The ID can be AFX_IDW_PANE_FIRST unless the splitter window is nested inside another splitter window.

#### Comments

 A static splitter window is a splitter where the number of panes are fixed at window creation time. Currently this is the only splitter window supported by win32ui.

#### MFC References

- CSplitterWnd::CreateStatic


<!-- page: PyCSplitterWnd__CreateView_meth.html -->

## PyCSplitterWnd.CreateView

 CreateView(view, row, col, width, height)

Creates a view in a splitter window

#### Parameters

- view : PyCView

 The view to place in the splitter pane.

- row : int

 The row in the splitter to place the view.

- col : int

 The column in the splitter to place the view.

- width, height : (int, int)

 The initial size of the new view.

#### MFC References

- CSplitterWnd::CreateView exception set.


<!-- page: PyCSplitterWnd__DoKeyboardSplit_meth.html -->

## PyCSplitterWnd.DoKeyboardSplit

 int = DoKeyboardSplit()


<!-- page: PyCSplitterWnd__GetPane_meth.html -->

## PyCSplitterWnd.GetPane

 PyCWnd = GetPane(row, col )

Returns the PyCView associated with the specified pane.

#### Parameters

- row : int

 The row in the splitter.

- col : int

 The column in the splitter.

#### Comments

 Theoretically the return value can be a PyCWnd object, but currently it will always be a PyCView or derived object.


<!-- page: PyCSplitterWnd__IdFromRowCol_meth.html -->

## PyCSplitterWnd.IdFromRowCol

 IdFromRowCol(row, col)

Gets the child window ID for the specified child.

#### Parameters

- row : int

 The row in the splitter.

- col : int

 The col in the splitter


<!-- page: PyCSplitterWnd__SetColumnInfo_meth.html -->

## PyCSplitterWnd.SetColumnInfo

 SetColumnInfo(column, ideal, min)

Sets a new minimum height and ideal height for a column

#### Parameters

- column : int

 The column in the splitter.

- ideal : int

 Specifies an ideal height for the splitter window column in pixels.

- min : int

 Specifies a minimum height for the splitter window column in pixels.


<!-- page: PyCSplitterWnd__SetRowInfo_meth.html -->

## PyCSplitterWnd.SetRowInfo

 SetRowInfo(row, ideal, min)

Sets a new minimum height and ideal height for a row.

#### Parameters

- row : int

 The row in the splitter.

- ideal : int

 Specifies an ideal height for the splitter window row in pixels.

- min : int

 Specifies a minimum height for the splitter window row in pixels.


---

<!-- object: PyCStatusBar -->


<!-- page: PyCStatusBar.html -->

---

## PyCStatusBar Object

 A class which encapsulates an MFC CStatusBar . Derived from a PyCControlBar object.

#### Methods

- GetPaneInfo

 Returns indicator ID, style, and width for a given pane index.

- GetStatusBarCtrl

 Returns the status bar control object associated with the status bar.

- SetIndicators

 Sets each indicator's ID.

- SetPaneInfo

 Sets indicator ID, style, and width for a given pane index.


<!-- page: PyCStatusBar__GetPaneInfo_meth.html -->

## PyCStatusBar.GetPaneInfo

 (id, style, width) = GetPaneInfo(index)

Returns the id, style, and width of the indicator pane at the location specified by index.

#### Parameters

- index : int

 Index of the pane whose information is to be retrieved.

#### MFC References

- CStatusBar::GetPaneInfo


<!-- page: PyCStatusBar__GetStatusBarCtrl_meth.html -->

## PyCStatusBar.GetStatusBarCtrl

 PyCStatusBarCtrl = GetStatusBarCtrl()

Gets the statusbar control object for the statusbar.

#### MFC References

- CStatusBar::GetStatusBarCtrl Note that below we take the address of rTBC because it's a reference and not a pointer and ui_assoc_object::make expects a pointer. We need to create a new class and not do a map lookup because in MFC CToolBarCtrl is simply a casted CToolBarCtrl (afxext.inl) so the lookup will return the PyCToolBar object which will fail the type tests.


<!-- page: PyCStatusBar__SetIndicators_meth.html -->

## PyCStatusBar.SetIndicators

 SetIndicators(indicators)

Sets each indicator's ID.

#### Parameters

- indicators : tuple

 A tuple containing the ID's of the indicators.


<!-- page: PyCStatusBar__SetPaneInfo_meth.html -->

## PyCStatusBar.SetPaneInfo

 SetPaneInfo(index, id, style, width)

Sets the specified indicator pane to a new ID, style, and width.

#### Parameters

- index : int

 Index of the indicator pane whose style is to be set.

- id : int

 New ID for the indicator pane.

- style : int

 New style for the indicator pane.
The following indicator styles are supported:
afxres.SBPS_NOBORDERS - No 3-D border around the pane.
afxres.SBPS_POPOUT - Reverse border so that text "pops out."
afxres.SBPS_DISABLED - Do not draw text.
afxres.SBPS_STRETCH - Stretch pane to fill unused space. Only one pane per status bar can have this style.
afxres.SBPS_NORMAL - No stretch, borders, or pop-out.

- width : int

 New width for the indicator pane.

#### MFC References

- CStatusBar::SetPaneInfo


---

<!-- object: PyCStatusBarCtrl -->


<!-- page: PyCStatusBarCtrl.html -->

---

## PyCStatusBarCtrl Object

 A windows progress bar control. Encapsulates an MFC CStatusBarCtrl class. Derived from PyCControl.

#### Methods

- CreateWindow

 Creates the window for a new progress bar object.

- GetBorders

 Retrieve the status bar control's current widths of the horizontal and vertical borders and of the space between rectangles.

- GetParts

 Retrieve coordinates of the parts in a status bar control.

- GetRect

 Retrieves the bounding rectangle of a part in a status bar control.

- GetText

 Retrieves the text of a part in a status bar control.

- GetTextAttr

 Retrieves the text attributes of a part in a status bar control.

- GetTextLength

 Retrieves the length of the text in a part in a status bar control.

- SetMinHeight

 Set the minimum height of a status bar control's drawing area.

- SetParts

 Sets the number of parts in a status bar control and the coordinate of the right edge of each part.

- SetText

 Set the text in the given part of a status bar control.

- SetTipText

 Sets the tooltip text for a pane in a status bar.


<!-- page: PyCStatusBarCtrl__CreateWindow_meth.html -->

## PyCStatusBarCtrl.CreateWindow

 CreateWindow(style, rect, parent, id)

Creates the actual control.

#### Parameters

- style : int

 The style for the control.

- rect : (left, top, right, bottom)

 The size and position of the control.

- parent : PyCWnd

 The parent window of the control. Usually a PyCDialog.

- id : int

 The control's ID.


<!-- page: PyCStatusBarCtrl__GetBorders_meth.html -->

## PyCStatusBarCtrl.GetBorders

 (width, height, spacing) = GetBorders()

Retrieve the status bar control's current widths of the horizontal and vertical borders and of the space between rectangles.


<!-- page: PyCStatusBarCtrl__GetParts_meth.html -->

## PyCStatusBarCtrl.GetParts

 (int) = GetParts(nParts)

Retrieve coordinates of the parts in a status bar control.

#### Parameters

- nParts : int

 The number of coordinates to retrieve

#### Comments

 This function, as designed in MFC, returns both the *number* of parts, and, through an OUT parameter, an array of ints giving the coordinates of the parts. There is also an IN parameter saying how many coordinates to give back. Here, we're explicitly changing the semantics a bit.

GetParts() -> Tuple of all coordinates
GetParts(n) -> Tuple of the first n coordinates (or all coordinates, if fewer than n)

 So, in Python, you can't simultaneously find out how many coordinates there are, and retrieve a subset of them. In a reasonable universe, there would have been GetParts() -> int, and GetCoords() -> List. This means that I need to call the MFC method twice; once to find out how many there are, and another time to get them.


<!-- page: PyCStatusBarCtrl__GetRect_meth.html -->

## PyCStatusBarCtrl.GetRect

 (left, top, right, bottom) = GetRect(nPane)

Retrieves the bounding rectangle of a part in a status bar control.

#### Parameters

- nPane : int

 Zero-based index of the part whose bounding rectangle is to be retrieved.


<!-- page: PyCStatusBarCtrl__GetTextAttr_meth.html -->

## PyCStatusBarCtrl.GetTextAttr

 int = GetTextAttr(nPane)

Retrieve the attributes of the text in the given part of a status bar control.

#### Parameters

- nPane : int

 Zero-based index of the part whose text is to be retrieved.


<!-- page: PyCStatusBarCtrl__GetTextLength_meth.html -->

## PyCStatusBarCtrl.GetTextLength

 int = GetTextLength(nPane)

Retrieve the length the text in the given part of a status bar control.

#### Parameters

- nPane : int

 Zero-based index of the part whose text is to be retrieved.


<!-- page: PyCStatusBarCtrl__GetText_meth.html -->

## PyCStatusBarCtrl.GetText

 text = GetText(nPane)

Retrieve the text from the given part of a status bar control.

#### Parameters

- nPane : int

 Zero-based index of the part whose text is to be retrieved.


<!-- page: PyCStatusBarCtrl__SetMinHeight_meth.html -->

## PyCStatusBarCtrl.SetMinHeight

 SetMinHeight(nHeight)

Set the minimum height of a status bar control's drawing area.

#### Parameters

- nHeight : int

 Minimum height


<!-- page: PyCStatusBarCtrl__SetParts_meth.html -->

## PyCStatusBarCtrl.SetParts

 SetParts(coord)

Sets the number of parts in a status bar control and the coordinate of the right edge of each part.

#### Parameters

- coord : int...

 Coordinates of each part


<!-- page: PyCStatusBarCtrl__SetSimple_meth.html -->

## PyCStatusBarCtrl.SetSimple

 SetSimple(bSimple)

Specify whether a status bar control displays simple text or displays all control parts set by a previous call to SetParts.

#### Parameters

- bSimple : int

 If non-zero, displays simple text.


<!-- page: PyCStatusBarCtrl__SetText_meth.html -->

## PyCStatusBarCtrl.SetText

 SetText(text, nPane, nType)

Set the text in the given part of a status bar control.

#### Parameters

- text : string

 The text to display

- nPane : int

 Zero-based index of the part to set.

- nType : int

 Type of drawing operation.

#### Comments

 The drawing type can be set to one of:~ 0 - The text is drawn with a border to appear lower than the plane of the status bar.~ win32con.SBT_NOBORDERS - The text is drawn without borders.~ win32con.SBT_OWNERDRAW - The text is drawn by the parent window.~ win32con.SBT_POPOUT - The text is drawn with a border to appear higher than the plane of the status bar.


<!-- page: PyCStatusBarCtrl__SetTipText_meth.html -->

## PyCStatusBarCtrl.SetTipText

 SetTipText(nPane, text)

Sets the tooltip text for a pane in a status bar. The status bar must have been created with the afxres.SBT_TOOLTIPS control style to enable ToolTips.

#### Parameters

- nPane : int

 The zero-based index of status bar pane to receive the tooltip text.

- text : string

 The string containing the tooltip text.

#### Comments

 Pay attention, this tooltip text is ONLY displayed in two situations:
1. When the corresponding pane in the status bar contains only an icon.
2. When the corresponding pane in the status bar contains text that is truncated due to the size of the pane.
To make the tooltip appear even if the text is not truncated, you could add additional spaces to the end of the pane text.

#### MFC References

- CStatusBarCtrl::SetTipText


---

<!-- object: PyCTL_CONTEXT -->


<!-- page: PyCTL_CONTEXT.html -->

---

## PyCTL_CONTEXT Object

 Object containing a Certificate Trust List

#### Methods

- CertFreeCTLContext

 Closes the context handle

- CertEnumCTLContextProperties

 Lists property id's for the context

- CertEnumSubjectInSortedCTL

 Retrieves trusted subjects contained in CTL

- CertDeleteCTLFromStore

 Removes the CTL from the store that it is contained in

- CertSerializeCTLStoreElement

 Serializes the CTL and its properties

#### Properties

- int HCTL_CONTEXT
 Raw message handle


<!-- page: PyCTL_CONTEXT__CertDeleteCTLFromStore_meth.html -->

## PyCTL_CONTEXT.CertDeleteCTLFromStore

 CertDeleteCTLFromStore()

Removes the CTL from the store that it is contained in


<!-- page: PyCTL_CONTEXT__CertEnumCTLContextProperties_meth.html -->

## PyCTL_CONTEXT.CertEnumCTLContextProperties

 (int,...) = CertEnumCTLContextProperties()

Lists property id's for the context


<!-- page: PyCTL_CONTEXT__CertEnumSubjectInSortedCTL_meth.html -->

## PyCTL_CONTEXT.CertEnumSubjectInSortedCTL

 ((str,str),...) = CertEnumSubjectInSortedCTL()

Retrieves trusted subjects contained in CRL

#### Return Value

Returns a sequence of tuples containing two strings (SubjectIdentifier, EncodedAttributes)


<!-- page: PyCTL_CONTEXT__CertFreeCTLContext_meth.html -->

## PyCTL_CONTEXT.CertFreeCTLContext

 CertFreeCTLContext()

Closes the CTL handle


<!-- page: PyCTL_CONTEXT__CertSerializeCTLStoreElement_meth.html -->

## PyCTL_CONTEXT.CertSerializeCTLStoreElement

 string = CertSerializeCTLStoreElement(Flags)

Serializes the CTL and its properties

#### Parameters

- Flags=0 : int

 Reserved, use only 0 if passed in


---

<!-- object: PyCTL_USAGE -->


<!-- page: PyCTL_USAGE.html -->

---

## PyCTL_USAGE Object

 Sequence of string OIDs (szOID_*). This struct is identical to CERT_ENHKEY_USAGE.


---

<!-- object: PyCTabCtrl -->


<!-- page: PyCTabCtrl.html -->

---

## PyCTabCtrl Object

 A class which encapsulates an MFC CTabCtrl object. Derived from a PyCWnd object.

#### Methods

- GetCurSel

 Gets the current selection of a tab control.

- GetItemCountl

 Returns the number of tabs in the control.

- SetCurSel

 Sets the current selection of a tab control.


<!-- page: PyCTabCtrl__GetCurSel_meth.html -->

## PyCTabCtrl.GetCurSel

 int = GetCurSel()

Gets the current selection of a tab control.

#### Return Value

The zero-based index of the currently selected item, or -1 if no selection.


<!-- page: PyCTabCtrl__GetItemCountl_meth.html -->

## PyCTabCtrl.GetItemCountl

 int = GetItemCountl()

Returns the number of tabs in the control.


<!-- page: PyCTabCtrl__SetCurSel_meth.html -->

## PyCTabCtrl.SetCurSel

 int = SetCurSel(index)

Sets the current selection of a tab control.

#### Parameters

- index : int

 The index of the tab to set current.

#### Return Value

The zero-based index of the previously selected item.


---

<!-- object: PyCToolBar -->


<!-- page: PyCToolBar.html -->

---

## PyCToolBar Object

 A class which encapsulates an MFC CToolBar . Derived from a PyCControlBar object.

#### Methods

- GetButtonStyle

 Retrieves the style for a button.

- GetButtonText

 Gets the text for a button.

- GetItemID

 Returns the command ID of a button or separator at the given index.

- SetButtonInfo

 Gets the associated tooltip control

- GetToolBarCtrl

 Returns the tool bar control object associated with the tool bar

- LoadBitmap

 Loads the bitmap containing bitmap-button images.

- LoadToolBar

 Loads a toolbar from a Toolbar resource.

- SetBarStyle

 Sets toolbar's (CBRS_xxx) part of style

- SetBitmap

 Sets a bitmapped image.

- SetButtonInfo

 Sets the button's command ID, style, and image number.

- SetButtons

 Sets button styles and an index of button images within the bitmap.

- SetButtonStyle

 Sets the style for a button

- SetHeight

 Sets the height of the toolbar.

- SetSizes

 Sets the sizes for the toolbar items.

- SetButtonInfo

 Sets the tooltips control


<!-- page: PyCToolBar__GetButtonStyle_meth.html -->

## PyCToolBar.GetButtonStyle

 GetButtonStyle(index)

Retrieves the style for a button.

#### Parameters

- index : int

 Index of the item whose style is to be retrieved.


<!-- page: PyCToolBar__GetButtonText_meth.html -->

## PyCToolBar.GetButtonText

 string = GetButtonText(index)

Gets the text for a button.

#### Parameters

- index : int

 Index of the item whose text is to be retrieved.


<!-- page: PyCToolBar__GetItemID_meth.html -->

## PyCToolBar.GetItemID

 GetItemID(index)

Returns the command ID of a button or separator at the given index.

#### Parameters

- index : int

 Index of the item whose ID is to be retrieved.


<!-- page: PyCToolBar__GetToolBarCtrl_meth.html -->

## PyCToolBar.GetToolBarCtrl

 PyCToolBarCtrl = GetToolBarCtrl()

Gets the toolbar control object for the toolbar


<!-- page: PyCToolBar__GetToolTips_meth.html -->

## PyCToolBar.GetToolTips

 GetToolTips()

Returns the associated tooltips control


<!-- page: PyCToolBar__LoadBitmap_meth.html -->

## PyCToolBar.LoadBitmap

 LoadBitmap(id)

Loads the bitmap containing bitmap-button images.

#### Parameters

- id : PyResourceId

 Name or id of the resource that contains the bitmap.

#### Comments

 The bitmap should contain one image for each toolbar button. If the images are not of the standard size (16 pixels wide and 15 pixels high), call PyCToolBar::SetSizes to set the button sizes and their images.


<!-- page: PyCToolBar__LoadToolBar_meth.html -->

## PyCToolBar.LoadToolBar

 LoadToolBar(id)

Loads a toolbar from a toolbar resource.

#### Parameters

- id : PyResourceId

 Name or resource id of the resource

#### Comments

 The bitmap should contain one image for each toolbar button. If the images are not of the standard size (16 pixels wide and 15 pixels high), call PyCToolBar::SetSizes to set the button sizes and their images.


<!-- page: PyCToolBar__SetBarStyle_meth.html -->

## PyCToolBar.SetBarStyle

 SetBarStyle(style)

Sets the toolbar part of style

#### Parameters

- style : long

 The toolbar style to set.


<!-- page: PyCToolBar__SetBitmap_meth.html -->

## PyCToolBar.SetBitmap

 SetBitmap(hBitmap)

Sets a bitmapped image.

#### Parameters

- hBitmap : int

 The handle to a bitmap resource.

#### Comments

 Call this method to set the bitmap image for the toolbar. For example, call SetBitmap to change the bitmapped image after the user takes an action on a document that changes the action of a button.


<!-- page: PyCToolBar__SetButtonInfo_meth.html -->

## PyCToolBar.SetButtonInfo

 SetButtonInfo(index, ID, style, imageIx)

Sets the button's command ID, style, and image number.

#### Parameters

- index : int

 Index of the button or separator whose information is to be set.

- ID : int

 The value to which the button's command ID is set.

- style : int

 The new button style

- imageIx : int

 New index for the button's image within the bitmap


<!-- page: PyCToolBar__SetButtonStyle_meth.html -->

## PyCToolBar.SetButtonStyle

 SetButtonStyle(index, style)

Sets the style for a button.

#### Parameters

- index : int

 Index of the item whose style is to be set

- style : int

 The new style


<!-- page: PyCToolBar__SetButtonText_meth.html -->

## PyCToolBar.SetButtonText

 SetButtonText(index, text)

Sets the text for a button.

#### Parameters

- index : int

 Index of the item whose style is to be set

- text : string

 The new text


<!-- page: PyCToolBar__SetButtons_meth.html -->

## PyCToolBar.SetButtons

 SetButtons(buttons)

Sets button styles and an index of button images within the bitmap.

#### Parameters

- buttons : tuple

 A tuple containing the ID's of the buttons.

#### Alternative Parameters

- numButtons

 The number of buttons to pre-allocate. If this option is used, then PyCToolBar::PySetButtonInfo must be used.


<!-- page: PyCToolBar__SetHeight_meth.html -->

## PyCToolBar.SetHeight

 SetHeight(height)

Sets the height of the toolbar.

#### Parameters

- height : int

 The height in pixels of the toolbar.


<!-- page: PyCToolBar__SetSizes_meth.html -->

## PyCToolBar.SetSizes

 SetSizes(sizeButton, sizeButton)

Sets the size of each button.

#### Parameters

- sizeButton : (cx, cy)

 The size of each button.

- sizeButton : (cx, cy)

 The size of each bitmap.


<!-- page: PyCToolBar__SetToolTips_meth.html -->

## PyCToolBar.SetToolTips

 SetToolTips(obTTC)

Sets the tooltips control

#### Parameters

- obTTC : PyCToolTipCtrl

 The ToolTipCtrl ctrl to be set.


---

<!-- object: PyCToolBarCtrl -->


<!-- page: PyCToolBarCtrl.html -->

---

## PyCToolBarCtrl Object

 A class which encapsulates an MFC CToolBarCtrl . Derived from a PyCWnd object. Created using PyCToolBar::GetToolBarCtrl

#### Methods

- AddBitmap

 Add one or more button images to the list of button images

- AddButtons

 Add one or more buttons

- AddStrings

 Add one or more strings

- AutoSize

 Resize the entire toolbar

- CheckButton

 Check or clear a button

- CommandToIndex

 Retrieve the zero-based index for the button associated with the specified command identifier.

- CreateWindow

 Create the actual control

- Customize

 Display the customize toolbar dialog box

- DeleteButton

 Delete a button from the toolbar control

- EnableButton

 Enable or disable a toolbar control button.

- GetBitmapFlags

 Retrieve the bitmap flags from the toolbar.

- GetButton

 Retrieve information about the specified button in a toolbar control.

- GetButtonCount

 Retrieve a count of the buttons currently in the toolbar control.

- GetItemRect

 Retrieve the bounding rectangle of a button in a toolbar control.

- GetRows

 Retrieve the number of rows of buttons currently displayed

- HideButton

 Hide or show the specified button in a toolbar control.

- Indeterminate

 Hide or show the specified button in a toolbar control.

- InsertButton

 Insert a button into a toolbar control.

- IsButtonChecked

 See if a button is checked.

- IsButtonEnabled

 See if a button is enabled.

- IsButtonHidden

 See if a button is checked.

- IsButtonIndeterminate

 See if a button is Indeterminate.

- IsButtonPressed

 See if a button is pressed.

- PressButton

 Mark or unmark the specified button as pressed.

- SetBitmapSize

 Set the size of the actual bitmapped images to be added to a toolbar control.

- SetButtonSize

 Set the size of the actual buttons to be added to a toolbar control.

- SetCmdID

 Set the command identifier which will be sent to the owner window when the specified button is pressed.

- SetRows

 Ask the toolbar control to resize itself to the requested number of rows.


<!-- page: PyCToolBarCtrl__AddBitmap_meth.html -->

## PyCToolBarCtrl.AddBitmap

 int = AddBitmap(numButtons, bitmap )

Add one or more button images to the list of button images

#### Parameters

- numButtons : int

 Number of button images in the bitmap.

- bitmap : PyBitmap

 Bitmap containing button or buttons to be added

#### MFC References

- CToolBarCtrl::AddBitmap


<!-- page: PyCToolBarCtrl__AddButtons_meth.html -->

## PyCToolBarCtrl.AddButtons

 int = AddButtons()

Add one or more buttons to the toolbar

#### MFC References

- CToolBarCtrl::AddButtons


<!-- page: PyCToolBarCtrl__AddStrings_meth.html -->

## PyCToolBarCtrl.AddStrings

 int = AddStrings(strings)

Add one or more strings to the toolbar

#### Parameters

- strings : string...

 Strings to add. Can give more than one string.


<!-- page: PyCToolBarCtrl__AutoSize_meth.html -->

## PyCToolBarCtrl.AutoSize

 AutoSize()

Resize the entire toolbar control

#### MFC References

- CToolBarCtrl::AutoSize


<!-- page: PyCToolBarCtrl__CheckButton_meth.html -->

## PyCToolBarCtrl.CheckButton

 int = CheckButton(nID, bCheck )

Check or clear a given button in a toolbar control

#### Parameters

- nID : int

 Command identifier of the button to check or clear.

- bCheck=1 : int

 1 to check, 0 to clear the button

#### MFC References

- CToolBarCtrl::CheckButton


<!-- page: PyCToolBarCtrl__CommandToIndex_meth.html -->

## PyCToolBarCtrl.CommandToIndex

 int = CommandToIndex(nID)

Retrieve the zero-based index for the button associated with the specified command identifier.

#### Parameters

- nID : int

 Command identifier of the button you want to find.

#### MFC References

- CToolBarCtrl::CommandToIndex


<!-- page: PyCToolBarCtrl__CreateWindow_meth.html -->

## PyCToolBarCtrl.CreateWindow

 CreateWindow(style, rect, parent, id)

Creates the window for a new toolbar object

#### Parameters

- style : int

 The style for the button. Use any of the win32con.BS_* constants.

- rect : (left, top, right, bottom)

 The size and position of the button.

- parent : PyCWnd

 The parent window of the button. Usually a PyCDialog.

- id : int

 The buttons control ID.

#### MFC References

- CToolBarCtrl::Create


<!-- page: PyCToolBarCtrl__Customize_meth.html -->

## PyCToolBarCtrl.Customize

 Customize()

Display the Customize Toolbar dialog box.

#### MFC References

- CToolBarCtrl::Customize


<!-- page: PyCToolBarCtrl__DeleteButton_meth.html -->

## PyCToolBarCtrl.DeleteButton

 DeleteButton(nID)

Delete a button from the toolbar control.

#### Parameters

- nID : int

 ID of the button to delete.

#### MFC References

- CToolBarCtrl::DeleteButton


<!-- page: PyCToolBarCtrl__EnableButton_meth.html -->

## PyCToolBarCtrl.EnableButton

 EnableButton(nID, bEnable)

Enable or disable a toolbar control button.

#### Parameters

- nID : int

 ID of the button to enable or disable.

- bEnable=1 : int

 1 to enable, 0 to disable

#### MFC References

- CToolBarCtrl::EnableButton


<!-- page: PyCToolBarCtrl__GetBitmapFlags_meth.html -->

## PyCToolBarCtrl.GetBitmapFlags

 int = GetBitmapFlags()

retrieve the bitmap flags from the toolbar.

#### MFC References

- CToolBarCtrl::GetBitmapFlags


<!-- page: PyCToolBarCtrl__GetButtonCount_meth.html -->

## PyCToolBarCtrl.GetButtonCount

 int = GetButtonCount()

Retrieve a count of the buttons currently in the toolbar control.

#### MFC References

- CToolBarCtrl::GetButtonCount


<!-- page: PyCToolBarCtrl__GetButton_meth.html -->

## PyCToolBarCtrl.GetButton

 PyCToolBarCtrl::TBBUTTON = GetButton(nID)

Retrieve information about the specified button in a toolbar control.

#### Parameters

- nID : int

 ID of the button to retrieve.

#### MFC References

- CToolBarCtrl::GetButton


<!-- page: PyCToolBarCtrl__GetItemRect_meth.html -->

## PyCToolBarCtrl.GetItemRect

 left, top, right, bottom = GetItemRect(nID)

Retrieve the bounding rectangle of a button in a toolbar control.

#### Parameters

- nID : int

 ID of the button.

#### MFC References

- CToolBarCtrl::GetItemRect


<!-- page: PyCToolBarCtrl__GetRows_meth.html -->

## PyCToolBarCtrl.GetRows

 left, top, right, bottom = GetRows()

Retrieve the number of rows of buttons currently displayed

#### MFC References

- CToolBarCtrl::GetRows


<!-- page: PyCToolBarCtrl__HideButton_meth.html -->

## PyCToolBarCtrl.HideButton

 HideButton(nID, bEnable)

Hide or show the specified button in a toolbar control.

#### Parameters

- nID : int

 ID of the button to hide.

- bEnable=1 : int

 1 to hide, 0 to show.

#### MFC References

- CToolBarCtrl::HideButton


<!-- page: PyCToolBarCtrl__Indeterminate_meth.html -->

## PyCToolBarCtrl.Indeterminate

 Indeterminate(nID, bEnable)

Mark or unmark the specified button as indeterminate

#### Parameters

- nID : int

 ID of the button to mark.

- bEnable=1 : int

 1 to hide, 0 to show.

#### MFC References

- CToolBarCtrl::Indeterminate


<!-- page: PyCToolBarCtrl__InsertButton_meth.html -->

## PyCToolBarCtrl.InsertButton

 int = InsertButton(nID, button )

Insert a button in a toolbar control.

#### Parameters

- nID : int

 Zero-based index of a button. This function inserts the new button to the left of this button.

- button : PyCToolBarCtrl::TBBUTTON

 Bitmap containing button to be inserted

#### Comments

 The image and/or string whose index you provide must have previously been added to the toolbar control's list using PyCToolBarCtrl::AddBitmap, PyCToolBarCtrl::AddString , and/or PyCToolBarCtrl::AddStrings.

#### MFC References

- CToolBarCtrl::InsertButton


<!-- page: PyCToolBarCtrl__IsButtonChecked_meth.html -->

## PyCToolBarCtrl.IsButtonChecked

 int = IsButtonChecked(nID)

Determine whether the specified button in a toolbar control is checked.

#### Parameters

- nID : int

 ID of the button to check.

#### MFC References

- CToolBarCtrl::IsButtonChecked


<!-- page: PyCToolBarCtrl__IsButtonEnabled_meth.html -->

## PyCToolBarCtrl.IsButtonEnabled

 int = IsButtonEnabled(nID)

Determine whether the specified button in a toolbar control is enabled.

#### Parameters

- nID : int

 ID of the button to check.

#### MFC References

- CToolBarCtrl::IsButtonEnabled


<!-- page: PyCToolBarCtrl__IsButtonHidden_meth.html -->

## PyCToolBarCtrl.IsButtonHidden

 int = IsButtonHidden(nID)

Determine whether the specified button in a toolbar control is hidden.

#### Parameters

- nID : int

 ID of the button to check.

#### MFC References

- CToolBarCtrl::IsButtonHidden


<!-- page: PyCToolBarCtrl__IsButtonIndeterminate_meth.html -->

## PyCToolBarCtrl.IsButtonIndeterminate

 int = IsButtonIndeterminate(nID)

Determine whether the specified button in a toolbar control is indeterminate.

#### Parameters

- nID : int

 ID of the button to check.

#### MFC References

- CToolBarCtrl::IsButtonIndeterminate


<!-- page: PyCToolBarCtrl__IsButtonPressed_meth.html -->

## PyCToolBarCtrl.IsButtonPressed

 int = IsButtonPressed(nID)

Determine whether the specified button in a toolbar control is pressed.

#### Parameters

- nID : int

 ID of the button to check.

#### MFC References

- CToolBarCtrl::IsButtonPressed


<!-- page: PyCToolBarCtrl__PressButton_meth.html -->

## PyCToolBarCtrl.PressButton

 PressButton(nID, bEnable)

Mark or unmark the specified button as pressed.

#### Parameters

- nID : int

 ID of the button to mark.

- bEnable=1 : int

 1 to mark, 0 to unmark.

#### MFC References

- CToolBarCtrl::PressButton


<!-- page: PyCToolBarCtrl__SetBitmapSize_meth.html -->

## PyCToolBarCtrl.SetBitmapSize

 SetBitmapSize(width, height)

Set the size of the actual bitmapped images to be added to a toolbar control.

#### Parameters

- width=16 : int

 Width of bitmap images.

- height=15 : int

 Height of bitmap images.

#### Alternative Parameters

- width

 Width of bitmap images.

- height

 Height of bitmap images.

#### MFC References

- CToolBarCtrl::SetBitmapSize


<!-- page: PyCToolBarCtrl__SetButtonSize_meth.html -->

## PyCToolBarCtrl.SetButtonSize

 SetButtonSize(width, height)

Set the size of the buttons to be added to a toolbar control.

#### Parameters

- width=16 : int

 Width of buttons

- height=15 : int

 Height of buttons

#### Alternative Parameters

- width

 Width of bitmap images.

- height

 Height of bitmap images.

#### MFC References

- CToolBarCtrl::SetButtonSize


<!-- page: PyCToolBarCtrl__SetCmdID_meth.html -->

## PyCToolBarCtrl.SetCmdID

 SetCmdID(nIndex, nID)

Set the command identifier which will be sent to the owner window when the specified button is pressed.

#### Parameters

- nIndex : int

 The zero-based index of the button whose command ID is to be set.

- nID : int

 The command ID to set the selected button to.

#### MFC References

- CToolBarCtrl::SetCmdID


<!-- page: PyCToolBarCtrl__SetRows_meth.html -->

## PyCToolBarCtrl.SetRows

 left, top, right, bottom = SetRows(nRows, bLarger )

Ask the toolbar control to resize itself to the requested number of rows.

#### Parameters

- nRows : int

 Requested number of rows.

- bLarger : int

 Tells whether to use more rows or fewer rows if the toolbar cannot be resized to the requested number of rows.

#### MFC References

- CToolBarCtrl::SetRows


<!-- page: PyCToolBarCtrl__TBUTTON_tuple_meth.html -->

## PyCToolBarCtrl.TBUTTON tuple

 TBUTTON tuple(iBitmap, idCommand, fsState, fsStyle, userob, iString)

Describes a TBUTTON tuple, used by the PyCToolBarCtrl AddButtons method

#### Parameters

- iBitmap : int

 Zero-based index of button image

- idCommand : int

 Command to be sent when button pressed

- fsState : int

 Button state. Can be any of the TBSTATE values defined in win32con

- fsStyle : int

 Button style. Can be any of the TBSTYLE values defined in win32con

- userob : object

 Arbitrary Python object

- iString : int

 Zero-based index of button label string

#### Comments

 Userob is any Python object at all, but no reference count is kept, so you must ensure the object remains referenced throughout.


---

<!-- object: PyCToolTipCtrl -->


<!-- page: PyCToolTipCtrl.html -->

---

## PyCToolTipCtrl Object

 A windows tooltip control. Encapsulates an MFC CToolTipCtrl class. Derived from PyCControl.

#### Methods

- CreateWindow

 Creates the window for a new progress bar object.

- UpdateTipText

 Update the tool tip text for a control's tools

- AddTool

 Adds a tool to tooltip control.

- SetMaxTipWidth


<!-- page: PyCToolTipCtrl__AddTool_meth.html -->

## PyCToolTipCtrl.AddTool

 AddTool(wnd, text, rect, id)

Adds a tool to tooltip control.

#### Parameters

- wnd : PyCWnd

 The window of the tool.

- text : string

 The text for the tool.

- rect=None : int, int, int, int

 The default rectangle

- id : int

 The id of the tool


<!-- page: PyCToolTipCtrl__CreateWindow_meth.html -->

## PyCToolTipCtrl.CreateWindow

 CreateWindow(parent, style)

Creates the actual control.

#### Parameters

- parent : PyCWnd

 The parent window of the control.

- style : int

 The style for the control.


<!-- page: PyCToolTipCtrl__SetMaxTipWidth_meth.html -->

## PyCToolTipCtrl.SetMaxTipWidth

 int = SetMaxTipWidth(width)

#### Parameters

- width : int

 The new width


<!-- page: PyCToolTipCtrl__UpdateTipText_meth.html -->

## PyCToolTipCtrl.UpdateTipText

 UpdateTipText(text, wnd, id)

Update the tool tip text for a control's tools

#### Parameters

- text : string

 The text for the tool.

- wnd : PyCWnd

 The window of the tool.

- id : int

 The id of the tool


---

<!-- object: PyCTreeCtrl -->


<!-- page: PyCTreeCtrl.html -->

---

## PyCTreeCtrl Object

 A class which encapsulates an MFC CTreeCtrl object. Derived from a PyCWnd object.

#### Methods

- CreateWindow

 Creates the actual window for the object.

- GetCount

 Retrieves the number of tree items associated with a tree view control.

- GetIndent

 Retrieves the offset (in pixels) of a tree view item from its parent.

- SetIndent

 Sets the offset (in pixels) of a tree view item from its parent.

- GetImageList

 Retrieves the current image list.

- SetImageList

 Assigns an image list to a list view control.

- GetNextItem

 Retrieves the next item.

- ItemHasChildren

 Returns nonzero if the specified item has child items.

- GetChildItem

 Retrieves the child item of the specified tree view item.

- GetNextSiblingItem

 Retrieves the next sibling of the specified tree view item.

- GetPrevSiblingItem

 Retrieves the previous sibling of the specified tree view item.

- GetParentItem

 Retrieves the parent item of the specified tree view item.

- GetFirstVisibleItem

 Retrieves the first visible item of the specified tree view item.

- GetNextVisibleItem

 Retrieves the next visible item of the specified tree view item.

- GetNextVisibleItem

 Retrieves the previous visible item of the specified tree view item.

- GetSelectedItem

 Retrieves the currently selected tree view item.

- GetDropHilightItem

 Retrieves the target of a drag-and-drop operation.

- GetRootItem

 Retrieves the root of the specified tree view item.

- GetToolTips

 Returns the tooltip control

- GetItem

 Retrieves the details of an items attributes.

- SetItem

 Sets some of all of an items attributes.

- GetItemState

 Retrieves the state of an item.

- SetItemState

 Sets the state of an item.

- GetItemImage

 Retrieves the index of an items images.

- SetItemImage

 Sets the index of an items images.

- SetItemText

 Changes the text of a list view item or subitem.

- GetItemText

 Retrieves the text of a list view item or subitem.

- GetItemData

 Retrieves the application-specific value associated with an item.

- SetItemData

 Sets the item's application-specific value

- GetItemRect

 Retrieves the bounding rectangle of a tree view item.

- GetEditControl

 Retrieves the handle of the edit control used to edit the specified tree view item.

- GetVisibleCount

 Retrieves the number of visible tree items associated with a tree view control.

- InsertItem

 Inserts an item into the list.

- DeleteItem

 Deletes an item from the list.

- DeleteAllItems

 Deletes all items from the list.

- Expand

 Expands, or collapses, the child items of the specified tree view item.

- Select

 Selects, scrolls into view, or redraws a specified tree view item.

- SelectItem

 Selects a specified tree view item.

- SelectDropTarget

 Redraws the tree item as the target of a drag-and-drop operation.

- SelectSetFirstVisible

 Selects a specified tree view item as the first visible item.

- EditLabel

 Edits a specified tree view item in-place.

- CreateDragImage

 Creates a dragging bitmap for the specified tree view item.

- SortChildren

 Sorts the children of a given parent item.

- EnsureVisible

 Ensures that a tree view item is visible in its tree view control.

- HitTest

 Determines which tree view item, if any, is at a specified position.

#### Comments

 Sam Rushing has found the following tidbits:
 You can implement dynamic collapsing and expanding of events for large collections yourself - see KB Q130697
 The MFC docs tell you to use TVE_COLLAPSERESET in order to throw away the child items when collapsing a node. They neglect to tell you a very important tidbit: that you need to combine the flag with TVE_COLLAPSE. This is pointed out in the docs for TreeView_Expand(), but not in those for CTreeCtrl::Expand.


<!-- page: PyCTreeCtrl__CreateDragImage_meth.html -->

## PyCTreeCtrl.CreateDragImage

 PyCImageList = CreateDragImage(item)

Creates a dragging bitmap for the specified tree view item.

#### Parameters

- item : HTREEITEM

 The item to edit.


<!-- page: PyCTreeCtrl__CreateWindow_meth.html -->

## PyCTreeCtrl.CreateWindow

 CreateWindow(style, rect, PyCWnd, id)

Creates the actual window for the object.

#### Parameters

- style : int

 The window style

- rect : int, int, int, int

 The default rectangle

- PyCWnd : parent

 The parent window

- id : int

 The control ID

#### MFC References

- CTreeCtrl::Create


<!-- page: PyCTreeCtrl__DeleteAllItems_meth.html -->

## PyCTreeCtrl.DeleteAllItems

 object = DeleteAllItems()

Deletes all items in the control


<!-- page: PyCTreeCtrl__DeleteItem_meth.html -->

## PyCTreeCtrl.DeleteItem

 DeleteItem(item)

Deletes the specified item.

#### Parameters

- item : HTREEITEM

 The specified item


<!-- page: PyCTreeCtrl__EditLabel_meth.html -->

## PyCTreeCtrl.EditLabel

 PyCEdit = EditLabel(item)

Edits a specified tree view item in-place.

#### Parameters

- item : HTREEITEM

 The item to edit.


<!-- page: PyCTreeCtrl__EnsureVisible_meth.html -->

## PyCTreeCtrl.EnsureVisible

 int = EnsureVisible(item)

Ensures that a tree view item is visible in its tree view control.

#### Parameters

- item : HTREEITEM

 The item to edit.


<!-- page: PyCTreeCtrl__Expand_meth.html -->

## PyCTreeCtrl.Expand

 Expand(item, code)

Expands, or collapses, the child items of the specified tree view item.

#### Parameters

- item : HTREEITEM

 The specified item

- code : int

 The action to take


<!-- page: PyCTreeCtrl__GetChildItem_meth.html -->

## PyCTreeCtrl.GetChildItem

 HTREEITEM = GetChildItem(item)

Retrieves the first child item.

#### Parameters

- item : HTREEITEM

 The specified item


<!-- page: PyCTreeCtrl__GetCount_meth.html -->

## PyCTreeCtrl.GetCount

 int = GetCount()

Retrieves the number of tree items associated with a tree view control.


<!-- page: PyCTreeCtrl__GetDropHilightItem_meth.html -->

## PyCTreeCtrl.GetDropHilightItem

 HTREEITEM = GetDropHilightItem()

Retrieves the target of a drag-and-drop operation.


<!-- page: PyCTreeCtrl__GetEditControl_meth.html -->

## PyCTreeCtrl.GetEditControl

 PyCEdit = GetEditControl()

Retrieves the handle of the edit control used to edit the specified tree view item.


<!-- page: PyCTreeCtrl__GetFirstVisibleItem_meth.html -->

## PyCTreeCtrl.GetFirstVisibleItem

 HTREEITEM = GetFirstVisibleItem()

Retrieves the first visible item of the tree view control.


<!-- page: PyCTreeCtrl__GetImageList_meth.html -->

## PyCTreeCtrl.GetImageList

 PyCImageList = GetImageList(nImageList)

Retrieves the current image list.

#### Parameters

- nImageList : int

 Value specifying which image list to retrieve. It can be one of:
- commctrl.LVSIL_NORMAL Image list with large icons.
- commctrl.LVSIL_SMALL Image list with small icons.
- commctrl.LVSIL_STATE Image list with state images.


<!-- page: PyCTreeCtrl__GetIndent_meth.html -->

## PyCTreeCtrl.GetIndent

 int = GetIndent()

Retrieves the offset (in pixels) of a tree view item from its parent.


<!-- page: PyCTreeCtrl__GetItemData_meth.html -->

## PyCTreeCtrl.GetItemData

 object = GetItemData(item)

Retrieves the application-specific value associated with an item.

#### Parameters

- item : HTREEITEM

 The index of the item whose data is to be retrieved.


<!-- page: PyCTreeCtrl__GetItemImage_meth.html -->

## PyCTreeCtrl.GetItemImage

 (int,int) = GetItemImage(item)

Retrieves the index of an items images.

#### Parameters

- item : HTREEITEM

 The specified item


<!-- page: PyCTreeCtrl__GetItemRect_meth.html -->

## PyCTreeCtrl.GetItemRect

 (int, int, int, int) = GetItemRect(item, bTextOnly )

Retrieves the bounding rectangle of a tree view item.

#### Parameters

- item : HTREEITEM

 The item whose Data is to be set.

- bTextOnly : int

 f this parameter is nonzero, the bounding rectangle includes only the text of the item. Otherwise it includes the entire line that the item occupies in the tree view control.


<!-- page: PyCTreeCtrl__GetItemState_meth.html -->

## PyCTreeCtrl.GetItemState

 (int,int) = GetItemState(item, stateMask )

Retrieves the state and mask of an item.

#### Parameters

- item : HTREEITEM

 The specified item

- stateMask : int

 The mask for the result.


<!-- page: PyCTreeCtrl__GetItemText_meth.html -->

## PyCTreeCtrl.GetItemText

 int = GetItemText(item)

Retrieves the text of a list view item or subitem.

#### Parameters

- item : HTREEITEM

 The item whose text is to be retrieved.


<!-- page: PyCTreeCtrl__GetItem_meth.html -->

## PyCTreeCtrl.GetItem

 TV_ITEM = GetItem(item, mask )

Retrieves the details of an items attributes.

#### Parameters

- item : HTREEITEM

 The item whose attributes are to be retrieved.

- mask=(all flags set) : int

 The requested attributes.


<!-- page: PyCTreeCtrl__GetNextItem_meth.html -->

## PyCTreeCtrl.GetNextItem

 HTREEITEM = GetNextItem(item, code )

Retrieves the next item.

#### Parameters

- item : HTREEITEM

 The specified item

- code : int

 Specifies the relationship of the item to fetch.


<!-- page: PyCTreeCtrl__GetNextSiblingItem_meth.html -->

## PyCTreeCtrl.GetNextSiblingItem

 HTREEITEM = GetNextSiblingItem(item)

Retrieves the next sibling of the specified tree view item.

#### Parameters

- item : HTREEITEM

 The specified item


<!-- page: PyCTreeCtrl__GetNextVisibleItem_meth.html -->

## PyCTreeCtrl.GetNextVisibleItem

 HTREEITEM = GetNextVisibleItem(item)

Retrieves the next visible item of the specified tree view item.

#### Parameters

- item : HTREEITEM

 The specified item


<!-- page: PyCTreeCtrl__GetParentItem_meth.html -->

## PyCTreeCtrl.GetParentItem

 HTREEITEM = GetParentItem(item)

Retrieves the parent item of the specified tree view item.

#### Parameters

- item : HTREEITEM

 The specified item


<!-- page: PyCTreeCtrl__GetPrevSiblingItem_meth.html -->

## PyCTreeCtrl.GetPrevSiblingItem

 HTREEITEM = GetPrevSiblingItem(item)

Retrieves the previous sibling of the specified tree view item.

#### Parameters

- item : HTREEITEM

 The specified item


<!-- page: PyCTreeCtrl__GetPrevVisibleItem_meth.html -->

## PyCTreeCtrl.GetPrevVisibleItem

 HTREEITEM = GetPrevVisibleItem(item)

Retrieves the previous visible item of the specified tree view item.

#### Parameters

- item : HTREEITEM

 The specified item


<!-- page: PyCTreeCtrl__GetRootItem_meth.html -->

## PyCTreeCtrl.GetRootItem

 HTREEITEM = GetRootItem()

Retrieves the root of the specified tree view item.


<!-- page: PyCTreeCtrl__GetSelectedItem_meth.html -->

## PyCTreeCtrl.GetSelectedItem

 HTREEITEM = GetSelectedItem()

Retrieves the currently selected tree view item.


<!-- page: PyCTreeCtrl__GetToolTips_meth.html -->

## PyCTreeCtrl.GetToolTips

 PyCToolTopCtrl = GetToolTips()

Returns the tooltip control


<!-- page: PyCTreeCtrl__GetVisibleCount_meth.html -->

## PyCTreeCtrl.GetVisibleCount

 int = GetVisibleCount()

Retrieves the number of visible tree items associated with a tree view control.


<!-- page: PyCTreeCtrl__HitTest_meth.html -->

## PyCTreeCtrl.HitTest

 (int, int) = HitTest(x,y)

Determines which tree view item, if any, is at a specified position.

#### Parameters

- x,y : point

 The point to test.

#### Return Value

The result is a tuple of (flags, hItem). flags may be a combination of the following values:

| | Value | Description
| |

---

 |

---

| | commctrl.TVHT_ABOVE | Above the client area.
| | commctrl.TVHT_BELOW | Below the client area.
| | commctrl.TVHT_NOWHERE | In the client area, but below the last item.
| | commctrl.TVHT_ONITEM | On the bitmap or label associated with an item.
| | commctrl.TVHT_ONITEMBUTTON | On the button associated with an item.
| | commctrl.TVHT_ONITEMICON | On the bitmap associated with an item.
| | commctrl.TVHT_ONITEMINDENT | In the indentation associated with an item.
| | commctrl.TVHT_ONITEMLABEL | On the label (string) associated with an item.
| | commctrl.TVHT_ONITEMRIGHT | In the area to the right of an item.
| | commctrl.TVHT_ONITEMSTATEICON | On the state icon for a tree view item that is in a user-defined state.
| | commctrl.TVHT_TOLEFT | To the left of the client area.
| | commctrl.TVHT_TORIGHT | To the right of the client area.


<!-- page: PyCTreeCtrl__InsertItem_meth.html -->

## PyCTreeCtrl.InsertItem

 int = InsertItem(hParent, hInsertAfter , item )

Inserts an item into the list.

#### Parameters

- hParent : HTREEITEM

 The parent item. If commctrl.TVI_ROOT or 0, it is added to the root.

- hInsertAfter : HTREEITEM

 The item to insert after. Can be an item or TVI_FIRST, TVI_LAST or TVI_SORT

- item : TV_ITEM

 A tuple describing the new item.

#### Alternative Parameters

- mask

 Integer specifying which attributes to set

- text

 The text of the item.

- image

 The index of the image to use.

- selectedImage

 The index of the items selected image.

- state

 The initial state of the item.

- stateMask

 Specifies which bits of the state are valid.

- lParam

 A user defined object for the item.

- parent

 The parent of the item.

- parent

 The parent of the item.

#### Alternative Parameters

- text

 The text for the item.

- image

 The index of the image to use.

- selectedImage

 The index of the items selected image.

- parent

 The parent of the item.

- insertAfter

 The item to insert the new item after, or TVI_FIRST, TVI_LAST or TVI_SORT

#### Alternative Parameters

- text

 The text for the item.

- parent

 The parent of the item.

- parent

 The parent of the item.


<!-- page: PyCTreeCtrl__ItemHasChildren_meth.html -->

## PyCTreeCtrl.ItemHasChildren

 int = ItemHasChildren(item)

Returns nonzero if the specified item has child items.

#### Parameters

- item : HTREEITEM

 The specified item


<!-- page: PyCTreeCtrl__SelectDropTarget_meth.html -->

## PyCTreeCtrl.SelectDropTarget

 SelectDropTarget(item)

Redraws the tree item as the target of a drag-and-drop operation.

#### Parameters

- item : HTREEITEM

 The specified item


<!-- page: PyCTreeCtrl__SelectItem_meth.html -->

## PyCTreeCtrl.SelectItem

 SelectItem(item)

Selects a specified tree view item.

#### Parameters

- item : HTREEITEM

 The specified item


<!-- page: PyCTreeCtrl__SelectSetFirstVisible_meth.html -->

## PyCTreeCtrl.SelectSetFirstVisible

 SelectSetFirstVisible(item)

Selects a specified tree view item as the first visible item.

#### Parameters

- item : HTREEITEM

 The specified item


<!-- page: PyCTreeCtrl__Select_meth.html -->

## PyCTreeCtrl.Select

 Select(item, code)

Selects, scrolls into view, or redraws a specified tree view item.

#### Parameters

- item : HTREEITEM

 The specified item

- code : int

 The action to take


<!-- page: PyCTreeCtrl__SetImageList_meth.html -->

## PyCTreeCtrl.SetImageList

 int = SetImageList(imageList, imageType )

Assigns an image list to a list view control.

#### Parameters

- imageList : PyCImageList

 The Image List to use.

- imageType : int

 Type of image list. It can be one of (COMMCTRL.) LVSIL_NORMAL, LVSIL_SMALL or LVSIL_STATE


<!-- page: PyCTreeCtrl__SetIndent_meth.html -->

## PyCTreeCtrl.SetIndent

 SetIndent(indent)

Sets the offset (in pixels) of a tree view item from its parent.

#### Parameters

- indent : int

 The new indent.


<!-- page: PyCTreeCtrl__SetItemData_meth.html -->

## PyCTreeCtrl.SetItemData

 int = SetItemData(item, Data )

Sets the item's application-specific value.

#### Parameters

- item : HTREEITEM

 The item whose Data is to be set.

- Data : int

 New value for the data.

#### Comments

 Note that a reference count is not added to the object. This it is your responsibility to make sure the object remains alive while in the list.


<!-- page: PyCTreeCtrl__SetItemImage_meth.html -->

## PyCTreeCtrl.SetItemImage

 SetItemImage(item, iImage, iSelectedImage)

Sets the index of an items images.

#### Parameters

- item : HTREEITEM

 The specified item

- iImage : int

 The offset of the image.

- iSelectedImage : int

 The offset of the selected image.


<!-- page: PyCTreeCtrl__SetItemState_meth.html -->

## PyCTreeCtrl.SetItemState

 SetItemState(item, state, stateMask)

Sets the state of item.

#### Parameters

- item : HTREEITEM

 The specified item

- state : int

 The new state

- stateMask : int

 The mask for the new state


<!-- page: PyCTreeCtrl__SetItemText_meth.html -->

## PyCTreeCtrl.SetItemText

 int = SetItemText(item, text )

Changes the text of a list view item or subitem.

#### Parameters

- item : HTREEITEM

 The item whose text is to be retrieved.

- text : string

 String that contains the new item text.


<!-- page: PyCTreeCtrl__SetItem_meth.html -->

## PyCTreeCtrl.SetItem

 int = SetItem(item)

Sets some of all of an items attributes.

#### Parameters

- item : TV_ITEM

 A tuple describing the new item.


<!-- page: PyCTreeCtrl__SortChildren_meth.html -->

## PyCTreeCtrl.SortChildren

 SortChildren(item)

Sorts the children of a given parent item.

#### Parameters

- item : HTREEITEM

 The specified parent item


---

<!-- object: PyCTreeView -->


<!-- page: PyCTreeView.html -->

---

## PyCTreeView Object

 A class which implements a CTreeView. Derived from PyCView and PyCTreeCtrl objects.

#### Methods

- PreCreateWindow

 Calls the underlying MFC PreCreateWindow method.

- GetTreeCtrl

 Returns the underlying tree control object.

- OnCommand

 Calls the standard Python framework OnCommand handler

#### Based On

PyCCtrlView


<!-- page: PyCTreeView__GetTreeCtrl_meth.html -->

## PyCTreeView.GetTreeCtrl

 PyCTreeCtrl = GetTreeCtrl()

Returns the underlying tree control object.


<!-- page: PyCTreeView__OnCommand_meth.html -->

## PyCTreeView.OnCommand

 OnCommand(wparam, lparam)

Calls the standard Python framework OnCommand handler

#### Parameters

- wparam : int

- lparam : int

#### See Also

- PyCWnd.OnCommand virtual method


<!-- page: PyCTreeView__PreCreateWindow_meth.html -->

## PyCTreeView.PreCreateWindow

 tuple = PreCreateWindow(createStruct)

Calls the underlying MFC PreCreateWindow method.

#### Parameters

- createStruct : tuple

 A tuple representing a CREATESTRUCT structure.


---

<!-- object: PyCView -->


<!-- page: PyCView.html -->

---

## PyCView Object

 A class which implements a generic CView. Derived from a PyCWnd object.

#### Methods

- CreateWindow

 Create the window for a view.

- GetDocument

 Returns the document for a view.

- OnActivateView

 Calls the underlying MFC OnActivateView method.

- OnInitialUpdate

 Calls the underlying MFC OnInitialUpdate method.

- OnMouseActivate

 Calls the underlying MFC OnMouseActivate method.

- PreCreateWindow

 Calls the underlying MFC PreCreateWindow method.

- OnFilePrint

 Calls the underlying MFC OnFilePrint method.

- OnFilePrint

 Calls the underlying MFC OnFilePrintPreview method.

- DoPreparePrinting

 Calls the underlying MFC DoPreparePrinting method.

- OnBeginPrinting

 Calls the underlying MFC OnBeginPrinting method.

- OnEndPrinting

 Calls the underlying MFC OnEndPrinting method.

#### Based On

PyCWnd


<!-- page: PyCView__CreateWindow_meth.html -->

## PyCView.CreateWindow

 CreateWindow(parent, id, style, rect)

Creates the window for a view.

#### Parameters

- parent : PyCWnd

 The parent window (usually a frame)

- id=win32ui.AFX_IDW_PANE_FIRST : int

 The child ID for the view

- style=win32ui.AFX_WS_DEFAULT_VIEW : int

 The style for the view

- rect=(0,0,0,0) : (left, top, right, bottom)

 The default position of the window.


<!-- page: PyCView__DoPreparePrinting_meth.html -->

## PyCView.DoPreparePrinting

 int = DoPreparePrinting()

Invoke the Print dialog box and create a printer device context.

#### Comments

 This function is usually called from PyCView.OnPreparePrinting virtual method


<!-- page: PyCView__GetDocument_meth.html -->

## PyCView.GetDocument

 PyCDocument = GetDocument()

Returns the document for a view.


<!-- page: PyCView__OnActivateView_meth.html -->

## PyCView.OnActivateView

 int = OnActivateView(activate, activateView , DeactivateView )

Calls the underlying MFC OnActivateView method.

#### Parameters

- activate : int

 Indicates whether the view is being activated or deactivated.

- activateView : PyCView

 The view object that is being activated.

- DeactivateView : PyCView

 The view object that is being deactivated.

#### See Also

- PyCView.OnActivateView virtual method


<!-- page: PyCView__OnActivateView_virtual.html -->

## PyCView.OnActivateView Virtual

 OnActivateView(bActivate, activateView , DeactivateView )

Called by the framework when a view is activated or deactivated.

#### Parameters

- bActivate : int

 Indicates whether the view is being activated or deactivated.

- activateView : PyCWnd

 The view object that is being activated.

- DeactivateView : PyCWnd

 The view object that is being deactivated.

#### Comments

 If a handler exists, the base MFC implementation is not called.
The activateView and deactiveView parameters are the same objects if the application's main frame window is activated with no change in the active view for example, if the focus is being transferred from another application to this one, rather than from one view to another within the application. This allows a view to re-realize its palette, if needed.

#### See Also

- PyCView::OnActivateView


<!-- page: PyCView__OnBeginPrinting_meth.html -->

## PyCView.OnBeginPrinting

 OnBeginPrinting()

Calls the underlying MFC OnBeginPrinting method.

#### See Also

- PyCView.OnBeginPrinting virtual method


<!-- page: PyCView__OnBeginPrinting_virtual.html -->

## PyCView.OnBeginPrinting Virtual

 OnBeginPrinting(dc, pInfo )

Called by the framework at the beginning of a print or print preview job, after OnPreparePrinting has been called.

#### Parameters

- dc : PyCDC

 The DC object.

- pInfo : PyCPrintInfo

 The print info object.

#### See Also

- PyCView::OnBeginPrinting


<!-- page: PyCView__OnDraw_virtual.html -->

## PyCView.OnDraw Virtual

 OnDraw(dc)

Called when the view should be drawn.

#### Parameters

- dc : PyCDC

 The DC object.

#### See Also

- PyCView::OnDraw


<!-- page: PyCView__OnEndPrinting_meth.html -->

## PyCView.OnEndPrinting

 OnEndPrinting()

Calls the underlying MFC OnEndPrinting method.

#### See Also

- PyCView.OnEndPrinting virtual method


<!-- page: PyCView__OnEndPrinting_virtual.html -->

## PyCView.OnEndPrinting Virtual

 OnEndPrinting(dc, pInfo )

Called by the framework after a document has been printed or previewed.

#### Parameters

- dc : PyCDC

 The DC object.

- pInfo : PyCPrintInfo

 The print info object.

#### See Also

- PyCView::OnEndPrinting


<!-- page: PyCView__OnFilePrintPreview_meth.html -->

## PyCView.OnFilePrintPreview

 OnFilePrintPreview()

Calls the underlying MFC OnFilePrintPreview method.


<!-- page: PyCView__OnFilePrint_meth.html -->

## PyCView.OnFilePrint

 OnFilePrint()

Calls the underlying MFC OnFilePrint method.


<!-- page: PyCView__OnInitialUpdate_meth.html -->

## PyCView.OnInitialUpdate

 OnInitialUpdate()

Calls the underlying MFC OnInitialUpdate method.

#### See Also

- PyCView.OnInitialUpdate virtual method


<!-- page: PyCView__OnInitialUpdate_virtual.html -->

## PyCView.OnInitialUpdate Virtual

 OnInitialUpdate()

Called before the first update for a view.

#### Comments

 The MFC base class is called only if no handler exists.

#### See Also

- PyCView::OnInitialUpdate


<!-- page: PyCView__OnMouseActivate_meth.html -->

## PyCView.OnMouseActivate

 int = OnMouseActivate(wnd, hittest , message )

Calls the base MFC OnMouseActivate function.

#### Parameters

- wnd : PyCWnd

- hittest : int

- message : int

#### See Also

- PyCWnd.OnMouseActivate virtual method


<!-- page: PyCView__OnPrepareDC_meth.html -->

## PyCView.OnPrepareDC

 OnPrepareDC()

Calls the underlying MFC OnPrepareDC method.

#### See Also

- PyCView.OnPrepareDC virtual method


<!-- page: PyCView__OnPrepareDC_virtual.html -->

## PyCView.OnPrepareDC Virtual

 OnPrepareDC(dc, pInfo )

Called to prepare the device context for a view.

#### Parameters

- dc : PyCDC

 The DC object.

- pInfo : PyCPrintInfo

 The print info object.

#### See Also

- PyCWnd::OnPrepareDC


<!-- page: PyCView__OnPreparePrinting_meth.html -->

## PyCView.OnPreparePrinting

 int = OnPreparePrinting()

Calls the underlying MFC OnPreparePrinting method.

#### See Also

- PyCView.OnPreparePrinting virtual method


<!-- page: PyCView__OnPreparePrinting_virtual.html -->

## PyCView.OnPreparePrinting Virtual

 OnPreparePrinting(pInfo)

Called by the framework before a document is printed or previewed

#### Parameters

- pInfo : PyCPrintInfo

 The print info object.

#### See Also

- PyCView::OnPreparePrinting


<!-- page: PyCView__OnPrint_virtual.html -->

## PyCView.OnPrint Virtual

 OnPrint(dc, pInfo )

Called when the view should be printed.

#### Parameters

- dc : PyCDC

 The DC object.

- pInfo : PyPrintInfo

 The PrintIfo object.

#### See Also

- PyCView::OnPrint


<!-- page: PyCView__OnUpdate_virtual.html -->

## PyCView.OnUpdate Virtual

 OnUpdate(sender, lHint , hint )

Called by the framework when a view needs updating.

#### Parameters

- sender : PyCView

- lHint : int

- hint : object

#### Comments

 Typically you should not perform any drawing directly from OnUpdate. Instead, determine the rectangle describing, in device coordinates, the area that requires updating; pass this rectangle to PyCWnd::InvalidateRect. You can then paint the update next PyCView::OnDraw

#### See Also

- PyCView::OnUpdate


<!-- page: PyCView__PreCreateWindow_meth.html -->

## PyCView.PreCreateWindow

 tuple = PreCreateWindow(createStruct)

Calls the underlying MFC PreCreateWindow method.

#### Parameters

- createStruct : tuple

 A tuple representing a CREATESTRUCT structure.

#### See Also

- PyCWnd.PreCreateWindow virtual method


---

<!-- object: PyCWinApp -->


<!-- page: PyCWinApp.html -->

---

## PyCWinApp Object

 An application class. Encapsulates an MFC CWinApp class

#### Methods

- AddDocTemplate

 Adds a template to the application list.

- FindOpenDocument

 Returns an existing document with the specified file name.

- GetDocTemplateList

 Returns a list of all document templates in use.

- InitDlgInstance

 Calls critical InitInstance processing for a dialog based application.

- LoadCursor

 Loads a cursor.

- LoadStandardCursor

 Loads a standard cursor.

- LoadOEMCursor

 Loads an OEM cursor.

- LoadIcon

 Loads an icon resource.

- LoadStandardIcon

 Loads an icon resource.

- OpenDocumentFile

 Opens a document file by name.

- OnFileNew

 Calls the underlying OnFileNew MFC method.

- OnFileOpen

 Calls the underlying OnFileOpen MFC method.

- RemoveDocTemplate

 Removes a template to the application list.

- Run

 Starts the main application message pump.

- IsInproc

 Returns a flag to indicate if the created CWinApp was in the DLL, or an external EXE.


<!-- page: PyCWinApp__AddDocTemplate_meth.html -->

## PyCWinApp.AddDocTemplate

 AddDocTemplate(template)

Adds a template to the application list.

#### Parameters

- template : PyCDocTemplate

 The template to be added.


<!-- page: PyCWinApp__FindOpenDocument_meth.html -->

## PyCWinApp.FindOpenDocument

 PyCDocument = FindOpenDocument(fileName)

Returns an existing document with the specified file name.

#### Parameters

- fileName : string

 The fully qualified filename to search for.


<!-- page: PyCWinApp__GetDocTemplateList_meth.html -->

## PyCWinApp.GetDocTemplateList

 [PyCDocTemplate,...] = GetDocTemplateList()

Returns a list of all document templates.


<!-- page: PyCWinApp__InitDlgInstance_meth.html -->

## PyCWinApp.InitDlgInstance

 InitDlgInstance(dialog)

Calls critical InitInstance processing for a dialog based application.

#### Parameters

- dialog : PyCDialog

 The dialog object to be used as the main window for the application.


<!-- page: PyCWinApp__IsInproc_meth.html -->

## PyCWinApp.IsInproc

 int = IsInproc()

Returns a flag to indicate if the created CWinApp was in the DLL, or an external EXE.


<!-- page: PyCWinApp__LoadCursor_meth.html -->

## PyCWinApp.LoadCursor

 int = LoadCursor(cursorId)

Loads a cursor.

#### Parameters

- cursorId : PyResourceId

 The resource id or name of the cursor to load.


<!-- page: PyCWinApp__LoadIcon_meth.html -->

## PyCWinApp.LoadIcon

 int = LoadIcon(idResource)

Loads an icon resource.

#### Parameters

- idResource : int

 The ID of the icon to load.


<!-- page: PyCWinApp__LoadOEMCursor_meth.html -->

## PyCWinApp.LoadOEMCursor

 int = LoadOEMCursor(cursorId)

Loads an OEM cursor.

#### Parameters

- cursorId : int

 The ID of the cursor to load.


<!-- page: PyCWinApp__LoadStandardCursor_meth.html -->

## PyCWinApp.LoadStandardCursor

 int = LoadStandardCursor(cursorId)

Loads a standard cursor.

#### Parameters

- cursorId : PyResourceId

 The resource ID or name of the cursor to load.


<!-- page: PyCWinApp__LoadStandardIcon_meth.html -->

## PyCWinApp.LoadStandardIcon

 int = LoadStandardIcon(resourceName)

Loads an icon resource.

#### Parameters

- resourceName : PyResourceId

 The resource name or id of the standard icon to load.


<!-- page: PyCWinApp__OnFileNew_meth.html -->

## PyCWinApp.OnFileNew

 OnFileNew()

Calls the underlying OnFileNew MFC method.


<!-- page: PyCWinApp__OnFileOpen_meth.html -->

## PyCWinApp.OnFileOpen

 OnFileOpen()

Calls the underlying OnFileOpen MFC method.


<!-- page: PyCWinApp__OpenDocumentFile_meth.html -->

## PyCWinApp.OpenDocumentFile

 OpenDocumentFile(fileName)

Opens a document file by name.

#### Parameters

- fileName : string

 The name of the document to open.


<!-- page: PyCWinApp__RemoveDocTemplate_meth.html -->

## PyCWinApp.RemoveDocTemplate

 RemoveDocTemplate(template)

Removes a template to the application list.

#### Parameters

- template : PyCDocTemplate

 The template to be removed. Must have previously been added by PyCWinApp::AddDocTemplate.

#### Comments

 Note that MFC does not provide an equivalent function.


<!-- page: PyCWinApp__Run_meth.html -->

## PyCWinApp.Run

 int = Run()

Starts the message pump. Advanced users only


---

<!-- object: PyCWinThread -->


<!-- page: PyCWinThread.html -->

---

## PyCWinThread Object

 An application class. Encapsulates an MFC CWinThread class

#### Methods

- CreateThread

 Creates the actual thread behind the thread object.

- PumpIdle

 Pumps idle messages.

- PumpMessages

 Pumps all messages to the application until a WM_QUIT message is received.

- Run

 Starts the main application message pump.

- SetMainFrame

 Sets the C++ applications main frame

- SetThreadPriority

 Sets the threads priority


<!-- page: PyCWinThread__CreateThread_meth.html -->

## PyCWinThread.CreateThread

 CreateThread()

Creates the actual thread behind the thread object.


<!-- page: PyCWinThread__PumpIdle_meth.html -->

## PyCWinThread.PumpIdle

 PumpIdle()

Pumps all idle messages.


<!-- page: PyCWinThread__PumpMessages_meth.html -->

## PyCWinThread.PumpMessages

 PumpMessages()

Pumps all messages to the application until a WM_QUIT message is received.

#### Comments

 This allows an application which is performing a long operation to dispatch paint messages during the operation.


<!-- page: PyCWinThread__Run_meth.html -->

## PyCWinThread.Run

 int = Run()

Starts the message pump. Advanced users only


<!-- page: PyCWinThread__SetMainFrame_meth.html -->

## PyCWinThread.SetMainFrame

 SetMainFrame(mainFrame)

Sets the threads main frame

#### Parameters

- mainFrame : PyCWnd

 The applications main frame.

#### Comments

 You can pass None to this function to reset the main frame. Should I free this? I don't think so!


<!-- page: PyCWinThread__SetThreadPriority_meth.html -->

## PyCWinThread.SetThreadPriority

 SetThreadPriority(priority)

Sets the threads priority. Returns TRUE if successful.

#### Parameters

- priority : PyCWnd

 The threads priority.


---

<!-- object: PyCWnd -->


<!-- page: PyCWnd.html -->

---

## PyCWnd Object

 A base window class. Encapsulates an MFC CWnd class

#### Methods

- ActivateFrame

 Searches upwards for a parent window which has a frame, and activates it.

- BringWindowToTop

 Brings the window to the top of a stack of overlapping windows.

- BeginPaint

 Prepares the window for painting.

- CalcWindowRect

 Computes the size of the window rectangle based on the desired client rectangle size.

- CenterWindow

 Centers a window relative to its parent.

- CheckRadioButton

 Selects a specified radio button

- ChildWindowFromPoint

 Identifies the child window that contains the point

- ClientToScreen

 Convert coordinates from Client to Screen

- CreateWindow

 Create the underlying window object

- CreateWindowEx

 Creates the actual window for the PyCWnd object using extended attributes.

- DefWindowProc

 Calls the default message handler.

- DestroyWindow

 Destroys the window attached to the object.

- DlgDirList

 Fill a listbox control with a file specification.

- DlgDirListComboBox

 Fill a combobox control with a file specification.

- DlgDirSelect

 Retrieves the current selection from a list box.

- DlgDirSelectComboBox

 Retrieves the current selection from a combo box.

- DragAcceptFiles

 Indicate the window can accept files dragges from file manager.

- DrawMenuBar

 Redraw the windows menu bar.

- EnableWindow

 Enable or disable the window.

- EndModalLoop

 Ends a modal loop.

- EndPaint

 Ends painting in a window

- GetCheckedRadioButton

 Get the ID of the checked a radio button in a group.

- GetClientRect

 Gets the client rectangle for thewindow.

- GetDC

 Gets the window's current device context.

- GetDCEx

 Gets the window's current device context.

- GetDlgCtrlID

 Get the current window's control id.

- GetDlgItem

 Get a child control by Id

- GetDlgItemInt

 Returns the integer value of a child window or control with the specified ID.

- GetDlgItemText

 Returns the text of child window or control with the specified ID.

- GetLastActivePopup

 Identifies the most recently active pop-up window

- GetMenu

 Get the current menu for a window.

- GetParent

 Get the parent window.

- GetParentFrame

 Returns the window's frame.

- GetParent

 Returns the child window's parent window or owner window.

- GetSafeHwnd

 Returns the HWnd of this window.

- GetScrollInfo

 Retrieve information about a scroll bar

- GetScrollPos

 Retrieves the current position of the scroll box of a scroll bar.

- GetStyle

 Retrieves the window style

- GetExStyle

 Retrieves the window extended style

- GetSystemMenu

 Get the system menu for the window.

- GetTopLevelFrame

 Get the top-level frame window.

- GetTopLevelOwner

 Get the top-level owner window.

- GetTopLevelParent

 Get the top-level parent window.

- GetTopWindow

 Get the top level window attached to this window.

- GetWindow

 Get a specified window (eg, parent, child, etc).

- GetWindowDC

 Obtains the PyDC for a window.

- GetWindowPlacement

 Gets the window's current placement information.

- GetWindowRect

 Get the windows rectangle.

- GetWindowText

 Get the window's current text.

- HideCaret

 Hides the caret

- HookAllKeyStrokes

 Hook a handler for all keystroke messages.

- HookKeyStroke

 Hook a keystroke handler.

- HookMessage

 Hook a message notification handler.

- InvalidateRect

 Invalidate a specified rectangle in a window.

- InvalidateRgn

 Invalidate a specified region of a window.

- IsChild

 Indicates if a window is a child.

- IsDlgButtonChecked

 Indicates if a dialog botton is checked.

- IsIconic

 Indicates if the window is currently minimised.

- IsZoomed

 Indicates if the window is currently maximised.

- IsWindow

 determines whether the specified window handle identifies an existing window.

- IsWindowVisible

 Determines if the window is currently visible.

- IsWindowVisible

 Determines if the window is currently enabled.

- KillTimer

 Destroys a system timer

- LockWindowUpdate

 Disables drawing in the given window

- MapWindowPoints

 Converts (maps) a set of points from the coordinate space of the CWnd to the coordinate space of another window.

- MouseCaptured

 Indicates if the window currently has the mouse captured.

- MessageBox

 Displays a message box.

- ModifyStyle

 Modifies the style of a window.

- ModifyStyleEx

 Modifies the style of a window.

- MoveWindow

 Moves the window to a new location.

- OnClose

 Calls the default MFC OnClose handler.

- OnCtlColor

 Calls the default MFC OnCtlColor handler.

- OnEraseBkgnd

 Calls the default MFC OnEraseBkgnd handler.

- OnNcHitTest

 Calls the base MFC OnNcHitTest function.

- OnPaint

 Calls the default MFC OnPaint handler.

- OnQueryDragIcon

 Calls the default MFC OnQueryDragIcon handler.

- OnQueryNewPalette

 Calls the underlying MFC OnQueryNewPalette method.

- OnSetCursor

 Calls the default MFC OnSetCursor message

- OnMouseActivate

 Calls the default MFC OnMouseActicate message

- OnWndMsg

 Calls the default MFC Window Message handler.

- PreCreateWindow

 Calls the underlying MFC PreCreateWindow method.

- PumpWaitingMessages

 Calls the Peek/Dispatch loop on the wnd.

- RedrawWindow

 Updates the specified rectangle or region in the given window's client area.

- ReleaseCapture

 Releases the mouse capture for the window.

- ReleaseDC

 Releases a device context, freeing it for use by other applications.

- RepositionBars

 Repositions the control bars for the window.

- RunModalLoop

 Starts a modal loop for the window.

- PostMessage

 Post a message to the window.

- SendMessageToDescendants

 Send a message to a window's children.

- SendMessage

 Send a message to the window.

- SetActiveWindow

 Sets the window active.

- SetForegroundWindow

 Puts the window into the foreground and activates the window.

- SetWindowPos

 Sets the windows position information.

- ScreenToClient

 Converts from screen coordinates to client coordinates.

- SetCapture

 Captures the mouse input for thw window.

- SetDlgItemText

 Sets the text for the child window or control with the specified ID.

- SetFocus

 Sets focus to the window.

- SetFont

 Sets the window's current font to the specified font.

- SetIcon

 Sets the handle to a specific icon.

- SetMenu

 Sets the menu for a window.

- SetRedraw

 Sets the redraw flag for the window.

- SetScrollPos

 Sets the current position of the scroll box of a scroll bar.

- SetScrollInfo

 Set information about a scroll bar

- SetTimer

 Installs a system timer

- SetWindowPlacement

 Sets the window's placement options.

- SetWindowText

 Sets the window's text.

- ShowCaret

 Shows the caret

- ShowScrollBar

 Shows/Hides the window's scroll bars.

- ShowWindow

 Shows the window.

- UnLockWindowUpdate

 Unlocks a window that was locked with LockWindowUpdate

- UpdateData

 Updates a windows dialog data.

- UpdateDialogControls

 Updates the state of dialog buttons and other controls in a dialog box or window that uses the PyCCmdUI::HookCommandUpdate callback mechanism.

- UpdateWindow

 Updates a window.

#### Based On

PyCCmdTarget


<!-- page: PyCWnd__ActivateFrame_meth.html -->

## PyCWnd.ActivateFrame

 ActivateFrame(cmdShow)

Searches upwards for a parent window which has a frame, and activates it.

#### Parameters

- cmdShow=SW_SHOW : int

 The param passed to CFrameWnd::ShowWindow . See also PyCWnd::ShowWindow.

#### MFC References

- CFrameWnd::ActivateFrame


<!-- page: PyCWnd__BeginPaint_meth.html -->

## PyCWnd.BeginPaint

 PyCDC, PAINTSTRUCT = BeginPaint()

Prepares a window for painting

#### Return Value

You must pass the PAINTSTRUCT param to the PyCWnd::EndPaint method.


<!-- page: PyCWnd__BringWindowToTop_meth.html -->

## PyCWnd.BringWindowToTop

 BringWindowToTop()

Brings the window to the top of a stack of overlapping windows.

#### Comments

 This method activates pop-up, top-level, and MDI child windows. The BringWindowToTop member function should be used to uncover any window that is partially or completely obscured by any overlapping windows.
 Calling this method is similar to calling the PyCWnd::SetWindowPos method to change a window's position in the Z order. The BringWindowToTop method does not change the window style to make it a top-level window of the desktop.

#### MFC References

- CWnd::BringWindowToTop


<!-- page: PyCWnd__CalcWindowRect_meth.html -->

## PyCWnd.CalcWindowRect

 (left, top, right, bottom) = CalcWindowRect(rect, nAdjustType )

Computes the size of the window rectangle based on the desired client rectangle size. The resulting size can then be used as the initial size for the window object.

#### Parameters

- rect : (left, top, right, bottom)

 The size to calculate from

- nAdjustType=adjustBorder : int

 An enumerated type used for in-place editing. It can have the following values: CWnd::adjustBorder = 0, which means that scrollbar sizes are ignored in calculation; and CWnd::adjustOutside = 1, which means that they are added into the final measurements of the rectangle.

#### MFC References

- CWnd::CalcWindowRect


<!-- page: PyCWnd__CenterWindow_meth.html -->

## PyCWnd.CenterWindow

 CenterWindow(altwin)

Centers a window relative to its parent.

#### Parameters

- altwin=None : PyCWnd

 alternate window relative to which it will be centered (other than the parent window).

#### MFC References

- CWnd::CenterWindow


<!-- page: PyCWnd__CheckRadioButton_meth.html -->

## PyCWnd.CheckRadioButton

 CheckRadioButton(idFirst, idLast, idCheck)

Selects the specified radio button, and clears all others in the group.

#### Parameters

- idFirst : int

 The identifier of the first radio button in the group.

- idLast : int

 The identifier of the last radio button in the group.

- idCheck : int

 The identifier of the radio button to be checked.

#### MFC References

- CWnd::CheckRadioButton


<!-- page: PyCWnd__ChildWindowFromPoint_meth.html -->

## PyCWnd.ChildWindowFromPoint

 PyCWnd = ChildWindowFromPoint(x, y , flag )

Returns the child window that contains the point

#### Parameters

- x : int

 x coordinate of point

- y : int

 y coordinate of point

- flag=0 : int

 Specifies which child windows to skip

#### MFC References

- CWnd::ChildWindowFromPoint


<!-- page: PyCWnd__ClientToScreen_meth.html -->

## PyCWnd.ClientToScreen

 (x,y) or (l, t, r, b) = ClientToScreen(point)

Converts the client coordinates of a given point on the display to screen coordinates.

#### Parameters

- point : (x,y)

 The client coordinates.

#### Alternative Parameters

- rect

 The client coordinates.

#### Comments

 The new screen coordinates are relative to the upper-left corner of the system display. This function assumes that the given pointis in client coordinates.

#### MFC References

- CWnd::ClientToScreen


<!-- page: PyCWnd__CreateWindowEx_meth.html -->

## PyCWnd.CreateWindowEx

 CreateWindowEx(styleEx, classId, windowName, style, rect, parent, id, createStruct, createStruct)

Creates the actual window using extended capabilities.

#### Parameters

- styleEx : int

 The extended style of the window being created.

- classId : string

 The class ID for the window. May not be None.

- windowName : string

 The title for the window, or None

- style : int

 The style for the window.

- rect : (left, top, right, bottom)

 The size and position of the window.

- parent : PyCWnd

 The parent window of the new window..

- id : int

 The control's ID.

- createStruct=None : CREATESTRUCT

 A CreateStruct object (ie, a tuple)

- createStruct : tuple

 A tuple representing a CREATESTRUCT structure.

#### MFC References

- CWnd::CreateEx


<!-- page: PyCWnd__CreateWindow_meth.html -->

## PyCWnd.CreateWindow

 CreateWindow(classId, windowName, style, rect, parent, id, context)

Creates the actual window

#### Parameters

- classId : string

 The class ID for the window, or None

- windowName : string

 The title for the window, or None

- style : int

 The style for the window.

- rect : (left, top, right, bottom)

 The size and position of the window.

- parent : PyCWnd

 The parent window of the new window..

- id : int

 The control's ID.

- context=None : object

 A CreateContext object.

#### MFC References

- CWnd::Create


<!-- page: PyCWnd__DefWindowProc_meth.html -->

## PyCWnd.DefWindowProc

 int = DefWindowProc(message, idLast , idCheck )

Calls the default message handler.

#### Parameters

- message : int

 The Windows message.

- idLast : int

 The lParam for the message.

- idCheck : int

 The wParam for the message.

#### MFC References

- CWnd::DefWindowProc


<!-- page: PyCWnd__DestroyWindow_meth.html -->

## PyCWnd.DestroyWindow

 DestroyWindow()

Destroy the window attached to the object.

#### Comments

 The DestroyWindow member function sends appropriate messages to the window to deactivate it and remove the input focus. It also destroys the window's menu, flushes the application queue, destroys outstanding timers, removes Clipboard ownership, and breaks the Clipboard-viewer chain if CWnd is at the top of the viewer chain. It sends WM_DESTROY and WM_NCDESTROY messages to the window.


<!-- page: PyCWnd__DlgDirListComboBox_meth.html -->

## PyCWnd.DlgDirListComboBox

 DlgDirListComboBox()

Fill a combo with a file or directory listing. See PyCWnd::DlgDirList for details.

#### MFC References

- CWnd::DlgDirListComboBox


<!-- page: PyCWnd__DlgDirList_meth.html -->

## PyCWnd.DlgDirList

 DlgDirList(defPath, idListbox, idStaticPath, fileType)

Fill a list box with a file or directory listing.

#### Parameters

- defPath : string

 The file spec to fill the list box with

- idListbox : int

 The Id of the listbox control to fill.

- idStaticPath : int

 The Id of the static control used to display the current drive and directory. If idStaticPath is 0, it is assumed that no such control exists.

- fileType : int

 Specifies the attributes of the files to be displayed. It can be any combination of DDL_READWRITE, DDL_READONLY, DDL_HIDDEN, DDL_SYSTEM, DDL_DIRECTORY, DDL_ARCHIVE, DDL_POSTMSGS, DDL_DRIVES or DDL_EXCLUSIVE

#### MFC References

- CWnd::DlgDirList


<!-- page: PyCWnd__DlgDirSelectComboBox_meth.html -->

## PyCWnd.DlgDirSelectComboBox

 string = DlgDirSelectComboBox(idListbox)

Retrieves the current selection from the list box of a combo box. It assumes that the list box has been filled by the PyCWnd::DlgDirListComboBox member function and that the selection is a drive letter, a file, or a directory name.

#### Parameters

- idListbox : int

 The Id of the combobox.

#### MFC References

- CWnd::DlgDirSelectComboBox


<!-- page: PyCWnd__DlgDirSelect_meth.html -->

## PyCWnd.DlgDirSelect

 string = DlgDirSelect(idListbox)

Retrieves the current selection from a list box. It assumes that the list box has been filled by the PyCWnd::DlgDirList member function and that the selection is a drive letter, a file, or a directory name.

#### Parameters

- idListbox : int

 The Id of the listbox.

#### MFC References

- CWnd::DlgDirSelect


<!-- page: PyCWnd__DragAcceptFiles_meth.html -->

## PyCWnd.DragAcceptFiles

 DragAcceptFiles(bAccept)

Indicates that the window and children supports files dropped from file manager

#### Parameters

- bAccept=1 : int

 A flag indicating if files are accepted.

#### MFC References

- CWnd::DragAcceptFiles


<!-- page: PyCWnd__DrawMenuBar_meth.html -->

## PyCWnd.DrawMenuBar

 DrawMenuBar()

Redraws the menu bar. Can be called if the menu changes.


<!-- page: PyCWnd__EnableWindow_meth.html -->

## PyCWnd.EnableWindow

 int = EnableWindow(bEnable)

Enables or disables the window. Typically used for dialog controls.

#### Parameters

- bEnable=1 : int

 A flag indicating if the window is to be enabled or disabled.

#### MFC References

- CWnd::EnableWindow

#### Return Value

Returns the state before the EnableWindow member function was called


<!-- page: PyCWnd__EndModalLoop_meth.html -->

## PyCWnd.EndModalLoop

 EndModalLoop(result)

Ends a modal loop.

#### Parameters

- result : int

 The result as returned to RunModalLoop


<!-- page: PyCWnd__EndPaint_meth.html -->

## PyCWnd.EndPaint

 EndPaint(paintStruct)

Ends painting

#### Parameters

- paintStruct : PAINTSTRUCT

 The object returned from PyCWnd::BeginPaint


<!-- page: PyCWnd__GetCheckedRadioButton_meth.html -->

## PyCWnd.GetCheckedRadioButton

 int = GetCheckedRadioButton(idFirst, idLast )

Returns the ID of the checked radio button, or 0 if none is selected.

#### Parameters

- idFirst : int

 The Id of the first radio button in the group.

- idLast : int

 The Id of the last radio button in the group.

#### MFC References

- CWnd::GetCheckedRadioButton


<!-- page: PyCWnd__GetClientRect_meth.html -->

## PyCWnd.GetClientRect

 (left, top, right, bottom) = GetClientRect()

Returns the client coordinates of the window. left and top will be zero.


<!-- page: PyCWnd__GetDCEx_meth.html -->

## PyCWnd.GetDCEx

 PyCDC = GetDCEx()

Gets the windows current DC object with extended caps.


<!-- page: PyCWnd__GetDC_meth.html -->

## PyCWnd.GetDC

 PyCDC = GetDC()

Gets the windows current DC object.

#### Return Value

The result is a PyCDC, or a win32ui.error exception is raised.


<!-- page: PyCWnd__GetDlgCtrlID_meth.html -->

## PyCWnd.GetDlgCtrlID

 int = GetDlgCtrlID()

Returns the ID of this child window.

#### MFC References

- CWnd::GetDlgCtrlId


<!-- page: PyCWnd__GetDlgItemInt_meth.html -->

## PyCWnd.GetDlgItemInt

 int = GetDlgItemInt(idControl, bUnsigned )

Returns the integer value of a child window or control with the specified ID.

#### Parameters

- idControl : int

 The Id of the control to be retrieved.

- bUnsigned=1 : int

 Should the function check for a minus sign

#### MFC References

- CWnd::GetDlgItemInt

#### Return Value

If the value can not be converted, a ValueError is raised.


<!-- page: PyCWnd__GetDlgItemText_meth.html -->

## PyCWnd.GetDlgItemText

 string = GetDlgItemText(idControl)

Returns the text of child window or control with the specified ID.

#### Parameters

- idControl : int

 The Id of the control to be retrieved.

#### MFC References

- CWnd::GetDlgItemText


<!-- page: PyCWnd__GetDlgItem_meth.html -->

## PyCWnd.GetDlgItem

 PyCWnd = GetDlgItem(idControl)

Returns a window object for the child window or control with the specified ID. The type of the return object will be as specific as possible, but will always be derived from an PyCWnd object.

#### Parameters

- idControl : int

 The Id of the control to be retrieved.

#### MFC References

- CWnd::GetDlgItem

#### Return Value

The result is a PyCWnd (or derived) object, or a win32ui.error exception is raised.


<!-- page: PyCWnd__GetExStyle_meth.html -->

## PyCWnd.GetExStyle

 int = GetExStyle()

Retrieves the window's extended style


<!-- page: PyCWnd__GetLastActivePopup_meth.html -->

## PyCWnd.GetLastActivePopup

 PyCWnd = GetLastActivePopup()

Returns the last active popup Window, or the Window itself.

#### MFC References

- CWnd::GetLastActivePopup

#### Return Value

The result is a PyCWnd object, or None if no Window can be found.


<!-- page: PyCWnd__GetMenu_meth.html -->

## PyCWnd.GetMenu

 PyCMenu = GetMenu()

Returns the menu object for the window's menu.

#### MFC References

- CWnd::GetMenu

#### Return Value

The result is a PyMenu object, or an exception is thrown.


<!-- page: PyCWnd__GetParentFrame_meth.html -->

## PyCWnd.GetParentFrame

 PyCWnd = GetParentFrame()

Returns the window's frame.

#### MFC References

- CWnd::GetParentFrame

#### Return Value

The result is a PyCWnd object, or None if no Window can be found.


<!-- page: PyCWnd__GetParentOwner_meth.html -->

## PyCWnd.GetParentOwner

 PyCWnd = GetParentOwner()

Returns the child window's parent window or owner window.

#### MFC References

- CWnd::GetParentOwner

#### Return Value

The result is a PyCWnd object, or None if no Window can be found.


<!-- page: PyCWnd__GetParent_meth.html -->

## PyCWnd.GetParent

 PyCWnd = GetParent()

Returns the window's parent.

#### MFC References

- CWnd::GetParent

#### Return Value

The result is a PyCWnd object, or None if no Window can be found.


<!-- page: PyCWnd__GetSafeHwnd_meth.html -->

## PyCWnd.GetSafeHwnd

 int = GetSafeHwnd()

Returns the HWnd of this window.

#### MFC References

- CWnd::GetSafeHwnd


<!-- page: PyCWnd__GetScrollInfo_meth.html -->

## PyCWnd.GetScrollInfo

 SCROLLINFO tuple = GetScrollInfo(nBar, mask )

Returns information about a scroll bar

#### Parameters

- nBar : int

 The scroll bar to examine. Can be one of win32con.SB_BOTH, win32con.SB_VERT or win32con.SB_HORZ

- mask=SIF_ALL : int

 The mask for attributes to retrieve.


<!-- page: PyCWnd__GetScrollPos_meth.html -->

## PyCWnd.GetScrollPos

 int = GetScrollPos(nBar)

Retrieves the current position of the scroll box of a scroll bar.

#### Parameters

- nBar : int

 The scroll bar to examine. Can be one of win32con.SB_VERT or win32con.SB_HORZ


<!-- page: PyCWnd__GetStyle_meth.html -->

## PyCWnd.GetStyle

 int = GetStyle()

Retrieves the window style


<!-- page: PyCWnd__GetSystemMenu_meth.html -->

## PyCWnd.GetSystemMenu

 PyCMenu = GetSystemMenu()

Returns the menu object for the window's system menu.

#### MFC References

- CWnd::GetSystemMenu


<!-- page: PyCWnd__GetTopLevelFrame_meth.html -->

## PyCWnd.GetTopLevelFrame

 PyCWnd = GetTopLevelFrame()

Returns the top-level frame of the window.

#### MFC References

- CWnd::GetTopLevelFrame

#### Return Value

The result is a PyCWnd object, or None if no Window can be found.


<!-- page: PyCWnd__GetTopLevelOwner_meth.html -->

## PyCWnd.GetTopLevelOwner

 PyCWnd = GetTopLevelOwner()

Returns the top-level owner of the window.

#### MFC References

- CWnd::GetTopLevelOwner

#### Return Value

The result is a PyCWnd object, or None if no Window can be found.


<!-- page: PyCWnd__GetTopLevelParent_meth.html -->

## PyCWnd.GetTopLevelParent

 PyCWnd = GetTopLevelParent()

Returns the top-level parent of the window.

#### MFC References

- CWnd::GetTopLevelParent

#### Return Value

The result is a PyCWnd object, or None if no Window can be found.


<!-- page: PyCWnd__GetTopWindow_meth.html -->

## PyCWnd.GetTopWindow

 PyCWnd = GetTopWindow()

Identifies the top-level child window in a linked list of child windows.

#### Comments

 Searches for the top-level child window that belongs to this window. If this window has no children, this function returns None

#### MFC References

- CWnd::GetTopWindow

#### Return Value

If no child windows exist, the value is None.


<!-- page: PyCWnd__GetWindowDC_meth.html -->

## PyCWnd.GetWindowDC

 PyCDC = GetWindowDC()

Gets the windows current DC object.


<!-- page: PyCWnd__GetWindowPlacement_meth.html -->

## PyCWnd.GetWindowPlacement

 tuple = GetWindowPlacement()

Returns placement information about the current window.

#### MFC References

- CWnd::GetWindowPlacement

#### Return Value

The result is a tuple of (flags, showCmd, (minposX, minposY), (maxposX, maxposY), (normalposX, normalposY))

| | Item | Description
| |

---

 |

---

| | flags | One of the WPF_* constants
| | showCmd | Current state - one of the SW_* constants.
| | minpos | Specifies the coordinates of the window's upper-left corner when the window is minimized.
| | maxpos | Specifies the coordinates of the window's upper-left corner when the window is maximized.
| | normalpos | Specifies the window's coordinates when the window is in the restored position.


<!-- page: PyCWnd__GetWindowRect_meth.html -->

## PyCWnd.GetWindowRect

 (left, top, right, bottom) = GetWindowRect()

Returns the screen coordinates of the windows upper left corner

#### MFC References

- CWnd::GetWindowRect


<!-- page: PyCWnd__GetWindowText_meth.html -->

## PyCWnd.GetWindowText

 string = GetWindowText()

Returns the windows text.

#### MFC References

- CWnd::Py_BuildValue


<!-- page: PyCWnd__GetWindow_meth.html -->

## PyCWnd.GetWindow

 PyCWnd = GetWindow(type)

Returns a window, with the specified relationship to this window.

#### Parameters

- type : int

 Specifies the relationship between the current and the returned window. It can take one of the following values: GW_CHILD, GW_HWNDFIRST, GW_HWNDLAST, GW_HWNDNEXT, GW_HWNDPREV or GW_OWNER

#### MFC References

- CWnd::GetWindow

#### Return Value

The result is a PyCWnd or None if no Window can be found.


<!-- page: PyCWnd__HideCaret_meth.html -->

## PyCWnd.HideCaret

 HideCaret()

Hides the caret

#### Comments

 See also PyCWnd::ShowCaret


<!-- page: PyCWnd__HookAllKeyStrokes_meth.html -->

## PyCWnd.HookAllKeyStrokes

 HookAllKeyStrokes(obHandler)

Hook a key stroke handler for all key strokes.

#### Parameters

- obHandler : object

 The handler for the keystrokes. This must be a callable object.

#### Comments

 The handler object passed will be called as the application receives WM_CHAR messages. The handler will be called with 2 arguments
 The handler object (as per all hook functions).
 The keystroke being handled.
 If the handler returns TRUE, then the keystroke will be passed on to the default handler, otherwise it will be consumed.
 Note: This handler will prevent any PyCWnd::HookKeyStroke hooks from being called.


<!-- page: PyCWnd__HookKeyStroke_meth.html -->

## PyCWnd.HookKeyStroke

 object = HookKeyStroke(obHandler, ch )

Hook a key stroke handler

#### Parameters

- obHandler : object

 The handler of the keystroke. This must be a callable object.

- ch : int

 The ID for the keystroke to be handled. This may be an ascii code, or a virtual key code.

#### Comments

 The handler object passed will be called as the application receives WM_CHAR message for the specified character code. The handler will be called with 2 arguments
 The handler object (as per all hook functions)
 The keystroke being handled.
 If the handler returns TRUE, then the keystroke will be passed on to the default handler, otherwise the keystroke will be consumed.
 Note: This handler will not be called if a PyCWnd::HookAllKeyStrokes hook is in place.

#### Return Value

The return value is the previous handler, or None.


<!-- page: PyCWnd__HookMessage_meth.html -->

## PyCWnd.HookMessage

 object = HookMessage(obHandler, message )

Hook a message notification handler

#### Parameters

- obHandler : object

 The handler for the message notification. This must be a callable object.

- message : int

 The ID of the message to be handled.

#### Comments

 The handler object passed will be called as the application receives messages with the specified ID. Note that it is not possible for PythonWin to consume a message - it is always passed on to the default handler. The handler will be called with 2 arguments
 The handler object (as per all hook functions).
 A tuple representing the message.
 The message tuple is in the following format:

#### Items

- [0] int : hwnd

 The hwnd of the window.

- [1] int : message

 The message.

- [2] int : wParam

 The wParam sent with the message.

- [3] int : lParam

 The lParam sent with the message.

- [4] int : time

 The time the message was posted.

- [5] int, int : point

 The point where the mouse was when the message was posted.

#### Return Value

The return value is the previous handler, or None.


<!-- page: PyCWnd__InvalidateRect_meth.html -->

## PyCWnd.InvalidateRect

 InvalidateRect(rect, bErase)

Invalidates an area of a window.

#### Parameters

- rect=(0,0,0,0) : (left, top, right, bottom)

 Rectangle to be updated. If default param is used, the entire window is invalidated.

- bErase=1 : int

 Specifies whether the background within the update region is to be erased.

#### MFC References

- CWnd::InvalidateRect


<!-- page: PyCWnd__InvalidateRgn_meth.html -->

## PyCWnd.InvalidateRgn

 InvalidateRgn(region, bErase)

Invalidates a region of the window

#### Parameters

- region : PyCRgn

 The region to erase.

- bErase=1 : int

 Indicates if the region should be erased.


<!-- page: PyCWnd__IsChild_meth.html -->

## PyCWnd.IsChild

 int = IsChild(obWnd)

Determines if a given window is a child of this window.

#### Parameters

- obWnd : PyCWnd

 The window to be checked

#### MFC References

- CWnd::IsChild


<!-- page: PyCWnd__IsDlgButtonChecked_meth.html -->

## PyCWnd.IsDlgButtonChecked

 int = IsDlgButtonChecked(idCtl)

Determines if a dialog button is checked.

#### Parameters

- idCtl : int

 The ID of the button to check.

#### MFC References

- CWnd::IsDlgButtonChecked


<!-- page: PyCWnd__IsIconic_meth.html -->

## PyCWnd.IsIconic

 int = IsIconic()

Determines if the window is currently displayed as an icon.


<!-- page: PyCWnd__IsWindowEnabled_meth.html -->

## PyCWnd.IsWindowEnabled

 int = IsWindowEnabled()

Determines if the window is currently enabled.


<!-- page: PyCWnd__IsWindowVisible_meth.html -->

## PyCWnd.IsWindowVisible

 int = IsWindowVisible()

Determines if the window is currently visible.


<!-- page: PyCWnd__IsWindow_meth.html -->

## PyCWnd.IsWindow

 int = IsWindow()

determines whether the specified window handle identifies an existing window


<!-- page: PyCWnd__IsZoomed_meth.html -->

## PyCWnd.IsZoomed

 int = IsZoomed()

Determines if the window is currently maximised.


<!-- page: PyCWnd__KillTimer_meth.html -->

## PyCWnd.KillTimer

 int = KillTimer()

Kills a system timer

#### MFC References

- CWnd::KillTimer


<!-- page: PyCWnd__LockWindowUpdate_meth.html -->

## PyCWnd.LockWindowUpdate

 LockWindowUpdate()

Disables drawing in the given window

#### MFC References

- CWnd::LockWindowUpdate


<!-- page: PyCWnd__MapWindowPoints_meth.html -->

## PyCWnd.MapWindowPoints

 MapWindowPoints(wnd, points)

Converts (maps) a set of points from the coordinate space of a window to the coordinate space of another window.

#### Parameters

- wnd : PyCWnd

- points : [ (x,y), ...]

 The points to map

#### Return Value

A list of the mapped points from the coordinate space of the CWnd to the coordinate space of another window.


<!-- page: PyCWnd__MessageBox_meth.html -->

## PyCWnd.MessageBox

 MessageBox(message, title, style)

Display a message box.

#### Parameters

- message : string

 The message to be displayed in the message box.

- title=None : string/None

 The title for the message box. If None, the applications title will be used.

- style=win32con.MB_OK : int

 The style of the message box.

#### MFC References

- CWnd::MessageBox

#### Return Value

An integer identifying the button pressed to dismiss the dialog.


<!-- page: PyCWnd__ModifyStyleEx_meth.html -->

## PyCWnd.ModifyStyleEx

 int = ModifyStyleEx(remove, add , flags )

Modifies the extended style of a window.

#### Parameters

- remove : int

 Specifies extended window styles to be removed during style modification.

- add : int

 Specifies extended extended window styles to be added during style modification.

- flags=0 : int

 Flags to be passed to SetWindowPos, or zero if SetWindowPos should not be called. The default is zero.

#### Comments

 If nFlags is nonzero, ModifyStyleEx calls the Windows API function ::SetWindowPos and redraws the window by combining nFlags with the following four preset flags:
* SWP_NOSIZE Retains the current size.
* SWP_NOMOVE Retains the current position.
* SWP_NOZORDER Retains the current Z order.
* SWP_NOACTIVATE Does not activate the window.
See also PyCWnd::ModifyStyle

#### MFC References

- CWnd::ModifyStyleEx

#### Return Value

The result is true if the style was changed, or false if the style is already the same as requested and no change was made.


<!-- page: PyCWnd__ModifyStyle_meth.html -->

## PyCWnd.ModifyStyle

 int = ModifyStyle(remove, add , flags )

Modifies the style of a window.

#### Parameters

- remove : int

 Specifies window styles to be removed during style modification.

- add : int

 Specifies window styles to be added during style modification.

- flags=0 : int

 Flags to be passed to SetWindowPos, or zero if SetWindowPos should not be called. The default is zero.

#### Comments

 If nFlags is nonzero, ModifyStyle calls the Windows API function ::SetWindowPos and redraws the window by combining nFlags with the following four preset flags:
* SWP_NOSIZE Retains the current size.
* SWP_NOMOVE Retains the current position.
* SWP_NOZORDER Retains the current Z order.
* SWP_NOACTIVATE Does not activate the window.
See also PyCWnd::ModifyStyleEx

#### MFC References

- CWnd::ModifyStyle

#### Return Value

The result is true if the style was changed, or false if the style is already the same as requested and no change was made.


<!-- page: PyCWnd__MouseCaptured_meth.html -->

## PyCWnd.MouseCaptured

 int = MouseCaptured()

Returns 1 if the window has the mouse capture, else 0


<!-- page: PyCWnd__MoveWindow_meth.html -->

## PyCWnd.MoveWindow

 MoveWindow(rect, bRepaint)

Move a window to a new location.

#### Parameters

- rect : (left, top, right, bottom)

 The new location of the window, relative to the parent.

- bRepaint=1 : int

 Indicates if the window should be repainted after the move.

#### MFC References

- CWnd::MoveWindow


<!-- page: PyCWnd__OnClose_meth.html -->

## PyCWnd.OnClose

 int = OnClose()

Calls the default MFC OnClose handler.

#### See Also

- PyCWnd.OnClose virtual method

#### MFC References

- CWnd::OnClose


<!-- page: PyCWnd__OnClose_virtual.html -->

## PyCWnd.OnClose Virtual

 OnClose()

Called for the WM_CLOSE message.

#### Comments

 The default calls DestroyWindow(). If you supply a handler, the default is not called.

 The MFC base class is always called before the Python method.

#### See Also

- PyCWnd::OnClose


<!-- page: PyCWnd__OnCommand_virtual.html -->

## PyCWnd.OnCommand Virtual

 OnCommand(wparam, lparam )

Allows a Window to override the OnCommand handling.

#### Parameters

- wparam : int

- lparam : int

#### Comments

 The base class method must be called manually via PyCWnd::OnCommand . Failure to call the base implementation will prevent all Python command handlers (hooked via PyCWnd::HookCommand ).


<!-- page: PyCWnd__OnCreate_virtual.html -->

## PyCWnd.OnCreate Virtual

 OnCreate()

Called for the WM_CREATE message.

#### Comments

 The MFC implementation is always called before Python.

#### Return Value

The result is an integer indicating if the window should be created.


<!-- page: PyCWnd__OnCtlColor_meth.html -->

## PyCWnd.OnCtlColor

 int = OnCtlColor(dc, control , type )

Calls the default MFC OnCtlColor handler.

#### Parameters

- dc : PyCDC

 The dc

- control : PyCWin

 The control that want's it's color changed

- type : int

 Type of control

#### See Also

- PyCWnd.OnCtlColor virtual method

#### MFC References

- CWnd::OnCtlColor


<!-- page: PyCWnd__OnCtlColor_virtual.html -->

## PyCWnd.OnCtlColor Virtual

 OnCtlColor()

Called for the WM_CTLCOLOR message.

#### Comments

 Setup dc to paint the control pWnd of type nCtlColor.

 The default calls OnCtlColor(). If you supply a handler, the default is not called.

#### See Also

- PyCWnd::OnCtlColor

#### Return Value

Handle of the brush to paint the control's background.


<!-- page: PyCWnd__OnEraseBkgnd_meth.html -->

## PyCWnd.OnEraseBkgnd

 int = OnEraseBkgnd(dc)

Calls the default MFC OnEraseBkgnd handler.

#### Parameters

- dc : PyCDC

 The dc

#### See Also

- PyCWnd.OnEraseBkgnd virtual method

#### MFC References

- CWnd::OnEraseBkgnd


<!-- page: PyCWnd__OnEraseBkgnd_virtual.html -->

## PyCWnd.OnEraseBkgnd Virtual

 OnEraseBkgnd(dc)

Called for the WN_ERASEBACKGROUND message.

#### Parameters

- dc : PyCDC

 The device context.

#### See Also

- PyCWnd::OnEraseBkgnd

#### Return Value

Nonzero if it erases the background; otherwise 0.


<!-- page: PyCWnd__OnMDIActivate_virtual.html -->

## PyCWnd.OnMDIActivate Virtual

 OnMDIActivate(bActivate, wndActivate , wndDeactivate )

#### Parameters

- bActivate : int

- wndActivate : PyCWnd

- wndDeactivate : PyCWnd

#### Comments

 The MFC implementation is always called before this.


<!-- page: PyCWnd__OnMouseActivate_meth.html -->

## PyCWnd.OnMouseActivate

 int = OnMouseActivate(wnd, hittest , message )

Calls the base MFC OnMouseActivate function.

#### Parameters

- wnd : PyCWnd

- hittest : int

- message : int

#### See Also

- PyCWnd.OnMouseActivate virtual method


<!-- page: PyCWnd__OnMouseActivate_virtual.html -->

## PyCWnd.OnMouseActivate Virtual

 OnMouseActivate(wndDesktop, hitTest , msg )

Called when the mouse is used to activate a window.

#### Parameters

- wndDesktop : PyCWnd

- hitTest : int

- msg : int

#### See Also

- PyCWnd::OnMouseActivate


<!-- page: PyCWnd__OnNcCalcSize_virtual.html -->

## PyCWnd.OnNcCalcSize Virtual

 OnNcCalcSize()

Called for the WM_NCCALCSIZE message.


<!-- page: PyCWnd__OnNcHitTest_meth.html -->

## PyCWnd.OnNcHitTest

 int = OnNcHitTest(x, y)

Calls the base MFC OnNcHitTest function.

#### Parameters

- x, y : int, int

 The point

#### See Also

- PyCWnd.OnNcHitTest virtual method


<!-- page: PyCWnd__OnNcHitTest_virtual.html -->

## PyCWnd.OnNcHitTest Virtual

 OnNcHitTest(x,y)

Called for the WM_NCHITTEST message.

#### Parameters

- x,y : int, int

 The point to test.

#### See Also

- PyCWnd::OnNcHitTest


<!-- page: PyCWnd__OnPaint_meth.html -->

## PyCWnd.OnPaint

 int = OnPaint()

Calls the default MFC OnPaint handler.

#### See Also

- PyCWnd.OnPaint virtual method

#### MFC References

- CWnd::OnEraseBkgnd


<!-- page: PyCWnd__OnPaint_virtual.html -->

## PyCWnd.OnPaint Virtual

 OnPaint()

Default message handler.

#### See Also

- Wnd::OnPaint


<!-- page: PyCWnd__OnPaletteChanged_virtual.html -->

## PyCWnd.OnPaletteChanged Virtual

 OnPaletteChanged(focusWnd)

Called to allow windows that use a color palette to realize their logical palettes and update their client areas.

#### Parameters

- focusWnd : PyCWnd

 The window that caused the system palette to change.


<!-- page: PyCWnd__OnPaletteIsChanging_virtual.html -->

## PyCWnd.OnPaletteIsChanging Virtual

 OnPaletteIsChanging(realizeWnd)

Informs other applications when an application is going to realize its logical palette.

#### Parameters

- realizeWnd : PyCWnd

 Specifies the window that is about to realize its logical palette.

#### Comments

 The MFC base class is always called before the Python method.


<!-- page: PyCWnd__OnQueryDragIcon_meth.html -->

## PyCWnd.OnQueryDragIcon

 int = OnQueryDragIcon()

Calls the default MFC OnQueryDragIcon handler.

#### See Also

- PyCWnd.OnQueryDragIcon virtual method


<!-- page: PyCWnd__OnQueryDragIcon_virtual.html -->

## PyCWnd.OnQueryDragIcon Virtual

 OnQueryDragIcon()

Called for the WM_QUERYDRAGICON message.

#### See Also

- PyCWnd::OnQueryDragIcon

#### Return Value

The result is an integer containing a HCURSOR for the icon.


<!-- page: PyCWnd__OnQueryNewPalette_meth.html -->

## PyCWnd.OnQueryNewPalette

 int = OnQueryNewPalette()

Calls the underlying MFC OnQueryNewPalette method.

#### See Also

- PyCWnd.OnQueryNewPalette virtual method


<!-- page: PyCWnd__OnQueryNewPalette_virtual.html -->

## PyCWnd.OnQueryNewPalette Virtual

 OnQueryNewPalette()

Informs the window it is about to receive input focus, and shoudl realize its logical palette.

#### Comments

 The base class method must be called manually via PyCScrollView::OnQueryNewPalette

#### See Also

- PyCWnd::OnQueryNewPalette


<!-- page: PyCWnd__OnSetCursor_meth.html -->

## PyCWnd.OnSetCursor

 int = OnSetCursor(wnd, hittest , message )

Calls the base MFC OnSetCursor function.

#### Parameters

- wnd : PyCWnd

- hittest : int

- message : int

#### See Also

- PyCWnd.OnSetCursor virtual method


<!-- page: PyCWnd__OnSetCursor_virtual.html -->

## PyCWnd.OnSetCursor Virtual

 OnSetCursor(wnd, hitTest , msg )

Called for the WM_SETCURSOR message.

#### Parameters

- wnd : PyCWnd

- hitTest : int

- msg : int

#### See Also

- PyCWnd::OnSetCursor


<!-- page: PyCWnd__OnSysColorChange_virtual.html -->

## PyCWnd.OnSysColorChange Virtual

 OnSysColorChange()

Called for all top-level windows when a change is made in the system color setting.

#### Comments

 The MFC base class is always called before the Python method.


<!-- page: PyCWnd__OnTimer_virtual.html -->

## PyCWnd.OnTimer Virtual

 OnTimer(nIDEvent)

Called for the WM_TIMER message.

#### Parameters

- nIDEvent : int

 Specifies the identifier of the timer.


<!-- page: PyCWnd__OnWinIniChange_virtual.html -->

## PyCWnd.OnWinIniChange Virtual

 OnWinIniChange(section)

Called when the system configuration changes.

#### Parameters

- section : string

 The section which changed.

#### Comments

 The MFC base class is always called before the Python method.


<!-- page: PyCWnd__OnWndMsg_meth.html -->

## PyCWnd.OnWndMsg

 (int,int) = OnWndMsg(msg, wParam , lParam )

Calls the default MFC Window Message handler.

#### Parameters

- msg : int

 The message

- wParam : int

 The wParam for the message

- lParam : int

 The lParam for the message

#### MFC References

- CWnd::OnWndMsg

#### Return Value

The return value is a tuple of (int, int), being the return value from the MFC function call, and the value of the lResult param. Please see the MFC documentation for more details.


<!-- page: PyCWnd__PostMessage_meth.html -->

## PyCWnd.PostMessage

 PostMessage(idMessage, wParam, lParam)

Post a message to the window.

#### Parameters

- idMessage : int

 The ID of the message to post.

- wParam=0 : int

 The wParam for the message

- lParam=0 : int

 The lParam for the message

#### MFC References

- CWnd::PostMessage


<!-- page: PyCWnd__PreCreateWindow_meth.html -->

## PyCWnd.PreCreateWindow

 tuple = PreCreateWindow(createStruct)

Calls the underlying MFC PreCreateWindow method.

#### Parameters

- createStruct : tuple

 A tuple representing a CREATESTRUCT structure.

#### See Also

- PyCWnd.PreCreateWindow virtual method


<!-- page: PyCWnd__PreCreateWindow_virtual.html -->

## PyCWnd.PreCreateWindow Virtual

 PreCreateWindow(CREATESTRUCT)

Called by the framework before the creation of the Windows window attached to this View object.

#### Parameters

- CREATESTRUCT : tuple

 A tuple describing a CREATESTRUCT structure.

#### See Also

- PyCWnd::PreCreateWindow


<!-- page: PyCWnd__PreTranslateMessage_virtual.html -->

## PyCWnd.PreTranslateMessage Virtual

 PreTranslateMessage(msg)

Allows a Window to override the PreTranslateMessage handling.

#### Parameters

- msg : tuple

 Built from a MSG structure using format "iiiii(ii)"

#### Return Value

The result should be a tuple of the same format as the msg param, in which case the MSG structure will be updated and TRUE returned from the C++ function. If None is returned, the default handler is called.


<!-- page: PyCWnd__PumpWaitingMessages_meth.html -->

## PyCWnd.PumpWaitingMessages

 PumpWaitingMessages(firstMsg, lastMsg)

Pump messages associate with a window.

#### Parameters

- firstMsg : int

 First message ID to process

- lastMsg : int

 First message ID to process

#### MFC References

- CWnd::PeekMessage and DispatchMessage


<!-- page: PyCWnd__RedrawWindow_meth.html -->

## PyCWnd.RedrawWindow

 RedrawWindow(rect, object, flags)

Updates the specified rectangle or region in the given window's client area.

#### Parameters

- rect=None : (left, top, right, bottom)

 A rect, or None

- object=PyCRgn or None : PyCRgn

 A region

- flags=RDW_INVALIDATE | RDW_UPDATENOW | RDW_ERASE : int

#### MFC References

- CWnd::RedrawWindow


<!-- page: PyCWnd__ReleaseCapture_meth.html -->

## PyCWnd.ReleaseCapture

 ReleaseCapture()

Releases the mouse capture for this window. See PyCWnd::SetCapture.


<!-- page: PyCWnd__ReleaseDC_meth.html -->

## PyCWnd.ReleaseDC

 ReleaseDC(dc)

Releases a device context, freeing it for use by other applications.

#### Parameters

- dc : PyCDC

 The DC to be released.


<!-- page: PyCWnd__RepositionBars_meth.html -->

## PyCWnd.RepositionBars

 RepositionBars(idFirst, idLast, idLeftOver)

Repositions the windows control bars.( UINT nIDFirst, UINT nIDLast, UINT nIDLeftOver, UINT nFlag = CWnd::reposDefault, LPRECT lpRectParam = NULL, LPCRECT lpRectClient = NULL, BOOL bStretch = TRUE );

#### Parameters

- idFirst : int

 The ID of the first control to reposition.

- idLast : int

 The ID of the last control to reposition.

- idLeftOver : int


<!-- page: PyCWnd__RunModalLoop_meth.html -->

## PyCWnd.RunModalLoop

 int = RunModalLoop(flags)

Begins a modal loop for the window.

#### Parameters

- flags : int


<!-- page: PyCWnd__ScreenToClient_meth.html -->

## PyCWnd.ScreenToClient

 (left, top, right, bottom) or (x, y) = ScreenToClient(rect)

Converts the screen coordinates of a given point or rectangle on the display to client coordinates.

#### Parameters

- rect : (left, top, right, bottom) or (x,y)

 The coordinates to convert.

#### Alternative Parameters

- pnt

 The coordinates to convert.

#### MFC References

- CWnd::ScreenToClient

#### Return Value

The result is the same size as the input argument.


<!-- page: PyCWnd__SendMessageToDescendants_meth.html -->

## PyCWnd.SendMessageToDescendants

 SendMessageToDescendants(idMessage, wParam, lParam, bDeep)

Send a message to all descendant windows.

#### Parameters

- idMessage : int

 The ID of the message to send.

- wParam=0 : int

 The wParam for the message

- lParam=0 : int

 The lParam for the message

- bDeep=1 : int

 Indicates if the message should be recursively sent to all children

#### MFC References

- CWnd::SendMessageToDescendants


<!-- page: PyCWnd__SendMessage_meth.html -->

## PyCWnd.SendMessage

 SendMessage(idMessage, wParam, lParam)

Send a message to the window.

#### Parameters

- idMessage : int

 The ID of the message to send.

- wParam=0 : int

 The wParam for the message

- lParam=0 : int

 The lParam for the message

#### MFC References

- CWnd::SendMessage


<!-- page: PyCWnd__SetActiveWindow_meth.html -->

## PyCWnd.SetActiveWindow

 PyCWnd = SetActiveWindow()

Sets the window active. Returns the previously active window, or None.

#### Return Value

The result is the previous window with focus, or None.


<!-- page: PyCWnd__SetCapture_meth.html -->

## PyCWnd.SetCapture

 SetCapture()

Causes all subsequent mouse input to be sent to the window object regardless of the position of the cursor.


<!-- page: PyCWnd__SetDlgItemText_meth.html -->

## PyCWnd.SetDlgItemText

 SetDlgItemText(idControl, text)

Sets the text for the child window or control with the specified ID.

#### Parameters

- idControl : int

 The Id of the control

- text : string

 The new text

#### MFC References

- CWnd::SetDlgItemText


<!-- page: PyCWnd__SetFocus_meth.html -->

## PyCWnd.SetFocus

 SetFocus()

Claims the input focus. The object that previously had the focus loses it.


<!-- page: PyCWnd__SetFont_meth.html -->

## PyCWnd.SetFont

 SetFont(font, bRedraw)

Sets the window's current font to the specified font.

#### Parameters

- font : PyCFont

 The new font to use.

- bRedraw=1 : int

 If TRUE, redraw the window.


<!-- page: PyCWnd__SetForegroundWindow_meth.html -->

## PyCWnd.SetForegroundWindow

 SetForegroundWindow()

Puts the window into the foreground and activates the window.


<!-- page: PyCWnd__SetIcon_meth.html -->

## PyCWnd.SetIcon

 HICON = SetIcon()

Calls the underlying MFC SetIcon method.


<!-- page: PyCWnd__SetMenu_meth.html -->

## PyCWnd.SetMenu

 SetMenu(menuObj)

Sets the menu for a window.

#### Parameters

- menuObj : PyCMenu

 The menu object to set, or None to remove the window.


<!-- page: PyCWnd__SetRedraw_meth.html -->

## PyCWnd.SetRedraw

 SetRedraw(bState)

Allows changes to be redrawn or to prevent changes from being redrawn.

#### Parameters

- bState=1 : int

 Specifies the state of the redraw flag.

#### MFC References

- CWnd::SetRedraw


<!-- page: PyCWnd__SetScrollInfo_meth.html -->

## PyCWnd.SetScrollInfo

 int = SetScrollInfo(nBar, ScrollInfo , redraw )

Set information about a scroll bar

#### Parameters

- nBar : int

 The scroll bar to examine. Can be one of win32con.SB_BOTH, win32con.SB_VERT or win32con.SB_HORZ

- ScrollInfo : SCROLLINFO tuple

 The information to set

- redraw=1 : int

 A flag indicating if the scrollbar should be re-drawn.


<!-- page: PyCWnd__SetScrollPos_meth.html -->

## PyCWnd.SetScrollPos

 int = SetScrollPos(nBar, nPos , redraw )

Sets the current position of the scroll box of a scroll bar.

#### Parameters

- nBar : int

 The scroll bar to set. Can be one of win32con.SB_VERT or win32con.SB_HORZ

- nPos : int

 The new position

- redraw=1 : int

 A flag indicating if the scrollbar should be redrawn.


<!-- page: PyCWnd__SetTimer_meth.html -->

## PyCWnd.SetTimer

 int = SetTimer(idEvent, elapse )

Installs a system timer

#### Parameters

- idEvent : int

 The ID of the event

- elapse : int

 How often the timer should fire.

#### MFC References

- CWnd::SetTimer


<!-- page: PyCWnd__SetWindowPlacement_meth.html -->

## PyCWnd.SetWindowPlacement

 SetWindowPlacement(placement)

Sets the windows placement

#### Parameters

- placement : (tuple)

 A tuple representing the WINDOWPLACEMENT structure.

#### MFC References

- CWnd::SetWindowPlacement


<!-- page: PyCWnd__SetWindowPos_meth.html -->

## PyCWnd.SetWindowPos

 SetWindowPos(hWndInsertAfter, position, flags)

Sets the windows position information

#### Parameters

- hWndInsertAfter : int

 A hwnd, else one of the win32con.HWND_* constants.

- position : (x,y,cx,cy)

 The new position of the window.

- flags : int

 Window positioning flags.

#### MFC References

- CWnd::SetWindowPos


<!-- page: PyCWnd__SetWindowText_meth.html -->

## PyCWnd.SetWindowText

 SetWindowText(text)

Sets the window's text.

#### Parameters

- text : string

 The windows text.

#### MFC References

- CWnd::SetWindowText


<!-- page: PyCWnd__ShowCaret_meth.html -->

## PyCWnd.ShowCaret

 ShowCaret()

Shows the caret

#### Comments

 See also PyCWnd::HideCaret


<!-- page: PyCWnd__ShowScrollBar_meth.html -->

## PyCWnd.ShowScrollBar

 ShowScrollBar(nBar, bShow)

Shows or hides a scroll bar. An application should not call ShowScrollBar to hide a scroll bar while processing a scroll-bar notification message.

#### Parameters

- nBar : int

 Specifies whether the scroll bar is a control or part of a window's nonclient area. If it is part of the nonclient area, nBar also indicates whether the scroll bar is positioned horizontally, vertically, or both. It must be one of win32con.SB_BOTH, win32con.SB_HORZ or win32con.SB_VERT.

- bShow=1 : int

 Indicates if the scroll bar should be shown or hidden.

#### MFC References

- CWnd::ShowScrollBar


<!-- page: PyCWnd__ShowWindow_meth.html -->

## PyCWnd.ShowWindow

 int = ShowWindow(style)

Sets the visibility state of the window.

#### Parameters

- style=win32con.SW_SHOWNORMAL : int

 Specifies how the window is to be shown. It must be one of win32con.SW_HIDE, win32con.SW_MINIMIZE, win32con.SW_RESTORE, win32con.SW_SHOW, win32con.SW_SHOWMAXIMIZED win32con.SW_SHOWMINIMIZED, win32con.SW_SHOWMINNOACTIVE, win32con.SW_SHOWNA, win32con.SW_SHOWNOACTIVATE, or win32con.SW_SHOWNORMAL

#### MFC References

- CWnd::ShowWindow

#### Return Value

Returns TRUE is the window was previously visible.


<!-- page: PyCWnd__UnlockWindowUpdate_meth.html -->

## PyCWnd.UnlockWindowUpdate

 UnlockWindowUpdate()

Unlocks a window that was locked with LockWindowUpdate

#### MFC References

- CWnd::UnLockWindowUpdate


<!-- page: PyCWnd__UpdateData_meth.html -->

## PyCWnd.UpdateData

 int = UpdateData(bSaveAndValidate)

Initialises data in a dialog box, or to retrieves and validates dialog data. Returns nonzero if the operation is successful; otherwise 0. If bSaveAndValidate is TRUE, then a return value of nonzero means that the data is successfully validated.

#### Parameters

- bSaveAndValidate=1 : int

 Flag that indicates whether dialog box is being initialized (FALSE) or data is being retrieved (TRUE).

#### MFC References

- CWnd::UpdateData


<!-- page: PyCWnd__UpdateDialogControls_meth.html -->

## PyCWnd.UpdateDialogControls

 int = UpdateDialogControls(pTarget, disableIfNoHandler )

Updates the state of dialog buttons and other controls in a dialog box or window that uses the PyCCmdUI::HookCommandUpdate callback mechanism.

#### Parameters

- pTarget : PyCCmdTarget

 The main frame window of the application, and is used for routing update messages.

- disableIfNoHandler : int

 Flag that indicates whether a control that has no update handler should be automatically displayed as disabled.


<!-- page: PyCWnd__UpdateWindow_meth.html -->

## PyCWnd.UpdateWindow

 UpdateWindow()

Updates a window. This forces a paint message to be sent to the window, if any part of the window is marked as invalid.


---

<!-- object: PyConsoleScreenBuffer -->


<!-- page: PyConsoleScreenBuffer.html -->

---

## PyConsoleScreenBuffer Object

 Handle to a console screen buffer Create using win32console::CreateConsoleScreenBuffer or win32console::GetStdHandle Use PyConsoleScreenBufferType(Handle) to wrap a pre-existing handle as returned by win32api::GetStdHandle. Will also accept a handle created by win32file::CreateFile for CONIN$ or CONOUT$. When an existing handle is wrapped, a copy is made using DuplicateHandle, and caller is still responsible for any cleanup of original handle.

#### Methods

- Detach

 Releases reference to handle without closing it

- Close

 Closes the handle

- SetConsoleActiveScreenBuffer

 Sets this handle as the currently display screen buffer

- GetConsoleCursorInfo

 Retrieves size and visibility of console's cursor

- SetConsoleCursorInfo

 Sets the size and visibility of console's cursor

- GetConsoleMode

 Returns the input or output mode of the console buffer

- SetConsoleMode

 Sets the input or output mode of the console buffer

- ReadConsole

 Reads characters from the console input buffer

- WriteConsole

 Writes characters at current cursor position

- FlushConsoleInputBuffer

 Flush input buffer for console

- SetConsoleTextAttribute

 Sets character attributes for subsequent write operations

- SetConsoleCursorPosition

 Sets the console screen buffer's cursor position

- SetConsoleScreenBufferSize

 Sets the size of the console screen buffer

- SetConsoleWindowInfo

 Changes size and position of a console's window

- GetConsoleScreenBufferInfo

 Returns the state of the screen buffer

- GetLargestConsoleWindowSize

 Returns the largest possible size for the console's window

- FillConsoleOutputAttribute

 Set text attributes for a consecutive series of characters

- FillConsoleOutputCharacter

 Sets consecutive character positions to a specified character

- ReadConsoleOutputCharacter

 Reads consecutive characters from a starting position

- ReadConsoleOutputAttribute

 Retrieves attributes from consecutive character cells

- WriteConsoleOutputCharacter

 Writes a string of characters at a specified position

- WriteConsoleOutputAttribute

 Sets the attributes of a range of character cells

- ScrollConsoleScreenBuffer

 Scrolls a region of the display

- GetCurrentConsoleFont

 Returns the currently displayed font

- GetConsoleFontSize

 Returns size of specified font for the console

- SetConsoleFont

 Changes the font used by the screen buffer

- SetStdHandle

 Replaces one of calling process's standard handles with this handle

- SetConsoleDisplayMode

 Sets the display mode of the console buffer

- WriteConsoleInput

 Places input records in the console's input queue

- ReadConsoleInput

 Reads input records and removes them from the input queue

- PeekConsoleInput

 Returns pending input records without removing them from the input queue

- GetNumberOfConsoleInputEvents

 Returns the number of unread records in the input queue


<!-- page: PyConsoleScreenBuffer__FillConsoleOutputAttribute_meth.html -->

## PyConsoleScreenBuffer.FillConsoleOutputAttribute

 int = FillConsoleOutputAttribute(Attribute, Length , WriteCoord )

Set text attributes for a consecutive series of characters

#### Parameters

- Attribute : int

 Text attributes to be set, combination of FOREGROUND_*, BACKGROUND_*, and COMMON_LVB_* constants

- Length : int

 The number of characters to set

- WriteCoord : PyCOORD

 The screen position to begin at

#### Return Value

Returns the number of character cells whose attributes were set


<!-- page: PyConsoleScreenBuffer__FillConsoleOutputCharacter_meth.html -->

## PyConsoleScreenBuffer.FillConsoleOutputCharacter

 int = FillConsoleOutputCharacter(Character, Length , WriteCoord )

Sets consecutive character positions to a specified character

#### Parameters

- Character : PyUNICODE

 A single character to be used to fill the specified range

- Length : int

 The number of characters positions to fill

- WriteCoord : PyCOORD

 The screen position to begin at

#### Return Value

Returns the number of characters actually written


<!-- page: PyConsoleScreenBuffer__FlushConsoleInputBuffer_meth.html -->

## PyConsoleScreenBuffer.FlushConsoleInputBuffer

 FlushConsoleInputBuffer()

Flush input buffer


<!-- page: PyConsoleScreenBuffer__GetConsoleCursorInfo_meth.html -->

## PyConsoleScreenBuffer.GetConsoleCursorInfo

 (Size, bVisible) = GetConsoleCursorInfo()

Retrieves size and visibility of console's cursor

#### Return Value

Returns the size of the console's cursor expressed as a percentage of character size, and a boolen indicating if cursor is visible


<!-- page: PyConsoleScreenBuffer__GetConsoleFontSize_meth.html -->

## PyConsoleScreenBuffer.GetConsoleFontSize

 PyCOORD = GetConsoleFontSize(Font)

Returns size of specified font for the console

#### Parameters

- Font : int

 Index of font as returned by GetCurrentConsoleFont


<!-- page: PyConsoleScreenBuffer__GetConsoleMode_meth.html -->

## PyConsoleScreenBuffer.GetConsoleMode

 int = GetConsoleMode()

Returns the input or output mode of the console buffer

#### Return Value

Returns a combination of ENABLE_*_INPUT or ENABLE_*_OUTPUT constants


<!-- page: PyConsoleScreenBuffer__GetConsoleScreenBufferInfo_meth.html -->

## PyConsoleScreenBuffer.GetConsoleScreenBufferInfo

 dict = GetConsoleScreenBufferInfo()

Returns the state of the screen buffer


<!-- page: PyConsoleScreenBuffer__GetCurrentConsoleFont_meth.html -->

## PyConsoleScreenBuffer.GetCurrentConsoleFont

 (int, PyCOORD) = GetCurrentConsoleFont(MaximumWindow)

Returns currently displayed font

#### Parameters

- MaximumWindow=False : boolean

 If True, retrieves font size for maximum window size

#### Return Value

Returns the index of current font and window size MSDN docs claim the returned COORD is the font size, but it's actually the window size.
 Use PyConsoleScreenBuffer::GetConsoleFontSize for the font size.


<!-- page: PyConsoleScreenBuffer__GetLargestConsoleWindowSize_meth.html -->

## PyConsoleScreenBuffer.GetLargestConsoleWindowSize

 PyCOORD = GetLargestConsoleWindowSize()

Returns the largest possible size for the console's window


<!-- page: PyConsoleScreenBuffer__GetNumberOfConsoleInputEvents_meth.html -->

## PyConsoleScreenBuffer.GetNumberOfConsoleInputEvents

 int = GetNumberOfConsoleInputEvents()

Returns the number of unread records in the input queue


<!-- page: PyConsoleScreenBuffer__PeekConsoleInput_meth.html -->

## PyConsoleScreenBuffer.PeekConsoleInput

 (PyINPUT_RECORD,...) = PeekConsoleInput(Length)

Returns pending input records without removing them from the input queue

#### Parameters

- Length : int

 The number of input records to read

#### Comments

 This function does not block as ReadConsoleInput does.
 The number of records returned may be less than the nbr requested

#### Return Value

Returns a sequence of PyINPUT_RECORD objects


<!-- page: PyConsoleScreenBuffer__ReadConsoleInput_meth.html -->

## PyConsoleScreenBuffer.ReadConsoleInput

 (PyINPUT_RECORD,...) = ReadConsoleInput(Length)

Reads input records and removes them from the input queue

#### Parameters

- Length : int

 The number of input records to read

#### Comments

 This functions blocks until at least one record is read.
 The number of records returned may be less than the nbr requested

#### Return Value

Returns a sequence of PyINPUT_RECORD objects


<!-- page: PyConsoleScreenBuffer__ReadConsoleOutputAttribute_meth.html -->

## PyConsoleScreenBuffer.ReadConsoleOutputAttribute

 (int,...) = ReadConsoleOutputAttribute(Length, ReadCoord )

Retrieves attributes from consecutive character cells

#### Parameters

- Length : int

 The number of attributes to read

- ReadCoord : PyCOORD

 The screen position from which to start reading

#### Return Value

Returns a sequence of ints containing the attributes of a range of characters


<!-- page: PyConsoleScreenBuffer__ReadConsoleOutputCharacter_meth.html -->

## PyConsoleScreenBuffer.ReadConsoleOutputCharacter

 PyUnicode = ReadConsoleOutputCharacter(Length, ReadCoord )

Reads consecutive characters from a starting position

#### Parameters

- Length : int

 The number of characters positions to read

- ReadCoord : PyCOORD

 The screen position start reading from


<!-- page: PyConsoleScreenBuffer__ReadConsole_meth.html -->

## PyConsoleScreenBuffer.ReadConsole

 PyUNICODE = ReadConsole(NumberOfCharsToRead)

Reads characters from the console input buffer

#### Parameters

- NumberOfCharsToRead : int

 Characters to read


<!-- page: PyConsoleScreenBuffer__ScrollConsoleScreenBuffer_meth.html -->

## PyConsoleScreenBuffer.ScrollConsoleScreenBuffer

 ScrollConsoleScreenBuffer(ScrollRectangle, ClipRectangle, DestinationOrigin, FillCharacter, FillAttribute)

Scrolls a region of the display

#### Parameters

- ScrollRectangle : PySMALL_RECT

 The region to be scrolled

- ClipRectangle : PySMALL_RECT

 Rectangle that limits display area affected, can be None

- DestinationOrigin : PyCOORD

 The position to which ScrollRectangle will be moved

- FillCharacter : PyUNICODE

 Character to fill in the area left blank by scrolling operation

- FillAttribute : int

 Text attributes to apply to FillCharacter


<!-- page: PyConsoleScreenBuffer__SetConsoleActiveScreenBuffer_meth.html -->

## PyConsoleScreenBuffer.SetConsoleActiveScreenBuffer

 SetConsoleActiveScreenBuffer()

Sets this handle as the currently displayed screen buffer


<!-- page: PyConsoleScreenBuffer__SetConsoleCursorInfo_meth.html -->

## PyConsoleScreenBuffer.SetConsoleCursorInfo

 SetConsoleCursorInfo(Size, Visible)

Sets the size and visibility of console's cursor

#### Parameters

- Size : int

 Percentage of character size that cursor will occupy

- Visible : boolen

 Determines if cursor is visible


<!-- page: PyConsoleScreenBuffer__SetConsoleCursorPosition_meth.html -->

## PyConsoleScreenBuffer.SetConsoleCursorPosition

 SetConsoleCursorPosition(CursorPosition)

Sets the console screen buffer's cursor position

#### Parameters

- CursorPosition : PyCOORD

 A PyCOORD containing the new cursor position


<!-- page: PyConsoleScreenBuffer__SetConsoleDisplayMode_meth.html -->

## PyConsoleScreenBuffer.SetConsoleDisplayMode

 SetConsoleDisplayMode(Flags, NewScreenBufferDimensions)

Sets the display mode of the console buffer

#### Parameters

- Flags : int

 CONSOLE_FULLSCREEN_MODE or CONSOLE_WINDOWED_MODE

- NewScreenBufferDimensions : PyCOORD

 New size of the screen buffer in characters


<!-- page: PyConsoleScreenBuffer__SetConsoleFont_meth.html -->

## PyConsoleScreenBuffer.SetConsoleFont

 SetConsoleFont(Font)

Changes the font used by the screen buffer

#### Parameters

- Font : int

 The number of the font to be set

#### Comments

 Function is not documented on MSDN and removed in Windows 10.0.1607


<!-- page: PyConsoleScreenBuffer__SetConsoleMode_meth.html -->

## PyConsoleScreenBuffer.SetConsoleMode

 SetConsoleMode(Mode)

Sets the input or output mode of the console buffer

#### Parameters

- Mode : int

 Combination of ENABLE_*_INPUT or ENABLE_*_OUTPUT constants


<!-- page: PyConsoleScreenBuffer__SetConsoleScreenBufferSize_meth.html -->

## PyConsoleScreenBuffer.SetConsoleScreenBufferSize

 SetConsoleScreenBufferSize(Size)

Sets the size of the console screen buffer

#### Parameters

- Size : PyCOORD

 COORD object containing the new dimensions


<!-- page: PyConsoleScreenBuffer__SetConsoleTextAttribute_meth.html -->

## PyConsoleScreenBuffer.SetConsoleTextAttribute

 SetConsoleTextAttribute(Attributes)

Sets character attributes for subsequent write operations

#### Parameters

- Attributes : int

 Attributes to be set, combination of FOREGROUND_*, BACKGROUND_*, and COMMON_LVB_* constants


<!-- page: PyConsoleScreenBuffer__SetConsoleWindowInfo_meth.html -->

## PyConsoleScreenBuffer.SetConsoleWindowInfo

 SetConsoleWindowInfo(Absolute, ConsoleWindow)

Changes size and position of a console's window

#### Parameters

- Absolute : boolean

 If False, coordinates are relative to current position

- ConsoleWindow : PySMALL_RECT

 A SMALL_RECT containing the new window coordinates


<!-- page: PyConsoleScreenBuffer__SetStdHandle_meth.html -->

## PyConsoleScreenBuffer.SetStdHandle

 SetStdHandle(StdHandle)

Replaces one of calling process's standard handles with this handle

#### Parameters

- StdHandle : int

 Specifies handle to be replaced - STD_INPUT_HANDLE, STD_OUTPUT_HANDLE, or STD_ERROR_HANDLE


<!-- page: PyConsoleScreenBuffer__WriteConsoleInput_meth.html -->

## PyConsoleScreenBuffer.WriteConsoleInput

 int = WriteConsoleInput(Buffer)

Places input records in the console's input queue

#### Parameters

- Buffer : (PyINPUT_RECORD,...)

 A sequence of PyINPUT_RECORD objects

#### Return Value

Returns the number of records written


<!-- page: PyConsoleScreenBuffer__WriteConsoleOutputAttribute_meth.html -->

## PyConsoleScreenBuffer.WriteConsoleOutputAttribute

 int = WriteConsoleOutputAttribute(Attributes, WriteCoord )

Sets the attributes of a range of character cells

#### Parameters

- Attributes : (int,...)

 A sequence of ints containing the attributes to be set

- WriteCoord : PyCOORD

 The screen position at which to start writing

#### Return Value

Returns the number of attributes set


<!-- page: PyConsoleScreenBuffer__WriteConsoleOutputCharacter_meth.html -->

## PyConsoleScreenBuffer.WriteConsoleOutputCharacter

 int = WriteConsoleOutputCharacter(Characters, WriteCoord )

Writes a string of characters at a specified position

#### Parameters

- Characters : PyUNICODE

 Characters to be written

- WriteCoord : PyCOORD

 The screen position at which to start writing

#### Return Value

Returns the number of characters actually written


<!-- page: PyConsoleScreenBuffer__WriteConsole_meth.html -->

## PyConsoleScreenBuffer.WriteConsole

 int = WriteConsole(Buffer)

Writes characters at current cursor position

#### Parameters

- Buffer : PyUNICODE

 String or Unicode to be written to console

#### Return Value

Returns the number of characters written


---

<!-- object: PyCredHandle -->


<!-- page: PyCredHandle.html -->

---

## PyCredHandle Object

 Handle to a set of logon credentials, used with sspi authentication functions

#### Comments

 This object is usually created using win32security::AcquireCredentialsHandle. An uninitialized handle can also be created using win32security.PyCredHandleType()

#### Methods

- Detach

 Disassociates object from handle and returns integer value of handle (prevents automatic freeing of credentials when object is deallocated),

- FreeCredentialsHandle

 Releases the credentials handle

- QueryCredentialsAttributes

 Returns information about the credentials


<!-- page: PyCredHandle__Detach_meth.html -->

## PyCredHandle.Detach

 long = Detach()

Disassociates object from handle and returns integer value of handle,


<!-- page: PyCredHandle__FreeCredentialsHandle_meth.html -->

## PyCredHandle.FreeCredentialsHandle

 FreeCredentialsHandle()

Releases the credentials handle and makes object unusable


<!-- page: PyCredHandle__QueryCredentialsAttributes_meth.html -->

## PyCredHandle.QueryCredentialsAttributes

 QueryCredentialsAttributes(Attribute)

Returns information about the credentials

#### Parameters

- Attribute : int

 SECPKG_* constant specifying which type of information to return

#### Comments

 Only SECPKG_CRED_ATTR_NAMES currently supported

| | Attribute | Return type
| |

---

 |

---

| | SECPKG_CRED_ATTR_NAMES | PyUnicode - returns username that credentials represent
| | SECPKG_ATTR_SUPPORTED_ALGS | Not supported yet SecPkgCred_SupportedAlgs:
| | SECPKG_ATTR_CIPHER_STRENGTHS | Not supported yet SecPkgCred_CipherStrengths:
| | SECPKG_ATTR_SUPPORTED_PROTOCOLS | Not supported yet SecPkgCred_SupportedProtocols:

#### Return Value

Type of returned values is dependent on Attribute


---

<!-- object: PyCtxtHandle -->


<!-- page: PyCtxtHandle.html -->

---

## PyCtxtHandle Object

 Security context handle, as used with sspi functions

#### Comments

 Create using win32security.PyCtxtHandleType(). The handle must be initialized by passing it to win32security::InitializeSecurityContext or win32security::AcceptSecurityContext

#### Methods

- Detach

 Disassociates object from handle and returns integer value of handle

- CompleteAuthToken

 Completes the authentication token

- QueryContextAttributes

 Retrieves info about a security context

- DeleteSecurityContext

 Frees the security context and invalidates the handle

- QuerySecurityContextToken

 Returns the access token for a security context

- MakeSignature

 Generates a signature for a message

- VerifySignature

 Verifies a signature created using PyCtxtHandle::MakeSignature

- EncryptMessage

 Encrypts data with security context's session key

- DecryptMessage

 Decrypts data encrypted by PyCtxtHandle::EncryptMessage

- ImpersonateSecurityContext

 Causes a server to act in the security context of an authenticated client

- RevertSecurityContext

 Stops impersonation of a client initiated by PyCtxtHandle::ImpersonateSecurityContext


<!-- page: PyCtxtHandle__CompleteAuthToken_meth.html -->

## PyCtxtHandle.CompleteAuthToken

 CompleteAuthToken(Token)

Completes the authentication token

#### Parameters

- Token : PySecBufferDesc

 The buffer that contains the token buffer used when the context was initialized

#### Comments

 This method should be invoked on a context handle if the InitializeSecurityContext call that created it returned SEC_I_COMPLETE_NEEDED or SEC_I_COMPLETE_AND_CONTINUE


<!-- page: PyCtxtHandle__DecryptMessage_meth.html -->

## PyCtxtHandle.DecryptMessage

 DecryptMessage(Message, MessageSeqNo)

Decrypts data produced by PyCtxtHandle::EncryptMessage

#### Parameters

- Message : PySecBufferDesc

 PySecBufferDesc containing data buffers to be decrypted

- MessageSeqNo : int

 A sequential number used by some packages to verify that no extraneous messages have been received

#### Comments

 The buffer configuration is dependent on the security package. Usually there is one buffer of type SECBUFFER_DATA which is modified in place and a second buffer of type SECBUFFER_TOKEN or SECBUFFER_PADDING containing signature, padding, or other extra data from encryption process that doesn't fit in first buffer

#### Return Value

Returns flags specfic to security package indicating quality of protection


<!-- page: PyCtxtHandle__DeleteSecurityContext_meth.html -->

## PyCtxtHandle.DeleteSecurityContext

 DeleteSecurityContext()

Frees the security context and invalidates the handle


<!-- page: PyCtxtHandle__Detach_meth.html -->

## PyCtxtHandle.Detach

 long = Detach()

Disassociates object from handle and returns integer value of handle

#### Comments

 Use when the security context needs to persist beyond the lifetime of the Python object


<!-- page: PyCtxtHandle__EncryptMessage_meth.html -->

## PyCtxtHandle.EncryptMessage

 EncryptMessage(fqop, Message, MessageSeqNo)

Encrypts data with session key of security context

#### Parameters

- fqop : int

 Flags that indicate quality of protection desired, specific to each security package

- Message : PySecBufferDesc

 PySecBufferDesc that contains data buffer(s) to be encrypted

- MessageSeqNo : int

 A sequential number used by some packages to verify that no extraneous messages have been received

#### Comments

 The buffer configuration is dependent on the security package. Usually there is one input buffer of type SECBUFFER_DATA to be encrypted in-place and another empty buffer of type SECBUFFER_PADDING or SECBUFFER_TOKEN to receive signature or padding data

#### Return Value

Returns None on success, and buffer(s) will contain encrypted data


<!-- page: PyCtxtHandle__ImpersonateSecurityContext_meth.html -->

## PyCtxtHandle.ImpersonateSecurityContext

 ImpersonateSecurityContext()

Impersonates a client security context


<!-- page: PyCtxtHandle__MakeSignature_meth.html -->

## PyCtxtHandle.MakeSignature

 MakeSignature(fqop, Message, MessageSeqNo)

Creates a crytographic hash of a message using session key of the security context

#### Parameters

- fqop : int

 Flags that indicate quality of protection desired, specific to each security package

- Message : PySecBufferDesc

 Buffer set that includes buffers for input data and output signature

- MessageSeqNo : int

 A sequential number used by some packages to verify that no extraneous messages have been received

#### Comments

 The buffer configuration is dependent on the security package. Usually there is one input buffer of type SECBUFFER_DATA and an output buffer of type SECBUFFER_TOKEN

#### Return Value

Returns None on success, and output buffer in Message will contain the signature


<!-- page: PyCtxtHandle__QueryContextAttributes_meth.html -->

## PyCtxtHandle.QueryContextAttributes

 QueryContextAttributes(Attribute)

Retrieves info about a security context

#### Parameters

- Attribute : int

 SECPKG_ATTR_* constant

#### Comments

 Not all attributes are available for every security package

| | Attribute | Return type
| |

---

 |

---

| | SECPKG_ATTR_ACCESS_TOKEN | PyHANDLE - returns a handle to the context's access token
| | SECPKG_ATTR_AUTHORITY | PyUnicode - returns the name of the authenticating entity
| | SECPKG_ATTR_CIPHER_STRENGTHS | (int,int) - returns the mininum and maximum cipher strengths allowed
| | SECPKG_ATTR_CONNECTION_INFO | Returns a dictionary of connection info representing a SecPkgContext_ConnectionInfo struct
| | SECPKG_ATTR_SESSION_KEY | string - returns the session key for the context
| | SECPKG_ATTR_ISSUER_LIST_EX | (int, string) - Returns names of trusted certificate issuers
| | SECPKG_ATTR_FLAGS | int - returns flags negotiated when context was established
| | SECPKG_ATTR_PACKAGE_INFO | dict - returns dictionary containing info for context's security package
| | SECPKG_ATTR_NEGOTIATION_INFO | (int, dict) - returns state of negotiation (SECPKG_NEGOTIATION_COMPLETE, SECPKG_NEGOTIATION_OPTIMISTIC,SECPKG_NEGOTIATION_IN_PROGRESS) and info for negotiated package
| | SECPKG_ATTR_NAMES | PyUnicode - returns the user name for the context
| | SECPKG_ATTR_SIZES | dict containing buffer sizes to be used with the context
| | SECPKG_ATTR_PASSWORD_EXPIRY | PyDateTime - returns time password expires
| | SECPKG_ATTR_LIFESPAN | (PyDateTime,PyDateTime) - returns time period during which context is valid
| | SECPKG_ATTR_NATIVE_NAMES | (PyUnicode ,PyUnicode ) - returns client and server names
| | SECPKG_ATTR_TARGET_INFORMATION | string - returns the target for the context
| | SECPKG_ATTR_STREAM_SIZES | dict (see SecPkgContext_StreamSizes) containing message buffer sizes
| | SECPKG_ATTR_KEY_INFO | dict (see SecPkgContext_KeyInfo) containing encryption key parameters
| | SECPKG_ATTR_DCE_INFO | not supported yet SecPkgContext_DceInfo
| | SECPKG_ATTR_LOCAL_CERT_CONTEXT | not supported yet PCCERT_CONTEXT
| | SECPKG_ATTR_REMOTE_CERT_CONTEXT | not supported yet PCCERT_CONTEXT
| | SECPKG_ATTR_ROOT_STORE | not supported yet HCERTCONTEXT
| | SECPKG_ATTR_SUPPORTED_ALGS | not supported yet SecPkgCred_SupportedAlgs
| | SECPKG_ATTR_SUPPORTED_PROTOCOLS | not supported yet SecPkgCred_SupportedProtocols


<!-- page: PyCtxtHandle__QuerySecurityContextToken_meth.html -->

## PyCtxtHandle.QuerySecurityContextToken

 PyHandle = QuerySecurityContextToken()

Returns the access token for a security context


<!-- page: PyCtxtHandle__RevertSecurityContext_meth.html -->

## PyCtxtHandle.RevertSecurityContext

 RevertSecurityContext()

Stops impersonation of client context (see PyCtxtHandle::ImpersonateSecurityContext)


<!-- page: PyCtxtHandle__VerifySignature_meth.html -->

## PyCtxtHandle.VerifySignature

 VerifySignature(Message, MessageSeqNo)

Verifies a signature created using PyCtxtHandle::MakeSignature

#### Parameters

- Message : PySecBufferDesc

 SecBufferDesc that contains data buffer and signature buffer

- MessageSeqNo : int

 A sequential number used by some packages to verify that no extraneous messages have been received

#### Comments

 The buffer configuration is dependent on the security package. Usually there is a data buffer of type SECBUFFER_DATA and a signature buffer of type SECBUFFER_TOKEN

#### Return Value

Returns quality of protection flags used to create signature


---

<!-- object: PyDCB -->


<!-- page: PyDCB.html -->

---

## PyDCB Object

 A Python object, representing an DCB structure

#### Comments

 Typically you query a device for its DCB using win32file::GetCommState, change any setting necessary, then call win32file::SetCommState with the new structure. TRUE*/)

#### Properties

- integer BaudRate
 current baud rate

- integer wReserved
 not currently used

- integer XonLim
 transmit XON threshold

- integer XoffLim
 transmit XOFF threshold

- integer ByteSize
 number of bits/byte, 4-8

- integer Parity
 0-4=no,odd,even,mark,space

- integer StopBits
 0,1,2 = 1, 1.5, 2

- character XonChar
 Tx and Rx XON character

- character XoffChar
 Tx and Rx XOFF character

- character ErrorChar
 error replacement character

- character EofChar
 end of input character

- character EvtChar
 received event character

- integer wReserved1
 reserved; do not use

- integer fBinary
 binary mode, no EOF check

- integer fParity
 enable parity checking

- integer fOutxCtsFlow
 CTS output flow control

- integer fOutxDsrFlow
 DSR output flow control

- integer fDtrControl
 DTR flow control type

- integer fDsrSensitivity
 DSR sensitivity

- integer fTXContinueOnXoff
 XOFF continues Tx

- integer fOutX
 XON/XOFF out flow control

- integer fInX
 XON/XOFF in flow control

- integer fErrorChar
 enable error replacement

- integer fNull
 enable null stripping

- integer fRtsControl
 RTS flow control

- integer fAbortOnError
 abort on error

- integer fDummy2
 reserved


---

<!-- object: PyDDEConv -->


<!-- page: PyDDEConv.html -->

---

## PyDDEConv Object

 A DDE topic.

#### Methods

- ConnectTo

 Connects to a server

- Connected

 Determines if a connection has been made.

- Exec

 Executes a command.

- Request

 Sends a request.

- Poke

 Sends a poke. sentinel


<!-- page: PyDDEConv__ConnectTo_meth.html -->

## PyDDEConv.ConnectTo

 ConnectTo(service, topic)

Connects to a server

#### Parameters

- service : string

 The service to connect to

- topic : string

 The topic to connect to


<!-- page: PyDDEConv__Connected_meth.html -->

## PyDDEConv.Connected

 Connected()

Determines if the conversation is connected.


<!-- page: PyDDEConv__Exec_meth.html -->

## PyDDEConv.Exec

 Exec(Cmd)

Executes a command.

#### Parameters

- Cmd : string

 The Python statement to execute


<!-- page: PyDDEConv__Poke_meth.html -->

## PyDDEConv.Poke

 Poke()

Sends a poke.


<!-- page: PyDDEConv__Request_meth.html -->

## PyDDEConv.Request

 Request()

Sends a request.


---

<!-- object: PyDDEServer -->


<!-- page: PyDDEServer.html -->

---

## PyDDEServer Object

 A DDE server.

#### Methods

- AddTopic

 Adds a topic to the server.

- Create

 Creates a DDE server

- Destroy

 Destroys the underlying C++ object.

- GetLastError

 Returns the last DDE error.

- Shutdown

 Shutsdown the server. sentinel


<!-- page: PyDDEServer__AddTopic_meth.html -->

## PyDDEServer.AddTopic

 AddTopic(topic)

#### Parameters

- topic : PyDDETopic

 The topic to add.


<!-- page: PyDDEServer__Create_meth.html -->

## PyDDEServer.Create

 Create(name, filterFlags)

Create a server

#### Parameters

- name : string

 Name of the server to start.

- filterFlags=0 : int

 Filter flags.

#### Comments

 Note there can only be one server per application.


<!-- page: PyDDEServer__Destroy_meth.html -->

## PyDDEServer.Destroy

 Destroy()


<!-- page: PyDDEServer__GetLastError_meth.html -->

## PyDDEServer.GetLastError

 int = GetLastError()


<!-- page: PyDDEServer__Shutdown_meth.html -->

## PyDDEServer.Shutdown

 Shutdown()

#### Comments

 Note the underlying DDE object (ie, Server, Topics and Items) are not cleaned up by this call.


---

<!-- object: PyDDEStringItem -->


<!-- page: PyDDEStringItem.html -->

---

## PyDDEStringItem Object

 A DDE string item.

#### Methods

- SetData

 Sets an items data, and causes any underlying notification. sentinel


<!-- page: PyDDEStringItem__Destroy_meth.html -->

## PyDDEStringItem.Destroy

 Destroy()

Destroys an item


<!-- page: PyDDEStringItem__SetData_meth.html -->

## PyDDEStringItem.SetData

 SetData(data)

Sets an items data, and causes any underlying notification.

#### Parameters

- data : string

 The data to set.


---

<!-- object: PyDDETopic -->


<!-- page: PyDDETopic.html -->

---

## PyDDETopic Object

 A DDE topic.

#### Methods

- AddItem

 Add an item to the topic.

- Destroy

 Destroys an item sentinel


<!-- page: PyDDETopic__AddItem_meth.html -->

## PyDDETopic.AddItem

 AddItem(item)

Add an item to the topic.

#### Parameters

- item : PyDDEItem

 The item to add


<!-- page: PyDDETopic__Destroy_meth.html -->

## PyDDETopic.Destroy

 Destroy()

Destroys an item


---

<!-- object: PyDEVMODEW -->


<!-- page: PyDEVMODEW.html -->

---

## PyDEVMODEW Object

 Unicode version of PyDEVMODE object

#### Methods

- Clear

 Resets all members of the structure

#### Properties

- int SpecVersion
 Should always be set to DM_SPECVERSION

- int DriverVersion
 Version nbr assigned to printer driver by vendor

- int Size
 Size of structure

- int DriverExtra
 Number of extra bytes allocated for driver data, can only be set when new object is created

- int Fields
 Bitmask of win32con.DM_* constants indicating which members are set

- int Orientation
 Only applies to printers, DMORIENT_PORTRAIT or DMORIENT_LANDSCAPE

- int PaperSize
 Use 0 if PaperWidth and PaperLength are set, otherwise win32con.DMPAPER_* constant

- int PaperLength
 Specified in 1/10 millimeters

- int PaperWidth
 Specified in 1/10 millimeters

- int Position_x
 Position of display relative to desktop

- int Position_y
 Position of display relative to desktop

- int DisplayOrientation
 Display rotation: DMDO_DEFAULT,DMDO_90, DMDO_180, DMDO_270

- int DisplayFixedOutput
 DMDFO_DEFAULT, DMDFO_CENTER, DMDFO_STRETCH

- int Scale
 Specified as percentage, eg 50 means half size of original

- int Copies
 Nbr of copies to print

- int DefaultSource
 DMBIN_* constant, or can be a printer-specific value

- int PrintQuality
 DMRES_* constant, interpreted as DPI if positive

- int Color
 DMCOLOR_COLOR or DMCOLOR_MONOCHROME

- int Duplex
 For printers that do two-sided printing: DMDUP_SIMPLEX, DMDUP_HORIZONTAL, DMDUP_VERTICAL

- int YResolution
 Vertical printer resolution in DPI - if this is set, PrintQuality indicates horizontal DPI

- int TTOption
 TrueType options: DMTT_BITMAP, DMTT_DOWNLOAD, DMTT_DOWNLOAD_OUTLINE, DMTT_SUBDEV

- int Collate
 DMCOLLATE_TRUE or DMCOLLATE_FALSE

- int LogPixels
 Pixels per inch (only for display devices

- int BitsPerPel
 Color resolution in bits per pixel

- int PelsWidth
 Pixel width of display

- int PelsHeight
 Pixel height of display

- int DisplayFlags
 Combination of DM_GRAYSCALE and DM_INTERLACED

- int DisplayFrequency
 Refresh rate

- int ICMMethod
 Indicates where ICM is performed, one of win32con.DMICMMETHOD_* values

- int ICMIntent
 Intent of ICM, one of win32con.DMICM_* values

- int MediaType
 win32con.DMMEDIA_*, can also be a printer-specific value greater then DMMEDIA_USER

- int DitherType
 Dithering option, win32con.DMDITHER_*

- int Reserved1
 Reserved, use only 0

- int Reserved2
 Reserved, use only 0

- int Nup
 Controls printing of multiple logical pages per physical page, DMNUP_SYSTEM or DMNUP_ONEUP

- int PanningWidth
 Not used, leave as 0

- int PanningHeight
 Not used, leave as 0

- string DeviceName
 String of at most 32 chars

- str FormName
 Name of form as returned by win32print::EnumForms, at most 32 chars

- str DriverData
 Driver data appended to end of structure


---

<!-- object: PyDISPLAY_DEVICE -->


<!-- page: PyDISPLAY_DEVICE.html -->

---

## PyDISPLAY_DEVICE Object

 Python object wrapping a DISPLAY_DEVICE structure

#### Methods

- Clear

 Resets all members of the structure

#### Properties

- int Size
 Size of structure

- str DeviceName
 String of at most 32 chars

- str DeviceString
 String of at most 128 chars

- int StateFlags
 Bitmask of win32con.DISPLAY_DEVICE_* constants indicating current device status

- str DeviceID
 String of at most 128 chars

- str DeviceKey
 String of at most 128 chars


<!-- page: PyDISPLAY_DEVICE__Clear_meth.html -->

## PyDISPLAY_DEVICE.Clear

 Clear()

Resets all members of the structure


---

<!-- object: PyDLGITEMTEMPLATE -->


<!-- page: PyDLGITEMTEMPLATE.html -->

---

## PyDLGITEMTEMPLATE Object

 A tuple describing a control in a dialog box.

#### Win32 API References

- Search for DLGITEMTEMPLATE at [msdn](https://learn.microsoft.com/en-ca/search/?terms=DLGITEMTEMPLATE), [google](https://www.google.com/search?q=DLGITEMTEMPLATE) or [google groups](https://groups.google.com/groups?q=DLGITEMTEMPLATE).

#### Items

- [0] string/int : windowClass

 The window class. If not a string, it must be in integer defining one of the built-in Windows controls. If a string, it must be a pre-registered windows class name, a built-in class, or the CLSID of an OLE controls. Built-in classes include:

| | Control Type | String Class Name
| |

---

 |

---

| | Check Box | Button
| | Combo Box | ComboBox
| | Command Button | Button
| | Header | SysHeader32
| | Label | Static
| | List Box | ListBox
SysListView32
| | Option Button | Button
| | Tab | SysTabControl32
| | Text Box | Edit
RICHEDIT
| | Tool Bar | ToolbarWindow32
| | Tool Tips | tooltips_class32
tooltips_class
| | Tree View | SysTreeView32 The built-in windows controls are:

| | Integer Value | Window Type
| |

---

 |

---

| | 0x0080 | Button
| | 0x0081 | Edit
| | 0x0082 | Static
| | 0x0083 | List box
| | 0x0084 | Scroll bar
| | 0x0085 | Combo box

- [1] PyUnicode : caption

 Caption for the control, or None

- [2] int : ID

 The child ID of this control. All children should have unique IDs. This ID can be used by PyCDialog::GetDlgItem to retrieve the actual control object at runtime.

- [3] (int,int,int,int) : (x,y,cx,cy)

 The bounding rectange for the control, relative to the upper left of the dialog, in dialog units.

- [4] int : style

 The window style of the control (WS_* constants). Depending on the type of control, other constants may also be valid (eg, BS_* for Button, ES_* for Edit controls, etc).

- [5] int : extStyle

 The extended style of the control.

- [6] buffer : extraData

 A byte string or buffer used as extra data for the control. The value depends on the control.


---

<!-- object: PyDLGTEMPLATE -->


<!-- page: PyDLGTEMPLATE.html -->

---

## PyDLGTEMPLATE Object

 A tuple of items describing a dialog box, that can be used to create the dialog.

#### Win32 API References

- Search for DLGTEMPLATE at [msdn](https://learn.microsoft.com/en-ca/search/?terms=DLGTEMPLATE), [google](https://www.google.com/search?q=DLGTEMPLATE) or [google groups](https://groups.google.com/groups?q=DLGTEMPLATE).

#### Items

- [0] string : caption

 The caption for the window

- [1] (int,int,int,int) : (x,y,cx,cy)

 The bounding rectange for the dialog.

- [2] int : style

 The style bits for the dialog. Combination of WS_* and DS_* constants. Note that the DS_SETFONT style need never be specified - it is determined by the font item (below)
See MSDN documentation on Dialog Boxes for allowable values.

- [3] int : extStyle

 The extended style bits for the dialog. Defaults to 0 if not passed and None is supported for backwards compatibility.

- [4] (int, string) : (fontSize, fontName)

 A tuple describing the font, or None if the system default font is to be used.

- [5] PyResourceId : menuResource

 The resource ID of the menu to be used for the dialog, or None for no menu.

- [6] PyResourceId : windowClass

 Window class name or atom as returned from RegisterWindowClass. Defaults to None.


---

<!-- object: PyDLL -->


<!-- page: PyDLL.html -->

---

## PyDLL Object

 A DLL object. A general utility object, and not associated with an MFC object.

#### Methods

- GetFileName

 Returns the file name of the DLL associated with the object.

- AttachToMFC

 Attaches the DLL to the internal list of MFC DLL's.


<!-- page: PyDLL__AttachToMFC_meth.html -->

## PyDLL.AttachToMFC

 AttachToMFC()

Attaches the DLL object to the MFC list of DLL's.

#### Comments

 After calling this method, MFC will search this DLL when looking for resources. A program can use this function once, instead of specifying the DLL in each call to load/find a resource.
In addition, this is the only way that an application can provide status bar messages and tool tips for custom control ID's in an external DLL.


<!-- page: PyDLL__GetFileName_meth.html -->

## PyDLL.GetFileName

 string = GetFileName()

Returns the name of the module associated with the DLL.

#### Comments

 Note that this is the name that Windows knows the DLL by, not necessarily the name that was specified!


<!-- page: PyDLL____repr___meth.html -->

## PyDLL.__repr__

 string = __repr__()

Returns the HINSTANCE and filename of the DLL.

#### Win32 API References

- Search for GetModuleFileName at [msdn](https://learn.microsoft.com/en-ca/search/?terms=GetModuleFileName), [google](https://www.google.com/search?q=GetModuleFileName) or [google groups](https://groups.google.com/groups?q=GetModuleFileName).


---

<!-- object: PyDSBCAPS -->


<!-- page: PyDSBCAPS.html -->

---

## PyDSBCAPS Object

 A Python object, representing a DSBCAPS structure

#### Properties

- integer dwFlags
 Flags that specify buffer-object capabilities.

| | Flag | Description
| |

---

 |

---

| | DSBCAPS_PRIMARYBUFFER | Indicates that the buffer is a primary sound buffer. If this value is not specified, a secondary sound buffer will be created.
| | DSBCAPS_STATIC | Indicates that the buffer will be used for static sound data. Typically, these buffers are loaded once and played many times. These buffers are candidates for hardware memory.
| | DSBCAPS_LOCHARDWARE | The buffer is in hardware memory and uses hardware mixing.
| | DSBCAPS_LOCSOFTWARE | The buffer is in software memory and uses software mixing.
| | DSBCAPS_CTRL3D | The buffer is either a primary buffer or a secondary buffer that uses 3-D control. To create a primary buffer, the dwFlags member of the DSBUFFERDESC structure should include the DSBCAPS_PRIMARYBUFFER flag.
| | DSBCAPS_CTRLFREQUENCY | The buffer must have frequency control capability.
| | DSBCAPS_CTRLPAN | The buffer must have pan control capability.
| | DSBCAPS_CTRLVOLUME | The buffer must have volume control capability.
| | DSBCAPS_CTRLPOSITIONNOTIFY | The buffer must have control position notify capability.
| | DSBCAPS_STICKYFOCUS | Changes the focus behavior of the sound buffer. This flag can be specified in an IDirectSound::CreateSoundBuffer call. With this flag set, an application using DirectSound can continue to play its sticky focus buffers if the user switches to another application not using DirectSound. In this situation, the application's normal buffers are muted, but the sticky focus buffers are still audible. This is useful for nongame applications, such as movie playback (DirectShow™), when the user wants to hear the soundtrack while typing in Microsoft Word or Microsoft® Excel, for example. However, if the user switches to another DirectSound application, all sound buffers, both normal and sticky focus, in the previous application are muted.
| | DSBCAPS_GLOBALFOCUS | The buffer is a global sound buffer. With this flag set, an application using DirectSound can continue to play its buffers if the user switches focus to another application, even if the new application uses DirectSound. The one exception is if you switch focus to a DirectSound application that uses the DSSCL_EXCLUSIVE or DSSCL_WRITEPRIMARY flag for its cooperative level. In this case, the global sounds from other applications will not be audible.
| | DSBCAPS_GETCURRENTPOSITION2 | Indicates that IDirectSoundBuffer::GetCurrentPosition should use the new behavior of the play cursor. In DirectSound in DirectX 1, the play cursor was significantly ahead of the actual playing sound on emulated sound cards; it was directly behind the write cursor. Now, if the DSBCAPS_GETCURRENTPOSITION2 flag is specified, the application can get a more accurate play position. If this flag is not specified, the old behavior is preserved for compatibility. Note that this flag affects only emulated sound cards; if a DirectSound driver is present, the play cursor is accurate for DirectSound in all versions of DirectX.
| | DSBCAPS_MUTE3DATMAXDISTANCE | The sound is reduced to silence at the maximum distance. The buffer will stop playing when the maximum distance is exceeded, so that processor time is not wasted.
- integer nChannels
 Size of the buffer, in bytes.

- integer dwUnlockTransferRate
 Specifies the rate, in kilobytes per second, at which data is transferred to the buffer memory when IDirectSoundBuffer::Unlock is called. High-performance applications can use this value to determine the time required for IDirectSoundBuffer::Unlock to execute. For software buffers located in system memory, the rate will be very high because no processing is required. For hardware buffers, the rate might be slower because the buffer might have to be downloaded to the sound card, which might have a limited transfer rate.

- integer nAvgBytesPerSec
 Specifies whether the returned handle is inherited when a new process is created. If this member is TRUE, the new process inherits the handle. Sentinel


---

<!-- object: PyDSBUFFERDESC -->


<!-- page: PyDSBUFFERDESC.html -->

---

## PyDSBUFFERDESC Object

 A Python object, representing a DSBUFFERDESC structure

#### Properties

- integer dwFlags
 Identifies the capabilities to include when creating a new DirectSoundBuffer object. Specify one or more of the following:

| | Flag | Description
| |

---

 |

---

| | DSBCAPS_PRIMARYBUFFER | Indicates that the buffer is a primary sound buffer. If this value is not specified, a secondary sound buffer will be created.
| | DSBCAPS_STATIC | Indicates that the buffer will be used for static sound data. Typically, these buffers are loaded once and played many times. These buffers are candidates for hardware memory.
| | DSBCAPS_LOCHARDWARE | The buffer is in hardware memory and uses hardware mixing.
| | DSBCAPS_LOCSOFTWARE | The buffer is in software memory and uses software mixing.
| | DSBCAPS_CTRL3D | The buffer is either a primary buffer or a secondary buffer that uses 3-D control. To create a primary buffer, the dwFlags member of the DSBUFFERDESC structure should include the DSBCAPS_PRIMARYBUFFER flag.
| | DSBCAPS_CTRLFREQUENCY | The buffer must have frequency control capability.
| | DSBCAPS_CTRLPAN | The buffer must have pan control capability.
| | DSBCAPS_CTRLVOLUME | The buffer must have volume control capability.
| | DSBCAPS_CTRLPOSITIONNOTIFY | The buffer must have control position notify capability.
| | DSBCAPS_STICKYFOCUS | Changes the focus behavior of the sound buffer. This flag can be specified in an IDirectSound::CreateSoundBuffer call. With this flag set, an application using DirectSound can continue to play its sticky focus buffers if the user switches to another application not using DirectSound. In this situation, the application's normal buffers are muted, but the sticky focus buffers are still audible. This is useful for nongame applications, such as movie playback (DirectShow™), when the user wants to hear the soundtrack while typing in Microsoft Word or Microsoft® Excel, for example. However, if the user switches to another DirectSound application, all sound buffers, both normal and sticky focus, in the previous application are muted.
| | DSBCAPS_GLOBALFOCUS | The buffer is a global sound buffer. With this flag set, an application using DirectSound can continue to play its buffers if the user switches focus to another application, even if the new application uses DirectSound. The one exception is if you switch focus to a DirectSound application that uses the DSSCL_EXCLUSIVE or DSSCL_WRITEPRIMARY flag for its cooperative level. In this case, the global sounds from other applications will not be audible.
| | DSBCAPS_GETCURRENTPOSITION2 | Indicates that IDirectSoundBuffer::GetCurrentPosition should use the new behavior of the play cursor. In DirectSound in DirectX 1, the play cursor was significantly ahead of the actual playing sound on emulated sound cards; it was directly behind the write cursor. Now, if the DSBCAPS_GETCURRENTPOSITION2 flag is specified, the application can get a more accurate play position. If this flag is not specified, the old behavior is preserved for compatibility. Note that this flag affects only emulated sound cards; if a DirectSound driver is present, the play cursor is accurate for DirectSound in all versions of DirectX.
| | DSBCAPS_MUTE3DATMAXDISTANCE | The sound is reduced to silence at the maximum distance. The buffer will stop playing when the maximum distance is exceeded, so that processor time is not wasted.
- integer dwBufferBytes
 Size of the new buffer, in bytes. This value must be 0 when creating primary buffers. For secondary buffers, the minimum and maximum sizes allowed are specified by DSBSIZE_MIN and DSBSIZE_MAX.

- WAVEFORMATEX lpwfxFormat
 Structure specifying the waveform format for the buffer. This value must be None for primary buffers. The application can use IDirectSoundBuffer::SetFormat to set the format of the primary buffer. Sentinel


---

<!-- object: PyDSCAPS -->


<!-- page: PyDSCAPS.html -->

---

## PyDSCAPS Object

 A Python object, representing a DSCAPS structure

#### Properties

- integer dwFlags
 Specifies device capabilities. Can be one or more of the following:

| | Flag | Description
| |

---

 |

---

| | DSCAPS_PRIMARYMONO | The device supports monophonic primary buffers.
| | DSCAPS_PRIMARYSTEREO | The device supports stereo primary buffers.
| | DSCAPS_PRIMARY8BIT | The device supports hardware-mixed secondary buffers with 8-bit samples.
| | DSCAPS_PRIMARY16BIT | The device supports primary sound buffers with 16-bit samples.
| | DSCAPS_CONTINUOUSRATE | The device supports all sample rates between the dwMinSecondarySampleRate and dwMaxSecondarySampleRate member values. Typically, this means that the actual output rate will be within +/- 10 hertz (Hz) of the requested frequency.
| | DSCAPS_EMULDRIVER | The device does not have a DirectSound driver installed, so it is being emulated through the waveform-audio functions. Performance degradation should be expected.
| | DSCAPS_CERTIFIED | This driver has been tested and certified by Microsoft.
| | DSCAPS_SECONDARYMONO | The device supports hardware-mixed monophonic secondary buffers.
| | DSCAPS_SECONDARYSTEREO | The device supports hardware-mixed stereo secondary buffers.
| | DSCAPS_SECONDARY8BIT | The device supports hardware-mixed secondary buffers with 8-bit samples.
| | DSCAPS_SECONDARY16BIT | The device supports hardware-mixed secondary sound buffers with 16-bit samples.
- integer dwMinSecondarySampleRate
 Minimum sample rate supported by this device's hardware secondary sound buffers.

- integer dwMaxSecondarySampleRate
 Maximum sample rate supported by this device's hardware secondary sound buffers.

- integer dwPrimaryBuffers
 Number of primary buffers supported. This value will always be 1.

- integer dwMaxHwMixingAllBuffers
 Specifies the total number of buffers that can be mixed in hardware. This member can be less than the sum of dwMaxHwMixingStaticBuffers and dwMaxHwMixingStreamingBuffers. Resource tradeoffs frequently occur.

- integer dwMaxHwMixingStaticBuffers
 Specifies the maximum number of static sound buffers.

- integer dwMaxHwMixingStreamingBuffers
 Specifies the maximum number of streaming sound buffers.

- integer dwFreeHwMixingAllBuffers
 Description of the free hardware mixing capabilities of the device. An application can use this value to determine whether hardware resources are available for allocation to a secondary sound buffer. Also, by comparing these values to the members that specify maximum mixing capabilities, the resources that are already allocated can be determined.

- integer dwFreeHwMixingStaticBuffers
 Description of the free hardware mixing capabilities of the device. An application can use this value to determine whether hardware resources are available for allocation to a secondary sound buffer. Also, by comparing these values to the members that specify maximum mixing capabilities, the resources that are already allocated can be determined.

- integer dwFreeHwMixingStreamingBuffers
 Description of the free hardware mixing capabilities of the device. An application can use this value to determine whether hardware resources are available for allocation to a secondary sound buffer. Also, by comparing these values to the members that specify maximum mixing capabilities, the resources that are already allocated can be determined.

- integer dwMaxHw3DAllBuffers
 Description of the hardware 3-D positional capabilities of the device.

- integer dwMaxHw3DStaticBuffers
 Description of the hardware 3-D positional capabilities of the device.

- integer dwMaxHw3DStreamingBuffers
 Description of the hardware 3-D positional capabilities of the device.

- integer dwFreeHw3DAllBuffers
 Description of the free, or unallocated, hardware 3-D positional capabilities of the device.

- integer dwFreeHw3DStaticBuffers
 Description of the free, or unallocated, hardware 3-D positional capabilities of the device.

- integer dwFreeHw3DStreamingBuffers
 Description of the free, or unallocated, hardware 3-D positional capabilities of the device.

- integer dwTotalHwMemBytes
 Size, in bytes, of the amount of memory on the sound card that stores static sound buffers.

- integer dwFreeHwMemBytes
 Size, in bytes, of the free memory on the sound card.

- integer dwMaxContigFreeHwMemBytes
 Size, in bytes, of the largest contiguous block of free memory on the sound card.

- integer dwUnlockTransferRateHwBuffers
 Description of the rate, in kilobytes per second, at which data can be transferred to hardware static sound buffers. This and the number of bytes transferred determines the duration of a call to the IDirectSoundBuffer::Update method.

- integer dwPlayCpuOverheadSwBuffers
 Description of the processing overhead, as a percentage of the central processing unit, needed to mix software buffers (those located in main system memory). This varies according to the bus type, the processor type, and the clock speed. The unlock transfer rate for software buffers is 0 because the data need not be transferred anywhere. Similarly, the play processing overhead for hardware buffers is 0 because the mixing is done by the sound device.


---

<!-- object: PyDSCBCAPS -->


<!-- page: PyDSCBCAPS.html -->

---

## PyDSCBCAPS Object

 A Python object, representing a DSCBCAPS structure

#### Properties

- integer dwFlags
 Specifies device capabilities. Can be 0 or DSCBCAPS_EMULDRIVER (indicates that no DirectSound Device is available and standard wave audio functions are being used).

- integer dwBufferBytes
 The size, in bytes, of the capture buffer.


---

<!-- object: PyDSCBUFFERDESC -->


<!-- page: PyDSCBUFFERDESC.html -->

---

## PyDSCBUFFERDESC Object

 A Python object, representing a DSCBUFFERDESC structure

#### Properties

- integer dwFlags
 Identifies the capabilities to include when creating a new DirectSoundBuffer object. Can be zero or the following flag:

| | Flag | Description
| |

---

 |

---

| | DSCBCAPS_WAVEMAPPED | The Win32 wave mapper will be used for formats not supported by the device.
- integer dwBufferBytes
 Size of the new buffer, in bytes. This value must be 0 when creating primary buffers. For secondary buffers, the minimum and maximum sizes allowed are specified by DSBSIZE_MIN and DSBSIZE_MAX.

- WAVEFORMATEX lpwfxFormat
 Structure specifying the waveform format for the buffer. This value must be None for primary buffers. The application can use IDirectSoundBuffer::SetFormat to set the format of the primary buffer. Sentinel


---

<!-- object: PyDSCCAPS -->


<!-- page: PyDSCCAPS.html -->

---

## PyDSCCAPS Object

 A Python object, representing a DSCCAPS structure

#### Properties

- integer dwFlags
 Specifies device capabilities. Can be zero or the following flag:

| | Flag | Description
| |

---

 |

---

| | DSCCAPS_EMULDRIVER | Indicates that no DirectSound Device is available and standard wave audio functions are being used.
- integer dwFormats
 Bitset of supported WAVE_FORMAT formats.

- integer dwChannels
 Number of channels supported by the device.


---

<!-- object: PyDSOP_FILTER_FLAGS -->


<!-- page: PyDSOP_FILTER_FLAGS.html -->

---

## PyDSOP_FILTER_FLAGS Object

 An object representing an ActiveDirectory DSOP_FILTER_FLAGS structure
These objects can only be accessed via a PyDSOP_SCOPE_INIT_INFO object.

#### Properties

- PyDSOP_UPLEVEL_FILTER_FLAGS uplevel

- int downlevel


---

<!-- object: PyDSOP_SCOPE_INIT_INFO -->


<!-- page: PyDSOP_SCOPE_INIT_INFO.html -->

---

## PyDSOP_SCOPE_INIT_INFO Object

 An object representing an ActiveDirectory DSOP_SCOPE_INIT_INFO structure.
These objects can only be accessed by indexing a PyDSOP_SCOPE_INIT_INFOs object.

#### Properties

- int type

- int scope

- int hr

- PyUnicode dcName

- PyDSOP_FILTER_FLAGS filterFlags


---

<!-- object: PyDSOP_SCOPE_INIT_INFOs -->


<!-- page: PyDSOP_SCOPE_INIT_INFOs.html -->

---

## PyDSOP_SCOPE_INIT_INFOs Object

 An object representing an array of PyDSOP_SCOPE_INIT_INFO objects

#### Comments

 You must pass the number of items in the array to the constructor. Once set, this can not be changed. You can index the index (eg, ob[2]). The object has no other (interesting) methods or attributes.
These objects are created via adsi::DSOP_SCOPE_INIT_INFOs(size)


---

<!-- object: PyDSOP_UPLEVEL_FILTER_FLAGS -->


<!-- page: PyDSOP_UPLEVEL_FILTER_FLAGS.html -->

---

## PyDSOP_UPLEVEL_FILTER_FLAGS Object

 An object representing an ActiveDirectory DSOP_UPLEVEL_FILTER_FLAGS structure.
These objects can only be accessed via a PyDSOP_FILTER_FLAGS object.

#### Properties

- int bothModes

- int mixedModeOnly

- int nativeModeOnly


---

<!-- object: PyDS_HANDLE -->


<!-- page: PyDS_HANDLE.html -->

---

## PyDS_HANDLE Object

 Directory service handle, returned by win32security::DsBind Subtype of PyHANDLE, inherits all properties and methods.
 When closed, DsUnBind is called.


---

<!-- object: PyDS_NAME_RESULT_ITEM -->


<!-- page: PyDS_NAME_RESULT_ITEM.html -->

---

## PyDS_NAME_RESULT_ITEM Object

 A tuple representing a DS_NAME_RESULT_ITEM

#### Items

- [0] int : status

 One of ntsecuritycon.DS_NAME_* error codes

- [1] PyUnicode : Domain

 Dns domain that object belongs to

- [2] PyUnicode : Name

 Formatted object name


---

<!-- object: PyDateTime -->


<!-- page: PyDateTime.html -->

---

## PyDateTime Object

 A Python object, representing an instant in time.

#### Comments

 PyDateTime is a sub-class of the regular datetime.datetime object. It is subclassed so it can provide a somewhat backwards compatible PyDateTime::Format method, but is otherwise identical. Functions accepting a PyDateTime object also accept a datetime.datetime object. A PyDateTime object can be created via pywintypes::Time.

 Migration note: pywin32 builds for Python 2 used an (incompatible) PyTime object instad of datetime.

#### Methods

- Format

 Formats the time value - an alias for strftime with a default param.


<!-- page: PyDateTime__Format_meth.html -->

## PyDateTime.Format

 str = Format()

#### Comments

 This method is an alias for the datetime strftime method, using %c as the default value for the format string.


---

<!-- object: PyDialogTemplate -->


<!-- page: PyDialogTemplate.html -->

---

## PyDialogTemplate Object

 Sequence of items defining a dialog. The first item is a PyDLGTEMPLATE describing the dialog, followed by zero or more PyDLGITEMTEMPLATEs describing controls within the dialog.


---

<!-- object: PyEVTLOG_HANDLE -->


<!-- page: PyEVTLOG_HANDLE.html -->

---

## PyEVTLOG_HANDLE Object

 Object representing a handle to the windows event log. Identical to PyHANDLE, but calls CloseEventLog() on destruction


---

<!-- object: PyEVT_HANDLE -->


<!-- page: PyEVT_HANDLE.html -->

---

## PyEVT_HANDLE Object

 Handle to an event log, session, query, or any other object used with the Evt* event log functions. When the object is destroyed, EvtClose is called.


---

<!-- object: PyEVT_RPC_LOGIN -->


<!-- page: PyEVT_RPC_LOGIN.html -->

---

## PyEVT_RPC_LOGIN Object

 Tuple containing login credentials for a remote Event Log connection

#### Comments

 To use current login credentials, pass None for User, Domain, and Password

#### Items

- [0] string : Server

 Machine to connect to (only required item)

- [1] string : User

 User account to login with, defaults to None

- [2] string : Domain

 Domain of account, defaults to None

- [3] string : Password

 Password, defaults to None

- [4] int : Flags

 Type of authentication, EvtRpcLogin*. Default is EvtRpcLoginAuthDefault


---

<!-- object: PyEventLogRecord -->


<!-- page: PyEventLogRecord.html -->

---

## PyEventLogRecord Object

 An object containing the data in an EVENTLOGRECORD.

#### Properties

- integer Reserved

- integer RecordNumber

- PyDateTime TimeGenerated

- PyDateTime TimeWritten

- integer EventID

- integer EventType

- integer EventCategory

- integer ReservedFlags

- integer ClosingRecordNumber

- PyUnicode SourceName

- (PyUnicode ,...) StringInserts

- PySID Sid

- string Data

- PyUnicode ComputerName


---

<!-- object: PyFORMATETC -->


<!-- page: PyFORMATETC.html -->

---

## PyFORMATETC Object

 Tuple representing a FORMATETC struct describing an OLE data format

#### Items

- [0] int : Format

 CLIPFORMAT value (CF_*) identifying the type of data

- [1] None : td

 DVTARGETDEVICE (currently not supported, use only None)

- [2] int : Aspect

 One of pythoncom.DVASPECT_* values specifying level of detail

- [3] int : index

 Usually -1, used only when data spans multiple pages

- [4] int : tymed

 One of pythoncom.TYMED_* values indicating how the data is stored


---

<!-- object: PyGFileOperationProgressSink -->


<!-- page: PyGFileOperationProgressSink.html -->

---

## PyGFileOperationProgressSink Object

 Implement-only gateway for IFileOperationProgressSink, used to receive events from a PyIFileOperation object.
To abort the operation, an implementation of any method can raise a com_error with an appropriate HRESULT.

#### Methods

- StartOperations

 Called as operation begins, before any modifications are done

- FinishOperations

 Called after all actions have been performed

- PreRenameItem

 Called before each file rename

- PostRenameItem

 Called after each file rename

- PreMoveItem

 Called before each move operation

- PostMoveItem

 Called after each move operation

- PreCopyItem

 Called before each copy operation

- PostCopyItem

 Called after each copy operation

- PreDeleteItem

 Called before each delete operation

- PostDeleteItem

 Called after each delete operation

- PreNewItem

 Called before each new file is created

- PostNewItem

 Called after each new file is created

- UpdateProgress

 Gives an estimate of total work completed

- ResetTimer

 Not implemented, according to MSDN

- PauseTimer

 Not implemented, according to MSDN

- ResumeTimer

 Not implemented, according to MSDN


<!-- page: PyGFileOperationProgressSink__FinishOperations_meth.html -->

## PyGFileOperationProgressSink.FinishOperations

 FinishOperations(Result)

Called after all actions have been performed

#### Parameters

- Result : int

 HRESULT of last operation performed


<!-- page: PyGFileOperationProgressSink__PauseTimer_meth.html -->

## PyGFileOperationProgressSink.PauseTimer

 PauseTimer()

Not implemented, according to MSDN


<!-- page: PyGFileOperationProgressSink__PostCopyItem_meth.html -->

## PyGFileOperationProgressSink.PostCopyItem

 PostCopyItem(Flags, Item, DestinationFolder, NewName, hrCopy, NewlyCreated)

Called after each copy operation

#### Parameters

- Flags : int

 Flags specifying copy behaviour, combination of shellcon.TSF_* flags

- Item : PyIShellItem

 The original item

- DestinationFolder : PyIShellItem

 Folder into which it was copied

- NewName : str

 Name of item after copy, may be mangled in case of name conflict

- hrCopy : int

 HRESULT of the copy operation

- NewlyCreated : PyIShellItem

 Shell interface of the copy


<!-- page: PyGFileOperationProgressSink__PostDeleteItem_meth.html -->

## PyGFileOperationProgressSink.PostDeleteItem

 PostDeleteItem(Flags, Item, hrDelete, NewlyCreated)

Called after each delete operation

#### Parameters

- Flags : int

 Flags specifying delete behaviour, combination of shellcon.TSF_* flags

- Item : PyIShellItem

 Item that was deleted

- hrDelete : int

 HRESULT of the delete operation

- NewlyCreated : PyIShellItem

 Item in the recycle bin, or None if deleted without recycling


<!-- page: PyGFileOperationProgressSink__PostMoveItem_meth.html -->

## PyGFileOperationProgressSink.PostMoveItem

 PostMoveItem(Flags, Item, DestinationFolder, NewName, hrMove, NewlyCreated)

Called after each move operation

#### Parameters

- Flags : int

 Flags specifying move behaviour, combination of shellcon.TSF_* flags

- Item : PyIShellItem

 Interface of the item before it was moved

- DestinationFolder : PyIShellItem

 The folder into which it was moved

- NewName : str

 Name of item in its new location, may be mangled in case of conflict

- hrMove : int

 HRESULT of the move operation

- NewlyCreated : PyIShellItem

 Shell interface of the item in its new location


<!-- page: PyGFileOperationProgressSink__PostNewItem_meth.html -->

## PyGFileOperationProgressSink.PostNewItem

 PostNewItem(Flags, DestinationFolder, NewName, TemplateName, FileAttributes, hrNew, NewItem)

Called after each new file is created

#### Parameters

- Flags : int

 Flags specifying creation behaviour, combination of shellcon.TSF_* flags

- DestinationFolder : PyIShellItem

 Folder in which item was created

- NewName : str

 Name of created item, may be mangled if file name conflicts occurred

- TemplateName : str

 Template file used to initialize new item

- FileAttributes : int

 File attributes of new item

- hrNew : int

 HRESULT of the create operation

- NewItem : PyIShellItem

 Shell interface of created item


<!-- page: PyGFileOperationProgressSink__PostRenameItem_meth.html -->

## PyGFileOperationProgressSink.PostRenameItem

 PostRenameItem(Flags, Item, NewName, hrRename, NewlyCreated)

Called after each file rename

#### Parameters

- Flags : int

 Flags specifying rename behaviour, combination of shellcon.TSF_* flags

- Item : PyIShellItem

 Shell interface of item before rename

- NewName : str

 The new name of the item, may be mangled to resolve filename conflicts

- hrRename : int

 HRESULT of the rename operation

- NewlyCreated : PyIShellItem

 Shell interface of the item after rename


<!-- page: PyGFileOperationProgressSink__PreCopyItem_meth.html -->

## PyGFileOperationProgressSink.PreCopyItem

 PreCopyItem(Flags, Item, DestinationFolder, NewName)

Called before each copy operation

#### Parameters

- Flags : int

 Flags specifying copy behaviour, combination of shellcon.TSF_* flags

- Item : PyIShellItem

 The item to be copied

- DestinationFolder : PyIShellItem

 Folder into which it will be copied

- NewName : str

 Name to be given to the copy, will be None if keeping original name


<!-- page: PyGFileOperationProgressSink__PreDeleteItem_meth.html -->

## PyGFileOperationProgressSink.PreDeleteItem

 PreDeleteItem(Flags, Item)

Called before each delete operation

#### Parameters

- Flags : int

 Flags specifying delete behaviour, combination of shellcon.TSF_* flags

- Item : PyIShellItem

 Item to be deleted


<!-- page: PyGFileOperationProgressSink__PreMoveItem_meth.html -->

## PyGFileOperationProgressSink.PreMoveItem

 PreMoveItem(Flags, Item, DestinationFolder, NewName)

Called before each move operation

#### Parameters

- Flags : int

 Flags specifying move behaviour, combination of shellcon.TSF_* flags

- Item : PyIShellItem

 The item to be moved

- DestinationFolder : PyIShellItem

 The folder into which it will be moved

- NewName : str

 Name of moved item, may be None if not to be changed


<!-- page: PyGFileOperationProgressSink__PreNewItem_meth.html -->

## PyGFileOperationProgressSink.PreNewItem

 PreNewItem(Flags, DestinationFolder, NewName)

Called before each new file is created

#### Parameters

- Flags : int

 Flags specifying creation behaviour, combination of shellcon.TSF_* flags

- DestinationFolder : PyIShellItem

 Folder where item will be created

- NewName : str

 Name of item to be created


<!-- page: PyGFileOperationProgressSink__PreRenameItem_meth.html -->

## PyGFileOperationProgressSink.PreRenameItem

 PreRenameItem(Flags, Item, NewName)

Called before each file rename

#### Parameters

- Flags : int

 Flags specifying copy behaviour, combination of shellcon.TSF_* flags

- Item : PyIShellItem

 Shell interface of the copied item

- NewName : str

 New display name of the item


<!-- page: PyGFileOperationProgressSink__ResetTimer_meth.html -->

## PyGFileOperationProgressSink.ResetTimer

 ResetTimer()

Not implemented, according to MSDN


<!-- page: PyGFileOperationProgressSink__ResumeTimer_meth.html -->

## PyGFileOperationProgressSink.ResumeTimer

 ResumeTimer()

Not implemented, according to MSDN


<!-- page: PyGFileOperationProgressSink__StartOperations_meth.html -->

## PyGFileOperationProgressSink.StartOperations

 StartOperations()

Called as operation begins, before any modifications are done


<!-- page: PyGFileOperationProgressSink__UpdateProgress_meth.html -->

## PyGFileOperationProgressSink.UpdateProgress

 UpdateProgress(WorkTotal, WorkSoFar)

Gives an estimate of total work completed

#### Parameters

- WorkTotal : int

 Undimensioned number representing total amount of work

- WorkSoFar : int

 Undimensioned number representing amount already completed


---

<!-- object: PyGROUP_INFO_.2a -->


<!-- page: PyGROUP_INFO_.2a.html -->

---

## PyGROUP_INFO_* Object

 The following GROUP_INFO levels are supported.

| | Level | Data
| |

---

 |

---

| | 0 | PyGROUP_INFO_0
| | 1 | PyGROUP_INFO_1
| | 2 | PyGROUP_INFO_2
| | 1002 | PyGROUP_INFO_1002
| | 1005 | PyGROUP_INFO_1005


---

<!-- object: PyGROUP_INFO_0 -->


<!-- page: PyGROUP_INFO_0.html -->

---

## PyGROUP_INFO_0 Object

 A dictionary holding the information in a Win32 GROUP_INFO_0 structure.

#### Properties

- string/PyUnicode name
 Name of the group


---

<!-- object: PyGROUP_INFO_1 -->


<!-- page: PyGROUP_INFO_1.html -->

---

## PyGROUP_INFO_1 Object

 A dictionary holding the information in a Win32 GROUP_INFO_1 structure.

#### Properties

- string/PyUnicode name
 Name of the group

- string/PyUnicode comment
 The group's comment.


---

<!-- object: PyGROUP_INFO_1002 -->


<!-- page: PyGROUP_INFO_1002.html -->

---

## PyGROUP_INFO_1002 Object

 A dictionary holding the information in a Win32 GROUP_INFO_1002 structure.

#### Properties

- string/PyUnicode comment


---

<!-- object: PyGROUP_INFO_1005 -->


<!-- page: PyGROUP_INFO_1005.html -->

---

## PyGROUP_INFO_1005 Object

 A dictionary holding the information in a Win32 GROUP_INFO_1005 structure.

#### Properties

- int attributes


---

<!-- object: PyGROUP_INFO_2 -->


<!-- page: PyGROUP_INFO_2.html -->

---

## PyGROUP_INFO_2 Object

 A dictionary holding the information in a Win32 GROUP_INFO_2 structure.

#### Properties

- string/PyUnicode name
 Name of the group

- string/PyUnicode comment
 The group's comment.

- int group_id

- int attributes


---

<!-- object: PyGROUP_USERS_INFO_.2a -->


<!-- page: PyGROUP_USERS_INFO_.2a.html -->

---

## PyGROUP_USERS_INFO_* Object

 The following GROUP_USERS_INFO levels are supported.

| | Level | Data
| |

---

 |

---

| | 0 | PyGROUP_USERS_INFO_0
| | 1 | PyGROUP_USERS_INFO_1


---

<!-- object: PyGROUP_USERS_INFO_0 -->


<!-- page: PyGROUP_USERS_INFO_0.html -->

---

## PyGROUP_USERS_INFO_0 Object

 A dictionary holding the information in a Win32 GROUP_USERS_INFO_0 structure.

#### Properties

- string/PyUnicode name
 Name of the group or user


---

<!-- object: PyGROUP_USERS_INFO_1 -->


<!-- page: PyGROUP_USERS_INFO_1.html -->

---

## PyGROUP_USERS_INFO_1 Object

 A dictionary holding the information in a Win32 GROUP_USERS_INFO_1 structure.

#### Properties

- string/PyUnicode name
 Name of the group or user

- int attributes


---

<!-- object: PyGSecurityInformation -->


<!-- page: PyGSecurityInformation.html -->

---

## PyGSecurityInformation Object

 Gateway wrapper for the implement-only ISecurityInformation interface

#### Methods

- GetObjectInformation

 Returns information identifying the object

- GetSecurity

 Requests the object's current security descriptor

- SetSecurity

 Applies the modified security information to the object

- GetAccessRights

 Requests the permission flags that will be available for user to set

- MapGeneric

 Translates generic permission flags into specific flags

- GetInheritTypes

 Retrieves inheritance flags that will be shown in dialog for containers

- PropertySheetPageCallback

 Invoked each time a property sheet page is created or destroyed


<!-- page: PyGSecurityInformation__GetAccessRights_meth.html -->

## PyGSecurityInformation.GetAccessRights

 ((SI_ACCESS,...) int) = GetAccessRights(ObjectType, Flags )

Retrieves permission that can be set

#### Parameters

- ObjectType : PyIID

 GUID representing type of object, may be None

- Flags : int

 Indicates which page is requesting the access rights (SI_ADVANCED, SI_EDIT_AUDITS, SI_EDIT_PROPERTIES)

#### Return Value

This method should return a 2-tuple containing a sequence of SI_ACCESS tuples, and a zero-based index indicating which of them is the default


<!-- page: PyGSecurityInformation__GetInheritTypes_meth.html -->

## PyGSecurityInformation.GetInheritTypes

 (SI_INHERIT_TYPE,...) = GetInheritTypes()

Requests types of inheritance that your implementation supports

#### Return Value

Returns a sequence of SI_INHERIT_TYPE tuples


<!-- page: PyGSecurityInformation__GetObjectInformation_meth.html -->

## PyGSecurityInformation.GetObjectInformation

 SI_OBJECT_INFO = GetObjectInformation()

Returns information identifying the object whose security is to be editted, and which pages are to appear in the property sheet

#### Comments

 Due to peculiarities of the underlying system calls, this method will only be called once, and subsequent calls will return the information obtained on the first call. As a consequence, a new instance of the interface will need to be created for each object whose security is to be displayed.

#### Return Value

Your implementation of this method should return a SI_OBJECT_INFO tuple


<!-- page: PyGSecurityInformation__GetSecurity_meth.html -->

## PyGSecurityInformation.GetSecurity

 PySECURITY_DESCRIPTOR = GetSecurity(RequestedInformation, Default )

Retrieves the object's current security settings

#### Parameters

- RequestedInformation : int

 Combination of SECURITY_INFORMATION flags indicating which components of the object's security descriptor you should return

- Default : bool

 If true, return a default security descriptor rather than current security. (invoked when 'Reset' button is clicked)


<!-- page: PyGSecurityInformation__MapGeneric_meth.html -->

## PyGSecurityInformation.MapGeneric

 int = MapGeneric(ObjectType, AceFlags , Mask )

Translates generic access rights to specific equivalents

#### Parameters

- ObjectType : PyIID

 Type of object that permissions apply to, None or GUID_NULL indicates object itself

- AceFlags : int

 Flags from the ACE that contains the permissions

- Mask : int

 Bitmask containing access rights

#### Comments

 See win32security::MapGenericMask

#### Return Value

This method should return the input bitmask will all generic rights mapped to specific rights


<!-- page: PyGSecurityInformation__PropertySheetPageCallback_meth.html -->

## PyGSecurityInformation.PropertySheetPageCallback

 PropertySheetPageCallback(hwnd, Msg, Page)

Called by each page as it is created and destroyed

#### Parameters

- hwnd : int

 Handle to the window for the page

- Msg : int

 Flag indicating type of event, one of PSPCB_CREATE,PSPCB_RELEASE,PSPCB_SI_INITDIALOG

- Page : int

 SI_PAGE_TYPE value indicating which page is making the call (ntsecuritycon.SI_PAGE_*)

#### Return Value

Any returned value will be ignored


<!-- page: PyGSecurityInformation__SetSecurity_meth.html -->

## PyGSecurityInformation.SetSecurity

 SetSecurity(SecurityInformation, SecurityDescriptor)

Applies the modified security to the object

#### Parameters

- SecurityInformation : int

 SECURITY_INFORMATION flags specifying which types of security information are to be applied

- SecurityDescriptor : PySECURITY_DESCRIPTOR

 The security information to be applied to the object

#### Return Value

Any returned value is ignored


---

<!-- object: PyGdiHANDLE -->


<!-- page: PyGdiHANDLE.html -->

---

## PyGdiHANDLE Object

 Gdi objects such as brush (HBRUSH), pen (HPEN), font (HFONT), region (HRGN), bitmap (HBITMAP) On destruction, the handle is closed using DeleteObject. The object's Close() method also calls DeleteObject. The gdi object should be deselected from any DC that it is selected into before it's closed. Inherits the methods and properties of PyHANDLE.


---

<!-- object: PyGetSignerCertificate -->


<!-- page: PyGetSignerCertificate.html -->

---

## PyGetSignerCertificate Object

 Callback used with CRYPT_VERIFY_MESSAGE_PARA to locate a certficate by issuer and serial nbr. This function will receive 4 args: 1. Arbitrary context object given as GetArg in CRYPT_VERIFY_MESSAGE_PARA 2. CertEncodingType (int) - specifies the type of encoding used 3. SignerId - Dict containing issuer and serial nbr that uniquely identifies a certificate 4. PyCERTSTORE containing certificates extracted from the message Function must return a PyCERT_CONTEXT. If no certificate could be found, it should raise pywintypes.error(winerror.CRYPT_E_NO_MATCH) If this function is not specified, the default action is to locate a certificate encoded in the message.


---

<!-- object: PyHANDLE -->


<!-- page: PyHANDLE.html -->

---

## PyHANDLE Object

 A Python object, representing a win32 HANDLE.

#### Comments

 This object wraps a win32 HANDLE object, automatically closing it when the object is destroyed. To guarantee cleanup, you can call either PyHANDLE::Close, or win32api::CloseHandle.
Most functions which accept a handle object also accept an integer - however, use of the handle object is encouraged.

#### Properties

- long handle
 Integer value of the handle

#### Methods

- Close

 Closes the handle

- close

 Synonym for PyHANDLE::Close

- Detach

 Detaches the Win32 handle from the handle object.

- __bool__

 Used for detecting true/false. is nb_bool in Python 3.0

- __int__

 Used when an integer representation of the handle object is required.

- __hash__

 Used when the hash value of an object is required tp_hash

- __str__

 Used when a string representation is required tp_str


<!-- page: PyHANDLE__Close_meth.html -->

## PyHANDLE.Close

 Close()

Closes the underlying Win32 handle.

#### Comments

 If the handle is already closed, no error is raised.


<!-- page: PyHANDLE__Detach_meth.html -->

## PyHANDLE.Detach

 int = Detach()

Detaches the Win32 handle from the handle object.

#### Comments

 After calling this function, the handle is effectively invalidated, but the handle is not closed. You would call this function when you need the underlying win32 handle to exist beyond the lifetime of the handle object.

#### Return Value

The result is the value of the handle before it is detached. If the handle is already detached, this will return zero.


<!-- page: PyHANDLE____bool___meth.html -->

## PyHANDLE.__bool__

 __bool__()

Used for detecting true/false.

#### Return Value

The result is 1 if the attached handle is non zero, else 0. static*/ int PyHANDLE::nonzeroFunc(PyObject *ob) { return ((PyHANDLE *)ob)->m_handle != 0; }


<!-- page: PyHANDLE____hash___meth.html -->

## PyHANDLE.__hash__

 int = __hash__()

Used when the hash value of a HANDLE object is required


<!-- page: PyHANDLE____int___meth.html -->

## PyHANDLE.__int__

 __int__()

Used when the handle as an integer is required.

#### Comments

 To get the underling win32 handle from a PyHANDLE object, use int(handleObject)


<!-- page: PyHANDLE____print___meth.html -->

## PyHANDLE.__print__

 __print__()

Used when the HANDLE object is printed.


<!-- page: PyHANDLE____str___meth.html -->

## PyHANDLE.__str__

 __str__()

Used when a string representation of the handle object is required.


---

<!-- object: PyHDESK -->


<!-- page: PyHDESK.html -->

---

## PyHDESK Object

 Object representing a handle to a desktop, created by win32service::CreateDesktop, win32service::GetThreadDesktop and win32service::OpenDesktop.

#### Methods

- SetThreadDesktop

 Assigns desktop to calling thread

- EnumDesktopWindows

 Lists all top-level windows on the desktop

- SwitchDesktop

 Activates the desktop

- CloseDesktop

 Closes the desktop handle

- Detach

 Releases reference to handle without closing it


<!-- page: PyHDESK__CloseDesktop_meth.html -->

## PyHDESK.CloseDesktop

 CloseDesktop()

Closes the desktop handle


<!-- page: PyHDESK__EnumDesktopWindows_meth.html -->

## PyHDESK.EnumDesktopWindows

 (PyHANDLE,...) = EnumDesktopWindows()

Returns a list of handles to all top-level windows on desktop


<!-- page: PyHDESK__SetThreadDesktop_meth.html -->

## PyHDESK.SetThreadDesktop

 SetThreadDesktop()

Assigns this desktop to the calling thread


<!-- page: PyHDESK__SwitchDesktop_meth.html -->

## PyHDESK.SwitchDesktop

 SwitchDesktop()

Activates the desktop


---

<!-- object: PyHDEVNOTIFY -->


<!-- page: PyHDEVNOTIFY.html -->

---

## PyHDEVNOTIFY Object

 A handle returned by RegisterDeviceNotifications which automatically calls UnregisterDeviceNotification on destruction. Inherits the methods and properties of PyHANDLE.


---

<!-- object: PyHHNTRACK -->


<!-- page: PyHHNTRACK.html -->

---

## PyHHNTRACK Object

 A Python object, representing an HHNTRACK structure

#### Comments

 Typically you create a PyHHNTRACK (via win32help::HHNTRACK) object, and set its properties. The object can then be passed to any function which takes an HHNTRACK object.

 This structure returns the file name of the current topic and a constant that specfies the user action that is about to occur, such as hiding the Navigation pane by clicking the Hide button on the toolbar.

 Used by
 HHN_TRACK

#### Properties

- int action
 Specifies the action the user is about to take. This is an HHACT_ constant.

- NMHDR hdr
 Standard WM_NOTIFY header(win32help::NMHDR).

- string curUrl
 A multi-byte, zero-terminated string that specifies the topic navigated to, or the name of the help window being created.

- HH_WINTYPE winType
 A pointer to the current HH_WINTYPE structure (win32help::HH_WINTYPE).


---

<!-- object: PyHHN_NOTIFY -->


<!-- page: PyHHN_NOTIFY.html -->

---

## PyHHN_NOTIFY Object

 A Python object, representing an HHN_NOTIFY structure

#### Comments

 Typically you create a PyHHN_NOTIFY (via win32help::HHN_NOTIFY) object, and set its properties. The object can then be passed to any function which takes an HHN_NOTIFY object.

 Use this structure to return the file name of the topic that has been navigated to, or to return the window type name of the help window that has been created.

 Used by
 HHN_NAVCOMPLETE
 HHN_WINDOW_CREATE

#### Properties

- NMHDR hdr
 Standard WM_NOTIFY header.(win32help::NMHDR)

- string url
 A multi-byte, zero-terminated string that specifies the topic navigated to, or the name of the help window being created.


---

<!-- object: PyHH_AKLINK -->


<!-- page: PyHH_AKLINK.html -->

---

## PyHH_AKLINK Object

 A Python object, representing an HH_AKLINK structure

#### Comments

 Typically you create a PyHH_AKLINK (via win32help::HH_AKLINK) object, and set its properties. The object can then be passed to any function which takes an HH_AKLINK object.

 Use this structure to specify one or more ALink names or KLink keywords that you want to search for.

 If the lookup yields no matching topics, HtmlHelp() checks the values of the following HH_AKLINK members to determine what alternative action to take:

 indexOnFail. If indexOnFail is TRUE, the Index tab is selected in the help window specified in window, and the keyword specified in keyword is selected in the entry field.

 url. If indexOnFail is FALSE, the topic file specified in url appears in the help window specified in window.
 msgText and msgTitle. If indexOnFail is FALSE and url is NULL, a message box appears using the text and caption specified in msgText and msgTitle.

 Used by
 HH_ALINK_LOOKUP
 HH_KEYWORD_LOOKUP

#### Properties

- int indexOnFail
 Specifies whether to display the keyword in the Index tab of the HTML Help Viewer if the lookup fails. The value of window specifies the Help Viewer.

- string keywords
 Specifies one or more ALink names or KLink keywords to look up. Multiple entries are delimited by a semicolon.

- string url
 Specifies the topic file to navigate to if the lookup fails. url refers to a valid topic within the specified compiled help (.chm) file and does not support Internet protocols that point to an HTML file.

- string msgText
 Specifies the text to display in a message box if the lookup fails and indexOnFail is FALSE and url is NULL.

- string msgTitle
 Specifies the caption of the message box in which the msgText parameter appears.

- string window
 Specifies the name of the window type in which to display one of the following:

 The selected topic, if the lookup yields one or more matching topics. The topic specified in url, if the lookup fails and a topic is specified in url.

 The Index tab, if the lookup fails and indexOnFail is specified as TRUE.


---

<!-- object: PyHH_FTS_QUERY -->


<!-- page: PyHH_FTS_QUERY.html -->

---

## PyHH_FTS_QUERY Object

 A Python object, representing an HH_FTS_QUERY structure

#### Comments

 Typically you create a PyHH_FTS_QUERY (via win32help::HH_FTS_QUERY) object, and set its properties. The object can then be passed to any function which takes an HH_FTS_QUERY object.

 Use this structure for full-text search.

#### Properties

- int uniCodeStrings
 TRUE if all strings are Unicode.

- long proximity
 Word proximity.

- int stemmedSearch
 TRUE for StemmedSearch only.

- int titleOnly
 TRUE for Title search only.

- int execute
 TRUE to initiate the search.

- string searchQuery
 String containing the search query.


---

<!-- object: PyHH_POPUP -->


<!-- page: PyHH_POPUP.html -->

---

## PyHH_POPUP Object

 A Python object, representing an HH_POPUP structure

#### Comments

 Typically you create a PyHH_POPUP (via win32help::HH_POPUP) object, and set its properties. The object can then be passed to any function which takes an HH_POPUP object.

 Use this structure to specify or modify the attributes of a pop-up window.

 Used by
 HH_DISPLAY_TEXT_POPUP

#### Properties

- long hinst
 Instance handle of the program or DLL to retrieve the string resource from. Ignored if idString is zero.

- unsigned int idString
 Specifies zero, or a resource ID in the program or DLL specified in hinst.

- int clrForeground
 Specifies the RGB value to use for the foreground color of the pop-up window. To use the system color for the window text, specify -1.

- int clrBackground
 Specifies the RGB value to use for the background color of the pop-up window. To use the system color for the window background, specify -1.

- string text
 Specifies the text to display if idString is zero.

- string font
 Specifies the font attributes to use for the text in the pop-up window.
 Use the following format to specify font family, point size, character set, and font format:
 facename[, point size[, charset[ BOLD ITALIC UNDERLINE]]]
 To omit an attribute, enter a comma. For example, to specify bold, 10-pt, MS Sans Serif font, font would be:
 MS Sans Serif, 10, , BOLD

- tuple pt
 (x,y). Specifies (in pixels) where the top center of the pop-up window should be located.

- tuple margins
 (left,top,right,bottom). Specifies (in pixels) the margins to use on the left, top, right, and bottom sides of the pop-up window. The default for all rectangle members is -1.


---

<!-- object: PyHH_WINTYPE -->


<!-- page: PyHH_WINTYPE.html -->

---

## PyHH_WINTYPE Object

 A Python object, representing an HH_WINTYPE structure

#### Comments

 Typically you create a PyHH_WINTYPE (via win32help::HH_WINTYPE) object, and set its properties. The object can then be passed to any function which takes an HH_WINTYPE object.

 Use this structure to specify or modify the attributes of a window type. Window types can be defined by an author in a project (.hhp) file, or they can be defined programmatically using the HTML Help API.
 When a HH_WINTYPE structure is passed to HtmlHelp() using the HH_SET_WIN_TYPE command, the HTML Help API makes a private copy of the contents of the structure. The help developer is therefore responsible for freeing memory used by the HH_WINTYPE structure or character arrays within it. The help developer can free memory after calling HH_SET_WIN_TYPE .

 Used by
 HH_SET_WIN_TYPE
 HH_GET_WIN_TYPE

#### Properties

- int uniCodeStrings
 Specifies whether the strings used in this structure are UNICODE.

- int validMembers
 Specifies which members in the structure are valid.

- int winProperties
 Specifies the properties of the window, such as whether it is the standard HTML Help Viewer or whether it includes a Search tab.

- int styles
 Specifies the styles used to create the window. These styles can be ignored, combined with extended styles, or used exclusively depending on the value of the validMembers and winProperties parameters.

- int exStyles
 Specifies the extended styles used to create the window. These styles can be ignored, combined with default styles, or used exclusively depending on the value of the validMembers and winProperties parameters.

- int showState
 Specifies the initial display state of the window. Valid values are the same as those for the Win32 API ShowWindow function.

- int hwndHelp
 Specifies the handle of the window if the window has been created.

- int hwndCaller
 Specifies the window that will receive HTML Help notification messages. Notification messages are sent via Windows WM_NOTIFY messages.

- int hwndToolBar
 Specifies the handle of the toolbar.

- int hwndNavigation
 Specifies the handle of the Navigation pane.

- int hwndHTML
 Specifies the handle of the Topic pane, which hosts Shdocvw.dll.

- int navWidth
 Specifies the width of the Navigation pane when the Help Viewer is expanded.

- int toolBarFlags
 Specifies which buttons to include on the toolbar.

- int notExpanded
 Specifies that the Help Viewer open with the Navigation pane closed.

- int curNavType
 Specifies the default tab to display on the Navigation pane.

- int idNotify
 Specifies a non-zero ID for enabling HTML Help notification messages. This ID is passed as the wParam value of Windows WM_NOTIFY messages.

- string typeName
 A null-terminated string that specifies the name of the window type.

- string caption
 A null-terminated string that specifies the caption to display in the title bar of the window.

- tuple windowPos
 (left,top,right,bottom). Specifies the coordinates of the window in pixels.

- tuple HTMLPos
 (left,top,right,bottom). Specifies the coordinates of the Topic pane.

- string toc
 Specifies the contents (.hhc) file to display in the Navigation pane.

- string index
 Specifies the index (.hhk) file to display in the Navigation pane.

- string file
 Specifies the default HTML file to display in the Topic pane.

- string home
 Specifies the file or URL to display in the Topic pane when the Home button is clicked.

- string jump1
 Specifies the text to display underneath the Jump1 button.

- string jump2
 Specifies the text to display underneath the Jump2 button.

- string urlJump1
 Specifies the URL to jump to when the Jump1 button is clicked.

- string urlJump2
 Specifies the URL to jump to when the Jump2 button is clicked.


---

<!-- object: PyHINTERNET -->


<!-- page: PyHINTERNET.html -->

---

## PyHINTERNET Object

 An object that wraps a HINTERNET handle. When the handle object is destroyed, it is automatically closed. See the PyHANDLE object for more details.


---

<!-- object: PyHKEY -->


<!-- page: PyHKEY.html -->

---

## PyHKEY Object

 A Python object, representing a win32 HKEY (a HANDLE to a registry key). See the PyHANDLE object for more details


---

<!-- object: PyHTHEME -->


<!-- page: PyHTHEME.html -->

---

## PyHTHEME Object

 A PyHANDLE object wrapping a HTHEME. _winxptheme::CloseThemeData will be called when the object dies or PyHANDLE::Close is called.


---

<!-- object: PyHWINSTA -->


<!-- page: PyHWINSTA.html -->

---

## PyHWINSTA Object

 Wrapper for a handle to a window station - returned by CreateWindowStation, OpenWindowStation, or GetProcessWindowStation

#### Methods

- EnumDesktops

 List desktop names within the window station

- SetProcessWindowStation

 Associates the calling process with the window station

- CloseWindowStation

 Closes the window station handle

- Detach

 Releases reference to handle without closing it


<!-- page: PyHWINSTA__CloseWindowStation_meth.html -->

## PyHWINSTA.CloseWindowStation

 CloseWindowStation()

Closes the window station handle

#### Comments

 This function cannot close the handle to current process's window station


<!-- page: PyHWINSTA__EnumDesktops_meth.html -->

## PyHWINSTA.EnumDesktops

 (string,...) = EnumDesktops()

Lists names of desktops in the window station


<!-- page: PyHWINSTA__SetProcessWindowStation_meth.html -->

## PyHWINSTA.SetProcessWindowStation

 SetProcessWindowStation()

Associates the calling process with the window station


---

<!-- object: PyLOCALGROUP_INFO_.2a -->


<!-- page: PyLOCALGROUP_INFO_.2a.html -->

---

## PyLOCALGROUP_INFO_* Object

 The following LOCALGROUP_INFO levels are supported.

| | Level | Data
| |

---

 |

---

| | 0 | PyLOCALGROUP_INFO_0
| | 1 | PyLOCALGROUP_INFO_1
| | 1002 | PyLOCALGROUP_INFO_1002


---

<!-- object: PyLOCALGROUP_INFO_0 -->


<!-- page: PyLOCALGROUP_INFO_0.html -->

---

## PyLOCALGROUP_INFO_0 Object

 A dictionary holding the information in a Win32 LOCALGROUP_INFO_0 structure.

#### Properties

- string/PyUnicode name
 Name of the group


---

<!-- object: PyLOCALGROUP_INFO_1 -->


<!-- page: PyLOCALGROUP_INFO_1.html -->

---

## PyLOCALGROUP_INFO_1 Object

 A dictionary holding the information in a Win32 LOCALGROUP_INFO_1 structure.

#### Properties

- string/PyUnicode name
 Name of the group

- string/PyUnicode comment
 The group's comment.


---

<!-- object: PyLOCALGROUP_INFO_1002 -->


<!-- page: PyLOCALGROUP_INFO_1002.html -->

---

## PyLOCALGROUP_INFO_1002 Object

 A dictionary holding the information in a Win32 LOCALGROUP_INFO_1002 structure.

#### Properties

- string/PyUnicode comment


---

<!-- object: PyLOCALGROUP_MEMBERS_INFO_.2a -->


<!-- page: PyLOCALGROUP_MEMBERS_INFO_.2a.html -->

---

## PyLOCALGROUP_MEMBERS_INFO_* Object

 The following LOCALGROUP_MEMBER_INFO levels are supported.

| | Level | Data
| |

---

 |

---

| | 0 | PyLOCALGROUP_MEMBERS_INFO_0
| | 1 | PyLOCALGROUP_MEMBERS_INFO_1
| | 2 | PyLOCALGROUP_MEMBERS_INFO_2
| | 3 | PyLOCALGROUP_MEMBERS_INFO_3


---

<!-- object: PyLOCALGROUP_MEMBERS_INFO_0 -->


<!-- page: PyLOCALGROUP_MEMBERS_INFO_0.html -->

---

## PyLOCALGROUP_MEMBERS_INFO_0 Object

 A dictionary holding the information in a Win32 LOCALGROUP_MEMBERS_INFO_0 structure.

#### Properties

- PySID sid


---

<!-- object: PyLOCALGROUP_MEMBERS_INFO_1 -->


<!-- page: PyLOCALGROUP_MEMBERS_INFO_1.html -->

---

## PyLOCALGROUP_MEMBERS_INFO_1 Object

 A dictionary holding the information in a Win32 LOCALGROUP_MEMBERS_INFO_1 structure.

#### Properties

- PySID sid

- int sidusage

- string/PyUnicode name


---

<!-- object: PyLOCALGROUP_MEMBERS_INFO_2 -->


<!-- page: PyLOCALGROUP_MEMBERS_INFO_2.html -->

---

## PyLOCALGROUP_MEMBERS_INFO_2 Object

 A dictionary holding the information in a Win32 LOCALGROUP_MEMBERS_INFO_2 structure.

#### Properties

- PySID sid

- int sidusage

- string/PyUnicode domainandname
 string containing the name of the member prefixed by the domain name and the "\\" separator character


---

<!-- object: PyLOCALGROUP_MEMBERS_INFO_3 -->


<!-- page: PyLOCALGROUP_MEMBERS_INFO_3.html -->

---

## PyLOCALGROUP_MEMBERS_INFO_3 Object

 A dictionary holding the information in a Win32 LOCALGROUP_MEMBERS_INFO_3 structure.

#### Properties

- string/PyUnicode domainandname
 string containing the name of the member prefixed by the domain name and the "\\" separator character


---

<!-- object: PyLOGBRUSH -->


<!-- page: PyLOGBRUSH.html -->

---

## PyLOGBRUSH Object

 Dict representing a LOGBRUSH struct as used with win32gui::CreateBrushIndirect and win32gui::ExtCreatePen

#### Win32 API References

- Search for LOGBRUSH at [msdn](https://learn.microsoft.com/en-ca/search/?terms=LOGBRUSH), [google](https://www.google.com/search?q=LOGBRUSH) or [google groups](https://groups.google.com/groups?q=LOGBRUSH).

#### Properties

- int Style
 Brush style, one of win32con.BS_* values

- int Color
 RGB color value. Can also be DIB_PAL_COLORS or DIB_RGB_COLORS if Style is BS_DIBPATTERN or BS_DIBPATTERNPT=

- int/PyHANDLE Hatch
 For BS_HATCH style, one of win32con.HS_*. Not used For BS_SOLID or BS_HOLLOW. For a pattern brush, this should be a handle to a bitmap


---

<!-- object: PyLOGFONT -->


<!-- page: PyLOGFONT.html -->

---

## PyLOGFONT Object

 A Python object, representing an PyLOGFONT structure

#### Comments

 Typically you create a PyLOGFONT object, and set its properties. The object can then be passed to any function which takes an LOGFONT object

#### Properties

- integer lfHeight

- integer lfWidth

- integer lfEscapement

- integer lfOrientation

- integer lfWeight

- integer lfItalic

- integer lfUnderline

- integer lfStrikeOut

- integer lfCharSet

- integer lfOutPrecision

- integer lfClipPrecision

- integer lfQuality

- integer lfPitchAndFamily

- string lfFaceName
 Name of the typeface, at most 31 characters


---

<!-- object: PyLSA_HANDLE -->


<!-- page: PyLSA_HANDLE.html -->

---

## PyLSA_HANDLE Object

 Object representing an Lsa policy handle (LSA_HANDLE), created by win32security::LsaOpenPolicy Identical to PyHANDLE, but calls LsaClose on destruction


---

<!-- object: PyLUID_AND_ATTRIBUTES -->


<!-- page: PyLUID_AND_ATTRIBUTES.html -->

---

## PyLUID_AND_ATTRIBUTES Object

 A sequence containing (LUID,Attributes) representing an LUID_AND_ATTRIBUTES structure

#### Comments

 LUID is a large integer, and attributes is an integer containing flags


---

<!-- object: PyLsaLogon_HANDLE -->


<!-- page: PyLsaLogon_HANDLE.html -->

---

## PyLsaLogon_HANDLE Object

 Lsa handle used to access authentication packages, returned by win32security::LsaRegisterLogonProcess or win32security::LsaConnectUntrusted. Base low-level object is a plain HANDLE. Inherits all properties and methods of PyHANDLE, but Close uses LsaDeregisterLogonProcess


---

<!-- object: PyMAPINAMEIDArray -->


<!-- page: PyMAPINAMEIDArray.html -->

---

## PyMAPINAMEIDArray Object

 A sequence (PyIID, string/int) objects FALSE*/)


---

<!-- object: PyMSG -->


<!-- page: PyMSG.html -->

---

## PyMSG Object

 A tuple representing a win32 MSG structure.

#### Items

- [0] PyHANDLE : hwnd

 Handle to the window whose window procedure receives the message.

- [1] int : message

 Specifies the message identifier.

- [2] int : wParam

 Specifies additional information about the message.

- [3] int : lParam

 Specifies additional information about the message.

- [4] int : time

 Specifies the time at which the message was posted (retrieved via GetTickCount()).

- [5] (int, int) : point

 Specifies the cursor position, in screen coordinates, when the message was posted.


---

<!-- object: PyNETRESOURCE -->


<!-- page: PyNETRESOURCE.html -->

---

## PyNETRESOURCE Object

 A Python object that encapsulates a Win32 NETRESOURCE structure.

#### Properties

- integer dwScope

- integer dwType

- integer dwDisplayType

- integer dwUsage

- string localName

- string remoteName

- string comment

- string provider

#### Comments

 Note that in pywin32-212 and earlier, the string attributes were always strings, but empty strings when the underlying Windows structure had NULL. On later pywin32 builds, these string attributes will return None in such cases.


---

<!-- object: PyNET_VALIDATE_AUTHENTICATION_INPUT_ARG -->


<!-- page: PyNET_VALIDATE_AUTHENTICATION_INPUT_ARG.html -->

---

## PyNET_VALIDATE_AUTHENTICATION_INPUT_ARG Object

 A dictionary or tuple passed as input to win32net::NetValidatePasswordPolicy

#### Parameters

- InputPersistedFields=None : NET_VALIDATE_PERSISTED_FIELDS

- PasswordMatched=0 : int


---

<!-- object: PyNET_VALIDATE_PASSWORD_CHANGE_INPUT_ARG -->


<!-- page: PyNET_VALIDATE_PASSWORD_CHANGE_INPUT_ARG.html -->

---

## PyNET_VALIDATE_PASSWORD_CHANGE_INPUT_ARG Object

 A dictionary or tuple passed as input to win32net::NetValidatePasswordPolicy

#### Parameters

- InputPersistedFields=None : NET_VALIDATE_PERSISTED_FIELDS

- ClearPassword=None : PyUnicode

- UserAccountName=None : PyUnicode

- HashedPassword=None : buffer

 A string or anything else holding bytes.

- PasswordMatch=0 : int

 Note MSDN incorrectly documents this member as PasswordMatched


---

<!-- object: PyNET_VALIDATE_PERSISTED_FIELDS -->


<!-- page: PyNET_VALIDATE_PERSISTED_FIELDS.html -->

---

## PyNET_VALIDATE_PERSISTED_FIELDS Object

 A dictionary returned by win32net::NetValidatePasswordPolicy

#### Comments

 Note that these fields will only appear if the PresentFields structure element indicates the fields are valid. Thus, the result dictionary may contain none, all, or any combination of these.

#### Parameters

- PasswordLastSet : PyDateTime

- BadPasswordTime : PyDateTime

- LockoutTime : PyDateTime

- BadPasswordCount : int

- PasswordHistoryLength : int

- PasswordHistory : None/string


---

<!-- object: PyNMHDR -->


<!-- page: PyNMHDR.html -->

---

## PyNMHDR Object

 A Python object, representing an NMHDR structure

#### Comments

 Typically you create a PyNMHDR (via win32help::NMHDR) object, and set its properties. The object can then be passed to any function which takes an NMHDR object.

 Contains information about a notification message.

#### Properties

- int hwndFrom
 Window handle to the control sending a message. ??? 64-bit problem here ???

- unsigned int idFrom
 Identifier of the control sending a message.

- unsigned int code
 Notification code. This member can be a control-specific notification code or it can be one of the common notification codes.


---

<!-- object: PyNOTIFYICONDATA -->


<!-- page: PyNOTIFYICONDATA.html -->

---

## PyNOTIFYICONDATA Object

 Tuple used to fill a NOTIFYICONDATA struct as used with win32gui::Shell_NotifyIcon

#### Win32 API References

- Search for NOTIFYICONDATA at [msdn](https://learn.microsoft.com/en-ca/search/?terms=NOTIFYICONDATA), [google](https://www.google.com/search?q=NOTIFYICONDATA) or [google groups](https://groups.google.com/groups?q=NOTIFYICONDATA).

#### Items

- [0] PyHANDLE : hWnd

 Handle to window that will process icon's messages

- [1] int : ID

 Unique id used when hWnd processes messages from more than one icon

- [2] int : Flags

 Combination of win32gui.NIF_* flags

- [3] int : CallbackMessage

 Message id to be pass to hWnd when processing messages

- [4] PyHANDLE : hIcon

 Handle to the icon to be displayed

- [5] str : Tip

 Tooltip text (optional)

- [6] str : Info

 Balloon tooltip text (optional)

- [7] int : Timeout

 Timeout for balloon tooltip, in milliseconds (optional)

- [8] str : InfoTitle

 Title for balloon tooltip (optional)

- [9] int : InfoFlags

 Combination of win32gui.NIIF_* flags (optional)


---

<!-- object: PyOLEMENUGROUPWIDTHS -->


<!-- page: PyOLEMENUGROUPWIDTHS.html -->

---

## PyOLEMENUGROUPWIDTHS Object

 Tuple containing 6 ints indicating nbr of options in each menu group


---

<!-- object: PyOVERLAPPED -->


<!-- page: PyOVERLAPPED.html -->

---

## PyOVERLAPPED Object

 A Python object, representing an overlapped structure

#### Comments

 Typically you create a PyOVERLAPPED object, and set its hEvent property. The object can then be passed to any function which takes an OVERLAPPED object, and the object attributes will be automatically updated.

#### Properties

- integer Offset
 Specifies a file position at which to start the transfer. The file position is a byte offset from the start of the file. The calling process sets this member before calling the ReadFile or WriteFile function. This member is ignored when reading from or writing to named pipes and communications devices.

- integer OffsetHigh
 Specifies the high word of the byte offset at which to start the transfer.

- object object
 Any python object that you want to attach to your overlapped I/O request.

- int dword
 An integer buffer that may be used by overlapped functions (eg, win32file::WaitCommEvent)

- PyHANDLE hEvent
 Identifies an event set to the signaled state when the transfer has been completed. The calling process sets this member before calling the win32file::ReadFile, win32file::WriteFile, win32pipe::ConnectNamedPipe, or win32pipe::TransactNamedPipe function.

- integer Internal
 Reserved for operating system use. (pointer-sized value)

- integer InternalHigh
 Reserved for operating system use. (pointer-sized value)


---

<!-- object: PyOVERLAPPEDReadBuffer -->


<!-- page: PyOVERLAPPEDReadBuffer.html -->

---

## PyOVERLAPPEDReadBuffer Object

 An alias for a standard Python buffer object. Previous versions of the Windows extensions had a custom object for holding a read buffer. This has been replaced with the standard Python buffer object.
Python does not provide a method for creating a read-write buffer of arbitrary size, so currently this can only be created by win32file::AllocateReadBuffer.


---

<!-- object: PyPERF_COUNTER_DEFINITION -->


<!-- page: PyPERF_COUNTER_DEFINITION.html -->

---

## PyPERF_COUNTER_DEFINITION Object

 An object encapsulating a Windows NT Performance Monitor counter definition (PERF_COUNTER_DEFINITION).

#### Comments

 Note that all the counter "set" functions will silently do nothing if the counter does not appear in a block. This is so the application can avoid excessive tests for lack of performance monitor functionality. However, the method PyPERF_COUNTER_DEFINITION::Get will raise a ValueError exception in this case.

#### Methods

- Increment

 Increments the value of the performance counter

- Decrement

 Decrements the value of the performance counter

- Set

 Sets the counter to a specific value

- Get

 Gets the current value of the counter

#### Properties

- integer DefaultScale
 The default scale of the counter.

- integer DetailLevel
 The detail level of the counter.

- integer CounterType
 The counter type.

- integer CounterNameTitleIndex

- integer CounterHelpTitleIndex
 Sentinel


<!-- page: PyPERF_COUNTER_DEFINITION__Decrement_meth.html -->

## PyPERF_COUNTER_DEFINITION.Decrement

 Decrement()

Decrements the value of the performance counter


<!-- page: PyPERF_COUNTER_DEFINITION__Get_meth.html -->

## PyPERF_COUNTER_DEFINITION.Get

 Get()

Gets the current value of the counter


<!-- page: PyPERF_COUNTER_DEFINITION__Increment_meth.html -->

## PyPERF_COUNTER_DEFINITION.Increment

 Increment()

Increments the value of the performance counter


<!-- page: PyPERF_COUNTER_DEFINITION__Set_meth.html -->

## PyPERF_COUNTER_DEFINITION.Set

 Set()

Sets the counter to a specific value


---

<!-- object: PyPERF_OBJECT_TYPE -->


<!-- page: PyPERF_OBJECT_TYPE.html -->

---

## PyPERF_OBJECT_TYPE Object

 A Python object, representing a PERF_OBJECT_TYPE structure

#### Methods

- Close

 Closes all counters.

#### Properties

- integer ObjectNameTitleIndex

- integer ObjectHelpTitleIndex

- integer DefaultCounterIndex


<!-- page: PyPERF_OBJECT_TYPE__Close_meth.html -->

## PyPERF_OBJECT_TYPE.Close

 Close()

Closes the object.


---

<!-- object: PyPOINT -->


<!-- page: PyPOINT.html -->

---

## PyPOINT Object

 Tuple of two ints (x,y) representing a POINT struct


---

<!-- object: PyPROFILEINFO -->


<!-- page: PyPROFILEINFO.html -->

---

## PyPROFILEINFO Object

 Dictionary containing data to fill a PROFILEINFO struct, to be passed to win32profile::LoadUserProfile. UserName is only required member.

#### Win32 API References

- Search for PROFILEINFO at [msdn](https://learn.microsoft.com/en-ca/search/?terms=PROFILEINFO), [google](https://www.google.com/search?q=PROFILEINFO) or [google groups](https://groups.google.com/groups?q=PROFILEINFO).

#### Properties

- PyUnicode UserName
 Name of user for which to load profile

- int Flags
 Combination of PI_* flags

- PyUnicode ProfilePath
 Path to roaming profile, can be None. Use win32net::NetUserGetInfo to retrieve user's profile path

- PyUnicode DefaultPath
 Path to Default user profile, can be None

- PyUnicode ServerName
 Domain controller, can be None

- PyUnicode PolicyPath
 Location of policy file, can be None

- PyHKEY Profile
 Handle to root of user's registry key. This member is output.


---

<!-- object: PyPROPERTYKEY -->


<!-- page: PyPROPERTYKEY.html -->

---

## PyPROPERTYKEY Object

 A tuple of a fmtid and property id (IID, int) that uniquely identifies a property


---

<!-- object: PyPROPVARIANT -->


<!-- page: PyPROPVARIANT.html -->

---

## PyPROPVARIANT Object

 Encapsulates a PROPVARIANT structure. Constructed using PROPVARIANTType(Value, Type=VT_ILLEGAL). Value can be any object that can be be converted to the requested variant type. Type should be a combination of VARENUM values (pythoncom.VT_*). VT_ILLEGAL indicates that an appropriate variant type should be inferred from the Value. If the requested Type includes VT_VECTOR, Value should be a sequence of compatible objects. Currently VT_ARRAY and VT_BYREF are not supported, although some types can be coerced into a safearray using PyPROPVARIANT::ChangeType.

#### Properties

- int vt
 The variant type, a combination of VARENUM values including flags. (read only)

#### Methods

- GetValue

 Returns an object representing the variant value

- ToString

 Returns the value as a string

- ChangeType

 Coerce to a different variant type


<!-- page: PyPROPVARIANT__ChangeType_meth.html -->

## PyPROPVARIANT.ChangeType

 PyPROPVARIANT = ChangeType(Type, Flags )

Coerce to a different variant type

#### Parameters

- Type : int

 New variant type, combination of pythoncom.VT_* values

- Flags=0 : int

 Reserved (PROPVAR_CHANGE_FLAGS)

#### Win32 API References

- Search for PropVariantChangeType at [msdn](https://learn.microsoft.com/en-ca/search/?terms=PropVariantChangeType), [google](https://www.google.com/search?q=PropVariantChangeType) or [google groups](https://groups.google.com/groups?q=PropVariantChangeType).


<!-- page: PyPROPVARIANT__GetValue_meth.html -->

## PyPROPVARIANT.GetValue

 object = GetValue()

Returns an object representing the variant value


<!-- page: PyPROPVARIANT__ToString_meth.html -->

## PyPROPVARIANT.ToString

 str = ToString()

Returns the value as a string

#### Win32 API References

- Search for PropVariantToString at [msdn](https://learn.microsoft.com/en-ca/search/?terms=PropVariantToString), [google](https://www.google.com/search?q=PropVariantToString) or [google groups](https://groups.google.com/groups?q=PropVariantToString).


---

<!-- object: PyPerfMonManager -->


<!-- page: PyPerfMonManager.html -->

---

## PyPerfMonManager Object

 A Python object

#### Methods

- Close

 Closes all counters.


<!-- page: PyPerfMonManager__Close_meth.html -->

## PyPerfMonManager.Close

 Close()

Closes the performance monitor manager.


---

<!-- object: PyPrinterHANDLE -->


<!-- page: PyPrinterHANDLE.html -->

---

## PyPrinterHANDLE Object

 Handle to a printer or print server.
Created using win32print::OpenPrinter or win32print::AddPrinter
Inherits all methods and properties of PyHANDLE.
When object is destroyed, handle is released using ClosePrinter.


---

<!-- object: PyRECT -->


<!-- page: PyRECT.html -->

---

## PyRECT Object

 Tuple of 4 ints defining a rectangle: (left, top, right, bottom)


---

<!-- object: PyResourceId -->


<!-- page: PyResourceId.html -->

---

## PyResourceId Object

 Identifies a resource or function in a module. This can be a WORD-sized integer value (0-65536), or bytes.


---

<!-- object: PyResourceId_1 -->


<!-- page: PyResourceId_1.html -->

---

## PyResourceId Object

 Identifies a resource or function in a module. This can be a WORD-sized integer value (0-65536), or unicode. Class atoms as used with win32gui::CreateWindow are also treated as resource ids since they can also be represented by a name or WORD id. When passing resource names and types as strings, they are usually formatted as a pound sign followed by decimal form of the id. ('#42' for example)


---

<!-- object: PySAndRestriction -->


<!-- page: PySAndRestriction.html -->

---

## PySAndRestriction Object

#### Parameters

- restriction : [PySRestriction, ...]

 A sequence of PySRestriction objects.


---

<!-- object: PySBinaryArray -->


<!-- page: PySBinaryArray.html -->

---

## PySBinaryArray Object

 A sequence of strings containing binary data.


---

<!-- object: PySBitMaskRestriction -->


<!-- page: PySBitMaskRestriction.html -->

---

## PySBitMaskRestriction Object

#### Parameters

- relBMR : int

- propTag : ULONG

 The property ID.

- ulMask=0 : int


---

<!-- object: PySCROLLINFO -->


<!-- page: PySCROLLINFO.html -->

---

## PySCROLLINFO Object

 A tuple representing a SCROLLINFO structure

#### Items

- [0] int : addnMask

 Additional mask information. Python automatically fills the mask for valid items, so currently the only valid values are zero, and win32con.SIF_DISABLENOSCROLL.

- [1] int : min

 The minimum scrolling position. Both min and max, or neither, must be provided.

- [2] int : max

 The maximum scrolling position. Both min and max, or neither, must be provided.

- [3] int : page

 Specifies the page size. A scroll bar uses this value to determine the appropriate size of the proportional scroll box.

- [4] int : pos

 Specifies the position of the scroll box.

- [5] int : trackPos

 Specifies the immediate position of a scroll box that the user is dragging. An application can retrieve this value while processing the SB_THUMBTRACK notification message. An application cannot set the immediate scroll position; the PyCWnd::SetScrollInfo function ignores this member.

#### Comments

 When passed to Python, will always be a tuple of size 6, and items may be None if not available.

 When passed from Python, it must have the addn mask attribute, but all other items may be None, or not exist.


---

<!-- object: PySC_HANDLE -->


<!-- page: PySC_HANDLE.html -->

---

## PySC_HANDLE Object

 Handle to a service or service control manager. This is a variant of PyHANDLE that releases its handle using CloseServiceHandle.


---

<!-- object: PySContentRestriction -->


<!-- page: PySContentRestriction.html -->

---

## PySContentRestriction Object

#### Parameters

- fuzzyLevel : int

- propTag : ULONG

 The property ID.

- propertyValue : PySPropValue


---

<!-- object: PySECURITY_ATTRIBUTES -->


<!-- page: PySECURITY_ATTRIBUTES.html -->

---

## PySECURITY_ATTRIBUTES Object

 A Python object, representing a SECURITY_ATTRIBUTES structure

#### Properties

- boolean bInheritHandle
 Specifies whether the returned handle is inherited when a new process is created. If this member is TRUE, the new process inherits the handle.

- PySECURITY_DESCRIPTOR SECURITY_DESCRIPTOR
 A PySECURITY_DESCRIPTOR, or None

#### Comments

 On platforms that support security descriptor operations, SECURITY_DESCRIPTOR defaults to a blank security descriptor with no owner, group, dacl, or sacl. Set to None to use a NULL security descriptor instead. When SECURITY_DESCRIPTOR is not None, any of its methods can be invoked directly on the PySECURITY_ATTRIBUTES object


---

<!-- object: PySECURITY_DESCRIPTOR -->


<!-- page: PySECURITY_DESCRIPTOR.html -->

---

## PySECURITY_DESCRIPTOR Object

 A Python object, representing a SECURITY_DESCRIPTOR structure

#### Methods

- Initialize

 Initializes the object.

- GetSecurityDescriptorOwner

 Return the owner of the security descriptor. SID is returned.

- GetSecurityDescriptorOwner

 Return the group owning the security descriptor. SID is returned.

- GetSecurityDescriptorDacl

 Return the discretionary ACL of the security descriptor.

- GetSecurityDescriptorSacl

 Return the system ACL of the security descriptor.

- GetSecurityDescriptorControl

 Returns the control bit flags and revistion of the SD

- SetSecurityDescriptorOwner

 Set the owner of the security descriptor. Returns non-zero on success.

- SetSecurityDescriptorGroup

 Set the primary group of the security descriptor. Returns non-zero on success.

- SetDacl

 Sets information in a discretionary access-control list.

- SetSecurityDescriptorSacl

 Sets the system access control list in the security descriptor

- IsValid

 Determine if security descriptor is valid (IsValidSecurityDescriptor)

- GetLength

 Return length of security descriptor (GetSecurityDescriptorLength)

- IsSelfRelative

 Returns true if SD is self-relative, false if absolute

- SetSecurityDescriptorControl

 Sets control bitmask of a security descriptor

#### Comments

 Note the PySECURITY_DESCRIPTOR object supports the buffer interface. Thus buffer(sd) can be used to obtain the raw bytes. tp_as_buffer


<!-- page: PySECURITY_DESCRIPTOR__GetLength_meth.html -->

## PySECURITY_DESCRIPTOR.GetLength

 GetLength()

return length of security descriptor (GetSecurityDescriptorLenght).


<!-- page: PySECURITY_DESCRIPTOR__GetSecurityDescriptorControl_meth.html -->

## PySECURITY_DESCRIPTOR.GetSecurityDescriptorControl

 (int,int) = GetSecurityDescriptorControl()

Returns tuple of Control bit flags and revision of SD.


<!-- page: PySECURITY_DESCRIPTOR__GetSecurityDescriptorDacl_meth.html -->

## PySECURITY_DESCRIPTOR.GetSecurityDescriptorDacl

 PyACL = GetSecurityDescriptorDacl()

Return the discretionary ACL of the security descriptor.


<!-- page: PySECURITY_DESCRIPTOR__GetSecurityDescriptorGroup_meth.html -->

## PySECURITY_DESCRIPTOR.GetSecurityDescriptorGroup

 PySID = GetSecurityDescriptorGroup()

Return the group owning the security descriptor. SID is returned.


<!-- page: PySECURITY_DESCRIPTOR__GetSecurityDescriptorOwner_meth.html -->

## PySECURITY_DESCRIPTOR.GetSecurityDescriptorOwner

 PySID = GetSecurityDescriptorOwner()

Return the owner of the security descriptor.


<!-- page: PySECURITY_DESCRIPTOR__GetSecurityDescriptorSacl_meth.html -->

## PySECURITY_DESCRIPTOR.GetSecurityDescriptorSacl

 PyACL = GetSecurityDescriptorSacl()

Return system access control list (SACL) of SD


<!-- page: PySECURITY_DESCRIPTOR__Initialize_meth.html -->

## PySECURITY_DESCRIPTOR.Initialize

 Initialize()

Initialize the SD.


<!-- page: PySECURITY_DESCRIPTOR__IsSelfRelative_meth.html -->

## PySECURITY_DESCRIPTOR.IsSelfRelative

 IsSelfRelative()

Returns 1 if security descriptor is self relative, 0 if absolute


<!-- page: PySECURITY_DESCRIPTOR__IsValid_meth.html -->

## PySECURITY_DESCRIPTOR.IsValid

 IsValid()

Determines if the security descriptor is valid.


<!-- page: PySECURITY_DESCRIPTOR__SetSecurityDescriptorControl_meth.html -->

## PySECURITY_DESCRIPTOR.SetSecurityDescriptorControl

 SetSecurityDescriptorControl(ControlBitsOfInterest, ControlBitsToSet)

Sets the control bit flags related to inheritance for a security descriptor

#### Parameters

- ControlBitsOfInterest : int

 Bitmask of flags to be modified

- ControlBitsToSet : int

 Bitmask containing flag values to set


<!-- page: PySECURITY_DESCRIPTOR__SetSecurityDescriptorDacl_meth.html -->

## PySECURITY_DESCRIPTOR.SetSecurityDescriptorDacl

 SetSecurityDescriptorDacl(bDaclPresent, DACL, bDaclDefaulted)

Replaces DACL in a security descriptor.

#### Parameters

- bDaclPresent : int

 A flag indicating if the SE_DACL_PRESENT flag should be set.

- DACL : PyACL

 The DACL to set. If None, a NULL ACL will be created allowing world access.

- bDaclDefaulted : int

 A flag indicating if the SE_DACL_DEFAULTED flag should be set.


<!-- page: PySECURITY_DESCRIPTOR__SetSecurityDescriptorGroup_meth.html -->

## PySECURITY_DESCRIPTOR.SetSecurityDescriptorGroup

 int = SetSecurityDescriptorGroup(sid, bOwnerDefaulted )

Set group SID.

#### Parameters

- sid : PySID

 The group sid to be set in the security descriptor.

- bOwnerDefaulted : int

 Normally set to false since this explicitly set the owner.


<!-- page: PySECURITY_DESCRIPTOR__SetSecurityDescriptorOwner_meth.html -->

## PySECURITY_DESCRIPTOR.SetSecurityDescriptorOwner

 SetSecurityDescriptorOwner(sid, bOwnerDefaulted)

Set owner SID.

#### Parameters

- sid : PySID

 The sid to be set as owner in the security descriptor.

- bOwnerDefaulted : int

 Normally set to false since this explicitly set the owner.


<!-- page: PySECURITY_DESCRIPTOR__SetSecurityDescriptorSacl_meth.html -->

## PySECURITY_DESCRIPTOR.SetSecurityDescriptorSacl

 SetSecurityDescriptorSacl(bSaclPresent, SACL, bSaclDefaulted)

Replaces system access control list (SACL) in the security descriptor.

#### Parameters

- bSaclPresent : int

 A flag indicating if SACL is to be used. If false, last 2 parms are ignored.

- SACL : PyACL

 The SACL to set in the security descriptor

- bSaclDefaulted : int

 Flag, set to false if user has specifically set the SACL.


---

<!-- object: PySERVER_INFO_.2a -->


<!-- page: PySERVER_INFO_.2a.html -->

---

## PySERVER_INFO_* Object

 The following SERVER_INFO levels are supported.

| | Level | Data
| |

---

 |

---

| | 100 | PySERVER_INFO_100
| | 101 | PySERVER_INFO_101
| | 102 | PySERVER_INFO_102
| | 402 | PySERVER_INFO_402
| | 403 | PySERVER_INFO_403
| | 502 | PySERVER_INFO_502
| | 503 | PySERVER_INFO_503


---

<!-- object: PySERVER_INFO_100 -->


<!-- page: PySERVER_INFO_100.html -->

---

## PySERVER_INFO_100 Object

 A dictionary holding the information in a Win32 SERVER_INFO_100 structure.

#### Properties

- int platform_id

- string/PyUnicode name


---

<!-- object: PySERVER_INFO_101 -->


<!-- page: PySERVER_INFO_101.html -->

---

## PySERVER_INFO_101 Object

 A dictionary holding the information in a Win32 SERVER_INFO_101 structure.

#### Properties

- int platform_id

- string/PyUnicode name

- int version_major

- int version_minor

- int type
 one of the SV_TYPE_* constants

- string/PyUnicode comment


---

<!-- object: PySERVER_INFO_102 -->


<!-- page: PySERVER_INFO_102.html -->

---

## PySERVER_INFO_102 Object

 A dictionary holding the information in a Win32 SERVER_INFO_102 structure.

#### Properties

- int platform_id

- string/PyUnicode name

- int version_major

- int version_minor

- int type
 one of the SV_TYPE_* constants

- string/PyUnicode comment

- int users

- int disc

- bool hidden

- int announce

- int anndelta

- string/PyUnicode userpath


---

<!-- object: PySERVER_INFO_402 -->


<!-- page: PySERVER_INFO_402.html -->

---

## PySERVER_INFO_402 Object

 A dictionary holding the information in a Win32 SERVER_INFO_402 structure.

#### Properties

- int ulist_mtime

- int glist_mtime

- int alist_mtime

- int security

- int numadmin

- int lanmask

- string/PyUnicode guestacct

- int chdevs

- int chdevq

- int chdevjobs

- int connections

- int shares

- int openfiles

- int sessopens

- int sessvcs

- int sessreqs

- int opensearch

- int activelocks

- int numreqbuf

- int sizreqbuf

- int numbigbuf

- int numfiletasks

- int alertsched

- int erroralert

- int logonalert

- int accessalert

- int diskalert

- int netioalert

- int maxauditsz

- string/PyUnicode srvheuristics


---

<!-- object: PySERVER_INFO_403 -->


<!-- page: PySERVER_INFO_403.html -->

---

## PySERVER_INFO_403 Object

 A dictionary holding the information in a Win32 SERVER_INFO_403 structure.

#### Properties

- int ulist_mtime

- int glist_mtime

- int alist_mtime

- int security

- int numadmin

- int lanmask

- string/PyUnicode guestacct

- int chdevs

- int chdevq

- int chdevjobs

- int connections

- int shares

- int openfiles

- int sessopens

- int sessvcs

- int sessreqs

- int opensearch

- int activelocks

- int numreqbuf

- int sizreqbuf

- int numbigbuf

- int numfiletasks

- int alertsched

- int erroralert

- int logonalert

- int accessalert

- int diskalert

- int netioalert

- int maxauditsz

- string/PyUnicode srvheuristics

- int auditedevents

- int autoprofile

- string/PyUnicode autopath


---

<!-- object: PySERVER_INFO_502 -->


<!-- page: PySERVER_INFO_502.html -->

---

## PySERVER_INFO_502 Object

 A dictionary holding the information in a Win32 SERVER_INFO_502 structure.

#### Properties

- int sessopens

- int sessvcs

- int opensearch

- int sizreqbuf

- int initworkitems

- int maxworkitems

- int rawworkitems

- int irpstacksize

- int maxrawbuflen

- int sessusers

- int sessconns

- int maxpagedmemoryusage

- int maxnonpagedmemoryusage

- bool enableforcedlogoff

- bool timesource

- bool acceptdownlevelapis

- bool lmannounce


---

<!-- object: PySERVER_INFO_503 -->


<!-- page: PySERVER_INFO_503.html -->

---

## PySERVER_INFO_503 Object

 A dictionary holding the information in a Win32 SERVER_INFO_503 structure.

#### Properties

- int sessopens

- int sessvcs

- int opensearch

- int sizreqbuf

- int initworkitems

- int maxworkitems

- int rawworkitems

- int irpstacksize

- int maxrawbuflen

- int sessusers

- int sessconns

- int maxpagedmemoryusage

- int maxnonpagedmemoryusage

- bool enableforcedlogoff

- bool timesource

- bool acceptdownlevelapis

- bool lmannounce

- string/PyUnicode domain

- int maxkeepsearch

- int scavtimeout

- int minrcvqueue

- int minfreeworkitems

- int xactmemsize

- int threadpriority

- int maxmpxct

- int oplockbreakwait

- int oplockbreakresponsewait

- bool enableoplocks

- bool enablefcbopens

- bool enableraw

- bool enablesharednetdrives

- int minfreeconnections

- int maxfreeconnections


---

<!-- object: PySExistRestriction -->


<!-- page: PySExistRestriction.html -->

---

## PySExistRestriction Object

#### Parameters

- propTag : ULONG

 The property ID to check for existance.

- reserved1=0 : int

- reserved2=0 : int


---

<!-- object: PySHARE_INFO_.2a -->


<!-- page: PySHARE_INFO_.2a.html -->

---

## PySHARE_INFO_* Object

 The following SHARE_INFO levels are supported.

| | Level | Data
| |

---

 |

---

| | 0 | PySHARE_INFO_0
| | 1 | PySHARE_INFO_1
| | 2 | PySHARE_INFO_2
| | 501 | PySHARE_INFO_501
| | 502 | PySHARE_INFO_502


---

<!-- object: PySHARE_INFO_0 -->


<!-- page: PySHARE_INFO_0.html -->

---

## PySHARE_INFO_0 Object

 A dictionary holding the infomation in a Win32 SHARE_INFO_0 structure.

#### Properties

- string/PyUnicode netname


---

<!-- object: PySHARE_INFO_1 -->


<!-- page: PySHARE_INFO_1.html -->

---

## PySHARE_INFO_1 Object

 A dictionary holding the infomation in a Win32 SHARE_INFO_1 structure.

#### Properties

- string/PyUnicode netname

- int type

- string/PyUnicode remark


---

<!-- object: PySHARE_INFO_2 -->


<!-- page: PySHARE_INFO_2.html -->

---

## PySHARE_INFO_2 Object

 A dictionary holding the infomation in a Win32 SHARE_INFO_2 structure.

#### Properties

- string/PyUnicode netname

- int type

- string/PyUnicode remark

- int permissions

- int max_uses

- int current_uses

- string/PyUnicode path

- string/PyUnicode passwd


---

<!-- object: PySHARE_INFO_501 -->


<!-- page: PySHARE_INFO_501.html -->

---

## PySHARE_INFO_501 Object

 A dictionary holding the infomation in a Win32 SHARE_INFO_501 structure.

#### Properties

- string/PyUnicode netname

- int type

- string/PyUnicode remark

- int flags


---

<!-- object: PySHARE_INFO_502 -->


<!-- page: PySHARE_INFO_502.html -->

---

## PySHARE_INFO_502 Object

 A dictionary holding the infomation in a Win32 SHARE_INFO_502 structure.

#### Properties

- string/PyUnicode netname

- int type

- string/PyUnicode remark

- int permissions

- int max_uses

- int current_uses

- string/PyUnicode path

- string/PyUnicode passwd

- int reserved

- PySECURITY_DESCRIPTOR security_descriptor


---

<!-- object: PySHELL_ITEM_RESOURCE -->


<!-- page: PySHELL_ITEM_RESOURCE.html -->

---

## PySHELL_ITEM_RESOURCE Object

 Tuple of (PyIID, str) that identifies a shell resource


---

<!-- object: PySID -->


<!-- page: PySID.html -->

---

## PySID Object

 A Python object, representing a SID structure

#### Methods

- Initialize

 Initialize the SID.

- IsValid

 Determines if the SID is valid.

- SetSubAuthority

 Sets a SID SubAuthority

- GetLength

 Return length of sid (GetLengthSid)

- GetSubAuthorityCount

 Return nbr of subauthorities from SID

- GetSubAuthority

 Return specified subauthory from SID

- GetSidIdentifierAuthority

 Return identifier for the authority who issued the SID (one of the SID_IDENTIFIER_AUTHORITY constants)

#### Comments

 Note the PySID object supports the buffer interface. Thus buffer(sid) can be used to obtain the raw bytes. tp_as_buffer


<!-- page: PySID__GetLength_meth.html -->

## PySID.GetLength

 int = GetLength()

return length of SID (GetLengthSid).


<!-- page: PySID__GetSidIdentifierAuthority_meth.html -->

## PySID.GetSidIdentifierAuthority

 (int,int,int,int,int,int) = GetSidIdentifierAuthority()

Returns a tuple of 6 SID_IDENTIFIER_AUTHORITY constants


<!-- page: PySID__GetSubAuthorityCount_meth.html -->

## PySID.GetSubAuthorityCount

 int = GetSubAuthorityCount()

return nbr of subauthorities from SID


<!-- page: PySID__GetSubAuthority_meth.html -->

## PySID.GetSubAuthority

 int = GetSubAuthority()

Returns specified subauthority from SID


<!-- page: PySID__Initialize_meth.html -->

## PySID.Initialize

 Initialize(idAuthority, numSubauthorities)

Initialize the SID.

#### Parameters

- idAuthority : SID_IDENTIFIER_AUTHORITY

 The identifier authority.

- numSubauthorities : int

 The number of sub authorities to allocate.


<!-- page: PySID__IsValid_meth.html -->

## PySID.IsValid

 IsValid()

Determines if the SID is valid.


<!-- page: PySID__SetSubAuthority_meth.html -->

## PySID.SetSubAuthority

 SetSubAuthority(index, val)

Sets a SID SubAuthority

#### Parameters

- index : int

 The index of the sub authority to set

- val : int

 The value for the sub authority

#### Comments

 See the function SetSidSubAuthority


---

<!-- object: PySID_AND_ATTRIBUTES -->


<!-- page: PySID_AND_ATTRIBUTES.html -->

---

## PySID_AND_ATTRIBUTES Object

 A sequence containing (PySID,Attributes) Representing a SID_AND_ATTRIBUTES structure

#### Comments

 Attributes is an integer containing flags that depend on intended usage


---

<!-- object: PySIZE -->


<!-- page: PySIZE.html -->

---

## PySIZE Object

 Tuple of two ints (cx,cy) representing a SIZE struct


---

<!-- object: PySMALL_RECT -->


<!-- page: PySMALL_RECT.html -->

---

## PySMALL_RECT Object

 Wrapper for a SMALL_RECT struct Create using PySMALL_RECTType(Left, Top, Right, Bottom). All params optional, defaulting to 0

#### Properties

- int Left
 Left side of rectangle

- int Top
 Top edge of rectangle

- int Right
 Right edge of rectangle

- int Bottom
 Bottome edge of rectangle


---

<!-- object: PySNotRestriction -->


<!-- page: PySNotRestriction.html -->

---

## PySNotRestriction Object

#### Parameters

- restriction : PySRestriction

- reserved=0 : int


---

<!-- object: PySOrRestriction -->


<!-- page: PySOrRestriction.html -->

---

## PySOrRestriction Object

#### Parameters

- restriction : [PySRestriction, ...]

 A sequence of PySRestriction objects.


---

<!-- object: PySPropTagArray -->


<!-- page: PySPropTagArray.html -->

---

## PySPropTagArray Object

 A sequence of integers


---

<!-- object: PySPropValue -->


<!-- page: PySPropValue.html -->

---

## PySPropValue Object

 A MAPI property value. Property values can either be passed from python into MAPI functions, or returned from MAPI functions to Python.

#### Parameters

- propType : ULONG

 The type of the MAPI property

- value : object

 The property value

#### Comments

 The parameters can be one of the following pairs of values.

| | propType | value
| |

---

 |

---

| | PT_I2 | An integer case PT_SHORT:
| | PT_MV_I2 | A sequence of integers
| | PT_I4 | An integer case PT_LONG:
| | PT_MV_I4 | A sequence of integers
| | PT_R4 | A float case PT_FLOAT:
| | PT_MV_R4 | A sequence of floats
| | PT_R8 | A float case PT_DOUBLE:
| | PT_MV_R8 | A sequence of floats
| | PT_BOOLEAN | A boolean value (or an int)
| | PT_APPTIME | A PyTime object
| | PT_MV_APPTIME | An sequence of PyTime object
| | PT_SYSTIME | A PyTime object
| | PT_MV_APPTIME | An sequence of PyTime object
| | PT_STRING8 | A string or PyUnicode Copy into new MAPI memory block
| | PT_STRING8 | A sequence of string or PyUnicode objects.
| | PT_UNICODE | A string or PyUnicode Bit of a hack - need to copy into MAPI block.
| | PT_MV_UNICODE | A sequence of string or PyUnicode
| | PT_BINARY | A string containing binary data
| | PT_MV_BINARY | A sequence of strings containing binary data
| | PT_CLSID | A PyIID
| | PT_MV_CLSID | A sequence of PyIID objects
| | PT_I8 | A PyLARGE_INTEGER
| | PT_MV_I8 | A sequence of PyLARGE_INTEGER
| | PT_ERROR | An integer error code.
| | PT_NULL | Anything!


---

<!-- object: PySPropValueArray -->


<!-- page: PySPropValueArray.html -->

---

## PySPropValueArray Object

 A sequence of PySPropValue, as passed to many MAPI functions.


---

<!-- object: PySPropertyRestriction -->


<!-- page: PySPropertyRestriction.html -->

---

## PySPropertyRestriction Object

#### Parameters

- relOp : int

- propTag : ULONG

 The property ID.

- propertyValue : PySPropValue


---

<!-- object: PySRestriction -->


<!-- page: PySRestriction.html -->

---

## PySRestriction Object

#### Parameters

- restrictionType : int

 An integer describing the contents of the second parameter.

- restriction : object

 An object in one of the formats describe below.

#### Comments

 The parameters can be one of the following pairs of values.

| | restrictionType | restrictionValue
| |

---

 |

---

| | RES_AND | PySAndRestriction
| | RES_OR | PySOrRestriction
| | RES_PROPERTY | PySPropertyRestriction
| | RES_EXIST | PySExistRestriction
| | RES_NOT | PySNotRestriction
| | RES_CONTENT | PySContentRestriction
| | RES_BITMASK | PySBitMaskRestriction


---

<!-- object: PySRow -->


<!-- page: PySRow.html -->

---

## PySRow Object

 Identical to a PySValue object


---

<!-- object: PySRowSet -->


<!-- page: PySRowSet.html -->

---

## PySRowSet Object

 A sequence of PySRow objects, as passed to many MAPI functions.


---

<!-- object: PySSortOrderItem -->


<!-- page: PySSortOrderItem.html -->

---

## PySSortOrderItem Object

 An item in a SortOrderSet.

#### Parameters

- propTag : int

 A property tag.

- order : int

 The order in which the data is to be sorted. Possible values are: mapi.TABLE_SORT_ASCEND, mapi.TABLE_SORT_COMBINE and mapi.TABLE_SORT_DESCEND


---

<!-- object: PySSortOrderSet -->


<!-- page: PySSortOrderSet.html -->

---

## PySSortOrderSet Object

 An object describing a SortOrderSet.

#### Parameters

- sortItems : ( PySSortOrderItem, ...)

 The items to sort by

- cCategories=0 : int

- cExpanded=0 : int

 TRUE */)


---

<!-- object: PySTARTUPINFO -->


<!-- page: PySTARTUPINFO.html -->

---

## PySTARTUPINFO Object

 A Python object, representing an STARTUPINFO structure

#### Comments

 Typically you create a PySTARTUPINFO (via win32process::STARTUPINFO) object, and set its properties. The object can then be passed to any function which takes an STARTUPINFO object.

#### Properties

- integer dwX
 Specifies the x offset, in pixels, of the upper left corner of a window if a new window is created. The offset is from the upper left corner of the screen.

- integer dwY
 Specifies the y offset, in pixels, of the upper left corner of a window if a new window is created. The offset is from the upper left corner of the screen.

- integer dwXSize
 Specifies the width, in pixels, of the window if a new window is created.

- integer dwYSize
 Specifies the height, in pixels, of the window if a new window is created.

- integer dwXCountChars
 For console processes, if a new console window is created, specifies the screen buffer width in character columns. This value is ignored in a GUI process.

- integer dwYCountChars
 For console processes, if a new console window is created, specifies the screen buffer height in character rows.

- integer dwFillAttribute
 Specifies the initial text and background colors if a new console window is created in a console application. These values are ignored in GUI applications

- integer dwFlags
 This is a bit field that determines whether certain STARTUPINFO attributes are used when the process creates a window. To use many of the additional attributes, you typically must set the appropriate mask in this attribute, and also set the attributes themselves. Any combination of the win32con.STARTF_* flags can be specified.

- integer wShowWindow
 Can be any of the SW_ constants defined in win32con. For GUI processes, this specifies the default value the first time ShowWindow is called.

- integer/PyHANDLE hStdInput

- integer/PyHANDLE hStdOutput

- integer/PyHANDLE hStdError

- string/None lpDesktop

- string/None lpTitle


---

<!-- object: PySTGMEDIUM -->


<!-- page: PySTGMEDIUM.html -->

---

## PySTGMEDIUM Object

 A STGMEDIUM object represents a COM STGMEDIUM structure.

#### Methods

- set

 Sets the type and data of the object

#### Properties

- int tymed
 An integer indicating the type of data in the stgmedium

- object data
 The data in the stgmedium. The result depends on the value of the 'tymed' property of the PySTGMEDIUM object.

| | tymed | Result Type
| |

---

 |

---

| | TYMED_GDI | An integer GDI handle
| | TYMED_MFPICT | An integer METAFILE handle
| | TYMED_ENHMF | An integer ENHMETAFILE handle
| | TYMED_HGLOBAL | A string with the bytes of the global memory object.
| | TYMED_FILE | A string/unicode filename
| | TYMED_ISTREAM | A PyIStream object
| | TYMED_ISTORAGE | A PyIStorage object
- int data_handle
 The raw 'integer' representation of the data. For TYMED_HGLOBAL, this is the handle rather than the string data. For the string and interface types, this is an integer holding the pointer.


<!-- page: PySTGMEDIUM__set_meth.html -->

## PySTGMEDIUM.set

 set(tymed, data)

Sets the type and data of the object.

#### Parameters

- tymed : int

 The type of the data

- data : object


---

<!-- object: PySecBuffer -->


<!-- page: PySecBuffer.html -->

---

## PySecBuffer Object

 Python object wrapping a SecBuffer structure Created using win32security.PySecBufferType(type,size) where type is a SECBUFFER_* constant

#### Methods

- Clear

 Resets all members of the structure

#### Properties

- int BufferType

- string Buffer

- int BufferSize

- int MaxBufferSize


<!-- page: PySecBuffer__Clear_meth.html -->

## PySecBuffer.Clear

 Clear()

Resets the buffer to all NULL's, and set the current size to maximum


---

<!-- object: PySecBufferDesc -->


<!-- page: PySecBufferDesc.html -->

---

## PySecBufferDesc Object

 Sequence-like object that contains a group of buffers to be used with SSPI functions.

#### Comments

 This object is created using win32security.PySecBufferDescType(Version), where Version is an int that defaults to SECBUFFER_VERSION if not passed in.

#### Methods

- append

 Adds a PySecBuffer to the list of buffers


<!-- page: PySecBufferDesc__append_meth.html -->

## PySecBufferDesc.append

 append(buffer)

Adds a PySecBuffer to the buffer configuration

#### Parameters

- buffer :

 PySecBuffer object to be attached to the group of buffers


---

<!-- object: PyTASK_TRIGGER -->


<!-- page: PyTASK_TRIGGER.html -->

---

## PyTASK_TRIGGER Object

 Python object representing a TASK_TRIGGER structure via the structmember Api


---

<!-- object: PyTOKEN_GROUPS -->


<!-- page: PyTOKEN_GROUPS.html -->

---

## PyTOKEN_GROUPS Object

 A sequence of PySID_AND_ATTRIBUTES sequences, eg [(PySID,int),...] representing a TOKEN_GROUPS structure


---

<!-- object: PyTOKEN_PRIVILEGES -->


<!-- page: PyTOKEN_PRIVILEGES.html -->

---

## PyTOKEN_PRIVILEGES Object

 An object representing Win32 token privileges.

#### Comments

 This is a sequence (eg, list) of ((id, attributes),...) where id is a privilege LUID as returned by win32security::LookupPrivilegeValue and attributes is a combination of SE_PRIVILEGE_ENABLED, SE_PRIVILEGE_ENABLED_BY_DEFAULT, and SE_PRIVILEGE_USED_FOR_ACCESS


---

<!-- object: PyTRIVERTEX -->


<!-- page: PyTRIVERTEX.html -->

---

## PyTRIVERTEX Object

 Dict representing a TRIVERTEX struct containing color information at a point

#### Win32 API References

- Search for TRIVERTEX at [msdn](https://learn.microsoft.com/en-ca/search/?terms=TRIVERTEX), [google](https://www.google.com/search?q=TRIVERTEX) or [google groups](https://groups.google.com/groups?q=TRIVERTEX).

#### Properties

- int x
 X coord in logical units

- int y
 Y coord in logical units

- int Red
 Red component

- int Green
 Green component

- int Blue
 Blue component

- int Alpha
 Transparency value


---

<!-- object: PyTRUSTEE -->


<!-- page: PyTRUSTEE.html -->

---

## PyTRUSTEE Object

 A dictionary representing a TRUSTEE structure.

#### Properties

- int TrusteeForm

- int TrusteeType

- object Identifier
 Depends on the value of TrusteeForm (string or sid)

- object MultipleTrustee
 default is None

- object MultipleTrusteeOperation
 default is None


---

<!-- object: PyTS_HANDLE -->


<!-- page: PyTS_HANDLE.html -->

---

## PyTS_HANDLE Object

 Handle to a Terminal Server


---

<!-- object: PyTime -->


<!-- page: PyTime.html -->

---

## PyTime Object

 An alias for the builtin datetime object.


---

<!-- object: PyUSER_INFO_.2a -->


<!-- page: PyUSER_INFO_.2a.html -->

---

## PyUSER_INFO_* Object

 The following USER_INFO levels are supported.

| | Level | Data
| |

---

 |

---

| | 0 | PyUSER_INFO_0
| | 1 | PyUSER_INFO_1
| | 2 | PyUSER_INFO_2
| | 3 | PyUSER_INFO_3
| | 4 | PyUSER_INFO_4
| | 10 | PyUSER_INFO_10
| | 11 | PyUSER_INFO_11
| | 20 | PyUSER_INFO_20
| | 1003 | PyUSER_INFO_1003
| | 1005 | PyUSER_INFO_1005
| | 1006 | PyUSER_INFO_1006
| | 1007 | PyUSER_INFO_1007
| | 1008 | PyUSER_INFO_1008
| | 1009 | PyUSER_INFO_1009
| | 1010 | PyUSER_INFO_1010
| | 1011 | PyUSER_INFO_1011


---

<!-- object: PyUSER_INFO_0 -->


<!-- page: PyUSER_INFO_0.html -->

---

## PyUSER_INFO_0 Object

 A dictionary holding the information in a Win32 USER_INFO_0 structure.

#### Properties

- string/PyUnicode name


---

<!-- object: PyUSER_INFO_1 -->


<!-- page: PyUSER_INFO_1.html -->

---

## PyUSER_INFO_1 Object

 A dictionary holding the information in a Win32 USER_INFO_1 structure.

#### Properties

- string/PyUnicode name

- string/PyUnicode password

- int password_age

- int priv

- string/PyUnicode home_dir

- string/PyUnicode comment

- int flags

- string/PyUnicode script_path


---

<!-- object: PyUSER_INFO_10 -->


<!-- page: PyUSER_INFO_10.html -->

---

## PyUSER_INFO_10 Object

 A dictionary holding the information in a Win32 USER_INFO_10 structure.

#### Properties

- string/PyUnicode name

- string/PyUnicode comment

- string/PyUnicode usr_comment

- string/PyUnicode full_name


---

<!-- object: PyUSER_INFO_1003 -->


<!-- page: PyUSER_INFO_1003.html -->

---

## PyUSER_INFO_1003 Object

 A dictionary holding the information in a Win32 USER_INFO_1003 structure.

#### Properties

- string/PyUnicode password


---

<!-- object: PyUSER_INFO_1005 -->


<!-- page: PyUSER_INFO_1005.html -->

---

## PyUSER_INFO_1005 Object

 A dictionary holding the information in a Win32 USER_INFO_1005 structure.

#### Properties

- int priv


---

<!-- object: PyUSER_INFO_1006 -->


<!-- page: PyUSER_INFO_1006.html -->

---

## PyUSER_INFO_1006 Object

 A dictionary holding the information in a Win32 USER_INFO_1006 structure.

#### Properties

- string/PyUnicode home_dir


---

<!-- object: PyUSER_INFO_1007 -->


<!-- page: PyUSER_INFO_1007.html -->

---

## PyUSER_INFO_1007 Object

 A dictionary holding the information in a Win32 USER_INFO_1007 structure.

#### Properties

- string/PyUnicode comment


---

<!-- object: PyUSER_INFO_1008 -->


<!-- page: PyUSER_INFO_1008.html -->

---

## PyUSER_INFO_1008 Object

 A dictionary holding the information in a Win32 USER_INFO_1008 structure.

#### Properties

- int flags


---

<!-- object: PyUSER_INFO_1009 -->


<!-- page: PyUSER_INFO_1009.html -->

---

## PyUSER_INFO_1009 Object

 A dictionary holding the information in a Win32 USER_INFO_1009 structure.

#### Properties

- string/PyUnicode script_path


---

<!-- object: PyUSER_INFO_1010 -->


<!-- page: PyUSER_INFO_1010.html -->

---

## PyUSER_INFO_1010 Object

 A dictionary holding the information in a Win32 USER_INFO_1010 structure.

#### Properties

- int auth_flags


---

<!-- object: PyUSER_INFO_1011 -->


<!-- page: PyUSER_INFO_1011.html -->

---

## PyUSER_INFO_1011 Object

 A dictionary holding the information in a Win32 USER_INFO_1011 structure.

#### Properties

- string/PyUnicode full_name


---

<!-- object: PyUSER_INFO_11 -->


<!-- page: PyUSER_INFO_11.html -->

---

## PyUSER_INFO_11 Object

 A dictionary holding the information in a Win32 USER_INFO_11 structure.

#### Properties

- string/PyUnicode name

- string/PyUnicode comment

- string/PyUnicode usr_comment

- string/PyUnicode full_name

- int priv

- int auth_flags

- int password_age

- string/PyUnicode home_dir

- string/PyUnicode parms

- int last_logon

- int last_logoff

- int bad_pw_count

- int num_logons

- string/PyUnicode logon_server

- int country_code

- string/PyUnicode workstations

- int max_storage

- int units_per_week

- string logon_hours

- int code_page


---

<!-- object: PyUSER_INFO_2 -->


<!-- page: PyUSER_INFO_2.html -->

---

## PyUSER_INFO_2 Object

 A dictionary holding the information in a Win32 USER_INFO_2 structure.

#### Properties

- string/PyUnicode name

- string/PyUnicode password

- int password_age

- int priv

- string/PyUnicode home_dir

- string/PyUnicode comment

- int flags

- string/PyUnicode script_path

- int auth_flags

- string/PyUnicode full_name

- string/PyUnicode usr_comment

- string/PyUnicode parms

- string/PyUnicode workstations

- int last_logon

- int last_logoff

- int acct_expires

- int max_storage

- int units_per_week

- string logon_hours

- int bad_pw_count

- int num_logons

- string/PyUnicode logon_server

- int country_code

- int code_page


---

<!-- object: PyUSER_INFO_20 -->


<!-- page: PyUSER_INFO_20.html -->

---

## PyUSER_INFO_20 Object

 A dictionary holding the information in a Win32 USER_INFO_20 structure.

#### Properties

- string/PyUnicode name

- string/PyUnicode full_name

- string/PyUnicode comment

- int flags

- int user_id


---

<!-- object: PyUSER_INFO_3 -->


<!-- page: PyUSER_INFO_3.html -->

---

## PyUSER_INFO_3 Object

 A dictionary holding the information in a Win32 USER_INFO_3 structure.

#### Properties

- string/PyUnicode name

- string/PyUnicode password

- int password_age

- int priv

- string/PyUnicode home_dir

- string/PyUnicode comment

- int flags

- string/PyUnicode script_path

- int auth_flags

- string/PyUnicode full_name

- string/PyUnicode usr_comment

- string/PyUnicode parms

- string/PyUnicode workstations

- int last_logon

- int last_logoff

- int acct_expires

- int max_storage

- int units_per_week

- string logon_hours

- int bad_pw_count

- int num_logons

- string/PyUnicode logon_server

- int country_code

- int code_page

- int user_id

- int primary_group_id

- string/PyUnicode profile

- string/PyUnicode home_dir_drive

- int password_expired


---

<!-- object: PyUSER_INFO_4 -->


<!-- page: PyUSER_INFO_4.html -->

---

## PyUSER_INFO_4 Object

 A dictionary holding the information in a Win32 USER_INFO_4 structure.

#### Properties

- string/PyUnicode name

- string/PyUnicode password

- int password_age

- int priv

- string/PyUnicode home_dir

- string/PyUnicode comment

- int flags

- string/PyUnicode script_path

- int auth_flags

- string/PyUnicode full_name

- string/PyUnicode usr_comment

- string/PyUnicode parms

- string/PyUnicode workstations

- int last_logon

- int last_logoff

- int acct_expires

- int max_storage

- int units_per_week

- string logon_hours

- int bad_pw_count

- int num_logons

- string/PyUnicode logon_server

- int country_code

- int code_page

- PySID user_sid

- int primary_group_id

- string/PyUnicode profile

- string/PyUnicode home_dir_drive

- int password_expired


---

<!-- object: PyUSER_MODALS_INFO_.2a -->


<!-- page: PyUSER_MODALS_INFO_.2a.html -->

---

## PyUSER_MODALS_INFO_* Object

 The following USER_MODALS_INFO levels are supported.

| | Level | Data
| |

---

 |

---

| | 0 | PyUSER_MODALS_INFO_0
| | 1 | PyUSER_MODALS_INFO_1
| | 2 | PyUSER_MODALS_INFO_2
| | 3 | PyUSER_MODALS_INFO_3


---

<!-- object: PyUSER_MODALS_INFO_0 -->


<!-- page: PyUSER_MODALS_INFO_0.html -->

---

## PyUSER_MODALS_INFO_0 Object

 A dictionary holding the information in a Win32 USER_MODALS_INFO_0 structure.

#### Properties

- int min_passwd_len

- int max_passwd_age

- int min_passwd_age

- int force_logoff

- int password_hist_len


---

<!-- object: PyUSER_MODALS_INFO_1 -->


<!-- page: PyUSER_MODALS_INFO_1.html -->

---

## PyUSER_MODALS_INFO_1 Object

 A dictionary holding the information in a Win32 USER_MODALS_INFO_1 structure.

#### Properties

- int role

- string/PyUnicode primary


---

<!-- object: PyUSER_MODALS_INFO_2 -->


<!-- page: PyUSER_MODALS_INFO_2.html -->

---

## PyUSER_MODALS_INFO_2 Object

 A dictionary holding the information in a Win32 USER_MODALS_INFO_2 structure.

#### Properties

- string/PyUnicode domain_name

- PySID domain_id


---

<!-- object: PyUSER_MODALS_INFO_3 -->


<!-- page: PyUSER_MODALS_INFO_3.html -->

---

## PyUSER_MODALS_INFO_3 Object

 A dictionary holding the information in a Win32 USER_MODALS_INFO_3 structure.

#### Properties

- int lockout_duration

- int lockout_observation_window

- int usrmod3_lockout_threshold


---

<!-- object: PyUSE_INFO_.2a -->


<!-- page: PyUSE_INFO_.2a.html -->

---

## PyUSE_INFO_* Object

 The following USE_INFO levels are supported.

| | Level | Data
| |

---

 |

---

| | 0 | PyUSE_INFO_0
| | 1 | PyUSE_INFO_1
| | 2 | PyUSE_INFO_2
| | 3 | PyUSE_INFO_3


---

<!-- object: PyUSE_INFO_0 -->


<!-- page: PyUSE_INFO_0.html -->

---

## PyUSE_INFO_0 Object

 A dictionary holding the infomation in a Win32 USE_INFO_0 structure.

#### Properties

- string/PyUnicode local

- string/PyUnicode remote


---

<!-- object: PyUSE_INFO_1 -->


<!-- page: PyUSE_INFO_1.html -->

---

## PyUSE_INFO_1 Object

 A dictionary holding the infomation in a Win32 USE_INFO_1 structure.

#### Properties

- string/PyUnicode local

- string/PyUnicode remote

- strng/PyUnicode password

- int status

- int asg_type

- int refcount

- int usecount


---

<!-- object: PyUSE_INFO_2 -->


<!-- page: PyUSE_INFO_2.html -->

---

## PyUSE_INFO_2 Object

 A dictionary holding the infomation in a Win32 USE_INFO_2 structure.

#### Properties

- string/PyUnicode local

- string/PyUnicode remote

- strng/PyUnicode password

- int status

- int asg_type

- int refcount

- int usecount

- string/PyUnicode username

- string/PyUnicode domainname


---

<!-- object: PyUSE_INFO_3 -->


<!-- page: PyUSE_INFO_3.html -->

---

## PyUSE_INFO_3 Object

 A dictionary holding the infomation in a Win32 USE_INFO_3 structure.

#### Properties

- string/PyUnicode local

- string/PyUnicode remote

- strng/PyUnicode password

- int status

- int asg_type

- int refcount

- int usecount

- string/PyUnicode username

- string/PyUnicode domainname

- int flags


---

<!-- object: PyUrlCacheHANDLE -->


<!-- page: PyUrlCacheHANDLE.html -->

---

## PyUrlCacheHANDLE Object

 Handle used to enumerate the browser cache. Created by win32inet::FindFirstUrlCacheEntry. Object's Close() method calls FindCloseUrlCache to free the handle.


---

<!-- object: PyWAVEFORMATEX -->


<!-- page: PyWAVEFORMATEX.html -->

---

## PyWAVEFORMATEX Object

 A Python object, representing a WAVEFORMATEX structure

#### Properties

- integer wFormatTag
 Waveform-audio format type. pywintypes only defines WAVE_FORMAT_PCM as a constant. Other values must be looked up in the mmsystem.h header file.

- integer nChannels
 Number of channels. 1 for Mono, 2 for Stereo, anything, but never 5.1.

- integer nSamplesPerSec
 Sample rate, in samples per second (hertz), that each channel should be played or recorded. If wFormatTag is WAVE_FORMAT_PCM, then common values for nSamplesPerSec are 8000, 11025, 22050, and 44100 Hz

- integer nAvgBytesPerSec
 Required average data-transfer rate, in bytes per second, for the format tag. If wFormatTag is WAVE_FORMAT_PCM, nAvgBytesPerSec should be equal to the product of nSamplesPerSec and nBlockAlign.

- integer nBlockAlign
 Block alignment, in bytes. The block alignment is the minimum atomic unit of data for the wFormatTag format type. If wFormatTag is WAVE_FORMAT_PCM, nBlockAlign should be equal to the product of nChannels and wBitsPerSample divided by 8 (bits per byte). For non-PCM formats, this member must be computed according to the manufacturer's specification of the format tag.

- integer wBitsPerSample
 Bits per sample for the wFormatTag format type. If wFormatTag is WAVE_FORMAT_PCM, then wBitsPerSample should be equal to 8 or 16. Sentinel


---

<!-- object: PyWINHTTP_AUTOPROXY_OPTIONS -->


<!-- page: PyWINHTTP_AUTOPROXY_OPTIONS.html -->

---

## PyWINHTTP_AUTOPROXY_OPTIONS Object

 Used by win32inet::WinHTTPGetProxyForUrl

#### Parameters

- dwFlags : int

- dwAutoDetectFlags : int

- obAutoConfig : string

- obReserved=None : object

 Must be None

- dwReserved=0 : int

 Must be zero

- autoLogin=1 : bool


---

<!-- object: PyWINHTTP_PROXY_INFO -->


<!-- page: PyWINHTTP_PROXY_INFO.html -->

---

## PyWINHTTP_PROXY_INFO Object

 A tuple representing a WINHTTP_PROXY_INFO structure.

#### Items

- [0] int : dwAccessType

- [2] string : lpszProxy

- [3] string : lpszProxy


---

<!-- object: PyWKSTA_INFO_.2a -->


<!-- page: PyWKSTA_INFO_.2a.html -->

---

## PyWKSTA_INFO_* Object

 The following WKSTA_INFO levels are supported.

| | Level | Data
| |

---

 |

---

| | 100, | PyWKSTA_INFO_100
| | 101, | PyWKSTA_INFO_101
| | 102, | PyWKSTA_INFO_102
| | 502, | PyWKSTA_INFO_502


---

<!-- object: PyWKSTA_INFO_100 -->


<!-- page: PyWKSTA_INFO_100.html -->

---

## PyWKSTA_INFO_100 Object

 A dictionary holding the infomation in a Win32 WKSTA_INFO_100 structure.

#### Properties

- int platform_id
 Indicates platform level to use to retrieve platform specific information

- string/PyUnicode computername
 Name of the local computer

- string/PyUnicode langroup
 Name of the domain to which computer belongs

- int ver_major
 Major version number of operating system running on the computer

- int ver_minor
 Minor version number of operating system running on the computer


---

<!-- object: PyWKSTA_INFO_101 -->


<!-- page: PyWKSTA_INFO_101.html -->

---

## PyWKSTA_INFO_101 Object

 A dictionary holding the infomation in a Win32 WKSTA_INFO_101 structure.

#### Properties

- int platform_id
 Indicates platform level to use to retrieve platform specific information

- string/PyUnicode computername
 Name of the local computer

- string/PyUnicode langroup
 Name of the domain to which computer belongs

- int ver_major
 Major version number of operating system running on the computer

- int ver_minor
 Minor version number of operating system running on the computer

- string/PyUnicode lanroot
 Path to the LANMAN directory


---

<!-- object: PyWKSTA_INFO_102 -->


<!-- page: PyWKSTA_INFO_102.html -->

---

## PyWKSTA_INFO_102 Object

 A dictionary holding the infomation in a Win32 WKSTA_INFO_102 structure.

#### Properties

- int platform_id
 Indicate platform level to use to retrieve platform specific information

- string/PyUnicode computername
 Name of the local computer

- string/PyUnicode langroup
 Name of the domain to which computer belongs

- int ver_major
 Major version number of operating system running on the computer

- int ver_minor
 Minor version number of operating system running on the computer

- string/PyUnicode lanroot
 Path to the LANMAN directory

- int logged_on_users
 Number of users who are logged on to the local computer


---

<!-- object: PyWKSTA_INFO_302 -->


<!-- page: PyWKSTA_INFO_302.html -->

---

## PyWKSTA_INFO_302 Object

 A dictionary holding the infomation in a Win32 WKSTA_INFO_302 structure.

#### Properties

- int char_wait
 number of seconds the computer will wait for a remote resource to become available

- int collection_time
 number of milliseconds the computer will collect data before sending the data to a character device resource. The workstation waits the specified time or collects the number of characters specified by wki302_maximum_collection_count, whichever comes first.

- int maximum_collection_count
 Specifies the number of bytes of information the computer will collect before sending the data to a character device resource. The workstation collects the specified number of bytes or waits the time specified by wki302_collection_time, whichever comes first.

- int keep_conn
 Specifies the number of seconds the server will maintain an inactive connection to a resource.

- int keep_search
 Defines the number of seconds an inactive search will continue.

- int max_cmds
 Specifies the number of simultaneous network device driver commands that can be sent to the network.

- int num_work_buf
 Specifies the number of internal buffers the computer has.

- int siz_work_buf
 Specifies the size, in bytes, of each internal buffer.

- int max_wrk_cache
 Specifies the maximum size, in bytes, of an internal cache buffer.

- int max_wrk_cache
 Indicates the number of seconds the server waits before disconnecting an inactive session.

- int siz_error
 Specifies the size, in bytes, of an internal error buffer.

- int num_alerts
 Specifies the maximum number of clients that can receive alert messages. (This member is not supported under MS-DOS.) The Alerter service registers at least three clients when it begins to run.

- int num_services
 Specifies the number of services that can be installed on the computer at any time.

- int errlog_sz
 Specifies the maximum size, in kilobytes, of the client's error log file.

- int print_buf_time
 Specifies the number of seconds the server waits before closing inactive compatibility-mode print jobs.

- int num_char_buf
 Specifies the number of character pipe buffers and device buffers the client can have.

- int siz_char_buf
 Specifies the maximum size, in bytes, of a character pipe buffer and device buffer.

- string/PyUnicode wrk_heuristics
 Pointer to a Unicode string of flags used to control a client's operation.

- int mailslots
 Specifies the maximum number of mailslots allowed.

- int num_dgram_buf
 Specifies the number of buffers to allocate for receiving datagrams.


---

<!-- object: PyWKSTA_INFO_402 -->


<!-- page: PyWKSTA_INFO_402.html -->

---

## PyWKSTA_INFO_402 Object

 A dictionary holding the infomation in a Win32 WKSTA_INFO_402 structure.

#### Properties

- int char_wait
 number of seconds the computer will wait for a remote resource to become available

- int collection_time
 number of milliseconds the computer will collect data before sending the data to a character device resource. The workstation waits the specified time or collects the number of characters specified by wki402_maximum_collection_count, whichever comes first.

- string/PyUnicode maximum_collection_count
 Name of the domain to which computer belongs

- int keep_conn
 Major version number of operating system running on the computer

- int keep_search
 Minor version number of operating system running on the computer

- int max_cmds
 ..

- int num_work_buf
 Number of users who are logged on to the local computer

- int siz_work_buf
 Number of users who are logged on to the local computer

- int max_wrk_cache
 ..

- int sess_timeout
 ..

- int siz_error
 ..

- int num_alerts
 ..

- int num_services
 ..

- int errlog_sz
 ..

- int print_buf_time
 ..

- int num_char_buf
 ..

- int siz_char_buf
 Specifies the maximum size, in bytes, of a character pipe buffer and device buffer.

- string/PyUnicode siz_char_buf
 ..

- int mailslots
 ..

- int num_dgram_buf
 ..

- int max_threads
 Number of threads the computer can dedicate to the network


---

<!-- object: PyWKSTA_INFO_502 -->


<!-- page: PyWKSTA_INFO_502.html -->

---

## PyWKSTA_INFO_502 Object

 A dictionary holding the infomation in a Win32 WKSTA_INFO_502 structure.

#### Properties

- int char_wait
 number of seconds the computer will wait for a remote resource to become available

- int collection_time
 number of milliseconds the computer will collect data before sending the data to a character device resource. The workstation waits the specified time or collects the number of characters specified by wki502_maximum_collection_count, whichever comes first.

- int maximum_collection_count
 Specifies the number of bytes of information the computer will collect before sending the data to a character device resource. The workstation collects the specified number of bytes or waits the time specified by wki302_collection_time, whichever comes first.

- int keep_conn
 Specifies the number of seconds the server will maintain an inactive connection to a resource.

- int max_cmds
 Specifies the number of simultaneous network device driver commands that can be sent to the network.

- int max_wrk_cache
 Indicates the number of seconds the server waits before disconnecting an inactive session.

- int siz_char_buf
 Specifies the maximum size, in bytes, of a character pipe buffer and device buffer.

- int lock_quota
 TODO

- int lock_increment
 TODO

- int lock_maximum
 TODO

- int pipe_increment
 TODO

- int pipe_maximum
 TODO

- int cache_file_timeout
 TODO

- int dormant_file_limit
 TODO

- int read_ahead_throughput
 TODO

- int num_mailslot_buffers
 TODO

- int num_srv_announce_buffers
 TODO

- int max_illegal_datagram_events
 TODO

- int illegal_datagram_event_reset_frequency
 TODO

- bool log_election_packets
 TODO

- bool use_opportunistic_locking
 TODO

- bool use_unlock_behind
 TODO

- bool use_close_behind
 TODO

- bool buf_named_pipes
 TODO

- bool use_lock_read_unlock
 TODO

- bool utilize_nt_caching
 TODO

- bool use_raw_read
 TODO

- bool use_raw_write
 TODO

- bool use_write_raw_data
 TODO

- bool use_encryption
 TODO

- bool buf_files_deny_write
 TODO

- bool buf_read_only_files
 TODO

- bool force_core_create_mode
 TODO

- bool use_512_byte_max_transfer
 TODO


---

<!-- object: PyWKSTA_TRANSPORT_INFO_.2a -->


<!-- page: PyWKSTA_TRANSPORT_INFO_.2a.html -->

---

## PyWKSTA_TRANSPORT_INFO_* Object

 The following WKSTA_TRANSPORT_INFO levels are supported.

| | Level | Data
| |

---

 |

---

| | 0, | PyWKSTA_TRANSPORT_INFO_0


---

<!-- object: PyWKSTA_TRANSPORT_INFO_0 -->


<!-- page: PyWKSTA_TRANSPORT_INFO_0.html -->

---

## PyWKSTA_TRANSPORT_INFO_0 Object

 A dictionary holding the infomation in a Win32 WKSTA_TRANSPORT_INFO_0 structure.

#### Properties

- int quality_of_service
 Supplies a value that specifies the search order of the transport protocol with respect to other transport protocols. The highest value is searched first.

- int number_of_vcs
 Specifies the number of clients communicating with the server using this transport protocol.

- string/PyUnicode transport_name
 Specifies the device name of the transport protocol.

- string/PyUnicode transport_address
 Specifies the address of the server on this transport protocol.

- bool wan_ish
 This member is ignored by the NetWkstaTransportAdd function. For the NetWkstaTransportEnum function, this member indicates that this transport protocol is a WAN transport protocol. This member is set TRUE for NetBIOS/TCIP; it is set FALSE for NetBEUI and NetBIOS/IPX.


---

<!-- object: PyWKSTA_USER_INFO_.2a -->


<!-- page: PyWKSTA_USER_INFO_.2a.html -->

---

## PyWKSTA_USER_INFO_* Object

 The following WKSTA_USER_INFO levels are supported.

| | Level | Data
| |

---

 |

---

| | 0, | PyWKSTA_USER_INFO_0
| | 1, | PyWKSTA_USER_INFO_1


---

<!-- object: PyWKSTA_USER_INFO_0 -->


<!-- page: PyWKSTA_USER_INFO_0.html -->

---

## PyWKSTA_USER_INFO_0 Object

 A dictionary holding the infomation in a Win32 WKSTA_USER_INFO_0 structure.

#### Properties

- string/PyUnicode username
 Name of user currently logged on to the workstation


---

<!-- object: PyWKSTA_USER_INFO_1 -->


<!-- page: PyWKSTA_USER_INFO_1.html -->

---

## PyWKSTA_USER_INFO_1 Object

 A dictionary holding the infomation in a Win32 WKSTA_USER_INFO_1 structure.

#### Properties

- string/PyUnicode username
 Name of user currently logged on to the workstation

- string/PyUnicode logon_domain
 Returns the domain name of the user account of the user currently logged on to the workstation.

- string/PyUnicode oth_domains
 Returns the list of other operating system domains browsed by the workstation. The domain names are separated by blanks.

- string/PyUnicode logon_server
 Returns the name of the computer that authenticated the server.


---

<!-- object: PyWNDCLASS -->


<!-- page: PyWNDCLASS.html -->

---

## PyWNDCLASS Object

 A Python object, representing an WNDCLASS structure

#### Comments

 Typically you create a PyWNDCLASS object, and set its properties. The object can then be passed to any function which takes an WNDCLASS object

#### Properties

- integer style

- integer cbWndExtra

- integer hInstance

- integer hIcon

- integer hCursor

- integer hbrBackground
 These 3 handled manually in PyWNDCLASS::getattro/setattro. The pymeth below is used as an end tag, so these props will be lost if below it

- string lpszMenuName

- string lpszClassName

- function lpfnWndProc

#### Methods

- SetDialogProc

 Sets the WNDCLASS to be for a dialog box.


<!-- page: PyWNDCLASS__SetDialogProc_meth.html -->

## PyWNDCLASS.SetDialogProc

 SetDialogProc()

Sets the WNDCLASS to be for a dialog box


---

<!-- object: PyXFORM -->


<!-- page: PyXFORM.html -->

---

## PyXFORM Object

 Dict representing an XFORM struct used as a world transformation matrix All members are optional, defaulting to 0.0.

#### Win32 API References

- Search for XFORM struct at [msdn](https://learn.microsoft.com/en-ca/search/?terms=XFORM struct), [google](https://www.google.com/search?q=XFORM struct) or [google groups](https://groups.google.com/groups?q=XFORM struct).

#### Properties

- float M11
 Usage is dependent on operation performed, see MSDN docs

- float M12
 Usage is dependent on operation performed, see MSDN docs

- float M21
 Usage is dependent on operation performed, see MSDN docs

- float M22
 Usage is dependent on operation performed, see MSDN docs

- float Dx
 Horizontal offset in logical units

- float Dy
 Vertical offset in logical units


---

<!-- object: Pymmapfile -->


<!-- page: Pymmapfile.html -->

---

## Pymmapfile Object

 Object that provides access to memory-mapped file operations.

#### Methods

- close

 Closes the file mapping handle and releases mapped view

- find

 Finds a string in the buffer.

- flush

 Flushes memory buffer to disk

- move

 Moves data from one place in buffer to another

- read

 Returns specified number of bytes from buffer, and advances current position

- read_byte

 Reads a single character from current pos

- read_line

 Reads data from current pos up to next EOL.

- resize

 Resizes the file mapping and view

- seek

 Changes current position

- size

 Returns size of file mapping

- tell

 Returns current position in buffer

- write

 Places data at current pos in buffer.

- write_byte

 Writes a single character of data


<!-- page: Pymmapfile__close_meth.html -->

## Pymmapfile.close

 close()

Closes the file mapping handle and releases mapped view


<!-- page: Pymmapfile__find_meth.html -->

## Pymmapfile.find

 int = find(needle, start )

Finds a string in the buffer.

#### Parameters

- needle : str

 String to be located

- start : int

 Pos at which to start search, current pos assumed if not specified

#### Return Value

Returns pos of string, or -1 if not found


<!-- page: Pymmapfile__flush_meth.html -->

## Pymmapfile.flush

 flush(offset, size)

Flushes memory buffer to disk

#### Parameters

- offset=0 : int

 Position in buffer at which to flush

- size=0 : int

 Number of bytes to flush, 0 to flush remainder of buffer past the offset


<!-- page: Pymmapfile__move_meth.html -->

## Pymmapfile.move

 move(dest, src, count)

Moves data from one place in buffer to another

#### Parameters

- dest : int

 Destination position in buffer

- src : int

 Source position in buffer

- count : int

 Number of bytes to move


<!-- page: Pymmapfile__read_byte_meth.html -->

## Pymmapfile.read_byte

 str = read_byte()

Reads a single character from current pos


<!-- page: Pymmapfile__read_line_meth.html -->

## Pymmapfile.read_line

 str = read_line()

Reads data from current pos up to next EOL.


<!-- page: Pymmapfile__read_meth.html -->

## Pymmapfile.read

 str = read(num_bytes)

Returns specified number of bytes from buffer, and advances current position

#### Parameters

- num_bytes : int

 Number of bytes to read


<!-- page: Pymmapfile__resize_meth.html -->

## Pymmapfile.resize

 resize(MaximumSize, FileOffset, NumberOfBytesToMap)

Resizes the file mapping and view.

#### Parameters

- MaximumSize : long

 New size for file mapping. Use a multiple of system page size (see win32api::GetSystemInfo)

- FileOffset=0 : long

 Offset into file mapping. Must be multiple of allocation granularity.

- NumberOfBytesToMap=0 : long

 New view size. Specify a multiple of system page size.

#### Comments

 If MaximumSize is 0, only the mapped view will be affected.

 Accepts keyword args.


<!-- page: Pymmapfile__seek_meth.html -->

## Pymmapfile.seek

 seek(dist, how)

Changes current position

#### Parameters

- dist : int

 Distance to seek

- how=0 : int

 Pos from which to seek

| | how | meaning
| |

---

 |

---

| | 0 | Seek from start of buffer
| | 1 | Seek from current position
| | 2 | Seek backwards from end of buffer


<!-- page: Pymmapfile__size_meth.html -->

## Pymmapfile.size

 long = size()

Returns size of current view


<!-- page: Pymmapfile__tell_meth.html -->

## Pymmapfile.tell

 int = tell()

Returns current position in buffer


<!-- page: Pymmapfile__write_byte_meth.html -->

## Pymmapfile.write_byte

 write_byte(char)

Writes a single character of data

#### Parameters

- char : str

 Single byte to be placed in buffer


<!-- page: Pymmapfile__write_meth.html -->

## Pymmapfile.write

 write(data)

Places data at current pos in buffer.

#### Parameters

- data : str

 Data to be written
