# 模块 propsys

> 来源：https://mhammond.github.io/pywin32/propsys.html （及其成员页，已全部内联）

## Module propsys

 A module, encapsulating the Property System interfaces

#### Methods

- PSGetItemPropertyHandler

 Retrieves the property store for a shell item

- PSGetPropertyDescription

 Gets a description interface for a property

- PSGetPropertySystem

 Creates an IPropertySystem interface

- PSGetNameFromPropertyKey

 Retrieves the canonical name for a property key

- PSGetPropertyKeyFromName

 Retrieves the property key by canonical name

- PSRegisterPropertySchema

 Registers a group of properties described in a schema file

- PSUnregisterPropertySchema

 Removes a property schema definition

- SHGetPropertyStoreFromParsingName

 Retrieves the property store for an item by path

- StgSerializePropVariant

 Serializes a PyPROPVARIANT

- StgDeserializePropVariant

 Creates a PyPROPVARIANT from a serialized buffer

- PSCreateMemoryPropertyStore

 Creates a temporary property store that is not connected to any backing storage

- PSCreatePropertyStoreFromPropertySetStorage

 Wraps a PyIPropertySetStorage interface in a PyIPropertyStore object

- PSLookupPropertyHandlerCLSID

 Returns the GUID of the property handler for a file

- SHGetPropertyStoreForWindow

 Retrieves a collection of a window's properties

- PSGetPropertyFromPropertyStorage

 Extracts a property from a serialized buffer by key

- PSGetNamedPropertyFromPropertyStorage

 Extracts a property from a serialized buffer by name

- PSCreateSimplePropertyChange

 Creates a PyIPropertyChange interface used to apply changes to a PyPROPVARIANT

- PSCreatePropertyChangeArray

 Creates a PyIPropertyChangeArray interface to be used with PyIFileOperation

- SHSetDefaultProperties

 Sets the default properties for a file.


---

# propsys 成员详细文档（共 19 项）


---

<!-- page: propsys__PSCreateMemoryPropertyStore_meth.html -->

## propsys.PSCreateMemoryPropertyStore

 PyIPropertyStore = PSCreateMemoryPropertyStore(riid)

Creates a temporary property store that is not connected to any backing storage

#### Parameters

- riid=IID_IPropertyStore : PyIID

 The interface to create

#### Comments

 May also be used to create PyINamedPropertyStore, PyIPropertyStoreCache, PyIPersistStream, or PyIPropertyBag


---

<!-- page: propsys__PSCreatePropertyChangeArray_meth.html -->

## propsys.PSCreatePropertyChangeArray

 PyIPropertyChangeArray = PSCreatePropertyChangeArray()

Creates an IPropertyChangeArray interface to be used with PyIFileOperation

#### Comments

 Currently only creates an empty array to be filled in later


---

<!-- page: propsys__PSCreatePropertyStoreFromPropertySetStorage_meth.html -->

## propsys.PSCreatePropertyStoreFromPropertySetStorage

 PyIPropertyStore = PSCreatePropertyStoreFromPropertySetStorage(pss, Mode , riid )

Wraps a PyIPropertySetStorage interface in a PyIPropertyStore object

#### Parameters

- pss : PyIPropertySetStorage

 Property container to be adapted

- Mode : int

 Read or write mode, shellcon.STGM_*. Must match mode used to open input interface.

- riid=IID_IPropertyStore : PyIID

 The interface to create

#### Comments

 This function does not work for the NTFS property storage implementation based on alternate data streams.


---

<!-- page: propsys__PSCreateSimplePropertyChange_meth.html -->

## propsys.PSCreateSimplePropertyChange

 PyIPropertyChange = PSCreateSimplePropertyChange(flags, key , val , riid )

Creates an IPropertyChange interface used to apply changes to a PyPROPVARIANT

#### Parameters

- flags : int

 The change operation, pscon.PKA_*

- key : PyPROPERTYKEY

 The property key

- val : PyPROPVARIANT

 The value that the change operation will apply

- riid=IID_IPropertyChange : PyIID

 The interface to return.


---

<!-- page: propsys__PSGetItemPropertyHandler_meth.html -->

## propsys.PSGetItemPropertyHandler

 PyIPropertyStore = PSGetItemPropertyHandler(Item, ReadWrite , riid )

Retrieves the property store for a shell item

#### Parameters

- Item : PyIShellItem

 A shell item

- ReadWrite=False : bool

 Pass True for a writeable property store

- riid=IID_IPropertyStore : PyIID

 Interface to return


---

<!-- page: propsys__PSGetNameFromPropertyKey_meth.html -->

## propsys.PSGetNameFromPropertyKey

 string = PSGetNameFromPropertyKey(Key)

Retrieves the canonical name of a property

#### Parameters

- Key : PyPROPERTYKEY

 A property key


---

<!-- page: propsys__PSGetNamedPropertyFromPropertyStorage_meth.html -->

## propsys.PSGetNamedPropertyFromPropertyStorage

 PyPROPVARIANT = PSGetNamedPropertyFromPropertyStorage(ps, name )

Extracts a property value from a serialized buffer by name

#### Parameters

- ps : buffer

 Bytes or buffer (or str in Python 2) containing a serialized property set (see PyIPersistSerializedPropStorage::GetPropertyStorage)

