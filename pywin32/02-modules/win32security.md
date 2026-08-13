# 模块 win32security

> 来源：https://mhammond.github.io/pywin32/win32security.html （及其成员页，已全部内联）

## Module win32security

 An interface to the win32 security API's

#### Methods

- DsGetSpn

 Compose one or more service principal names to be registered using win32security::DsWriteAccountSpn

- DsWriteAccountSpn

 Associates a set of service principal names with an account

- DsBind

 Creates a connection to a directory service

- DsUnBind

 Closes a directory services handle created by win32security::DsBind

- DsGetDcName

 Returns the name of a domain controller (DC) in a specified domain. You can supply DC selection criteria to this function to indicate preference for a DC with particular characteristics.

- DsCrackNames

 Converts an array of directory service object names from one format to another.

- DsListInfoForServer

 Lists miscellaneous information for a server.

- DsListServersInSite

- DsListServersInSite

- DsListServersInSite

- DsListRoles

- DsListDomainsInSite

- ACL

 Creates a new PyACL object.

- SID

 Creates a new PySID object.

- SECURITY_ATTRIBUTES

 Creates a new PySECURITY_ATTRIBUTES object.

- SECURITY_DESCRIPTOR

 Creates a new PySECURITY_DESCRIPTOR object.

- ImpersonateNamedPipeClient

 Impersonates a named-pipe client application.

- ImpersonateLoggedOnUser

 Impersonates a logged on user.

- ImpersonateAnonymousToken

 Cause a thread to act in the security context of an anonymous token

- IsTokenRestricted

 Checks if a token contains restricted sids

- RevertToSelf

 Terminates the impersonation of a client application.

- LogonUser

 Attempts to log a user on to the local computer, that is, to the computer from which LogonUser was called. You cannot use LogonUser to log on to a remote computer.

- LogonUserEx

 Log a user onto the local machine,

- LookupAccountName

 Accepts the name of a system and an account as input. It retrieves a security identifier (SID) for the account and the name of the domain on which the account was found.

- LookupAccountSid

 Accepts a security identifier (SID) as input. It retrieves the name of the account for this SID and the name of the first domain on which this SID is found.

- GetBinarySid

 Accepts a SID string (eg: S-1-5-32-544) and returns the SID as a PySID object.

- SetSecurityInfo

 Sets security info for an object by handle

- GetSecurityInfo

 Retrieve security info for an object by handle

- SetNamedSecurityInfo

 Sets security info for an object by name

- GetNamedSecurityInfo

 Retrieve security info for an object by name

- OpenProcessToken

 Opens the access token associated with a process.

- LookupPrivilegeValue

 Retrieves the locally unique id for a privilege name

- LookupPrivilegeName

 return the text name for a privilege LUID

- LookupPrivilegeDisplayName

 Returns long description for a privilege name

- AdjustTokenPrivileges

 Enables or disables privileges for an access token.

- AdjustTokenGroups

 Sets the groups associated to an access token.

- GetTokenInformation

 Retrieves a specified type of information about an access token. The calling process must have appropriate access rights to obtain the information.

- OpenThreadToken

 Opens the access token associated with a thread.

- SetThreadToken

 Assigns an impersonation token to a thread. The function can also cause a thread to stop using an impersonation token.

- GetFileSecurity

 Obtains specified information about the security of a file or directory. The information obtained is constrained by the caller's access rights and privileges.

- SetFileSecurity

 Sets information about the security of a file or directory. The information obtained is constrained by the caller's access rights and privileges.

- GetUserObjectSecurity

 Obtains specified information about the security of a user object. The information obtained is constrained by the caller's access rights and privileges.

- SetUserObjectSecurity

 Sets information about the security of a user object. The information obtained is constrained by the caller's access rights and privileges.

- GetKernelObjectSecurity

 Obtains specified information about the security of a kernel object. The information obtained is constrained by the caller's access rights and privileges.

- SetKernelObjectSecurity

 Sets information about the security of a kernel object. The information obtained is constrained by the caller's access rights and privileges.

- SetTokenInformation

 Set a specified type of information in an access token

- LsaOpenPolicy

 Opens a policy handle for the specified system

- LsaClose

 Closes a policy handle created by win32security::LsaOpenPolicy

- LsaQueryInformationPolicy

 Retrieves information from the policy handle

- LsaSetInformationPolicy

 Sets policy options

- LsaAddAccountRights

 Adds a list of privileges to an account

- LsaRemoveAccountRights

 Removes privs from an account

- LsaEnumerateAccountRights

 Lists privileges held by SID

- LsaEnumerateAccountsWithUserRight

 Return SIDs that hold specified priv

- ConvertSidToStringSid

 Return string representation of a SID

- ConvertStringSidToSid

 Creates a SID from a string representation

- ConvertSecurityDescriptorToStringSecurityDescriptor

 Return string representation of a SECURITY_DESCRIPTOR

- ConvertStringSecurityDescriptorToSecurityDescriptor

 Turns string representation of a SECURITY_DESCRIPTOR into the real thing

- LsaStorePrivateData

 Stores encrypted unicode data under specified Lsa registry key. Returns None on success

- LsaRetrievePrivateData

 Retreives encrypted unicode data from Lsa registry key.

- LsaRegisterPolicyChangeNotification

 Register an event handle to receive policy change events

- LsaUnregisterPolicyChangeNotification

 Stop receiving policy change notification

- CryptEnumProviders

 List cryptography providers

- EnumerateSecurityPackages

 List available security packages as a sequence of dictionaries representing SecPkgInfo structures

- AllocateLocallyUniqueId

 Creates a new LUID

- ImpersonateSelf

 Assigns an impersonation token for current security context to current process

- DuplicateToken

 Creates a copy of an access token with specified impersonation level

- DuplicateTokenEx

 Extended version of DuplicateToken.

- CheckTokenMembership

 Checks if a SID is enabled in a token

- CreateRestrictedToken

 Creates a restricted copy of an access token with reduced privs - requires win2K or higher

- LsaRegisterLogonProcess

 Creates a trusted connection to LSA

- LsaConnectUntrusted

 Creates untrusted connection to LSA

- LsaDeregisterLogonProcess

 Closes connection to LSA server

- LsaLookupAuthenticationPackage

 Retrieves the unique id for an authentication package

- LsaEnumerateLogonSessions

 Lists all current logon ids

- LsaGetLogonSessionData

 Returns information about a logon session

- AcquireCredentialsHandle

 Creates a handle to credentials for use with SSPI

- InitializeSecurityContext

 Creates a security context based on credentials created by AcquireCredentialsHandle

- AcceptSecurityContext

 Builds security context between server and client

