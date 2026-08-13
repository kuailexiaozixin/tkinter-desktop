# 模块 win32file

> 来源：https://mhammond.github.io/pywin32/win32file.html （及其成员页，已全部内联）

## Module win32file

 An interface to the win32 File API's
This module includes the transactional NTFS operations introduced with Vista. The transacted functions are not wrapped separately, but are invoked by passing a transaction handle to the corresponding Unicode API function. This makes it simple to convert a set of file operations into a transaction by simply adding Transaction=PyHANDLE to the passed arguments. If Transaction is None, 0, or not specified, the non-transacted API function will be called.
Functions combined in this manner:
CreateFile / CreateFileTransacted
DeleteFile / DeleteFileTransacted
CreateDirectoryEx / CreateDirectoryTransacted
MoveFileWithProgress / MoveFileTransacted
CopyFileEx / CopyFileTransacted
GetFileAttributes / GetFileAttributesTransacted
SetFileAttributes / SetFileAttributesTransacted
CreateHardLink / CreateHardLinkTransacted
CreateSymbolicLink / CreateSymbolicLinkTransacted
RemoveDirectory / RemoveDirectoryTransacted

#### Methods

- AreFileApisANSI

 Determines whether a set of Win32 file functions is using the ANSI or OEM character set code page. This function is useful for 8-bit console input and output operations.

- CancelIo

 Cancels pending IO requests for the object.

- CopyFile

 Copies a file

- CopyFileW

 Copies a file

- CreateDirectory

 Creates a directory

- CreateDirectoryW

 Creates a directory

- CreateDirectoryEx

 Creates a directory

- CreateFile

 Creates or opens the a file or other object and returns a handle that can be used to access the object.

- CreateIoCompletionPort

 Can associate an instance of an opened file with a newly created or an existing input/output (I/O) completion port; or it can create an I/O completion port without associating it with a file.

- CreateMailslot

 Creates a mailslot on the local machine

- GetMailslotInfo

 Retrieves information about a mailslot

- SetMailslotInfo

 Sets a mailslot's timeout

- DefineDosDevice

 Lets an application define, redefine, or delete MS-DOS device names.

- DefineDosDeviceW

 Lets an application define, redefine, or delete MS-DOS device names.

- DeleteFile

 Deletes a file.

- DeviceIoControl

 Sends a control code to a device or file system driver

- FindClose

 Closes a find handle.

- FindCloseChangeNotification

 Closes a handle.

- FindFirstChangeNotification

 Creates a change notification handle and sets up initial change notification filter conditions. A wait on a notification handle succeeds when a change matching the filter conditions occurs in the specified directory or subtree.

- FindNextChangeNotification

 Requests that the operating system signal a change notification handle the next time it detects an appropriate change,

- FlushFileBuffers

 Clears the buffers for the specified file and causes all buffered data to be written to the file.

- GetBinaryType

 Determines whether a file is executable, and if so, what type of executable file it is. That last property determines which subsystem an executable file runs under.

- GetDiskFreeSpace

 Determines the free space on a device.

- GetDiskFreeSpaceEx

 Determines the free space on a device.

- GetDriveType

 Determines whether a disk drive is a removable, fixed, CD-ROM, RAM disk, or network drive.

- GetDriveTypeW

 Determines whether a disk drive is a removable, fixed, CD-ROM, RAM disk, or network drive.

- GetFileAttributes

 Determines a files attributes.

- GetFileAttributesW

 Determines a files attributes

- GetFileTime

 Returns a file's creation, last access, and modification times.

- SetFileTime

 Sets the date and time that a file was created, last accessed, or last modified.

- GetFileInformationByHandle

 Retrieves file information for a specified file.

- GetCompressedFileSize

 Determines the compressed size of a file.

- GetFileSize

 Determines the size of a file.

- AllocateReadBuffer

 Allocates a buffer which can be used with an overlapped Read operation using win32file::ReadFile

- ReadFile

 Reads a string from a file

- WriteFile

 Writes a string to a file

- CloseHandle

 Closes an open handle.

- LockFileEx

 Locks a file. Wrapper for LockFileEx win32 API.

- UnlockFileEx

 Unlocks a file. Wrapper for UnlockFileEx win32 API.

- GetQueuedCompletionStatus

 Attempts to dequeue an I/O completion packet from a specified input/output completion port.

- PostQueuedCompletionStatus

 lets you post an I/O completion packet to an I/O completion port. The I/O completion packet will satisfy an outstanding call to the GetQueuedCompletionStatus function.

- GetFileType

 Determines the type of a file.

- GetLogicalDrives

 Returns a bitmaks of the logical drives installed.

- GetOverlappedResult

 Determines the result of the most recent call with an OVERLAPPED object.

- LockFile

 Locks a specified file for exclusive access by the calling process.

- MoveFile

 Renames an existing file or a directory (including all its children).

- MoveFileW

 Renames an existing file or a directory (including all its children).

- MoveFileEx

 Renames an existing file or a directory (including all its children).

- MoveFileExW

 Renames an existing file or a directory (including all its children).

- QueryDosDevice

 Returns the mapping for a device name, or all device names

- ReadDirectoryChangesW

 retrieves information describing the changes occurring within a directory.

- FILE_NOTIFY_INFORMATION

 Decodes a PyFILE_NOTIFY_INFORMATION buffer.

- SetCurrentDirectory

 Sets the current directory.

- SetEndOfFile

 Moves the end-of-file (EOF) position for the specified file to the current position of the file pointer.

- SetFileApisToANSI

 Causes a set of Win32 file functions to use the ANSI character set code page. This function is useful for 8-bit console input and output operations.

- SetFileApisToOEM

 Causes a set of Win32 file functions to use the OEM character set code page. This function is useful for 8-bit console input and output operations.

- SetFileAttributes

 Changes a file's attributes.

- SetFilePointer

 Moves the file pointer of an open file.

- SetVolumeLabel

 Sets a volume label for a disk drive.

- UnlockFile

 Unlocks a region of a file locked by win32file::LockFile or win32file::LockFileEx

- _get_osfhandle

 Gets operating-system file handle associated with existing stream

- _open_osfhandle

 Associates a C run-time file handle with a existing operating-system file handle.

- _setmaxstdio

 Set the maximum allowed number of open stdio handles

- _getmaxstdio

 Returns the maximum number of CRT io streams.

- TransmitFile

 Transmits a file over a socket TransmitFile(sock, filehandle, bytes_to_write, bytes_per_send, overlap, flags [, (prepend_buf, postpend_buf)])

- ConnectEx

 Version of connect that uses Overlapped I/O ConnectEx(sock, (addr, port), buf, overlap)

- AcceptEx

 Version of accept that uses Overlapped I/O

- CalculateSocketEndPointSize

 Calculate how many bytes are needed for the connection endpoints data for a socket.

- GetAcceptExSockaddrs

 Parses the connection endpoints from the buffer passed into AcceptEx

- WSAEventSelect

 Specifies an event object to be associated with the supplied set of FD_XXXX network events.

- WSAEnumNetworkEvents

 Return network events that caused the event associated with the socket to be signaled.

- WSAAsyncSelect

 Request windows message notification for the supplied set of FD_XXXX network events.

- WSASend

 Winsock send() equivalent function for Overlapped I/O.

- WSARecv

 Winsock recv() equivalent function for Overlapped I/O.

- BuildCommDCB

 Fills the specified DCB structure with values specified in a device-control string. The device-control string uses the syntax of the mode command

- ClearCommError

 retrieves information about a communications error and reports the current status of a communications device.

- EscapeCommFunction

 directs a specified communications device to perform an extended function.

- GetCommState

 Returns a device-control block (a DCB structure) with the current control settings for a specified communications device.

- SetCommState

 Configures a communications device according to the specifications in a device-control block. The function reinitializes all hardware and control settings, but it does not empty output or input queues.

- ClearCommBreak

 Restores character transmission for a specified communications device and places the transmission line in a nonbreak state

- GetCommMask

 Retrieves the value of the event mask for a specified communications device.

- SetCommMask

 Sets the value of the event mask for a specified communications device.

- GetCommModemStatus

 Retrieves modem control-register values.

- GetCommTimeouts

 Retrieves the time-out parameters for all read and write operations on a specified communications device.

- SetCommTimeouts

 Sets the time-out parameters for all read and write operations on a specified communications device.

- PurgeComm

 Discards all characters from the output or input buffer of a specified communications resource. It can also terminate pending read or write operations on the resource.

- SetCommBreak

 Suspends character transmission for a specified communications device and places the transmission line in a break state until the win32file::ClearCommBreak function is called.

- SetupComm

 Initializes the communications parameters for a specified communications device.

- TransmitCommChar

 Transmits a specified character ahead of any pending data in the output buffer of the specified communications device.

- WaitCommEvent

 Waits for an event to occur for a specified communications device. The set of events that are monitored by this function is contained in the event mask associated with the device handle.

- SetVolumeMountPoint

 Mounts the specified volume at the specified volume mount point.

- DeleteVolumeMountPoint

 Unmounts the volume from the specified volume mount point.

- GetVolumeNameForVolumeMountPoint

 Returns unique volume name.

- GetVolumePathName

 Returns volume mount point for a path

- GetVolumePathNamesForVolumeName

 Returns mounted paths for a volume

- CreateHardLink

 Establishes an NTFS hard link between an existing file and a new file.

- CreateSymbolicLink

 Creates a symbolic link (reparse point)

- EncryptFile

 Encrypts specified file (requires Win2k or higher and NTFS)

- DecryptFile

 Decrypts specified file (requires Win2k or higher and NTFS)

- EncryptionDisable

 Enables/disables encryption for a directory (requires Win2k or higher and NTFS)

- FileEncryptionStatus

 retrieves the encryption status of the specified file.

- QueryUsersOnEncryptedFile

 Returns list of users for an encrypted file as tuples of (SID, certificate hash blob, display info)

- QueryRecoveryAgentsOnEncryptedFile

 Lists recovery agents for file as a tuple of tuples.

- RemoveUsersFromEncryptedFile

 Removes specified certificates from file - if certificate is not found, it is ignored

- AddUsersToEncryptedFile

 Allows user identified by SID and EFS certificate access to decrypt specified file

- DuplicateEncryptionInfoFile

 Duplicates EFS encryption from one file to another

- BackupRead

 Reads streams of data from a file

- BackupSeek

 Seeks forward in a file stream

- BackupWrite

 Restores file data

- SetFileShortName

 Set the 8.3 name of a file

- CopyFileEx

 Restartable file copy with optional progress routine

- MoveFileWithProgress

 Moves a file, and reports progress to a callback function

- ReplaceFile

 Replaces one file with another

- OpenEncryptedFileRaw

 Initiates a backup or restore operation on an encrypted file

- ReadEncryptedFileRaw

 Reads the encrypted bytes of a file for backup and restore purposes

- WriteEncryptedFileRaw

 Writes raw bytes to an encrypted file

- CloseEncryptedFileRaw

 Frees a context created by win32file::OpenEncryptedFileRaw

- CreateFileW

 Unicode version of CreateFile - see win32file::CreateFile for more information.

- DeleteFileW

 Deletes a file

- GetFileAttributesEx

 Retrieves attributes for a specified file or directory.

- SetFileAttributesW

 Sets a file's attributes

- CreateDirectoryExW

 Creates a directory

- RemoveDirectory

 Removes an existing directory

- FindFilesW

 Retrieves a list of matching filenames, using the Windows Unicode API. An interface to the API FindFirstFileW/FindNextFileW/Find close functions.

- FindFilesIterator

 Returns an interator based on FindFirstFile/FindNextFile. Similar to win32file::FindFiles , but avoids the creation of the list for huge directories.

- FindStreams

 List the data streams for a file

- FindFileNames

 Enumerates hard links that point to specified file

- GetFinalPathNameByHandle

 Returns the file name for an open file handle

- SfcGetNextProtectedFile

 Returns list of protected operating system files

- SfcIsFileProtected

 Checks if a file is protected

- GetLongPathName

 Retrieves the long path for a short path (8.3 filename)

- GetFullPathName

 Returns full path for path passed in

- Wow64DisableWow64FsRedirection

 Disables file system redirection for 32-bit processes running on a 64-bit system

