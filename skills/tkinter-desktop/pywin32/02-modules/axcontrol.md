# 模块 axcontrol

> 来源：https://mhammond.github.io/pywin32/axcontrol.html （及其成员页，已全部内联）

## Module axcontrol

 A module, encapsulating the ActiveX Control interfaces

#### Methods

- OleCreate

 Creates a new embedded object identified by a CLSID.

- OleLoadPicture

 Creates a new picture object and initializes it from the contents of a stream.

- OleLoadPicturePath

 Creates a new picture object and initializes it from the contents of a stream.

- OleSetContainedObject

 Notifies an object embedded in an OLE container to ensure correct reference.

- OleTranslateAccelerator

 Called by the object application, allows an object's container to translate accelerators according to the container's accelerator table.


---

# axcontrol 成员详细文档（共 5 项）


---

<!-- page: axcontrol__OleCreate_meth.html -->

## axcontrol.OleCreate

 PyIOleObject = OleCreate(clsid, clsid , obCLSID , obIID , renderopt , obFormatEtc , obOleClientSite , obStorage )

Creates a new embedded object identified by a CLSID.

#### Parameters

- clsid : IID

 A CLSID in string or native format

- clsid : IID

 A IID in string or native format

- obCLSID : PyIID

 The PyIID CLSID for the OLE object to create.

- obIID : PyIID

 The PyIID for the interface to return.

- renderopt : DWORD

 The DWORD renderopt for redering the Display.

- obFormatEtc : FORMATETC

 The FORMATETC structure.

- obOleClientSite : PyIOleClientSite

 The PyIOleClientSite interface to the container.

- obStorage : PyIStorage

 The PyIStorage interface.


---

<!-- page: axcontrol__OleLoadPicturePath_meth.html -->

## axcontrol.OleLoadPicturePath

 PyIUnknown = OleLoadPicturePath(url_or_path, unk , reserved , clr , , )

Creates a new picture object and initializes it from the contents of a stream.

#### Parameters

- url_or_path : string/unicode

 The path or url to the file you want to open.

- unk : PyIUknown

 The IUnknown for COM aggregation.

- reserved : int

 reserved

- clr : int

 The color you want to reserve to be transparent.

- =iid : PyIID

 The identifier of the interface describing the type of interface pointer to return

- =iidRet : PyIID

 The IID to use for the return object - use only if pythoncom does not support the native interface requested.


---

<!-- page: axcontrol__OleLoadPicture_meth.html -->

## axcontrol.OleLoadPicture

 PyIUnknown = OleLoadPicture(stream, size , runMode , , )

Creates a new picture object and initializes it from the contents of a stream.

#### Parameters

- stream : PyIStream

 The stream that contains picture's data.

- size : int

 Number of bytes read from the stream

- runMode : int

 The opposite of the initial value of the KeepOriginalFormat property. If TRUE, KeepOriginalFormat is set to FALSE and vice-versa.

- =iid : PyIID

 The identifier of the interface describing the type of interface pointer to return

- =iidRet : PyIID

 The IID to use for the return object - use only if pythoncom does not support the native interface requested.


---

<!-- page: axcontrol__OleSetContainedObject_meth.html -->

## axcontrol.OleSetContainedObject

 OleSetContainedObject(unk, fContained)

Notifies an object embedded in an OLE container to ensure correct reference.

#### Parameters

- unk : PyIUnknown

 The object

- fContained : int


---

<!-- page: axcontrol__OleTranslateAccelerator_meth.html -->

## axcontrol.OleTranslateAccelerator

 OleTranslateAccelerator(frame, frame_info, msg)

Called by the object application, allows an object's container to translate accelerators according to the container's accelerator table.

#### Parameters

- frame : PyIOleInPlaceFrame

 frame to send keystrokes to.

- frame_info : PyOLEINPLACEFRAMEINFO

- msg : PyMSG
