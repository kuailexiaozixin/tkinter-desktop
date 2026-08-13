# 模块 win32cred

> 来源：https://mhammond.github.io/pywin32/win32cred.html （及其成员页，已全部内联）

## Module win32cred

 Interface to credentials management functions. Functions operate only on the credential set of the calling user.
 User's profile must be loaded for stored credentials to be accessible.
 Each credential is uniquely identified by its TargetName and Type.
 All functions accept keyword arguments.

#### Methods

- CredMarshalCredential

 Marshals a credential into a unicode string

- CredUnmarshalCredential

 Unmarshals credentials formatted using win32cred::CredMarshalCredential

- CredIsMarshaledCredential

 Checks if a string matches the form of a marshaled credential

- CredEnumerate

 Lists stored credentials for current logon session

- CredGetTargetInfo

 Determines type and location of credential target

- CredWriteDomainCredentials

 Creates or updates credential for a domain or server

- CredReadDomainCredentials

 Retrieves a user's credentials for a domain or server

- CredDelete

 Deletes a stored credential

- CredWrite

 Creates or updates a stored credential

- CredRead

 Retrieves a stored credential

- CredRename

 Changes the target name of stored credentials

- CredUICmdLinePromptForCredentials

 Prompt for username/passwd from a console app

- CredUIPromptForCredentials

 Initiates dialog to request user credentials

- CredUIConfirmCredentials

 Confirms whether credentials entered by user are valid or not

- CredUIReadSSOCredW

 Retrieves single sign on username

- CredUIStoreSSOCredW

 Creates a single sign on credential

- CredUIParseUserName

 Parses a full username into domain and username


---

# win32cred 成员详细文档（共 18 项）


---

<!-- page: win32cred__CredDelete_meth.html -->

## win32cred.CredDelete

 CredDelete(TargetName, Type, Flags, Target)

Deletes a stored credential

#### Parameters

- TargetName : PyUnicode

 Target of credential to be deleted

- Type : int

 One of the CRED_TYPE_* values

- Flags=0 : int

 Reserved, use only 0

- Target : dict

 Credential to be deleted


---

<!-- page: win32cred__CredEnumerate_meth.html -->

## win32cred.CredEnumerate

 (dict,...) = CredEnumerate(Filter, Flags )

Lists credentials for current logon session

#### Parameters

- Filter=None : PyUnicode

 Matches credentials' target names by prefix, can be None

- Flags=0 : int

 Reserved, use 0 if passed in

#### Return Value

Returns a sequence of PyCREDENTIAL dictionaries


---

<!-- page: win32cred__CredGetSessionTypes_meth.html -->

## win32cred.CredGetSessionTypes

 dict = CredGetSessionTypes(MaximumPersistCount)

Returns maximum persistence supported by the current logon session

#### Parameters

- MaximumPersistCount=CRED_TYPE_MAXIMUM : int

 Maximum array entries

#### Return Value

Returns an integer list


---

<!-- page: win32cred__CredGetTargetInfo_meth.html -->

## win32cred.CredGetTargetInfo

 dict = CredGetTargetInfo(TargetName, Flags )

Determines type and location of credential target

#### Parameters

- TargetName : PyUnicode

 Name of server that is target of stored credentials

- Flags=0 : int

 CRED_ALLOW_NAME_RESOLUTION, or 0

#### Comments

 The target information will not be available until an attempt is made to authenticate against it

#### Return Value

Returns a PyCREDENTIAL_TARGET_INFORMATION dict


---

<!-- page: win32cred__CredIsMarshaledCredential_meth.html -->

## win32cred.CredIsMarshaledCredential

 boolean = CredIsMarshaledCredential(MarshaledCredential)

Checks if a string matches the form of a marshaled credential

#### Parameters

- MarshaledCredential : PyUnicode

 Marshaled credential as returned by win32cred::CredMarshalCredential


---

<!-- page: win32cred__CredMarshalCredential_meth.html -->

## win32cred.CredMarshalCredential

 PyUnicode = CredMarshalCredential(CredType, Credential )

Marshals a credential into a unicode string

#### Parameters

- CredType : int

 CertCredential or UsernameTargetCredential

