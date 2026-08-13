# 模块 mapi

> 来源：https://mhammond.github.io/pywin32/mapi.html （及其成员页，已全部内联）

## Module mapi

 A COM interface to MAPI

#### Methods

- HexFromBin

 converts a binary number into a string representation of a hexadecimal number.

- BinFromHex

 converts a hexadecimal number into a binary string

- MAPIUninitialize

 Decrements the reference count, cleans up, and deletes per-instance global data for the MAPI DLL.

- MAPIInitialize

 Increments the MAPI subsystem reference count and initializes global data for the MAPI DLL.

- MAPILogonEx

- MAPIAdminProfiles

- HrQueryAllRows

- RTFSync

- WrapCompressedRTFStream

- WrapCompressedRTFStreamEx

- OpenIMsgSession

- CloseIMsgSession

- OpenIMsgOnIStg

 Builds a new IMessage object on top of an existing OLE IStorage object, to be used within a message session.

- RTFStreamToHTML

- OpenStreamOnFile

 Allocates and initializes an OLE IStream object to access the contents of a file.

- OpenStreamOnFileW

 Allocates and initializes an OLE IStream object to access the contents of a file.

- HrGetOneProp

 Retrieves the value of a single property from an IMAPIProp object.

- HrSetOneProp

 Sets the value of a single property on a IMAPIProp object.

- HrAllocAdviseSink

 Creates an advise sink object, given a context specified by the calling implementation and a callback function to be triggered by an event notification.

- HrThisThreadAdviseSink

 Creates an advise sink that wraps an existing advise sink for thread safety.


---

# mapi 成员详细文档（共 20 项）


---

<!-- page: mapi__BinFromHex_meth.html -->

## mapi.BinFromHex

 PyUnicode = BinFromHex(val)

converts a hexadecimal number into a binary string

#### Parameters

- val : string/PyUnicode

 The string to be converted.


---

<!-- page: mapi__CloseIMsgSession_meth.html -->

## mapi.CloseIMsgSession

 CloseIMsgSession()


---

<!-- page: mapi__HexFromBin_meth.html -->

## mapi.HexFromBin

 PyUnicode = HexFromBin(val)

converts a binary number into a string representation of a hexadecimal number.

#### Parameters

- val : string

 Converts an EntryID into a hex string representation.

#### Comments

 Note: This function may not be supported in future versions of MAPI.


---

<!-- page: mapi__HrAllocAdviseSink_meth.html -->

## mapi.HrAllocAdviseSink

 PyIMAPIAdviseSink = HrAllocAdviseSink(callback, context )

Creates an advise sink object, given a context specified by the calling implementation and a callback function to be triggered by an event notification.

#### Parameters

- callback : function

 OnNotify callback function

- context : object

 Context data to be passed to the callback


---

<!-- page: mapi__HrGetOneProp_meth.html -->

## mapi.HrGetOneProp

 item = HrGetOneProp(prop, propTag )

Retrieves the value of a single property from an IMAPIProp object.

#### Parameters

- prop : PyIMAPIProp

 Object to retrieve property value from.

- propTag : ULONG

 The property tag to open.


---

<!-- page: mapi__HrQueryAllRows_meth.html -->

## mapi.HrQueryAllRows

 SRowSet = HrQueryAllRows(table, properties , restrictions , sortOrderSet , rowsMax )

#### Parameters

- table : PyIMAPITable

- properties : PySPropTagArray

 A sequence of property tags indicating table columns. These tags are used to select the specific columns to be retrieved. If this parameter is None, HrQueryAllRows retrieves the entire column set of the current table view passed in the table parameter.

- restrictions : PySRestriction

 Defines the retrieval restrictions. If this parameter is None, HrQueryAllRows makes no restrictions.

- sortOrderSet : PySSortOrderSet

 Identifies the sort order of the columns to be retrieved. If this parameter is None, the default sort order for the table is used.

- rowsMax : int

 Maximum number of rows to be retrieved. If the value of the rowsMax parameter is zero, no limit on the number of rows retrieved is set.


---

<!-- page: mapi__HrSetOneProp_meth.html -->

## mapi.HrSetOneProp

 item = HrSetOneProp(prop, propValue )

Sets the value of a single property on a IMAPIProp object.

#### Parameters

- prop : PyIMAPIProp

 Object to set property value on.

