# 模块 win32ras

> 来源：https://mhammond.github.io/pywin32/win32ras.html （及其成员页，已全部内联）

## Module win32ras

 A module encapsulating the Windows Remote Access Service (RAS) API.

#### Methods

- CreatePhonebookEntry

 Creates a new phonebook entry. The function displays a dialog box into which the user can enter information about the entry.

- Dial

 Establishes a RAS connection to a RAS server.

- EditPhonebookEntry

 Creates a new phonebook entry. The function displays a dialog box into which the user can enter information about the entry

- EnumConnections

 Returns a list of tuples, one for each active connection.

- EnumEntries

 Returns a list of tuples, one for each phonebook entry.

- GetConnectStatus

 Returns a tuple with connection information.

- RasGetEapUserIdentity

 Retrieves identity information for the current user. Use this information to call RasDial with a phone-book entry that requires Extensible Authentication Protocol (EAP).

- GetEntryDialParams

 Returns a tuple with the most recently set dial parameters for the specified entry.

- GetErrorString

 Returns an error string for a RAS error code.

- HangUp

 Terminates a remote access session.

- IsHandleValid

 Indicates if the given RAS handle is valid.

- SetEntryDialParams

 Sets the dial parameters for the specified entry.

- RASDIALEXTENSIONS

 Creates a new RASDIALEXTENSIONS object


---

# win32ras 成员详细文档（共 13 项）


---

<!-- page: win32ras__CreatePhonebookEntry_meth.html -->

## win32ras.CreatePhonebookEntry

 CreatePhonebookEntry(hWnd, fileName)

Creates a new phonebook entry. The function displays a dialog box into which the user can enter information about the entry

#### Parameters

- hWnd : int

 Handle to the parent window of the dialog box.

- fileName=None : string

 Specifies the filename of the phonebook entry. Currently this is ignored.

#### Win32 API References

