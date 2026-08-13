# 模块 win32lz

> 来源：https://mhammond.github.io/pywin32/win32lz.html （及其成员页，已全部内联）

## Module win32lz

 A module encapsulating the Windows LZ compression routines.

#### Methods

- GetExpandedName

 Retrieves the original name of an expanded file,

- Close

 Closes a handle to an LZ file.

- Copy

 Copies a source file to a destination file.

- Init

 Allocates memory for the internal data structures required to decompress files, and then creates and initializes them.

- OpenFile

 Creates, opens, reopens, or deletes the specified file.


---

# win32lz 成员详细文档（共 5 项）


---

<!-- page: win32lz__Close_meth.html -->

## win32lz.Close

 Close(handle)

Closes a handle to an LZ file.

#### Parameters

- handle : int

 The handle of the LZ file to close.

#### Win32 API References

- Search for LZClose at [msdn](https://learn.microsoft.com/en-ca/search/?terms=LZClose), [google](https://www.google.com/search?q=LZClose) or [google groups](https://groups.google.com/groups?q=LZClose).


---

<!-- page: win32lz__Copy_meth.html -->

## win32lz.Copy

 int = Copy(hSrc, hDest )

Copies a source file to a destination file.

#### Parameters

- hSrc : int

 The handle of the source file to copy.

- hDest : int

 The handle of the destination file.

#### Comments

 If the source file is compressed with the Microsoft File Compression Utility (COMPRESS.EXE), this function creates a decompressed destination file. If the source file is not compressed, this function duplicates the original file.

#### Win32 API References

- Search for LZCopy at [msdn](https://learn.microsoft.com/en-ca/search/?terms=LZCopy), [google](https://www.google.com/search?q=LZCopy) or [google groups](https://groups.google.com/groups?q=LZCopy).


---

<!-- page: win32lz__GetExpandedName_meth.html -->

## win32lz.GetExpandedName

 string = GetExpandedName(Source)

Retrieves the original name of an expanded file,

#### Parameters

- Source : str

 Name of a compressed file

#### Win32 API References

- Search for GetExpandedName at [msdn](https://learn.microsoft.com/en-ca/search/?terms=GetExpandedName), [google](https://www.google.com/search?q=GetExpandedName) or [google groups](https://groups.google.com/groups?q=GetExpandedName).


---

<!-- page: win32lz__Init_meth.html -->

## win32lz.Init

 Init(handle)

Allocates memory for the internal data structures required to decompress files, and then creates and initializes them.

#### Parameters

- handle : int

 handle of source file

#### Win32 API References

- Search for LZInit at [msdn](https://learn.microsoft.com/en-ca/search/?terms=LZInit), [google](https://www.google.com/search?q=LZInit) or [google groups](https://groups.google.com/groups?q=LZInit).


---

<!-- page: win32lz__OpenFile_meth.html -->

## win32lz.OpenFile

 int,(tuple) = OpenFile(fileName, action )

Creates, opens, reopens, or deletes the specified file.

#### Parameters

- fileName : string

 Name of file to open

- action : int

 Can be one of the wi32con.OF_ constants (OF_CREATE, OF_DELETE, etc)

#### Win32 API References

- Search for LZOpenFile at [msdn](https://learn.microsoft.com/en-ca/search/?terms=LZOpenFile), [google](https://www.google.com/search?q=LZOpenFile) or [google groups](https://groups.google.com/groups?q=LZOpenFile).
