# pywin32 对象文档 · 分卷 L

> 共 3 个对象，来源 https://mhammond.github.io/pywin32/<Object>.html


---

<!-- object: LARGE_INTEGER -->


<!-- page: LARGE_INTEGER.html -->

---

## LARGE_INTEGER Object

 A Python object used wherever a COM LARGE_INTEGER is used.

#### Comments

 Please see pywintypes::ULARGE_INTEGER for a description.


---

<!-- object: LV_COLUMN -->


<!-- page: LV_COLUMN.html -->

---

## LV_COLUMN Object

 A tuple that describes a Win32 LV_COLUMN tuple. Used by the PyCListCtrl object. A tuple of 4 items, being fmt, cx, pszText, iSubItem

#### Items

- [0] int : fmt

 Alignment of the column header and the subitem text in the column.

- [1] int : cx

 Width of the column.

- [2] string : text

 Column header text.

- [3] int : subItem

 Index of subitem associated with the column.
When passed to Python, will always be a tuple of size 4, and items may be None if not available.
When passed from Python, the tuple may be any length up to 4, and any item may be None.


---

<!-- object: LV_ITEM -->


<!-- page: LV_ITEM.html -->

---

## LV_ITEM Object

 Describes an LV_ITEM tuple, used by the PyCListCtrl object.

#### Items

- [0] int : item

 The item number.

- [1] int : subItem

 The sub-item number.

- [2] int : state

 The items state. If specified, the stateMask must also be specified.

- [3] int : stateMask

 A mask indicating which of the state bits are valid..

- [4] string : text

 The text for the item

- [5] int : iImage

 The image offset for the item

- [6] int : userObject

 Any integer to be associated with the item.

#### Comments

 When passed to Python, will always be a tuple of size 7, and items may be None if not available.
When passed from Python, the tuple must be at least 2 items long, and any item may be None.
userob is any Python object at all, but no reference count is kept, so you must ensure the object remains referenced throught the lists life.
