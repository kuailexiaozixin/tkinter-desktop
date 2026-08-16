# 模块 win32uiole

> 来源：https://mhammond.github.io/pywin32/win32uiole.html （及其成员页，已全部内联）

## Module win32uiole

 A module, encapsulating the Microsoft Foundation Classes OLE functionality.

#### Methods

- AfxOleInit

- CreateInsertDialog

 Creates a InsertObject dialog.

- CreateOleClientItem

 Creates a PyCOleClientItem object.

- CreateOleDocument

 Creates a PyCOleDocument object.

- DaoGetEngine

- GetIDispatchForWindow

 Gets an OCX IDispatch pointer, if the window has one!

- OleGetUserCtrl

 Retrieves the current user-control flag.

- OleSetUserCtrl

 Sets the current user-control flag.

- SetMessagePendingDelay

- EnableNotRespondingDialog

- EnableNotRespondingDialog


---

# win32uiole 成员详细文档（共 11 项）


---

<!-- page: win32uiole__AfxOleInit_meth.html -->

## win32uiole.AfxOleInit

 AfxOleInit(enabled)

#### Parameters

- enabled : bool


---

<!-- page: win32uiole__CreateInsertDialog_meth.html -->

## win32uiole.CreateInsertDialog

 PyCOleInsertDialog = CreateInsertDialog()

Creates a InsertObject dialog. self*/, PyObject *args)


---

<!-- page: win32uiole__CreateOleClientItem_meth.html -->

## win32uiole.CreateOleClientItem

 PyCOleClientItem = CreateOleClientItem()

Creates a PyCOleClientItem object.


---

<!-- page: win32uiole__CreateOleDocument_meth.html -->

## win32uiole.CreateOleDocument

 PyCOleDocument = CreateOleDocument(template, fileName )

Creates an OLE document.

#### Parameters

- template : PyCDocTemplate

 The template to be attached to this document.

- fileName=None : string

 The filename for the document.


---

<!-- page: win32uiole__DaoGetEngine_meth.html -->

## win32uiole.DaoGetEngine

 PyIDispatch = DaoGetEngine()


---

<!-- page: win32uiole__EnableBusyDialog_meth.html -->

## win32uiole.EnableBusyDialog

 EnableBusyDialog(enabled)

#### Parameters

- enabled : bool


---

<!-- page: win32uiole__EnableNotRespondingDialog_meth.html -->

## win32uiole.EnableNotRespondingDialog

 EnableNotRespondingDialog(enabled)

#### Parameters

- enabled : bool


---

<!-- page: win32uiole__GetIDispatchForWindow_meth.html -->

## win32uiole.GetIDispatchForWindow

 PyIDispatch = GetIDispatchForWindow()

Gets an OCX IDispatch pointer, if the window has one!


---

<!-- page: win32uiole__OleGetUserCtrl_meth.html -->

## win32uiole.OleGetUserCtrl

 int = OleGetUserCtrl()

Returns the application name.


---

<!-- page: win32uiole__OleSetUserCtrl_meth.html -->

## win32uiole.OleSetUserCtrl

 int = OleSetUserCtrl(bUserCtrl)

Sets or clears the user control flag.

#### Parameters

- bUserCtrl : int

 Specifies whether the user-control flag is to be set or cleared.


---

<!-- page: win32uiole__SetMessagePendingDelay_meth.html -->

## win32uiole.SetMessagePendingDelay

 SetMessagePendingDelay(delay)

#### Parameters

- delay : int
