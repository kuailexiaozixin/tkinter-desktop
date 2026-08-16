# 模块 exchange

> 来源：https://mhammond.github.io/pywin32/exchange.html （及其成员页，已全部内联）

## Module exchange

 A COM interface to Exchange's API

#### Methods

- HrGetExchangeStatus

 Obtains the current state of the server on a computer.

- HrGetMailboxDN

 Retrieves the distinguished name (DN) for a mailbox

- HrGetServerDN

 Retrieves the distinguished name (DN) for a server

- HrMAPIFindDefaultMsgStore

 Retrieves the entry identifier of the default information store.

- HrMAPIFindIPMSubtree

 Retrieves the entry ID of the IPM (interpersonal message) subtree folder

- HrMAPIFindInbox

 Retrieves the Entry ID of the IPM inbox folder

- HrMAPIFindSubfolderEx

 Retrieves a subfolder in an information store using the hierarchical path name of the folder.

- HrMAPIFindFolder

 Retrieves the entry ID for a folder in an information store using the hierarchical path name of the folder.

- HrMAPIFindFolderEx

 Retrieves the entry ID of a folder in an information store using the hierarchical path name of the folder.

- HrMAPIFindStore

 Retrieves a pointer to the entry identifier of an information store from the display name of the store.

- HrCreateProfileName

 Creates a profile with the specified name

- HrCreateDirEntryIdEx

 Creates a directory identifier for a MAPI object, given the address of the object in the directory

- HrMailboxLogon

 Logs on a server and mailbox.

- HrMailboxLogoff

 Logs off a server and mailbox.

- HrMAPIOpenFolderEx

 Opens a folder in the information store from the hierarchical path name of the folder.

- HrMAPISetPropBoolean

 Sets a boolean property.

- HrMAPISetPropLong

 Sets a long property.

- HrOpenExchangePublicStore

 Retrieves an interface to the public information store provider.

- HrOpenExchangePrivateStore

 Locates the primary user information store provider.

- HrOpenExchangePublicFolders

 Opens the root of the public folder hierarchy in the public information store.

- HrOpenSessionObject

 Retrieves a MAPI PyIMAPIProp object for the current session object.

- HrOpenSiteContainer

 Retrieves a MAPI PyIMAPIProp object for a site object.

- HrOpenSiteContainerAddressing

 Retrieves a MAPI PyIMAPIProp object for a site-addressing object.


---

# exchange 成员详细文档（共 23 项）


---

<!-- page: exchange__HrCreateDirEntryIdEx_meth.html -->

## exchange.HrCreateDirEntryIdEx

 string = HrCreateDirEntryIdEx(addrBook, distinguishedName )

Creates a directory identifier for a MAPI object, given the address of the object in the directory

#### Parameters

- addrBook : PyIAddrBook

 The address book interface

- distinguishedName : string

 The dn of the object to obtain the entry ID for.


---

<!-- page: exchange__HrCreateProfileName_meth.html -->

## exchange.HrCreateProfileName

 string = HrCreateProfileName(profPrefix)

Creates a profile with the specified name

#### Parameters

- profPrefix : string/PyUnicode

 A prefix for the new profile.


---

<!-- page: exchange__HrGetExchangeStatus_meth.html -->

## exchange.HrGetExchangeStatus

 int, int = HrGetExchangeStatus(server)

Obtains the current state of the server on a computer.

#### Parameters

- server : string/PyUnicode

 The name of the server to query.

#### Return Value

The result is a tuple of serviceState, serverState


---

<!-- page: exchange__HrGetMailboxDN_meth.html -->

## exchange.HrGetMailboxDN

 string = HrGetMailboxDN(session)

Retrieves the distinguished name (DN) for a mailbox

#### Parameters

- session : IMAPISession

 The root folder.


---

<!-- page: exchange__HrGetServerDN_meth.html -->

## exchange.HrGetServerDN

 string = HrGetServerDN(session)

Retrieves the distinguished name (DN) for a server

#### Parameters

- session : IMAPISession

 The root folder.


---

<!-- page: exchange__HrMAPIFindDefaultMsgStore_meth.html -->

## exchange.HrMAPIFindDefaultMsgStore

 string = HrMAPIFindDefaultMsgStore(session)

Retrieves the entry identifier of the default information store.

#### Parameters

- session : PyIMAPISession


---

<!-- page: exchange__HrMAPIFindFolderEx_meth.html -->

## exchange.HrMAPIFindFolderEx

 string = HrMAPIFindFolderEx(msgStore, sepString , path )

Retrieves the entry ID of a folder in an information store using the hierarchical path name of the folder.

#### Parameters

- msgStore : PyIMsgStore

 The folder to search

- sepString : string

 The character separating the folder names - eg '\\'

- path : string

 Path to the folder


---

<!-- page: exchange__HrMAPIFindFolder_meth.html -->

## exchange.HrMAPIFindFolder

 string = HrMAPIFindFolder(folder, name )

Retrieves the entry ID for a folder in an information store using the hierarchical path name of the folder.

#### Parameters

- folder : PyIMAPIFolder

 The folder to search

- name : string

 Name of the folder


