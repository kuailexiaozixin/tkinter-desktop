# pywin32 对象文档 · 分卷 S

> 共 12 个对象，来源 https://mhammond.github.io/pywin32/<Object>.html


---

<!-- object: SCROLLINFO_tuple -->


<!-- page: SCROLLINFO_tuple.html -->

---

## SCROLLINFO tuple Object

 Tuple representing a SCROLLINFO struct

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

 When returned from a method, will always be a tuple of size 6, and items may be None if not available.

 When passed as an arg, it must have the addn mask attribute, but all other items may be None, or not exist.


---

<!-- object: SC_ACTION -->


<!-- page: SC_ACTION.html -->

---

## SC_ACTION Object

 Tuple of 2 ints (Type,Delay) used to represent an SC_ACTION structure

#### Properties

- int Type
 One of SC_ACTION_NONE, SC_ACTION_REBOOT, SC_ACTION_RESTART, SC_ACTION_RUN_COMMAND

- int Delay
 Time delay before specified action is taken (in milliseconds)


---

<!-- object: SERVICE_FAILURE_ACTIONS -->


<!-- page: SERVICE_FAILURE_ACTIONS.html -->

---

## SERVICE_FAILURE_ACTIONS Object

 A dictionary representing a SERVICE_FAILURE_ACTIONS structure

#### Properties

- int ResetPeriod
 Indicates how many seconds to wait to reset the failure count, can be INFINITE

- string RebootMsg
 Message displayed when reboot action is taken

- string Command
 Command line to execute for SC_ACTION_RUN_COMMAND

- tuple Actions
 A tuple of SC_ACTION tuples


---

<!-- object: SERVICE_STATUS -->


<!-- page: SERVICE_STATUS.html -->

---

## SERVICE_STATUS Object

 A Win32 service status object is represented by a tuple:

#### Items

- [0] int : serviceType

 The type of service.

- [1] int : serviceState

 The current state of the service.

- [2] int : controlsAccepted

 The controls the service accepts.

- [3] int : win32ExitCode

 The win32 error code for the service.

- [4] int : serviceSpecificErrorCode

 The service specific error code.

- [5] int : checkPoint

 The checkpoint reported by the service.

- [6] int : waitHint

 The wait hint reported by the service.


---

<!-- object: SHFILEINFO -->


<!-- page: SHFILEINFO.html -->

---

## SHFILEINFO Object

 A tuple representing a SHFILEINFO structure Represented as a tuple of (hIcon, iIcon, dwAttributes, displayName, typeName)


---

<!-- object: SHFILEOPSTRUCT -->


<!-- page: SHFILEOPSTRUCT.html -->

---

## SHFILEOPSTRUCT Object

 A tuple representing a Win32 shell SHFILEOPSTRUCT structure, used with shell::SHFileOperation

#### Comments

 From and To can contain multiple file names concatenated with a single null between them, eg "c:\\file1.txt\\0c:\\file2.txt". A double null terminator will be appended automatically. If To specifies multiple file names, flags must contain FOF_MULTIDESTFILES

#### Items

- [0] int : hwnd

 Handle of window in which to display status messages

- [1] int : wFunc

 One of the shellcon.FO_* values

- [2] string : From

 String containing source file name(s) separated by nulls

- [3] string : To

 String containing destination file name(s) separated by nulls, can be None

- [4] int : flags

 Combination of shellcon.FOF_* flags. Default=0

- [5] None : NameMappings

 Maps input file names to their new names. This is actually output, and must be None if passed as input. Default=None

- [6] string : ProgressTitle

 Title for progress dialog (flags must contain FOF_SIMPLEPROGRESS). Default=None


---

<!-- object: SI_ACCESS -->


<!-- page: SI_ACCESS.html -->

---

## SI_ACCESS Object

 Tuple of 4 items representing SI_ACCESS struct

#### Items

- [0] PyIID : guid

 GUID identifying the object type permissions apply to. Use GUID_NULL for object itself

- [1] int : mask

 Bitmask of permissions

- [2] PyUNICODE : Name

 Description to be displayed for the permissions

- [3] int : Flags

 Indicates which pages will display the permissions, and how they may be inherited. Combination of SI_ACCESS_SPECIFIC, SI_ACCESS_GENERAL, SI_ACCESS_CONTAINER, SI_ACCESS_PROPERTY, CONTAINER_INHERIT_ACE, INHERIT_ONLY_ACE, OBJECT_INHERIT_ACE


