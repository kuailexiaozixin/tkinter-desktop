# pywin32 对象文档 · 分卷 I

> 共 5 个对象，来源 https://mhammond.github.io/pywin32/<Object>.html


---

<!-- object: IDLDESC -->


<!-- page: IDLDESC.html -->

---

## IDLDESC Object

 An IDLDESC is respresented as

#### Items

- [0] int : reserved

 A reserved value!

- [1] int : flags

 IDL flags.


---

<!-- object: ImportCallback -->


<!-- page: ImportCallback.html -->

---

## ImportCallback Object

 User-defined callback function used with win32file::WriteEncryptedFileRaw
 Function is called with 3 parameters: (Data, CallbackContext, Length)
 Data: Writeable buffer to be filled with raw encrypted data. Buffer memory is only valid within the callback function.
 CallbackContext: The arbitrary object passed to WriteEncryptedFileRaw.
 Length: Size of the data buffer.
 Your implementation of this function should return a tuple of 2 ints containing an error code (ERROR_SUCCESS on success), and the length of data written to the buffer.
 Function exits when 0 is returned for the data length.


---

<!-- object: isapi.simple.SimpleExtension -->


<!-- page: isapi.simple.SimpleExtension.html -->

---

## isapi.simple.SimpleExtension Object

 Base class for a simple ISAPI extension

#### Methods

- GetExtensionVersion

 Called by the ISAPI framework to get the extension version

- HttpExtensionProc

 Called by the ISAPI framework for each extension request.

- TerminateExtension

 Called by the ISAPI framework as the extension terminates.


<!-- page: isapi.simple.SimpleExtension__GetExtensionVersion_meth.html -->

## isapi.simple.SimpleExtension.GetExtensionVersion

 GetExtensionVersion()

Called by the ISAPI framework to get the extension version

#### Comments

 The default implementation uses the classes docstring to set the extension description.


<!-- page: isapi.simple.SimpleExtension__GetExtensionVersion_meth_1.html -->

## isapi.simple.SimpleExtension.GetExtensionVersion

 GetExtensionVersion(self, vi)

Called by the ISAPI framework to get the extension version

#### Parameters

- self :

 self

- vi :

 vi

#### Comments

 The default implementation uses the classes docstring to set the extension description.


<!-- page: isapi.simple.SimpleExtension__HttpExtensionProc_meth.html -->

## isapi.simple.SimpleExtension.HttpExtensionProc

 HttpExtensionProc()

Called by the ISAPI framework for each extension request.

#### Comments

 sub-classes must provide an implementation for this method.


<!-- page: isapi.simple.SimpleExtension__HttpExtensionProc_meth_1.html -->

## isapi.simple.SimpleExtension.HttpExtensionProc

 HttpExtensionProc(self, control_block)

Called by the ISAPI framework for each extension request.

#### Parameters

- self :

 self

- control_block :

 control_block

#### Comments

 sub-classes must provide an implementation for this method.


<!-- page: isapi.simple.SimpleExtension__TerminateExtension_meth.html -->

## isapi.simple.SimpleExtension.TerminateExtension

 TerminateExtension()

Called by the ISAPI framework as the extension terminates.


<!-- page: isapi.simple.SimpleExtension__TerminateExtension_meth_1.html -->

## isapi.simple.SimpleExtension.TerminateExtension

 TerminateExtension(self, status)

Called by the ISAPI framework as the extension terminates.

#### Parameters

- self :

 self

- status :

 status


---

<!-- object: isapi.simple.SimpleFilter -->


<!-- page: isapi.simple.SimpleFilter.html -->

---

## isapi.simple.SimpleFilter Object

 Base class for a a simple ISAPI filter

#### Methods

- GetFilterVersion

 Called by the ISAPI framework to get the extension version

- HttpFilterProc

 Called by the ISAPI framework for each filter request.

- TerminateFilter

 Called by the ISAPI framework as the filter terminates.


<!-- page: isapi.simple.SimpleFilter__GetFilterVersion_meth.html -->

## isapi.simple.SimpleFilter.GetFilterVersion

 GetFilterVersion()

Called by the ISAPI framework to get the extension version

#### Comments

 The default implementation uses the classes docstring to set the extension description, and uses the classes filter_flags attribute to set the ISAPI filter flags - you must specify filter_flags in your class.