---

<!-- page: exchange__HrMAPIFindIPMSubtree_meth.html -->

## exchange.HrMAPIFindIPMSubtree

 string = HrMAPIFindIPMSubtree(msgStore)

Retrieves the entry ID of the IPM (interpersonal message) subtree folder

#### Parameters

- msgStore : PyIMsgStore


---

<!-- page: exchange__HrMAPIFindInbox_meth.html -->

## exchange.HrMAPIFindInbox

 string = HrMAPIFindInbox(msgStore)

Retrieves the Entry ID of the IPM inbox folder

#### Parameters

- msgStore : PyIMsgStore


---

<!-- page: exchange__HrMAPIFindStore_meth.html -->

## exchange.HrMAPIFindStore

 PyIMsgStore = HrMAPIFindStore(session, name )

Retrieves a pointer to the entry identifier of an information store from the display name of the store.

#### Parameters

- session : PyIMAPISession

- name : string


---

<!-- page: exchange__HrMAPIFindSubfolderEx_meth.html -->

## exchange.HrMAPIFindSubfolderEx

 PyIMsgStore = HrMAPIFindSubfolderEx(rootFolder, sep , name )

Retrieves a subfolder in an information store using the hierarchical path name of the folder.

#### Parameters

- rootFolder : PyIMAPIFolder

 The root folder.

- sep : string/PyUnicode

 The folder separator character.

- name : string/PyUnicode

 The folder name


---

<!-- page: exchange__HrMAPIOpenFolderEx_meth.html -->

## exchange.HrMAPIOpenFolderEx

 PyIMAPIFolder = HrMAPIOpenFolderEx(msgStore, sep , name )

Opens a folder in the information store from the hierarchical path name of the folder.

#### Parameters

- msgStore : PyIMsgStore

- sep : string/PyUnicode

 The folder separator character.

- name : string/PyUnicode

 The folder name


---

<!-- page: exchange__HrMAPISetPropBoolean_meth.html -->

## exchange.HrMAPISetPropBoolean

 HrMAPISetPropBoolean(obj, tag)

Sets a boolean property.

#### Parameters

- obj : PyIMAPIProp

 The object to set

- tag : int

 The property tag


---

<!-- page: exchange__HrMAPISetPropLong_meth.html -->

## exchange.HrMAPISetPropLong

 HrMAPISetPropLong(obj, tag)

Sets a long property.

#### Parameters

- obj : PyIMAPIProp

 The object to set

- tag : int

 The property tag


---

<!-- page: exchange__HrMailboxLogoff_meth.html -->

## exchange.HrMailboxLogoff

 HrMailboxLogoff(inbox)

Logs off a server and mailbox.

#### Parameters

- inbox : PyIMsgStore

 The open inbox.


---

<!-- page: exchange__HrMailboxLogon_meth.html -->

## exchange.HrMailboxLogon

 PyIMsgStore = HrMailboxLogon(session, msgStore , msgStoreDN , mailboxDN )

Logs on a server and mailbox.

#### Parameters

- session : PyIMAPISession

 The session object

- msgStore : PyIMsgStore

- msgStoreDN : string/PyUnicode

- mailboxDN : string/PyUnicode


---

<!-- page: exchange__HrOpenExchangePrivateStore_meth.html -->

## exchange.HrOpenExchangePrivateStore

 PyIMsgStore = HrOpenExchangePrivateStore(session)

Locates the primary user information store provider.

#### Parameters

- session : PyIMAPISession

 The MAPI session object


---

<!-- page: exchange__HrOpenExchangePublicFolders_meth.html -->

## exchange.HrOpenExchangePublicFolders

 PyIMAPIFolder = HrOpenExchangePublicFolders(store)

Opens the root of the public folder hierarchy in the public information store.

#### Parameters

- store : PyIMsgStore


---

<!-- page: exchange__HrOpenExchangePublicStore_meth.html -->

## exchange.HrOpenExchangePublicStore

 PyIMsgStore = HrOpenExchangePublicStore(session)

Retrieves an interface to the public information store provider.

#### Parameters

- session : PyIMAPISession

 The MAPI session object


---

<!-- page: exchange__HrOpenSessionObject_meth.html -->

## exchange.HrOpenSessionObject

 PyIMAPIProp = HrOpenSessionObject(session)

Retrieves a MAPI PyIMAPIProp object for the current session object.

#### Parameters

- session : PyIMAPISession

 The MAPI session object


---

<!-- page: exchange__HrOpenSiteContainerAddressing_meth.html -->

## exchange.HrOpenSiteContainerAddressing

 PyIMAPIProp = HrOpenSiteContainerAddressing(session)

Retrieves a MAPI PyIMAPIProp object for a site-addressing object.

#### Parameters

- session : PyIMAPISession

 The MAPI session object


---

<!-- page: exchange__HrOpenSiteContainer_meth.html -->

## exchange.HrOpenSiteContainer

 PyIMAPIProp = HrOpenSiteContainer(session)

Retrieves a MAPI PyIMAPIProp object for a site object.

#### Parameters

- session : PyIMAPISession

 The MAPI session object
