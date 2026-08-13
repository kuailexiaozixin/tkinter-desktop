# pywin32 对象文档 · 分卷 T

> 共 5 个对象，来源 https://mhammond.github.io/pywin32/<Object>.html


---

<!-- object: TLIBATTR -->


<!-- page: TLIBATTR.html -->

---

## TLIBATTR Object

 Type library attributes are represented as a tuple of:

#### Items

- [0] PyIID : IID

 The IID for the library

- [1] int : lcid

 The default locale ID for the library

- [2] int : syskind

 Identifies the target operating system platform

- [3] int : majorVersion

 The major version number of the library

- [4] int : minorVersion

 The minor version number of the library

- [5] int : flags

 Flags for the library.


---

<!-- object: TRACKMOUSEEVENT -->


<!-- page: TRACKMOUSEEVENT.html -->

---

## TRACKMOUSEEVENT Object

 A tuple of (dwFlags, hwndTrack, dwHoverTime)


---

<!-- object: TV_ITEM -->


<!-- page: TV_ITEM.html -->

---

## TV_ITEM Object

 Describes a TV_ITEM tuple, used by the PyCListCtrl object. A tuple of 8 items:
When returned from a win32ui function, will always be a tuple of size 8, and items may be None if not available.
When passed to a win32ui function, the tuple may be any length up to 8, and any item may be None.

#### Items

- [0] int : hItem

 Item handle

- [1] int : state

 Item state. If specified, the stateMask must also be specified.

- [2] int : stateMask

 Item state mask

- [3] string : text

 Item text

- [4] int : iImage

 Image list index of icon for non-seleted state.

- [5] int : iSelectedImage

 Offset of items selected image.

- [6] int : cChildren

 Number of child items.

- [7] int : lParam

 User defined integer param.


---

<!-- object: TYPEATTR -->


<!-- page: TYPEATTR.html -->

---

## TYPEATTR Object

 A TYPEATTR object represents a COM TYPEATTR structure.

#### Properties

- PyIID iid
 The IID

- int lcid
 The lcid

- int memidConstructor
 ID of constructor

- int memidDestructor
 ID of destructor

- int cbSizeInstance
 The size of an instance of this type

- int typekind
 The kind of type this information describes. One of the win32con.TKIND_* constants.

- int cFuncs
 Number of functions.

- int cVars
 Number of variables/data members.

- int cImplTypes
 Number of implemented interfaces.

- int cbSizeVft
 The size of this type's VTBL

- int cbAlignment
 Byte alignment for an instance of this type.

- int wTypeFlags
 One of the pythoncom TYPEFLAG_

- int wMajorVerNum
 Major version number.

- int wMinorVerNum
 Minor version number.

- TYPEDESC tdescAlias
 If TypeKind == pythoncom.TKIND_ALIAS, specifies the type for which this type is an alias.

- IDLDESC idldeskType
 IDL attributes of the described type.

#### Items

- [0] PyIID : IID

 The IID

- [1] int : lcid

 The lcid

- [2] int : memidConstructor

 ID of constructor

- [3] int : memidDestructor

 ID of destructor,

- [4] int : cbSizeInstance

 The size of an instance of this type

- [5] int : typekind

 The kind of type this information describes. One of the win32con.TKIND_* constants.

- [6] int : cFuncs

 Number of functions.

- [7] int : cVars

 Number of variables/data members.

- [8] int : cImplTypes

 Number of implemented interfaces.

- [9] int : cbSizeVft

 The size of this type's VTBL

- [10] int : cbAlignment

 Byte alignment for an instance of this type.

- [11] int : wTypeFlags

 One of the pythoncom TYPEFLAG_* constants

- [12] int : wMajorVerNum

 Major version number.

- [13] int : wMinorVerNum

 Minor version number.

- [14] TYPEDESC : obDescAlias

 If TypeKind == pythoncom.TKIND_ALIAS, specifies the type for which this type is an alias.

- [15] IDLDESC : obIDLDesc

 IDL attributes of the described type.


---

<!-- object: TYPEDESC -->


<!-- page: TYPEDESC.html -->

---

## TYPEDESC Object

 A typedesc is a complicated, recursive object, It may be either a simple Python type, or a tuple of (indirectType, object), where object may be a simple Python type, or a tuple of etc ...
