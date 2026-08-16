# 模块 adsi

> 来源：https://mhammond.github.io/pywin32/adsi.html （及其成员页，已全部内联）

## Module adsi

 A COM interface to ADSI

#### Methods

- ADsOpenObject

 Binds to an ADSI object using explicit username and password credentials.

- ADsGetObject

 Binds to an object given its path and a specified interface identifier (IID).

- ADsBuildEnumerator

 Builds an enumerator object for the specified ADSI container object.

- ADsEnumerateNext

- ADsGetLastError

- StringAsDS_SELECTION_LIST

 Unpacks a string (generally fetched via PyIDataObject::GetData) into a PyDS_SELECTION_LIST list.

- DSOP_SCOPE_INIT_INFOs

 The type object for PyDSOP_SCOPE_INIT_INFOs objects.


---

# adsi 成员详细文档（共 7 项）


---

<!-- page: adsi__ADsBuildEnumerator_meth.html -->

## adsi.ADsBuildEnumerator

 PyIEnumerator = ADsBuildEnumerator(container)

Builds an enumerator object for the specified ADSI container object.

#### Parameters

- container : PyIADsContainer


---

<!-- page: adsi__ADsEnumerateNext_meth.html -->

## adsi.ADsEnumerateNext

 PyIEnumerator = ADsEnumerateNext(enum, num )

#### Parameters

- enum : PyIEnumVARIANT

 The enumerator.

- num=1 : int

 Number of items to retrieve.

#### Return Value

The result is a tuple of Python objects converted from Variants, one for each element returned. Note that if zero elements are returned, it is not considered an error condition - an empty tuple is simply returned.


---

<!-- page: adsi__ADsGetLastError_meth.html -->

## adsi.ADsGetLastError

 (int, unicode, unicode) = ADsGetLastError()


---

<!-- page: adsi__ADsGetObject_meth.html -->

## adsi.ADsGetObject

 com_object = ADsGetObject(path, iid )

Binds to an object given its path and a specified interface identifier (IID).

#### Parameters

- path : unicode

- iid=IID_IDispatch : PyIID

 The requested interface


---

<!-- page: adsi__ADsOpenObject_meth.html -->

## adsi.ADsOpenObject

 com_object = ADsOpenObject(path, username , password , reserved , iid )

Binds to an ADSI object using explicit username and password credentials.

#### Parameters

- path : unicode

- username : unicode

- password : unicode

- reserved=0 : int

- iid=IID_IDispatch : PyIID

 The requested interface


---

<!-- page: adsi__DSOP_SCOPE_INIT_INFOs_meth.html -->

## adsi.DSOP_SCOPE_INIT_INFOs

 DSOP_SCOPE_INIT_INFOs = DSOP_SCOPE_INIT_INFOs(size)

The type object for PyDSOP_SCOPE_INIT_INFOs objects.

#### Parameters

- size : int

 The number of PyDSOP_SCOPE_INIT_INFO objects to create in the array.


---

<!-- page: adsi__StringAsDS_SELECTION_LIST_meth.html -->

## adsi.StringAsDS_SELECTION_LIST

 PyDS_SELECTION_LIST = StringAsDS_SELECTION_LIST(buf)

Unpacks a string (generally fetched via PyIDataObject::GetData) into a PyDS_SELECTION_LIST list.

#### Parameters

- buf : str

 The raw buffer
