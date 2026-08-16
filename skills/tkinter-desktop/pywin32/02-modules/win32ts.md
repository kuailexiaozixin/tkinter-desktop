# 模块 win32ts

> 来源：https://mhammond.github.io/pywin32/win32ts.html （及其成员页，已全部内联）

## Module win32ts

 Interface to the Terminal Services Api All functions in this module accept keyword arguments

#### Methods

- WTSOpenServer

 Opens a handle to a terminal server

- WTSCloseServer

 Closes a terminal server handle

- WTSQueryUserConfig

 Returns user configuration

- WTSSetUserConfig

 Changes user configuration

- WTSEnumerateServers

 Lists terminal servers in a domain

- WTSEnumerateSessions

 Lists sessions on a server

- WTSLogoffSession

 Logs off a user logged in through Terminal Services

- WTSDisconnectSession

 Disconnects a session without logging it off

- WTSQuerySessionInformation

 Retrieve information about a session

- WTSEnumerateProcesses

 Lists processes on a terminal server

- WTSQueryUserToken

 Retrieves the access token for a session

- WTSShutdownSystem

 Issues a shutdown request to a terminal server

- WTSTerminateProcess

 Kills a process on a terminal server

- ProcessIdToSessionId

 Finds the session under which a process is running

- WTSGetActiveConsoleSessionId

 Returns the id of the console session

- WTSRegisterSessionNotification

 Registers a window to receive terminal service notifications

- WTSUnRegisterSessionNotification

 Disables terminal service window messages

- WTSWaitSystemEvent

 Waits for an event to occur

- WTSSendMessage

 Sends a popup message to a terminal services session


---

# win32ts 成员详细文档（共 19 项）


---

<!-- page: win32ts__ProcessIdToSessionId_meth.html -->

## win32ts.ProcessIdToSessionId

 int = ProcessIdToSessionId(ProcessId)

Finds the session under which a process is running

#### Parameters

- ProcessId : int

 Id of a process as returned by win32ts::WTSEnumerateProcesses


---

<!-- page: win32ts__WTSCloseServer_meth.html -->

## win32ts.WTSCloseServer

 WTSCloseServer(Server)

Closes a terminal server handle

#### Parameters

- Server : PyHANDLE

 Terminal Server handle


---

<!-- page: win32ts__WTSDisconnectSession_meth.html -->

## win32ts.WTSDisconnectSession

 WTSDisconnectSession(Server, SessionId, Wait)

Disconnects a session without logging it off

#### Parameters

- Server : PyHANDLE

 Handle to a terminal server

- SessionId : int

 Terminal services session id as returned by win32ts::WTSEnumerateSessions

- Wait : boolean

 Indicates whether operation should be performed asynchronously


---

<!-- page: win32ts__WTSEnumerateProcesses_meth.html -->

## win32ts.WTSEnumerateProcesses

 (PyUnicode ,...) = WTSEnumerateProcesses(Server, Version , Reserved )

Lists processes on a terminal server

#### Parameters

- Server=WTS_CURRENT_SERVER_HANDLE : PyHANDLE

 Handle to a terminal server

- Version=1 : int

 Version of request, currently 1 is only valid value

- Reserved=0 : int

 Reserved, use 0 if passed in


---

<!-- page: win32ts__WTSEnumerateServers_meth.html -->

## win32ts.WTSEnumerateServers

 (PyUnicode ,...) = WTSEnumerateServers(DomainName, Version , Reserved )

Lists terminal servers in a domain

#### Parameters

- DomainName=None : PyUnicode

 Use None for current domain

- Version=1 : int

 Version of request, currently 1 is only valid value

- Reserved=0 : int

 Reserved, use 0 if passed in


---

<!-- page: win32ts__WTSEnumerateSessions_meth.html -->

## win32ts.WTSEnumerateSessions

 (dict,...) = WTSEnumerateSessions(Server, Version , Reserved )

Lists sessions on a server

#### Parameters

- Server=WTS_CURRENT_SERVER_HANDLE : PyHANDLE

 Handle to a terminal server

- Version=1 : int

 Version of request, currently 1 is only valid value

- Reserved=0 : int

 Reserved, use 0 if passed in

#### Return Value

Returns a sequence of dictionaries representing WTS_SESSION_INFO structs, containing {SessionId:int, WinStationName:str, State:int}


---

<!-- page: win32ts__WTSGetActiveConsoleSessionId_meth.html -->

## win32ts.WTSGetActiveConsoleSessionId

 int = WTSGetActiveConsoleSessionId()

Returns the id of the console session

#### Comments

 Returns 0xffffffff if no active console session exists


---

<!-- page: win32ts__WTSLogoffSession_meth.html -->

## win32ts.WTSLogoffSession

 WTSLogoffSession(Server, SessionId, Wait)

