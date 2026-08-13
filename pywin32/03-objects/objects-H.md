# pywin32 对象文档 · 分卷 H

> 共 8 个对象，来源 https://mhammond.github.io/pywin32/<Object>.html


---

<!-- object: HSE_VERSION_INFO -->


<!-- page: HSE_VERSION_INFO.html -->

---

## HSE_VERSION_INFO Object

 An object used by ISAPI GetExtensionVersion

#### Properties

- string ExtensionDesc
 The description of the extension.


---

<!-- object: HTTP_FILTER_AUTHENT -->


<!-- page: HTTP_FILTER_AUTHENT.html -->

---

## HTTP_FILTER_AUTHENT Object

 A Python representation of an ISAPI HTTP_FILTER_AUTHENT structure.

#### Properties

- string User

- string Password


---

<!-- object: HTTP_FILTER_CONTEXT -->


<!-- page: HTTP_FILTER_CONTEXT.html -->

---

## HTTP_FILTER_CONTEXT Object

 A Python representation of an ISAPI HTTP_FILTER_CONTEXT structure.

#### Methods

- GetData

- GetServerVariable

- WriteClient

- AddResponseHeaders

 Specifies a response header for IIS to send to the client.

- write

 A synonym for WriteClient, this allows you to 'print >> fc'

- SendResponseHeader

- DisableNotifications

#### Properties

- int Revision
 (read-only)

- bool fIsSecurePort
 (read-only)

- int NotificationType
 (read-only)

- object FilterContext
 Any object you wish to associate with the request.


<!-- page: HTTP_FILTER_CONTEXT__AddResponseHeaders_meth.html -->

## HTTP_FILTER_CONTEXT.AddResponseHeaders

 AddResponseHeaders(data, reserverd)

#### Parameters

- data : string

- reserverd=0 : int


<!-- page: HTTP_FILTER_CONTEXT__DisableNotifications_meth.html -->

## HTTP_FILTER_CONTEXT.DisableNotifications

 DisableNotifications(flags)

#### Parameters

- flags : int


<!-- page: HTTP_FILTER_CONTEXT__GetData_meth.html -->

## HTTP_FILTER_CONTEXT.GetData

 object = GetData()

Obtains the data passed to The HttpFilterProc function. This is not techinally part of the HTTP_FILTER_CONTEXT structure, but packaged here for convenience.

#### Return Value

The result depends on the value of HTTP_FILTER_CONTEXT::NotificationType

| | NotificationType | Result type
| |

---

 |

---

| | SF_NOTIFY_URL_MAP | HTTP_FILTER_URL_MAP
| | SF_NOTIFY_PREPROC_HEADERS | HTTP_FILTER_PREPROC_HEADERS
| | SF_NOTIFY_LOG | HTTP_FILTER_LOG
| | SF_NOTIFY_SEND_RAW_DATA | HTTP_FILTER_RAW_DATA
| | SF_NOTIFY_READ_RAW_DATA | HTTP_FILTER_RAW_DATA
| | SF_NOTIFY_AUTHENTICATION | HTTP_FILTER_AUTHENT


<!-- page: HTTP_FILTER_CONTEXT__GetServerVariable_meth.html -->

## HTTP_FILTER_CONTEXT.GetServerVariable

 string = GetServerVariable(variable, default )

#### Parameters

- variable : string

- default : object

 If specified, the function will return this value instead of raising an error if the variable could not be fetched.

#### Return Value

The result is a string object, unless the server variable name begins with 'UNICODE_', in which case it is a unicode object - see the ISAPI docs for more details.


<!-- page: HTTP_FILTER_CONTEXT__SendResponseHeader_meth.html -->

## HTTP_FILTER_CONTEXT.SendResponseHeader

 SendResponseHeader(status, header)

#### Parameters

- status : string

- header : string


<!-- page: HTTP_FILTER_CONTEXT__WriteClient_meth.html -->

## HTTP_FILTER_CONTEXT.WriteClient

 WriteClient(data, reserverd)

#### Parameters

- data : string

- reserverd=0 : int


---

<!-- object: HTTP_FILTER_LOG -->


<!-- page: HTTP_FILTER_LOG.html -->

---

## HTTP_FILTER_LOG Object

 A Python representation of an ISAPI HTTP_FILTER_LOG structure.

#### Properties

- string ClientHostName

- string ClientUserName

- string ServerName

- string Operation

- string Target

- string Parameters

- int HttpStatus

- int HttpStatus


---

<!-- object: HTTP_FILTER_PREPROC_HEADERS -->


<!-- page: HTTP_FILTER_PREPROC_HEADERS.html -->

---

## HTTP_FILTER_PREPROC_HEADERS Object

 A Python representation of an ISAPI HTTP_FILTER_PREPROC_HEADERS structure.

#### Methods

- GetHeader

- SetHeader

- AddHeader


<!-- page: HTTP_FILTER_PREPROC_HEADERS__AddHeader_meth.html -->

## HTTP_FILTER_PREPROC_HEADERS.AddHeader

 AddHeader()


<!-- page: HTTP_FILTER_PREPROC_HEADERS__GetHeader_meth.html -->

## HTTP_FILTER_PREPROC_HEADERS.GetHeader

 string = GetHeader(header, default )

#### Parameters

- header : string

- default : object

 If specified, this will be returned on error.


<!-- page: HTTP_FILTER_PREPROC_HEADERS__SetHeader_meth.html -->

## HTTP_FILTER_PREPROC_HEADERS.SetHeader

 SetHeader(name, val)

#### Parameters

- name : string

- val : string


---

<!-- object: HTTP_FILTER_RAW_DATA -->


<!-- page: HTTP_FILTER_RAW_DATA.html -->

---

## HTTP_FILTER_RAW_DATA Object

 A Python representation of an ISAPI HTTP_FILTER_RAW_DATA structure.

#### Properties

- string InData


---

<!-- object: HTTP_FILTER_URL_MAP -->


<!-- page: HTTP_FILTER_URL_MAP.html -->

---

## HTTP_FILTER_URL_MAP Object

 A Python representation of an ISAPI HTTP_FILTER_URL_MAP structure.

#### Properties

- string URL

- string PhysicalPath


---

<!-- object: HTTP_FILTER_VERSION -->


<!-- page: HTTP_FILTER_VERSION.html -->

---

## HTTP_FILTER_VERSION Object

 A Python interface to the ISAPI HTTP_FILTER_VERSION structure.

#### Properties

- int ServerFilterVersion
 (read-only)

- int FilterVersion

- int Flags

- string FilterDesc
