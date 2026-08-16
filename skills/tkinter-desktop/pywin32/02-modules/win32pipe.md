# 模块 win32pipe

> 来源：https://mhammond.github.io/pywin32/win32pipe.html （及其成员页，已全部内联）

## Module win32pipe

 An interface to the win32 pipe API's

#### Methods

- GetNamedPipeHandleState

 Determines the state of the named pipe.

- SetNamedPipeHandleState

 Sets the state of the named pipe.

- ConnectNamedPipe

 Connects to a named pipe

- TransactNamedPipe

 Combines the functions that write a message to and read a message from the specified named pipe into a single network operation.

- CallNamedPipe

 Opens and performs a transaction on a named pipe.

- CreatePipe

 Creates an anonymous pipe, and returns handles to the read and write ends of the pipe

- FdCreatePipe

 As CreatePipe but returns file descriptors

- CreateNamedPipe

 Creates an instance of a named pipe and returns a handle for subsequent pipe operations

- DisconnectNamedPipe

 Disconnects the server end of a named pipe instance from a client process.

- GetOverlappedResult

 Determines the result of the most recent call with an OVERLAPPED object.

- WaitNamedPipe

 Waits until either a time-out interval elapses or an instance of the specified named pipe is available to be connected to (that is, the pipe's server process has a pending win32pipe::ConnectNamedPipe operation on the pipe).

- GetNamedPipeInfo

 Returns pipe's flags, buffer sizes, and max instances

- PeekNamedPipe

 Copies data from a named or anonymous pipe into a buffer without removing it from the pipe. It also returns information about data in the pipe.

- GetNamedPipeClientProcessId

 Returns the process id of client that is connected to a named pipe

- GetNamedPipeServerProcessId

 Returns pid of server process that created a named pipe

- GetNamedPipeClientSessionId

 Returns the session id of client that is connected to a named pipe

- GetNamedPipeServerSessionId

 Returns session id of server process that created a named pipe

- popen

 Version of popen that works in a GUI

#### Comments

 Not implemented in py3k.

#### Methods

- popen2

 Variation on popen - returns 2 pipes

Not implemented in py3k.

#### Methods

- popen3

 Variation on popen - returns 3 pipes

Not implemented in py3k.

#### Methods

- popen4

 Like popen2, but stdout/err are combined.

Not implemented in py3k.


---

# win32pipe 成员详细文档（共 17 项）


---

<!-- page: win32pipe__CallNamedPipe_meth.html -->

## win32pipe.CallNamedPipe

 string = CallNamedPipe(pipeName, data , bufSize , timeOut )

Opens and performs a transaction on a named pipe.

#### Parameters

- pipeName : PyUNICODE

 The name of the pipe.

- data : string

 The data to write.

- bufSize : int

 The size of the result buffer to allocate for the read.

- timeOut : int

 Specifies the number of milliseconds to wait for the named pipe to be available. In addition to numeric values, the following special values can be specified.

| | Value | Meaning
| |

---

 |

---

| | win32pipe.NMPWAIT_NOWAIT | Does not wait for the named pipe. If the named pipe is not available, the function returns an error.
| | win32pipe.NMPWAIT_WAIT_FOREVER | Waits indefinitely.
| | win32pipe.NMPWAIT_USE_DEFAULT_WAIT | Uses the default time-out specified in a call to the CreateNamedPipe function.


---

<!-- page: win32pipe__ConnectNamedPipe_meth.html -->

## win32pipe.ConnectNamedPipe

 int = ConnectNamedPipe(hPipe, overlapped )

Connects to a named pipe

#### Parameters

- hPipe : PyHANDLE

 The handle to the pipe.

- overlapped=None : PyOVERLAPPED

 An overlapped object to use, else None

#### Comments

 The result is zero if the function succeeds. If the function fails, GetLastError() is called, and if the result is ERROR_IO_PENDING or ERROR_PIPE_CONNECTED (common when passing an overlapped object), this value is returned. All other error values raise a win32 exception (from which the error code can be extracted)


---

<!-- page: win32pipe__CreateNamedPipe_meth.html -->

## win32pipe.CreateNamedPipe

 PyHANDLE = CreateNamedPipe(pipeName, openMode , pipeMode , nMaxInstances , nOutBufferSize , nInBufferSize , nDefaultTimeOut , sa )

Creates an instance of a named pipe and returns a handle for subsequent pipe operations

#### Parameters

- pipeName : PyUnicode

 The name of the pipe

- openMode : int

 OpenMode of the pipe

- pipeMode : int

- nMaxInstances : int

- nOutBufferSize : int

- nInBufferSize : int

- nDefaultTimeOut : int

- sa : PySECURITY_ATTRIBUTES


---

<!-- page: win32pipe__CreatePipe_meth.html -->

## win32pipe.CreatePipe

 (PyHANDLE, PyHANDLE) = CreatePipe(sa, nSize )

Creates an anonymous pipe, and returns handles to the read and write ends of the pipe

#### Parameters

- sa : PySECURITY_ATTRIBUTES

- nSize : int


---

<!-- page: win32pipe__DisconnectNamedPipe_meth.html -->

## win32pipe.DisconnectNamedPipe

 DisconnectNamedPipe(hFile)

Disconnects the server end of a named pipe instance from a client process.

#### Parameters

- hFile : PyHANDLE

 The handle to the pipe to disconnect.


---

<!-- page: win32pipe__FdCreatePipe_meth.html -->

## win32pipe.FdCreatePipe

 (int, int) = FdCreatePipe(sa, nSize , mode )

As CreatePipe but returns file descriptors

#### Parameters

- sa : PySECURITY_ATTRIBUTES

 Specifies security and inheritance for the pipe

- nSize : int

 Buffer size for pipe. Use 0 for default size.

- mode : int

 O_TEXT or O_BINARY


---

<!-- page: win32pipe__GetNamedPipeClientProcessId_meth.html -->

## win32pipe.GetNamedPipeClientProcessId

 int = GetNamedPipeClientProcessId(hPipe)

Returns the process id of client that is connected to a named pipe

#### Parameters

- hPipe : PyHANDLE

 The handle to the pipe.


---

<!-- page: win32pipe__GetNamedPipeClientSessionId_meth.html -->

## win32pipe.GetNamedPipeClientSessionId

 int = GetNamedPipeClientSessionId(hPipe)

Returns the session id of client that is connected to a named pipe

#### Parameters

- hPipe : PyHANDLE

 The handle to the pipe.


---

<!-- page: win32pipe__GetNamedPipeHandleState_meth.html -->

## win32pipe.GetNamedPipeHandleState

 (int, int, int/None, int/None, PyUnicode = GetNamedPipeHandleState(hPipe, bGetCollectionData , bGetUserName )

Determines the state of the named pipe.

#### Parameters

- hPipe : PyHANDLE

 The handle to the pipe.

- bGetCollectionData=0 : int

 Determines if the collection data should be retrieved. If not, None is returned in their place.

- bGetUserName=0 : int

 Determines if the username should be retrieved. Works only for a server handle and if the client opened the pipe with SECURITY_IMPERSONATION access.


---

<!-- page: win32pipe__GetNamedPipeInfo_meth.html -->

## win32pipe.GetNamedPipeInfo

 (int, int, int, int) = GetNamedPipeInfo(hNamedPipe)

Returns pipe's flags, buffer sizes, and max instances

#### Parameters

- hNamedPipe : PyHANDLE

 Handle to a named pipe


---

<!-- page: win32pipe__GetNamedPipeServerProcessId_meth.html -->

## win32pipe.GetNamedPipeServerProcessId

 int = GetNamedPipeServerProcessId(hPipe)

Returns pid of server process that created a named pipe

#### Parameters

- hPipe : PyHANDLE

 The handle to the pipe.


---

<!-- page: win32pipe__GetNamedPipeServerSessionId_meth.html -->

## win32pipe.GetNamedPipeServerSessionId

 int = GetNamedPipeServerSessionId(hPipe)

Returns session id of server process that created a named pipe

#### Parameters

- hPipe : PyHANDLE

 The handle to the pipe.


---

<!-- page: win32pipe__GetOverlappedResult_meth.html -->

## win32pipe.GetOverlappedResult

 int = GetOverlappedResult(hFile, overlapped , bWait )

Determines the result of the most recent call with an OVERLAPPED object.

#### Parameters

- hFile : PyHANDLE

 The handle to the pipe or file

- overlapped : PyOVERLAPPED

 The overlapped object to check.

- bWait : int

 Indicates if the function should wait for data to become available.

#### Comments

 The result is the number of bytes transferred. The overlapped object's attributes will be changed during this call.


---

<!-- page: win32pipe__PeekNamedPipe_meth.html -->

## win32pipe.PeekNamedPipe

 (string, int, int) = PeekNamedPipe(hPipe, size )

Copies data from a named or anonymous pipe into a buffer without removing it from the pipe. It also returns information about data in the pipe.

#### Parameters

- hPipe : PyHANDLE

 The handle to the pipe.

- size : int

 The size of the buffer.


---

<!-- page: win32pipe__SetNamedPipeHandleState_meth.html -->

## win32pipe.SetNamedPipeHandleState

 SetNamedPipeHandleState(hPipe, Mode, MaxCollectionCount, CollectDataTimeout)

Sets the state of the named pipe.

#### Parameters

- hPipe : PyHANDLE

 The handle to the pipe.

- Mode : int/None

 The pipe read mode.

- MaxCollectionCount : int/None

 Maximum bytes collected before transmission to the server.

- CollectDataTimeout : int/None

 Maximum time to wait, in milliseconds, before transmission to server.


---

<!-- page: win32pipe__TransactNamedPipe_meth.html -->

## win32pipe.TransactNamedPipe

 string/buffer = TransactNamedPipe(pipeName, writeData , buffer/bufSize , overlapped )

Combines the functions that write a message to and read a message from the specified named pipe into a single network operation.

#### Parameters

- pipeName : PyUNICODE

 The name of the pipe.

- writeData : string/buffer

 The data to write to the pipe.

- buffer/bufSize : PyOVERLAPPEDReadBuffer/int

 Size of the buffer to create for the result, or a buffer to fill with the result. If a buffer object and overlapped is passed, the result is the buffer itself. If a buffer but no overlapped is passed, the result is a new string object, built from the buffer, but with a length that reflects the data actually read.

- overlapped=None : PyOVERLAPPED

 An overlapped structure or None

#### Comments

 This function is modelled on win32file::ReadFile - for overlapped operations you are expected to provide a buffer which will be filled asynchronously.


---

<!-- page: win32pipe__WaitNamedPipe_meth.html -->

## win32pipe.WaitNamedPipe

 WaitNamedPipe(pipeName, timeout)

Waits until either a time-out interval elapses or an instance of the specified named pipe is available to be connected to (that is, the pipe's server process has a pending win32pipe::ConnectNamedPipe operation on the pipe).

#### Parameters

- pipeName : PyUnicode

 The name of the pipe

- timeout : int

 The number of milliseconds the function will wait. instead of a literal value, you can specify one of the following values for the timeout:

| | Value | Meaning
| |

---

 |

---

| | NMPWAIT_USE_DEFAULT_WAIT | The time-out interval is the default value specified by the server process in the CreateNamedPipe function.
| | NMPWAIT_WAIT_FOREVER | The function does not return until an instance of the named pipe is available
