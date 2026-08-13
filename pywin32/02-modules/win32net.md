# 模块 win32net

> 来源：https://mhammond.github.io/pywin32/win32net.html （及其成员页，已全部内联）

## Module win32net

 A module encapsulating the Windows Network API.

#### Methods

- NetGetJoinInformation

 Retrieves join status information for the specified computer.

- NetGroupGetInfo

 Retrieves information about a particular group on a server.

- NetGroupGetUsers

 Enumerates the users in a group.

- NetGroupSetUsers

 Sets the users in a group on server.

- NetGroupSetInfo

 Sets information about a particular group account on a server.

- NetGroupAdd

 Creates a new group.

- NetGroupAddUser

 Adds a user to a group

- NetGroupDel

 Deletes a group.

- NetGroupDelUser

 Deletes a user from the group

- NetGroupEnum

 Enumerates the groups.

- NetGroupAdd

 Creates a new group.

- NetLocalGroupAddMembers

 Adds users to a local group.

- NetLocalGroupDelMembers

 Deletes users from a local group.

- NetGroupDel

 Deletes a group.

- NetGroupEnum

 Enumerates the groups.

- NetGroupGetInfo

 Retrieves information about a particular group on a server.

- NetLocalGroupGetMembers

 Enumerates the members in a local group.

- NetGroupSetInfo

 Sets information about a particular group account on a server.

- NetLocalGroupSetMembers

 Sets the members of a local group. Any existing members not listed are removed.

- NetMessageBufferSend

 sends a string to a registered message alias.

- NetMessageNameAdd

 Add a message alias for a computer

- NetMessageNameDel

 Removes a message alias

- NetMessageNameEnum

 List message aliases for a computer

- NetServerEnum

 Retrieves information about all servers of a specific type

- NetServerGetInfo

 Retrieves information about a particular server.

- NetServerSetInfo

 Sets information about a particular server.

- NetShareAdd

 Creates a new share.

- NetShareDel

 Deletes a share

- NetShareCheck

 Checks if server is sharing a device

- NetShareEnum

 Retrieves information about each shared resource on a server.

- NetShareGetInfo

 Retrieves information about a particular share on a server.

- NetShareSetInfo

 Sets information about a particular share on a server.

- NetUserAdd

 Creates a new user.

- NetUserChangePassword

 Changes a users password on the specified domain.

- NetUserEnum

 Enumerates all users.

- NetUserGetGroups

 Returns a list of groups,attributes for all groups for the user.

- NetUserGetInfo

 Retrieves information about a particular user account on a server.

- NetUserGetLocalGroups

 Retrieves a list of local groups to which a specified user belongs.

- NetUserSetInfo

 Sets information about a particular user account on a server.

- NetUserDel

 Deletes a user.

- NetUserModalsGet

 Retrieves global user information on a server.

- NetUserModalsSet

 Sets global user information on a server.

- NetWkstaUserEnum

 Retrieves information about all users currently logged on to the workstation.

- NetWkstaGetInfo

 returns information about the configuration elements for a workstation.

- NetWkstaSetInfo

 Sets information about the configuration elements for a workstation.

- NetWkstaTransportEnum

 Retrieves information about transport protocols that are currently managed by the redirector.

- NetWkstaTransportAdd

 binds the redirector to a transport.

- NetWkstaTransportDel

 unbinds transport protocol from the redirector.

- NetServerDiskEnum

 Retrieves the list of disk drives on a server.

- NetUseAdd

 Establishes connection between local or NULL device name and a shared resource through redirector.

- NetUseDel

 Ends connection to a shared resource.

- NetUseEnum

 Enumerates connection between local machine and shared resources on remote computers.

- NetUseGetInfo

 Get information about locally mapped shared resource on remote computer.

- NetGetAnyDCName

 Returns the name of any domain controller trusted by the specified server.

- NetGetDCName

 Returns the name of the primary domain controller (PDC).

- NetSessionEnum

 Returns network session for the server, limited to single client and/or user if specified.

- NetSessionDel

 Delete network session for specified server, client computer and user. Returns None on success.

- NetSessionGetInfo

 Get network session information.

- NetFileEnum

 Returns open file resources for server (single client and/or user may also be passed as criteria).

- NetFileClose

 Closes file for specified server and file id.

- NetFileGetInfo

 Get info about files open on the server.

- NetStatisticsGet

 Return server or workstation stats

- NetServerComputerNameAdd

 Adds an extra network name for a server

- NetServerComputerNameDel

 Deletes an emulated computer name created by win32net::PyNetServerComputerNameAdd

- NetValidateName

 Verify that computer/domain name is valid for given context

- NetValidatePasswordPolicy

 Allows an application to check password compliance against an application-provided account database.


---

# win32net 成员详细文档（共 66 项）


---

<!-- page: win32net__NetFileClose_meth.html -->

## win32net.NetFileClose

 NetFileClose(servername, fileid)

Closes an open network resource on a server

#### Parameters

- servername : string/PyUnicode

 Name of server on which to operate, local machine assumed if None

- fileid : int

 Id of opened resource, as returned by win32net::NetFileEnum


---

<!-- page: win32net__NetFileEnum_meth.html -->

## win32net.NetFileEnum

 (dict,...) = NetFileEnum(level, servername , basepath , username )

Lists remotely opened resources on a server

#### Parameters

- level : int

 Level of information, 2 or 3 supported

- servername=None : string/PyUnicode

 The name of the server for which to list open resources, local machine assumed if None

- basepath=None : string/PyUnicode

 If specified, limits returned list to files on given path

- username=None : string/PyUnicode

 User that opened resource, or None to list open files for all users

#### Return Value

Returns a sequence of dictionaries representing FILE_INFO_* structs, depending on level specified


---

<!-- page: win32net__NetFileGetInfo_meth.html -->

## win32net.NetFileGetInfo

 dict = NetFileGetInfo(level, servername , fileid )

Returns information about an open network resource

#### Parameters

- level : int

 Level of information to return, 2 or 3 supported

- servername : string/PyUnicode

 Server on which resource is open, local machine assumed if None

- fileid : int

 Id of opened resource, as returned by win32net::NetFileEnum


---

<!-- page: win32net__NetGetAnyDCName_meth.html -->

## win32net.NetGetAnyDCName

 PyUnicode = NetGetAnyDCName(server, domain )

Returns the name of any domain controller trusted by the specified server.

#### Parameters

- server=None : PyUnicode

 Specifies the name of the remote server on which the function is to execute. If this parameter is None, the local computer is used.

- domain=None : PyUnicode

 Specifies the name of the domain. If this parameter is None, the name of the domain controller for the primary domain is used.


---

<!-- page: win32net__NetGetDCName_meth.html -->

## win32net.NetGetDCName

 PyUnicode = NetGetDCName(server, domain )

Returns the name of the primary domain controller (PDC).

#### Parameters

