# com/win32com/HTML/COM_Records.html

> 来源：https://github.com/mhammond/pywin32/blob/main/com/win32com/HTML/COM_Records.html
> （该文档在 mhammond.github.io 文档站已 404，仅仓库内存在，此处为全文转录）

## COM Record support in pywin32

The pywin32 package provides COM Record support for late-bound and early-bound objects. In both cases it is required that the Type Library which defines the COM Record has been registered in Windows.

### Late-bound objects

For late-bound objects, were makepy-support is not available, it is possible to create a particular COM Record if the following is known:

- GUID of the Type Library were the Record is defined
- Major version of the registered Type Library
- Minor version of the registered Type Library
- LCID of the registered Type Library
- GUID of the COM Record in this Type Library

An instance of the COM Record is created with `pythoncom.GetRecordFromGuids`, e.g.:

```


```
import pythoncom
PyCOMTestLib_GUID = '{6bcdcb60-5605-11d0-ae5f-cadd4c000000}'
MAJVER = 1
MINVER = 1
LCID = 0
TestStruct1_GUID = '{7a4ce6a7-7959-4e85-a3c0-b41442ff0f67}'
record1 = pythoncom.GetRecordFromGuids(PyCOMTestLib_GUID, MAJVER, MINVER, LCID, TestStruct1_GUID)
```


```

The Python type of the returned COM Record instance is:

```


```
>>> type(record1)
 <class 'com_record'>
```


```

which is a generic type that is returned for all COM Records, i.e. COM Records with different GUIDs nevertheless all have the same Python type `pythoncom.com_record`.

Instances of `<class 'com_record'>` can be used as method parameters and are returned by COM methods that return a COM Record. However, it is not possible to differentiate the COM Record Types, i.e. COM Records of different GUID at runtime.

### Early-bound objects

The availability of makepy-support does in its basic form offer the convenience function `win32com.client.Record` to create COM Record instances using the COM Record name from the Type Library and an interface object of the same Type Library:

```


```
import win32com.client
com_test = win32com.client.Dispatch("PyCOMTest.PyCOMTest")
record1 = win32com.client.Record('TestStruct1' ,com_test)
```


```

Still the Python type of the returned COM Record instance is:

```


```
>>> type(record1)
 <class 'com_record'>
```


```

i.e. the generic base type of all COM Records.

#### Defining subclasses of `pythoncom.com_record`

It is possible to create subclasses of the base `pythoncom.com_record` type and register such a subclass for a particular COM Record type. As a prerequisite, it is mandatory for the subclass to define the following class attributes:

- TLBID : The GUID of the containing TypeLibrary as a string
- MJVER : The major version number of the TypeLibrary as an integer
- MNVER : The minor version number of the TypeLibrary as an integer
- LCID : The LCID of the TypeLibrary as an integer
- GUID : The GUID of the COM Record as a string

with GUID strings in {xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx} notation, e.g.:

```


```
import pythoncom
class TestStruct1(pythoncom.com_record):
 TLBID = '{6bcdcb60-5605-11d0-ae5f-cadd4c000000}'
 MJVER = 1
 MNVER = 1
 LCID = 0
 GUID = '{7a4ce6a7-7959-4e85-a3c0-b41442ff0f67}'
```


```

Before this subclass can be used to create TestStruct1 instances, it has to be registered with `win32com.client.register_record_class`, e.g.:

```


```
from win32com.client import register_record_class
register_record_class(TestStruct1)
```


```

With such a class, registered for a particular COM Record type, it is possible to identify the COM Record type at runtime:

```


```
>>> record1 = TestStruct1()
>>> type(record1)
 <class 'main.TestStruct1'>
```


```

Also COM methods that return a COM Record type for which a Python class was registered as described above, will return values of the proper Python class type, e.g.:

```


```
>>> # Given the following definition in the Type Library IDL-file:
>>> # HRESULT GetStruct([out, retval]TestStruct1 *ret);
>>> retval = GetStruct()
>>> type(retval)
 <class 'main.TestStruct1'>
```


```

COM methods that return a COM Record type for which no Python class was registered will continue to return values of the generic type `pythoncom.com_record`, e.g.:

```


```
>>> # Given the following definition in the Type Library IDL-file:
>>> # HRESULT GetOtherStruct([out, retval]AnotherStruct *ret);
>>> retval = GetOtherStruct()
>>> type(retval)
 <class 'com_record'>
```


```
