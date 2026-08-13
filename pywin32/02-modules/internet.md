# 模块 internet

> 来源：https://mhammond.github.io/pywin32/internet.html （及其成员页，已全部内联）

## Module internet

 A module, encapsulating the ActiveX Internet interfaces

#### Methods

- CoInternetCreateSecurityManager

- CoInternetIsFeatureEnabled

- CoInternetSetFeatureEnabled


---

# internet 成员详细文档（共 3 项）


---

<!-- page: internet__CoInternetCreateSecurityManager_meth.html -->

## internet.CoInternetCreateSecurityManager

 PyIInternetSecurityManager = CoInternetCreateSecurityManager(reserved)

#### Parameters

- reserved : int


---

<!-- page: internet__CoInternetIsFeatureEnabled_meth.html -->

## internet.CoInternetIsFeatureEnabled

 bool = CoInternetIsFeatureEnabled(flags)

#### Parameters

- flags : int

#### Return Value

Returns true for S_OK, False for other non-error hresults, or raises a com_error.


---

<!-- page: internet__CoInternetSetFeatureEnabled_meth.html -->

## internet.CoInternetSetFeatureEnabled

 int = CoInternetSetFeatureEnabled(flags, enable )

#### Parameters

- flags : int

- enable : bool