<!-- page: isapi.simple.SimpleFilter__GetFilterVersion_meth_1.html -->

## isapi.simple.SimpleFilter.GetFilterVersion

 GetFilterVersion(self, fv)

Called by the ISAPI framework to get the extension version

#### Parameters

- self :

 self

- fv :

 fv

#### Comments

 The default implementation uses the classes docstring to set the extension description, and uses the classes filter_flags attribute to set the ISAPI filter flags - you must specify filter_flags in your class.


<!-- page: isapi.simple.SimpleFilter__HttpFilterProc_meth.html -->

## isapi.simple.SimpleFilter.HttpFilterProc

 HttpFilterProc()

Called by the ISAPI framework for each filter request.

#### Comments

 sub-classes must provide an implementation for this method.


<!-- page: isapi.simple.SimpleFilter__HttpFilterProc_meth_1.html -->

## isapi.simple.SimpleFilter.HttpFilterProc

 HttpFilterProc(self, fc)

Called by the ISAPI framework for each filter request.

#### Parameters

- self :

 self

- fc :

 fc

#### Comments

 sub-classes must provide an implementation for this method.


<!-- page: isapi.simple.SimpleFilter__TerminateFilter_meth.html -->

## isapi.simple.SimpleFilter.TerminateFilter

 TerminateFilter()

Called by the ISAPI framework as the filter terminates.


<!-- page: isapi.simple.SimpleFilter__TerminateFilter_meth_1.html -->

## isapi.simple.SimpleFilter.TerminateFilter

 TerminateFilter(self, status)

Called by the ISAPI framework as the filter terminates.

#### Parameters

- self :

 self

- status :

 status


---

<!-- object: isapi.threaded_extension.ThreadPoolExtension -->


<!-- page: isapi.threaded_extension.ThreadPoolExtension.html -->

---

## isapi.threaded_extension.ThreadPoolExtension Object

 Base class for an ISAPI extension based around a thread-pool

#### Methods

- Dispatch

 Overridden by the sub-class to handle connection requests.

- HandleDispatchError

 Handles errors in the Dispatch method.


<!-- page: isapi.threaded_extension.ThreadPoolExtension__Dispatch_meth.html -->

## isapi.threaded_extension.ThreadPoolExtension.Dispatch

 Dispatch()

Overridden by the sub-class to handle connection requests.

#### Comments

 This class creates a thread-pool using a Windows completion port, and dispatches requests via this port. Sub-classes can generally implement each connection request using blocking reads and writes, and the thread-pool will still provide decent response to the end user.

 The sub-class can set a max_workers attribute (default is 20). Note that this generally does *not* mean 20 threads will all be concurrently running, via the magic of Windows completion ports.

 There is no default implementation - sub-classes must implement this.


<!-- page: isapi.threaded_extension.ThreadPoolExtension__Dispatch_meth_1.html -->

## isapi.threaded_extension.ThreadPoolExtension.Dispatch

 Dispatch(self, ecb)

Overridden by the sub-class to handle connection requests.

#### Parameters

- self :

 self

- ecb :

 ecb

#### Comments

 This class creates a thread-pool using a Windows completion port, and dispatches requests via this port. Sub-classes can generally implement each connection request using blocking reads and writes, and the thread-pool will still provide decent response to the end user.

 The sub-class can set a max_workers attribute (default is 20). Note that this generally does *not* mean 20 threads will all be concurrently running, via the magic of Windows completion ports.

 There is no default implementation - sub-classes must implement this.


<!-- page: isapi.threaded_extension.ThreadPoolExtension__HandleDispatchError_meth.html -->

## isapi.threaded_extension.ThreadPoolExtension.HandleDispatchError

 HandleDispatchError()

Handles errors in the Dispatch method.

#### Comments

 When a Dispatch method call fails, this method is called to handle the exception. The default implementation formats the traceback in the browser.


<!-- page: isapi.threaded_extension.ThreadPoolExtension__HandleDispatchError_meth_1.html -->

## isapi.threaded_extension.ThreadPoolExtension.HandleDispatchError

 HandleDispatchError(self, ecb)

Handles errors in the Dispatch method.

#### Parameters

- self :

 self

- ecb :

 ecb

#### Comments

 When a Dispatch method call fails, this method is called to handle the exception. The default implementation formats the traceback in the browser.