- Credential : str/PyUnicode

 The credential to be marshalled. Type is dependent on CredType.

| | CredType | Type of Credential
| |

---

 |

---

| | CertCredential | String containing the SHA1 hash of user's certificate
| | UsernameTargetCredential | Unicode string containing a username for which credentials exist in current logon session

#### Comments

 Credentials with Flags that contain CRED_FLAGS_USERNAME_TARGET can be marshalled to be passed as the username to functions that normally require a username/password combination, such as win32security::LogonUser and win32net::NetUseAdd


---

<!-- page: win32cred__CredReadDomainCredentials_meth.html -->

## win32cred.CredReadDomainCredentials

 (dict,...) = CredReadDomainCredentials(TargetInfo, Flags )

Retrieves credentials for a domain or server

#### Parameters

- TargetInfo : dict

 PyCREDENTIAL_TARGET_INFORMATION identifying a domain or server. At least one of the Names is required.

- Flags=0 : int

 CRED_CACHE_TARGET_INFORMATION is only valid flag

#### Return Value

Returns a sequence of PyCREDENTIAL dicts


---

<!-- page: win32cred__CredRead_meth.html -->

## win32cred.CredRead

 dict = CredRead(TargetName, Type , Flags )

Retrieves a stored credential

#### Parameters

- TargetName : PyUnicode

 The target of the credentials to retrieve

- Type : int

 One of the CRED_TYPE_* constants

- Flags=0 : int

 Reserved, use 0

#### Return Value

Returns a PyCREDENTIAL dict


---

<!-- page: win32cred__CredRename_meth.html -->

## win32cred.CredRename

 dict = CredRename(OldTargetName, NewTargetName , Type , Flags )

Changes the target name of stored credentials

#### Parameters

- OldTargetName : PyUnicode

 The target of credential to be renamed

- NewTargetName : PyUnicode

 New target for the specified credential

- Type : int

 Type of the credential to be renamed (CRED_TYPE_*)

- Flags=0 : int

 Reserved, use only 0

#### Comments

 CRED_FLAGS_USERNAME_TARGET credentials can't be renamed since their TargetName and Username must be equal


---

<!-- page: win32cred__CredUICmdLinePromptForCredentials_meth.html -->

## win32cred.CredUICmdLinePromptForCredentials

 (PyUnicode , PyUnicode , boolean) = CredUICmdLinePromptForCredentials(TargetName, AuthError , UserName , Password , Save , Flags )

Prompt for username/passwd from a console app

#### Parameters

- TargetName : PyUnicode

 Server or domain against which to authenticate

- AuthError=0 : int

 Error code indicating why credentials are required, can be 0

- UserName=None : PyUnicode

 Default username, can be None. At most CREDUI_MAX_USERNAME_LENGTH chars

- Password=None : PyUnicode

 Password, can be None. At most CREDUI_MAX_PASSWORD_LENGTH chars

- Save=True : boolean

 Specifies default value for Save prompt

- Flags=CREDUI_FLAGS_EXCLUDE_CERTIFICATES : int

 Combination of CREDUI_FLAGS_* values

#### Comments

 The command-line version of this function does not accept certificates, so Flags must contain CREDUI_FLAGS_EXCLUDE_CERTIFICATES or CREDUI_FLAGS_REQUIRE_SMARTCARD

#### Return Value

Returns the username and password entered, and a boolean indicating if credential was saved


---

<!-- page: win32cred__CredUIConfirmCredentials_meth.html -->

## win32cred.CredUIConfirmCredentials

 CredUIConfirmCredentials(TargetName, Confirm)

Confirms whether credentials entered by user are valid or not

#### Parameters

- TargetName : PyUnicode

 Target of credentials that are pending confirmation

- Confirm : boolean

 Indicates if authentication succeeded

#### Comments

 This function should be called to confirm credentials entered via win32cred::CredUICmdLinePromptForCredentials or win32cred::CredUIPromptForCredentials if CREDUI_FLAGS_EXPECT_CONFIRMATION was passed in Flags to either function.
 Sequence of operations:
 Prompt for credentials
 Authenticate against target using credentials
 Call this function to indicate if authentication succeeded or not


---

