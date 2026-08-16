# 模块 pythoncom

> 来源：https://mhammond.github.io/pywin32/pythoncom.html （及其成员页，已全部内联）

## Module pythoncom

 A module, encapsulating the OLE automation API

#### Methods

- _GetInterfaceCount

 Retrieves the number of interface objects currently in existance

- _GetInterfaceCount

 Retrieves the number of gateway objects currently in existance

- CoCreateFreeThreadedMarshaler

 Creates an aggregatable object capable of context-dependent marshaling.

- CoCreateInstanceEx

 Create a new instance of an OLE automation server possibly on a remote machine.

- CoCreateInstance

 Create a new instance of an OLE automation server.

- CoFreeUnusedLibraries

 Unloads any DLLs that are no longer in use and that, when loaded, were specified to be freed automatically.

- CoInitialize

 Initialize the COM libraries for the calling thread.

- CoInitializeEx

 Initialize the COM libraries for the calling thread.

- CoInitializeSecurity

 Registers security and sets the default security values.

- CoGetInterfaceAndReleaseStream

 Unmarshals a buffer containing an interface pointer and releases the stream when an interface pointer has been marshaled from another thread to the calling thread.

- CoMarshalInterThreadInterfaceInStream

 Marshals an interface pointer from one thread to another thread in the same process.

- CoMarshalInterface

 Marshals an interface into a stream

- CoUnmarshalInterface

 Unmarshals an interface

- CoReleaseMarshalData

 Frees resources used by a marshalled interface

- CoGetObject

 Converts a display name into a moniker that identifies the object named, and then binds to the object identified by the moniker.

- CoUninitialize

 Uninitialize the COM libraries.

- CoRegisterClassObject

 Registers an EXE class object with OLE so other applications can connect to it.

- CoResumeClassObjects

 Called by a server that can register multiple class objects to inform the OLE SCM about all registered classes, and permits activation requests for those class objects.

- CoRevokeClassObject

 Informs OLE that a class object, previously registered with the pythoncom::CoRegisterClassObject method, is no longer available for use.

- CoTreatAsClass

 Establishes or removes an emulation, in which objects of one class are treated as objects of a different class.

- CoWaitForMultipleHandles

 Waits for specified handles to be signaled or for a specified timeout period to elapse.

- Connect

 Connects to a running instance of an OLE automation server.

- CreateGuid

 Creates a new, unique GUIID.

- CreateBindCtx

 Obtains a PyIBindCtx object.

- CreateFileMoniker

 Creates a file moniker given a file name.

- CreateItemMoniker

 Creates an item moniker that identifies an object within a containing object (typically a compound document).

- CreatePointerMoniker

 Creates a pointer moniker based on a pointer to an object.

- CreateURLMoniker

 Create a URL moniker from a full url or partial url and base moniker

- CreateTypeLib

 Provides access to a new object instance that supports the ICreateTypeLib interface.

- CreateTypeLib2

 Provides access to a new object instance that supports the ICreateTypeLib2 interface.

- CreateStreamOnHGlobal

 Creates an in-memory stream storage object

- CreateILockBytesOnHGlobal

 Creates an ILockBytes interface based on global memory

- EnableQuitMessage

 Indicates the thread PythonCOM should post a WM_QUIT message to.

- FUNCDESC

 Returns a new FUNCDESC object.

- GetActiveObject

 Retrieves an object representing a running object registered with OLE

- GetClassFile

 Supplies the CLSID associated with the given filename.

- GetFacilityString

 Returns the facility string, given an OLE scode.

- GetRecordFromGuids

 Creates a new record object from the given GUIDs

- GetRecordFromTypeInfo

 Creates a PyRecord object from a PyITypeInfo interface

- GetRunningObjectTable

 Obtains a PyIRunningObjectTable object.

- GetScodeString

 Returns the string for an OLE scode.

- GetScodeRangeString

 Returns the scode range string, given an OLE scode.

- GetSeverityString

 Returns the severity string, given an OLE scode.

- IsGatewayRegistered

 Returns 1 if the given IID has a registered gateway object.

- LoadRegTypeLib

 Loads a registered type library by CLSID

- LoadTypeLib

 Loads a type library by name

- MakePyFactory

 Creates a new PyIClassFactory object wrapping a PythonCOM Class Factory object.

- MkParseDisplayName

 Parses a moniker display name into a moniker object. The inverse of IMoniker::GetDisplayName.

- New

 Create a new instance of an OLE automation server.

- ObjectFromAddress

 Returns a COM object given its address in memory.

- ObjectFromLresult

 Retrieves a requested interface pointer for an object based on a previously generated object reference.

- OleInitialize

- OleGetClipboard

 Retrieves a data object that you can use to access the contents of the clipboard.

- OleFlushClipboard

 Carries out the clipboard shutdown sequence. It also releases the IDataObject pointer that was placed on the clipboard by the pythoncom::OleSetClipboard function.

- OleIsCurrentClipboard

 Determines whether the data object pointer previously placed on the clipboard by the OleSetClipboard function is still on the clipboard.

- OleSetClipboard

 Places a pointer to a specific data object onto the clipboard. This makes the data object accessible to the OleGetClipboard function.

- OleLoadFromStream

 Load an object from an IStream.

- OleSaveToStream

 Save an object to an IStream.

- OleLoad

 Loads into memory an object nested within a specified storage object.

- ProgIDFromCLSID

 Converts a CLSID string to a progID.

- PumpWaitingMessages

 Pumps all waiting messages for the current thread.

- PumpMessages

 Pumps all messages for the current thread until a WM_QUIT message.

- QueryPathOfRegTypeLib

 Retrieves the path of a registered type library

- ReadClassStg

 Reads a CLSID from a storage object

- ReadClassStm

 Reads a CLSID from a PyIStream object

- RegisterTypeLib

 Adds information about a type library to the system registry.

- UnRegisterTypeLib

 Removes a type library from the system registry.

- RegisterActiveObject

 Register an object as the active object for its class

- RevokeActiveObject

 Ends an object's status as active.

- RegisterDragDrop

 Registers the specified window as one that can be the target of an OLE drag-and-drop operation.

- RevokeDragDrop

 Revokes the specified window as the target of an OLE drag-and-drop operation.

- DoDragDrop

 Carries out an OLE drag and drop operation.

