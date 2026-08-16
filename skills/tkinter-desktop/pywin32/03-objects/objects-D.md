# pywin32 对象文档 · 分卷 D

> 共 2 个对象，来源 https://mhammond.github.io/pywin32/<Object>.html


---

<!-- object: DEFCONTENTMENU -->


<!-- page: DEFCONTENTMENU.html -->

---

## DEFCONTENTMENU Object

 A tuple representing a DEFCONTEXTMENU structure.

#### Parameters

- hwnd : PyHANDLE

- callback : PyIContextMenuCB

 May be None bNoneOK */))

- pidlFolder : PIDL

 May be None

- sf : PyIShellFolder

 The Shell data source object that is the parent of the child items specified in children. If parent is specified, this parameter can be NULL. bNoneOK */))

- children : [PIDL , ...]

- unkAssocInfo : PyIUnknown

 May be None


---

<!-- object: DOCINFO -->


<!-- page: DOCINFO.html -->

---

## DOCINFO Object

 A tuple of information representing a DOCINFO struct

#### Properties

- string/PyUnicode DocName
 Name of document

- string/PyUnicode Output
 Name of output file when printing to file. Use None for normal printing.

- string/PyUnicode DataType
 Type of data to be sent to printer, eg RAW, EMF, TEXT. Use None for printer default.

- int Type
 Flag specifying mode of operation. Can be DI_APPBANDING, DI_ROPS_READ_DESTINATION, or 0
