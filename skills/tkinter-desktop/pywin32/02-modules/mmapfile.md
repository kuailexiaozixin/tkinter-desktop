# 模块 mmapfile

> 来源：https://mhammond.github.io/pywin32/mmapfile.html （及其成员页，已全部内联）

## Module mmapfile

 Compiled extension module that provides access to the memory mapped file API

#### Methods

- mmapfile

 Creates or opens a file mapping, and maps a view into memory


---

# mmapfile 成员详细文档（共 1 项）


---

<!-- page: mmapfile__mmapfile_meth.html -->

## mmapfile.mmapfile

 Pymmapfile = mmapfile(File, Name , MaximumSize , FileOffset , NumberOfBytesToMap )

Creates or opens a memory mapped file. This method uses the following API functions: CreateFileMapping, MapViewOfFile, VirtualQuery

#### Parameters

- File : str

 Name of file. Use None or '' when opening an existing named mapping, or to use system pagefile.

- Name : str

 Name of mapping object to create or open, can be None

- MaximumSize=0 : int

 Size of file mapping to create, should be specified as a multiple of system page size (see win32api::GetSystemInfo). Defaults to size of existing file if 0. If an existing named mapping is opened, the returned object will have the same size as the original mapping.

- FileOffset=0 : int

 Offset into the file at which to create view. This should be specified as a multiple of system allocation granularity. (see win32api::GetSystemInfo)

- NumberOfBytesToMap=0 : int

 Size of view to create, also a multiple of system page size. If 0, view will span from offset to end of file mapping.

#### Comments

 Accepts keyword args.

#### Win32 API References

- Search for CreateFileMapping at [msdn](https://learn.microsoft.com/en-ca/search/?terms=CreateFileMapping), [google](https://www.google.com/search?q=CreateFileMapping) or [google groups](https://groups.google.com/groups?q=CreateFileMapping).

- Search for MapViewOfFile at [msdn](https://learn.microsoft.com/en-ca/search/?terms=MapViewOfFile), [google](https://www.google.com/search?q=MapViewOfFile) or [google groups](https://groups.google.com/groups?q=MapViewOfFile).

- Search for VirtualQuery at [msdn](https://learn.microsoft.com/en-ca/search/?terms=VirtualQuery), [google](https://www.google.com/search?q=VirtualQuery) or [google groups](https://groups.google.com/groups?q=VirtualQuery).