- StgCreateDocfile

 Creates a new compound file storage object using the OLE-provided compound file implementation for the PyIStorage interface.

- StgCreateDocfileOnILockBytes

 Creates a new compound file storage object using the OLE-provided compound file implementation for the PyIStorage interface.

- StgOpenStorageOnILockBytes

 Open an existing storage object that does not reside in a disk file, but instead has an underlying PyILockBytes byte array provided by the caller.

- StgIsStorageFile

 Indicates whether a particular disk file contains a storage object.

- STGMEDIUM

 Creates a new PySTGMEDIUM object suitable for the PyIDataObject interface.

- StgOpenStorage

 Opens an existing root storage object in the file system.

- StgOpenStorageEx

 Access IStorage and IPropertySetStorage interfaces for normal files

- StgCreateStorageEx

 Creates a new structured storage file or property set

- TYPEATTR

 Returns a new TYPEATTR object.

- VARDESC

 Returns a new VARDESC object.

- WrapObject

 Wraps an object in a gateway.

- WriteClassStg

 Stores a CLSID from a storage object

- WriteClassStm

 Sets the CLSID of a stream

- UnwrapObject

 Unwraps a Python instance in a gateway object.

- FmtIdToPropStgName

 Convert a FMTID to its stream name

- PropStgNameToFmtId

 Convert property set name to FMTID

- CoGetCallContext

 Creates interfaces used to access client security settings and perform impersonation

- CoGetObjectContext

 Creates an interface to interact with the context of the current object

- CoGetCancelObject

 Retrieves an interface used to cancel a pending call

- CoSetCancelObject

 Sets or removes a PyICancelMethodCalls interface to be used on the current thread

- CoEnableCallCancellation

 Enables call cancellation for synchronous calls on the current thread

- CoDisableCallCancellation

 Disables call cancellation for synchronous calls on the current thread

#### Properties

- int dcom
 1 if the system is DCOM aware, else 0. Only Win95 without DCOM extensions should return 0


---

# pythoncom 成员详细文档（共 96 项）


---

<!-- page: pythoncom__CoCreateFreeThreadedMarshaler_meth.html -->

## pythoncom.CoCreateFreeThreadedMarshaler

 PyIUnknown = CoCreateFreeThreadedMarshaler(unk)

Creates an aggregatable object capable of context-dependent marshaling.

#### Parameters

- unk : PyIUnknown

 The unknown object to marshal.


---

<!-- page: pythoncom__CoCreateInstanceEx_meth.html -->

## pythoncom.CoCreateInstanceEx

 PyIUnknown = CoCreateInstanceEx(clsid, unkOuter , context , serverInfo , iids )

Create a new instance of an OLE automation server possibly on a remote machine.

#### Parameters

- clsid : PyIID

 Class identifier (CLSID) of the object

- unkOuter : PyIUnknown

 The outer unknown, or None

- context : int

 The create context for the object, combination of pythoncom.CLSCTX_* flags

- serverInfo : (server, authino=None, reserved1=0,reserved2=0)

 May be None, or describes the remote server to execute on.

- iids : [PyIID, ...]

 A list of IIDs required from the object


---

<!-- page: pythoncom__CoCreateInstance_meth.html -->

## pythoncom.CoCreateInstance

 PyIUnknown = CoCreateInstance(clsid, unkOuter , context , iid )

Create a new instance of an OLE automation server.

#### Parameters

- clsid : PyIID

 Class identifier (CLSID) of the object

- unkOuter : PyIUnknown

 The outer unknown, or None

- context : int

 The create context for the object, combination of pythoncom.CLSCTX_* flags

- iid : PyIID

 The IID required from the object


---

<!-- page: pythoncom__CoDisableCallCancellation_meth.html -->

## pythoncom.CoDisableCallCancellation

 CoDisableCallCancellation()

Disables call cancellation for synchronous calls on the current thread


---

<!-- page: pythoncom__CoEnableCallCancellation_meth.html -->

## pythoncom.CoEnableCallCancellation

 CoEnableCallCancellation()

Enables call cancellation for synchronous calls on the current thread


---

<!-- page: pythoncom__CoFreeUnusedLibraries_meth.html -->

## pythoncom.CoFreeUnusedLibraries

 CoFreeUnusedLibraries()

Unloads any DLLs that are no longer in use and that, when loaded, were specified to be freed automatically.


---

<!-- page: pythoncom__CoGetCallContext_meth.html -->

## pythoncom.CoGetCallContext

 PyIServerSecurity = CoGetCallContext(riid)

Creates interfaces used to access client security requirements and perform impersonation

#### Parameters

- riid=IID_IServerSecurity : PyIID

 The interface to create, IID_IServerSecurity or IID_ISecurityCallContext

#### Comments

 ISecurityCallContext will only be available for a server that uses role-based security


---

<!-- page: pythoncom__CoGetCancelObject_meth.html -->

## pythoncom.CoGetCancelObject

 PyICancelMethodCalls = CoGetCancelObject(ThreadID, riid )

Retrieves an interface used to cancel a pending call

#### Parameters

- ThreadID=0 : int

 Id of thread with pending call, or 0 for current thread

- riid=IID_ICancelMethodCalls : PyIID

 The interface to return


---

<!-- page: pythoncom__CoGetInterfaceAndReleaseStream_meth.html -->

## pythoncom.CoGetInterfaceAndReleaseStream

 PyIUnknown = CoGetInterfaceAndReleaseStream(stream, iid )

Unmarshals a buffer containing an interface pointer and releases the stream when an interface pointer has been marshaled from another thread to the calling thread.

#### Parameters

- stream : PyIStream

 The stream to unmarshal the object from.

- iid : PyIID

 The IID if the interface to unmarshal.


---

<!-- page: pythoncom__CoGetObjectContext_meth.html -->

## pythoncom.CoGetObjectContext

 PyIContext = CoGetObjectContext(riid)

Creates an interface to interact with the context of the current object

#### Parameters

- riid=IID_IContext : PyIID

 The interface to return

#### Comments

 COM applications can use this function to create IComThreadingInfo, IContext, or IContextCallback COM+ applications may also create IObjectContext, IObjectContextInfo, IObjectContextActivity, or IContextState


---

<!-- page: pythoncom__CoGetObject_meth.html -->

## pythoncom.CoGetObject

 PyIUnknown = CoGetObject(name, bindOpts , iid )