- server=None : PyUnicode

 Specifies the name of the remote server on which the function is to execute. If this parameter is None, the local computer is used.

- domain=None : PyUnicode

 Specifies the name of the domain. If this parameter is None, the name of the domain controller for the primary domain is used.


---

<!-- page: win32net__NetGetJoinInformation_meth.html -->

## win32net.NetGetJoinInformation

 PyUnicode , int = NetGetJoinInformation()

Retrieves join status information for the specified computer.


---

<!-- page: win32net__NetGroupAddUser_meth.html -->

## win32net.NetGroupAddUser

 NetGroupAddUser(server, group, username)

Adds a user to the group

#### Parameters

- server : string/PyUnicode

 The name of the server, or None.

- group : string/PyUnicode

 The group name

- username : string/PyUnicode

 The user to add to the group.

#### Win32 API References

- Search for NetGroupAddUser at [msdn](https://learn.microsoft.com/en-ca/search/?terms=NetGroupAddUser), [google](https://www.google.com/search?q=NetGroupAddUser) or [google groups](https://groups.google.com/groups?q=NetGroupAddUser).


---

<!-- page: win32net__NetGroupAdd_meth.html -->

## win32net.NetGroupAdd

 NetGroupAdd(server, level, data)

Creates a new group.

#### Parameters

- server : string/PyUnicode

 The name of the server, or None.

- level : int

 The information level contained in the data

- data : PyGROUP_INFO_*

 A dictionary holding the group data.

#### Win32 API References

- Search for NetGroupAdd at [msdn](https://learn.microsoft.com/en-ca/search/?terms=NetGroupAdd), [google](https://www.google.com/search?q=NetGroupAdd) or [google groups](https://groups.google.com/groups?q=NetGroupAdd).


---

<!-- page: win32net__NetGroupDelUser_meth.html -->

## win32net.NetGroupDelUser

 NetGroupDelUser(server, group, username)

Deletes a user from the group

#### Parameters

- server : string/PyUnicode

 The name of the server, or None.

- group : string/PyUnicode

 The group name

- username : string/PyUnicode

 The user to delete from the group.

#### Win32 API References

- Search for NetGroupDelUser at [msdn](https://learn.microsoft.com/en-ca/search/?terms=NetGroupDelUser), [google](https://www.google.com/search?q=NetGroupDelUser) or [google groups](https://groups.google.com/groups?q=NetGroupDelUser).


---

<!-- page: win32net__NetGroupDel_meth.html -->

## win32net.NetGroupDel

 NetGroupDel(server, groupname)

Deletes a group.

#### Parameters

- server : string/PyUnicode

 The name of the server, or None.

- groupname : string/PyUnicode

 The group name

#### Win32 API References

- Search for NetGroupDel at [msdn](https://learn.microsoft.com/en-ca/search/?terms=NetGroupDel), [google](https://www.google.com/search?q=NetGroupDel) or [google groups](https://groups.google.com/groups?q=NetGroupDel).


---

<!-- page: win32net__NetGroupEnum_meth.html -->

## win32net.NetGroupEnum

 ([dict, ...], total, resumeHandle) = NetGroupEnum(server, level , resumeHandle , prefLen )

Enumerates all groups.

#### Parameters

- server : string/PyUnicode

 The name of the server, or None.

- level : int

 The level of data required.

- resumeHandle=0 : int

 A resume handle. See the return description for more information.

- prefLen=MAX_PREFERRED_LENGTH : int

 The preferred length of the data buffer.

#### Win32 API References

- Search for NetGroupEnum at [msdn](https://learn.microsoft.com/en-ca/search/?terms=NetGroupEnum), [google](https://www.google.com/search?q=NetGroupEnum) or [google groups](https://groups.google.com/groups?q=NetGroupEnum).

#### Return Value

The result is a list of items read (with each item being a dictionary of format PyGROUP_INFO_*, depending on the level parameter), the total available, and a new "resume handle". The first time you call this function, you should pass zero for the resume handle. If more data is available than what was returned, a new non-zero resume handle will be returned, which can be used to call the function again to fetch more data. This process may repeat, each time with a new resume handle, until zero is returned for the new handle, indicating all the data has been read.


---

<!-- page: win32net__NetGroupGetInfo_meth.html -->

## win32net.NetGroupGetInfo

 dict = NetGroupGetInfo(server, groupname , level )

Retrieves information about a particular group on a server.

#### Parameters

- server : string/PyUnicode

 The name of the server, or None.

- groupname : string/PyUnicode

 The group name

- level : int

 The information level contained in the data

#### Win32 API References

- Search for NetGroupGetInfo at [msdn](https://learn.microsoft.com/en-ca/search/?terms=NetGroupGetInfo), [google](https://www.google.com/search?q=NetGroupGetInfo) or [google groups](https://groups.google.com/groups?q=NetGroupGetInfo).

#### Return Value

The result will be a dictionary in one of the PyGROUP_INFO_* formats, depending on the level parameter.


---

<!-- page: win32net__NetGroupGetUsers_meth.html -->

## win32net.NetGroupGetUsers

 ([dict, ...], total, resumeHandle) = NetGroupGetUsers(server, groupName , level , resumeHandle , prefLen )

Enumerates the users in a group.

#### Parameters

- server : string/PyUnicode

 The name of the server, or None.

- groupName : string/PyUnicode

 The name of the local group.

- level : int

 The level of data required.

- resumeHandle=0 : int

 A resume handle. See the return description for more information.

- prefLen=4096 : int

 The preferred length of the data buffer.

#### Win32 API References

- Search for NetGroupGetUsers at [msdn](https://learn.microsoft.com/en-ca/search/?terms=NetGroupGetUsers), [google](https://www.google.com/search?q=NetGroupGetUsers) or [google groups](https://groups.google.com/groups?q=NetGroupGetUsers).

#### Return Value

The result is a list of items read (with each item being a dictionary of format PyGROUP_USERS_INFO_*, depending on the level parameter), the total available, and a new "resume handle". The first time you call this function, you should pass zero for the resume handle. If more data is available than what was returned, a new non-zero resume handle will be returned, which can be used to call the function again to fetch more data. This process may repeat, each time with a new resume handle, until zero is returned for the new handle, indicating all the data has been read.


---

<!-- page: win32net__NetGroupSetInfo_meth.html -->

## win32net.NetGroupSetInfo

 NetGroupSetInfo(server, groupname, level, data)

Sets information about a particular group account on a server.

#### Parameters

- server : string/PyUnicode

 The name of the server, or None.

- groupname : string/PyUnicode

 The group name

- level : int

 The information level contained in the data

- data : PyGROUP_INFO_*

 A dictionary holding the group data.

#### Win32 API References

- Search for NetGroupSetInfo at [msdn](https://learn.microsoft.com/en-ca/search/?terms=NetGroupSetInfo), [google](https://www.google.com/search?q=NetGroupSetInfo) or [google groups](https://groups.google.com/groups?q=NetGroupSetInfo).


---

<!-- page: win32net__NetGroupSetUsers_meth.html -->

## win32net.NetGroupSetUsers

 NetGroupSetUsers(server, group, level, members)

Sets the members of a local group. Any existing members not listed are removed.

#### Parameters

- server : string/PyUnicode

 The name of the server, or None.

- group : string/PyUnicode

 The group name

- level : int

 The level of information in the data. Must be 0

- members : [PyGROUP_USERS_INFO_0, ..]

 The list of new members to add.

#### Win32 API References

- Search for NetGroupSetUsers at [msdn](https://learn.microsoft.com/en-ca/search/?terms=NetGroupSetUsers), [google](https://www.google.com/search?q=NetGroupSetUsers) or [google groups](https://groups.google.com/groups?q=NetGroupSetUsers).


---

<!-- page: win32net__NetLocalGroupAddMembers_meth.html -->

## win32net.NetLocalGroupAddMembers

 NetLocalGroupAddMembers(server, group, level, members)

Adds users to a local group.

#### Parameters

- server : string/PyUnicode

 The name of the server, or None.

- group : string/PyUnicode

 The group name

- level : int

 The level of information in the data.

- members : [PyLOCALGROUP_MEMBERS_INFO_*, ]

 The new members to add.

#### Win32 API References

- Search for NetLocalGroupAddMembers at [msdn](https://learn.microsoft.com/en-ca/search/?terms=NetLocalGroupAddMembers), [google](https://www.google.com/search?q=NetLocalGroupAddMembers) or [google groups](https://groups.google.com/groups?q=NetLocalGroupAddMembers).


---

<!-- page: win32net__NetLocalGroupAdd_meth.html -->

## win32net.NetLocalGroupAdd

 NetLocalGroupAdd(server, level, data)

Creates a new group.

#### Parameters

- server : string/PyUnicode

 The name of the server, or None.

- level : int

 The information level contained in the data

- data : PyLOCALGROUP_INFO_*

 A dictionary holding the group data.

#### Win32 API References

- Search for NetLocalGroupAdd at [msdn](https://learn.microsoft.com/en-ca/search/?terms=NetLocalGroupAdd), [google](https://www.google.com/search?q=NetLocalGroupAdd) or [google groups](https://groups.google.com/groups?q=NetLocalGroupAdd).


---

<!-- page: win32net__NetLocalGroupDelMembers_meth.html -->

## win32net.NetLocalGroupDelMembers

 NetLocalGroupDelMembers(server, group, members)

Deletes users from a local group.

#### Parameters

- server : string/PyUnicode

 The name of the server, or None.

- group : string/PyUnicode

 The group name

- members : [string, ...]

 A list of strings with fully qualified user names to delete from a local group.

#### Win32 API References

- Search for NetLocalGroupDelMembers at [msdn](https://learn.microsoft.com/en-ca/search/?terms=NetLocalGroupDelMembers), [google](https://www.google.com/search?q=NetLocalGroupDelMembers) or [google groups](https://groups.google.com/groups?q=NetLocalGroupDelMembers).


---

<!-- page: win32net__NetLocalGroupDel_meth.html -->

## win32net.NetLocalGroupDel

 NetLocalGroupDel(server, groupname)

Deletes a group.

#### Parameters

- server : string/PyUnicode

 The name of the server, or None.

- groupname : string/PyUnicode

 The group name

#### Win32 API References

- Search for NetLocalGroupDel at [msdn](https://learn.microsoft.com/en-ca/search/?terms=NetLocalGroupDel), [google](https://www.google.com/search?q=NetLocalGroupDel) or [google groups](https://groups.google.com/groups?q=NetLocalGroupDel).


---

<!-- page: win32net__NetLocalGroupEnum_meth.html -->

## win32net.NetLocalGroupEnum

 ([dict, ...], total, resumeHandle) = NetLocalGroupEnum(server, level , resumeHandle , prefLen )

Enumerates all groups.

#### Parameters

- server : string/PyUnicode

 The name of the server, or None.

- level : int

 The level of data required.

- resumeHandle=0 : int

 A resume handle. See the return description for more information.

- prefLen=MAX_PREFERRED_LENGTH : int

 The preferred length of the data buffer.

#### Win32 API References

- Search for NetLocalGroupEnum at [msdn](https://learn.microsoft.com/en-ca/search/?terms=NetLocalGroupEnum), [google](https://www.google.com/search?q=NetLocalGroupEnum) or [google groups](https://groups.google.com/groups?q=NetLocalGroupEnum).

#### Return Value

The result is a list of items read (with each item being a dictionary of format PyGROUP_INFO_*, depending on the level parameter), the total available, and a new "resume handle". The first time you call this function, you should pass zero for the resume handle. If more data is available than what was returned, a new non-zero resume handle will be returned, which can be used to call the function again to fetch more data. This process may repeat, each time with a new resume handle, until zero is returned for the new handle, indicating all the data has been read.


---

<!-- page: win32net__NetLocalGroupGetInfo_meth.html -->

## win32net.NetLocalGroupGetInfo

 dict = NetLocalGroupGetInfo(server, groupname , level )

Retrieves information about a particular group on a server.

#### Parameters

- server : string/PyUnicode

 The name of the server, or None.

- groupname : string/PyUnicode

 The group name

- level : int

 The information level contained in the data

#### Win32 API References

- Search for NetLocalGroupGetInfo at [msdn](https://learn.microsoft.com/en-ca/search/?terms=NetLocalGroupGetInfo), [google](https://www.google.com/search?q=NetLocalGroupGetInfo) or [google groups](https://groups.google.com/groups?q=NetLocalGroupGetInfo).

#### Return Value

The result will be a dictionary in one of the PyLOCALGROUP_INFO_* formats, depending on the level parameter.


---

<!-- page: win32net__NetLocalGroupGetMembers_meth.html -->

## win32net.NetLocalGroupGetMembers

 ([dict, ...], total, resumeHandle) = NetLocalGroupGetMembers(server, groupName , level , resumeHandle , prefLen )

Enumerates the members in a local group.

#### Parameters

- server : string/PyUnicode

 The name of the server, or None.

- groupName : string/PyUnicode

 The name of the local group.

- level : int

 The level of data required.

- resumeHandle=0 : int

 A resume handle. See the return description for more information.

- prefLen=4096 : int

 The preferred length of the data buffer.

#### Win32 API References

- Search for NetLocalGroupGetMembers at [msdn](https://learn.microsoft.com/en-ca/search/?terms=NetLocalGroupGetMembers), [google](https://www.google.com/search?q=NetLocalGroupGetMembers) or [google groups](https://groups.google.com/groups?q=NetLocalGroupGetMembers).

#### Return Value

The result is a list of items read (with each item being a dictionary of format PyLOCALGROUP_MEMBERS_INFO_*, depending on the level parameter), the total available, and a new "resume handle". The first time you call this function, you should pass zero for the resume handle. If more data is available than what was returned, a new non-zero resume handle will be returned, which can be used to call the function again to fetch more data. This process may repeat, each time with a new resume handle, until zero is returned for the new handle, indicating all the data has been read.


---

<!-- page: win32net__NetLocalGroupSetInfo_meth.html -->

## win32net.NetLocalGroupSetInfo

 NetLocalGroupSetInfo(server, groupname, level, data)

Sets information about a particular group account on a server.

#### Parameters

- server : string/PyUnicode

 The name of the server, or None.

- groupname : string/PyUnicode

 The group name

- level : int

 The information level contained in the data

- data : PyLOCALGROUP_INFO_*

 A dictionary holding the group data.

#### Win32 API References

- Search for NetLocalGroupSetInfo at [msdn](https://learn.microsoft.com/en-ca/search/?terms=NetLocalGroupSetInfo), [google](https://www.google.com/search?q=NetLocalGroupSetInfo) or [google groups](https://groups.google.com/groups?q=NetLocalGroupSetInfo).


---

<!-- page: win32net__NetLocalGroupSetMembers_meth.html -->

## win32net.NetLocalGroupSetMembers

 NetLocalGroupSetMembers(server, group, level, members)

Sets the members of a local group. Any existing members not listed are removed.

#### Parameters

- server : string/PyUnicode

 The name of the server, or None.

- group : string/PyUnicode

 The group name

- level : int

 The level of information in the data.

- members : [PyLOCALGROUP_MEMBERS_INFO_*, ..]

 The list of new members to add.

#### Win32 API References

- Search for NetLocalGroupSetMembers at [msdn](https://learn.microsoft.com/en-ca/search/?terms=NetLocalGroupSetMembers), [google](https://www.google.com/search?q=NetLocalGroupSetMembers) or [google groups](https://groups.google.com/groups?q=NetLocalGroupSetMembers).


---

<!-- page: win32net__NetMessageBufferSend_meth.html -->

## win32net.NetMessageBufferSend

 NetMessageBufferSend(domain, userName, fromName, message)

sends a string to a registered message alias.

#### Parameters

- domain : string

 Specifies the name of the remote server on which the function is to execute. None or empty string the local computer.

- userName : string

 Specifies the message name to which the message buffer should be sent.

- fromName : string

 The user the message is to come from, or None for the current user.

- message : string

 The message text

#### Win32 API References

- Search for NetMessageBufferSend at [msdn](https://learn.microsoft.com/en-ca/search/?terms=NetMessageBufferSend), [google](https://www.google.com/search?q=NetMessageBufferSend) or [google groups](https://groups.google.com/groups?q=NetMessageBufferSend).


---

<!-- page: win32net__NetMessageNameAdd_meth.html -->

## win32net.NetMessageNameAdd

 NetMessageNameAdd(server, msgname)

Adds a message alias for specified machine

#### Parameters

- server : str/unicode

 Name of server on which to execute - leading backslashes required on NT - local machine used if None

- msgname : str/unicode

 Message alias to add, 15 characters max


---

<!-- page: win32net__NetMessageNameDel_meth.html -->

## win32net.NetMessageNameDel

 NetMessageNameDel(server, msgname)

Removes a message alias for specified machine

#### Parameters

- server : str/unicode

 Name of server on which to execute - leading backslashes required on NT - local machine used if None

- msgname : str/unicode

 Message alias to delete for specified machine


---

<!-- page: win32net__NetMessageNameEnum_meth.html -->

## win32net.NetMessageNameEnum

 NetMessageNameEnum(Server)

Lists aliases for a computer

#### Parameters

- Server : str/unicode

 Name of server on which to execute - leading backslashes required on NT - local machine used if None


---

<!-- page: win32net__NetServerComputerNameAdd_meth.html -->

## win32net.NetServerComputerNameAdd

 NetServerComputerNameAdd(ServerName, EmulatedDomainName, EmulatedServerName)

Adds an additional network name for a server

#### Parameters

- ServerName : string/PyUnicode

 Name of server that will receive additional name

- EmulatedDomainName : string/PyUnicode

 Domain under which to add the new server name, can be None

- EmulatedServerName : string/PyUnicode

 New network name that server will respond to

#### Return Value

Returns none on success


---

<!-- page: win32net__NetServerComputerNameDel_meth.html -->

## win32net.NetServerComputerNameDel

 NetServerComputerNameDel(ServerName, EmulatedServerName)

Removes a network name added by win32net::NetServerComputerNameAdd

#### Parameters

- ServerName : string/PyUnicode

 Name of server on which to operate

- EmulatedServerName : string/PyUnicode

 Network name to be removed

#### Return Value

Returns none on success


---

<!-- page: win32net__NetServerDiskEnum_meth.html -->

## win32net.NetServerDiskEnum

 list = NetServerDiskEnum(server, level )

Retrieves the list of disk drives on a server.

#### Parameters

- server : string/PyUnicode

 The name of the server to execute on, or None.

- level : int

 The level of data required. Must be 0.

#### Win32 API References

- Search for NetServerDiskEnum at [msdn](https://learn.microsoft.com/en-ca/search/?terms=NetServerDiskEnum), [google](https://www.google.com/search?q=NetServerDiskEnum) or [google groups](https://groups.google.com/groups?q=NetServerDiskEnum).

#### Return Value

The result is a list of drives on the server


---

<!-- page: win32net__NetServerEnum_meth.html -->

## win32net.NetServerEnum

 ([dict, ...], total, resumeHandle) = NetServerEnum(server, level , type , domain , resumeHandle , prefLen )

Retrieves information about each server of a particular type

#### Parameters

- server : string/PyUnicode

 The name of the server to execute on, or None.

- level : int

 The level of data required.

- type=SV_TYPE_ALL : int

 Type of server to return - one of the SV_TYPE_* constants.

- domain=None : string/PyUnicode

 The domain to enumerate, or None for the current domain.

- resumeHandle=0 : int

 A resume handle. See the return description for more information.

- prefLen=MAX_PREFERRED_LENGTH : int

 The preferred length of the data buffer.

#### Win32 API References

- Search for NetServerEnum at [msdn](https://learn.microsoft.com/en-ca/search/?terms=NetServerEnum), [google](https://www.google.com/search?q=NetServerEnum) or [google groups](https://groups.google.com/groups?q=NetServerEnum).

#### Return Value

The result is a list of items read (with each item being a dictionary of format PySERVER_INFO_*, depending on the level parameter), the total available, and a new "resume handle". The first time you call this function, you should pass zero for the resume handle. If more data is available than what was returned, a new non-zero resume handle will be returned, which can be used to call the function again to fetch more data. This process may repeat, each time with a new resume handle, until zero is returned for the new handle, indicating all the data has been read.


---

<!-- page: win32net__NetServerGetInfo_meth.html -->

## win32net.NetServerGetInfo

 dict = NetServerGetInfo(server, level )

Retrieves information about a particular server.

#### Parameters

- server : string/PyUnicode

 The name of the server to execute on, or None.

- level : int

 The information level contained in the data

#### Win32 API References

- Search for NetServerGetInfo at [msdn](https://learn.microsoft.com/en-ca/search/?terms=NetServerGetInfo), [google](https://www.google.com/search?q=NetServerGetInfo) or [google groups](https://groups.google.com/groups?q=NetServerGetInfo).

#### Return Value

The result will be a dictionary in one of the PySERVER_INFO_* formats, depending on the level parameter.


---

<!-- page: win32net__NetServerSetInfo_meth.html -->

## win32net.NetServerSetInfo

 NetServerSetInfo(server, level, data)

Sets information about a particular server.

#### Parameters

- server : string/PyUnicode

 The name of the server, or None.

- level : int

 The information level contained in the data

- data : mapping

 A dictionary holding the share data.

#### Win32 API References

- Search for NetServerSetInfo at [msdn](https://learn.microsoft.com/en-ca/search/?terms=NetServerSetInfo), [google](https://www.google.com/search?q=NetServerSetInfo) or [google groups](https://groups.google.com/groups?q=NetServerSetInfo).


---

<!-- page: win32net__NetSessionDel_meth.html -->

## win32net.NetSessionDel

 NetSessionDel(server, client, username)

Disconnects network connections on a server

#### Parameters

- server : string/PyUnicode

 The name of the server on which to operate, local machine assumed if None or blank

- client=None : string/PyUnicode

 Name of client computer, or None

- username=None : string/PyUnicode

 User name, or None for all connected users

#### Return Value

Returns None on success


---

<!-- page: win32net__NetSessionEnum_meth.html -->

## win32net.NetSessionEnum

 (dict,...) = NetSessionEnum(level, server , client , username )

Returns network sessions for a server, limited to single client and/or user if specified.

#### Parameters

- level : int

 Level of information requested, currently accepts 0, 1, 2, 10, and 502

- server=None : string/PyUnicode

 The name of the server for which to list sessions, local machine assumed if None

- client=None : string/PyUnicode

 Name of client computer, or None to list all computer sessions

- username=None : string/PyUnicode

 User name, or None to list all connected users

#### Return Value

Returns a sequence of dictionaries representing SESSION_INFO_* structs, depending on level specified


---

<!-- page: win32net__NetSessionGetInfo_meth.html -->

## win32net.NetSessionGetInfo

 dict = NetSessionGetInfo(level, server , client , username )

Returns information for a network session from specified client

#### Parameters

- level : int

 Level of information requested, currently accepts 0, 1, 2, 10, and 502

- server : string/PyUnicode

 The name of the server on which to operate, None or blank assumes local machine

- client : string/PyUnicode

 Name of client computer

- username : string/PyUnicode

 User that established session

#### Return Value

Returns a dictionary representing a SESSION_INFO_* struct, depending on level specified


---

<!-- page: win32net__NetShareAdd_meth.html -->

## win32net.NetShareAdd

 NetShareAdd(server, level, data)

Creates a new share.

#### Parameters

- server : string/PyUnicode

 The name of the server, or None.

- level : int

 The information level contained in the data. Must be level 2 or 502.

- data : mapping

 A dictionary holding the share data, in the format of SHARE_INFO_*

#### Win32 API References

- Search for NetShareAdd at [msdn](https://learn.microsoft.com/en-ca/search/?terms=NetShareAdd), [google](https://www.google.com/search?q=NetShareAdd) or [google groups](https://groups.google.com/groups?q=NetShareAdd).


---

<!-- page: win32net__NetShareCheck_meth.html -->

## win32net.NetShareCheck

 (ret, type) = NetShareCheck(server, deviceName )

Checks if server is sharing a device

#### Parameters

- server : string/PyUnicode

 The name of the server, or None.

- deviceName : string/PyUnicode

 The share name

#### Win32 API References

- Search for NetShareCheck at [msdn](https://learn.microsoft.com/en-ca/search/?terms=NetShareCheck), [google](https://www.google.com/search?q=NetShareCheck) or [google groups](https://groups.google.com/groups?q=NetShareCheck).

#### Return Value

The result is (1, type-of-device) if device is shared, (0, None) if it is not shared.


---

<!-- page: win32net__NetShareDel_meth.html -->

## win32net.NetShareDel

 NetShareDel(server, shareName, reserved)

Deletes a share

#### Parameters

- server : string/PyUnicode

 The name of the server, or None.

- shareName : string/PyUnicode

 The share name

- reserved=0 : int

 Must be zero.

#### Win32 API References

- Search for NetShareDel at [msdn](https://learn.microsoft.com/en-ca/search/?terms=NetShareDel), [google](https://www.google.com/search?q=NetShareDel) or [google groups](https://groups.google.com/groups?q=NetShareDel).


---

<!-- page: win32net__NetShareEnum_meth.html -->

## win32net.NetShareEnum

 ([dict, ...], total, resumeHandle) = NetShareEnum(server, level , resumeHandle , prefLen )

Retrieves information about each shared resource on a server.

#### Parameters

- server : string/PyUnicode

 The name of the server, or None.

- level : int

 The level of data required.

- resumeHandle=0 : int

 A resume handle. See the return description for more information.

- prefLen=MAX_PREFERRED_LENGTH : int

 The preferred length of the data buffer.

#### Alternative Parameters

- serverName

 The name of the server on which the call should execute, or None for the local computer.

#### Comments

 If the old style is used, the result is a list of [(shareName, type, remarks), ...]

#### Win32 API References

- Search for NetShareEnum param 1 is not declared as const :-( at [msdn](https://learn.microsoft.com/en-ca/search/?terms=NetShareEnum

param 1 is not declared as const :-(), [google](https://www.google.com/search?q=NetShareEnum

param 1 is not declared as const :-() or [google groups](https://groups.google.com/groups?q=NetShareEnum

param 1 is not declared as const :-().

#### Return Value

The result is a list of items read (with each item being a dictionary of format PySHARE_INFO_*, depending on the level parameter), the total available, and a new "resume handle". The first time you call this function, you should pass zero for the resume handle. If more data is available than what was returned, a new non-zero resume handle will be returned, which can be used to call the function again to fetch more data. This process may repeat, each time with a new resume handle, until zero is returned for the new handle, indicating all the data has been read.


---

<!-- page: win32net__NetShareGetInfo_meth.html -->

## win32net.NetShareGetInfo

 dict = NetShareGetInfo(server, netname , level )

Retrieves information about a particular share on a server.

#### Parameters

- server : string/PyUnicode

 The name of the server, or None.

- netname : string/PyUnicode

 The network name

- level : int

 The information level contained in the data

#### Win32 API References

- Search for NetShareGetInfo at [msdn](https://learn.microsoft.com/en-ca/search/?terms=NetShareGetInfo), [google](https://www.google.com/search?q=NetShareGetInfo) or [google groups](https://groups.google.com/groups?q=NetShareGetInfo).

#### Return Value

The result will be a dictionary in one of the PySHARE_INFO_* formats, depending on the level parameter.


---

<!-- page: win32net__NetShareSetInfo_meth.html -->

## win32net.NetShareSetInfo

 NetShareSetInfo(server, netname, level, data)

Sets information about a particular share on a server.

#### Parameters

- server : string/PyUnicode

 The name of the server, or None.

- netname : string/PyUnicode

 The network name

- level : int

 The information level contained in the data

- data : mapping

 A dictionary holding the share data.

#### Win32 API References

- Search for NetShareSetInfo at [msdn](https://learn.microsoft.com/en-ca/search/?terms=NetShareSetInfo), [google](https://www.google.com/search?q=NetShareSetInfo) or [google groups](https://groups.google.com/groups?q=NetShareSetInfo).


---

<!-- page: win32net__NetStatisticsGet_meth.html -->

## win32net.NetStatisticsGet

 dict = NetStatisticsGet(server, service , level , options )

Retrieves network statistics for specified service on specified machine

#### Parameters

- server : string/PyUnicode

 Name of server/workstation to retrieve statistics for (None or blank uses local).

- service : string/PyUnicode

 SERVICE_SERVER or SERVICE_WORKSTATION

- level : int

 Only 0 currently supported.

- options : int

 Must be zero.

#### Return Value

The result is a dictionary representing a STAT_SERVER_0 or STAT_WORKSTATION_0 struct


---

<!-- page: win32net__NetUseAdd_meth.html -->

## win32net.NetUseAdd

 NetUseAdd(server, level, data)

Establishes connection between local or NULL device name and a shared resource through redirector

#### Parameters

- server : string/PyUnicode

 The name of the server, or None.

- level : int

 The information level contained in the data

- data : mapping

 A dictionary holding the share data in the format of PyUSE_INFO_*.

#### Win32 API References

- Search for NetUseAdd at [msdn](https://learn.microsoft.com/en-ca/search/?terms=NetUseAdd), [google](https://www.google.com/search?q=NetUseAdd) or [google groups](https://groups.google.com/groups?q=NetUseAdd).


---

<!-- page: win32net__NetUseDel_meth.html -->

## win32net.NetUseDel

 NetUseDel(server, useName, forceCond)

Ends connection to a shared resource.

#### Parameters

- server : string/PyUnicode

 The name of the server, or None.

- useName : string/PyUnicode

 The share name

- forceCond=0 : int

 Level of force to use. Can be USE_FORCE or USE_NOFORCE or USE_LOTS_OF_FORCE

#### Win32 API References

- Search for NetUseDel at [msdn](https://learn.microsoft.com/en-ca/search/?terms=NetUseDel), [google](https://www.google.com/search?q=NetUseDel) or [google groups](https://groups.google.com/groups?q=NetUseDel).


---

<!-- page: win32net__NetUseEnum_meth.html -->

## win32net.NetUseEnum

 ([dict, ...], total, resumeHandle) = NetUseEnum(server, level , resumeHandle , prefLen )

Retrieves information about transport protocols that are currently managed by the redirector

#### Parameters

- server : string/PyUnicode

 The name of the server to execute on, or None.

- level : int

 The level of data required. Currently levels 0, 1 and 2 are supported.

- resumeHandle=0 : int

 A resume handle. See the return description for more information.

- prefLen=MAX_PREFERRED_LENGTH : int

 The preferred length of the data buffer.

#### Win32 API References

- Search for NetUseEnum at [msdn](https://learn.microsoft.com/en-ca/search/?terms=NetUseEnum), [google](https://www.google.com/search?q=NetUseEnum) or [google groups](https://groups.google.com/groups?q=NetUseEnum).

#### Return Value

The result is a list of items read (with each item being a dictionary of format PyUSE_INFO_*, depending on the level parameter), the total available, and a new "resume handle". The first time you call this function, you should pass zero for the resume handle. If more data is available than what was returned, a new non-zero resume handle will be returned, which can be used to call the function again to fetch more data. This process may repeat, each time with a new resume handle, until zero is returned for the new handle, indicating all the data has been read.


---

<!-- page: win32net__NetUseGetInfo_meth.html -->

## win32net.NetUseGetInfo

 dict = NetUseGetInfo(server, usename , level )

Retrieves information about the configuration elements for a workstation

#### Parameters

- server : string/PyUnicode

 The name of the server to execute on, or None.

- usename : string/PyUnicode

 The name of the locally mapped resource.

- level=0 : int

 The information level contained in the data. NOTE: levels 302 and 402 don't seem to work correctly. They return error 124. So currently these info levels are not available.

#### Win32 API References

- Search for NetUseGetInfo at [msdn](https://learn.microsoft.com/en-ca/search/?terms=NetUseGetInfo), [google](https://www.google.com/search?q=NetUseGetInfo) or [google groups](https://groups.google.com/groups?q=NetUseGetInfo).

#### Return Value

The result will be a dictionary in one of the PyUSE_INFO_* formats, depending on the level parameter.


---

<!-- page: win32net__NetUserAdd_meth.html -->

## win32net.NetUserAdd

 NetUserAdd(server, level, data)

Creates a new user.

#### Parameters

- server : string/PyUnicode

 The name of the server, or None.

- level : int

 The information level contained in the data

- data : mapping

 A dictionary holding the user data in the format of PyUSER_INFO_*.

#### Win32 API References

- Search for NetUserAdd at [msdn](https://learn.microsoft.com/en-ca/search/?terms=NetUserAdd), [google](https://www.google.com/search?q=NetUserAdd) or [google groups](https://groups.google.com/groups?q=NetUserAdd).


---

<!-- page: win32net__NetUserChangePassword_meth.html -->

## win32net.NetUserChangePassword

 NetUserChangePassword(server, username, oldPassword, newPassword)

Changes the password for a user.

#### Parameters

- server : string/PyUnicode

 The name of the server, or None.

- username : string/PyUnicode

 The user name, or None for the current username.

- oldPassword : string/PyUnicode

 The old password

- newPassword : string/PyUnicode

 The new password

#### Comments

 A server or domain can be configured to require that a user log on to change the password on a user account. If that is the case, you need administrator or account operator access to change the password for another user acount. If logging on is not required, you can change the password for any user account, so long as you know the current password.

#### Win32 API References

- Search for NetUserChangePassword at [msdn](https://learn.microsoft.com/en-ca/search/?terms=NetUserChangePassword), [google](https://www.google.com/search?q=NetUserChangePassword) or [google groups](https://groups.google.com/groups?q=NetUserChangePassword).


---

<!-- page: win32net__NetUserDel_meth.html -->

## win32net.NetUserDel

 NetUserDel(server, username)

Deletes a user.

#### Parameters

- server : string/PyUnicode

 The name of the server, or None.

- username : string/PyUnicode

 The user name

#### Win32 API References

- Search for NetUserDel at [msdn](https://learn.microsoft.com/en-ca/search/?terms=NetUserDel), [google](https://www.google.com/search?q=NetUserDel) or [google groups](https://groups.google.com/groups?q=NetUserDel).


---

<!-- page: win32net__NetUserEnum_meth.html -->

## win32net.NetUserEnum

 ([dict, ...], total, resumeHandle) = NetUserEnum(server, level , filter , resumeHandle , prefLen )

Enumerates all users.

#### Parameters

- server : string/PyUnicode

 The name of the server, or None.

- level : int

 The level of data required.

- filter=win32netcon.FILTER_NORMAL_ACCOUNT : int

 The types of accounts to enumerate.

- resumeHandle=0 : int

 A resume handle. See the return description for more information.

- prefLen=MAX_PREFERRED_LENGTH : int

 The preferred length of the data buffer.

#### Win32 API References

- Search for NetUserEnum at [msdn](https://learn.microsoft.com/en-ca/search/?terms=NetUserEnum), [google](https://www.google.com/search?q=NetUserEnum) or [google groups](https://groups.google.com/groups?q=NetUserEnum).

#### Return Value

The result is a list of items read (with each item being a dictionary of format PyUSER_INFO_*, depending on the level parameter), the total available, and a new "resume handle". The first time you call this function, you should pass zero for the resume handle. If more data is available than what was returned, a new non-zero resume handle will be returned, which can be used to call the function again to fetch more data. This process may repeat, each time with a new resume handle, until zero is returned for the new handle, indicating all the data has been read.


---

<!-- page: win32net__NetUserGetGroups_meth.html -->

## win32net.NetUserGetGroups

 [(groupName, attribute), ...] = NetUserGetGroups(serverName, userName )

Returns a list of groups,attributes for all groups for the user.

#### Parameters

- serverName : string

 The name of the remote server on which the function is to execute. None or an empty string specifies the server program running on the local computer.

- userName : string

 The name of the user to search for in each group account.

#### To Do

 This needs to be extended to support the new model, while not breaking existing code. A default arg would be perfect.

#### Return Value

Always makes the level 1 call and returns all data. Data return format is a Python List. Each "Item" is a tuple of (groupname, attributes). "(s,i)" respectively. In NT 4 the attributes seem to be hardcoded to 7. Earlier version of NT have not been tested.


---

<!-- page: win32net__NetUserGetInfo_meth.html -->

## win32net.NetUserGetInfo

 dict = NetUserGetInfo(server, username , level )

Retrieves information about a particular user account on a server.

#### Parameters

- server : string/PyUnicode

 The name of the server, or None.

- username : string/PyUnicode

 The user name

- level : int

 The information level contained in the data

#### Win32 API References

- Search for NetUserGetInfo at [msdn](https://learn.microsoft.com/en-ca/search/?terms=NetUserGetInfo), [google](https://www.google.com/search?q=NetUserGetInfo) or [google groups](https://groups.google.com/groups?q=NetUserGetInfo).

#### Return Value

The result will be a dictionary in one of the PyUSER_INFO_* formats, depending on the level parameter.


---

<!-- page: win32net__NetUserGetLocalGroups_meth.html -->

## win32net.NetUserGetLocalGroups

 [groupName, ...] = NetUserGetLocalGroups(serverName, userName , flags )

Retrieves a list of local groups to which a specified user belongs.

#### Parameters

- serverName : string

 The name of the remote server on which the function is to execute. None or an empty string specifies the server program running on the local computer.

- userName : string

 The name of the user to search for in each group account. This parameter can be of the form <UserName>, in which case the username is expected to be found on servername. The user name can also be of the form <DomainName>\\<UserName> in which case <DomainName> is associated with servername and <UserName> is expected to be to be found on that domain.

- flags=LG_INCLUDE_INDIRECT : int

 Flags for the call.

#### To Do

 This needs to be extended to support the new model, while not breaking existing code. A default arg would be perfect.


---

<!-- page: win32net__NetUserModalsGet_meth.html -->

## win32net.NetUserModalsGet

 dict = NetUserModalsGet(server, level )

Retrieves global user information on a server.

#### Parameters

- server : string/PyUnicode

 The name of the server, or None.

- level : int

 The information level contained in the data

#### Win32 API References

- Search for NetUserModalsGet at [msdn](https://learn.microsoft.com/en-ca/search/?terms=NetUserModalsGet), [google](https://www.google.com/search?q=NetUserModalsGet) or [google groups](https://groups.google.com/groups?q=NetUserModalsGet).

#### Return Value

The result will be a dictionary in one of the PyUSER_MODALS_INFO_* formats, depending on the level parameter.


---

<!-- page: win32net__NetUserModalsSet_meth.html -->

## win32net.NetUserModalsSet

 NetUserModalsSet(server, level, data)

Sets global user parameters on a server.

#### Parameters

- server : string/PyUnicode

 The name of the server, or None.

- level : int

 The information level contained in the data

- data : mapping

 A dictionary holding the data in the format of PyUSER_MODALS_INFO_*.

#### Win32 API References

- Search for NetUserModalsSet at [msdn](https://learn.microsoft.com/en-ca/search/?terms=NetUserModalsSet), [google](https://www.google.com/search?q=NetUserModalsSet) or [google groups](https://groups.google.com/groups?q=NetUserModalsSet).


---

<!-- page: win32net__NetUserSetInfo_meth.html -->

## win32net.NetUserSetInfo

 NetUserSetInfo(server, username, level, data)

Sets information about a particular user account on a server.

#### Parameters

- server : string/PyUnicode

 The name of the server, or None.

- username : string/PyUnicode

 The user name

- level : int

 The information level contained in the data

- data : mapping

 A dictionary holding the user data in the format of PyUSER_INFO_*

#### Win32 API References

- Search for NetUserSetInfo at [msdn](https://learn.microsoft.com/en-ca/search/?terms=NetUserSetInfo), [google](https://www.google.com/search?q=NetUserSetInfo) or [google groups](https://groups.google.com/groups?q=NetUserSetInfo).


---

<!-- page: win32net__NetValidateName_meth.html -->

## win32net.NetValidateName

 NetValidateName(Server, Name, NameType, Account, Password)

Checks that domain/machine/workgroup name is valid for given context

#### Parameters

- Server : string/PyUnicode

 Name of server on which to execute (None or blank uses local)

- Name : string/PyUnicode

 Machine, domain, or workgroup name to validate

- NameType : int

 Type of name to validate - from NETSETUP_NAME_TYPE enum (win32net.NetSetup*)

- Account=None : string/PyUnicode

 Account name to use while validating, current security context is used if not specified

- Password=None : string/PyUnicode

 Password for Account

#### Comments

 If Account and Password aren't passed, current logon credentials are used

#### Return Value

Returns none if valid, exception if not


---

<!-- page: win32net__NetValidatePasswordPolicy_meth.html -->

## win32net.NetValidatePasswordPolicy

 NetValidatePasswordPolicy(Server, Qualifier, ValidationType, arg)

Allows an application to check password compliance against an application-provided account database and verify that passwords meet the complexity, aging, minimum length, and history reuse requirements of a password policy.

#### Parameters

- Server : string/PyUnicode

 Name of server on which to execute (None or blank uses local)

- Qualifier : None

 Reserved, must be None

- ValidationType : int

 The type of password validation to perform

- arg : dict/tuple

 Depends on the ValidationType param - either a PyNET_VALIDATE_AUTHENTICATION_INPUT_ARG, PyNET_VALIDATE_PASSWORD_CHANGE_INPUT_ARG or PyNET_VALIDATE_PASSWORD_RESET_INPUT_ARG tuple or dict.

#### Comments

 Will raise win32net.error if the function fails.

#### Return Value

Returns a tuple of (PyNET_VALIDATE_PERSISTED_FIELDS, int) with the integer being the ValidationResult.


---

<!-- page: win32net__NetWkstaGetInfo_meth.html -->

## win32net.NetWkstaGetInfo

 dict = NetWkstaGetInfo(server, level )

Retrieves information about the configuration elements for a workstation

#### Parameters

- server : string/PyUnicode

 The name of the server to execute on, or None.

- level : int

 The information level contained in the data. NOTE: levels 302 and 402 don't seem to work correctly. They return error 124. So currently these info levels are not available.

#### Win32 API References

- Search for NetWkstaGetInfo at [msdn](https://learn.microsoft.com/en-ca/search/?terms=NetWkstaGetInfo), [google](https://www.google.com/search?q=NetWkstaGetInfo) or [google groups](https://groups.google.com/groups?q=NetWkstaGetInfo).

#### Return Value

The result will be a dictionary in one of the PyWKSTA_INFO_* formats, depending on the level parameter.


---

<!-- page: win32net__NetWkstaSetInfo_meth.html -->

## win32net.NetWkstaSetInfo

 NetWkstaSetInfo(server, level, data)

Sets information about the configuration elements for a workstation

#### Parameters

- server : string/PyUnicode

 The name of the server, or None.

- level : int

 The information level contained in the data

- data : mapping

 A dictionary holding the share data.

#### Win32 API References

- Search for NetWkstaSetInfo at [msdn](https://learn.microsoft.com/en-ca/search/?terms=NetWkstaSetInfo), [google](https://www.google.com/search?q=NetWkstaSetInfo) or [google groups](https://groups.google.com/groups?q=NetWkstaSetInfo).


---

<!-- page: win32net__NetWkstaTransportAdd_meth.html -->

## win32net.NetWkstaTransportAdd

 NetWkstaTransportAdd(server, level, data)

binds the redirector to a transport

#### Parameters

- server : string/PyUnicode

 The name of the server, or None.

- level : int

 The information level contained in the data

- data : mapping

 A dictionary holding the share data.

#### Win32 API References

- Search for NetWkstaTransportAdd at [msdn](https://learn.microsoft.com/en-ca/search/?terms=NetWkstaTransportAdd), [google](https://www.google.com/search?q=NetWkstaTransportAdd) or [google groups](https://groups.google.com/groups?q=NetWkstaTransportAdd).


---

<!-- page: win32net__NetWkstaTransportDel_meth.html -->

## win32net.NetWkstaTransportDel

 NetWkstaTransportDel(server, TransportName, ucond)

unbinds the transport protocol from redirector

#### Parameters

- server : string/PyUnicode

 The name of the server, or None.

- TransportName : string/PyUnicode

 The name of the transport to delete.

- ucond=0 : int

 Level of force to use. Can be USE_FORCE or USE_NOFORCE or USE_LOTS_OF_FORCE

#### Win32 API References

- Search for NetWkstaTransportDel at [msdn](https://learn.microsoft.com/en-ca/search/?terms=NetWkstaTransportDel), [google](https://www.google.com/search?q=NetWkstaTransportDel) or [google groups](https://groups.google.com/groups?q=NetWkstaTransportDel).


---

<!-- page: win32net__NetWkstaTransportEnum_meth.html -->

## win32net.NetWkstaTransportEnum

 ([dict, ...], total, resumeHandle) = NetWkstaTransportEnum(server, level , resumeHandle , prefLen )

Retrieves information about transport protocols that are currently managed by the redirector

#### Parameters

- server : string/PyUnicode

 The name of the server to execute on, or None.

- level : int

 The level of data required.

- resumeHandle=0 : int

 A resume handle. See the return description for more information.

- prefLen=MAX_PREFERRED_LENGTH : int

 The preferred length of the data buffer.

#### Win32 API References

- Search for NetWkstaTransportEnum at [msdn](https://learn.microsoft.com/en-ca/search/?terms=NetWkstaTransportEnum), [google](https://www.google.com/search?q=NetWkstaTransportEnum) or [google groups](https://groups.google.com/groups?q=NetWkstaTransportEnum).

#### Return Value

The result is a list of items read (with each item being a dictionary of format PyWKSTA_TRANSPORT_INFO_*, depending on the level parameter), the total available, and a new "resume handle". The first time you call this function, you should pass zero for the resume handle. If more data is available than what was returned, a new non-zero resume handle will be returned, which can be used to call the function again to fetch more data. This process may repeat, each time with a new resume handle, until zero is returned for the new handle, indicating all the data has been read.


---

<!-- page: win32net__NetWkstaUserEnum_meth.html -->

## win32net.NetWkstaUserEnum

 ([dict, ...], total, resumeHandle) = NetWkstaUserEnum(server, level , resumeHandle , prefLen )

Retrieves information about all users currently logged on to the workstation.

#### Parameters

- server : string/PyUnicode

 The name of the server to execute on, or None.

- level : int

 The level of data required.

- resumeHandle=0 : int

 A resume handle. See the return description for more information.

- prefLen=MAX_PREFERRED_LENGTH : int

 The preferred length of the data buffer.

#### Win32 API References

- Search for NetWkstaUserEnum at [msdn](https://learn.microsoft.com/en-ca/search/?terms=NetWkstaUserEnum), [google](https://www.google.com/search?q=NetWkstaUserEnum) or [google groups](https://groups.google.com/groups?q=NetWkstaUserEnum).

#### Return Value

The result is a list of items read (with each item being a dictionary of format PyWKSTA_USER_INFO_*, depending on the level parameter), the total available, and a new "resume handle". The first time you call this function, you should pass zero for the resume handle. If more data is available than what was returned, a new non-zero resume handle will be returned, which can be used to call the function again to fetch more data. This process may repeat, each time with a new resume handle, until zero is returned for the new handle, indicating all the data has been read.