- QuerySecurityPackageInfo

 Retrieves parameters for a security package

- LsaCallAuthenticationPackage

 Requests the services of an authentication package

- TranslateName

 Converts a directory service object name from one format to another.

- CreateWellKnownSid

 Returns one of the predefined well known sids

- MapGenericMask

 Translates generic access rights into specific rights


---

# win32security 成员详细文档（共 84 项）


---

<!-- page: win32security__ACL_meth.html -->

## win32security.ACL

 PyACL = ACL(bufSize)

Creates a new PyACL object.

#### Parameters

- bufSize=64 : int

 The size of the buffer for the ACL.


---

<!-- page: win32security__AcceptSecurityContext_meth.html -->

## win32security.AcceptSecurityContext

 (int, long, int) = AcceptSecurityContext(Credential, Context , pInput , ContextReq , TargetDataRep , NewContext , pOutput )

Builds security context between server and client

#### Parameters

- Credential : PyCredHandle

 Handle to server's credentials (see AcquireCredentialsHandle)

- Context : PyCtxtHandle

 Use None on initial call, then handle returned in NewContext thereafter

- pInput : PySecBufferDesc

 Data buffer received from client

- ContextReq : int

 Combination of ASC_REQ_* flags

- TargetDataRep : int

 One of SECURITY_NATIVE_DREP,SECURITY_NETWORK_DREP

- NewContext : PyCtxtHandle

 Uninitialized context handle to receive output

- pOutput : PySecBufferDesc

 Buffer that receives output data, to be passed back as pInput on subsequent calls

#### Return Value

Returns a tuple of (return code, context attributes, context expiration time)


---

<!-- page: win32security__AcquireCredentialsHandle_meth.html -->

## win32security.AcquireCredentialsHandle

 (PyCredHandle,PyDateTime) = AcquireCredentialsHandle(Principal, Package , CredentialUse , LogonID , AuthData )

Creates a handle to credentials for use with SSPI

#### Parameters

- Principal : str/unicode

 Use None for current security context

- Package : str/unicode

 Name of security package that credentials will be used with

- CredentialUse : int

 Intended use of requested credentials, SECPKG_CRED_INBOUND, SECPKG_CRED_OUTBOUND, or SECPKG_CRED_BOTH

- LogonID : long

 LUID representing a logon session, can be None

- AuthData : tuple

 Sequence of 3 strings: (User, Domain, Password) - use none for existing credentials

#### Return Value

Returns credential handle and credential's expiration time


---

<!-- page: win32security__AdjustTokenGroups_meth.html -->

## win32security.AdjustTokenGroups

 PyTOKEN_GROUPS = AdjustTokenGroups(TokenHandle, ResetToDefault , NewState )

Sets the groups associated to an access token.

#### Parameters

- TokenHandle : PyHANDLE

 The handle to access token to be modified

- ResetToDefault : boolean

 Sets groups to default enabled/disabled states,

- NewState : PyTOKEN_GROUPS

 Groups and attributes to be set for token

#### Comments

 Accepts keyword args.

#### Return Value

Returns previous state of groups modified


---

<!-- page: win32security__AdjustTokenPrivileges_meth.html -->

## win32security.AdjustTokenPrivileges

 PyTOKEN_PRIVILEGES = AdjustTokenPrivileges(TokenHandle, bDisableAllPrivileges , NewState )

Enables or disables privileges for an access token.

#### Parameters

- TokenHandle : PyHANDLE

 Handle to an access token

- bDisableAllPrivileges : int

 Flag for disabling all privileges

- NewState : PyTOKEN_PRIVILEGES

 The new state, can be None if bDisableAllPrivileges is True

#### Comments

 Accepts keyword args.

#### Return Value

Returns modified privileges for later restoral. Privileges deleted from the token using SE_PRIVILEGE_REMOVED are not returned.


---

<!-- page: win32security__AllocateLocallyUniqueId_meth.html -->

## win32security.AllocateLocallyUniqueId

 AllocateLocallyUniqueId()

Creates a new LUID


---

<!-- page: win32security__CheckTokenMembership_meth.html -->

## win32security.CheckTokenMembership

 bool = CheckTokenMembership(TokenHandle, SidToCheck )

Checks if a SID is enabled in a token

#### Parameters

- TokenHandle : PyHANDLE

 Handle to an access token, current process token used if None

- SidToCheck : PySID

 Sid to be checked for presence in token


---

<!-- page: win32security__ConvertSecurityDescriptorToStringSecurityDescriptor_meth.html -->

## win32security.ConvertSecurityDescriptorToStringSecurityDescriptor

 string = ConvertSecurityDescriptorToStringSecurityDescriptor(SecurityDescriptor, RequestedStringSDRevision , SecurityInformation )

Return string representation of a SECURITY_DESCRIPTOR

#### Parameters

- SecurityDescriptor : PySECURITY_DESCRIPTOR

 PySECURITY_DESCRIPTOR object

- RequestedStringSDRevision : int

 Only SDDL_REVISION_1 currently valid

- SecurityInformation : int

 Combination of bit flags from SECURITY_INFORMATION enum


---

<!-- page: win32security__ConvertSidToStringSid_meth.html -->

## win32security.ConvertSidToStringSid

 string = ConvertSidToStringSid(Sid)

Return string representation of a SID

#### Parameters

- Sid : PySID

 PySID object


---

<!-- page: win32security__ConvertStringSecurityDescriptorToSecurityDescriptor_meth.html -->

## win32security.ConvertStringSecurityDescriptorToSecurityDescriptor

 PySECURITY_DESCRIPTOR = ConvertStringSecurityDescriptorToSecurityDescriptor(StringSecurityDescriptor, StringSDRevision )

Turns string representation of a SECURITY_DESCRIPTOR into the real thing

#### Parameters

- StringSecurityDescriptor : string

 String representation of a SECURITY_DESCRIPTOR

- StringSDRevision : int

 Only SDDL_REVISION_1 currently valid


---

<!-- page: win32security__ConvertStringSidToSid_meth.html -->

## win32security.ConvertStringSidToSid

 PySID = ConvertStringSidToSid(StringSid)

Creates a SID from a string representation

#### Parameters

- StringSid : string

 String representation of a SID


---

<!-- page: win32security__CreateRestrictedToken_meth.html -->

## win32security.CreateRestrictedToken

 PyHANDLE = CreateRestrictedToken(ExistingTokenHandle, Flags , SidsToDisable , PrivilegesToDelete , SidsToRestrict )

Creates a restricted copy of an access token with reduced privs - requires win2K or higher

#### Parameters