- Wow64RevertWow64FsRedirection

 Reenables file system redirection for 32-bit processes running on a 64-bit system

- GetFileInformationByHandleEx

 Retrieves extended file information for an open file handle.

- SetFileInformationByHandle

 Changes file characteristics by file handle

- ReOpenFile

 Creates a new handle to an open file

- OpenFileById

 Opens a file by File Id or Object Id


---

# win32file 成员详细文档（共 140 项）


---

<!-- page: win32file__AcceptEx_meth.html -->

## win32file.AcceptEx

 AcceptEx(sListening, sAccepting, buffer, ol)

Version of accept that uses Overlapped I/O

#### Parameters

- sListening : PySocket /int

 Socket that had listen() called on.

- sAccepting : PySocket /int

 Socket that will be used as the incoming connection.

- buffer : buffer

 Buffer to read incoming data and connection point information into. This buffer MUST be big enough to recieve your connection endpoints... AF_INET sockets need to be at least 64 bytes. The correct minimum of the buffer is determined by the protocol family that the listening socket is using.

- ol : PyOVERLAPPED

 An overlapped structure

#### Comments

 In order to make sure the connection has been accepted, either use the hEvent in PyOVERLAPPED, GetOverlappedResult, or GetQueuedCompletionStatus.

 To use this with I/O completion ports, don't forget to attach sAccepting to your completion port.

 Pass a buffer of exactly the size returned by win32file::CalculateSocketEndPointSize to have AcceptEx return without reading any bytes from the remote connection.

#### Example

To have sAccepting inherit the properties of sListening, you need to do the following after a connection is successfully accepted

```
import struct



sAccepting.setsockopt(socket.SOL_SOCKET, win32file.SO_UPDATE_ACCEPT_CONTEXT, struct.pack("I", sListening.fileno()))




```

#### Return Value

The result is 0 or ERROR_IO_PENDING. All other values will raise win32file.error. Specifically: if the win32 function returns FALSE, WSAGetLastError() is checked for ERROR_IO_PENDING.


---

<!-- page: win32file__AddUsersToEncryptedFile_meth.html -->

## win32file.AddUsersToEncryptedFile

 AddUsersToEncryptedFile(FileName, pUsers)

Allows user identified by SID and EFS certificate access to decrypt specified file

#### Parameters

- FileName : string

 File that additional users will be allowed to decrypt

- pUsers : ((PySID,string,int),...)

 Sequence representing ENCRYPTION_CERTIFICATE_LIST - elements are sequences consisting of users' Sid, encoded EFS certficate (user must export a .cer to obtain this data), and encoding type (usually 1 for X509_ASN_ENCODING)


---

<!-- page: win32file__AllocateReadBuffer_meth.html -->

## win32file.AllocateReadBuffer

 PyOVERLAPPEDReadBuffer = AllocateReadBuffer(bufSize)

Allocates a buffer which can be used with an overlapped Read operation using win32file::ReadFile

#### Parameters

- bufSize : int

 The size of the buffer to allocate.


---

<!-- page: win32file__AreFileApisANSI_meth.html -->

## win32file.AreFileApisANSI

 int = AreFileApisANSI()

Determines whether a set of Win32 file functions is using the ANSI or OEM character set code page. This function is useful for 8-bit console input and output operations.


---

<!-- page: win32file__BackupRead_meth.html -->

## win32file.BackupRead

 (int, buffer, int) = BackupRead(hFile, NumberOfBytesToRead , Buffer , bAbort , bProcessSecurity , lpContext )

Reads streams of data from a file

#### Parameters

- hFile : PyHANDLE

 File handle opened by CreateFile

- NumberOfBytesToRead : int

 Number of bytes to be read from file

- Buffer : buffer

 Writeable buffer object that receives data read

- bAbort : int

 If true, ends read operation and frees backup context

- bProcessSecurity : int

 Indicates whether file's ACL stream should be read

- lpContext : int

 Pass 0 on first call, then pass back value returned from last call thereafter

#### Comments

 Returns number of bytes read, data buffer, and context pointer for next operation If Buffer is None, a new buffer will be created of size NbrOfBytesToRead that can be passed back in subsequent calls


---

<!-- page: win32file__BackupSeek_meth.html -->

## win32file.BackupSeek

 long = BackupSeek(hFile, NumberOfBytesToSeek , lpContext )

Seeks forward in a file stream

#### Parameters

- hFile : PyHANDLE

 File handle used by a BackupRead operation

- NumberOfBytesToSeek : long

 Number of bytes to move forward in current stream

- lpContext : int

 Context pointer returned from a BackupRead operation

#### Comments

 Function will only seek to end of current stream, used to seek past bad data or find beginning position for read of next stream Returns number of bytes actually moved


---

<!-- page: win32file__BackupWrite_meth.html -->

## win32file.BackupWrite

 (int,int) = BackupWrite(hFile, NumberOfBytesToWrite , Buffer , bAbort , bProcessSecurity , lpContext )

Restores file data

#### Parameters

- hFile : PyHANDLE

 File handle opened by CreateFile

- NumberOfBytesToWrite : int

 Length of data to be written to file

- Buffer : string

 A string or buffer object that contains the data to be written

- bAbort : int

 If true, ends write operation and frees backup context

- bProcessSecurity : int

 Indicates whether ACL's should be restored

- lpContext : int

 Pass 0 on first call, then pass back value returned from last call thereafter

#### Comments

 Returns number of bytes written and context pointer for next operation


---

<!-- page: win32file__BuildCommDCB_meth.html -->

## win32file.BuildCommDCB

 PyDCB = BuildCommDCB(def, dcb )

Fills the specified DCB structure with values specified in a device-control string. The device-control string uses the syntax of the mode command

#### Parameters

- def : string

 device-control string

- dcb : PyDCB

 The device-control block


---

<!-- page: win32file__COMSTAT_meth.html -->

## win32file.COMSTAT

 PyCOMSTAT = COMSTAT()

Creates a new COMSTAT object


---

<!-- page: win32file__CalculateSocketEndPointSize_meth.html -->

## win32file.CalculateSocketEndPointSize

 int = CalculateSocketEndPointSize(socket)

Calculate how many bytes are needed for the connection endpoints data for a socket.

#### Parameters

- socket : PySocket /int

 The socket for which to determine the size.

#### Comments

 This function allows you to determine the minumum buffer size which can be passed to win32file::AcceptEx


---

<!-- page: win32file__CancelIo_meth.html -->

## win32file.CancelIo

 CancelIo(handle)

Cancels pending IO requests for the object.

#### Parameters

- handle : PyHANDLE

 The handle being cancelled.


---

<!-- page: win32file__ClearCommBreak_meth.html -->

## win32file.ClearCommBreak

 ClearCommBreak(handle)

Restores character transmission for a specified communications device and places the transmission line in a nonbreak state

#### Parameters

- handle : PyHANDLE

 The handle to the communications device.


---

<!-- page: win32file__ClearCommError_meth.html -->

## win32file.ClearCommError

 int, PyCOMSTAT = ClearCommError(PyHANDLE)

retrieves information about a communications error and reports the current status of a communications device.

#### Parameters

- PyHANDLE : handle

 A handle to the device.


---

<!-- page: win32file__CloseEncryptedFileRaw_meth.html -->

## win32file.CloseEncryptedFileRaw

 CloseEncryptedFileRaw(Context)

Frees a context created by win32file::OpenEncryptedFileRaw

#### Parameters

- Context : PyCObject

 Context object returned from win32file::OpenEncryptedFileRaw


---

<!-- page: win32file__CloseHandle_meth.html -->

## win32file.CloseHandle

 CloseHandle(handle)

Closes an open handle.

#### Parameters

- handle : PyHANDLE/int

 A previously opened handle.


---

<!-- page: win32file__ConnectEx_meth.html -->

## win32file.ConnectEx

 (int, int) = ConnectEx(s, name , Overlapped , SendBuffer )

Version of connect that uses Overlapped I/O ConnectEx(sock, (addr, port), buf, overlap)

#### Parameters

- s : PySocket /int

 A bound, unconnected socket that will be used to connect

- name : tuple

 Address to connect to (host, port)

- Overlapped : PyOVERLAPPED

 An overlapped structure

- SendBuffer=None : buffer

 Buffer to send on the socket after connect

#### Return Value

Returns the completion code and number of bytes sent. The completion code will be 0 for a completed operation, or ERROR_IO_PENDING for a pending overlapped operation.


---

<!-- page: win32file__CopyFileEx_meth.html -->

## win32file.CopyFileEx

 CopyFileEx(ExistingFileName, NewFileName, ProgressRoutine, Data, Cancel, CopyFlags, Transaction)

Restartable file copy with optional progress routine

#### Parameters

- ExistingFileName : string

 File to be copied

- NewFileName : string

 Place to which it will be copied

- ProgressRoutine=None : CopyProgressRoutine

 A python function that receives progress updates, can be None

- Data=None : object

 An arbitrary object to be passed to the callback function

- Cancel=False : boolean

 Pass True to cancel a restartable copy that was previously interrupted

- CopyFlags=0 : int

 Combination of COPY_FILE_* flags

- Transaction=None : PyHANDLE

 Handle to a transaction as returned by win32transaction::CreateTransaction

#### Comments

 Accepts keyword args.

 The Transaction arg can be passed to invoke CopyFileTransacted

#### Win32 API References