Logs off a user logged in through Terminal Services

#### Parameters

- Server : PyHANDLE

 Handle to a terminal server

- SessionId : int

 Terminal services session id as returned by win32ts::WTSEnumerateSessions

- Wait : boolean

 Indicates whether operation should be performed asynchronously


---

<!-- page: win32ts__WTSOpenServer_meth.html -->

## win32ts.WTSOpenServer

 PyHANDLE = WTSOpenServer(ServerName)

Opens a handle to a terminal server

#### Parameters

- ServerName : PyUnicode

 Name ot terminal server to be opened


---

<!-- page: win32ts__WTSQuerySessionInformation_meth.html -->

## win32ts.WTSQuerySessionInformation

 WTSQuerySessionInformation(Server, SessionId, WTSInfoClass)

Returns information about a terminal services session

#### Parameters

- Server : PyHANDLE

 Handle to a terminal server as returned by win32ts::WTSOpenServer

- SessionId : int

 Terminal services session id as returned by win32ts::WTSEnumerateSessions

- WTSInfoClass : int

 Type of information requested, from WTS_INFO_CLASS enum

| | InfoClass | Returned value
| |

---

 |

---

| | WTSApplicationName | Unicode string
| | WTSClientDirectory | Unicode string
| | WTSClientName | Unicode string
| | WTSDomainName | Unicode string
| | WTSInitialProgram | Unicode string
| | WTSOEMId | Unicode string
| | WTSUserName | Unicode string
| | WTSWinStationName | Unicode string
| | WTSWorkingDirectory | Unicode string
| | WTSClientProtocolType | Int, one of WTS_PROTOCOL_TYPE_CONSOLE,WTS_PROTOCOL_TYPE_ICA,WTS_PROTOCOL_TYPE_RDP
| | WTSClientProductId | Int
| | WTSClientBuildNumber | Int
| | WTSClientHardwareId | Int
| | WTSSessionId | Int
| | WTSConnectState | Int, from WTS_CONNECTSTATE_CLASS
| | WTSIsRemoteSession | Boolean
| | WTSClientDisplay | Dict containing client's display settings
| | WTSClientAddress | Dict containing type and value of client's IP address (None if console session)


---

<!-- page: win32ts__WTSQueryUserConfig_meth.html -->

## win32ts.WTSQueryUserConfig

 object = WTSQueryUserConfig(ServerName, UserName , ConfigClass )

Returns user configuration

#### Parameters

- ServerName : PyUnicode

 Name ot terminal server

- UserName : PyUnicode

 Name of user

- ConfigClass : int

 Type of information to be returned, win32ts.WTSUserConfig*

| | ConfigClass | Returned value
| |

---

 |

---

| | WTSUserConfigInitialProgram | Unicode string, program to be run when user logs on
| | WTSUserConfigWorkingDirectory | Unicode string, working dir for initial program
| | WTSUserConfigModemCallbackPhoneNumber | Unicode string
| | WTSUserConfigTerminalServerProfilePath | Unicode string
| | WTSUserConfigTerminalServerHomeDir | Unicode string
| | WTSUserConfigTerminalServerHomeDirDrive | Unicode string
| | WTSUserConfigfInheritInitialProgram | Int
| | WTSUserConfigfAllowLogonTerminalServer | Int, 1 if user can log on thru Terminal Service
| | WTSUserConfigTimeoutSettingsConnections | Int, max connection time (ms)
| | WTSUserConfigTimeoutSettingsDisconnections | Int
| | WTSUserConfigTimeoutSettingsIdle | Int, max idle time (ms)
| | WTSUserConfigfDeviceClientDrives | Int
| | WTSUserConfigfDeviceClientPrinters | Int
| | WTSUserConfigfDeviceClientDefaultPrinter | Int
| | WTSUserConfigBrokenTimeoutSettings | Int
| | WTSUserConfigReconnectSettings | Int
| | WTSUserConfigModemCallbackSettings | Int
| | WTSUserConfigShadowingSettings | Int, indicates if user's session my be monitored
| | WTSUserConfigfTerminalServerRemoteHomeDir | Int,

#### Return Value

The type of the returned value is dependent on the config class requested


---

<!-- page: win32ts__WTSQueryUserToken_meth.html -->

## win32ts.WTSQueryUserToken

 PyHANDLE = WTSQueryUserToken(SessionId)

Retrieves the access token for a session

#### Parameters

- SessionId : int

 Terminal services session id

#### Comments

 This function is intended only for use by trusted processes that have SE_TCB_PRIVILEGE enabled


---

<!-- page: win32ts__WTSRegisterSessionNotification_meth.html -->

## win32ts.WTSRegisterSessionNotification

 WTSRegisterSessionNotification(Wnd, Flags)

Registers a window to receive terminal service notifications