- ExistingTokenHandle : PyHANDLE

 Handle to an access token (see win32security::LogonUser,win32security::OpenProcessToken

- Flags : int

 Valid values are zero or a combination of DISABLE_MAX_PRIVILEGE and SANDBOX_INERT

- SidsToDisable : (PySID_AND_ATTRIBUTES,...)

 Ssequence of PySID_AND_ATTRIBUTES tuples, or None

- PrivilegesToDelete : (PyLUID_AND_ATTRIBUTES,...)

 Privilege LUIDS to remove from token (attributes are ignored), or None

- SidsToRestrict : (PySID_AND_ATTRIBUTES,...)

 Sequence of PySID_AND_ATTRIBUTES tuples (attributes must be 0). Can be None.


---

<!-- page: win32security__CreateWellKnownSid_meth.html -->

## win32security.CreateWellKnownSid

 PySID = CreateWellKnownSid(WellKnownSidType, DomainSid )

Returns one of the predefined well known sids

#### Parameters

- WellKnownSidType : int

 One of the Win*Sid constants

- DomainSid=None : PySID

 Domain for the new SID, or None for local machine


---

<!-- page: win32security__CryptEnumProviders_meth.html -->

## win32security.CryptEnumProviders

 [(PyUnicode ,int),...] = CryptEnumProviders()

List cryptography providers

#### Return Value

Returns a sequence of tuples containing provider name and type


---

<!-- page: win32security__DsBind_meth.html -->

## win32security.DsBind

 PyDS_HANDLE = DsBind(DomainController, DnsDomainName )

Creates a connection to a directory service

#### Parameters

- DomainController : PyUnicode

 Name of domain controller to contact, can be None

- DnsDomainName : PyUnicode

 Dotted name of domain to bind to, can be None


---

<!-- page: win32security__DsCrackNames_meth.html -->

## win32security.DsCrackNames

 [ (status, domain, name) ] = DsCrackNames(hds, flags , formatOffered , formatDesired , names )

Converts an array of directory service object names from one format to another.

#### Parameters

- hds : PyDS_HANDLE

 Directory service handle as returned by win32security::DsBind

- flags : int

- formatOffered : int

- formatDesired : int

- names : [name, ...]


---

<!-- page: win32security__DsGetDcName_meth.html -->

## win32security.DsGetDcName

 dict = DsGetDcName(computerName, domainName , domainGUID , siteName , flags )

Returns the name of a domain controller (DC) in a specified domain. You can supply DC selection criteria to this function to indicate preference for a DC with particular characteristics.

#### Parameters

- computerName=None : PyUnicode

- domainName=None : PyUnicode

- domainGUID=None : PyIID

- siteName=None : PyUnicode

- flags=0 : int

#### Comments

 This function supports keyword arguments.


---

<!-- page: win32security__DsGetSpn_meth.html -->

## win32security.DsGetSpn

 (PyUnicode ,...) = DsGetSpn(ServiceType, ServiceClass , ServiceName , InstancePort , InstanceNames , InstancePorts )

Compose one or more service principal names to be registered using win32security::DsWriteAccountSpn

#### Parameters

- ServiceType : int

 Type of Spn to create, one of the DS_SPN_* constants

- ServiceClass : PyUnicode

 Arbitrary string that describes type of service, eg http

- ServiceName : PyUnicode

 Name of service, can be None (not required for DS_SPN_*_HOST Spn's)

- InstancePort=0 : int

 Port nbr for service instance, use 0 for no port

- InstanceNames=None : (PyUnicode ,...)

 A sequence of service instance names, can be None - not required for for host Spn's

- InstancePorts=None : (int,...)

 A sequence of extra instance ports. If specified, must be same length as InstanceNames.


---

<!-- page: win32security__DsListDomainsInSite_meth.html -->

## win32security.DsListDomainsInSite

 [ PyDS_NAME_RESULT_ITEM, ...] = DsListDomainsInSite(hds)

#### Parameters

- hds : PyDS_HANDLE

 Directory service handle as returned by win32security::DsBind


---

<!-- page: win32security__DsListInfoForServer_meth.html -->

## win32security.DsListInfoForServer

 [ PyDS_NAME_RESULT_ITEM, ...] = DsListInfoForServer(hds, server )

Lists miscellaneous information for a server.

#### Parameters

- hds : PyDS_HANDLE

 Directory service handle as returned by win32security::DsBind

- server : PyUnicode


---

<!-- page: win32security__DsListRoles_meth.html -->

## win32security.DsListRoles

 [ PyDS_NAME_RESULT_ITEM, ...] = DsListRoles(hds)

#### Parameters

- hds : PyDS_HANDLE

 Directory service handle as returned by win32security::DsBind


---

<!-- page: win32security__DsListServersInSite_meth.html -->

## win32security.DsListServersInSite

 [ PyDS_NAME_RESULT_ITEM, ...] = DsListServersInSite(hds, site )

#### Parameters

- hds : PyDS_HANDLE

 Directory service handle as returned by win32security::DsBind

- site : PyUnicode


---

<!-- page: win32security__DsListServersInSite_meth_1.html -->

## win32security.DsListServersInSite

 [ PyDS_NAME_RESULT_ITEM, ...] = DsListServersInSite(hds, domain , site )

#### Parameters

- hds : PyDS_HANDLE

 Directory service handle as returned by win32security::DsBind

- domain : PyUnicode

- site : PyUnicode


---

<!-- page: win32security__DsListServersInSite_meth_2.html -->

## win32security.DsListServersInSite

 [ PyDS_NAME_RESULT_ITEM, ...] = DsListServersInSite(hds)

#### Parameters

- hds : PyDS_HANDLE

 Directory service handle as returned by win32security::DsBind


---

<!-- page: win32security__DsUnBind_meth.html -->

## win32security.DsUnBind

 DsUnBind(hDS)

Closes a directory services handle created by win32security::DsBind

#### Parameters

- hDS : PyDS_HANDLE

 A handle to a directory service as returned by win32security::DsBind


---

<!-- page: win32security__DsWriteAccountSpn_meth.html -->

## win32security.DsWriteAccountSpn

 DsWriteAccountSpn(hDS, Operation, Account, Spns)

Associates a set of service principal names with an account

#### Parameters

- hDS : PyDS_HANDLE

 Directory service handle as returned from win32security::DsBind

- Operation : int

 Constant from DS_SPN_WRITE_OP enum

- Account : PyUnicode

 Distinguished name of account whose Spn's will be modified

- Spns : (PyUnicode ,...)

 A sequence of target Spn's as returned by win32security::DsGetSpn


---

<!-- page: win32security__DuplicateTokenEx_meth.html -->

## win32security.DuplicateTokenEx

 PyHANDLE = DuplicateTokenEx(ExistingToken, ImpersonationLevel , DesiredAccess , TokenType , TokenAttributes )

Extended version of DuplicateToken.

#### Parameters

- ExistingToken : PyHANDLE

 Logon token opened with TOKEN_DUPLICATE access

- ImpersonationLevel : int

 One of win32security.Security* values

- DesiredAccess : int

 Type of access required for the handle, combination of win32security.TOKEN_* flags

- TokenType : int

 Type of token to be created, TokenPrimary or TokenImpersonation

- TokenAttributes=None : PySECURITY_ATTRIBUTES

 Specifies security and inheritance for the new handle. None results in default DACL and no inheritance,

#### Comments

 Accepts keyword arguments


---

<!-- page: win32security__DuplicateToken_meth.html -->

## win32security.DuplicateToken

 PyHANDLE = DuplicateToken(ExistingTokenHandle, ImpersonationLevel )

Creates a copy of an access token with specified impersonation level

#### Parameters

- ExistingTokenHandle : PyHANDLE

 Handle to an access token (see win32security::LogonUser,win32security::OpenProcessToken)

- ImpersonationLevel : int

 A value from SECURITY_IMPERSONATION_LEVEL enum


---

<!-- page: win32security__EnumerateSecurityPackages_meth.html -->

## win32security.EnumerateSecurityPackages

 (dict,...) = EnumerateSecurityPackages()

List available security packages as a sequence of dictionaries representing SecPkgInfo structures


---

<!-- page: win32security__GetBinarySid_meth.html -->

## win32security.GetBinarySid

 PySID = GetBinarySid(SID)

Accepts a SID string (eg: S-1-5-32-544) and returns the SID as a PySID object.

#### Parameters

- SID : string

 Textual representation of a SID. Textual SID example: S-1-5-32-544


---

<!-- page: win32security__GetFileSecurity_meth.html -->

## win32security.GetFileSecurity

 PySECURITY_DESCRIPTOR = GetFileSecurity(filename, info )

Obtains specified information about the security of a file or directory. The information obtained is constrained by the caller's access rights and privileges.

#### Parameters

- filename : string

 The name of the file

- info=OWNER_SECURITY_INFORMATION | GROUP_SECURITY_INFORMATION | DACL_SECURITY_INFORMATION | SACL_SECURITY_INFORMATION : int

 Flags that specify the information requested.

#### Comments

 This function reportedly will not return the INHERITED_ACE flag on some Windows XP SP1 systems Use GetNamedSecurityInfo if you encounter this problem.


---

<!-- page: win32security__GetKernelObjectSecurity_meth.html -->

## win32security.GetKernelObjectSecurity

 PySECURITY_DESCRIPTOR = GetKernelObjectSecurity(handle, info )

Obtains specified information about the security of a kernel object. The information obtained is constrained by the caller's access rights and privileges.

#### Parameters

- handle : PyHANDLE

 The handle to the object

- info=OWNER_SECURITY_INFORMATION | GROUP_SECURITY_INFORMATION | DACL_SECURITY_INFORMATION | SACL_SECURITY_INFORMATION : int

 Flags that specify the information requested.


---

<!-- page: win32security__GetNamedSecurityInfo_meth.html -->

## win32security.GetNamedSecurityInfo

 PySECURITY_DESCRIPTOR = GetNamedSecurityInfo(ObjectName, ObjectType , SecurityInfo )

Retrieve security info for an object by name

#### Parameters

- ObjectName : str/unicode

 Name of object

- ObjectType : int

 Value from SE_OBJECT_TYPE enum

- SecurityInfo : int

 Combination of SECURITY_INFORMATION constants

#### Comments

 Separate owner, group, dacl, and sacl are not returned as they can be easily retrieved from the returned PySECURITY_DESCRIPTOR


---

<!-- page: win32security__GetSecurityInfo_meth.html -->

## win32security.GetSecurityInfo

 PySECURITY_DESCRIPTOR = GetSecurityInfo(handle, ObjectType , SecurityInfo )

Retrieve security info for an object by handle

#### Parameters

- handle : int/PyHANDLE

 Handle to object

- ObjectType : int

 Value from SE_OBJECT_TYPE enum

- SecurityInfo : int

 Combination of SECURITY_INFORMATION constants

#### Comments

 Separate owner, group, dacl, and sacl are not returned as they can be easily retrieved from the returned PySECURITY_DESCRIPTOR


---

<!-- page: win32security__GetTokenInformation_meth.html -->

## win32security.GetTokenInformation

 object = GetTokenInformation(TokenHandle, TokenInformationClass )

Retrieves a specified type of information about an access token. The calling process must have appropriate access rights to obtain the information.

#### Parameters

- TokenHandle : PyHANDLE

 Handle to an access token.

- TokenInformationClass : int

 Specifies a value from the TOKEN_INFORMATION_CLASS enumerated type identifying the type of information the function retrieves.

#### Return Value

The following types are supported

| | TokenInformationClass | Return type
| |

---

 |

---

| | TokenSessionId | int - Terminal Services session id
| | TokenSandBoxInert | Boolean
| | TokenType | Value from TOKEN_TYPE enum (TokenPrimary,TokenImpersonation)
| | TokenImpersonationLevel | Value from SECURITY_IMPERSONATION_LEVEL enum
| | TokenVirtualizationEnabled | Boolean
| | TokenVirtualizationAllowed | Boolean
| | TokenHasRestrictions | Boolean
| | TokenElevationType | int - TokenElevation* value indicating what type of token is linked to
| | TokenUIAccess | Boolean
| | TokenUser | (PySID,int)
| | TokenOwner | PySID
| | TokenGroups | ((PySID,int),) returns a list of tuples containing (group Sid, attribute flags)
| | TokenRestrictedSids | ((PySID,int),)
| | TokenPrivileges | ((int,int),) returns PyTOKEN_PRIVILEGES (tuple of LUID and attribute flags for each privilege) attributes are combination of SE_PRIVILEGE_ENABLED,SE_PRIVILEGE_ENABLED_BY_DEFAULT,SE_PRIVILEGE_USED_FOR_ACCESS
| | TokenPrimaryGroup | PySID
| | TokenSource | (string,LUID)
| | TokenDefaultDacl | PyACL
| | TokenStatistics | dict Returns a dictionary representing a TOKEN_STATISTICS structure
| | TokenOrigin | LUID identifying the logon session
| | TokenLinkedToken | PyHANDLE - Returns handle to the access token to which token is linked
| | TokenLogonSid | PySID
| | TokenElevation | Boolean
| | TokenIntegrityLevel | (PySID, int)
| | TokenMandatoryPolicy | int (TOKEN_MANDATORY_POLICY_* flag)


---

<!-- page: win32security__GetUserObjectSecurity_meth.html -->

## win32security.GetUserObjectSecurity

 PySECURITY_DESCRIPTOR = GetUserObjectSecurity(handle, info )

Obtains specified information about the security of a user object. The information obtained is constrained by the caller's access rights and privileges.

#### Parameters

- handle : PyHANDLE

 The handle to the object

- info=OWNER_SECURITY_INFORMATION | GROUP_SECURITY_INFORMATION | DACL_SECURITY_INFORMATION | SACL_SECURITY_INFORMATION : int

 Flags that specify the information requested.


---

<!-- page: win32security__ImpersonateAnonymousToken_meth.html -->

## win32security.ImpersonateAnonymousToken

 ImpersonateAnonymousToken(ThreadHandle)

Cause a thread to act in the security context of an anonymous token

#### Parameters

- ThreadHandle : PyHANDLE

 Handle to thread that will


---

<!-- page: win32security__ImpersonateLoggedOnUser_meth.html -->

## win32security.ImpersonateLoggedOnUser

 ImpersonateLoggedOnUser(handle)

Impersonates a logged on user.

#### Parameters

- handle : PyHANDLE

 Handle to a token that represents a logged-on user


---

<!-- page: win32security__ImpersonateNamedPipeClient_meth.html -->

## win32security.ImpersonateNamedPipeClient

 ImpersonateNamedPipeClient(handle)

Impersonates a named-pipe client application.

#### Parameters

- handle : int

 handle of a named pipe.


---

<!-- page: win32security__ImpersonateSelf_meth.html -->

## win32security.ImpersonateSelf

 ImpersonateSelf(ImpersonationLevel)

Assigns an impersonation token for current security context to current process

#### Parameters

- ImpersonationLevel : int

 A value from SECURITY_IMPERSONATION_LEVEL enum


---

<!-- page: win32security__InitializeSecurityContext_meth.html -->

## win32security.InitializeSecurityContext

 (int, int, PyDateTime) = InitializeSecurityContext(Credential, Context , TargetName , ContextReq , TargetDataRep , pInput , NewContext , pOutput )

Creates a security context based on credentials created by AcquireCredentialsHandle

#### Parameters

- Credential : PyCredHandle

 A credentials handle as returned by win32security::AcquireCredentialsHandle

- Context : PyCtxtHandle

 Use None on initial call, then handle returned in NewContext thereafter

- TargetName : str/unicode

 Target of context, security package specific - Use None with NTLM

- ContextReq : int

 Combination of ISC_REQ_* flags

- TargetDataRep : int

 One of SECURITY_NATIVE_DREP,SECURITY_NETWORK_DREP

- pInput : PySecBufferDesc

 Data buffer - use None initially

- NewContext : PyCtxtHandle

 Uninitialized context handle to receive output

- pOutput : PySecBufferDesc

 Buffer that receives output data for subsequent calls

#### Return Value

Return value is a tuple of (return code, attribute flags, expiration time)


---

<!-- page: win32security__IsTokenRestricted_meth.html -->

## win32security.IsTokenRestricted

 bool = IsTokenRestricted(TokenHandle)

Checks if a token contains restricted sids

#### Parameters

- TokenHandle : PyHANDLE

 Handle to an access token


---

<!-- page: win32security__LogonUserEx_meth.html -->

## win32security.LogonUserEx

 (PyHANDLE, PySID, str, dict) = LogonUserEx(Username, Domain , Password , LogonType , LogonProvider )

Log a user onto the local machine,

#### Parameters

- Username : PyUnicode

 User account, may be specified as a UPN (user@domain.com). This may also be a marshalled credential (see win32cred::CredMarshalCredential).

- Domain : PyUnicode

 User's domain. Can be None if Username is a full UPN.

- Password : PyUnicode

 User's password. Use a blank string if Username contains a marshalled credential.

- LogonType : int

 One of LOGON32_LOGON_* values

- LogonProvider : int

 One of LOGON32_PROVIDER_* values

#### Comments

 Accepts keyword args

#### Return Value

Returns access token, logon sid, profile buffer, and process quotas. Format of the profile buffer is not known, so returned object is subject to change.


---

<!-- page: win32security__LogonUser_meth.html -->

## win32security.LogonUser

 PyHANDLE = LogonUser(Username, Domain , Password , LogonType , LogonProvider )

Attempts to log a user on to the local computer, that is, to the computer from which LogonUser was called. You cannot use LogonUser to log on to a remote computer.

#### Parameters

- Username : PyUnicode

 The name of the user account to log on to. This may also be a marshalled credential (see win32cred::CredMarshalCredential).

- Domain : PyUnicode

 The name of the domain, or None for the current domain

- Password : PyUnicode

 User's password. Use a blank string if Username contains a marshalled credential.

- LogonType : int

 One of LOGON32_LOGON_* values

- LogonProvider : int

 One of LOGON32_PROVIDER_* values

#### Comments

 Accepts keyword args


---

<!-- page: win32security__LookupAccountName_meth.html -->

## win32security.LookupAccountName

 PySID, string, int = LookupAccountName(systemName, accountName )

Accepts the name of a system and an account as input. It retrieves a security identifier (SID) for the account and the name of the domain on which the account was found.

#### Parameters

- systemName : string

 The system name, or None

- accountName : string

 The account name

#### Return Value

The result is a tuple of new SID object, the domain name where the account was found, and the type of account the SID is for.


---

<!-- page: win32security__LookupAccountSid_meth.html -->

## win32security.LookupAccountSid

 string, string, int = LookupAccountSid(systemName, sid )

Accepts a security identifier (SID) as input. It retrieves the name of the account for this SID and the name of the first domain on which this SID is found.

#### Parameters

- systemName : string

 The system name, or None

- sid : PySID

 The SID

#### Return Value

The result is a tuple of the name, the domain name where the account was found, and the type of account the SID is for.


---

<!-- page: win32security__LookupPrivilegeDisplayName_meth.html -->

## win32security.LookupPrivilegeDisplayName

 PyUnicode = LookupPrivilegeDisplayName(SystemName, Name )

Returns long description for a privilege name

#### Parameters

- SystemName : string/PyUnicode

 System name, local system assumed if not specified

- Name : string/PyUnicode

 Name of privilege, Se...Privilege string constants (win32security.SE_*_NAME)


---

<!-- page: win32security__LookupPrivilegeName_meth.html -->

## win32security.LookupPrivilegeName

 PyUnicode = LookupPrivilegeName(SystemName, luid )

return the text name for a privilege LUID

#### Parameters

- SystemName : string/PyUnicode

 System name, local system assumed if not specified

- luid : LARGE_INTEGER

 64 bit value representing a privilege


---

<!-- page: win32security__LookupPrivilegeValue_meth.html -->

## win32security.LookupPrivilegeValue

 LARGE_INTEGER = LookupPrivilegeValue(systemName, privilegeName )

Retrieves the locally unique id for a privilege name

#### Parameters

- systemName : string

 String specifying the system, use None for local machine

- privilegeName : string

 String specifying the privilege (win32security.SE_*_NAME)


---

<!-- page: win32security__LsaAddAccountRights_meth.html -->

## win32security.LsaAddAccountRights

 LsaAddAccountRights(PolicyHandle, AccountSid, UserRights)

Adds a list of privileges to an account

#### Parameters

- PolicyHandle : PyLSA_HANDLE

 An LSA policy handle as returned by win32security::LsaOpenPolicy

- AccountSid : PySID

 Account to which privs will be added

- UserRights : (str/unicode,...)

 Sequence of privilege names (SE_*_NAME unicode constants)

#### Comments

 Account is created if it doesn't already exist.

 Accepts keyword args.


---

<!-- page: win32security__LsaCallAuthenticationPackage_meth.html -->

## win32security.LsaCallAuthenticationPackage

 LsaCallAuthenticationPackage(LsaHandle, AuthenticationPackage, MessageType, ProtocolSubmitBuffer)

Requests the services of an authentication package

#### Parameters

- LsaHandle : PyLsaLogon_HANDLE

 Lsa handle as returned by win32security::LsaRegisterLogonProcess or win32security::LsaConnectUntrusted

- AuthenticationPackage : int

 Id of authentication package to call, as returned by win32security::LsaLookupAuthenticationPackage

- MessageType : int

 Type of request that is being made, Kerb*Message or MsV1_0* constant

- ProtocolSubmitBuffer : object

 Type is dependent on MessageType

#### Comments

 Message type is embedded in different types of submit buffers in the API call, but passed separately from python for simplicity of parsing input

| | MessageType | Input type
| |

---

 |

---

| | KerbQueryTicketCacheMessage | long - a logon id, use 0 for current logon session
| | KerbRetrieveTicketMessage | long - a logon id, use 0 for current logon session
| | KerbPurgeTicketCacheMessage | (long, PyUnicode , PyUnicode ) - tuple containing (LogonId, ServerName, RealmName)
| | KerbRetrieveEncodedTicketMessage | (LogonId, TargetName, TicketFlags, CacheOptions, EncryptionType, CredentialsHandle) (int, PyUnicode , int, int, int, PyCredHandle)

| | MessageType | Return type
| |

---

 |

---

| | KerbQueryTicketCacheMessage | (dict,...) - Returns all tickets for the specified logon session (form is KERB_TICKET_CACHE_INFO)
| | KerbPurgeTicketCacheMessage | None
| | KerbRetrieveTicketMessage | Returns the ticket granting ticket for the logon session as a KERB_EXTERNAL_TICKET
| | KerbRetrieveEncodedTicketMessage | Returns specified ticket as a KERB_EXTERNAL_TICKET

#### Return Value

Type of returned object is dependent on MessageType


---

<!-- page: win32security__LsaClose_meth.html -->

## win32security.LsaClose

 LsaClose(PolicyHandle)

Closes a policy handle created by win32security::LsaOpenPolicy

#### Parameters

- PolicyHandle : PyHANDLE

 An LSA policy handle as returned by win32security::LsaOpenPolicy


---

<!-- page: win32security__LsaConnectUntrusted_meth.html -->

## win32security.LsaConnectUntrusted

 PyLsaLogon_HANDLE = LsaConnectUntrusted()

Creates untrusted connection to LSA

#### Comments

 You don't need SeTcbPrivilege to execute this function as you do with LsaRegisterLogonProcess, but functionality of handle is limited


---

<!-- page: win32security__LsaDeregisterLogonProcess_meth.html -->

## win32security.LsaDeregisterLogonProcess

 LsaDeregisterLogonProcess(LsaHandle)

Closes connection to LSA server

#### Parameters

- LsaHandle : PyLsaLogon_HANDLE

 An Lsa handle as returned by win32security::LsaConnectUntrusted or win32security::LsaRegisterLogonProcess


---

<!-- page: win32security__LsaEnumerateAccountRights_meth.html -->

## win32security.LsaEnumerateAccountRights

 [PyUnicode , ...] = LsaEnumerateAccountRights(PolicyHandle, AccountSid )

Lists privileges held by SID

#### Parameters

- PolicyHandle : PyLSA_HANDLE

 An LSA policy handle as returned by win32security::LsaOpenPolicy

- AccountSid : PySID

 Security identifier of account for which to list privs


---

<!-- page: win32security__LsaEnumerateAccountsWithUserRight_meth.html -->

## win32security.LsaEnumerateAccountsWithUserRight

 (PySID,...) = LsaEnumerateAccountsWithUserRight(PolicyHandle, UserRight )

Return SIDs that hold specified priv

#### Parameters

- PolicyHandle : PyLSA_HANDLE

 An LSA policy handle as returned by win32security::LsaOpenPolicy

- UserRight : str/unicode

 Name of privilege (SE_*_NAME unicode constant)


---

<!-- page: win32security__LsaEnumerateLogonSessions_meth.html -->

## win32security.LsaEnumerateLogonSessions

 (long,...) = LsaEnumerateLogonSessions()

Lists all current logon ids


---

<!-- page: win32security__LsaGetLogonSessionData_meth.html -->

## win32security.LsaGetLogonSessionData

 (dict,...) = LsaGetLogonSessionData(LogonId)

Returns information about a logon session

#### Parameters

- LogonId : PyLARGE_INTEGER

 An LUID identifying a logon session

#### Return Value

Returns a dictionary representing a SECURITY_LOGON_SESSION_DATA structure


---

<!-- page: win32security__LsaLookupAuthenticationPackage_meth.html -->

## win32security.LsaLookupAuthenticationPackage

 int = LsaLookupAuthenticationPackage(LsaHandle, PackageName )

Retrieves the unique id for an authentication package

#### Parameters

- LsaHandle : PyLsaLogon_HANDLE

 An Lsa handle as returned by win32security::LsaConnectUntrusted or win32security::LsaRegisterLogonProcess

- PackageName : string

 Name of security package to be identified


---

<!-- page: win32security__LsaOpenPolicy_meth.html -->

## win32security.LsaOpenPolicy

 PyLSA_HANDLE = LsaOpenPolicy(system_name, access_mask )

Opens a policy handle for the specified system

#### Parameters

- system_name : string/PyUnicode

 System name, local system assumed if not specified

- access_mask : int

 Bitmask of requested access types


---

<!-- page: win32security__LsaQueryInformationPolicy_meth.html -->

## win32security.LsaQueryInformationPolicy

 LsaQueryInformationPolicy(PolicyHandle, InformationClass)

Retrieves information from the policy handle

#### Parameters

- PolicyHandle : PyLSA_HANDLE

 An LSA policy handle as returned by win32security::LsaOpenPolicy

- InformationClass : int

 POLICY_INFORMATION_CLASS value

| | POLICY_INFORMATION_CLASS value | Return type
| |

---

 |

---

| | PolicyAuditEventsInformation | returns tuple of (boolean,(int,...)) Tuple consists of a boolean indicating if auditing is enabled, and a tuple of ints, indexed by POLICY_AUDIT_EVENT_TYPE values, containing a combination of POLICY_AUDIT_EVENT_UNCHANGED, POLICY_AUDIT_EVENT_SUCCESS, POLICY_AUDIT_EVENT_FAILURE, POLICY_AUDIT_EVENT_NONE
| | PolicyDnsDomainInformation | Returns a tuple representing a POLICY_DNS_DOMAIN_INFO struct
| | PolicyPrimaryDomainInformation | Returns name and SID of primary domain
| | PolicyAccountDomainInformation | Returns name and SID of account domain
| | PolicyLsaServerRoleInformation | Returns an int, one of PolicyServerRoleBackup, PolicyServerRolePrimary
| | PolicyModificationInformation | Returns modification serial nbr and modified time of Lsa database


---

<!-- page: win32security__LsaRegisterLogonProcess_meth.html -->

## win32security.LsaRegisterLogonProcess

 PyLsaLogon_HANDLE = LsaRegisterLogonProcess(LogonProcessName)

Creates a trusted connection to LSA

#### Parameters

- LogonProcessName : string

 Name to use for this logon process

#### Comments

 Requires SeTcbPrivilege (and must be enabled)


---

<!-- page: win32security__LsaRegisterPolicyChangeNotification_meth.html -->

## win32security.LsaRegisterPolicyChangeNotification

 LsaRegisterPolicyChangeNotification(InformationClass, NotificationEventHandle)

Register an event handle to receive policy change events

#### Parameters

- InformationClass : int

 One of POLICY_NOTIFICATION_INFORMATION_CLASS contants

- NotificationEventHandle : PyHANDLE

 Event handle to receives notification


---

<!-- page: win32security__LsaRemoveAccountRights_meth.html -->

## win32security.LsaRemoveAccountRights

 LsaRemoveAccountRights(PolicyHandle, AccountSid, AllRights, UserRights)

Removes privs from an account

#### Parameters

- PolicyHandle : PyLSA_HANDLE

 An LSA policy handle as returned by win32security::LsaOpenPolicy

- AccountSid : PySID

 Account whose privileges will be removed

- AllRights : int

 Boolean value indicating if all privs should be removed from account

- UserRights : (str/unicode,...)

 List of privilege names to be removed (SE_*_NAME unicode constants)

#### Comments

 If AllRights parm is true, account is *deleted*

 Accepts keyword args.


---

<!-- page: win32security__LsaRetrievePrivateData_meth.html -->

## win32security.LsaRetrievePrivateData

 PyUnicode = LsaRetrievePrivateData(PolicyHandle, KeyName )

Retreives encrypted unicode data from Lsa registry key.

#### Parameters

- PolicyHandle : PyLSA_HANDLE

 An LSA policy handle as returned by win32security::LsaOpenPolicy

- KeyName : string

 Registry key to read


---

<!-- page: win32security__LsaSetInformationPolicy_meth.html -->

## win32security.LsaSetInformationPolicy

 LsaSetInformationPolicy(PolicyHandle, InformationClass, Information)

Sets policy options

#### Parameters

- PolicyHandle : PyLSA_HANDLE

 An LSA policy handle as returned by win32security::LsaOpenPolicy

- InformationClass : int

 POLICY_INFORMATION_CLASS value

- Information : object

 Type is dependent on InformationClass

| | InformationClass | Type of input expected
| |

---

 |

---

| | PolicyAuditEventsInformation | (boolean, (int, ...))
First member imdicates whether auditing is enabled or not.
Seconed member is a sequence of POLICY_AUDIT_EVENT_* flags specifying which events should be audited. See AuditCategory* values for positions of each event type.


---

<!-- page: win32security__LsaStorePrivateData_meth.html -->

## win32security.LsaStorePrivateData

 LsaStorePrivateData(PolicyHandle, KeyName, PrivateData)

Stores encrypted unicode data under specified Lsa registry key. Returns None on success

#### Parameters

- PolicyHandle : PyLSA_HANDLE

 An LSA policy handle as returned by win32security::LsaOpenPolicy

- KeyName : string

 Registry key in which to store data

- PrivateData : PyUNICODE

 Unicode string to be encrypted and stored


---

<!-- page: win32security__LsaUnregisterPolicyChangeNotification_meth.html -->

## win32security.LsaUnregisterPolicyChangeNotification

 LsaUnregisterPolicyChangeNotification(InformationClass, NotificationEventHandle)

Stop receiving policy change notification

#### Parameters

- InformationClass : int

 POLICY_NOTIFICATION_INFORMATION_CLASS constant

- NotificationEventHandle : PyHANDLE

 Event handle previously registered to receive policy change events


---

<!-- page: win32security__MapGenericMask_meth.html -->

## win32security.MapGenericMask

 int = MapGenericMask(AccessMask, GenericMapping )

Translates generic access rights into specific rights

#### Parameters

- AccessMask : int

 A bitmask of generic rights to be interpreted according to GenericMapping

- GenericMapping : (int,int,int,int)

 A tuple of 4 bitmasks (GenericRead, GenericWrite, GenericExecute, GenericAll) containing the standard and specific rights that correspond to the generic rights.

#### Return Value

The input AccessMask will be returned with any generic access rights translated into specific equivalents


---

<!-- page: win32security__OpenProcessToken_meth.html -->

## win32security.OpenProcessToken

 PyHANDLE = OpenProcessToken(processHandle, desiredAccess )

Opens the access token associated with a process.

#### Parameters

- processHandle : int

 The handle of the process to open.

- desiredAccess : int

 Desired access to process


---

<!-- page: win32security__OpenThreadToken_meth.html -->

## win32security.OpenThreadToken

 PyHandle = OpenThreadToken(handle, desiredAccess , openAsSelf )

Opens the access token associated with a thread.

#### Parameters

- handle : PyHANDLE

 handle to thread

- desiredAccess : int

 access to process

- openAsSelf : int

 Flag for process or thread security


---

<!-- page: win32security__QuerySecurityPackageInfo_meth.html -->

## win32security.QuerySecurityPackageInfo

 dict = QuerySecurityPackageInfo(PackageName)

Retrieves parameters for a security package

#### Parameters

- PackageName : PyUNICODE

 Name of the security package to query

#### Return Value

Returns a dictionary representing a SecPkgInfo struct


---

<!-- page: win32security__RevertToSelf_meth.html -->

## win32security.RevertToSelf

 RevertToSelf()

Terminates the impersonation of a client application.


---

<!-- page: win32security__SECURITY_ATTRIBUTES_meth.html -->

## win32security.SECURITY_ATTRIBUTES

 PySECURITY_ATTRIBUTES = SECURITY_ATTRIBUTES()

Creates a new PySECURITY_ATTRIBUTES object.


---

<!-- page: win32security__SECURITY_DESCRIPTOR_meth.html -->

## win32security.SECURITY_DESCRIPTOR

 PySECURITY_DESCRIPTOR = SECURITY_DESCRIPTOR()

Creates a new PySECURITY_DESCRIPTOR object.


---

<!-- page: win32security__SID_meth.html -->

## win32security.SID

 PySID = SID()

Creates a new PySID object.


---

<!-- page: win32security__SetFileSecurity_meth.html -->

## win32security.SetFileSecurity

 SetFileSecurity(filename, info, security)

Sets information about the security of a file or directory. The information obtained is constrained by the caller's access rights and privileges.

#### Parameters

- filename : string

 The name of the file

- info : int

 The type of information to set.

- security : PySECURITY_DESCRIPTOR

 The security information


---

<!-- page: win32security__SetKernelObjectSecurity_meth.html -->

## win32security.SetKernelObjectSecurity

 SetKernelObjectSecurity(handle, info, security)

Sets information about the security of a kernel object. The information obtained is constrained by the caller's access rights and privileges.

#### Parameters

- handle : PyHANDLE

 The handle to an object for which security information will be set.

- info : int

 The type of information to set - combination of SECURITY_INFORMATION values

- security : PySECURITY_DESCRIPTOR

 The security information


---

<!-- page: win32security__SetNamedSecurityInfo_meth.html -->

## win32security.SetNamedSecurityInfo

 SetNamedSecurityInfo(ObjectName, ObjectType, SecurityInfo, Owner, Group, Dacl, Sacl)

Sets security info for an object by name

#### Parameters

- ObjectName : str/unicode

 Name of object

- ObjectType : int

 Value from SE_OBJECT_TYPE enum

- SecurityInfo : int

 Combination of SECURITY_INFORMATION constants

- Owner : PySID

 Sid to set as owner of object, can be None

- Group : PySID

 Group Sid, can be None

- Dacl : PyACL

 Discretionary ACL to set for object, can be None

- Sacl : PyACL

 System Audit ACL to set for object, can be None


---

<!-- page: win32security__SetSecurityInfo_meth.html -->

## win32security.SetSecurityInfo

 SetSecurityInfo(handle, ObjectType, SecurityInfo, Owner, Group, Dacl, Sacl)

Sets security info for an object by handle

#### Parameters

- handle : int/PyHANDLE

 Handle to object

- ObjectType : int

 Value from SE_OBJECT_TYPE enum

- SecurityInfo : int

 Combination of SECURITY_INFORMATION constants

- Owner : PySID

 Sid to set as owner of object, can be None

- Group : PySID

 Group Sid, can be None

- Dacl : PyACL

 Discretionary ACL to set for object, can be None

- Sacl : PyACL

 System Audit ACL to set for object, can be None


---

<!-- page: win32security__SetThreadToken_meth.html -->

## win32security.SetThreadToken

 SetThreadToken(Thread, Token)

Assigns an impersonation token to a thread. The function can also cause a thread to stop using an impersonation token.

#### Parameters

- Thread : PyHANDLE

 Handle to a thread. Use None to indicate calling thread.

- Token : PyHANDLE

 Handle to an impersonation token. Use None to end impersonation.


---

<!-- page: win32security__SetTokenInformation_meth.html -->

## win32security.SetTokenInformation

 SetTokenInformation(TokenHandle, TokenInformationClass, TokenInformation)

Set a specified type of information in an access token

#### Parameters

- TokenHandle : PyHANDLE

 Handle to an access token to be modified

- TokenInformationClass : int

 Specifies a value from the TOKEN_INFORMATION_CLASS enumerated type identifying the type of information to be modfied

- TokenInformation : object

 Type is dependent on TokenInformationClass

| | TokenInformationClass | Type of input expected
| |

---

 |

---

| | TokenOwner | PySID to be used as owner of created objects
| | TokenPrimaryGroup | PySID
| | TokenDefaultDacl | PyACL - Default permissions for created objects
| | TokenSessionId | Int - Terminal services session id
| | TokenVirtualizationEnabled | Boolean
| | TokenVirtualizationAllowed | Boolean
| | TokenIntegrityLevel | PySID_AND_ATTRIBUTES containing an integrity SID and SE_GROUP_INTEGRITY flag
| | TokenMandatoryPolicy | Int. one of TOKEN_MANDATORY_POLICY_* values


---

<!-- page: win32security__SetUserObjectSecurity_meth.html -->

## win32security.SetUserObjectSecurity

 SetUserObjectSecurity(handle, info, security)

Sets information about the security of a user object. The information obtained is constrained by the caller's access rights and privileges.

#### Parameters

- handle : PyHANDLE

 The handle to an object for which security information will be set.

- info : int

 The type of information to set - combination of SECURITY_INFORMATION values

- security : PySECURITY_DESCRIPTOR

 The security information


---

<!-- page: win32security__TranslateName_meth.html -->

## win32security.TranslateName

 PyUnicode = TranslateName(accountName, accountNameFormat , accountNameFormat , numChars )

Converts a directory service object name from one format to another.

#### Parameters

- accountName : PyUnicode

 object name

- accountNameFormat : int

 A value from the EXTENDED_NAME_FORMAT enumeration type indicating the format of the accountName name.

- accountNameFormat : int

 A value from the EXTENDED_NAME_FORMAT enumeration type indicating the format of the desired name.

- numChars=1024 : int

 Number of Unicode characters to allocate for the return buffer.