---

<!-- object: SI_INHERIT_TYPE -->


<!-- page: SI_INHERIT_TYPE.html -->

---

## SI_INHERIT_TYPE Object

 Tuple of 3 items describing a method of inheritance

#### Items

- [0] PyIID : guid

 GUID for type of child object, GUID_NULL indicates object itself

- [1] int : Flags

 ACE inheritance flags, combination of OBJECT_INHERIT_ACE, CONTAINER_INHERIT_ACE, INHERIT_ONLY_ACE

- [2] PyUNICODE : Name

 Description that will be displayed on the Advanced page


---

<!-- object: SI_OBJECT_INFO -->


<!-- page: SI_OBJECT_INFO.html -->

---

## SI_OBJECT_INFO Object

 Six-tuple representing SI_OBJECT_INFO struct

#### Items

- [0] int : Flags

 Combination of ntsecuritycon.SI_* flags specifying options

- [1] PyHANDLE : hInstance

 Handle to a module containing string resources (not supported yet, use 0)

- [2] PyUNICODE : ServerName

 Name of authenticating server if not local machine

- [3] PyUNICODE : ObjectName

 Name of object whose security will be displayed

- [4] PyUNICODE : PageTitle

 Title to be used for basic propery sheet (SI_PAGE_TITLE must be passed in Flags)

- [5] PyIID : ObjectType

 GUID identifying the type of object, usually IID_NULL


---

<!-- object: STATSTG -->


<!-- page: STATSTG.html -->

---

## STATSTG Object

 A tuple representing a STATSTG structure

#### Items

- [0] string : name

 The name of the storage object

- [1] int : type

 Indicates the type of storage object. This is one of the values from the storagecon.STGTY_* values.

- [2] ULARGE_INTEGER : size

 Specifies the size in bytes of the stream or byte array.

- [3] PyDateTime : modificationTime

 Indicates the last modification time for this storage, stream, or byte array.

- [4] PyDateTime : creationTime

 Indicates the creation time for this storage, stream, or byte array.

- [5] PyDateTime : accessTime

 Indicates the last access time for this storage, stream or byte array.

- [6] int : mode

 Indicates the access mode specified when the object was opened. This member is only valid in calls to Stat methods.

- [7] int : locksSupported

 Indicates the types of region locking supported by the stream or byte array. See the storagecon.LOCKTYPES_* constants for the values available. This member is not used for storage objects.

- [8] PyIID : clsid

 Indicates the class identifier for the storage object; set to CLSID_NULL for new storage objects. This member is not used for streams or byte arrays.

- [9] int : stateBits

 Indicates the current state bits of the storage object, that is, the value most recently set by the PyIStorage::SetStateBits method. This member is not valid for streams or byte arrays.

- [10] int : storageFormat

 Indicates the format of the storage object. This is one of the values from the STGFMT_* constants. In some Win32 API documentation, this member is known as 'reserved'


---

<!-- object: sspi.ClientAuth -->


<!-- page: sspi.ClientAuth.html -->

---

## sspi.ClientAuth Object

 Manages the client side of an SSPI authentication handshake

#### Methods

- authorize

 Perform *one* step of the client authentication process. Pass None for the first round


<!-- page: sspi.ClientAuth__authorize_meth.html -->

## sspi.ClientAuth.authorize

 authorize()

Perform *one* step of the client authentication process. Pass None for the first round


<!-- page: sspi.ClientAuth__authorize_meth_1.html -->

## sspi.ClientAuth.authorize

 authorize(self, sec_buffer_in)

Perform *one* step of the client authentication process. Pass None for the first round

#### Parameters

- self :

 self

- sec_buffer_in :

 sec_buffer_in


---

<!-- object: sspi.ServerAuth -->


<!-- page: sspi.ServerAuth.html -->

---

## sspi.ServerAuth Object

 Manages the server side of an SSPI authentication handshake

#### Methods

- authorize

 Perform *one* step of the server authentication process.


<!-- page: sspi.ServerAuth__authorize_meth.html -->

## sspi.ServerAuth.authorize

 authorize()

Perform *one* step of the server authentication process.


<!-- page: sspi.ServerAuth__authorize_meth_1.html -->

## sspi.ServerAuth.authorize

 authorize(self, sec_buffer_in)

Perform *one* step of the server authentication process.

#### Parameters

- self :

 self

- sec_buffer_in :

 sec_buffer_in
