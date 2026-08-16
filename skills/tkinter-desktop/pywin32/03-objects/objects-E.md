# pywin32 对象文档 · 分卷 E

> 共 7 个对象，来源 https://mhammond.github.io/pywin32/<Object>.html


---

<!-- object: ELEMDESC -->


<!-- page: ELEMDESC.html -->

---

## ELEMDESC Object

 An ELEMDESC is respresented as a tuple of

#### Items

- [0] TYPEDESC : typeDesc

 The type description.

- [1] int : idlFlags

- [2] object : default

 If PARAMFLAG_FHASDEFAULT are set, then this is the default value.


---

<!-- object: EXP_DARWIN_LINK -->


<!-- page: EXP_DARWIN_LINK.html -->

---

## EXP_DARWIN_LINK Object

 Dictionary containing information for a EXP_DARWIN_LINK struct

#### Properties

- int Signature
 The type of data block, one of shellcon.*_SIG values

- str DarwinID
 The Windows Installer id for the link

- PyUNICODE wDarwinID
 The installer id as Unicode

- int Size
 Size of structure, ignored on input


---

<!-- object: EXP_SPECIAL_FOLDER -->


<!-- page: EXP_SPECIAL_FOLDER.html -->

---

## EXP_SPECIAL_FOLDER Object

 Dictionary containing information for a EXP_SPECIAL_FOLDER struct

#### Properties

- int Signature
 The type of data block, one of shellcon.*_SIG values

- int idSpecialFolder
 The special folder id of the target (shellcon.CSIDL_*)

- int Offset
 Offset into the link's PIDL

- int Size
 Size of structure, ignored on input


---

<!-- object: EXP_SZ_LINK -->


<!-- page: EXP_SZ_LINK.html -->

---

## EXP_SZ_LINK Object

 Dictionary containing information for an EXP_SZ_LINK or EXP_SZ_ICON struct

#### Properties

- int Signature
 The type of data block, one of shellcon.*_SIG values

- str Target
 The link's target or icon location

- PyUNICODE wTarget
 The target in Unicode form

- int Size
 Size of structure, ignored on input


---

<!-- object: EXTENSION_CONTROL_BLOCK -->


<!-- page: EXTENSION_CONTROL_BLOCK.html -->

---

## EXTENSION_CONTROL_BLOCK Object

 A python representation of an ISAPI EXTENSION_CONTROL_BLOCK.

#### Methods

- write

 A synonym for WriteClient, this allows you to 'print >> ecb'

- WriteClient

- GetServerVariable

- ReadClient

- SendResponseHeaders

- SetFlushFlag

- TransmitFile

- MapURLToPath

- DoneWithSession

- close

 A synonym for DoneWithSession.

- Redirect

- IsKeepAlive

- GetAnonymousToken

 Calls ServerSupportFunction with HSE_REQ_GET_ANONYMOUS_TOKEN or HSE_REQ_GET_UNICODE_ANONYMOUS_TOKEN

- GetImpersonationToken

- IsKeepConn

 Calls ServerSupportFunction with HSE_REQ_IS_KEEP_CONN

- ExecURL

 Calls ServerSupportFunction with HSE_REQ_EXEC_URL

- GetExecURLStatus

 Calls ServerSupportFunction with HSE_REQ_GET_EXEC_URL_STATUS

- IOCompletion

 Calls ServerSupportFunction with HSE_REQ_IO_COMPLETION

- ReportUnhealthy

 Calls ServerSupportFunction with HSE_REQ_REPORT_UNHEALTHY

- IOCallback

 A placeholder for a user-supplied callback function.

#### Properties

- integer Version
 Version info of this spec (read-only)

- int TotalBytes
 Total bytes indicated from client

- int AvailableBytes
 Available number of bytes

- int HttpStatusCode
 The status of the current transaction when the request is completed.

- bytes Method
 REQUEST_METHOD

- long ConnID
 Context number (read-only)

- bytes QueryString
 QUERY_STRING

- bytes PathInfo
 PATH_INFO

- bytes PathTranslated
 PATH_TRANSLATED

- bytes AvailableData
 Pointer to cbAvailable bytes

- bytes ContentType
 Content type of client data

- bytes LogData
 log data string


<!-- page: EXTENSION_CONTROL_BLOCK__DoneWithSession_meth.html -->

## EXTENSION_CONTROL_BLOCK.DoneWithSession

 DoneWithSession(status)

Calls ServerSupportFunction with HSE_REQ_DONE_WITH_SESSION

#### Parameters