<!-- page: win32cred__CredUIParseUserName_meth.html -->

## win32cred.CredUIParseUserName

 (PyUnicode , PyUnicode ) = CredUIParseUserName(UserName)

Parses a full username into domain and username

#### Parameters

- UserName : PyUnicode

 Username as returned by win32cred::CredUIPromptForCredentials

#### Return Value

Returns the username and domain


---

<!-- page: win32cred__CredUIPromptForCredentials_meth.html -->

## win32cred.CredUIPromptForCredentials

 (PyUnicode , PyUnicode , boolean) = CredUIPromptForCredentials(TargetName, AuthError , UserName , Password , Save , Flags , UiInfo )

Initiates dialog to request user credentials

#### Parameters

- TargetName : PyUnicode

 Server or domain against which to authenticate

- AuthError=0 : int

 Error code indicating why credentials are required, can be 0

- UserName=None : PyUnicode

 Default username, can be None. At most CREDUI_MAX_USERNAME_LENGTH chars

- Password=None : PyUnicode

 Password, can be None. At most CREDUI_MAX_PASSWORD_LENGTH chars

- Save=True : boolean

 Specifies whether Save checkbox defaults to checked or unchecked

- Flags=0 : int

 Combination of CREDUI_FLAGS_* values

- UiInfo=None : dict

 PyCREDUI_INFO dict for customizing the dialog, can be None

#### Return Value

Returns the username, password, and a boolean indicating if credential was persisted


---

<!-- page: win32cred__CredUIReadSSOCredW_meth.html -->

## win32cred.CredUIReadSSOCredW

 PyUnicode = CredUIReadSSOCredW(Realm)

Retrieves single sign on username

#### Parameters

- Realm=None : PyUnicode

 Realm for which to read username, can be None


---

<!-- page: win32cred__CredUIStoreSSOCredW_meth.html -->

## win32cred.CredUIStoreSSOCredW

 CredUIStoreSSOCredW(Realm, Username, Password, Persist)

Creates a single sign on credential

#### Parameters

- Realm : PyUnicode

 Realm for which to read username, can be None for default realm

- Username : PyUnicode

 Username for realm

- Password : PyUnicode

 User's password

- Persist : boolean

 Specifies whether to save credential


---

<!-- page: win32cred__CredUnmarshalCredential_meth.html -->

## win32cred.CredUnmarshalCredential

 int,PyUnicode = CredUnmarshalCredential(MarshaledCredential)

Unmarshals credentials formatted using win32cred::CredMarshalCredential

#### Parameters

- MarshaledCredential : PyUnicode

 Unicode string containing marshaled credential

| | CredType | Type of output credentials
| |

---

 |

---

| | CertCredential | Character string containing SHA1 hash of a certificate
| | UsernameTargetCredential | Unicode string containing username

#### Return Value

Returns the credential type and credentials.


---

<!-- page: win32cred__CredWriteDomainCredentials_meth.html -->

## win32cred.CredWriteDomainCredentials

 CredWriteDomainCredentials(TargetInfo, Credential, Flags)

Creates or updates credential for a domain or server

#### Parameters

- TargetInfo : dict

 PyCREDENTIAL_TARGET_INFORMATION identifying the target domain. At least one of the Names is required

- Credential : dict

 PyCREDENTIAL dict containing the credentials to be stored

- Flags=0 : int

 CRED_PRESERVE_CREDENTIAL_BLOB is only defined flag

#### Comments

 When updating a credential, to preserve a previously stored password use None or '' for CredentialBlob member of Credential and pass CRED_PRESERVE_CREDENTIAL_BLOB in Flags


---

<!-- page: win32cred__CredWrite_meth.html -->

## win32cred.CredWrite

 CredWrite(Credential, Flags)

Creates or updates a stored credential

#### Parameters

- Credential : dict

 PyCREDENTIAL dict containing the credentials to be stored

- Flags=0 : int

 CRED_PRESERVE_CREDENTIAL_BLOB is only defined flag

#### Comments

 When updating a credential, to preserve a previously stored password use None or '' for CredentialBlob member of Credential and pass CRED_PRESERVE_CREDENTIAL_BLOB in Flags
