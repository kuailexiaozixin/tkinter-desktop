# 模块 directsound

> 来源：https://mhammond.github.io/pywin32/directsound.html （及其成员页，已全部内联）

## Module directsound

 A module encapsulating the DirectSound interfaces. See DirectSound examples for a quick overview.

#### Methods

- DirectSoundCreate

 Creates and initializes a new object that supports the IDirectSound interface.

- DirectSoundEnumerate

 The DirectSoundEnumerate function enumerates the DirectSound drivers installed in the system.

- DirectSoundCaptureCreate

 The DirectSoundCaptureCreate function creates and initializes an object that supports the IDirectSoundCapture interface.

- DirectSoundCaptureEnumerate

 The DirectSoundCaptureEnumerate function enumerates the DirectSoundCapture objects installed in the system.

- DSCAPS

 Creates a new PyDSCAPS object.

- DSBCAPS

 Creates a new PyDSBCAPS object.

- DSCCAPS

 Creates a new PyDSCCAPS object.

- DSCBCAPS

 Creates a new PyDSCBCAPS object.

- DSBUFFERDESC

 Creates a new PyDSBUFFERDESC object.

- DSCBUFFERDESC

 Creates a new PyDSCBUFFERDESC object.


---

# directsound 成员详细文档（共 10 项）


---

<!-- page: directsound__DSBCAPS_meth.html -->

## directsound.DSBCAPS

 PyDSBCAPS = DSBCAPS()

Creates a new PyDSBCAPS object


---

<!-- page: directsound__DSBUFFERDESC_meth.html -->

## directsound.DSBUFFERDESC

 PyDSBUFFERDESC = DSBUFFERDESC()

Creates a new PyDSBUFFERDESC object


---

<!-- page: directsound__DSCAPS_meth.html -->

## directsound.DSCAPS

 PyDSCAPS = DSCAPS()

Creates a new PyDSCAPS object.


---

<!-- page: directsound__DSCBCAPS_meth.html -->

## directsound.DSCBCAPS

 PyDSCBCAPS = DSCBCAPS()

Creates a new PyDSCBCAPS object


---

<!-- page: directsound__DSCBUFFERDESC_meth.html -->

## directsound.DSCBUFFERDESC

 PyDSCBUFFERDESC = DSCBUFFERDESC()

Creates a new PyDSCBUFFERDESC object


---

<!-- page: directsound__DSCCAPS_meth.html -->

## directsound.DSCCAPS

 PyDSCCAPS = DSCCAPS()

Creates a new PyDSCCAPS object


---

<!-- page: directsound__DirectSoundCaptureCreate_meth.html -->

## directsound.DirectSoundCaptureCreate

 PyIUnknown = DirectSoundCaptureCreate(guid, unk )

Creates and initializes a new object that supports the IDirectSoundCapture interface.

#### Parameters

- guid=None : PyIID

 Address of the GUID that identifies the sound device. The value of this parameter must be one of the GUIDs returned by DirectSoundCaptureEnumerate, or None for the default device.

- unk=None : PyIUknown

 The IUnknown for COM aggregation.


---

<!-- page: directsound__DirectSoundCaptureEnumerate_meth.html -->

## directsound.DirectSoundCaptureEnumerate

 list = DirectSoundCaptureEnumerate()

Enumerates DirectSoundCapture drivers installed in the system.


---

<!-- page: directsound__DirectSoundCreate_meth.html -->

## directsound.DirectSoundCreate

 PyIUnknown = DirectSoundCreate(guid, unk )

Creates and initializes a new object that supports the IDirectSound interface.

#### Parameters

- guid=None : PyIID

 Address of the GUID that identifies the sound device. The value of this parameter must be one of the GUIDs returned by DirectSoundEnumerate, or None for the default device.

- unk=None : PyIUknown

 The IUnknown for COM aggregation.


---

<!-- page: directsound__DirectSoundEnumerate_meth.html -->

## directsound.DirectSoundEnumerate

 list = DirectSoundEnumerate()

Enumerates DirectSound drivers installed in the system.