- name : str

 Property to return


---

<!-- page: propsys__PSGetPropertyDescription_meth.html -->

## propsys.PSGetPropertyDescription

 PyIPropertyDescription = PSGetPropertyDescription(Key, riid )

Gets a description interface for a property

#### Parameters

- Key : PyPROPERTYKEY

 A property key identifier

- riid=IID_IPropertyDescription : PyIID

 The interface to return

#### Comments

 Possible interfaces include IPropertyDescription, IPropertyDescriptionAliasInfo, and IPropertyDescriptionSearchInfo


---

<!-- page: propsys__PSGetPropertyFromPropertyStorage_meth.html -->

## propsys.PSGetPropertyFromPropertyStorage

 PyPROPVARIANT = PSGetPropertyFromPropertyStorage(ps, key )

Extracts a property value from a serialized buffer by key

#### Parameters

- ps : buffer

 Bytes or buffer (or str in Python 2) containing a serialized property set (see PyIPersistSerializedPropStorage::GetPropertyStorage)

- key : PyPROPERTYKEY

 Property to return


---

<!-- page: propsys__PSGetPropertyKeyFromName_meth.html -->

## propsys.PSGetPropertyKeyFromName

 PyPROPERTYKEY = PSGetPropertyKeyFromName(Name)

Retrieves the property key by canonical name

#### Parameters

- Name : str

 The canonical name of a property (eg System.Author)


---

<!-- page: propsys__PSGetPropertySystem_meth.html -->

## propsys.PSGetPropertySystem

 PyIPropertySystem = PSGetPropertySystem(riid)

Creates an IPropertySystem interface

#### Parameters

- riid=IID_IPropertySystem : PyIID

 The interface to return


---

<!-- page: propsys__PSLookupPropertyHandlerCLSID_meth.html -->

## propsys.PSLookupPropertyHandlerCLSID

 PyIID = PSLookupPropertyHandlerCLSID(FilePath)

Returns the GUID of the property handler for a file

#### Parameters

- FilePath : str

 Name of file

#### Comments

 If no handler is found, the returned error code can be deceptive as it seems to indicate that the file itself was not found


---

<!-- page: propsys__PSRegisterPropertySchema_meth.html -->

## propsys.PSRegisterPropertySchema

 PSRegisterPropertySchema(filename)

Registers a group of properties described in a schema file

#### Parameters

- filename : unicode

 An XML file that defines a property schema (*.propdesc)


---

<!-- page: propsys__PSUnregisterPropertySchema_meth.html -->

## propsys.PSUnregisterPropertySchema

 PSUnregisterPropertySchema(filename)

Removes a property schema definition

#### Parameters

- filename : unicode

 A previously registered schema definition file


---

<!-- page: propsys__SHGetPropertyStoreForWindow_meth.html -->

## propsys.SHGetPropertyStoreForWindow

 PyIPropertyStore = SHGetPropertyStoreForWindow(hwnd, riid )

Retrieves a collection of a window's properties

#### Parameters

- hwnd : PyHANDLE

 Handle to a window

- riid=IID_IPropertyStore : PyIID

 The interface to create

#### Return Value

The returned store can be used to set the System.AppUserModel.ID property that determines how windows are grouped on the taskbar


---

<!-- page: propsys__SHGetPropertyStoreFromParsingName_meth.html -->

## propsys.SHGetPropertyStoreFromParsingName

 PyIPropertyStore = SHGetPropertyStoreFromParsingName(Path, BindCtx , Flags , riid )

Retrieves the property store for an item by path

#### Parameters

- Path : string

 Path to file

- BindCtx=None : PyIBindCtx

 Bind context, or None

- Flags=GPS_DEFAULT : int

 Combination of GETPROPERTYSTOREFLAGS values (shellcon.GPS_*)

- riid=IID_IPropertyStore : PyIID

 The interface to return

#### Comments

 This function does not exist on XP, even with Desktop Search installed


---

<!-- page: propsys__SHSetDefaultProperties_meth.html -->

## propsys.SHSetDefaultProperties

 SHSetDefaultProperties(hwnd, Item, FileOpFlags, Sink)

Sets the default properties for a file.

#### Parameters

- hwnd : PyHANDLE

 Parent window for any notifications, can be None

- Item : PyIShellItem

 Shell item whose defaults are to be set

- FileOpFlags=0 : int

 File operation flags, as used with PyIFileOperation::SetOperationFlags

- Sink=None : PyGFileOperationProgressSink

 Event sink to receive notifications

#### Comments

 Default properties are registered by filetype under SetDefaultsFor value.


---

<!-- page: propsys__StgDeserializePropVariant_meth.html -->

## propsys.StgDeserializePropVariant

 PyPROPVARIANT = StgDeserializePropVariant(prop)

Creates a PyPROPVARIANT from a serialized buffer

#### Parameters

- prop : bytes

 Buffer or bytes object (or str in Python 2) containing a serialized value


---

<!-- page: propsys__StgSerializePropVariant_meth.html -->

## propsys.StgSerializePropVariant

 bytes = StgSerializePropVariant(propvar)

Serializes a PyPROPVARIANT

#### Parameters

- propvar : PyPROPVARIANT

 The value to serialize