#### Parameters

- Wnd : PyHANDLE

 Window handle to receive terminal service messages

- Flags : int

 NOTIFY_FOR_THIS_SESSION or NOTIFY_FOR_ALL_SESSIONS


---

<!-- page: win32ts__WTSSendMessage_meth.html -->

## win32ts.WTSSendMessage

 int = WTSSendMessage(Server, SessionId , Title , Message , Style , Timeout , Wait )

Sends a popup message to a terminal services session

#### Parameters

- Server=WTS_CURRENT_SERVER_HANDLE : PyHANDLE

 Handle to a terminal server, or WTS_CURRENT_SERVER_HANDLE

- SessionId : int

 Terminal services session id

- Title : PyUnicode

 Title of dialog

- Message : PyUnicode

 Message to be displayed

- Style : int

 Usually MB_OK

- Timeout : int

 Seconds to wait before returning (only used if Wait is True)

- Wait : boolean

 Specifies if function should wait for user input before returning

#### Return Value

Returns one of IDABORT,IDCANCEL,IDIGNORE,IDNO,IDOK,IDRETRY,IDYES,IDASYNC,IDTIMEOUT,


---

<!-- page: win32ts__WTSSetUserConfig_meth.html -->

## win32ts.WTSSetUserConfig

 WTSSetUserConfig(ServerName, UserName, ConfigClass)

Changes user configuration

#### Parameters

- ServerName : PyUnicode

 Name ot terminal server

- UserName : PyUnicode

 Name of user

- ConfigClass : int

 Type of information to be set, win32ts.WTSUserConfig*

| | ConfigClass | Type of data required
| |

---

 |

---

| | WTSUserConfigInitialProgram | Unicode string, program to be run when user logs on
| | WTSUserConfigWorkingDirectory | Unicode string, working dir for initial program
| | WTSUserConfigModemCallbackPhoneNumber | Unicode string
| | WTSUserConfigTerminalServerProfilePath | Unicode string
| | WTSUserConfigTerminalServerHomeDir | Unicode string
| | WTSUserConfigTerminalServerHomeDirDrive | Unicode string
| | WTSUserConfigfInheritInitialProgram | Int
| | WTSUserConfigfAllowLogonTerminalServer | Int, 1 if user can log on thru Terminal Service
| | WTSUserConfigTimeoutSettingsConnections | Int, max connection time (ms)
| | WTSUserConfigTimeoutSettingsDisconnections | Int
| | WTSUserConfigTimeoutSettingsIdle | Int, max idle time (ms)
| | WTSUserConfigfDeviceClientDrives | Int
| | WTSUserConfigfDeviceClientPrinters | Int
| | WTSUserConfigfDeviceClientDefaultPrinter | Int
| | WTSUserConfigBrokenTimeoutSettings | Int
| | WTSUserConfigReconnectSettings | Int
| | WTSUserConfigModemCallbackSettings | Int
| | WTSUserConfigShadowingSettings | Int, indicates if user's session my be monitored
| | WTSUserConfigfTerminalServerRemoteHomeDir | Int,


---

<!-- page: win32ts__WTSShutdownSystem_meth.html -->

## win32ts.WTSShutdownSystem

 WTSShutdownSystem(Server, ShutdownFlag)

Issues a shutdown request to a terminal server

#### Parameters

- Server : PyHANDLE

 Handle to a terminal server

- ShutdownFlag : int

 One of the win32ts.WTS_WSD_* values


---

<!-- page: win32ts__WTSTerminateProcess_meth.html -->

## win32ts.WTSTerminateProcess

 WTSTerminateProcess(Server, ProcessId, ExitCode)

Kills a process on a terminal server

#### Parameters

- Server : PyHANDLE

 Handle to a terminal server

- ProcessId : int

 Id of a process as returned by win32ts::WTSEnumerateProcesses

- ExitCode : int

 Exit code for the process


---

<!-- page: win32ts__WTSUnRegisterSessionNotification_meth.html -->

## win32ts.WTSUnRegisterSessionNotification

 WTSUnRegisterSessionNotification(Wnd)

Disables terminal service window messages

#### Parameters

- Wnd : PyHANDLE

 Window previously registered to receive session notifications


---

<!-- page: win32ts__WTSWaitSystemEvent_meth.html -->

## win32ts.WTSWaitSystemEvent

 int = WTSWaitSystemEvent(Server, EventMask )

Waits for an event to occur

#### Parameters

- Server=WTS_CURRENT_SERVER_HANDLE : PyHANDLE

 Handle to a terminal server, or WTS_CURRENT_SERVER_HANDLE

- EventMask=WTS_EVENT_ALL : int

 Combination of WTS_EVENT_* values

#### Return Value

Returns a bitmask of WTS_EVENT_* flags indication which event(s) occurred
