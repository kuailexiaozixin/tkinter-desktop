# pywin32 对象文档 · 分卷 P

> 共 3 个对象，来源 https://mhammond.github.io/pywin32/<Object>.html


---

<!-- object: PARAFORMAT -->


<!-- page: PARAFORMAT.html -->

---

## PARAFORMAT Object

 Describes a PARAFORMAT tuple

#### Items

- [0] int : mask

 The mask to use. Bits in this mask indicate which of the following parameters are interpreted. Must be a combination the win32con.PFM_* constants.

- [1] int : numbering

 The numbering style to use.

- [2] int : yHeight

 Reserved

- [3] int : dxStartIndent

 Indentation of the first line.

- [4] int : dxRightIndent

 Indentation from the right.

- [5] int : dxOffset

 The indent of second and subsequent lines.

- [6] int : wAlignment

 The alignment of the paragraph.

- [7] [int ,...] : tabStops

 The tabstops to use.


---

<!-- object: PRINTER_DEFAULTS -->


<!-- page: PRINTER_DEFAULTS.html -->

---

## PRINTER_DEFAULTS Object

 A dictionary representing a PRINTER_DEFAULTS structure

#### Properties

- string pDatatype
 Data type to be used for print jobs, see win32print::EnumPrintProcessorDatatypes, optional, can be None

- PyDEVMODE pDevMode
 A PyDEVMODE that specifies default printer parameters, optional, can be None

- int DesiredAccess
 An ACCESS_MASK specifying what level of access is needed, eg PRINTER_ACCESS_ADMINISTER, PRINTER_ACCESS_USE


---

<!-- object: PROPSPEC -->


<!-- page: PROPSPEC.html -->

---

## PROPSPEC Object

 Identifies a property. Can be either an int property id, or a str/unicode property name.