Converts a display name into a moniker that identifies the object named, and then binds to the object identified by the moniker.

#### Parameters

- name : string

- bindOpts=None : None

 Must be None

- iid=IID_IUnknown : PyIID

 The IID of the interface to return.


---

<!-- page: pythoncom__CoInitializeEx_meth.html -->

## pythoncom.CoInitializeEx

 CoInitializeEx(flags)

Initialize the COM libraries for the calling thread.

#### Parameters

- flags : int

 Flags for the initialization.

#### Comments

 There is no need to call this for the main Python thread, as it is called automatically by pythoncom (using sys.coinit_flags as the param, or COINIT_APARTMENTTHREADED if sys.coinit_flags does not exist).
You must call this manually if you create a thread which wishes to use COM.

#### Return Value

This function will raise pythoncom.error for all error return values, including RPC_E_CHANGED_MODE error. This is in contrast to pythoncom::CoInitialize which will hide that specific error. If your code is happy to work in a threading model other than the one you specified, you must explicitly handle (and presumably ignore) this exception.


---

<!-- page: pythoncom__CoInitializeSecurity_meth.html -->

## pythoncom.CoInitializeSecurity

 CoInitializeSecurity(sd, authSvc, reserved1, authnLevel, impLevel, authInfo, capabilities, reserved2)

Registers security and sets the default security values.

#### Parameters

- sd : PySECURITY_DESCRIPTOR

 Security descriptor containing access permissions for process' objects, can be None.
If Capabilities contains EOAC_APPID, sd should be an AppId (guid), or None to use server executable.
If Capabilities contains EOAC_ACCESS_CONTROL, sd parameter should be an IAccessControl interface.

- authSvc : object

 A value of None tells COM to choose which authentication services to use. An empty list means use no services.

- reserved1 : object

 Must be None

- authnLevel : int

 One of pythoncom.RPC_C_AUTHN_LEVEL_* values. The default authentication level for proxies. On the server side, COM will fail calls that arrive at a lower level. All calls to AddRef and Release are made at this level.

- impLevel : int

 One of pythoncom.RPC_C_IMP_LEVEL_* values. The default impersonation level for proxies. This value is not checked on the server side. AddRef and Release calls are made with this impersonation level so even security aware apps should set this carefully. Setting IUnknown security only affects calls to QueryInterface, not AddRef or Release.

- authInfo : object

 Must be None

- capabilities : int

 Authentication capabilities, combination of pythoncom.EOAC_* flags.

- reserved2 : object

 Must be None


---

<!-- page: pythoncom__CoInitialize_meth.html -->

## pythoncom.CoInitialize

 CoInitialize()

Initialize the COM libraries for the calling thread.

#### Comments

 Apart from the error handling semantics, this is equivalent to pythoncom::CoInitializeEx(pythoncom.COINIT_APARTMENTTHREADED). See pythoncom::CoInitializeEx for a description.

#### Return Value

This function will ignore the RPC_E_CHANGED_MODE error, as that error indicates someone else beat you to the initialization, and did so with a different threading model. This error is ignored as it still means COM is ready for use on this thread, and as this function does not explicitly specify a threading model the caller probably doesn't care what model it is.
All other COM errors will raise pythoncom.error as usual. Use pythoncom::CoInitializeEx if you also want to handle the RPC_E_CHANGED_MODE error.


---

<!-- page: pythoncom__CoMarshalInterThreadInterfaceInStream_meth.html -->

## pythoncom.CoMarshalInterThreadInterfaceInStream

 PyIStream = CoMarshalInterThreadInterfaceInStream(iid, unk )

Marshals an interface pointer from one thread to another thread in the same process.

#### Parameters

- iid : PyIID

 The IID of the interface to marshal.

- unk : PyIUnknown

 The interface to marshal.


---

<!-- page: pythoncom__CoMarshalInterface_meth.html -->

## pythoncom.CoMarshalInterface

 CoMarshalInterface(Stm, riid, Unk, DestContext, flags)

Marshals an interface into a stream

#### Parameters

- Stm : PyIStream

 An IStream interface into which marshalled interface will be written

- riid : PyIID

 IID of interface to be marshalled

- Unk : PyIUnknown

 Base IUnknown of the object to be marshalled

- DestContext : int

 MSHCTX_* flag indicating where object will be unmarshalled

- flags=MSHLFLAGS_NORMAL : int

 MSHLFLAGS_* flag indicating marshalling options


---

<!-- page: pythoncom__CoRegisterClassObject_meth.html -->

## pythoncom.CoRegisterClassObject

 int = CoRegisterClassObject(iid, factory , context , flags )

Registers an EXE class object with OLE so other applications can connect to it.

#### Parameters

- iid : PyIID

 The IID of the object to register

- factory : PyIUnknown

 The class factory object. It is the Python programmers responsibility to ensure this object remains alive until the class is unregistered.

- context : int

 The create context for the server. Must be a combination of the CLSCTX_* flags.

- flags : int

 Create flags.

#### Comments

 The class factory object should be PyIClassFactory object, but as per the COM documentation, only PyIUnknown is checked.

#### Return Value

The result is a handle which should be revoked using pythoncom::CoRevokeClassObject


---

<!-- page: pythoncom__CoReleaseMarshalData_meth.html -->

## pythoncom.CoReleaseMarshalData

 CoReleaseMarshalData(Stm)

Frees resources used by a marshalled interface

#### Parameters

- Stm : PyIStream

 Stream containing marshalled interface

#### Comments

 This is usually only needed when the interface could not be successfully unmarshalled


---

<!-- page: pythoncom__CoResumeClassObjects_meth.html -->

## pythoncom.CoResumeClassObjects

 CoResumeClassObjects()

Called by a server that can register multiple class objects to inform the OLE SCM about all registered classes, and permits activation requests for those class objects.


---

<!-- page: pythoncom__CoRevokeClassObject_meth.html -->

## pythoncom.CoRevokeClassObject

 CoRevokeClassObject(reg)

Informs OLE that a class object, previously registered with the pythoncom::CoRegisterClassObject method, is no longer available for use.

#### Parameters

- reg : int

 The value returned from pythoncom::CoRegisterClassObject


---

<!-- page: pythoncom__CoSetCancelObject_meth.html -->

