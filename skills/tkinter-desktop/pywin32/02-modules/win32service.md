# 模块 win32service

> 来源：https://mhammond.github.io/pywin32/win32service.html （及其成员页，已全部内联）

## Module win32service

 An interface to the Windows NT Service API

#### Methods

- GetThreadDesktop

 Retrieves a handle to the desktop for a thread

- EnumWindowStations

 Lists names of window stations

- GetUserObjectInformation

 Returns specified type of info about a window station or desktop

- SetUserObjectInformation

 Set specified type of info for a window station or desktop object

- OpenWindowStation

 Returns a handle to the specified window station

- OpenDesktop

 Opens a handle to a desktop

- CreateDesktop

 Creates a new desktop in calling process's current window station

- OpenInputDesktop

 Returns a handle to desktop for logged-in user

- GetProcessWindowStation

 Returns a handle to calling process's current window station

- CreateWindowStation

 Creates a new window station

- EnumServicesStatus

 Returns a tuple of status info for each service that meets specified criteria

- EnumServicesStatusEx

 Lists the status of services that meet the specified criteria

- EnumDependentServices

 Lists services that depend on a service

- QueryServiceConfig

 Retrieves configuration parameters for a service

- StartService

 Starts the specified service

- OpenService

 Returns a handle to the specified service.

- OpenSCManager

 Returns a handle to the service control manager

- CloseServiceHandle

 Closes a service or SCM handle

- QueryServiceStatus

 Queries a service status

- QueryServiceStatusEx

 Queries a service status

- SetServiceObjectSecurity

 Set the security descriptor for a service

- QueryServiceObjectSecurity

 Retrieves information from the security descriptor for a service

- GetServiceKeyName

 Translates a service display name into its registry key name

- GetServiceDisplayName

 Translates an internal service name into its display name

- SetServiceStatus

 Sets a service status

- ControlService

 Sends a control message to a service.

- DeleteService

 Deletes the specified service

- CreateService

 Creates a new service.

- ChangeServiceConfig

 Changes the configuration of an existing service.

- LockServiceDatabase

 Locks the service database.

- UnlockServiceDatabase

 Unlocks the service database.

- QueryServiceLockStatus

 Retrieves the lock status of the specified service control manager database.

- ChangeServiceConfig2

 Modifies advanced service parameters

- QueryServiceConfig2

 Retrieves advanced service configuration options


---

# win32service 成员详细文档（共 34 项）


---

<!-- page: win32service__ChangeServiceConfig2_meth.html -->

## win32service.ChangeServiceConfig2

 ChangeServiceConfig2(hService, InfoLevel, info)

Modifies advanced service parameters

#### Parameters

- hService : PySC_HANDLE

 Service handle as returned by win32service::OpenService

- InfoLevel : int

 One of win32service.SERVICE_CONFIG_* values

- info : object

 Type depends on InfoLevel

| | InfoLevel | Input value
| |

---

 |

---

| | SERVICE_CONFIG_DESCRIPTION | Unicode string
| | SERVICE_CONFIG_FAILURE_ACTIONS | Dict representing a SERVICE_FAILURE_ACTIONS struct
| | SERVICE_CONFIG_DELAYED_AUTO_START_INFO | Boolean
| | SERVICE_CONFIG_FAILURE_ACTIONS_FLAG | Boolean
| | SERVICE_CONFIG_PRESHUTDOWN_INFO | int (shutdown timeout in milliseconds)
| | SERVICE_CONFIG_SERVICE_SID_INFO | int (SERVICE_SID_TYPE_*)
| | SERVICE_CONFIG_REQUIRED_PRIVILEGES_INFO | Sequence of unicode strings


---

<!-- page: win32service__ChangeServiceConfig_meth.html -->

## win32service.ChangeServiceConfig

 int/None = ChangeServiceConfig(hService, serviceType , startType , errorControl , binaryFile , loadOrderGroup , bFetchTag , serviceDeps , acctName , password , displayName )

Changes the configuration of an existing service.

#### Parameters

- hService : PySC_HANDLE

 handle to service to be modified

- serviceType : int

 type of service, or SERVICE_NO_CHANGE