- status=HSE_STATUS_SUCCESS : int

 An optional status. HSE_STATUS_SUCCESS_AND_KEEP_CONN is supported by IIS to keep the connection alive.


<!-- page: EXTENSION_CONTROL_BLOCK__ExecURL_meth.html -->

## EXTENSION_CONTROL_BLOCK.ExecURL

 int = ExecURL(url, method , clientHeaders , info , entity , flags )

Calls ServerSupportFunction with HSE_REQ_EXEC_URL

#### Parameters

- url : string

- method : string

- clientHeaders : string

- info : object

 Must be None

- entity : object

 Must be None

- flags : int

#### Comments

 This function is only available in IIS6 and later.


<!-- page: EXTENSION_CONTROL_BLOCK__GetAnonymousToken_meth.html -->

## EXTENSION_CONTROL_BLOCK.GetAnonymousToken

 int = GetAnonymousToken(metabase_path)

Calls ServerSupportFunction with HSE_REQ_GET_ANONYMOUS_TOKEN or HSE_REQ_GET_UNICODE_ANONYMOUS_TOKEN

#### Parameters

- metabase_path : string/unicode


<!-- page: EXTENSION_CONTROL_BLOCK__GetExecURLStatus_meth.html -->

## EXTENSION_CONTROL_BLOCK.GetExecURLStatus

 int = GetExecURLStatus()

Calls ServerSupportFunction with HSE_REQ_GET_EXEC_URL_STATUS

#### Win32 API References

