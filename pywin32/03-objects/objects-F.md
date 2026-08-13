# pywin32 对象文档 · 分卷 F

> 共 2 个对象，来源 https://mhammond.github.io/pywin32/<Object>.html


---

<!-- object: FORM_INFO_1 -->


<!-- page: FORM_INFO_1.html -->

---

## FORM_INFO_1 Object

 A dictionary containing FORM_INFO_1W data

#### Properties

- int Flags
 FORM_USER, FORM_BUILTIN, or FORM_PRINTER

- PyUnicode Name
 Name of form

- dict Size
 A dictionary representing a SIZEL structure {'cx':int,'cy':int}

- dict ImageableArea
 A dictionary representing a RECTL structure {'left':int, 'top':int, 'right':int, 'bottom':int}


---

<!-- object: FUNCDESC -->


<!-- page: FUNCDESC.html -->

---

## FUNCDESC Object

 A FUNCDESC object represents a COM TYPEATTR structure.

#### Properties

- integer memid

- (int, ...) scodeArray

- (ELEMDESC, ...) args

- int funckind

- int invkind

- int callconv

- int cParamsOpt

- int oVft

- ELEMDESC rettype

- int wFuncFlags

- int desckind
 Always DESCKIND_FUNCDESC

#### Items

- [0] int : memid

- [1] (int, ...) : scodeArray

- [2] (ELEMDESC, ...) : args

- [3] int : funckind

- [4] int : invkind

- [5] int : callconv

- [6] int : cParamsOpt

- [7] int : oVft

- [8] ELEMDESC : rettype

- [9] int : wFuncFlags