- Search for CopyFileEx at [msdn](https://learn.microsoft.com/en-ca/search/?terms=CopyFileEx), [google](https://www.google.com/search?q=CopyFileEx) or [google groups](https://groups.google.com/groups?q=CopyFileEx).

- Search for CopyFileTransacted at [msdn](https://learn.microsoft.com/en-ca/search/?terms=CopyFileTransacted), [google](https://www.google.com/search?q=CopyFileTransacted) or [google groups](https://groups.google.com/groups?q=CopyFileTransacted).


---

<!-- page: win32file__CopyFileW_meth.html -->

## win32file.CopyFileW

 CopyFileW(from, to, bFailIfExists)

Copies a file

#### Parameters

- from : string

 The name of the file to copy from

- to : string

 The name of the file to copy to

- bFailIfExists : int

 Indicates if the operation should fail if the file exists.


---

<!-- page: win32file__CopyFile_meth.html -->

## win32file.CopyFile

 CopyFile(from, to, bFailIfExists)

Copies a file

#### Parameters

- from : string

 The name of the file to copy from

- to : string

 The name of the file to copy to

- bFailIfExists : int

 Indicates if the operation should fail if the file exists.


---

<!-- page: win32file__CreateDirectoryExW_meth.html -->

## win32file.CreateDirectoryExW

 CreateDirectoryExW(TemplateDirectory, NewDirectory, SecurityAttributes, Transaction)

Creates a directory

#### Parameters

- TemplateDirectory : string

 Directory to use as a template, can be None

- NewDirectory : string

 Name of directory to be created

- SecurityAttributes=None : PySECURITY_ATTRIBUTES

 Security for new directory (optional)

- Transaction=None : PyHANDLE

 Handle to a transaction (optional). See win32transaction::CreateTransaction.

#### Comments

 If a transaction handle is passed, CreateDirectoryTransacted will be called.

 Accepts keyword arguments.

#### Win32 API References

- Search for CreateDirectoryEx at [msdn](https://learn.microsoft.com/en-ca/search/?terms=CreateDirectoryEx), [google](https://www.google.com/search?q=CreateDirectoryEx) or [google groups](https://groups.google.com/groups?q=CreateDirectoryEx).

- Search for CreateDirectoryTransacted at [msdn](https://learn.microsoft.com/en-ca/search/?terms=CreateDirectoryTransacted), [google](https://www.google.com/search?q=CreateDirectoryTransacted) or [google groups](https://groups.google.com/groups?q=CreateDirectoryTransacted).


---

<!-- page: win32file__CreateDirectoryEx_meth.html -->

## win32file.CreateDirectoryEx

 CreateDirectoryEx(templateName, newDirectory, sa)

Creates a directory

#### Parameters

- templateName : string

 Specifies the path of the directory to use as a template when creating the new directory.

- newDirectory : string

 Specifies the name of the new directory

- sa : PySECURITY_ATTRIBUTES

 The security attributes, or None


---

<!-- page: win32file__CreateDirectoryW_meth.html -->

## win32file.CreateDirectoryW

 CreateDirectoryW(name, sa)

Creates a directory

#### Parameters

- name : string

 The name of the directory to create

- sa : PySECURITY_ATTRIBUTES

 The security attributes, or None


---

<!-- page: win32file__CreateDirectory_meth.html -->

## win32file.CreateDirectory

 CreateDirectory(name, sa)

Creates a directory

#### Parameters

- name : string

 The name of the directory to create

- sa : PySECURITY_ATTRIBUTES

 The security attributes, or None


---

<!-- page: win32file__CreateFileW_meth.html -->

## win32file.CreateFileW

 PyHANDLE = CreateFileW(FileName, DesiredAccess , ShareMode , SecurityAttributes , CreationDisposition , FlagsAndAttributes , TemplateFile , Transaction , MiniVersion , ExtendedParameter )

Unicode version of CreateFile - see win32file::CreateFile for more information.

#### Parameters

- FileName : string

 Name of file

- DesiredAccess : int

 Combination of access mode flags. See MSDN docs.

- ShareMode : int

 Combination of FILE_SHARE_READ, FILE_SHARE_WRITE, FILE_SHARE_DELETE

- SecurityAttributes : PySECURITY_ATTRIBUTES

 Specifies security descriptor and handle inheritance, can be None

- CreationDisposition : int

 One of CREATE_ALWAYS,CREATE_NEW,OPEN_ALWAYS,OPEN_EXISTING or TRUNCATE_EXISTING

- FlagsAndAttributes : int

 Combination of FILE_ATTRIBUTE_* and FILE_FLAG_* flags

- TemplateFile=None : PyHANDLE

 Handle to file to be used as template, can be None

- Transaction=None : PyHANDLE

 Handle to the transaction as returned by win32transaction::CreateTransaction

- MiniVersion=None : int

 Transacted version of file to open, can be None

- ExtendedParameter=None : None

 Reserved, use only None

#### Comments

 If Transaction is specified, CreateFileTransacted will be called

 Accepts keyword arguments.

#### Win32 API References

- Search for CreateFile at [msdn](https://learn.microsoft.com/en-ca/search/?terms=CreateFile), [google](https://www.google.com/search?q=CreateFile) or [google groups](https://groups.google.com/groups?q=CreateFile).

- Search for CreateFileTransacted at [msdn](https://learn.microsoft.com/en-ca/search/?terms=CreateFileTransacted), [google](https://www.google.com/search?q=CreateFileTransacted) or [google groups](https://groups.google.com/groups?q=CreateFileTransacted).


---

<!-- page: win32file__CreateFile_meth.html -->

## win32file.CreateFile

 PyHANDLE = CreateFile(fileName, desiredAccess , shareMode , attributes , CreationDisposition , flagsAndAttributes , hTemplateFile )

Creates or opens the a file or other object and returns a handle that can be used to access the object.

#### Parameters

- fileName : string

 The name of the file

- desiredAccess : int

 access (read-write) mode Specifies the type of access to the object. An application can obtain read access, write access, read-write access, or device query access. This parameter can be any combination of the following values.

| | Value | Meaning
| |

---

 |

---

| | 0 | Specifies device query access to the object. An application can query device attributes without accessing the device.
| | GENERIC_READ | Specifies read access to the object. Data can be read from the file and the file pointer can be moved. Combine with GENERIC_WRITE for read-write access.
| | GENERIC_WRITE | Specifies write access to the object. Data can be written to the file and the file pointer can be moved. Combine with GENERIC_READ for read-write access.
- shareMode : int

 Set of bit flags that specifies how the object can be shared. If dwShareMode is 0, the object cannot be shared. Subsequent open operations on the object will fail, until the handle is closed. To share the object, use a combination of one or more of the following values:

| | Value | Meaning
| |

---

 |

---

| | FILE_SHARE_DELETE | Windows NT: Subsequent open operations on the object will succeed only if delete access is requested.
| | FILE_SHARE_READ | Subsequent open operations on the object will succeed only if read access is requested.
| | FILE_SHARE_WRITE | Subsequent open operations on the object will succeed only if write access is requested.
- attributes : PySECURITY_ATTRIBUTES

 The security attributes, or None

- CreationDisposition : int

 Specifies which action to take on files that exist, and which action to take when files do not exist. For more information about this parameter, see the Remarks section. This parameter must be one of the following values:

| | Value | Meaning
| |

---

 |

---

| | CREATE_NEW | Creates a new file. The function fails if the specified file already exists.
| | CREATE_ALWAYS | Creates a new file. If the file exists, the function overwrites the file and clears the existing attributes.
| | OPEN_EXISTING | Opens the file. The function fails if the file does not exist. See the Remarks section for a discussion of why you should use the OPEN_EXISTING flag if you are using the CreateFile function for devices, including the console.
| | OPEN_ALWAYS | Opens the file, if it exists. If the file does not exist, the function creates the file as if dwCreationDisposition were CREATE_NEW.
| | TRUNCATE_EXISTING | Opens the file. Once opened, the file is truncated so that its size is zero bytes. The calling process must open the file with at least GENERIC_WRITE access. The function fails if the file does not exist.
- flagsAndAttributes : int

 file attributes

- hTemplateFile : PyHANDLE

 Specifies a handle with GENERIC_READ access to a template file. The template file supplies file attributes and extended attributes for the file being created.

#### Comments

 The following objects can be opened:
files
pipes
mailslots
communications resources
disk devices (Windows NT only)
consoles
directories (open only)


---

<!-- page: win32file__CreateHardLink_meth.html -->

## win32file.CreateHardLink

 CreateHardLink(FileName, ExistingFileName, SecurityAttributes, Transaction)

Establishes an NTFS hard link between an existing file and a new file.

#### Parameters

- FileName : string

 The name of the new directory entry to be created.

- ExistingFileName : string

 The name of the existing file to which the new link will point.

- SecurityAttributes=None : PySECURITY_ATTRIBUTES

 Optional SECURITY_ATTRIBUTES object. MSDN describes this parameter as reserved, so use only None

- Transaction=None : PyHANDLE

 Handle to a transaction, as returned by win32transaction::CreateTransaction

#### Comments

 An NTFS hard link is similar to a POSIX hard link.
This function creates a second directory entry for an existing file, can be different name in same directory or any name in a different directory. Both file paths must be on the same NTFS volume.
To remove the link, simply delete it and the original file will still remain.

 Accepts keyword args.

 If the Transaction parameter is specified, CreateHardLinkTransacted will be called

#### Example

Usage

```
CreateHardLink('h:\\dir\\newfilename.txt','h:\\otherdir\\existingfile.txt')




```


---

<!-- page: win32file__CreateIoCompletionPort_meth.html -->

## win32file.CreateIoCompletionPort

 PyHANDLE = CreateIoCompletionPort(handle, existing , completionKey , numThreads )

Can associate an instance of an opened file with a newly created or an existing input/output (I/O) completion port; or it can create an I/O completion port without associating it with a file.

#### Parameters

- handle : PyHANDLE

 file handle to associate with the I/O completion port

- existing : PyHANDLE

 handle to the I/O completion port

- completionKey : int

 per-file completion key for I/O completion packets

- numThreads : int

 number of threads allowed to execute concurrently

#### Return Value

If an existing handle to a completion port is passed, the result of this function will be that same handle. See MSDN for more details.


---

<!-- page: win32file__CreateMailslot_meth.html -->

## win32file.CreateMailslot

 PyHANDLE = CreateMailslot(Name, MaxMessageSize , ReadTimeout , SecurityAttributes )

Creates a mailslot on the local machine

#### Parameters

- Name : str

 Name of the mailslot, of the form \\.\\mailslot\\[path]name

- MaxMessageSize : int

 Largest message size. Use 0 for unlimited.

- ReadTimeout : int

 Timeout in milliseconds. Use -1 for no timeout.

- SecurityAttributes : PySECURITY_ATTRIBUTES

 Determines if returned handle is inheritable, can be None

#### Win32 API References

- Search for CreateMailslot at [msdn](https://learn.microsoft.com/en-ca/search/?terms=CreateMailslot), [google](https://www.google.com/search?q=CreateMailslot) or [google groups](https://groups.google.com/groups?q=CreateMailslot).


---

<!-- page: win32file__CreateSymbolicLink_meth.html -->

## win32file.CreateSymbolicLink

 CreateSymbolicLink(SymlinkFileName, TargetFileName, Flags, Transaction)

Creates a symbolic link (reparse point)

#### Parameters

- SymlinkFileName : string

 Path of the symbolic link to be created

- TargetFileName : string

 The name of file to which link will point

- Flags=0 : int

 SYMBOLIC_LINK_FLAG_DIRECTORY and SYMBOLIC_LINK_FLAG_ALLOW_UNPRIVILEGED_CREATE are the only defined flags

- Transaction=None : PyHANDLE

 Handle to a transaction, as returned by win32transaction::CreateTransaction

#### Comments

 Accepts keyword args.

 Requires SeCreateSymbolicLink priv.

 If the Transaction parameter is passed in, CreateSymbolicLinkTransacted will be called


---

<!-- page: win32file__DCB_meth.html -->

## win32file.DCB

 PyDCB = DCB()

Creates a new DCB object


---

<!-- page: win32file__DecryptFile_meth.html -->

## win32file.DecryptFile

 DecryptFile(filename)

Decrypts specified file (requires Win2k or higher and NTFS)

#### Parameters

- filename : string

 File to decrypt


---

<!-- page: win32file__DefineDosDeviceW_meth.html -->

## win32file.DefineDosDeviceW

 DefineDosDeviceW(flags, deviceName, targetPath)

Lets an application define, redefine, or delete MS-DOS device names.

#### Parameters

- flags : int

 flags specifying aspects of device definition

- deviceName : string

 MS-DOS device name string

- targetPath : string

 MS-DOS or path string for 32-bit Windows.


---

<!-- page: win32file__DefineDosDevice_meth.html -->

## win32file.DefineDosDevice

 DefineDosDevice(flags, deviceName, targetPath)

Lets an application define, redefine, or delete MS-DOS device names.

#### Parameters

- flags : int

 flags specifying aspects of device definition

- deviceName : string

 MS-DOS device name string

- targetPath : string

 MS-DOS or path string for 32-bit Windows.


---

<!-- page: win32file__DeleteFileW_meth.html -->

## win32file.DeleteFileW

 DeleteFileW(FileName, Transaction)

Deletes a file

#### Parameters

- FileName : string

 Name of file to be deleted

- Transaction=None : PyHANDLE

 Transaction handle as returned by win32transaction::CreateTransaction

#### Comments

 If a transaction handle is passed in, DeleteFileTransacted will be called.

 Accepts keyword arguments.

#### Win32 API References

- Search for DeleteFile at [msdn](https://learn.microsoft.com/en-ca/search/?terms=DeleteFile), [google](https://www.google.com/search?q=DeleteFile) or [google groups](https://groups.google.com/groups?q=DeleteFile).

- Search for DeleteFileTransacted at [msdn](https://learn.microsoft.com/en-ca/search/?terms=DeleteFileTransacted), [google](https://www.google.com/search?q=DeleteFileTransacted) or [google groups](https://groups.google.com/groups?q=DeleteFileTransacted).


---

<!-- page: win32file__DeleteFile_meth.html -->

## win32file.DeleteFile

 DeleteFile(fileName)

Deletes a file.

#### Parameters

- fileName : string

 The filename to delete


---

<!-- page: win32file__DeleteVolumeMountPoint_meth.html -->

## win32file.DeleteVolumeMountPoint

 DeleteVolumeMountPoint(VolumeMountPoint)

Unmounts the volume from the specified volume mount point.

#### Parameters

- VolumeMountPoint : string

 The mount point to delete - must have a trailing backslash.

#### Comments

 Accepts keyword args.

 Throws an error if it is not a valid mount point, returns None on success.
Use carefully - will remove drive letter assignment if no directory specified

#### Example

Usage

```
DeleteVolumeMountPoint('h:\\tmp\\')




```


---

<!-- page: win32file__DeviceIoControl_meth.html -->

## win32file.DeviceIoControl

 str/buffer = DeviceIoControl(Device, IoControlCode , InBuffer , OutBuffer , Overlapped )

Sends a control code to a device or file system driver

#### Parameters

- Device : PyHANDLE

 Handle to a file, device, or volume

- IoControlCode : int

 IOControl Code to use, from winioctlcon

- InBuffer : str/buffer

 The input data for the operation, can be None for some operations.

- OutBuffer : int/buffer

 Size of the buffer to allocate for output, or a writeable buffer as returned by win32file::AllocateReadBuffer.

- Overlapped=None : PyOVERLAPPED

 An overlapped object for async operations. Device handle must have been opened with FILE_FLAG_OVERLAPPED.

#### Comments

 Accepts keyword args

#### Return Value

If a preallocated output buffer is passed in, the returned object may be the original buffer, or a view of the buffer with only the actual size of the retrieved data.
If OutBuffer is a buffer size and the operation is synchronous (ie no Overlapped is passed in), returns a plain string containing the retrieved data. For an async operation, a new writeable buffer is returned.


---

<!-- page: win32file__DuplicateEncryptionInfoFile_meth.html -->

## win32file.DuplicateEncryptionInfoFile

 DuplicateEncryptionInfoFile(SrcFileName, DstFileName, CreationDisposition, Attributes, SecurityAttributes)

Duplicates EFS encryption from one file to another

#### Parameters

- SrcFileName : string

 Encrypted file to read EFS metadata from

- DstFileName : string

 File to be encrypted using EFS data from source file

- CreationDisposition : int

 Specifies whether an existing file should be overwritten (CREATE_NEW or CREATE_ALWAYS)

- Attributes : int

 File attributes

- SecurityAttributes=None : PySECURITY_ATTRIBUTES

 Specifies security for destination file

#### Comments

 Accepts keyword arguments.

#### Win32 API References

- Search for DuplicateEncryptionInfoFile at [msdn](https://learn.microsoft.com/en-ca/search/?terms=DuplicateEncryptionInfoFile), [google](https://www.google.com/search?q=DuplicateEncryptionInfoFile) or [google groups](https://groups.google.com/groups?q=DuplicateEncryptionInfoFile).


---

<!-- page: win32file__EncryptFile_meth.html -->

## win32file.EncryptFile

 EncryptFile(filename)

Encrypts specified file (requires Win2k or higher and NTFS)

#### Parameters

- filename : string

 File to encrypt


---

<!-- page: win32file__EncryptionDisable_meth.html -->

## win32file.EncryptionDisable

 EncryptionDisable(DirName, Disable)

Enables/disables encryption for a directory (requires Win2k or higher and NTFS)

#### Parameters

- DirName : string

 Directory to enable or disable

- Disable : boolean

 Set to False to enable encryption


---

<!-- page: win32file__EscapeCommFunction_meth.html -->

## win32file.EscapeCommFunction

 EscapeCommFunction(handle)

directs a specified communications device to perform an extended function.

#### Parameters

- handle : PyHANDLE

 The handle to the communications device.

| | Value | Meaning
| |

---

 |

---

| | CLRDTR | Clears the DTR (data-terminal-ready) signal.
| | CLRRTS | Clears the RTS (request-to-send) signal.
| | SETDTR | Sends the DTR (data-terminal-ready) signal.
| | SETRTS | Sends the RTS (request-to-send) signal.
| | SETXOFF | Causes transmission to act as if an XOFF character has been received.
| | SETXON | Causes transmission to act as if an XON character has been received.
| | SETBREAK | Suspends character transmission and places the transmission line in a break state until the ClearCommBreak function is called (or EscapeCommFunction is called with the CLRBREAK extended function code). The SETBREAK extended function code is identical to the SetCommBreak function. Note that this extended function does not flush data that has not been transmitted.
| | CLRBREAK | Restores character transmission and places the transmission line in a nonbreak state. The CLRBREAK extended function code is identical to the ClearCommBreak function.


---

<!-- page: win32file__FILE_NOTIFY_INFORMATION_meth.html -->

## win32file.FILE_NOTIFY_INFORMATION

 [(action, filename), ... = FILE_NOTIFY_INFORMATION(buffer, size )

Decodes a PyFILE_NOTIFY_INFORMATION buffer.

#### Parameters

- buffer : string

 The buffer to decode.

- size : int

 The number of bytes to refer to. Generally this will be smaller than the size of the buffer (and certainly never greater!)

#### Comments

 See win32file::ReadDirectoryChangesW for more information.


---

<!-- page: win32file__FileEncryptionStatus_meth.html -->

## win32file.FileEncryptionStatus

 int = FileEncryptionStatus(FileName)

retrieves the encryption status of the specified file.

#### Parameters

- FileName : string

 file to query

#### Return Value

The result is documented as being one of FILE_ENCRYPTABLE, FILE_IS_ENCRYPTED, FILE_SYSTEM_ATTR, FILE_ROOT_DIR, FILE_SYSTEM_DIR, FILE_UNKNOWN, FILE_SYSTEM_NOT_SUPPORT, FILE_USER_DISALLOWED, or FILE_READ_ONLY


---

<!-- page: win32file__FindCloseChangeNotification_meth.html -->

## win32file.FindCloseChangeNotification

 FindCloseChangeNotification(hChangeHandle)

Closes a handle.

#### Parameters

- hChangeHandle : int

 handle to change notification to close


---

<!-- page: win32file__FindClose_meth.html -->

## win32file.FindClose

 FindClose(hFindFile)

Closes a find handle.

#### Parameters

- hFindFile : int

 file search handle


---

<!-- page: win32file__FindFileNames_meth.html -->

## win32file.FindFileNames

 [string,...] = FindFileNames(FileName, Transaction )

Enumerates hard links that point to specified file

#### Parameters

- FileName : string

 Name of file for which to find links

- Transaction=None : PyHANDLE

 Handle to a transaction, can be None

#### Comments

 This uses the API functions FindFirstFileNameW, FindNextFileNameW and FindClose

 If Transaction is specified, a transacted search is performed using FindFirstFileNameTransactedW


---

<!-- page: win32file__FindFilesIterator_meth.html -->

## win32file.FindFilesIterator

 iterator = FindFilesIterator(FileName, Transaction )

Returns an interator based on FindFirstFile/FindNextFile. Similar to win32file::FindFiles , but avoids the creation of the list for huge directories.

#### Parameters

- FileName : string

 A string that specifies a valid directory or path and filename, which can contain wildcard characters (* and ?).

- Transaction=None : PyHANDLE

 Handle to a transaction, can be None. If this parameter is not None, FindFirstFileTransacted will be called to perform a transacted search

#### Comments

 Accepts keyword args.

 FindFirstFileTransacted will be called if a transaction handle is passed in.

#### Return Value

The result is a Python iterator, with each next() method returning a WIN32_FIND_DATA tuple.


---

<!-- page: win32file__FindFilesW_meth.html -->

## win32file.FindFilesW

 list = FindFilesW(FileName, Transaction )

Retrieves a list of matching filenames, using the Windows Unicode API. An interface to the API FindFirstFileW/FindNextFileW/Find close functions.

#### Parameters

- FileName : string

 A string that specifies a valid directory or path and filename, which can contain wildcard characters (* and ?).

- Transaction=None : PyHANDLE

 Transaction handle as returned by win32transaction::CreateTransaction. Can be None. If this parameter is not None, FindFirstFileTransacted will be called to perform a transacted search

#### Comments

 Accepts keyword args.

 FindFirstFileTransacted will be called if a transaction handle is passed in.

#### Win32 API References

- Search for FindFirstFile at [msdn](https://learn.microsoft.com/en-ca/search/?terms=FindFirstFile), [google](https://www.google.com/search?q=FindFirstFile) or [google groups](https://groups.google.com/groups?q=FindFirstFile).

- Search for FindFirstFileTransacted at [msdn](https://learn.microsoft.com/en-ca/search/?terms=FindFirstFileTransacted), [google](https://www.google.com/search?q=FindFirstFileTransacted) or [google groups](https://groups.google.com/groups?q=FindFirstFileTransacted).

- Search for FindNextFile at [msdn](https://learn.microsoft.com/en-ca/search/?terms=FindNextFile), [google](https://www.google.com/search?q=FindNextFile) or [google groups](https://groups.google.com/groups?q=FindNextFile).

- Search for FindClose at [msdn](https://learn.microsoft.com/en-ca/search/?terms=FindClose), [google](https://www.google.com/search?q=FindClose) or [google groups](https://groups.google.com/groups?q=FindClose).

#### Return Value

The return value is a list of WIN32_FIND_DATA tuples.


---

<!-- page: win32file__FindFirstChangeNotification_meth.html -->

## win32file.FindFirstChangeNotification

 int = FindFirstChangeNotification(pathName, bWatchSubtree , notifyFilter )

Creates a change notification handle and sets up initial change notification filter conditions. A wait on a notification handle succeeds when a change matching the filter conditions occurs in the specified directory or subtree.

#### Parameters

- pathName : string

 Name of directory to watch

- bWatchSubtree : int

 flag for monitoring directory or directory tree

- notifyFilter : int

 filter conditions to watch for. See win32api::FindFirstChangeNotification for details.


---

<!-- page: win32file__FindNextChangeNotification_meth.html -->

## win32file.FindNextChangeNotification

 int = FindNextChangeNotification(hChangeHandle)

Requests that the operating system signal a change notification handle the next time it detects an appropriate change,

#### Parameters

- hChangeHandle : int

 handle to change notification to signal


---

<!-- page: win32file__FindStreams_meth.html -->

## win32file.FindStreams

 [(long, string),...] = FindStreams(FileName, Transaction )

List the data streams for a file

#### Parameters

- FileName : string

 Name of file (or directory) to operate on

- Transaction=None : PyHANDLE

 Handle to a transaction, can be None

#### Comments

 This uses the API functions FindFirstStreamW, FindNextStreamW and FindClose

 If the Transaction arg is not None, FindFirstStreamTransactedW will be called in place of FindFirstStreamW

#### Return Value

Returns a list of tuples containing each stream's size and name


---

<!-- page: win32file__FlushFileBuffers_meth.html -->

## win32file.FlushFileBuffers

 FlushFileBuffers(hFile)

Clears the buffers for the specified file and causes all buffered data to be written to the file.

#### Parameters

- hFile : PyHANDLE

 open handle to file whose buffers are to be flushed


---

<!-- page: win32file__GetAcceptExSockaddrs_meth.html -->

## win32file.GetAcceptExSockaddrs

 (iFamily, LocalSockAddr , RemoteSockAddr ) = GetAcceptExSockaddrs(sAccepting, buffer )

Parses the connection endpoints from the buffer passed into AcceptEx

#### Parameters

- sAccepting : PySocket /int

 Socket that was passed into the sAccepting parameter of AcceptEx

- buffer : PyOVERLAPPEDReadBuffer

 Buffer you passed into AcceptEx

#### Comments

 LocalSockAddr and RemoteSockAddr are ("xx.xx.xx.xx", port#) if iFamily == AF_INET

 otherwise LocalSockAddr and RemoteSockAddr are just binary strings

 and they should be unpacked with the struct module.


---

<!-- page: win32file__GetBinaryType_meth.html -->

## win32file.GetBinaryType

 int = GetBinaryType(appName)

Determines whether a file is executable, and if so, what type of executable file it is. That last property determines which subsystem an executable file runs under.

#### Parameters

- appName : string

 Fully qualified path of file to test


---

<!-- page: win32file__GetCommMask_meth.html -->

## win32file.GetCommMask

 int = GetCommMask(handle)

Retrieves the value of the event mask for a specified communications device.

#### Parameters

- handle : PyHANDLE

 The handle to the communications device.


---

<!-- page: win32file__GetCommModemStatus_meth.html -->

## win32file.GetCommModemStatus

 int = GetCommModemStatus(handle)

Retrieves modem control-register values.

#### Parameters

- handle : PyHANDLE

 The handle to the communications device.


---

<!-- page: win32file__GetCommState_meth.html -->

## win32file.GetCommState

 PyDCB = GetCommState(handle)

Returns a device-control block (a DCB structure) with the current control settings for a specified communications device.

#### Parameters

- handle : PyHANDLE

 The handle to the communications device.


---

<!-- page: win32file__GetCommTimeouts_meth.html -->

## win32file.GetCommTimeouts

 PyCOMMTIMEOUTS = GetCommTimeouts(handle)

Retrieves the time-out parameters for all read and write operations on a specified communications device.

#### Parameters

- handle : PyHANDLE

 The handle to the communications device.


---

<!-- page: win32file__GetCompressedFileSize_meth.html -->

## win32file.GetCompressedFileSize

 long = GetCompressedFileSize()

Determines the compressed size of a file.


---

<!-- page: win32file__GetDiskFreeSpaceEx_meth.html -->

## win32file.GetDiskFreeSpaceEx

 long, long, long = GetDiskFreeSpaceEx(rootPathName)

Determines the free space on a device.

#### Parameters

- rootPathName : string

 address of root path

#### Return Value

The result is a tuple of long integers:

#### Items

- [0] long integer : freeBytes

 The total number of free bytes on the disk that are available to the user associated with the calling thread.

- [1] long integer : totalBytes

 The total number of bytes on the disk that are available to the user associated with the calling thread. If per-user quotas are in use, this value may be less than the total number of bytes on the disk.

- [2] long integer : totalFreeBytes

 The total number of free bytes on the disk.


---

<!-- page: win32file__GetDiskFreeSpace_meth.html -->

## win32file.GetDiskFreeSpace

 (int, int, int, int) = GetDiskFreeSpace(rootPathName)

Determines the free space on a device.

#### Parameters

- rootPathName : string

 address of root path

#### Return Value

The result is a tuple of integers representing (sectors per cluster, bytes per sector, number of free clusters, total number of clusters)


---

<!-- page: win32file__GetDriveTypeW_meth.html -->

## win32file.GetDriveTypeW

 int = GetDriveTypeW(rootPathName)

Determines whether a disk drive is a removable, fixed, CD-ROM, RAM disk, or network drive.

#### Parameters

- rootPathName : string

#### Return Value

The result is one of the DRIVE_* constants.


---

<!-- page: win32file__GetDriveType_meth.html -->

## win32file.GetDriveType

 int = GetDriveType(rootPathName)

Determines whether a disk drive is a removable, fixed, CD-ROM, RAM disk, or network drive.

#### Parameters

- rootPathName : string

#### Return Value

The result is one of the DRIVE_* constants.


---

<!-- page: win32file__GetFileAttributesEx_meth.html -->

## win32file.GetFileAttributesEx

 tuple = GetFileAttributesEx(FileName, InfoLevelId , Transaction )

Retrieves attributes for a specified file or directory.

#### Parameters

- FileName : string/bytes

 File or directory for which to retrieve information In the usual case, the name is limited to MAX_PATH characters. To extend this limit to nearly 32,000 wide characters, call this and prepend r"\\?\\" to the path.

- InfoLevelId=GetFileExInfoStandard : int

 An integer that gives the set of attribute information to obtain. See the Win32 SDK documentation for more information.

- Transaction=None : PyHANDLE

 Handle to a transaction (optional). See win32transaction::CreateTransaction. If this parameter is specified, GetFileAttributesTransacted will be called.

#### Comments

 Not all file systems can record creation and last access time and not all file systems record them in the same manner. For example, on Windows NT FAT, create time has a resolution of 10 milliseconds, write time has a resolution of 2 seconds, and access time has a resolution of 1 day (really, the access date). On NTFS, access time has a resolution of 1 hour. Furthermore, FAT records times on disk in local time, while NTFS records times on disk in UTC, so it is not affected by changes in time zone or daylight saving time.

 Accepts keyword arguments.

 If bytes are passed for the filename, the ANSI Windows functions are called.

| | InfoLevelId | Information returned
| |

---

 |

---

| | GetFileExInfoStandard | Tuple representing a WIN32_FILE_ATTRIBUTE_DATA struc

#### Win32 API References

- Search for GetFileAttributesEx at [msdn](https://learn.microsoft.com/en-ca/search/?terms=GetFileAttributesEx), [google](https://www.google.com/search?q=GetFileAttributesEx) or [google groups](https://groups.google.com/groups?q=GetFileAttributesEx).

- Search for GetFileAttributesTransacted at [msdn](https://learn.microsoft.com/en-ca/search/?terms=GetFileAttributesTransacted), [google](https://www.google.com/search?q=GetFileAttributesTransacted) or [google groups](https://groups.google.com/groups?q=GetFileAttributesTransacted).

#### Return Value

The result is a tuple of:

#### Items

- [0] int : attributes

 File Attributes. A combination of the win32com.FILE_ATTRIBUTE_* flags.

- [1] PyDateTime : creationTime

 Specifies when the file or directory was created.

- [2] PyDateTime : lastAccessTime

 For a file, specifies when the file was last read from or written to. For a directory, the structure specifies when the directory was created. For both files and directories, the specified date will be correct, but the time of day will always be set to midnight.

- [3] PyDateTime : lastWriteTime

 For a file, the structure specifies when the file was last written to. For a directory, the structure specifies when the directory was created.

- [4] int/long : fileSize

 The size of the file. This member has no meaning for directories.


---

<!-- page: win32file__GetFileAttributesW_meth.html -->

## win32file.GetFileAttributesW

 int = GetFileAttributesW(fileName)

Determines a files attributes

#### Parameters

- fileName : string

 Name of the file to retrieve attributes for.


---

<!-- page: win32file__GetFileAttributes_meth.html -->

## win32file.GetFileAttributes

 int = GetFileAttributes(fileName)

Determines a files attributes.

#### Parameters

- fileName : string

 Name of the file to retrieve attributes for.


---

<!-- page: win32file__GetFileInformationByHandleEx_meth.html -->

## win32file.GetFileInformationByHandleEx

 object = GetFileInformationByHandleEx(File, FileInformationClass )

Retrieves extended file information for an open file handle.

#### Parameters

- File : PyHANDLE

 Handle to a file or directory. Do not pass a pipe handle.

- FileInformationClass : int

 Type of data to return, one of win32file.File*Info values

#### Comments

 Accepts keyword args.

#### Return Value

Type of returned object is determined by the requested information class

| | Class | Returned info
| |

---

 |

---

| | FileBasicInfo | Dict representing a FILE_BASIC_INFO struct
| | FileStandardInfo | Dict representing a FILE_STANDARD_INFO struct
| | FileNameInfo | String containing the file name, without the drive letter
| | FileCompressionInfo | Dict representing a FILE_COMPRESSION_INFO struct
| | FileAttributeTagInfo | Dict representing a FILE_ATTRIBUTE_TAG_INFO struct
| | FileIdBothDirectoryInfo | Sequence of dicts representing FILE_ID_BOTH_DIR_INFO structs. Call in loop until no more files are returned.
| | FileIdBothDirectoryRestartInfo | Sequence of dicts representing FILE_ID_BOTH_DIR_INFO structs.
| | FileStreamInfo | Sequence of dicts representing FILE_STREAM_INFO structs


---

<!-- page: win32file__GetFileInformationByHandle_meth.html -->

## win32file.GetFileInformationByHandle

 tuple = GetFileInformationByHandle(handle)

Retrieves file information for a specified file.

#### Parameters

- handle : PyHANDLE/int

 Handle to the file for which to obtain information.
This handle should not be a pipe handle. The GetFileInformationByHandle function does not work with pipe handles.

#### Comments

 Depending on the underlying network components of the operating system and the type of server connected to, the GetFileInformationByHandle function may fail, return partial information, or full information for the given file. In general, you should not use GetFileInformationByHandle unless your application is intended to be run on a limited set of operating system configurations.

#### Return Value

The result is a tuple of:

#### Items

- [0] int : dwFileAttributes

- [1] PyDateTime : ftCreationTime

- [2] PyDateTime : ftLastAccessTime

- [3] PyDateTime : ftLastWriteTime

- [4] int : dwVolumeSerialNumber

- [5] int : nFileSizeHigh

- [6] int : nFileSizeLow

- [7] int : nNumberOfLinks

- [8] int : nFileIndexHigh

- [9] int : nFileIndexLow


---

<!-- page: win32file__GetFileSize_meth.html -->

## win32file.GetFileSize

 long = GetFileSize()

Determines the size of a file.


---

<!-- page: win32file__GetFileTime_meth.html -->

## win32file.GetFileTime

 (PyDateTime, PyDateTime, PyDateTime) = GetFileTime(handle, creationTime , accessTime , writeTime )

Returns a file's creation, last access, and modification times.

#### Parameters

- handle : PyHANDLE

 Handle to the file.

- creationTime : PyDateTime

- accessTime : PyDateTime

- writeTime : PyDateTime

#### Comments

 Times are returned in UTC time.


---

<!-- page: win32file__GetFileType_meth.html -->

## win32file.GetFileType

 int = GetFileType(hFile)

Determines the type of a file.

#### Parameters

- hFile : PyHANDLE

 The handle to the file.


---

<!-- page: win32file__GetFinalPathNameByHandle_meth.html -->

## win32file.GetFinalPathNameByHandle

 string = GetFinalPathNameByHandle(File, Flags )

Returns the file name for an open file handle

#### Parameters

- File : PyHANDLE

 An open file handle

- Flags : int

 Specifies type of path to return. (win32con.FILE_NAME_NORMALIZED,FILE_NAME_OPENED,VOLUME_NAME_DOS,VOLUME_NAME_GUID,VOLUME_NAME_NONE,VOLUME_NAME_NT)

#### Comments

 Accepts keyword arguments.

#### Win32 API References

- Search for GetFinalPathNameByHandle at [msdn](https://learn.microsoft.com/en-ca/search/?terms=GetFinalPathNameByHandle), [google](https://www.google.com/search?q=GetFinalPathNameByHandle) or [google groups](https://groups.google.com/groups?q=GetFinalPathNameByHandle).


---

<!-- page: win32file__GetFullPathName_meth.html -->

## win32file.GetFullPathName

 string = GetFullPathName(FileName, Transaction )

Returns full path for path passed in

#### Parameters

- FileName : bytes/unicode

 Path on which to operate

- Transaction=None : PyHANDLE

 Handle to a transaction as returned by win32transaction::CreateTransaction

#### Comments

 This function takes either a bytes a unicode string, and returns the same type If unicode is passed in, GetFullPathNameW is called, which supports filenames longer than MAX_PATH

 If Transaction parameter is specified, GetFullPathNameTransacted is called


---

<!-- page: win32file__GetLogicalDrives_meth.html -->

## win32file.GetLogicalDrives

 int = GetLogicalDrives()

Returns a bitmaks of the logical drives installed.


---

<!-- page: win32file__GetLongPathName_meth.html -->

## win32file.GetLongPathName

 string = GetLongPathName(ShortPath, Transaction )

Retrieves the long path for a short path (8.3 filename)

#### Parameters

- ShortPath : string

 8.3 path to be expanded

- Transaction=None : PyHANDLE

 Handle to a transaction. If specified, GetLongPathNameTransacted will be called.

#### Comments

 Accepts keyword args


---

<!-- page: win32file__GetMailslotInfo_meth.html -->

## win32file.GetMailslotInfo

 (int,int,int,int) = GetMailslotInfo(Mailslot)

Retrieves information about a mailslot

#### Parameters

- Mailslot : PyHANDLE

 Handle to a mailslot

#### Win32 API References

- Search for GetMailslotInfo at [msdn](https://learn.microsoft.com/en-ca/search/?terms=GetMailslotInfo), [google](https://www.google.com/search?q=GetMailslotInfo) or [google groups](https://groups.google.com/groups?q=GetMailslotInfo).

#### Return Value

Returns (maximum message size, next message size, message count, timeout)


---

<!-- page: win32file__GetOverlappedResult_meth.html -->

## win32file.GetOverlappedResult

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

<!-- page: win32file__GetQueuedCompletionStatus_meth.html -->

## win32file.GetQueuedCompletionStatus

 (int, int, int, PyOVERLAPPED) = GetQueuedCompletionStatus(hPort, timeOut )

Attempts to dequeue an I/O completion packet from a specified input/output completion port.

#### Parameters

- hPort : PyHANDLE

 The handle to the completion port.

- timeOut : int

 Timeout in milli-seconds.

#### Comments

 This method never throws an API error.
The result is a tuple of (rc, numberOfBytesTransferred, completionKey, overlapped)
If the function succeeds, rc will be set to 0, otherwise it will be set to the win32 error code.


---

<!-- page: win32file__GetVolumeNameForVolumeMountPoint_meth.html -->

## win32file.GetVolumeNameForVolumeMountPoint

 string = GetVolumeNameForVolumeMountPoint(VolumeMountPoint)

Returns unique volume name.

#### Parameters

- VolumeMountPoint : string

 Volume mount point or root drive - trailing backslash required

#### Comments

 Accepts keyword args.


---

<!-- page: win32file__GetVolumePathName_meth.html -->

## win32file.GetVolumePathName

 string = GetVolumePathName(FileName, BufferLength )

Returns volume mount point for a path

#### Parameters

- FileName : string

 File/dir for which to return volume mount point

- BufferLength=0 : int

 Optional parm to allocate extra space for returned string

#### Comments

 Api gives no indication of how much memory is needed, so function assumes returned path will not be longer that length of input path + 1. Use GetFullPathName first for relative paths, or GetLongPathName for 8.3 paths. Optional second parm can also be used to override the buffer size for returned path

 Accepts keyword args.


---

<!-- page: win32file__GetVolumePathNamesForVolumeName_meth.html -->

## win32file.GetVolumePathNamesForVolumeName

 [string,...] = GetVolumePathNamesForVolumeName(VolumeName)

Returns mounted paths for a volume

#### Parameters

- VolumeName : string

 Name of a volume as returned by win32file::GetVolumeNameForVolumeMountPoint

#### Comments

 Accepts keyword args


---

<!-- page: win32file__LockFileEx_meth.html -->

## win32file.LockFileEx

 LockFileEx(hFile, int, int, int, ol)

Locks a file. Wrapper for LockFileEx win32 API.

#### Parameters

- hFile : PyHANDLE/int

 Handle to the file

- int : dwFlags

 Flags that specify exclusive/shared and blocking/non-blocking mode

- int : nbytesLow

 low-order part of number of bytes to lock

- int : nbytesHigh

 high-order part of number of bytes to lock

- ol=None : PyOVERLAPPED

 An overlapped structure


---

<!-- page: win32file__LockFile_meth.html -->

## win32file.LockFile

 LockFile(hFile, offsetLow, offsetHigh, nNumberOfBytesToLockLow, nNumberOfBytesToLockHigh)

Locks a specified file for exclusive access by the calling process.

#### Parameters

- hFile : PyHANDLE

 handle of file to lock

- offsetLow : int

 low-order word of lock region offset

- offsetHigh : int

 high-order word of lock region offset

- nNumberOfBytesToLockLow : int

 low-order word of length to lock

- nNumberOfBytesToLockHigh : int

 high-order word of length to lock


---

<!-- page: win32file__MoveFileExW_meth.html -->

## win32file.MoveFileExW

 MoveFileExW(existingFileName, newFileName, flags)

Renames an existing file or a directory (including all its children).

#### Parameters

- existingFileName : string

 Name of the existing file

- newFileName : string

 New name for the file, can be None for delayed delete operation

- flags : int

 flag to determine how to move file (win32file.MOVEFILE_*)


---

<!-- page: win32file__MoveFileEx_meth.html -->

## win32file.MoveFileEx

 MoveFileEx(existingFileName, newFileName, flags)

Renames an existing file or a directory (including all its children).

#### Parameters

- existingFileName : string

 Name of the existing file

- newFileName : string

 New name for the file, can be None for delayed delete operation

- flags : int

 flag to determine how to move file (win32file.MOVEFILE_*)


---

<!-- page: win32file__MoveFileW_meth.html -->

## win32file.MoveFileW

 MoveFileW(existingFileName, newFileName)

Renames an existing file or a directory (including all its children).

#### Parameters

- existingFileName : string

 Name of the existing file

- newFileName : string

 New name for the file


---

<!-- page: win32file__MoveFileWithProgress_meth.html -->

## win32file.MoveFileWithProgress

 MoveFileWithProgress(ExistingFileName, NewFileName, ProgressRoutine, Data, Flags, Transaction)

Moves a file, and reports progress to a callback function

#### Parameters

- ExistingFileName : string

 File or directory to be moved

- NewFileName : string

 Destination, can be None if flags contain MOVEFILE_DELAY_UNTIL_REBOOT

- ProgressRoutine=None : CopyProgressRoutine

 A python function that receives progress updates, can be None

- Data=None : object

 An arbitrary object to be passed to the callback function

- Flags=0 : int

 Combination of MOVEFILE_* flags

- Transaction=None : PyHANDLE

 Handle to a transaction (optional). See win32transaction::CreateTransaction.

#### Comments

 Accepts keyword arguments.

 The Transaction arg can be passed to invoke MoveFileTransacted


---

<!-- page: win32file__MoveFile_meth.html -->

## win32file.MoveFile

 MoveFile(existingFileName, newFileName)

Renames an existing file or a directory (including all its children).

#### Parameters

- existingFileName : string

 Name of the existing file

- newFileName : string

 New name for the file


---

<!-- page: win32file__OpenEncryptedFileRaw_meth.html -->

## win32file.OpenEncryptedFileRaw

 PyCObject = OpenEncryptedFileRaw(FileName, Flags )

Initiates a backup or restore operation on an encrypted file

#### Parameters

- FileName : string

 Name of file on which to operate

- Flags : int

 CREATE_FOR_IMPORT, CREATE_FOR_DIR, OVERWRITE_HIDDEN, or 0 for export

#### Return Value

Returns a PyCObject containing an operation context that can be passed to win32file::ReadEncryptedFileRaw or win32file::WriteEncryptedFileRaw. Context must be destroyed using win32file::CloseEncryptedFileRaw.


---

<!-- page: win32file__OpenFileById_meth.html -->

## win32file.OpenFileById

 PyHANDLE = OpenFileById(File, FileId , DesiredAccess , ShareMode , Flags , SecurityAttributes )

Opens a file by File Id or Object Id

#### Parameters

- File : PyHANDLE

 Handle to a file on the volume that contains the file to open

- FileId : int/PyIID

 File Id or Object Id of the file to open

- DesiredAccess : int

 Access mode

- ShareMode : int

 Sharing mode (FILE_SHARE_*)

- Flags : int

 Combination of FILE_FLAG_* flags

- SecurityAttributes=None : PySECURITY_ATTRIBUTES

 Reserved, use only None

#### Comments

 Accepts keyword args.


---

<!-- page: win32file__PostQueuedCompletionStatus_meth.html -->

## win32file.PostQueuedCompletionStatus

 None = PostQueuedCompletionStatus(handle, numberOfBytes , completionKey , overlapped )

lets you post an I/O completion packet to an I/O completion port. The I/O completion packet will satisfy an outstanding call to the GetQueuedCompletionStatus function.

#### Parameters

- handle : PyHANDLE

 handle to an I/O completion port

- numberOfBytes=0 : int

 value to return via GetQueuedCompletionStatus' first result

- completionKey=0 : int

 value to return via GetQueuedCompletionStatus' second result

- overlapped=None : PyOVERLAPPED

 value to return via GetQueuedCompletionStatus' third result

#### Comments

 Note that if you post overlapped objects, but your post is closed before all pending requests are processed, the overlapped objects (including its 'handle' and 'object' members) will leak. See MS KB article Q192800 for a summary of this.


---

<!-- page: win32file__PurgeComm_meth.html -->

## win32file.PurgeComm

 PurgeComm(handle, action)

Discards all characters from the output or input buffer of a specified communications resource. It can also terminate pending read or write operations on the resource.

#### Parameters

- handle : PyHANDLE

 The handle to the communications device.

- action : int

 The action to perform. This parameter can be one or more of the following values.

| | Value | Meaning
| |

---

 |

---

| | PURGE_TXABORT | Terminates all outstanding overlapped write operations and returns immediately, even if the write operations have not been completed.
| | PURGE_RXABORT | Terminates all outstanding overlapped read operations and returns immediately, even if the read operations have not been completed.
| | PURGE_TXCLEAR | Clears the output buffer (if the device driver has one).
| | PURGE_RXCLEAR | Clears the input buffer (if the device driver has one).


---

<!-- page: win32file__QueryDosDevice_meth.html -->

## win32file.QueryDosDevice

 string = QueryDosDevice(DeviceName)

Returns the mapping for a device name, or all device names

#### Parameters

- DeviceName : string

 Name of device to query, or None to return all defined devices

#### Return Value

Returns a string containing substrings separated by NULLs with 2 terminating NULLs


---

<!-- page: win32file__QueryRecoveryAgentsOnEncryptedFile_meth.html -->

## win32file.QueryRecoveryAgentsOnEncryptedFile

 (PySID,bytes,string) = QueryRecoveryAgentsOnEncryptedFile(FileName)

Lists recovery agents for file as a tuple of tuples.

#### Parameters

- FileName : string

 file to query

#### Return Value

The result is a tuple of tuples - ((SID, certificate hash blob, display info),....)


---

<!-- page: win32file__QueryUsersOnEncryptedFile_meth.html -->

## win32file.QueryUsersOnEncryptedFile

 (PySID,bytes,string) = QueryUsersOnEncryptedFile(FileName)

Returns list of users for an encrypted file as tuples of (SID, certificate hash blob, display info)

#### Parameters

- FileName : string

 file to query


---

<!-- page: win32file__ReOpenFile_meth.html -->

## win32file.ReOpenFile

 PyHANDLE = ReOpenFile(OriginalFile, DesiredAccess , ShareMode , Flags )

Creates a new handle to an open file

#### Parameters

- OriginalFile : PyHANDLE

 An open file handle

- DesiredAccess : int

 Access mode, cannot conflict with original access mode

- ShareMode : int

 Sharing mode (FILE_SHARE_*), cannot conflict with original share mode

- Flags : int

 Combination of FILE_FLAG_* flags

#### Comments

 Accepts keyword args.


---

<!-- page: win32file__ReadDirectoryChangesW_meth.html -->

## win32file.ReadDirectoryChangesW

 ReadDirectoryChangesW(handle, size, bWatchSubtree, dwNotifyFilter, overlapped)

retrieves information describing the changes occurring within a directory.

#### Parameters

- handle : PyHANDLE

 Handle to the directory to be monitored. This directory must be opened with the FILE_LIST_DIRECTORY access right.

- size : int

 Size of the buffer to allocate for the results.

- bWatchSubtree : int

 Specifies whether the ReadDirectoryChangesW function will monitor the directory or the directory tree. If TRUE is specified, the function monitors the directory tree rooted at the specified directory. If FALSE is specified, the function monitors only the directory specified by the hDirectory parameter.

- dwNotifyFilter : int

 Specifies filter criteria the function checks to determine if the wait operation has completed. This parameter can be one or more of the FILE_NOTIFY_CHANGE_* values.

- overlapped=None : PyOVERLAPPED

 An overlapped object. The directory must also be opened with FILE_FLAG_OVERLAPPED.

#### Comments

 If you pass an overlapped object, you almost certainly must pass a buffer object for the asynchronous results - failure to do so may crash Python as the asynchronous result writes to invalid memory.

 The FILE_NOTIFY_INFORMATION structure used by this function is variable length, depending on the length of the filename. The size of the buffer must be at least 6 bytes long + the length of the filenames returned. The number of notifications that can be returned for a given buffer size depends on the filename lengths.

#### Return Value

If a buffer size is passed, the result is a list of (action, filename)

 If a buffer is passed, the result is None - you must use the overlapped object to determine when the information is available and how much is valid. The buffer can then be passed to win32file::FILE_NOTIFY_INFORMATION


---

<!-- page: win32file__ReadEncryptedFileRaw_meth.html -->

## win32file.ReadEncryptedFileRaw

 ReadEncryptedFileRaw(ExportCallback, CallbackContext, Context)

Reads the encrypted bytes of a file for backup and restore purposes

#### Parameters

- ExportCallback : ExportCallBack

 Python function that receives chunks of data as it is read

- CallbackContext : object

 Arbitrary Python object to be passed to callback function

- Context : PyCObject

 Context object returned from win32file::OpenEncryptedFileRaw


---

<!-- page: win32file__ReadFile_meth.html -->

## win32file.ReadFile

 (int, string) = ReadFile(hFile, buffer/bufSize , overlapped )

Reads a string from a file

#### Parameters

- hFile : PyHANDLE/int

 Handle to the file

- buffer/bufSize : PyOVERLAPPEDReadBuffer/int

 Size of the buffer to create for the result, or a buffer to fill with the result. If a buffer object and overlapped is passed, the result is the buffer itself. If a buffer but no overlapped is passed, the result is a new string object, built from the buffer, but with a length that reflects the data actually read.

- overlapped=None : PyOVERLAPPED

 An overlapped structure

#### Comments

 in a multi-threaded overlapped environment, it is likely to be necessary to pre-allocate the read buffer using the win32file::AllocateReadBuffer method, otherwise the I/O operation may complete before you can assign to the resulting buffer.

#### Return Value

The result is a tuple of (hr, string/PyOVERLAPPEDReadBuffer), where hr may be 0, ERROR_MORE_DATA or ERROR_IO_PENDING. If the overlapped param is not None, then the result is a PyOVERLAPPEDReadBuffer. Once the overlapped IO operation has completed, you can convert this to a string (str(object)) [py2k] or (bytes(object)) [py3k] to obtain the data. While the operation is in progress, you can use the slice operations (object[:end]) to obtain the data read so far. You must use the OVERLAPPED API functions to determine how much of the data is valid.


---

<!-- page: win32file__RemoveDirectory_meth.html -->

## win32file.RemoveDirectory

 RemoveDirectory(PathName, Transaction)

Removes an existing directory

#### Parameters

- PathName : string

 Name of directory to be removed

- Transaction=None : PyHANDLE

 Handle to a transaction (optional). See win32transaction::CreateTransaction.

#### Comments

 If a transaction handle is passed in, RemoveDirectoryTransacted will be called

 Accepts keyword arguments.

#### Win32 API References

- Search for RemoveDirectory at [msdn](https://learn.microsoft.com/en-ca/search/?terms=RemoveDirectory), [google](https://www.google.com/search?q=RemoveDirectory) or [google groups](https://groups.google.com/groups?q=RemoveDirectory).

- Search for RemoveDirectoryTransacted at [msdn](https://learn.microsoft.com/en-ca/search/?terms=RemoveDirectoryTransacted), [google](https://www.google.com/search?q=RemoveDirectoryTransacted) or [google groups](https://groups.google.com/groups?q=RemoveDirectoryTransacted).


---

<!-- page: win32file__RemoveUsersFromEncryptedFile_meth.html -->

## win32file.RemoveUsersFromEncryptedFile

 RemoveUsersFromEncryptedFile(FileName, pHashes)

Removes specified certificates from file - if certificate is not found, it is ignored

#### Parameters

- FileName : string

 File from which to remove users

- pHashes : ((PySID,bytes,string),...)

 Sequence representing an ENCRYPTION_CERTIFICATE_HASH_LIST structure, as returned by QueryUsersOnEncryptedFile


---

<!-- page: win32file__ReplaceFile_meth.html -->

## win32file.ReplaceFile

 ReplaceFile(ReplacedFileName, ReplacementFileName, BackupFileName, ReplaceFlags, Exclude, Reserved)

Replaces one file with another

#### Parameters

- ReplacedFileName : string

 File to be replaced

- ReplacementFileName : string

 File that will replace it

- BackupFileName=None : string

 Place at which to create a backup of the replaced file, can be None

- ReplaceFlags=0 : int

 Combination of REPLACEFILE_* flags

- Exclude=None : None

 Reserved, use None if passed in

- Reserved=None : None

 Reserved, use None if passed in


---

<!-- page: win32file__SetCommBreak_meth.html -->

## win32file.SetCommBreak

 SetCommBreak(handle)

Suspends character transmission for a specified communications device and places the transmission line in a break state until the win32file::ClearCommBreak function is called.

#### Parameters

- handle : PyHANDLE

 The handle to the communications device.


---

<!-- page: win32file__SetCommMask_meth.html -->

## win32file.SetCommMask

 int = SetCommMask(handle, val )

Sets the value of the event mask for a specified communications device.

#### Parameters

- handle : PyHANDLE

 The handle to the communications device.

- val : int

 The new mask value.


---

<!-- page: win32file__SetCommState_meth.html -->

## win32file.SetCommState

 SetCommState(handle, dcb)

Configures a communications device according to the specifications in a device-control block. The function reinitializes all hardware and control settings, but it does not empty output or input queues.

#### Parameters

- handle : PyHANDLE

 The handle to the communications device.

- dcb : PyDCB

 The control settings.


---

<!-- page: win32file__SetCommTimeouts_meth.html -->

## win32file.SetCommTimeouts

 int = SetCommTimeouts(handle, val )

Sets the time-out parameters for all read and write operations on a specified communications device.

#### Parameters

- handle : PyHANDLE

 The handle to the communications device.

- val : PyCOMMTIMEOUTS

 The new time-out parameters.


---

<!-- page: win32file__SetCurrentDirectory_meth.html -->

## win32file.SetCurrentDirectory

 SetCurrentDirectory(lpPathName)

Sets the current directory.

#### Parameters

- lpPathName : str/string

 Name of the path to set current.


---

<!-- page: win32file__SetEndOfFile_meth.html -->

## win32file.SetEndOfFile

 SetEndOfFile(hFile)

Moves the end-of-file (EOF) position for the specified file to the current position of the file pointer.

#### Parameters

- hFile : PyHANDLE

 handle of file whose EOF is to be set


---

<!-- page: win32file__SetFileApisToANSI_meth.html -->

## win32file.SetFileApisToANSI

 SetFileApisToANSI()

Causes a set of Win32 file functions to use the ANSI character set code page. This function is useful for 8-bit console input and output operations.


---

<!-- page: win32file__SetFileApisToOEM_meth.html -->

## win32file.SetFileApisToOEM

 SetFileApisToOEM()

Causes a set of Win32 file functions to use the OEM character set code page. This function is useful for 8-bit console input and output operations.


---

<!-- page: win32file__SetFileAttributesW_meth.html -->

## win32file.SetFileAttributesW

 SetFileAttributesW(FileName, FileAttributes, Transaction)

Sets a file's attributes

#### Parameters

- FileName : string

 File or directory whose attributes are to be changed

- FileAttributes : int

 Combination of FILE_ATTRIBUTE_* flags

- Transaction=None : PyHANDLE

 Handle to the transaction. See win32transaction::CreateTransaction.

#### Comments

 If Transaction is not None, SetFileAttributesTransacted will be called

 Accepts keyword arguments.

#### Win32 API References

- Search for SetFileAttributes at [msdn](https://learn.microsoft.com/en-ca/search/?terms=SetFileAttributes), [google](https://www.google.com/search?q=SetFileAttributes) or [google groups](https://groups.google.com/groups?q=SetFileAttributes).

- Search for SetFileAttributesTransacted at [msdn](https://learn.microsoft.com/en-ca/search/?terms=SetFileAttributesTransacted), [google](https://www.google.com/search?q=SetFileAttributesTransacted) or [google groups](https://groups.google.com/groups?q=SetFileAttributesTransacted).


---

<!-- page: win32file__SetFileAttributes_meth.html -->

## win32file.SetFileAttributes

 SetFileAttributes(filename, newAttributes)

Changes a file's attributes.

#### Parameters

- filename : string

 filename

- newAttributes : int

 attributes to set


---

<!-- page: win32file__SetFileInformationByHandle_meth.html -->

## win32file.SetFileInformationByHandle

 SetFileInformationByHandle(File, FileInformationClass, Information)

Changes file characteristics by file handle

#### Parameters

- File : PyHANDLE

 Handle to a file or directory. Do not pass a pipe handle.

- FileInformationClass : int

 Type of data, one of win32file.File*Info values

- Information : object

 Type is dependent on the class to be changed

| | Class | Type of input
| |

---

 |

---

| | FileBasicInfo | Dict representing a FILE_BASIC_INFO struct, containing {"CreationTime":PyDateTime, "LastAccessTime":PyDateTime, "LastWriteTime":PyDateTime, "ChangeTime":PyDateTime, "FileAttributes":int}
| | FileRenameInfo | Dict representing a FILE_RENAME_INFO struct, containing {"ReplaceIfExists":boolean, "RootDirectory":PyHANDLE, "FileName":str} MSDN says the RootDirectory is "A handle to the root directory in which the file to be renamed is located". However, this is actually the destination dir, can be None to stay in same dir.
| | FileDispositionInfo | Boolean indicating if file should be deleted when handle is closed
| | FileAllocationInfo | Int giving the allocation size.
| | FileEndOfFileInfo | Int giving the EOF position, cannot be greater than allocated size.
| | FileIoPriorityHintInfo | Int containing the IO priority (IoPriorityHint*)

#### Comments

 Accepts keyword args.


---

<!-- page: win32file__SetFilePointer_meth.html -->

## win32file.SetFilePointer

 SetFilePointer(handle, offset, moveMethod)

Moves the file pointer of an open file.

#### Parameters

- handle : PyHANDLE

 The file to perform the operation on.

- offset : Py_LARGEINTEGER

 Offset to move the file pointer.

- moveMethod : int

 Starting point for the file pointer move. This parameter can be one of the following values.

| | Value | Meaning
| |

---

 |

---

| | FILE_BEGIN | The starting point is zero or the beginning of the file.
| | FILE_CURRENT | The starting point is the current value of the file pointer.
| | FILE_END | The starting point is the current end-of-file position.


---

<!-- page: win32file__SetFileShortName_meth.html -->

## win32file.SetFileShortName

 SetFileShortName(hFile, ShortName)

Set the 8.3 name of a file

#### Parameters

- hFile : PyHANDLE

 Handle to a file or directory

- ShortName : string

 The 8.3 name to be applied to the file

#### Comments

 File handle must be opened with FILE_FLAG_BACKUP_SEMANTICS, and SE_RESTORE_NAME privilege must be enabled


---

<!-- page: win32file__SetFileTime_meth.html -->

## win32file.SetFileTime

 SetFileTime(File, CreationTime, LastAccessTime, LastWriteTime, UTCTimes)

Sets the date and time that a file was created, last accessed, or last modified.

#### Parameters

- File : PyHANDLE

 Previously opened handle (opened with FILE_WRITE_ATTRIBUTES access).

- CreationTime=None : PyDateTime

 File created time. None for no change.

- LastAccessTime=None : PyDateTime

 File access time. None for no change.

- LastWriteTime=None : PyDateTime

 File written time. None for no change.

- UTCTimes=False : boolean

 If True, input times are treated as UTC and no conversion is done, otherwise they are treated as local times. Defaults to False for backward compatibility. This parameter is ignored in Python 3, where you should always pass datetime objects with timezone information.


---

<!-- page: win32file__SetMailslotInfo_meth.html -->

## win32file.SetMailslotInfo

 SetMailslotInfo(Mailslot, ReadTimeout)

Sets a mailslot's timeout

#### Parameters

- Mailslot : PyHANDLE

 Handle to a mailslot

- ReadTimeout : int

 Timeout in milliseconds, use -1 for no timeout

#### Win32 API References

- Search for SetMailslotInfo at [msdn](https://learn.microsoft.com/en-ca/search/?terms=SetMailslotInfo), [google](https://www.google.com/search?q=SetMailslotInfo) or [google groups](https://groups.google.com/groups?q=SetMailslotInfo).


---

<!-- page: win32file__SetVolumeLabel_meth.html -->

## win32file.SetVolumeLabel

 SetVolumeLabel(rootPathName, volumeName)

Sets a volume label for a disk drive.

#### Parameters

- rootPathName : string

 address of name of root directory for volume

- volumeName : string

 name for the volume


---

<!-- page: win32file__SetVolumeMountPoint_meth.html -->

## win32file.SetVolumeMountPoint

 string = SetVolumeMountPoint(VolumeMountPoint, VolumeName )

Mounts the specified volume at the specified volume mount point.

#### Parameters

- VolumeMountPoint : string

 The mount point - must be an existing empty directory on an NTFS volume

- VolumeName : string

 The volume to mount there

#### Comments

 Accepts keyword args.

 Note that both parameters must have trailing backslashes.

#### Example

Usage

```
SetVolumeMountPoint('h:\\tmp\\','c:\\')




```

#### Return Value

The result is the GUID of the volume mounted, as a string.


---

<!-- page: win32file__SetupComm_meth.html -->

## win32file.SetupComm

 SetupComm(handle, dwInQueue, dwOutQueue)

Initializes the communications parameters for a specified communications device.

#### Parameters

- handle : PyHANDLE

 The handle to the communications device.

- dwInQueue : int

 Specifies the recommended size, in bytes, of the device's internal input buffer.

- dwOutQueue : int

 Specifies the recommended size, in bytes, of the device's internal output buffer.


---

<!-- page: win32file__SfcGetNextProtectedFile_meth.html -->

## win32file.SfcGetNextProtectedFile

 [string,...] = SfcGetNextProtectedFile()

Returns list of protected operating system files

#### Win32 API References

- Search for SfcGetNextProtectedFile at [msdn](https://learn.microsoft.com/en-ca/search/?terms=SfcGetNextProtectedFile), [google](https://www.google.com/search?q=SfcGetNextProtectedFile) or [google groups](https://groups.google.com/groups?q=SfcGetNextProtectedFile).


---

<!-- page: win32file__SfcIsFileProtected_meth.html -->

## win32file.SfcIsFileProtected

 boolean = SfcIsFileProtected(ProtFileName)

Checks if a file is protected

#### Parameters

- ProtFileName : string

 Name of file to be checked


---

<!-- page: win32file__TransmitCommChar_meth.html -->

## win32file.TransmitCommChar

 TransmitCommChar(handle, cChar)

Transmits a specified character ahead of any pending data in the output buffer of the specified communications device.

#### Parameters

- handle : PyHANDLE

 The handle to the communications device.

- cChar : char

 The character to transmit.

#### Comments

 The TransmitCommChar function is useful for sending an interrupt character (such as a CTRL+C) to a host system.
If the device is not transmitting, TransmitCommChar cannot be called repeatedly. Once TransmitCommChar places a character in the output buffer, the character must be transmitted before the function can be called again. If the previous character has not yet been sent, TransmitCommChar returns an error.


---

<!-- page: win32file__TransmitFile_meth.html -->

## win32file.TransmitFile

 TransmitFile(Socket, File, NumberOfBytesToWrite, NumberOfBytesPerSend, Overlapped, Flags, Head, Tail)

Transmits a file over a socket TransmitFile(sock, filehandle, bytes_to_write, bytes_per_send, overlap, flags [, (prepend_buf, postpend_buf)])

#### Parameters

- Socket : PySocket /int

 Socket that will be used to send the file

- File : PyHANDLE/int

 Handle to the file

- NumberOfBytesToWrite : int

 The number of bytes in the file to transmit, use 0 for entire file.

- NumberOfBytesPerSend : int

 The size, in bytes, of each block of data sent in each send operation.

- Overlapped : PyOVERLAPPED

 An overlapped structure, can be None.

- Flags : int

 A set of flags used to modify the behavior of the TransmitFile function call. (win32file.TF_*)

- Head=None : buffer

 Buffer to send on the socket before the file

- Tail=None : buffer

 Buffer to send on the socket after the file

#### Return Value

Returns 0 on completion, or ERROR_IO_PENDING if an overlapped operation has been queued


---

<!-- page: win32file__UnlockFileEx_meth.html -->

## win32file.UnlockFileEx

 UnlockFileEx(hFile, int, int, ol)

Unlocks a file. Wrapper for UnlockFileEx win32 API.

#### Parameters

- hFile : PyHANDLE/int

 Handle to the file

- int : nbytesLow

 low-order part of number of bytes to lock

- int : nbytesLow

 high-order part of number of bytes to lock

- ol=None : PyOVERLAPPED

 An overlapped structure


---

<!-- page: win32file__UnlockFile_meth.html -->

## win32file.UnlockFile

 UnlockFile(hFile, offsetLow, offsetHigh, nNumberOfBytesToUnlockLow, nNumberOfBytesToUnlockHigh)

Unlocks a region of a file locked by win32file::LockFile or win32file::LockFileEx

#### Parameters

- hFile : PyHANDLE

 handle of file to unlock

- offsetLow : int

 low-order word of lock region offset

- offsetHigh : int

 high-order word of lock region offset

- nNumberOfBytesToUnlockLow : int

 low-order word of length to unlock

- nNumberOfBytesToUnlockHigh : int

 high-order word of length to unlock


---

<!-- page: win32file__WSAAsyncSelect_meth.html -->

## win32file.WSAAsyncSelect

 WSAAsyncSelect(socket, hwnd, int, networkEvents)

Request windows message notification for the supplied set of FD_XXXX network events.

#### Parameters

- socket : PySocket

 socket to attach to the event

- hwnd : hwnd

 Window handle for the socket to become attached to.

- int : int

 Window message that will be posted.

- networkEvents : int

 A bitmask of network events that will cause wMsg to be posted. e.g. (FD_CLOSE | FD_READ)


---

<!-- page: win32file__WSAEnumNetworkEvents_meth.html -->

## win32file.WSAEnumNetworkEvents

 dict = WSAEnumNetworkEvents(s, hEvent )

Return network events that caused the event associated with the socket to be signaled.

#### Parameters

- s : PySocket

 Socket to check for netork events, previously registered for network event notification with WSAEventSelect.

- hEvent : PyHANDLE

 Optional handle to the event associated with socket s in the last call to WSAEventSelect. If specified, the event will be reset.

#### Return Value

A dictionary mapping network events that occurred for the specified socket since the last call to this function (e.g. FD_READ, FD_WRITE) to their associated error code, or 0 if the event occurred without an error. The events returned are a subset of events previously registered for this socket with WSAEventSelect.


---

<!-- page: win32file__WSAEventSelect_meth.html -->

## win32file.WSAEventSelect

 WSAEventSelect(socket, hEvent, networkEvents)

Specifies an event object to be associated with the supplied set of FD_XXXX network events.

#### Parameters

- socket : PySocket

 socket to attach to the event

- hEvent : PyHandle

 Event handle for the socket to become attached to.

- networkEvents : int

 A bitmask of network events that will cause hEvent to be signaled. e.g. (FD_CLOSE | FD_READ)


---

<!-- page: win32file__WSARecv_meth.html -->

## win32file.WSARecv

 (rc, cBytesRecvd) = WSARecv(s, buffer , ol , dwFlags )

Winsock recv() equivalent function for Overlapped I/O.

#### Parameters

- s : PySocket /int

 Socket to send data on.

- buffer : buffer

 Buffer to send data from.

- ol : PyOVERLAPPED

 An overlapped structure

- dwFlags : int

 Optional reception flags.


---

<!-- page: win32file__WSASend_meth.html -->

## win32file.WSASend

 (rc, cBytesSent) = WSASend(s, buffer , ol , dwFlags )

Winsock send() equivalent function for Overlapped I/O.

#### Parameters

- s : PySocket /int

 Socket to send data on.

- buffer : string/buffer

 Buffer to send data from.

- ol : PyOVERLAPPED

 An overlapped structure

- dwFlags : int

 Optional send flags.


---

<!-- page: win32file__WaitCommEvent_meth.html -->

## win32file.WaitCommEvent

 WaitCommEvent(handle, overlapped)

Waits for an event to occur for a specified communications device. The set of events that are monitored by this function is contained in the event mask associated with the device handle.

#### Parameters

- handle : PyHANDLE

 The handle to the communications device.

- overlapped : PyOVERLAPPED

 This structure is required if hFile was opened with FILE_FLAG_OVERLAPPED.
If hFile was opened with FILE_FLAG_OVERLAPPED, the lpOverlapped parameter must not be NULL. It must point to a valid OVERLAPPED structure. If hFile was opened with FILE_FLAG_OVERLAPPED and lpOverlapped is NULL, the function can incorrectly report that the operation is complete.
If hFile was opened with FILE_FLAG_OVERLAPPED and lpOverlapped is not NULL, WaitCommEvent is performed as an overlapped operation. In this case, the OVERLAPPED structure must contain a handle to a manual-reset event object (created by using the CreateEvent function).
If hFile was not opened with FILE_FLAG_OVERLAPPED, WaitCommEvent does not return until one of the specified events or an error occurs.

#### Comments

 If an overlapped structure is passed, then the PyOVERLAPPED::dword address is passed to the Win32 API as the mask. This means that once the overlapped operation has completed, this dword attribute can be used to determine the type of event that occurred.

#### Return Value

The result is a tuple of (rc, mask_val), where rc is zero for success, or the result of calling GetLastError() otherwise. The mask_val is the new mask value once the function has returned, but if an Overlapped object is passed, this value will generally be meaningless. See the comments for more details.


---

<!-- page: win32file__Wow64DisableWow64FsRedirection_meth.html -->

## win32file.Wow64DisableWow64FsRedirection

 int = Wow64DisableWow64FsRedirection()

Disables file system redirection for 32-bit processes running on a 64-bit system

#### Return Value

Returns a state value to be passed to win32file::Wow64RevertWow64FsRedirection


---

<!-- page: win32file__Wow64RevertWow64FsRedirection_meth.html -->

## win32file.Wow64RevertWow64FsRedirection

 Wow64RevertWow64FsRedirection(OldValue)

Reenables file system redirection for 32-bit processes running on a 64-bit system

#### Parameters

- OldValue : int

 State returned from Wow64DisableWow64FsRedirection


---

<!-- page: win32file__WriteEncryptedFileRaw_meth.html -->

## win32file.WriteEncryptedFileRaw

 WriteEncryptedFileRaw(ImportCallback, CallbackContext, Context)

Writes raw bytes to an encrypted file

#### Parameters

- ImportCallback : ImportCallBack

 Python function that supplies data to be written

- CallbackContext : object

 Arbitrary Python object to be passed to callback function

- Context : PyCObject

 Context object returned from win32file::OpenEncryptedFileRaw


---

<!-- page: win32file__WriteFile_meth.html -->

## win32file.WriteFile

 int, int = WriteFile(hFile, data , ol )

Writes a string to a file

#### Parameters

- hFile : PyHANDLE/int

 Handle to the file

- data : string/PyOVERLAPPEDReadBuffer

 The data to write.

- ol=None : PyOVERLAPPED

 An overlapped structure

#### Comments

 If you use an overlapped buffer, then it is your responsibility to ensure the string object passed remains valid until the operation completes. If Python garbage collection reclaims the buffer before the win32 API has finished with it, the results are unpredictable.

#### Return Value

The result is a tuple of (errCode, nBytesWritten). If errCode is not zero, it will be ERROR_IO_PENDING (ie, it is an overlapped request).
Any other error will raise an exception.


---

<!-- page: win32file___get_osfhandle_meth.html -->

## win32file._get_osfhandle

 long = _get_osfhandle(fd)

Gets operating-system file handle associated with existing stream

#### Parameters

- fd : int

 File descriptor as returned by file.fileno()


---

<!-- page: win32file___getmaxstdio_meth.html -->

## win32file._getmaxstdio

 int = _getmaxstdio()

Returns the maximum number of CRT io streams.


---

<!-- page: win32file___open_osfhandle_meth.html -->

## win32file._open_osfhandle

 int = _open_osfhandle(osfhandle, flags )

Associates a C run-time file handle with a existing operating-system file handle.

#### Parameters

- osfhandle : PyHANDLE

 An open file handle

- flags : int

 O_APPEND,O_RDONLY, or O_TEXT


---

<!-- page: win32file___setmaxstdio_meth.html -->

## win32file._setmaxstdio

 int = _setmaxstdio(newmax)

Set the maximum allowed number of open stdio handles

#### Parameters

- newmax : int

 Maximum number of open stdio streams, 2048 max

#### Return Value

Returns the number that was set, or -1 on failure.