- Search for HSE_EXEC_URL_STATUS at [msdn](https://learn.microsoft.com/en-ca/search/?terms=HSE_EXEC_URL_STATUS), [google](https://www.google.com/search?q=HSE_EXEC_URL_STATUS) or [google groups](https://groups.google.com/groups?q=HSE_EXEC_URL_STATUS).

#### Return Value

The result of a tuple of 3 integers - (uHttpStatusCode, uHttpSubStatus, dwWin32Error)


<!-- page: EXTENSION_CONTROL_BLOCK__GetImpersonationToken_meth.html -->

## EXTENSION_CONTROL_BLOCK.GetImpersonationToken

 int = GetImpersonationToken()

Calls ServerSupportFunction with HSE_REQ_GET_IMPERSONATION_TOKEN


<!-- page: EXTENSION_CONTROL_BLOCK__GetServerVariable_meth.html -->

## EXTENSION_CONTROL_BLOCK.GetServerVariable

 string = GetServerVariable(variable, default )

#### Parameters

- variable : string

- default : object

 If specified, the function will return this value instead of raising an error if the variable could not be fetched.

#### Return Value

The result is a string object, unless the server variable name begins with 'UNICODE_', in which case it is a unicode object - see the ISAPI docs for more details.


<!-- page: EXTENSION_CONTROL_BLOCK__IOCallback_meth.html -->

## EXTENSION_CONTROL_BLOCK.IOCallback

 None = IOCallback(ecb, arg , cbIO , dwError )

A placeholder for a user-supplied callback function.

#### Parameters

- ecb : EXTENSION_CONTROL_BLOCK

 The extension control block that is associated with the current, active request.

- arg : object

 The user-supplied argument supplied to the EXTENSION_CONTROL_BLOCK::IOCompletion function.

- cbIO : int

 An integer that contains the number of bytes of I/O in the last call.

- dwError : int

 The error code returned.

#### Comments

 This is not a function you can call, it describes the signature of the callback function supplied to the EXTENSION_CONTROL_BLOCK::IOCompletion function.

#### Return Value

The result of this function is ignored.


<!-- page: EXTENSION_CONTROL_BLOCK__IOCompletion_meth.html -->

## EXTENSION_CONTROL_BLOCK.IOCompletion

 int = IOCompletion(func, arg )

Set a callback that will be used for handling asynchronous I/O operations.

#### Parameters

- func : callable

 The function to call, as described by the EXTENSION_CONTROL_BLOCK::IOCallback method.

- arg=None : object

 Any object which will be supplied as an argument to the callback function.

#### Comments

 If you call this multiple times, the previous callback will be discarded.

 A reference to the callback and args are held until EXTENSION_CONTROL_BLOCK::DoneWithSession is called. If the callback function fails, DoneWithSession(HSE_STATUS_ERROR) will automatically be called and no further callbacks for the ECB will be made.


<!-- page: EXTENSION_CONTROL_BLOCK__IsKeepAlive_meth.html -->

## EXTENSION_CONTROL_BLOCK.IsKeepAlive

 IsKeepAlive()

#### Comments

 This method simply checks a HTTP_CONNECTION header for 'keep-alive', making it fairly useless. See EXTENSION_CONTROL_BLOCK::IsKeepCon


<!-- page: EXTENSION_CONTROL_BLOCK__IsKeepConn_meth.html -->

## EXTENSION_CONTROL_BLOCK.IsKeepConn

 int = IsKeepConn()

Calls ServerSupportFunction with HSE_REQ_IS_KEEP_CONN


<!-- page: EXTENSION_CONTROL_BLOCK__MapURLToPath_meth.html -->

## EXTENSION_CONTROL_BLOCK.MapURLToPath

 MapURLToPath()

Calls ServerSupportFunction with HSE_REQ_MAP_URL_TO_PATH


<!-- page: EXTENSION_CONTROL_BLOCK__ReadClient_meth.html -->

## EXTENSION_CONTROL_BLOCK.ReadClient

 string = ReadClient(nbytes)

#### Parameters

- nbytes : int

 Default is to read all available data.


<!-- page: EXTENSION_CONTROL_BLOCK__Redirect_meth.html -->

## EXTENSION_CONTROL_BLOCK.Redirect

 Redirect(url)

Calls ServerSupportFunction with HSE_REQ_SEND_URL_REDIRECT_RESP

#### Parameters

- url : string

 The URL to redirect to


<!-- page: EXTENSION_CONTROL_BLOCK__ReportUnhealthy_meth.html -->

## EXTENSION_CONTROL_BLOCK.ReportUnhealthy

 int = ReportUnhealthy(reason)

Calls ServerSupportFunction with HSE_REQ_REPORT_UNHEALTHY

#### Parameters

- reason=None : string

 An optional reason to be written to the log.


<!-- page: EXTENSION_CONTROL_BLOCK__SendResponseHeaders_meth.html -->

## EXTENSION_CONTROL_BLOCK.SendResponseHeaders

 SendResponseHeaders(reply, headers, keepAlive)

Calls ServerSupportFunction with HSE_REQ_SEND_RESPONSE_HEADER_EX

#### Parameters

- reply : string

- headers : string

- keepAlive=False : bool


<!-- page: EXTENSION_CONTROL_BLOCK__SetFlushFlag_meth.html -->

## EXTENSION_CONTROL_BLOCK.SetFlushFlag

 SetFlushFlag(flag)

Calls ServerSupportFunction with HSE_REQ_SET_FLUSH_FLAG.

#### Parameters

- flag : bool


<!-- page: EXTENSION_CONTROL_BLOCK__TransmitFile_meth.html -->

## EXTENSION_CONTROL_BLOCK.TransmitFile

 int = TransmitFile(callback, param , hFile , statusCode , BytesToWrite , Offset , head , tail , flags )

Calls ServerSupportFunction with HSE_REQ_TRANSMIT_FILE

#### Parameters

- callback : callable

- param : object

 Any object - passed as 2nd arg to callback.

- hFile : int

- statusCode : string

- BytesToWrite : int

- Offset : int

- head : string

- tail : string

- flags : int

#### Comments

 The callback is called with 4 args - (PyECB , param, cbIO, dwErrCode)


<!-- page: EXTENSION_CONTROL_BLOCK__WriteClient_meth.html -->

## EXTENSION_CONTROL_BLOCK.WriteClient

 int = WriteClient(data, reserved )

#### Parameters

- data : string/buffer

 The data to write

- reserved=0 : int

#### Return Value

the result is the number of bytes written.


---

<!-- object: ExportCallback -->


<!-- page: ExportCallback.html -->

---

## ExportCallback Object

 User-defined callback function used with win32file::ReadEncryptedFileRaw.
 Function is called with 3 parameters: (Data, CallbackContext, Length)
 Data: Read-only buffer containing the raw data read from the file. Must not be referenced outside of the callback function.
 CallbackContext: Arbitrary object passed to ReadEncryptedFileRaw.
 Length: Number of bytes in the Data buffer.
 On success, function should return ERROR_SUCCESS. Otherwise, it can return a win32 error code, or simply raise an exception.


---

<!-- object: error -->


<!-- page: error.html -->

---

## error Object

 An exception raised when a win32 error occurs

#### Comments

 This error is defined in the pywintypes module, but most of the win32 modules expose this error object via their own error attribute - eg, win32api.error is pywintypes.error is win32gui.error.

 This exception is derived from the standard Python Exception object.

 Instances of these exception can be accessed via indexing or via attribute access. Attribute access is more forwards compatible with Python 3, so is recommended.

 See also com_error

#### Items

- [0] int : winerror

 The windows error code.

- [1] string : funcname

 The name of the windows function that failed.

- [2] string : strerror

 The error message.