- startType : int

 When/how to start service, or SERVICE_NO_CHANGE

- errorControl : int

 severity if service fails to start, or SERVICE_NO_CHANGE

- binaryFile : string

 name of binary file, or None

- loadOrderGroup : string

 name of load ordering group , or None

- bFetchTag : int

 Should the tag be fetched and returned? If TRUE, the result is the tag, else None.

- serviceDeps : [string,...]

 sequence of dependency names

- acctName : string

 account name of service, or None

- password : string

 password for service account , or None

- displayName : string

 Display name


---

<!-- page: win32service__CloseServiceHandle_meth.html -->

## win32service.CloseServiceHandle

 CloseServiceHandle(scHandle)

Closes a service or SCM handle

#### Parameters

- scHandle : PySC_HANDLE

 Handle to close


---

<!-- page: win32service__ControlService_meth.html -->

## win32service.ControlService

 SERVICE_STATUS = ControlService(scHandle, code )

Sends a control message to a service.

#### Parameters

- scHandle : PySC_HANDLE

 Handle to control

- code : int

 The service control code.

#### Return Value

The result is the new service status.


---

<!-- page: win32service__CreateDesktop_meth.html -->

## win32service.CreateDesktop

 PyHDESK = CreateDesktop(Desktop, Flags , DesiredAccess , SecurityAttributes )

Creates a new desktop in calling process's current window station

#### Parameters

- Desktop : string

 Name of desktop to create

- Flags : int

 DF_ALLOWOTHERACCOUNTHOOK or 0

- DesiredAccess : int

 An ACCESS_MASK determining level of access available thru returned handle

- SecurityAttributes : PySECURITY_ATTRIBUTES

 Specifies inheritance and controls access to desktop


---

<!-- page: win32service__CreateService_meth.html -->

## win32service.CreateService

 PySC_HANDLE/(PySC_HANDLE, int) = CreateService(scHandle, name , displayName , desiredAccess , serviceType , startType , errorControl , binaryFile , loadOrderGroup , bFetchTag , serviceDeps , acctName , password )

Creates a new service.

#### Parameters

- scHandle : PySC_HANDLE

 handle to service control manager database

- name : string

 Name of service

- displayName : string

 Display name

- desiredAccess : int

 type of access to service

- serviceType : int

 type of service

- startType : int

 When/how to start service

- errorControl : int

 severity if service fails to start

- binaryFile : string

 name of binary file

- loadOrderGroup : string

 name of load ordering group , or None

- bFetchTag : int

 Should the tag be fetched and returned? If TRUE, the result is a tuple of (handle, tag), otherwise just handle.

- serviceDeps : [string,...]

 sequence of dependency names

- acctName : string

 account name of service, or None

- password : string

 password for service account , or None


---

<!-- page: win32service__CreateWindowStation_meth.html -->

## win32service.CreateWindowStation

 PyHWINSTA = CreateWindowStation(WindowStation, Flags , DesiredAccess , SecurityAttributes )

Creates a new window station

#### Parameters

- WindowStation : string

 Name of window station to create, or None

- Flags : int

 CWF_CREATE_ONLY or 0

- DesiredAccess : int

 Bitmask of access types available to returned handle

- SecurityAttributes : PySECURITY_ATTRIBUTES

 Specifies security for window station, and whether handle is inheritable

#### Comments

 If name is None or empty string, name is formatteded from logon id


---

<!-- page: win32service__DeleteService_meth.html -->

## win32service.DeleteService

 DeleteService(scHandle)

Deletes the specified service

#### Parameters

- scHandle : PySC_HANDLE

 Handle to service to be deleted


---

<!-- page: win32service__EnumDependentServices_meth.html -->

## win32service.EnumDependentServices

 (tuple,...) = EnumDependentServices(hService, ServiceState )

Lists services that depend on a service

#### Parameters

- hService : PySC_HANDLE

 Handle to service for which to list dependent services (as returned by win32service::OpenService)

- ServiceState=SERVICE_STATE_ALL : int

 Limits to services in specified state - One of SERVICE_STATE_ALL, SERVICE_ACTIVE, SERVICE_INACTIVE

#### Return Value

