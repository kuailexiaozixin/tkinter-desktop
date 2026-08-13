# win32/Demos/win32wnet/netresource.htm

> 来源：https://github.com/mhammond/pywin32/blob/main/win32/Demos/win32wnet/netresource.htm
> （该文档在 mhammond.github.io 文档站已 404，仅仓库内存在，此处为全文转录）

## WIN32WNET

#### PyNETRESOURCE

The PyNETRESOURCE object is the Python encapsulation of the Win32 NETRESOURCE structure used with WNetXXX networking functions and other Win32 APIs. The implementation can be compiled for Ascii or Unicode and has been tested on Python 1.5.1.

#### PyNETRESOURCE Object Members:

- NETRESOURCE m_nr -- the actual NETRESOURCE data structure
- TCHAR szLName -- local storage for the lpLocalName member of the NETRESOURCE structure.
 The names are stored locally and are not stored as native Python strings.String length is 256 TCHARs maximum.

- TCHAR szRName -- lpRemoteName storage. See szLName.
- TCHAR szProv -- lpProvider storage. See szLName.
- TCHAR szComment -- lpComment storage. See szLName.

#### Relevant Python Methods:

- x = win32wnet.NETRESOURCE() will instantiate a new PyNETRESOURCE Object
- x.dwScope, x.dwType, x.dwDisplayType, x.dwUsage -- Integer attributes corresponding to the NETRESOURCE structure members. Attributes are both readable and writeable using standard Python attribute semantics.
- X.lpLocalName, x.lpRemoteName, x.lpComment, x.lpProvider -- String pointers in the NETRESOURCE structure. They are wrapped to point to szLName, etc.... These strings are not stored as Python strings and are therefore both readable and writeable. Using standard Python attribute semantics, the attributes return Python strings upon query and take python strings as input.

#### 'C' Programming Interface:

- BOOL PyWinObject_AsNETRESOURCE(PyObject *ob, NETRESOURCE **ppNetresource, BOOL bNoneOK = TRUE);
- PyObject *PyWinObject_FromNETRESOURCE(const NETRESOURCE *pNetresource

#### WIN32WNET Functions

win32wnet.py is the Python extension providing access to the WNetXXX Win32APIs. This module is fully compilable for both Ascii and Unicode. This module has been tested with Python 1.5.1 and Windows NT workstation 4.0 SP3.

- WNetAddConnection2 (

 INTEGER Type, - RESOURCETYPE_DISK, RESOURCETYPE_PRINT, or RESOURCETYPE_ANY
 STRING LocalName, - String or None
 STRING RemoteName, - String (required to be in network format
 STRING ProviderName, - String or None
 STRING Username,
 STRING Password
 )
- Returns: PyNone
 The WNetAddConnection2 function makes a connection to a network resource. The function can redirect a local device to the network resource. The first four parameters correspond to the NETRESOURCE object that is being constructed for the Win32API call. UserName and Password are obvious. Passing None for UserName and Password will attempt a NULL session connection.
 Note that this function has since been updated to optionally accept a NETRESOURCE object making its signature almost identical to the win32 version - see the pywin32 help for more information. Also note that WNetAddConnection3 is also implemented, which is similar to this function but accepts a HWND as the first (or named) param.

- WNetCancelConnection2 (

 STRING Name,
 INTEGER Flags,
 INTEGER Force
 )
- Returns: PyNone
 The WNetCancelConnection2 function breaks an existing network connection. It can also be used to remove remembered network connections that are not currently connected. The Python parameters correspond directly to the Win32API call parameters. The Name string is the name of the connection you wish to drop (i.e. O:, \\bexar\support, etc...). The Flags parameter indicates wether the permanent connection information should be updated or not. A value of zero indicates that no stored information about the connection should be updated. A value of CONNECT_UPDATE_PROFILE indicates that the persistent connection information for this connection should be updated (deleted). the Force parameter is a boolean indicated whether connection termination should be forced (i.e. open files and connects ignored).

- WNetOpenEnum (

 INTEGER Scope, - Specifies the scope of the enumeration.
 INTEGER Type, - Specifies the resource types to enumerate.
 INTEGER Usage, - Specifies the resource usage to be enumerated.
 OBJECT NetResource - Python PyNETRESOURCE object.
 )

- Returns: PyHANDLE
 The WNetOpenEnum function starts an enumeration of network resources or existing connections. For full documentation, see the Win32API references.

- WNetCloseEnum (

 OBJECT Handle - PyHANDLE object returned from a previous WNetOpenEnum call.
 )
- Returns: PyNone
 Closes a PyHANDLE that represents an Open Enumeration (from WNetOpenEnum)

- WNetEnumResource (

 OBJECT Handle, - HANDLE (in form of PyHANDLE) to an open Enumeration Object (from WNetOpenEnum)
 OPTIONAL INTEGER - how many items to try to recieve---0 will default to 64.
 )
- Returns: PyList
 The list contains PyNETRESOURCE objects. The total number of PyNETRESOURCE objects will be <= number requested (excepting the default behavior of requesting 0, which returns up to 64)
 Implements the WNetEnumResource Win32 API call. Successive calls to WNetEnumResource will enumerate starting where the previous call stopped. That is, the enumeration is not reset on successive calls UNLESS the enumeration handle is closed and reopened. This lets you process an enumeration in small chunks (as small as 1 item at a time) and still fully enumerate a network object! Network resources are not guaranteed to be returned in any particular order.