## pythoncom.CoSetCancelObject

 CoSetCancelObject(Unk)

Sets or removes a PyICancelMethodCalls interface to be used on the current thread

#### Parameters

- Unk : PyIUnknown

 An interface that support ICancelMethodCalls, can be None to unregister current cancel object


---

<!-- page: pythoncom__CoTreatAsClass_meth.html -->

## pythoncom.CoTreatAsClass

 CoTreatAsClass(clsidold, clsidnew)

Establishes or removes an emulation, in which objects of one class are treated as objects of a different class.

#### Parameters

- clsidold : PyIID

 CLSID of the object to be emulated.

- clsidnew=CLSID_NULL : PyIID

 CLSID of the object that should emulate the original object. This replaces any existing emulation for clsidOld. Can be ommitted or CLSID_NULL, in which case any existing emulation for clsidOld is removed.


---

<!-- page: pythoncom__CoUninitialize_meth.html -->

## pythoncom.CoUninitialize

 CoUninitialize()

Uninitialize the COM libraries for the calling thread.


---

<!-- page: pythoncom__CoUnmarshalInterface_meth.html -->

## pythoncom.CoUnmarshalInterface

 interface = CoUnmarshalInterface(Stm, riid )

Unmarshals an interface

#### Parameters

- Stm : PyIStream

 Stream containing marshalled interface

- riid : PyIID

 IID of interface to be unmarshalled


---

<!-- page: pythoncom__CoWaitForMultipleHandles_meth.html -->

## pythoncom.CoWaitForMultipleHandles

 int = CoWaitForMultipleHandles(Flags, Timeout , Handles )

Waits for specified handles to be signaled or for a specified timeout period to elapse.

#### Parameters

- Flags : int

 Combination of pythoncom.COWAIT_* values

- Timeout : int

 Timeout in milliseconds

- Handles : [PyHANDLE, ...]

 Sequence of handles


---

<!-- page: pythoncom__Connect_meth.html -->

## pythoncom.Connect

 PyIDispatch = Connect(cls)

Connect to an already running OLE automation server.

#### Parameters

- cls : CLSID

 An identifier for the program. Usually "program.item"

#### Comments

 This function is equivalent to pythoncom::GetActiveObject(clsid).pythoncom::QueryInterace (pythoncom.IID_IDispatch)


---

<!-- page: pythoncom__CreateBindCtx_meth.html -->

## pythoncom.CreateBindCtx

 PyIBindCtx = CreateBindCtx()

Creates a new PyIBindCtx object.


---

<!-- page: pythoncom__CreateFileMoniker_meth.html -->

## pythoncom.CreateFileMoniker

 PyIMoniker = CreateFileMoniker(filename)

Creates a new PyIMoniker object.

#### Parameters

- filename : string

 The name of the file.


---

<!-- page: pythoncom__CreateGuid_meth.html -->

## pythoncom.CreateGuid

 PyIID = CreateGuid()

Creates a new, unique GUIID.

#### Comments

 Use the CreateGuid function when you need an absolutely unique number that you will use as a persistent identifier in a distributed environment.To a very high degree of certainty, this function returns a unique value no other invocation, on the same or any other system (networked or not), should return the same value.


---

<!-- page: pythoncom__CreateILockBytesOnHGlobal_meth.html -->

## pythoncom.CreateILockBytesOnHGlobal

 PyILockBytes = CreateILockBytesOnHGlobal(hGlobal, DeleteOnRelease )

Creates an ILockBytes interface based on global memory

#### Parameters

- hGlobal=None : PyHANDLE

 Global memory handle. If None, a new global memory object is allocated.

- DeleteOnRelease=True : bool

 Indicates if global memory should be freed when interface is released.


---

<!-- page: pythoncom__CreateItemMoniker_meth.html -->

## pythoncom.CreateItemMoniker

 PyIMoniker = CreateItemMoniker(delim, item )

Creates an item moniker that identifies an object within a containing object (typically a compound document).

#### Parameters

- delim : string

 String containing the delimiter (typically "!") used to separate this item's display name from the display name of its containing object.

- item : string

 String indicating the containing object's name for the object being identified.


---

<!-- page: pythoncom__CreatePointerMoniker_meth.html -->

## pythoncom.CreatePointerMoniker

 PyIMoniker = CreatePointerMoniker(IUnknown)

Creates a new PyIMoniker object.

#### Parameters

- IUnknown : PyIUnknown

 The interface for the moniker.


---

<!-- page: pythoncom__CreateStreamOnHGlobal_meth.html -->

## pythoncom.CreateStreamOnHGlobal

 PyIStream = CreateStreamOnHGlobal(hGlobal, DeleteOnRelease )

Creates an in-memory stream storage object

#### Parameters

- hGlobal=None : PyHANDLE

 Global memory handle. If None, a new global memory object is allocated.

- DeleteOnRelease=True : bool

 Indicates if global memory should be freed when IStream object is destroyed.


---

<!-- page: pythoncom__CreateTypeLib2_meth.html -->

## pythoncom.CreateTypeLib2

 ICreateTypeLib2 = CreateTypeLib2()

Provides access to a new object instance that supports the ICreateTypeLib2 interface.


---

<!-- page: pythoncom__CreateTypeLib_meth.html -->

## pythoncom.CreateTypeLib

 ICreateTypeLib = CreateTypeLib()

Provides access to a new object instance that supports the ICreateTypeLib interface.


---

<!-- page: pythoncom__CreateURLMonikerEx_meth.html -->

## pythoncom.CreateURLMonikerEx

 PyIMoniker = CreateURLMonikerEx(Context, URL , Flags )

Create a URL moniker from a full url or partial url and base moniker

#### Parameters

- Context : PyIMoniker

 An IMoniker interface to be used as a base with a partial URL, can be None

- URL : PyUNICODE

 Full or partial url for which to create a moniker

- Flags=URL_MK_UNIFORM : int

 URL_MK_UNIFORM or URL_MK_LEGACY

#### Win32 API References

