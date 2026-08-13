# 模块 servicemanager

> 来源：https://mhammond.github.io/pywin32/servicemanager.html （及其成员页，已全部内联）

## Module servicemanager

 A module that interfaces with the Windows Service Control Manager. While this module can be imported by regular Python programs, it is only useful when used by a Python program hosting a service - and even then is generally used automatically by the Python Service framework. See the pipeTestService sample for an example of using this module.
The module win32service and win32serviceutil provide other facilities for controlling and managing services.

#### Methods

- CoInitializeEx

- CoUninitialize

- RegisterServiceCtrlHandler

 Registers a function to retrieve service control notification messages.

- LogMsg

 Write an specific message to the log.

- LogInfoMsg

 Write an informational message to the log.

- LogErrorMsg

 Write an error message to the log.

- LogWarningMsg

 Logs a generic warning message to the event log

- PumpWaitingMessages

 Pumps waiting window messages for the service.

- Debugging

 Indicates if the service is running in debug mode.

- StartServiceCtrlDispatcher

 Starts the service by calling the win32 StartServiceCtrlDispatcher function.

- Initialize

- Finalize

- PrepareToHostSingle

- PrepareToHostMultiple

- RunningAsService

 Indicates if the code is running as a service.

- SetEventSourceName

 Sets the event source name for event log entries written by the service.


---

# servicemanager 成员详细文档（共 15 项）


---

<!-- page: servicemanager__CoInitializeEx_meth.html -->

## servicemanager.CoInitializeEx

 CoInitializeEx()

Initialize OLE with additional options.


---

<!-- page: servicemanager__CoUninitialize_meth.html -->

## servicemanager.CoUninitialize

 CoUninitialize()

Unitialize OLE


---

<!-- page: servicemanager__Debugging_meth.html -->

## servicemanager.Debugging

 True/False = Debugging(newVal)

Indicates if the service is running in debug mode and optionally toggles the debug flag.

#### Parameters

- newVal=-1 : int

 If not -1, a new value for the debugging flag. The result is the value of the flag before it is changed.


---

<!-- page: servicemanager__Finalize_meth.html -->

## servicemanager.Finalize

 Finalize()


---

<!-- page: servicemanager__Initialize_meth.html -->

## servicemanager.Initialize

 Initialize(eventSourceName, eventSourceFile)

Initialize the module for hosting a service. This is generally called automatically

#### Parameters

- eventSourceName=None : string

 The event source name

- eventSourceFile=None : string

 The name of the file (generally a DLL) with the event source messages.


---

<!-- page: servicemanager__LogErrorMsg_meth.html -->

## servicemanager.LogErrorMsg

 LogErrorMsg(msg)

Logs a generic error message to the event log

#### Parameters

- msg : string

 The message to write.


---

<!-- page: servicemanager__LogInfoMsg_meth.html -->

## servicemanager.LogInfoMsg

 LogInfoMsg(msg)

Logs a generic informational message to the event log

#### Parameters

- msg : string

 The message to write.


---

<!-- page: servicemanager__LogMsg_meth.html -->

## servicemanager.LogMsg

 LogMsg(errorType, eventId, inserts)

Logs a specific message

#### Parameters

- errorType : int

- eventId : int

- inserts=None : (string, )


---

<!-- page: servicemanager__LogWarningMsg_meth.html -->

## servicemanager.LogWarningMsg

 LogWarningMsg(msg)

Logs a generic warning message to the event log

#### Parameters

- msg : string

 The message to write.


---

<!-- page: servicemanager__PrepareToHostMultiple_meth.html -->

## servicemanager.PrepareToHostMultiple

 PrepareToHostMultiple(service_name, klass)

Prepare for hosting a multiple services in this EXE

#### Parameters

- service_name : string

 The name of the service hosted by the class

- klass : object

 The Python class to host.


---

<!-- page: servicemanager__PrepareToHostSingle_meth.html -->

## servicemanager.PrepareToHostSingle

 PrepareToHostSingle(klass)

Prepare for hosting a single service in this EXE

#### Parameters

- klass=None : object

 The Python class to host. If not specified, the service name is looked up in the registry and the specified class instantiated.


---

<!-- page: servicemanager__PumpWaitingMessages_meth.html -->

## servicemanager.PumpWaitingMessages

 int = PumpWaitingMessages()

Pumps all waiting messages.

#### Return Value

Returns 1 if a WM_QUIT message was received, else 0


---

<!-- page: servicemanager__RegisterServiceCtrlHandler_meth.html -->

## servicemanager.RegisterServiceCtrlHandler

 int/None = RegisterServiceCtrlHandler(serviceName, callback , extra_args )

Registers the Python service control handler function.

#### Parameters

- serviceName : string

 The name of the service. This is provided in args[0] of the service class __init__ method.

- callback : object

 The Python function that performs as the control function. This will be called with an integer status argument.

- extra_args=False : bool

 Is this callback expecting the additional 2 args passed by HandlerEx?

#### Return Value

If the service manager is in debug mode, this returns None, indicating there is no service control manager handle, otherwise the handle to the Win32 service manager.


---

<!-- page: servicemanager__RunningAsService_meth.html -->

## servicemanager.RunningAsService

 True/False = RunningAsService()

Indicates if the code is being executed as a service.


---

<!-- page: servicemanager__SetEventSourceName_meth.html -->

## servicemanager.SetEventSourceName

 SetEventSourceName(sourceName, registerNow)

Sets the event source name for event log entries written by the service.

#### Parameters

- sourceName : string

 The event source name

- registerNow=False : bool

 If True, the event source name in the registry will be updated immediately. If False, the name will be registered the first time an event log entry is written via any pythonservice methods (or possibly never if no record if written).
Note that in some cases, the service itself will not have permission to write the event source in the registry. Therefore, it would be prudent for your installation program to call this function with registerNow=True, to ensure your services can write useful entries.