Returns a sequence of tuples representing ENUM_SERVICE_STATUS structs: (ServiceName, DisplayName, SERVICE_STATUS)


---

<!-- page: win32service__EnumServicesStatusEx_meth.html -->

## win32service.EnumServicesStatusEx

 (dict,...) = EnumServicesStatusEx(SCManager, ServiceType , ServiceState , GroupName , InfoLevel )

Lists the status of services that meet the specified criteria

#### Parameters

- SCManager : PySC_HANDLE

 Handle to service control manager as returned by win32service::OpenSCManager

- ServiceType=SERVICE_WIN32 : int

 Types of services to enumerate (SERVICE_DRIVER and/or SERVICE_WIN32)

- ServiceState=SERVICE_STATE_ALL : int

 Limits to services in specified state

- GroupName=None : str

 Name of group - use None for all, or '' for services that don't belong to a group

- InfoLevel=SC_ENUM_PROCESS_INFO : int

 Currently SC_ENUM_PROCESS_INFO is only level defined

#### Win32 API References

- Search for EnumServicesStatusEx at [msdn](https://learn.microsoft.com/en-ca/search/?terms=EnumServicesStatusEx), [google](https://www.google.com/search?q=EnumServicesStatusEx) or [google groups](https://groups.google.com/groups?q=EnumServicesStatusEx).

#### Return Value

Returns a sequence of dicts, whose contents depend on information level requested. Currently, only information level supported is SC_ENUM_PROCESS_INFO (returns ENUM_SERVICE_STATUS_PROCESS).


---

<!-- page: win32service__EnumServicesStatus_meth.html -->

## win32service.EnumServicesStatus

 (tuple,...) = EnumServicesStatus(hSCManager, ServiceType , ServiceState )

Returns a tuple of status info for each service that meets specified criteria

#### Parameters

- hSCManager : PySC_HANDLE

 Handle to service control manager as returned by win32service::OpenSCManager

- ServiceType=SERVICE_WIN32 : int

 Types of services to enumerate (SERVICE_DRIVER and/or SERVICE_WIN32)

- ServiceState=SERVICE_STATE_ALL : int

 Limits to services in specified state

#### Return Value

Returns a sequence of tuples representing ENUM_SERVICE_STATUS structs: (ServiceName, DisplayName, SERVICE_STATUS)


---

<!-- page: win32service__EnumWindowStations_meth.html -->

## win32service.EnumWindowStations

 (string,,...) = EnumWindowStations()

Lists names of window stations

#### Comments

 Only window stations for which you have WINSTA_ENUMERATE access will be returned


---

<!-- page: win32service__GetProcessWindowStation_meth.html -->

## win32service.GetProcessWindowStation

 PyHWINSTA = GetProcessWindowStation()

Returns a handle to calling process's current window station


---

<!-- page: win32service__GetServiceDisplayName_meth.html -->

## win32service.GetServiceDisplayName

 string = GetServiceDisplayName(hSCManager, ServiceName )

Translates an internal service name into its display name

#### Parameters

- hSCManager : PySC_HANDLE

 Handle to service control manager as returned by win32service::OpenSCManager

- ServiceName : string

 Name of service


---

<!-- page: win32service__GetServiceKeyName_meth.html -->

## win32service.GetServiceKeyName

 string = GetServiceKeyName(hSCManager, DisplayName )

Translates a service display name into its registry key name

#### Parameters

- hSCManager : PySC_HANDLE

 Handle to service control manager as returned by win32service::OpenSCManager

- DisplayName : string

 Display name of a service


---

<!-- page: win32service__GetThreadDesktop_meth.html -->

## win32service.GetThreadDesktop

 PyHDESK = GetThreadDesktop(ThreadId)

Retrieves a handle to the desktop for a thread

#### Parameters

- ThreadId : int

 Id of thread


---

<!-- page: win32service__GetUserObjectInformation_meth.html -->

## win32service.GetUserObjectInformation

 GetUserObjectInformation(Handle, type)

Returns specified type of info about a window station or desktop

#### Parameters

- Handle : PyHANDLE

 Handle to window station or desktop

- type : int

 Type of info to return, one of UOI_FLAGS,UOI_NAME, UOI_TYPE, or UOI_USER_SID

#### Return Value

Return type is dependent on UOI_* constant passed in


---

<!-- page: win32service__LockServiceDatabase_meth.html -->

## win32service.LockServiceDatabase

 int = LockServiceDatabase(sc_handle)

Locks the service database.

#### Parameters

- sc_handle : PySC_HANDLE

 A handle to the SCM.


---

<!-- page: win32service__OpenDesktop_meth.html -->

## win32service.OpenDesktop

 PyHDESK = OpenDesktop(szDesktop, Flags , Inherit , DesiredAccess )

Opens a handle to a desktop

#### Parameters

- szDesktop : string

 Name of desktop to open

- Flags : int

 DF_ALLOWOTHERACCOUNTHOOK or 0

- Inherit : bool

 Allow handle to be inherited

- DesiredAccess : int

 ACCESS_MASK specifying level of access for handle


---

<!-- page: win32service__OpenInputDesktop_meth.html -->

## win32service.OpenInputDesktop

 PyHDESK = OpenInputDesktop(Flags, Inherit , DesiredAccess )

Returns a handle to desktop for logged-in user

#### Parameters

- Flags : int

 DF_ALLOWOTHERACCOUNTHOOK or 0

- Inherit : bool

 Specifies if handle will be inheritable

- DesiredAccess : int

 ACCESS_MASK specifying access available to returned handle


---

<!-- page: win32service__OpenSCManager_meth.html -->

## win32service.OpenSCManager

 PySC_HANDLE = OpenSCManager(machineName, dbName , desiredAccess )

Returns a handle to the service control manager

#### Parameters

- machineName : string

 The name of the computer, or None

- dbName : string

 The name of the service database, or None

- desiredAccess : int

 The access desired. (combination of win32service.SC_MANAGER_* flags)


---

<!-- page: win32service__OpenService_meth.html -->

## win32service.OpenService

 PySC_HANDLE = OpenService(scHandle, name , desiredAccess )

Returns a handle to the specified service.

#### Parameters

- scHandle : PySC_HANDLE

 Handle to the Service Control Mananger

- name : string

 The name of the service to open.

- desiredAccess : int

 The access desired.


---

<!-- page: win32service__OpenWindowStation_meth.html -->

## win32service.OpenWindowStation

 PyHWINSTA = OpenWindowStation(szWinSta, Inherit , DesiredAccess )

Returns a handle to the specified window station

#### Parameters

- szWinSta : string

 Name of window station

- Inherit : Bool

 Allow handle to be inherited by subprocesses

- DesiredAccess : int

 Bitmask of access types


---

<!-- page: win32service__QueryServiceConfig2_meth.html -->

## win32service.QueryServiceConfig2

 object = QueryServiceConfig2(hService, InfoLevel )

Retrieves advanced service configuration options

#### Parameters

- hService : PySC_HANDLE

 Service handle as returned by win32service::OpenService

- InfoLevel : int

 One of win32service.SERVICE_CONFIG_* values

| | InfoLevel | Type of value returned
| |

---

 |

---

| | SERVICE_CONFIG_DESCRIPTION | Unicode string
| | SERVICE_CONFIG_FAILURE_ACTIONS | Dict representing a SERVICE_FAILURE_ACTIONS struct
| | SERVICE_CONFIG_DELAYED_AUTO_START_INFO | Boolean
| | SERVICE_CONFIG_FAILURE_ACTIONS_FLAG | Boolean
| | SERVICE_CONFIG_PRESHUTDOWN_INFO | int (shutdown timeout in milliseconds)
| | SERVICE_CONFIG_SERVICE_SID_INFO | int (SERVICE_SID_TYPE_*)
| | SERVICE_CONFIG_REQUIRED_PRIVILEGES_INFO | List of unicode strings

#### Return Value

Type of returned object depends on InfoLevel


---

<!-- page: win32service__QueryServiceConfig_meth.html -->

## win32service.QueryServiceConfig

 tuple = QueryServiceConfig(hService)

Retrieves configuration parameters for a service

#### Parameters

- hService : PySC_HANDLE

 Service handle as returned by win32service::OpenService

#### Return Value

Returns a tuple representing a QUERY_SERVICE_CONFIG struct:

#### Items

- [0] int : ServiceType

 Combination of SERVICE_*_DRIVER or SERVICE_*_PROCESS constants

- [1] int : StartType

 One of SERVICE_*_START constants

- [2] int : ErrorControl

 One of SERVICE_ERROR_* constants

- [3] string : BinaryPathName

 Service's binary executable, can also contain command line args

- [4] string : LoadOrderGroup

 Loading group that service is a member of

- [5] int : TagId

 Order of service within its load order group

- [6] [string,...] : Dependencies

 Sequence of names of services on which this service depends

- [7] string : ServiceStartName

 Account name under which service will run

- [8] string : DisplayName

 Name of service


---

<!-- page: win32service__QueryServiceLockStatus_meth.html -->

## win32service.QueryServiceLockStatus

 (int, string, int) = QueryServiceLockStatus(hSCManager)

Retrieves the lock status of the specified service control manager database.

#### Parameters

- hSCManager : PySC_HANDLE

 Handle to the SCM.

#### Return Value

The result is a tuple of (bIsLocked, userName, lockDuration)


---

<!-- page: win32service__QueryServiceObjectSecurity_meth.html -->

## win32service.QueryServiceObjectSecurity

 PySECURITY_DESCRIPTOR = QueryServiceObjectSecurity(Handle, SecurityInformation )

Retrieves information from the security descriptor for a service

#### Parameters

- Handle : PySC_HANDLE

 Service handle

- SecurityInformation : int

 Type of infomation to retrieve, combination of values from SECURITY_INFORMATION enum


---

<!-- page: win32service__QueryServiceStatusEx_meth.html -->

## win32service.QueryServiceStatusEx

 SERVICE_STATUS = QueryServiceStatusEx(hService)

Queries a service status

#### Parameters

- hService : PySC_HANDLE

 Handle to service to be queried


---

<!-- page: win32service__QueryServiceStatus_meth.html -->

## win32service.QueryServiceStatus

 SERVICE_STATUS = QueryServiceStatus(hService)

Queries a service status

#### Parameters

- hService : PySC_HANDLE

 Handle to service to be queried


---

<!-- page: win32service__SetServiceObjectSecurity_meth.html -->

## win32service.SetServiceObjectSecurity

 SetServiceObjectSecurity(Handle, SecurityInformation, SecurityDescriptor)

Set the security descriptor for a service

#### Parameters

- Handle : PySC_HANDLE

 Service handle

- SecurityInformation : int

 Type of infomation to set, combination of values from SECURITY_INFORMATION enum

- SecurityDescriptor : PySECURITY_DESCRIPTOR

 PySECURITY_DESCRIPTOR containing infomation to set


---

<!-- page: win32service__SetServiceStatus_meth.html -->

## win32service.SetServiceStatus

 SetServiceStatus(scHandle, serviceStatus)

Sets a service status

#### Parameters

- scHandle : int

 Handle to set

- serviceStatus : SERVICE_STATUS

 The new status


---

<!-- page: win32service__SetUserObjectInformation_meth.html -->

## win32service.SetUserObjectInformation

 SetUserObjectInformation(Handle, info, type)

Set specified type of info for a window station or desktop object

#### Parameters

- Handle : PyHANDLE

 Handle to window station or desktop

- info : object

 Information to set for handle, currently only a dictionary representing USEROBJECTFLAGS struct

- type=UOI_FLAGS : int

 Type of info to set, currently only accepts UOI_FLAGS

#### Comments

 Currently only UOI_FLAGS supported


---

<!-- page: win32service__StartService_meth.html -->

## win32service.StartService

 StartService(hService, args)

Starts the specified service

#### Parameters

- hService : PySC_HANDLE

 Handle to the service to be started

- args : [string, ...]

 Arguments to the service.


---

<!-- page: win32service__UnlockServiceDatabase_meth.html -->

## win32service.UnlockServiceDatabase

 int = UnlockServiceDatabase(lock)

Unlocks the service database.

#### Parameters

- lock : int

 A lock provided by win32service::LockServiceDatabase
