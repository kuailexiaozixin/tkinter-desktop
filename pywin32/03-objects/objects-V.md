# pywin32 对象文档 · 分卷 V

> 共 1 个对象，来源 https://mhammond.github.io/pywin32/<Object>.html


---

<!-- object: VARDESC -->


<!-- page: VARDESC.html -->

---

## VARDESC Object

 A VARDESC object represents a COM VARDESC structure.

#### Properties

- int memid
 The dispid of the member

- int/object value
 A value for the variant. If PERINSTANCE then an offset into the instance, otherwise a variant converted to a Python object.

- ELEMDESC elemdescVar
 Object describing the member.

- int varFlags
 Variable flags

- int varkind
 Kind flags.

- int desckind
 Always DESCKIND_VARDESC

#### Items

- [0] int : memid

 The id of the member

- [1] int/object : value

 A value for the variant. If PERINSTANCE then an offset into the instance, otherwise a variant converted to a Python object.

- [2] ELEMDESC : elemdescVar

 Object describing the member.

- [3] int : wVarFlags

 Variable flags

- [4] int : varkind

 Kind flags.