- Search for RasCreatePhonebookEntry at [msdn](https://learn.microsoft.com/en-ca/search/?terms=RasCreatePhonebookEntry), [google](https://www.google.com/search?q=RasCreatePhonebookEntry) or [google groups](https://groups.google.com/groups?q=RasCreatePhonebookEntry).


---

<!-- page: win32ras__Dial_meth.html -->

## win32ras.Dial

 int, int = Dial(dialExtensions, fileName , RasDialParams , callback )

Establishes a RAS connection to a RAS server.

#### Parameters

- dialExtensions : PyRASDIALEXTENSIONS

 An object providing the RASDIALEXTENSIONS information, or None

- fileName : string

 Specifies the filename of the phonebook entry, or None.

- RasDialParams : RASDIALPARAMS

 A tuple describing a RASDIALPARAMS structure.

- callback : method or hwnd

 The method to be called when RAS events occur, or None. If not None, the function must have the signature of win32ras::RasDialFunc1

#### Comments

 Note - this handle must be closed using win32ras::HangUp, or else the RAS port will remain open, even after the program has terminated. Your operating system may need rebooting to clean up otherwise!

#### Win32 API References

- Search for RasDial at [msdn](https://learn.microsoft.com/en-ca/search/?terms=RasDial), [google](https://www.google.com/search?q=RasDial) or [google groups](https://groups.google.com/groups?q=RasDial).

#### Return Value

The return value is (handle, retCode).
It is possible for a valid handle to be returned even on failure.
If the returned handle is = 0, then it can be assumed invalid.


---

<!-- page: win32ras__EditPhonebookEntry_meth.html -->

## win32ras.EditPhonebookEntry

 EditPhonebookEntry(hWnd, fileName, entryName)

Creates a new phonebook entry. The function displays a dialog box into which the user can enter information about the entry

#### Parameters

- hWnd : int

 Handle to the parent window of the dialog box.

- fileName : string

 Specifies the filename of the phonebook entry, or None. Currently this is ignored.

- entryName=None : string

 Specifies the name of the phonebook entry to edit

#### Win32 API References

- Search for RasEditPhonebookEntry at [msdn](https://learn.microsoft.com/en-ca/search/?terms=RasEditPhonebookEntry), [google](https://www.google.com/search?q=RasEditPhonebookEntry) or [google groups](https://groups.google.com/groups?q=RasEditPhonebookEntry).


---

<!-- page: win32ras__EnumConnections_meth.html -->

## win32ras.EnumConnections

 list = EnumConnections()

Returns a list of tuples, one for each active connection.

#### Win32 API References

- Search for RasEnumConnections at [msdn](https://learn.microsoft.com/en-ca/search/?terms=RasEnumConnections), [google](https://www.google.com/search?q=RasEnumConnections) or [google groups](https://groups.google.com/groups?q=RasEnumConnections).

#### Return Value

Each tuple is of format (handle, entryName, deviceType, deviceName)


---

<!-- page: win32ras__EnumEntries_meth.html -->

## win32ras.EnumEntries

 EnumEntries(reserved, fileName)

Returns a list of tuples, one for each phonebook entry.

#### Parameters

- reserved=None : string

 Reserved - must be None

- fileName=None : string

 The name of the phonebook file, or None.


---

<!-- page: win32ras__GetConnectStatus_meth.html -->

## win32ras.GetConnectStatus

 (int, int, string, string) = GetConnectStatus(hrasconn)

Returns a tuple with connection information.

#### Parameters

- hrasconn : int

 Handle to the RAS session.

#### Win32 API References

- Search for RasGetConnectStatus at [msdn](https://learn.microsoft.com/en-ca/search/?terms=RasGetConnectStatus), [google](https://www.google.com/search?q=RasGetConnectStatus) or [google groups](https://groups.google.com/groups?q=RasGetConnectStatus).

- Search for RasGetConnectStatus at [msdn](https://learn.microsoft.com/en-ca/search/?terms=RasGetConnectStatus), [google](https://www.google.com/search?q=RasGetConnectStatus) or [google groups](https://groups.google.com/groups?q=RasGetConnectStatus).


---

<!-- page: win32ras__GetEntryDialParams_meth.html -->

## win32ras.GetEntryDialParams

 (s,s,s,s,s,s),i = GetEntryDialParams(fileName, entryName )

Returns a tuple with the most recently set dial parameters for the specified entry.

#### Parameters

- fileName : string

 The filename of the phonebook, or None.

- entryName : string

 The name of the entry to retrieve the params for.

#### Win32 API References

- Search for RasGetEntryDialParams at [msdn](https://learn.microsoft.com/en-ca/search/?terms=RasGetEntryDialParams), [google](https://www.google.com/search?q=RasGetEntryDialParams) or [google groups](https://groups.google.com/groups?q=RasGetEntryDialParams).

- Search for RasGetConnectStatus at [msdn](https://learn.microsoft.com/en-ca/search/?terms=RasGetConnectStatus), [google](https://www.google.com/search?q=RasGetConnectStatus) or [google groups](https://groups.google.com/groups?q=RasGetConnectStatus).

#### Return Value

The return value is a tuple describing the params retrieved, plus a BOOL integer indicating if the password was also retrieved.


---

<!-- page: win32ras__GetErrorString_meth.html -->

## win32ras.GetErrorString

 string = GetErrorString(error)

Returns an error string for a RAS error code.

#### Parameters

- error : int

 The error value being queried.

#### Win32 API References

- Search for RasGetErrorString at [msdn](https://learn.microsoft.com/en-ca/search/?terms=RasGetErrorString), [google](https://www.google.com/search?q=RasGetErrorString) or [google groups](https://groups.google.com/groups?q=RasGetErrorString).


---

<!-- page: win32ras__HangUp_meth.html -->

## win32ras.HangUp

 HangUp(hras)

Terminates a remote access session.

#### Parameters

- hras : int

 The handle to the RAS connection to be terminated.

#### Win32 API References

- Search for RasHangUp at [msdn](https://learn.microsoft.com/en-ca/search/?terms=RasHangUp), [google](https://www.google.com/search?q=RasHangUp) or [google groups](https://groups.google.com/groups?q=RasHangUp).


---

<!-- page: win32ras__IsHandleValid_meth.html -->

## win32ras.IsHandleValid

 IsHandleValid(hras)

Indicates if the given RAS handle is valid.

#### Parameters

- hras : int

 The handle to the RAS connection being checked.


---

<!-- page: win32ras__PyRasGetEapUserIdentity_meth.html -->

## win32ras.PyRasGetEapUserIdentity

 PyRasGetEapUserIdentity(phoneBook, entry, flags, hwnd)

Sets the dial parameters for the specified entry.

#### Parameters

- phoneBook : string

 string containing the full path of the phone-book (PBK) file. If this parameter is None, the function will use the system phone book.

- entry : string

 string containing an existing entry name.

- flags : int

 Specifies zero or more of the following flags that qualify the authentication process.

| | Flag | Description
| |

---

 |

---

| | RASEAPF_NonInteractive | Specifies that the authentication protocol should not bring up a graphical user-interface. If this flag is not present, it is okay for the protocol to display a user interface.
| | RASEAPF_Logon | Specifies that the user data is obtained from Winlogon.
| | RASEAPF_Preview | Specifies that the user should be prompted for identity information before dialing.
- hwnd=None : PyHANDLE

 Handle to the parent window for the UI dialog.

#### Win32 API References

- Search for RasGetEapUserIdentity at [msdn](https://learn.microsoft.com/en-ca/search/?terms=RasGetEapUserIdentity), [google](https://www.google.com/search?q=RasGetEapUserIdentity) or [google groups](https://groups.google.com/groups?q=RasGetEapUserIdentity).


---

<!-- page: win32ras__RasDialFunc1_meth.html -->

---

## win32ras::RasDialFunc1 method

 RasDialFunc1()

 A placeholder for a RAS callback.

 Defined in: D:/A/PYWIN32/PYWIN32/WIN32/SRC/WIN32RASMODULE.CPP

#### Comments

 Certain RAS function require a callback function to be passed. This description describes the signature of the function you pass to these functions. handle to RAS connection type of event that has occurred connection state about to be entered error that may have occurred extended error information for some errors

#### Parameters

- hrascon : int

 The handle to the RAS session.

- msg : int

 A message code identifying the reason for the callback.

- rascs : int

 Connection state about to be entered.

- error : int

 The error state of the connection

- extendedError : int


---

<!-- page: win32ras__SetEntryDialParams_meth.html -->

## win32ras.SetEntryDialParams

 SetEntryDialParams(fileName, RasDialParams, bSavePassword)

Sets the dial parameters for the specified entry.

#### Parameters

- fileName : string

 The filename of the phonebook, or None.

- RasDialParams : (tuple)

 A tuple describing a RASDIALPARAMS structure.

- bSavePassword : int

 Indicates whether to remove password from entry's parameters.

#### Win32 API References

- Search for RasSetEntryDialParams at [msdn](https://learn.microsoft.com/en-ca/search/?terms=RasSetEntryDialParams), [google](https://www.google.com/search?q=RasSetEntryDialParams) or [google groups](https://groups.google.com/groups?q=RasSetEntryDialParams).

- Search for RasGetConnectStatus at [msdn](https://learn.microsoft.com/en-ca/search/?terms=RasGetConnectStatus), [google](https://www.google.com/search?q=RasGetConnectStatus) or [google groups](https://groups.google.com/groups?q=RasGetConnectStatus).