- propValue : PySPropValue

 Property value to set.


---

<!-- page: mapi__HrThisThreadAdviseSink_meth.html -->

## mapi.HrThisThreadAdviseSink

 PyIMAPIAdviseSink = HrThisThreadAdviseSink(object)

Creates an advise sink that wraps an existing advise sink for thread safety.

#### Parameters

- object : PyIMAPIAdviseSink

 The advise sink to be wrapped.


---

<!-- page: mapi__MAPIAdminProfiles_meth.html -->

## mapi.MAPIAdminProfiles

 PyIProfAdmin = MAPIAdminProfiles(fFlags)

#### Parameters

- fFlags : int


---

<!-- page: mapi__MAPIInitialize_meth.html -->

## mapi.MAPIInitialize

 MAPIInitialize(init)

Increments the MAPI subsystem reference count and initializes global data for the MAPI DLL.

#### Parameters

- init : MAPIINIT_0

 MAPI Initialization flags.


---

<!-- page: mapi__MAPILogonEx_meth.html -->

## mapi.MAPILogonEx

 PyIMAPISession = MAPILogonEx(uiParam, profileName , password , flags )

#### Parameters

- uiParam : int

 Handle to the window to which the logon dialog box is modal. If no dialog box appears during the call, the uiParam parameter is ignored. This parameter can be zero.

- profileName : string

 A string that contains the name of the profile to use when the user logs on. This string is limited to 64 characters.

- password=None : string

 A string that contains the password of the profile. The password parameter must be None.

- flags=0 : int


---

<!-- page: mapi__MAPIUninitialize_meth.html -->

## mapi.MAPIUninitialize

 MAPIUninitialize()

Decrements the reference count, cleans up, and deletes per-instance global data for the MAPI DLL.


---

<!-- page: mapi__OpenIMsgOnIStg_meth.html -->

## mapi.OpenIMsgOnIStg

 PyIMessage = OpenIMsgOnIStg(session, support , storage , callback , callbackData , flags )

Builds a new IMessage object on top of an existing OLE IStorage object, to be used within a message session.

#### Parameters

- session : object

- support : PyIMAPISupport

 May be None

- storage : PyIStorage

 A PyIStorage object that is open and has read-only or read/write access. Because IMessage does not support write-only access, OpenIMsgOnIStg does not accept a storage object opened in write-only mode.

- callback=None : object

 Only None is supported.

- callbackData=0 : int

- flags=0 : int


---

<!-- page: mapi__OpenIMsgSession_meth.html -->

## mapi.OpenIMsgSession

 object = OpenIMsgSession()


---

<!-- page: mapi__OpenStreamOnFileW_meth.html -->

## mapi.OpenStreamOnFileW

 PyIStream = OpenStreamOnFileW(filename, flags , prefix )

Allocates and initializes an OLE IStream object to access the contents of a file.

#### Parameters

- filename : unicode

- flags=0 : int

- prefix=None : unicode


---

<!-- page: mapi__OpenStreamOnFile_meth.html -->

## mapi.OpenStreamOnFile

 PyIStream = OpenStreamOnFile(filename, flags , prefix )

Allocates and initializes an OLE IStream object to access the contents of a file.

#### Parameters

- filename : string

- flags=0 : int

- prefix=None : string


---

<!-- page: mapi__RTFStreamToHTML_meth.html -->

## mapi.RTFStreamToHTML

 RTFStreamToHTML(The stream to read the uncompressed RTF from)

#### Parameters

- The stream to read the uncompressed RTF from : PyIStream


---

<!-- page: mapi__RTFSync_meth.html -->

## mapi.RTFSync

 int = RTFSync(message, flags )

#### Parameters

- message : PyIMessage

 The message.

- flags : int


---

<!-- page: mapi__WrapCompressedRTFStreamEx_meth.html -->

## mapi.WrapCompressedRTFStreamEx

 (PyIStream, ULONG) = WrapCompressedRTFStreamEx()

#### Return Value

Result is a tuple of (bodyStream, bodyType);


---

<!-- page: mapi__WrapCompressedRTFStream_meth.html -->

## mapi.WrapCompressedRTFStream

 PyIStream = WrapCompressedRTFStream(stream, flags )

#### Parameters

- stream : PyIStream

 Message stream

- flags : int
