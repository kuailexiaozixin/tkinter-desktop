# 模块 win32profile

> 来源：https://mhammond.github.io/pywin32/win32profile.html （及其成员页，已全部内联）

## Module win32profile

 Wraps functions for dealing with user profiles

#### Methods

- CreateEnvironmentBlock

 Retrieves environment variables for a user

- DeleteProfile

 Removes a user's profile

- ExpandEnvironmentStringsForUser

 Replaces environment variables in a string with per-user values

- GetAllUsersProfileDirectory

 Retrieve All Users profile directory

- GetDefaultUserProfileDirectory

 Retrieve profile path for Default user

- GetEnvironmentStrings

 Retrieves environment variables for current process

- GetProfilesDirectory

 Retrieves directory where user profiles are stored

- GetProfileType

 Returns type of current user's profile

- GetUserProfileDirectory

 Returns profile directory for a logon token

- LoadUserProfile

 Load user settings for a login token

- UnloadUserProfile

 Unload profile loaded by LoadUserProfile


---

# win32profile 成员详细文档（共 11 项）


---

<!-- page: win32profile__CreateEnvironmentBlock_meth.html -->

## win32profile.CreateEnvironmentBlock

 dict = CreateEnvironmentBlock(Token, Inherit )

Retrieves environment variables for a user

#### Parameters

- Token : PyHANDLE

 User token as returned by win32security::LogonUser, use None to retrieve system variables only

- Inherit : boolean

 Indicates if environment of current process should be inherited


---

<!-- page: win32profile__DeleteProfile_meth.html -->

## win32profile.DeleteProfile

 DeleteProfile(SidString, ProfilePath, ComputerName)

Remove profile for a user identified by string SID from specified machine.

#### Parameters

- SidString : PyUnicode

 String representation of user's Sid. See win32security::ConvertSidToStringSid.

- ProfilePath=None : PyUnicode

 Profile directory, value queried from registry if not specified

- ComputerName=None : PyUnicode

 Name of computer from which to delete profile, local machine assumed if not specified


---

<!-- page: win32profile__ExpandEnvironmentStringsForUser_meth.html -->

## win32profile.ExpandEnvironmentStringsForUser

 PyUnicode = ExpandEnvironmentStringsForUser(Token, Src )

Replaces environment variables in a string with per-user values

#### Parameters

- Token : PyHANDLE

 The logon token for a user. Use None for system variables.

- Src : PyUnicode

 String containing environment variables enclosed in % signs


---

<!-- page: win32profile__GetAllUsersProfileDirectory_meth.html -->

## win32profile.GetAllUsersProfileDirectory

 PyUnicode = GetAllUsersProfileDirectory()

Retrieve All Users profile path


---

<!-- page: win32profile__GetDefaultUserProfileDirectory_meth.html -->

## win32profile.GetDefaultUserProfileDirectory

 PyUnicode = GetDefaultUserProfileDirectory()

Retrieve Default user profile


---

<!-- page: win32profile__GetEnvironmentStrings_meth.html -->

## win32profile.GetEnvironmentStrings

 dict = GetEnvironmentStrings()

Retrieves environment variables for current process


---

<!-- page: win32profile__GetProfileType_meth.html -->

## win32profile.GetProfileType

 int = GetProfileType()

Returns type of current user's profile

#### Return Value

Returns a combination of PT_* flags


---

<!-- page: win32profile__GetProfilesDirectory_meth.html -->

## win32profile.GetProfilesDirectory

 PyUnicode = GetProfilesDirectory()

Retrieves directory where user profiles are stored


---

<!-- page: win32profile__GetUserProfileDirectory_meth.html -->

## win32profile.GetUserProfileDirectory

 PyUnicode = GetUserProfileDirectory(Token)

Returns profile directory for a logon token

#### Parameters

- Token : PyHANDLE

 User token as returned by win32security::LogonUser


---

<!-- page: win32profile__LoadUserProfile_meth.html -->

## win32profile.LoadUserProfile

 PyHKEY = LoadUserProfile(hToken, ProfileInfo )

Loads user settings into registry

#### Parameters

- hToken : PyHANDLE

 Logon token as returned by win32security::LogonUser, win32security::OpenThreadToken, etc

- ProfileInfo : PyPROFILEINFO

 Dictionary representing a PROFILEINFO structure

#### Comments

 SE_BACKUP_NAME and SE_RESTORE_NAME privs are required, but do not have to be enabled

#### Return Value

Returns a handle to user's registry key.


---

<!-- page: win32profile__UnloadUserProfile_meth.html -->

## win32profile.UnloadUserProfile

 UnloadUserProfile(Token, Profile)

Unloads user profile loaded by win32profile::LoadUserProfile

#### Parameters

- Token : PyHANDLE

 Logon token as returned by win32security::LogonUser, win32security::OpenProcessToken, etc

- Profile : PyHKEY

 Registry handle as returned by win32profile::LoadUserProfile