- Search for CreateURLMonikerEx at [msdn](https://learn.microsoft.com/en-ca/search/?terms=CreateURLMonikerEx), [google](https://www.google.com/search?q=CreateURLMonikerEx) or [google groups](https://groups.google.com/groups?q=CreateURLMonikerEx).


---

<!-- page: pythoncom__DoDragDrop_meth.html -->

## pythoncom.DoDragDrop

 DoDragDrop()

Carries out an OLE drag and drop operation.


---

<!-- page: pythoncom__EnableQuitMessage_meth.html -->

## pythoncom.EnableQuitMessage

 EnableQuitMessage(threadId)

Indicates the thread PythonCOM should post a WM_QUIT message to.

#### Parameters

- threadId : int

 The thread ID.


---

<!-- page: pythoncom__FUNCDESC_meth.html -->

## pythoncom.FUNCDESC

 FUNCDESC = FUNCDESC()

Creates a new FUNCDESC object


---

<!-- page: pythoncom__FmtIdToPropStgName_meth.html -->

## pythoncom.FmtIdToPropStgName

 PyUNICODE = FmtIdToPropStgName(fmtid)

Converts a FMTID to its stream name

#### Parameters

- fmtid : PyIID

 Format id - a property storage GUID (FMTID_* IIDs)


---

<!-- page: pythoncom__GetActiveObject_meth.html -->

## pythoncom.GetActiveObject

 PyIUnknown = GetActiveObject(cls)

Retrieves an object representing a running object registered with OLE

#### Parameters

- cls : CLSID

 The IID for the program. As for all CLSID's in Python, a "program.name" or IID format string may be used, or a real PyIID object.


---

<!-- page: pythoncom__GetClassFile_meth.html -->

## pythoncom.GetClassFile

 PyIID = GetClassFile(fileName)

Supplies the CLSID associated with the given filename.

#### Parameters

- fileName : str

 The filename for which you are requesting the associated CLSID.


---

<!-- page: pythoncom__GetFacilityString_meth.html -->

## pythoncom.GetFacilityString

 string = GetFacilityString(scode)

Returns the facility string, given an OLE scode.

#### Parameters

- scode : int

 The OLE error code for the facility string requested.


---

<!-- page: pythoncom__GetRecordFromGuids_meth.html -->

## pythoncom.GetRecordFromGuids

 PyRecord = GetRecordFromGuids(iid, verMajor , verMinor , lcid , infoIID , data )

Creates a new record object from the given GUIDs

#### Parameters

- iid : PyIID

 The GUID of the type library

- verMajor : int

 The major version number of the type lib.

- verMinor : int

 The minor version number of the type lib.

- lcid : int

 The LCID of the type lib.

- infoIID : PyIID

 The GUID of the record info in the library

- data=None : string or buffer

 The raw data to initialize the record with.


---

<!-- page: pythoncom__GetRecordFromTypeInfo_meth.html -->

## pythoncom.GetRecordFromTypeInfo

 PyRecord = GetRecordFromTypeInfo(TypeInfo, data )

Creates a new record object from a PyITypeInfo interface

#### Parameters

- TypeInfo : PyITypeInfo

 The type information to be converted into a PyRecord object

- data=None : string or buffer

 The raw data to initialize the record with.

#### Comments

 This function will fail if the specified type info does not have a guid defined


---

<!-- page: pythoncom__GetRunningObjectTable_meth.html -->

## pythoncom.GetRunningObjectTable

 PyIRunningObjectTable = GetRunningObjectTable(reserved)

Creates a new PyIRunningObjectTable object.

#### Parameters

- reserved=0 : int

 A reserved parameter. Should be zero unless you have inside information that I don't!


---

<!-- page: pythoncom__GetScodeRangeString_meth.html -->

## pythoncom.GetScodeRangeString

 string = GetScodeRangeString(scode)

Returns the scode range string, given an OLE scode.

#### Parameters

- scode : int

 An OLE error code to return the scode range string for.


---

<!-- page: pythoncom__GetScodeString_meth.html -->

## pythoncom.GetScodeString

 string = GetScodeString(scode)

Returns the string for an OLE scode (HRESULT)

#### Parameters

- scode : int

 The OLE error code for the scode string requested.

#### Comments

 This will obtain the COM Error message for a given HRESULT. Internally, PythonCOM uses this function to obtain the description when a com_error COM Exception is raised.


---

<!-- page: pythoncom__GetSeverityString_meth.html -->

## pythoncom.GetSeverityString

 string = GetSeverityString(scode)

Returns the severity string, given an OLE scode.

#### Parameters

- scode : int

 The OLE error code for the severity string requested.


---

<!-- page: pythoncom__IsGatewayRegistered_meth.html -->

## pythoncom.IsGatewayRegistered

 int = IsGatewayRegistered(iid)

Returns true if a gateway has been registered for the given IID

#### Parameters

- iid : PyIID

 IID of the interface.


---

<!-- page: pythoncom__LoadRegTypeLib_meth.html -->

## pythoncom.LoadRegTypeLib

 PyITypeLib = LoadRegTypeLib(iid, versionMajor , versionMinor , lcid )

Loads a registered type library.

#### Parameters

- iid : PyIID

 The IID of the type library.

- versionMajor : int

 The major version number of the library

- versionMinor : int

 The minor version number of the library

- lcid=LOCALE_USER_DEFAULT : int

 The locale ID to use.

#### Comments

 LoadRegTypeLib compares the requested version numbers against those found in the system registry, and takes one of the following actions:
 If one of the registered libraries exactly matches both the requested major and minor version numbers, then that type library is loaded.
 If one or more registered type libraries exactly match the requested major version number, and has a greater minor version number than that requested, the one with the greatest minor version number is loaded.
 If none of the registered type libraries exactly match the requested major version number (or if none of those that do exactly match the major version number also have a minor version number greater than or equal to the requested minor version number), then LoadRegTypeLib returns an error.


---

<!-- page: pythoncom__LoadTypeLib_meth.html -->

## pythoncom.LoadTypeLib

 PyITypeLib = LoadTypeLib(libFileName)

Loads a registered type library.

#### Parameters

- libFileName : string

 The path to the file containing the type information.


---

<!-- page: pythoncom__MakePyFactory_meth.html -->

## pythoncom.MakePyFactory

 PyIClassFactory = MakePyFactory(iid)

Creates a new PyIClassFactory object wrapping a PythonCOM Class Factory object.

#### Parameters

- iid : PyIID

 The IID of the object the class factory provides.


---

<!-- page: pythoncom__MkParseDisplayName_meth.html -->

## pythoncom.MkParseDisplayName

 PyIMoniker,int,PyIBindCtx = MkParseDisplayName(displayName, bindCtx )

Parses a moniker display name into a moniker object. The inverse of PyIMoniker::GetDisplayName

#### Parameters

- displayName : string

 The display name to parse

- bindCtx=None : PyIBindCtx

 The bind context object to use.

#### Comments

 If a binding context is not provided, then one will be created. Any binding context created or passed in will be returned to the caller.


---

<!-- page: pythoncom__ObjectFromAddress_meth.html -->

## pythoncom.ObjectFromAddress

 PyIUnknown = ObjectFromAddress(address, iid )

Returns a COM object given its address in memory.

#### Parameters

- address : int

 The address which holds a COM object

- iid=IUnknown : PyIID

 The IID to query

#### Return Value

This method is useful for applications which return objects via non-standard mechanisms - eg, Windows Explorer allows you to send a specific message to the explorer window and the result will be the address of an object Explorer implements. This method allows you to recover the object from that address.


---

<!-- page: pythoncom__ObjectFromLresult_meth.html -->

## pythoncom.ObjectFromLresult

 PyIUnknown = ObjectFromLresult(lresult, iid , wparm )

Retrieves a requested interface pointer for an object based on a previously generated object reference.

#### Parameters

- lresult : int

- iid : PyIID

 The IID to query

- wparm : int


---

<!-- page: pythoncom__OleFlushClipboard_meth.html -->

## pythoncom.OleFlushClipboard

 OleFlushClipboard()

Carries out the clipboard shutdown sequence. It also releases the IDataObject pointer that was placed on the clipboard by the pythoncom::OleSetClipboard function.


---

<!-- page: pythoncom__OleGetClipboard_meth.html -->

## pythoncom.OleGetClipboard

 PyIDataObject = OleGetClipboard()

Retrieves a data object that you can use to access the contents of the clipboard.


---

<!-- page: pythoncom__OleInitialize_meth.html -->

## pythoncom.OleInitialize

 OleInitialize()

Calls OleInitialized - this should rarely be needed, although some clipboard operations insist this is called rather than pythoncom::CoInitialize


---

<!-- page: pythoncom__OleIsCurrentClipboard_meth.html -->

## pythoncom.OleIsCurrentClipboard

 true/false = OleIsCurrentClipboard(dataObj)

Determines whether the data object pointer previously placed on the clipboard by the OleSetClipboard function is still on the clipboard.

#### Parameters

- dataObj : PyIDataObject

 The data object to check


---

<!-- page: pythoncom__OleLoadFromStream_meth.html -->

## pythoncom.OleLoadFromStream

 OleLoadFromStream(stream, iid)

Load an object from an IStream.

#### Parameters

- stream : PyIStream

 The stream to load the object from.

- iid : PyIID

 The IID if the interface to load.


---

<!-- page: pythoncom__OleLoad_meth.html -->

## pythoncom.OleLoad

 OleLoad(storage, iid, site)

Loads into memory an object nested within a specified storage object.

#### Parameters

- storage : PyIStorage

 The storage object from which to load

- iid : PyIID

 The IID if the interface to load.

- site : PyIOleClientSite

 The client site for the object.


---

<!-- page: pythoncom__OleSaveToStream_meth.html -->

## pythoncom.OleSaveToStream

 OleSaveToStream(persist, stream)

Save an object to an IStream.

#### Parameters

- persist : PyIPersistStream

 The object to save

- stream : PyIStream

 The stream to save the object to.


---

<!-- page: pythoncom__OleSetClipboard_meth.html -->

## pythoncom.OleSetClipboard

 OleSetClipboard(dataObj)

Places a pointer to a specific data object onto the clipboard. This makes the data object accessible to the OleGetClipboard function.

#### Parameters

- dataObj : PyIDataObject

 The data object to place on the clipboard. This parameter can be None in which case the clipboard is emptied.


---

<!-- page: pythoncom__ProgIDFromCLSID_meth.html -->

## pythoncom.ProgIDFromCLSID

 string = ProgIDFromCLSID(clsid)

Converts a CLSID to a progID.

#### Parameters

- clsid : IID

 A CLSID (either in a string, or in an PyIID object)


---

<!-- page: pythoncom__PropStgNameToFmtId_meth.html -->

## pythoncom.PropStgNameToFmtId

 PyIID = PropStgNameToFmtId(Name)

Converts a property set name to its format id (GUID)

#### Parameters

- Name : string/unicode

 Storage stream name


---

<!-- page: pythoncom__PumpMessages_meth.html -->

## pythoncom.PumpMessages

 PumpMessages()

Pumps all messages for the current thread until a WM_QUIT message.


---

<!-- page: pythoncom__PumpWaitingMessages_meth.html -->

## pythoncom.PumpWaitingMessages

 int = PumpWaitingMessages()

Pumps all waiting messages for the current thread.

#### Comments

 It is sometimes necessary for a COM thread to have a message loop. This function can be used with win32event::MsgWaitForMultipleObjects to pump all messages when necessary. Please see the COM documentation for more details.

#### Win32 API References

- Search for PeekMessage and DispatchMessage at [msdn](https://learn.microsoft.com/en-ca/search/?terms=PeekMessage and DispatchMessage), [google](https://www.google.com/search?q=PeekMessage and DispatchMessage) or [google groups](https://groups.google.com/groups?q=PeekMessage and DispatchMessage).

#### Return Value

Returns 1 if a WM_QUIT message was received, else 0


---

<!-- page: pythoncom__QueryPathOfRegTypeLib_meth.html -->

## pythoncom.QueryPathOfRegTypeLib

 PyUnicode = QueryPathOfRegTypeLib(iid, versionMajor , versionMinor , lcid )

Retrieves the path of a registered type library.

#### Parameters

- iid : PyIID

 The IID of the type library.

- versionMajor : int

 The major version number of the library

- versionMinor : int

 The minor version number of the library

- lcid=LOCALE_USER_DEFAULT : int

 The locale ID to use.


---

<!-- page: pythoncom__ReadClassStg_meth.html -->

## pythoncom.ReadClassStg

 PyIID = ReadClassStg(storage)

Reads a CLSID from a storage object.

#### Parameters

- storage : PyIStorage

 The storage to read the CLSID from.


---

<!-- page: pythoncom__ReadClassStm_meth.html -->

## pythoncom.ReadClassStm

 PyIID = ReadClassStm(Stm)

Retrieves the CLSID from a stream

#### Parameters

- Stm : PyIStream

 An IStream interface


---

<!-- page: pythoncom__RegisterActiveObject_meth.html -->

## pythoncom.RegisterActiveObject

 int = RegisterActiveObject(obUnknown, clsid , flags )

Register an object as the active object for its class

#### Parameters

- obUnknown : PyIUnknown

 The object to register.

- clsid : PyIID

 The CLSID for the object

- flags : int

 Flags to use.

#### Return Value

The result is a handle which should be pass to pythoncom::RevokeActiveObject


---

<!-- page: pythoncom__RegisterDragDrop_meth.html -->

## pythoncom.RegisterDragDrop

 RegisterDragDrop(hwnd, dropTarget)

Registers the specified window as one that can be the target of an OLE drag-and-drop operation and specifies the PyIDropTarget instance to use for drop operations.

#### Parameters

- hwnd : PyHANDLE

 Handle to a window

- dropTarget : PyIDropTarget

 Object that implements the IDropTarget interface


---

<!-- page: pythoncom__RegisterTypeLib_meth.html -->

## pythoncom.RegisterTypeLib

 RegisterTypeLib(typelib, fullPath, helpDir, lcid)

Adds information about a type library to the system registry.

#### Parameters

- typelib : PyITypeLib

 The type library being registered.

- fullPath : string

 Fully qualified path specification for the type library being registered

- helpDir=None : string

 Directory in which the Help file for the library being registered can be found. Can be None.

- lcid=LOCALE_USER_DEFAULT : int

 The locale ID to use.

#### Comments

 This function can be used during application initialization to register the application's type library correctly. When RegisterTypeLib is called to register a type library, both the minor and major version numbers are registered in hexadecimal.
 In addition to filling in a complete registry entry under the type library key, RegisterTypeLib adds entries for each of the dispinterfaces and Automation-compatible interfaces, including dual interfaces. This information is required to create instances of these interfaces. Coclasses are not registered (that is, RegisterTypeLib does not write any values to the CLSID key of the coclass).


---

<!-- page: pythoncom__RevokeActiveObject_meth.html -->

## pythoncom.RevokeActiveObject

 RevokeActiveObject(handle)

Ends an object's status as active.

#### Parameters

- handle : int

 A handle obtained from pythoncom::RegisterActiveObject


---

<!-- page: pythoncom__RevokeDragDrop_meth.html -->

## pythoncom.RevokeDragDrop

 RevokeDragDrop(hwnd)

Revokes the registration of the specified application window as a potential target for OLE drag-and-drop operations.

#### Parameters

- hwnd : PyHANDLE

 Handle to a window registered as an OLE drop target.


---

<!-- page: pythoncom__STGMEDIUM_meth.html -->

## pythoncom.STGMEDIUM

 PySTGMEDIUM = STGMEDIUM()

Creates a new STGMEDIUM object


---

<!-- page: pythoncom__StgCreateDocfileOnILockBytes_meth.html -->

## pythoncom.StgCreateDocfileOnILockBytes

 PyIStorage = StgCreateDocfileOnILockBytes(lockBytes, mode , reserved )

Creates a new compound file storage object using the OLE-provided compound file implementation for the PyIStorage interface.

#### Parameters

- lockBytes : PyILockBytes

 The PyILockBytes interface on the underlying byte array object on which to create a compound file.

- mode : int

 Specifies the access mode used to open the storage.

- reserved=0 : int

 A reserved value


---

<!-- page: pythoncom__StgCreateDocfile_meth.html -->

## pythoncom.StgCreateDocfile

 PyIStorage = StgCreateDocfile(name, mode , reserved )

Creates a new compound file storage object using the OLE-provided compound file implementation for the PyIStorage interface.

#### Parameters

- name : string

 the path of the compound file to create. It is passed uninterpreted to the file system. This can be a relative name or None. If None, a temporary stream is created.

- mode : int

 Specifies the access mode used to open the storage.

- reserved=0 : int

 A reserved value


---

<!-- page: pythoncom__StgCreateStorageEx_meth.html -->

## pythoncom.StgCreateStorageEx

 PyIStorage = StgCreateStorageEx(Name, Mode , stgfmt , Attrs , riid , StgOptions , SecurityDescriptor )

Creates a new structured storage file or property set

#### Parameters

- Name : string

 Name of the stream or file to open

- Mode : int

 Access mode, combination of storagecon.STGM_* flags

- stgfmt : int

 Storage format, storagecon.STGFMT_*

- Attrs : int

 File flags and attributes, only used with STGFMT_DOCFILE

- riid : PyIID

 Interface id to return, IStorage or IPropertySetStorage

- StgOptions=None : dict

 Dictionary representing STGOPTIONS struct (only used with STGFMT_DOCFILE)

- SecurityDescriptor=None : PySECURITY_DESCRIPTOR

 Specifies security for the new file. Must be None on Windows XP.

#### Comments

 Accepts keyword args


---

<!-- page: pythoncom__StgIsStorageFile_meth.html -->

## pythoncom.StgIsStorageFile

 int = StgIsStorageFile(name)

Indicates whether a particular disk file contains a storage object.

#### Parameters

- name : string

 The path to the file to check.

#### Return Value

The return value is 1 if a storage file, else 0. This method will also raise com_error if the StgIsStorageFile function returns a failure HRESULT.


---

<!-- page: pythoncom__StgOpenStorageEx_meth.html -->

## pythoncom.StgOpenStorageEx

 PyIStorage = StgOpenStorageEx(Name, Mode , stgfmt , Attrs , riid , StgOptions )

Advanced version of StgOpenStorage

#### Parameters

- Name : string

 Name of the stream or file to open

- Mode : int

 Access mode, combination of storagecon.STGM_* flags

- stgfmt : int

 Storage format (STGFMT_STORAGE,STGFMT_FILE,STGFMT_ANY, or STGFMT_DOCFILE)

- Attrs : int

 File flags and attributes, only used with STGFMT_DOCFILE

- riid : PyIID

 Interface id to return, IStorage or IPropertySetStorage

- StgOptions=None : dict

 Dictionary representing STGOPTIONS struct (only used with STGFMT_DOCFILE)

#### Comments

 Accepts keyword args


---

<!-- page: pythoncom__StgOpenStorageOnILockBytes_meth.html -->

## pythoncom.StgOpenStorageOnILockBytes

 PyIStorage = StgOpenStorageOnILockBytes(lockBytes, stgPriority , snbExclude , reserved )

Open an existing storage object that does not reside in a disk file, but instead has an underlying PyILockBytes byte array provided by the caller.

#### Parameters

- lockBytes : PyILockBytes

 The PyILockBytes interface on the underlying byte array object on which to open an existing storage object.

- stgPriority : PyIStorage

 Usually None, or another parent storage.

- snbExclude=None : object

 Not yet supported - must be None

- reserved=0 : int

 A reserved value


---

<!-- page: pythoncom__StgOpenStorage_meth.html -->

## pythoncom.StgOpenStorage

 PyIStorage = StgOpenStorage(name, other , mode , snbExclude , reserved )

Opens an existing root storage object in the file system.

#### Parameters

- name : string

 Name of the stream, or possibly None if storageOther is non None.

- other : PyIStorage

 Usually None, or another parent storage.

- mode : int

 Specifies the access mode used to open the storage. A combination of the storagecon.STGM_* constants.

- snbExclude=None : object

 Not yet supported - must be None

- reserved=0 : int

 A reserved value


---

<!-- page: pythoncom__TYPEATTR_meth.html -->

## pythoncom.TYPEATTR

 TYPEATTR = TYPEATTR()

Creates a new TYPEATTR object


---

<!-- page: pythoncom__UnRegisterTypeLib_meth.html -->

## pythoncom.UnRegisterTypeLib

 PyUnicode = UnRegisterTypeLib(iid, versionMajor , versionMinor , lcid , syskind )

Unregister a Type Library.

#### Parameters

- iid : PyIID

 The IID of the type library.

- versionMajor : int

 The major version number of the library

- versionMinor : int

 The minor version number of the library

- lcid=LOCALE_USER_DEFAULT : int

 The locale ID to use.

- syskind=SYS_WIN32 : int

 The target operating system.

#### Comments

 Removes type library information from the system registry. Use this API to allow applications to properly uninstall themselves. In-process objects typically call this API from DllUnregisterServer.


---

<!-- page: pythoncom__UnwrapObject_meth.html -->

## pythoncom.UnwrapObject

 PyIDispatch = UnwrapObject(ob)

Unwraps a Python instance in a gateway object.

#### Parameters

- ob : PyIUnknown

 The object to unwrap.

#### Comments

 If the object is not a PythonCOM object, then ValueError is raised.


---

<!-- page: pythoncom__VARDESC_meth.html -->

## pythoncom.VARDESC

 VARDESC = VARDESC()

Creates a new VARDESC object


---

<!-- page: pythoncom__WrapObject_meth.html -->

## pythoncom.WrapObject

 PyIUnknown = WrapObject(ob, gatewayIID , interfaceIID )

Wraps a Python instance in a gateway object.

#### Parameters

- ob : object

 The object to wrap.

- gatewayIID=IID_IDispatch : PyIID

 The IID of the gateway object to create (ie, the interface of the server object wrapped by the return value)

- interfaceIID=IID_IDispatch : PyIID

 The IID of the interface object to create (ie, the interface of the returned object)

#### Return Value

Note that there are 2 objects created by this call - a gateway (server) object, suitable for use by other external COM clients/hosts, as well as the returned Python interface (client) object, which maps to the new gateway.
There are some unusual cases where the 2 IID parameters will not be identical. If you need to do this, you should know exactly what you are doing, and why!


---

<!-- page: pythoncom__WriteClassStg_meth.html -->

## pythoncom.WriteClassStg

 WriteClassStg(storage, iid)

Writes a CLSID to a storage object

#### Parameters

- storage : PyIStorage

 Storage object into which CLSID will be written.

- iid : PyIID

 The IID to write


---

<!-- page: pythoncom__WriteClassStm_meth.html -->

## pythoncom.WriteClassStm

 WriteClassStm(Stm, clsid)

Writes a CLSID to a stream.

#### Parameters

- Stm : PyIStream

 An IStream interface

- clsid : PyIID

 The IID to write


---

<!-- page: pythoncom___GetGatewayCount_meth.html -->

## pythoncom._GetGatewayCount

 int = _GetGatewayCount()

Retrieves the number of gateway objects currently in existance

#### Comments

 This is the number of Python object that implement COM servers which are still alive (ie, serving a client). The only way to reduce this count is to have the process which uses these PythonCOM servers release its references.


---

<!-- page: pythoncom___GetInterfaceCount_meth.html -->

## pythoncom._GetInterfaceCount

 int = _GetInterfaceCount()

Retrieves the number of interface objects currently in existance

#### Comments

 If is occasionally a good idea to call this function before your Python program terminates. If this function returns non-zero, then you still have PythonCOM objects alive in your program (possibly in global variables).


---

<!-- page: pythoncom__dcom_prop.html -->

---

## pythoncom.dcom property

#### Data Type

 int

#### Description

 1 if the system is DCOM aware, else 0. Only Win95 without DCOM extensions should return 0

 Defined in: D:/A/PYWIN32/PYWIN32/COM/WIN32COM/SRC/PYTHONCOM.CPP


---

<!-- page: pythoncom__frozen_prop.html -->

---

## pythoncom.frozen property

#### Data Type

 int

#### Description

 `pythoncom.frozen` used to expose `Py_FrozenFlag` from the C API. `Py_FrozenFlag` is deprecated since Python 3.12. Ever since pywin32 b200, loading the `win32com` module has silently been replacing `pythoncom.frozen` with `sys.frozen`. Use `getattr(sys, "frozen", False)` directly instead.

 Defined in: D:/A/PYWIN32/PYWIN32/COM/WIN32COM/SRC/PYTHONCOM.CPP


---

<!-- page: pythoncom__new_meth.html -->

## pythoncom.new

 PyIDispatch = new(cls)

Create a new instance of an OLE automation server.

#### Parameters

- cls : CLSID

 An identifier for the program. Usually "program.item"

#### Comments

 This is just a wrapper for the CoCreateInstance method. Specifically, this call is identical to:
pythoncom.CoCreateInstance(cls, None, pythoncom.CLSCTX_SERVER, pythoncom.IID_IDispatch)
