# 模块 pywintypes

> 来源：https://mhammond.github.io/pywin32/pywintypes.html （及其成员页，已全部内联）

## Module pywintypes

 A module which supports common Windows types.

#### Methods

- DosDateTimeToTime

 Converts an MS-DOS Date/Time to a standard Time object

- UnicodeFromRaw

 Creates a new string object from raw binary data

- IsTextUnicode

 Determines whether a buffer probably contains a form of Unicode text.

- OVERLAPPED

 Creates a new PyOVERLAPPED object

- IID

 Makes an PyIID object from a string.

- Time

 Makes a PyDateTime object from the argument.

- Time

 Makes a PyDateTime object from the argument.

- CreateGuid

 Creates a new, unique GUIID.

- ACL

 Creates a new PyACL object.

- SID

 Creates a new PySID object.

- SECURITY_ATTRIBUTES

 Creates a new PySECURITY_ATTRIBUTES object.

- SECURITY_DESCRIPTOR

 Creates a new PySECURITY_DESCRIPTOR object.

- HANDLE

 Creates a new PyHANDLE object.

- HKEY

 Creates a new PyHKEY object.

- WAVEFORMATEX

 Creates a new PyWAVEFORMATEX object.


---

# pywintypes 成员详细文档（共 15 项）


---

<!-- page: pywintypes__ACL_meth.html -->

## pywintypes.ACL

 PyACL = ACL(bufSize)

Creates a new ACL object

#### Parameters

- bufSize=64 : int

 The size for the ACL.


---

<!-- page: pywintypes__CreateGuid_meth.html -->

## pywintypes.CreateGuid

 PyIID = CreateGuid()

Creates a new, unique GUIID.


---

<!-- page: pywintypes__DosDateTimeToTime_meth.html -->

## pywintypes.DosDateTimeToTime

 PyDateTime = DosDateTimeToTime()

Converts an MS-DOS Date/Time to a standard Time object.


---

<!-- page: pywintypes__HANDLE_meth.html -->

## pywintypes.HANDLE

 PyHANDLE = HANDLE()

Creates a new HANDLE object


---

<!-- page: pywintypes__HKEY_meth.html -->

## pywintypes.HKEY

 PyHKEY = HKEY()

Creates a new HKEY object


---

<!-- page: pywintypes__IID_meth.html -->

## pywintypes.IID

 PyIID = IID(iidString, is_bytes )

Creates a new IID object

#### Parameters

- iidString : string/Unicode

 A string representation of an IID, or a ProgID.

- is_bytes=False : bool

 Indicates if the first param is actually the bytes of an IID structure.


---

<!-- page: pywintypes__IsTextUnicode_meth.html -->

## pywintypes.IsTextUnicode

 int, int = IsTextUnicode(str, flags )

Determines whether a buffer probably contains a form of Unicode text.

#### Parameters

- str : string

 The string containing the binary data.

- flags : int

 Determines the specific tests to make

#### Return Value

The function returns (result, flags), both integers.
result is nonzero if the data in the buffer passes the specified tests.
result is zero if the data in the buffer does not pass the specified tests.
In either case, flags contains the results of the specific tests the function applied to make its determination.


---

<!-- page: pywintypes__OVERLAPPED_meth.html -->

## pywintypes.OVERLAPPED

 PyOVERLAPPED = OVERLAPPED()

Creates a new OVERLAPPED object


---

<!-- page: pywintypes__SECURITY_ATTRIBUTES_meth.html -->

## pywintypes.SECURITY_ATTRIBUTES

 PySECURITY_ATTRIBUTES = SECURITY_ATTRIBUTES()

Creates a new SECURITY_ATTRIBUTES object


---

<!-- page: pywintypes__SECURITY_DESCRIPTOR_meth.html -->

## pywintypes.SECURITY_DESCRIPTOR

 PySECURITY_DESCRIPTOR = SECURITY_DESCRIPTOR()

Creates a new SECURITY_DESCRIPTOR object

#### Alternative Parameters

- data

 A buffer (eg, a string) with the raw bytes for the security descriptor.


---

<!-- page: pywintypes__SID_meth.html -->

## pywintypes.SID

 PySID = SID(bufSize)

Creates a new SID object

#### Parameters

- bufSize=32 : int

 Size for the SID buffer

#### Alternative Parameters

- buffer

 A raw data buffer, assumed to hold the SID data.

#### Alternative Parameters

- idAuthority

 The identifier authority.

- subAuthorities

 A list of sub authorities.


---

<!-- page: pywintypes__TimeStamp_meth.html -->

## pywintypes.TimeStamp

 PyDateTime = TimeStamp(timestamp)

Creates a new time object.

#### Parameters

- timestamp : int

 An integer timestamp representation.


---

<!-- page: pywintypes__Time_meth.html -->

## pywintypes.Time

 PyDateTime = Time(timeRepr)

Creates a new time object.

#### Parameters

- timeRepr : object

 An integer/float/tuple time representation.

#### Comments

 Note that the parameter can be any object that supports int(object) or another PyDateTime object.
The integer should be as defined by the Python time module. See the description of the PyDateTime object for more information.


---

<!-- page: pywintypes__UnicodeFromRaw_meth.html -->

## pywintypes.UnicodeFromRaw

 string = UnicodeFromRaw(str)

Creates a new Unicode object from raw binary data

#### Parameters

- str : string/buffer

 The string containing the binary data.


---

<!-- page: pywintypes__WAVEFORMATEX_meth.html -->

## pywintypes.WAVEFORMATEX

 PyWAVEFORMATEX = WAVEFORMATEX()

Creates a new WAVEFORMATEX object
