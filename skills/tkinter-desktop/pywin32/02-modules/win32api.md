# 模块 win32api

> 来源：https://mhammond.github.io/pywin32/win32api.html （及其成员页，已全部内联）

## Module win32api

 A module, encapsulating the Windows Win32 API.

#### Methods

- AbortSystemShutdown

 Aborts a system shutdown

- InitiateSystemShutdown

 Initiates a shutdown and optional restart of the specified computer.

- Apply

 Calls a Python function, but traps Win32 exceptions.

- Beep

 Generates a simple tone on the speaker.

- BeginUpdateResource

 Begins an update cycle for a PE file.

- ChangeDisplaySettings

 Changes video mode for default display

- ChangeDisplaySettingsEx

 Changes video mode for specified display

- ClipCursor

 Confines the cursor to a rectangular area on the screen.

- CloseHandle

 Closes an open handle.

- CommandLineToArgv

 Parses a Unicode command line string and returns a list of command line arguments, in a way that is similar to sys.argv.

- CopyFile

 Copy a file.

- DebugBreak

 Breaks into the C debugger.

- DeleteFile

 Deletes the specified file.

- DragQueryFile

 Retrieve the file names for dropped files.

- DragFinish

 Free memory associated with dropped files.

- DuplicateHandle

 Duplicates a handle.

- EndUpdateResource

 Ends a resource update cycle of a PE file.

- EnumDisplayDevices

 Obtain information about the display devices in a system

- EnumDisplayMonitors

 Lists monitors for a device context

- EnumDisplaySettings

 Lists available modes for specified device

- EnumDisplaySettingsEx

 Lists available modes for a display device, with optional flags

- EnumResourceLanguages

 List languages for specified resource

- EnumResourceNames

 Enumerates all the resources of the specified type from the nominated file.

- EnumResourceTypes

 Return list of all resource types contained in module

- ExpandEnvironmentStrings

 Expands environment-variable strings and replaces them with their defined values.

- ExitWindows

 Logs off the current user

- ExitWindowsEx

 either logs off the current user, shuts down the system, or shuts down and restarts the system.

- FindFiles

 Find files matching a file spec.

- FindFirstChangeNotification

 Creates a change notification handle and sets up initial change notification filter conditions.

- FindNextChangeNotification

 Requests that the operating system signal a change notification handle the next time it detects an appropriate change.

- FindCloseChangeNotification

 Closes the change notification handle.

- FindExecutable

 Find an executable associated with a document.

- FormatMessage

 Return an error message string.

- FormatMessageW

 Return an error message string (as a Unicode object).

- FreeLibrary

 Decrements the reference count of the loaded dynamic-link library (DLL) module.

- GenerateConsoleCtrlEvent

 Send a specified signal to a console process group that shares the console associated with the calling process.

- GetAsyncKeyState

 Retrieves the asynch state of a virtual key code.

- GetCommandLine

 Return the application's command line.

- GetComputerName

 Returns the local computer name

- GetComputerNameEx

 Retrieves a NetBIOS or DNS name associated with the local computer

- GetComputerObjectName

 Retrieves the local computer's name in a specified format

- GetMonitorInfo

 Retrieves information for a monitor by handle

- GetUserName

 Returns the current user name.

- GetUserNameEx

 Returns the current user name in format specified by Name* constants

- GetCursorPos

 Returns the position of the cursor, in screen co-ordinates.

- GetCurrentThread

 Returns a pseudohandle for the current thread.

- GetCurrentThreadId

 Returns the thread ID for the current thread.

- GetCurrentProcessId

 Returns the thread ID for the current thread.

- GetCurrentProcess

 Returns a pseudohandle for the current process.

- GetConsoleTitle

 Return the application's console title.

- GetDateFormat

 Formats a date as a date string for a specified locale.

- GetDiskFreeSpace

 Retrieves information about a disk.

- GetDiskFreeSpaceEx

 Retrieves information about a disk.

- GetDllDirectory

 Retrieves the DLL search path

- GetDomainName

 Returns the current domain name

- GetEnvironmentVariable

 Retrieves the value of an environment variable.

- GetEnvironmentVariableW

 Retrieves the value of an environment variable.

- GetFileAttributes

 Retrieves the attributes for the named file.

- GetFileVersionInfo

 Retrieves string version info

- GetFocus

 Retrieves the handle of the keyboard focus window associated with the thread that called the method.

- GetFullPathName

 Returns the full path of a (possibly relative) path

- GetHandleInformation

 Retrieves a handle's flags.

- GetKeyboardLayout

 Retrieves the active input locale identifier

- GetKeyboardLayoutList

 Returns a sequence of all locale ids in the system

- GetKeyboardLayoutName

 Retrieves the name of the active input locale identifier (formerly called the keyboard layout).

- GetKeyboardState

 Retrieves the status of the 256 virtual keys on the keyboard.

- GetKeyState

 Retrives the last known key state for a key.

- GetLastError

 Retrieves the last error code known by the system.

- GetLastInputInfo

 Returns time of last input event in tick count

- GetLocalTime

 Returns the current local time.

- GetLongPathName

 Converts the specified path to its long form.

- GetLongPathNameW

 Converts the specified path to its long form.

- GetLogicalDrives

 Returns a bitmask representing the currently available disk drives.

- GetLogicalDriveStrings

 Returns a list of strings for all the drives.

- GetModuleFileName

 Retrieves the filename of the specified module.

- GetModuleFileNameW

 Retrieves the unicode filename of the specified module.

- GetModuleHandle

 Returns the handle of an already loaded DLL.

- GetPwrCapabilities

 Retrieves system's power capabilities

- GetProfileSection

 Returns a list of entries in an INI file.

- GetProcAddress

 Returns the address of the specified exported dynamic-link library (DLL) function.

- GetProfileVal

 Returns a value from an INI file.

- GetShortPathName

 Returns the 8.3 version of a pathname.

- GetStdHandle

 Returns a handle for the standard input, standard output, or standard error device

- GetSysColor

 Returns the system colors.

- GetSystemDefaultLangID

 Retrieves the system default language identifier.

- GetSystemDefaultLCID

 Retrieves the system default locale identifier.

- GetSystemDirectory

 Returns the Windows system directory.

- GetSystemFileCacheSize

 Returns the amount of memory reserved for file cache

- SetSystemFileCacheSize

 Sets the amount of memory reserved for file cache

- GetSystemInfo

 Retrieves information about the current system.

- GetNativeSystemInfo

 Retrieves information about the current system for a Wow64 process.

- GetSystemMetrics

 Returns the specified system metrics.

- GetSystemCpuSetInformation

 Returns CPU topology information for all logical processors.

- GetSystemPowerStatus

 Retrieves the power status of the system

- GetSystemTime

 Returns the current system time.

- GetTempFileName

 Creates a temporary file.

- GetTempPath

 Returns the path designated as holding temporary files.

- GetThreadLocale

 Returns the current thread's locale.

- GetTickCount

 Returns the milliseconds since windows started.

- GetTimeFormat

 Formats a time as a time string for a specified locale.

- GetTimeZoneInformation

 Returns the system time-zone information.

- GetVersion

 Returns Windows version information.

- GetVersionEx

 Returns Windows version information as a tuple.

- GetVolumeInformation

 Returns information about a volume and file system attached to the system.

- GetWindowsDirectory

 Returns the windows directory.

- GetWindowLong

 Retrieves a long value at the specified offset into the extra window memory of the given window.

- GetUserDefaultLangID

 Retrieves the user default language identifier.

- GetUserDefaultLCID

 Retrieves the user default locale identifier.

- GlobalMemoryStatus

 Returns systemwide memory usage

- GlobalMemoryStatusEx

 Returns physical and virtual memory usage

- keybd_event

 Simulate a keyboard event

- mouse_event

 Simulate a mouse event

- LoadCursor

 Loads a cursor.

- LoadKeyboardLayout

 Loads a new locale id

- LoadLibrary

 Loads the specified DLL, and returns the handle.

- LoadLibraryEx

 Loads the specified DLL, and returns the handle.

- LoadResource

 Finds and loads a resource from a PE file.

- LoadString

 Loads a string from a resource file.

- MapVirtualKeyEx

 Translates (maps) a virtual-key code into a scan code or character value, or translates a scan code into a virtual-key code.

- MessageBeep

 Plays a predefined waveform sound.

- MessageBox

 Display a message box.

- MonitorFromPoint

 Finds monitor that contains a point

- MonitorFromRect

 Finds monitor that has largest intersection with a rectangle

- MonitorFromWindow

 Finds monitor that contains a window

- MoveFile

 Moves or renames a file.

- MoveFileEx

 Moves or renames a file.

- OpenProcess

 Retrieves a handle to an existing process.

- OpenProcess

 Retrieves a handle to an existing thread.

- OutputDebugString

 Writes output to the Windows debugger.

- PostMessage

 Post a message to a window.

- PostQuitMessage

 Posts a quit message.

- PostThreadMessage

 Post a message to a thread.

- RegCloseKey

 Closes a registry key.

- RegConnectRegistry

 Establishes a connection to a predefined registry handle on another computer.

- RegCopyTree

 Copies an entire registry key to another location

- RegCreateKey

 Creates the specified key, or opens the key if it already exists.

- RegCreateKeyEx

 Extended version of RegCreateKey

- RegDeleteKey

 Deletes the specified key.

- RegDeleteKeyEx

 Deletes a registry key from 32 or 64 bit registry view

- RegDeleteTree

 Recursively deletes a key's subkeys and values

- RegDeleteValue

 Removes a named value from the specified registry key.

- RegEnumKey

 Enumerates subkeys of the specified open registry key.

- RegEnumKeyEx

 Enumerates subkeys of the specified open registry key.

- RegEnumKeyExW

 Unicode version of RegEnumKeyEx

- RegEnumValue

 Enumerates values of the specified open registry key.

- RegFlushKey

 Writes all the attributes of the specified key to the registry.

- RegGetKeySecurity

 Retrieves the security on the specified registry key.

- RegLoadKey

 Creates a subkey under HKEY_USER or HKEY_LOCAL_MACHINE and stores registration information from a specified file into that subkey.

- RegOpenCurrentUser

 Opens HKEY_CURRENT_USER for impersonated user

- RegOpenKey

 Alias for win32api::RegOpenKeyEx

- RegOpenKeyEx

 Opens the specified key.

- RegOpenKeyTransacted

 Opens a registry key as part of a transaction.

- RegOverridePredefKey

 Redirects one of the predefined keys to different key.

- RegQueryValue

 Retrieves the value associated with the unnamed value for a specified key in the registry.

- RegQueryValueEx

 Retrieves the type and data for a specified value name associated with an open registry key.

- RegQueryInfoKey

 Returns information about the specified key.

- RegQueryInfoKeyW

 Returns information about an open registry key

- RegRestoreKey

 Restores a key and subkeys from a saved registry file

- RegSaveKey

 Saves the specified key, and all its subkeys to the specified file.

- RegSaveKeyEx

 Extended version of RegSaveKey

- RegSetKeySecurity

 Sets the security on the specified registry key.

- RegSetValue

 Associates a value with a specified key. Currently, only strings are supported.

- RegSetValueEx

 Stores data in the value field of an open registry key.

- RegUnLoadKey

 Unloads the specified registry key and its subkeys from the registry. The keys must have been loaded previously by a call to RegLoadKey.

- RegisterWindowMessage

 Given a string, return a system wide unique message ID.

- RegNotifyChangeKeyValue

 Watch for registry changes

- SearchPath

 Searches a path for a file.

- SendMessage

 Send a message to a window.

- SetConsoleCtrlHandler

 Adds or removes an application-defined HandlerRoutine function from the list of handler functions for the calling process.

- SetConsoleTitle

 Sets the title for the current console.

- SetCursorPos

 The SetCursorPos function moves the cursor to the specified screen coordinates.

- SetDllDirectory

 Modifies the application-specific DLL search path

- SetErrorMode

 Controls whether the system will handle the specified types of serious errors, or whether the process will handle them.

- SetFileAttributes

 Sets the named file's attributes.

- SetLastError

 Sets the last error code known for the current thread.

- SetSysColors

 Changes color of various window elements

- SetLocalTime

 Changes the system's local time.

- SetSystemTime

 Sets the system time.

- SetClassLong

 Replaces the specified 32-bit (long) value at the specified offset into the extra class memory for the window.

- SetClassWord

 Replaces the specified 32-bit (long) value at the specified offset into the extra class memory for the window.

- SetWindowWord

- SetCursor

 Set the cursor to the HCURSOR object.

- SetEnvironmentVariable

 Creates, deletes, or changes the value of an environment variable.

- SetEnvironmentVariableW

 Creates, deletes, or changes the value of an environment variable.

- SetHandleInformation

 Sets a handles's flags

- SetStdHandle

 Sets a handle for the standard input, standard output, or standard error device

- SetSystemPowerState

 Powers machine down to a suspended state

- SetThreadLocale

 Sets the current thread's locale.

- SetTimeZoneInformation

 Sets the system time-zone information.

- SetWindowLong

 Places a long value at the specified offset into the extra window memory of the given window.

- ShellExecute

 Executes an application.

- ShowCursor

 The ShowCursor method displays or hides the cursor.

- Sleep

 Suspends current application execution

- TerminateProcess

 Terminates a process.

- ToAsciiEx

 Translates the specified virtual-key code and keyboard state to the corresponding character or characters.

- UpdateResource

 Updates a resource in a PE file.

- VkKeyScan

 Translates a character to the corresponding virtual-key code and shift state.

- VkKeyScan

 Translates a character to the corresponding virtual-key code and shift state.

- WinExec

 Execute a program.

- WinHelp

 Invokes the Windows Help engine.

- WriteProfileSection

 Writes a complete section to an INI file or registry.

- WriteProfileVal

 Write a value to a Windows INI file.

- HIBYTE

 An interface to the win32api HIBYTE macro.

- LOBYTE

 An interface to the win32api LOBYTE macro.

- HIWORD

 An interface to the win32api HIWORD macro.

- LOWORD

 An interface to the win32api LOWORD macro.

- RGB

 An interface to the win32api RGB macro.

- MAKELANGID

 Creates a language identifier from a primary language identifier and a sublanguage identifier.

- MAKEWORD

 creates a WORD value by concatenating the specified values.

- MAKELONG

 creates a LONG value by concatenating the specified values.


---

# win32api 成员详细文档（共 205 项）


---

<!-- page: win32api__AbortSystemShutdown_meth.html -->

## win32api.AbortSystemShutdown

 AbortSystemShutdown(computerName)

Aborts a system shutdown

#### Parameters

- computerName : string/PyUnicode

 Specifies the name of the computer where the shutdown is to be stopped.

#### Win32 API References

- Search for AbortSystemShutdown at [msdn](https://learn.microsoft.com/en-ca/search/?terms=AbortSystemShutdown), [google](https://www.google.com/search?q=AbortSystemShutdown) or [google groups](https://groups.google.com/groups?q=AbortSystemShutdown).


---

<!-- page: win32api__Apply_meth.html -->

## win32api.Apply

 object = Apply(exceptionHandler, func , args )

Calls a Python function, but traps Win32 exceptions.

#### Parameters

- exceptionHandler : object

 An object which will be called when a win32 exception occurs.

- func : object

 The function call call under the protection of the Win32 exception handler.

- args : tuple

 Args for the function.

#### Comments

 Calls the specified function in a manner similar to the built-in function apply(), but allows Win32 exceptions to be handled by Python. If a Win32 exception occurs calling the function, the specified exceptionHandler is called, and its return value determines the action taken.

| | Return value | Description
| |

---

 |

---

| | Tuple of (exc_type, exc_value) | This exception is raised to the Python caller of Apply() - This is conceptually similar to "raise exc_type, exc_value", although exception handlers must not themselves raise exceptions (see below).
| | Integer | Must be one of the win32 exception constants, and this value is returned to Win32. See the Win32 documentation for details.
| | None | The exception is considered not handled (ie, it is as if no exception handler exists). If a Python exception occurs in the Win32 exception handler, it is as if None were returned (ie, no tracebacks or other diagnostics are printed)


---

<!-- page: win32api__Beep_meth.html -->

## win32api.Beep

 Beep(freq, dur)

Generates simple tones on the speaker.

#### Parameters

- freq : int

 Specifies the frequency, in hertz, of the sound. This parameter must be in the range 37 through 32,767 (0x25 through 0x7FFF).

- dur : int

 Specifies the duration, in milliseconds, of the sound.~ One value has a special meaning: If dwDuration is - 1, the function operates asynchronously and produces sound until called again.

#### Win32 API References

- Search for Beep at [msdn](https://learn.microsoft.com/en-ca/search/?terms=Beep), [google](https://www.google.com/search?q=Beep) or [google groups](https://groups.google.com/groups?q=Beep).


---

<!-- page: win32api__BeginUpdateResource_meth.html -->

## win32api.BeginUpdateResource

 PyHANDLE = BeginUpdateResource(filename, delete )

Begins an update cycle for a PE file.

#### Parameters

- filename : string

 File in which to update resources.

- delete : int

 Flag to indicate that all existing resources should be deleted.


---

<!-- page: win32api__ChangeDisplaySettingsEx_meth.html -->

## win32api.ChangeDisplaySettingsEx

 int = ChangeDisplaySettingsEx(DeviceName, DevMode , Flags )

Changes video mode for specified display

#### Parameters

- DeviceName=None : str

 Name of device as returned by win32api::EnumDisplayDevices, use None for default display device

- DevMode=None : PyDEVMODE

 A PyDEVMODE object as returned from win32api::EnumDisplaySettings, or None to reset to default settings from registry

- Flags=0 : int

 One of the win32con.CDS_* constants, or 0

#### Comments

 Accepts keyword arguments

#### Return Value

Returns DISP_CHANGE_SUCCESSFUL on success, or one of the DISP_CHANGE_* error constants on failure


---

<!-- page: win32api__ChangeDisplaySettings_meth.html -->

## win32api.ChangeDisplaySettings

 int = ChangeDisplaySettings(DevMode, Flags )

Changes video mode for default display

#### Parameters

- DevMode : PyDEVMODE

 A PyDEVMODE object as returned from EnumDisplaySettings, or None to reset to default settings from registry

- Flags : int

 One of the win32con.CDS_* constants, or 0

#### Return Value

Returns DISP_CHANGE_SUCCESSFUL on success, or one of the DISP_CHANGE_* error constants on failure


---

<!-- page: win32api__ClipCursor_meth.html -->

## win32api.ClipCursor

 ClipCursor(left, top, right, bottom)

Confines the cursor to a rectangular area on the screen.

#### Parameters

- left, top, right, bottom : (int, int, int, int)

 contains the screen coordinates of the upper-left and lower-right corners of the confining rectangle. If this parameter is omitted or (0,0,0,0), the cursor is free to move anywhere on the screen.

#### Win32 API References

- Search for ClipCursor at [msdn](https://learn.microsoft.com/en-ca/search/?terms=ClipCursor), [google](https://www.google.com/search?q=ClipCursor) or [google groups](https://groups.google.com/groups?q=ClipCursor).


---

<!-- page: win32api__CloseHandle_meth.html -->

## win32api.CloseHandle

 CloseHandle(handle)

Closes an open handle.

#### Parameters

- handle : PyHANDLE/int

 A previously opened handle.


---

<!-- page: win32api__CommandLineToArgv_meth.html -->

## win32api.CommandLineToArgv

 [string] = CommandLineToArgv(cmdLine)

Parses a command line string and returns a list of command line arguments, in a way that is similar to sys.argv.

#### Parameters

- cmdLine : string

 A string that contains the full command line. If this parameter is an empty string the function returns the path to the current executable file.


---

<!-- page: win32api__CopyFile_meth.html -->

## win32api.CopyFile

 CopyFile(src, dest, bFailOnExist)

Copies an existing file to a new file

#### Parameters

- src : string

 Name of an existing file.

- dest : string

 Name of file to copy to.

- bFailOnExist=0 : int

 Indicates if the operation should fail if the file exists.

#### Win32 API References

- Search for CopyFile at [msdn](https://learn.microsoft.com/en-ca/search/?terms=CopyFile), [google](https://www.google.com/search?q=CopyFile) or [google groups](https://groups.google.com/groups?q=CopyFile).


---

<!-- page: win32api__DebugBreak_meth.html -->

## win32api.DebugBreak

 DebugBreak()

Breaks into the C debugger

#### Win32 API References

- Search for DebugBreak at [msdn](https://learn.microsoft.com/en-ca/search/?terms=DebugBreak), [google](https://www.google.com/search?q=DebugBreak) or [google groups](https://groups.google.com/groups?q=DebugBreak).


---

<!-- page: win32api__DeleteFile_meth.html -->

## win32api.DeleteFile

 DeleteFile(fileName)

Deletes the specified file.

#### Parameters

- fileName : string

 File to delete.

#### Win32 API References

- Search for DeleteFile at [msdn](https://learn.microsoft.com/en-ca/search/?terms=DeleteFile), [google](https://www.google.com/search?q=DeleteFile) or [google groups](https://groups.google.com/groups?q=DeleteFile).


---

<!-- page: win32api__DragFinish_meth.html -->

## win32api.DragFinish

 DragFinish(hDrop)

Releases the memory stored by Windows for the filenames.

#### Parameters

- hDrop : int

 Handle identifying the structure containing the file names.

#### Win32 API References

- Search for DragFinish at [msdn](https://learn.microsoft.com/en-ca/search/?terms=DragFinish), [google](https://www.google.com/search?q=DragFinish) or [google groups](https://groups.google.com/groups?q=DragFinish).


---

<!-- page: win32api__DragQueryFile_meth.html -->

## win32api.DragQueryFile

 string/int = DragQueryFile(hDrop, fileNum )

Retrieves the file names of dropped files.

#### Parameters

- hDrop : int

 Handle identifying the structure containing the file names.

- fileNum=0xFFFFFFFF : int

 Specifies the index of the file to query.

#### Win32 API References

- Search for DragQueryFile at [msdn](https://learn.microsoft.com/en-ca/search/?terms=DragQueryFile), [google](https://www.google.com/search?q=DragQueryFile) or [google groups](https://groups.google.com/groups?q=DragQueryFile).

#### Return Value

If the fileNum parameter is 0xFFFFFFFF (the default) then the return value is an integer with the count of files dropped. If fileNum is between 0 and Count, the return value is a string containing the filename.
 If an error occurs, and exception is raised.


---

<!-- page: win32api__DuplicateHandle_meth.html -->

## win32api.DuplicateHandle

 PyHANDLE = DuplicateHandle(hSourceProcess, hSource , hTargetProcessHandle , desiredAccess , bInheritHandle , options )

Duplicates a handle.

#### Parameters

- hSourceProcess : PyHANDLE

 Identifies the process containing the handle to duplicate.

- hSource : PyHANDLE

 Identifies the handle to duplicate. This is an open object handle that is valid in the context of the source process.

- hTargetProcessHandle : PyHANDLE

 Identifies the process that is to receive the duplicated handle. The handle must have PROCESS_DUP_HANDLE access.

- desiredAccess : int

 Specifies the access requested for the new handle. This parameter is ignored if the dwOptions parameter specifies the DUPLICATE_SAME_ACCESS flag. Otherwise, the flags that can be specified depend on the type of object whose handle is being duplicated. For the flags that can be specified for each object type, see the following Remarks section. Note that the new handle can have more access than the original handle.

- bInheritHandle : int

 Indicates whether the handle is inheritable. If TRUE, the duplicate handle can be inherited by new processes created by the target process. If FALSE, the new handle cannot be inherited.

- options : int

 Specifies optional actions. This parameter can be zero, or any combination of the following flags

| | DUPLICATE_CLOSE_SOURCE | loses the source handle. This occurs regardless of any error status returned.
| | DUPLICATE_SAME_ACCESS | Ignores the dwDesiredAccess parameter. The duplicate handle has the same access as the source handle.

#### Comments

 When duplicating a handle for a different process, you should either keep a reference to the returned PyHANDLE, or call .Detach() on it to prevent it from being closed prematurely.


---

<!-- page: win32api__EndUpdateResource_meth.html -->

## win32api.EndUpdateResource

 EndUpdateResource(handle, discard)

Ends a resource update cycle of a PE file.

#### Parameters

- handle : PyHANDLE

 The update-file handle.

- discard : int

 Flag to discard all writes.


---

<!-- page: win32api__EnumDisplayDevices_meth.html -->

## win32api.EnumDisplayDevices

 PyDISPLAY_DEVICE = EnumDisplayDevices(Device, DevNum , Flags )

Obtain information about the display devices in a system

#### Parameters

- Device=None : string

 Name of device, use None to obtain information for the display adapter(s) on the machine, based on DevNum

- DevNum=0 : int

 Index of device of interest, starting with zero

- Flags=0 : int

 Reserved, use 0 if passed in

#### Comments

 Accepts keyword arguments


---

<!-- page: win32api__EnumDisplayMonitors_meth.html -->

## win32api.EnumDisplayMonitors

 list = EnumDisplayMonitors(hdc, rcClip )

Lists display monitors for a given device context and area

#### Parameters

- hdc=None : PyHANDLE

 Handle to device context, use None for virtual desktop

- rcClip=None : PyRECT

 Clipping rectangle, can be None

#### Comments

 Accepts keyword arguments

#### Return Value

Returns a sequence of tuples. For each monitor found, returns a handle to the monitor, device context handle, and intersection rectangle: (hMonitor, hdcMonitor, PyRECT)


---

<!-- page: win32api__EnumDisplaySettingsEx_meth.html -->

## win32api.EnumDisplaySettingsEx

 PyDEVMODE = EnumDisplaySettingsEx(DeviceName, ModeNum , Flags )

Lists available modes for a display device, with optional flags

#### Parameters

- DeviceName=None : string

 Name of device as returned by win32api::EnumDisplayDevices. Can be None for default display

- ModeNum : int

 Index of setting to return, or one of ENUM_CURRENT_SETTINGS, ENUM_REGISTRY_SETTINGS

- Flags=0 : int

 EDS_RAWMODE (2) is only defined flag

#### Comments

 Accepts keyword arguments


---

<!-- page: win32api__EnumDisplaySettings_meth.html -->

## win32api.EnumDisplaySettings

 PyDEVMODE = EnumDisplaySettings(DeviceName, ModeNum )

List available modes for specified display device

#### Parameters

- DeviceName=None : string

 Name of device as returned by win32api::EnumDisplayDevices, use None for default display device

- ModeNum=0 : int

 Index of setting to return, or one of ENUM_CURRENT_SETTINGS, ENUM_REGISTRY_SETTINGS

#### Comments

 Accepts keyword arguments


---

<!-- page: win32api__EnumResourceLanguages_meth.html -->

## win32api.EnumResourceLanguages

 [int,...] = EnumResourceLanguages(hmodule, lpType , lpName )

List languages for a resource

#### Parameters

- hmodule : PyHANDLE

 Handle to the module that contains resource

- lpType : PyResourceId

 Resource type, can be string or integer

- lpName : PyResourceId

 Resource name, can be string or integer


---

<!-- page: win32api__EnumResourceNames_meth.html -->

## win32api.EnumResourceNames

 [string, ...] = EnumResourceNames(hmodule, resType )

Enumerates all the resources of the specified type from the nominated file.

#### Parameters

- hmodule : PyHANDLE

 The handle to the module to enumerate.

- resType : PyResourceId

 The type of resource to enumerate. (win32con.RT_*). If passed as a string, form is '#' sign followed by decimal number. eg RT_ANICURSOR would be '#21'

#### Return Value

The result is a list of string or integers, one for each resource enumerated.


---

<!-- page: win32api__EnumResourceTypes_meth.html -->

## win32api.EnumResourceTypes

 [PyUnicode ,...] = EnumResourceTypes(hmodule)

Return name or integer id of all resource types contained in module

#### Parameters

- hmodule : PyHANDLE

 The handle to the module to enumerate.


---

<!-- page: win32api__ExitWindowsEx_meth.html -->

## win32api.ExitWindowsEx

 ExitWindowsEx(flags, reserved)

either logs off the current user, shuts down the system, or shuts down and restarts the system.

#### Parameters

- flags : int

 The shutdown operation

- reserved=0 : int

#### Comments

 It sends the WM_QUERYENDSESSION message to all applications to determine if they can be terminated.

#### Win32 API References

- Search for AbortSystemShutdown at [msdn](https://learn.microsoft.com/en-ca/search/?terms=AbortSystemShutdown), [google](https://www.google.com/search?q=AbortSystemShutdown) or [google groups](https://groups.google.com/groups?q=AbortSystemShutdown).


---

<!-- page: win32api__ExitWindows_meth.html -->

## win32api.ExitWindows

 ExitWindows(reserved1, reserved2)

Logs off the current user

#### Parameters

- reserved1=0 : int

- reserved2=0 : int

#### Win32 API References

- Search for AbortSystemShutdown at [msdn](https://learn.microsoft.com/en-ca/search/?terms=AbortSystemShutdown), [google](https://www.google.com/search?q=AbortSystemShutdown) or [google groups](https://groups.google.com/groups?q=AbortSystemShutdown).


---

<!-- page: win32api__ExpandEnvironmentStrings_meth.html -->

## win32api.ExpandEnvironmentStrings

 string = ExpandEnvironmentStrings(in)

Expands environment-variable strings and replaces them with their defined values.

#### Parameters

- in : string

 String to expand

#### Win32 API References

- Search for ExpandEnvironmentStrings at [msdn](https://learn.microsoft.com/en-ca/search/?terms=ExpandEnvironmentStrings), [google](https://www.google.com/search?q=ExpandEnvironmentStrings) or [google groups](https://groups.google.com/groups?q=ExpandEnvironmentStrings).


---

<!-- page: win32api__FindCloseChangeNotification_meth.html -->

## win32api.FindCloseChangeNotification

 FindCloseChangeNotification(handle)

Closes the change notification handle.

#### Parameters

- handle : int

 The handle returned from win32api::FindFirstChangeNotification


---

<!-- page: win32api__FindExecutable_meth.html -->

## win32api.FindExecutable

 (int, string) = FindExecutable(filename, dir )

Retrieves the name and handle of the executable (.EXE) file associated with the specified filename.

#### Parameters

- filename : string

 A file name. This can be either a document or executable file.

- dir : string

 The default directory.

#### Comments

 The function will raise an exception if it fails.

#### Win32 API References

- Search for FindExecutable at [msdn](https://learn.microsoft.com/en-ca/search/?terms=FindExecutable), [google](https://www.google.com/search?q=FindExecutable) or [google groups](https://groups.google.com/groups?q=FindExecutable).

#### Return Value

The return value is a tuple of (integer, string)
 The integer is the instance handle of the executable file associated with the specified filename. (This handle could also be the handle of a dynamic data exchange [DDE] server application.)
 The may contain the path to the DDE server started if no server responds to a request to initiate a DDE conversation.


---

<!-- page: win32api__FindFiles_meth.html -->

## win32api.FindFiles

 list = FindFiles(fileSpec)

Retrieves a list of matching filenames. An interface to the API FindFirstFile/FindNextFile/Find close functions.

#### Parameters

- fileSpec : string

 A string that specifies a valid directory or path and filename, which can contain wildcard characters (* and ?).

#### Win32 API References

- Search for FindFirstFile at [msdn](https://learn.microsoft.com/en-ca/search/?terms=FindFirstFile), [google](https://www.google.com/search?q=FindFirstFile) or [google groups](https://groups.google.com/groups?q=FindFirstFile).

- Search for FindNextFile at [msdn](https://learn.microsoft.com/en-ca/search/?terms=FindNextFile), [google](https://www.google.com/search?q=FindNextFile) or [google groups](https://groups.google.com/groups?q=FindNextFile).

- Search for FindClose at [msdn](https://learn.microsoft.com/en-ca/search/?terms=FindClose), [google](https://www.google.com/search?q=FindClose) or [google groups](https://groups.google.com/groups?q=FindClose).

#### Return Value

Returns a sequence of WIN32_FIND_DATA tuples


---

<!-- page: win32api__FindFirstChangeNotification_meth.html -->

## win32api.FindFirstChangeNotification

 int = FindFirstChangeNotification(pathName, bSubDirs , filter )

Creates a change notification handle and sets up initial change notification filter conditions.

#### Parameters

- pathName : string

 Specifies the path of the directory to watch.

- bSubDirs : int

 Specifies whether the function will monitor the directory or the directory tree. If this parameter is TRUE, the function monitors the directory tree rooted at the specified directory; if it is FALSE, it monitors only the specified directory

- filter : int

 Specifies the filter conditions that satisfy a change notification wait. This parameter can be one or more of the following values:

| | Value | Meaning
| |

---

 |

---

| | FILE_NOTIFY_CHANGE_FILE_NAME | Any file name change in the watched directory or subtree causes a change notification wait operation to return. Changes include renaming, creating, or deleting a file name.
| | FILE_NOTIFY_CHANGE_DIR_NAME | Any directory-name change in the watched directory or subtree causes a change notification wait operation to return. Changes include creating or deleting a directory.
| | FILE_NOTIFY_CHANGE_ATTRIBUTES | Any attribute change in the watched directory or subtree causes a change notification wait operation to return.
| | FILE_NOTIFY_CHANGE_SIZE | Any file-size change in the watched directory or subtree causes a change notification wait operation to return. The operating system detects a change in file size only when the file is written to the disk. For operating systems that use extensive caching, detection occurs only when the cache is sufficiently flushed.
| | FILE_NOTIFY_CHANGE_LAST_WRITE | Any change to the last write-time of files in the watched directory or subtree causes a change notification wait operation to return. The operating system detects a change to the last write-time only when the file is written to the disk. For operating systems that use extensive caching, detection occurs only when the cache is sufficiently flushed.
| | FILE_NOTIFY_CHANGE_SECURITY | Any security-descriptor change in the watched directory or subtree causes a change notification wait operation to return

#### Return Value

Although the result is a handle, the handle can not be closed via CloseHandle() - therefore a PyHandle object is not used.


---

<!-- page: win32api__FindNextChangeNotification_meth.html -->

## win32api.FindNextChangeNotification

 FindNextChangeNotification(handle)

Requests that the operating system signal a change notification handle the next time it detects an appropriate change.

#### Parameters

- handle : PyHANDLE

 The handle returned from win32api::FindFirstChangeNotification


---

<!-- page: win32api__FormatMessageW_meth.html -->

## win32api.FormatMessageW

 string = FormatMessageW(errCode)

Returns an error message from the system error file.

#### Parameters

- errCode=0 : int

 The error code to return the message for, If this value is 0, then GetLastError() is called to determine the error code.

#### Alternative Parameters

- flags

 Flags for the call. Note that FORMAT_MESSAGE_ALLOCATE_BUFFER and FORMAT_MESSAGE_ARGUMENT_ARRAY will always be added.

- source

 The source object. If flags contain FORMAT_MESSAGE_FROM_HMODULE it should be an int or PyHANDLE; if flags contain FORMAT_MESSAGE_FROM_STRING it should be a string; otherwise it is ignored.

- messageId

 The message ID.

- languageID

 The language ID.

- inserts

 The string inserts to insert.

#### Win32 API References

- Search for GetLastError at [msdn](https://learn.microsoft.com/en-ca/search/?terms=GetLastError), [google](https://www.google.com/search?q=GetLastError) or [google groups](https://groups.google.com/groups?q=GetLastError).

- Search for FormatMessage at [msdn](https://learn.microsoft.com/en-ca/search/?terms=FormatMessage), [google](https://www.google.com/search?q=FormatMessage) or [google groups](https://groups.google.com/groups?q=FormatMessage).


---

<!-- page: win32api__FreeLibrary_meth.html -->

## win32api.FreeLibrary

 FreeLibrary(hModule)

Decrements the reference count of the loaded dynamic-link library (DLL) module.

#### Parameters

- hModule : PyHANDLE

 Specifies the handle to the module.

#### Win32 API References

- Search for FreeLibrary at [msdn](https://learn.microsoft.com/en-ca/search/?terms=FreeLibrary), [google](https://www.google.com/search?q=FreeLibrary) or [google groups](https://groups.google.com/groups?q=FreeLibrary).


---

<!-- page: win32api__GenerateConsoleCtrlEvent_meth.html -->

## win32api.GenerateConsoleCtrlEvent

 int = GenerateConsoleCtrlEvent(controlEvent, processGroupId )

Send a specified signal to a console process group that shares the console associated with the calling process.

#### Parameters

- controlEvent : int

 Signal to generate.

- processGroupId : int

 Process group to get signal.

#### Win32 API References

- Search for GenerateConsoleCtrlEvent at [msdn](https://learn.microsoft.com/en-ca/search/?terms=GenerateConsoleCtrlEvent), [google](https://www.google.com/search?q=GenerateConsoleCtrlEvent) or [google groups](https://groups.google.com/groups?q=GenerateConsoleCtrlEvent).


---

<!-- page: win32api__GetAsyncKeyState_meth.html -->

## win32api.GetAsyncKeyState

 int = GetAsyncKeyState(key)

Retrieves the status of the specified key.

#### Parameters

- key : int

 Specifies one of 256 possible virtual-key codes.

#### Comments

 An application can use the virtual-key code constants win32con.VK_SHIFT, win32con.VK_CONTROL, and win32con.VK_MENU as values for the key parameter. This gives the state of the SHIFT, CTRL, or ALT keys without distinguishing between left and right. An application can also use the following virtual-key code constants as values for key to distinguish between the left and right instances of those keys:
win32con.VK_LSHIFT
win32con.VK_RSHIFT
win32con.VK_LCONTROL
win32con.VK_RCONTROL
win32con.VK_LMENU
win32con.VK_RMENU
The GetAsyncKeyState method works with mouse buttons. However, it checks on the state of the physical mouse buttons, not on the logical mouse buttons that the physical buttons are mapped to.

#### Win32 API References

- Search for GetAsyncKeyState at [msdn](https://learn.microsoft.com/en-ca/search/?terms=GetAsyncKeyState), [google](https://www.google.com/search?q=GetAsyncKeyState) or [google groups](https://groups.google.com/groups?q=GetAsyncKeyState).

#### Return Value

The return value specifies whether the key was pressed since the last call to GetAsyncKeyState, and whether the key is currently up or down. If the most significant bit is set, the key is down, and if the least significant bit is set, the key was pressed after the previous call to GetAsyncKeyState.
The return value is zero if a window in another thread or process currently has the keyboard focus.


---

<!-- page: win32api__GetCommandLine_meth.html -->

## win32api.GetCommandLine

 string = GetCommandLine()

Retrieves the current application's command line.

#### Win32 API References

- Search for GetCommandLine at [msdn](https://learn.microsoft.com/en-ca/search/?terms=GetCommandLine), [google](https://www.google.com/search?q=GetCommandLine) or [google groups](https://groups.google.com/groups?q=GetCommandLine).


---

<!-- page: win32api__GetComputerNameEx_meth.html -->

## win32api.GetComputerNameEx

 string = GetComputerNameEx(NameType)

Retrieves a NetBIOS or DNS name associated with the local computer

#### Parameters

- NameType : int

 Value from COMPUTER_NAME_FORMAT enum, win32con.ComputerName*

#### Win32 API References

- Search for GetComputerNameEx at [msdn](https://learn.microsoft.com/en-ca/search/?terms=GetComputerNameEx), [google](https://www.google.com/search?q=GetComputerNameEx) or [google groups](https://groups.google.com/groups?q=GetComputerNameEx).


---

<!-- page: win32api__GetComputerName_meth.html -->

## win32api.GetComputerName

 string = GetComputerName()

Returns the local computer name

#### Win32 API References

- Search for GetComputerName at [msdn](https://learn.microsoft.com/en-ca/search/?terms=GetComputerName), [google](https://www.google.com/search?q=GetComputerName) or [google groups](https://groups.google.com/groups?q=GetComputerName).


---

<!-- page: win32api__GetComputerObjectName_meth.html -->

## win32api.GetComputerObjectName

 string = GetComputerObjectName(NameFormat)

Retrieves the local computer's name in a specified format.

#### Parameters

- NameFormat : int

 EXTENDED_NAME_FORMAT value, win32con.Name*

#### Win32 API References

- Search for GetComputerObjectName at [msdn](https://learn.microsoft.com/en-ca/search/?terms=GetComputerObjectName), [google](https://www.google.com/search?q=GetComputerObjectName) or [google groups](https://groups.google.com/groups?q=GetComputerObjectName).


---

<!-- page: win32api__GetConsoleTitle_meth.html -->

## win32api.GetConsoleTitle

 string = GetConsoleTitle()

Returns the title for the current console.


---

<!-- page: win32api__GetCurrentProcessId_meth.html -->

## win32api.GetCurrentProcessId

 int = GetCurrentProcessId()

Returns the thread ID for the current process.

#### Win32 API References

- Search for GetCurrentProcessId at [msdn](https://learn.microsoft.com/en-ca/search/?terms=GetCurrentProcessId), [google](https://www.google.com/search?q=GetCurrentProcessId) or [google groups](https://groups.google.com/groups?q=GetCurrentProcessId).


---

<!-- page: win32api__GetCurrentProcess_meth.html -->

## win32api.GetCurrentProcess

 int = GetCurrentProcess()

Returns a pseudohandle for the current process.

#### Comments

 A pseudohandle is a special constant that is interpreted as the current thread handle. The calling thread can use this handle to specify itself whenever a thread handle is required. Pseudohandles are not inherited by child processes. The method win32api::DuplicateHandle can be used to create a handle that other threads and processes can use. As this handle can not be closed, and integer is returned rather than a PyHANDLE object, which would attempt to automatically close the handle.

#### Win32 API References

- Search for GetCurrentProcess at [msdn](https://learn.microsoft.com/en-ca/search/?terms=GetCurrentProcess), [google](https://www.google.com/search?q=GetCurrentProcess) or [google groups](https://groups.google.com/groups?q=GetCurrentProcess).


---

<!-- page: win32api__GetCurrentThreadId_meth.html -->

## win32api.GetCurrentThreadId

 int = GetCurrentThreadId()

Returns the thread ID for the current thread.

#### Win32 API References

- Search for GetCurrentThreadId at [msdn](https://learn.microsoft.com/en-ca/search/?terms=GetCurrentThreadId), [google](https://www.google.com/search?q=GetCurrentThreadId) or [google groups](https://groups.google.com/groups?q=GetCurrentThreadId).


---

<!-- page: win32api__GetCurrentThread_meth.html -->

## win32api.GetCurrentThread

 int = GetCurrentThread()

Returns a pseudohandle for the current thread.

#### Comments

 A pseudohandle is a special constant that is interpreted as the current thread handle. The calling thread can use this handle to specify itself whenever a thread handle is required. Pseudohandles are not inherited by child processes. The method win32api::DuplicateHandle can be used to create a handle that other threads and processes can use. As this handle can not be closed, and integer is returned rather than a PyHANDLE object, which would attempt to automatically close the handle.

#### Win32 API References

- Search for GetCurrentThread at [msdn](https://learn.microsoft.com/en-ca/search/?terms=GetCurrentThread), [google](https://www.google.com/search?q=GetCurrentThread) or [google groups](https://groups.google.com/groups?q=GetCurrentThread).


---

<!-- page: win32api__GetCursorPos_meth.html -->

## win32api.GetCursorPos

 int, int = GetCursorPos()

Returns the position of the cursor, in screen co-ordinates.

#### Win32 API References

- Search for GetCursorPos at [msdn](https://learn.microsoft.com/en-ca/search/?terms=GetCursorPos), [google](https://www.google.com/search?q=GetCursorPos) or [google groups](https://groups.google.com/groups?q=GetCursorPos).


---

<!-- page: win32api__GetDateFormat_meth.html -->

## win32api.GetDateFormat

 string = GetDateFormat(locale, flags , time , format )

Formats a date as a date string for a specified locale. The function formats either a specified date or the local system date.

#### Parameters

- locale : int

- flags : int

- time : PyDateTime

 The time to use, or None to use the current time.

- format : string

 May be None


---

<!-- page: win32api__GetDiskFreeSpaceEx_meth.html -->

## win32api.GetDiskFreeSpaceEx

 tuple = GetDiskFreeSpaceEx(rootPath)

Retrieves information about the specified disk, including the amount of free space available.

#### Parameters

- rootPath : string

 Specifies the root directory of the disk to return information about. If rootPath is None, the method uses the root of the current directory.

#### Win32 API References

- Search for GetDiskFreeSpaceEx at [msdn](https://learn.microsoft.com/en-ca/search/?terms=GetDiskFreeSpaceEx), [google](https://www.google.com/search?q=GetDiskFreeSpaceEx) or [google groups](https://groups.google.com/groups?q=GetDiskFreeSpaceEx).

#### Return Value

The return value is a tuple of 3 integers, containing the number of free bytes available the total number of bytes available on disk the total number of free bytes on disk the above values may be less, if user-quotas are in effect
If the function fails, an error is returned.


---

<!-- page: win32api__GetDiskFreeSpace_meth.html -->

## win32api.GetDiskFreeSpace

 tuple = GetDiskFreeSpace(rootPath)

Retrieves information about the specified disk, including the amount of free space available.

#### Parameters

- rootPath : string

 Specifies the root directory of the disk to return information about. If rootPath is None, the method uses the root of the current directory.

#### Win32 API References

- Search for GetDiskFreeSpace at [msdn](https://learn.microsoft.com/en-ca/search/?terms=GetDiskFreeSpace), [google](https://www.google.com/search?q=GetDiskFreeSpace) or [google groups](https://groups.google.com/groups?q=GetDiskFreeSpace).

#### Return Value

The return value is a tuple of 4 integers, containing the number of sectors per cluster, the number of bytes per sector, the total number of free clusters on the disk and the total number of clusters on the disk.
If the function fails, an error is returned.


---

<!-- page: win32api__GetDllDirectory_meth.html -->

## win32api.GetDllDirectory

 PyUnicode = GetDllDirectory()

Returns the DLL search path

#### Win32 API References

- Search for GetDllDirectory at [msdn](https://learn.microsoft.com/en-ca/search/?terms=GetDllDirectory), [google](https://www.google.com/search?q=GetDllDirectory) or [google groups](https://groups.google.com/groups?q=GetDllDirectory).


---

<!-- page: win32api__GetDomainName_meth.html -->

## win32api.GetDomainName

 string = GetDomainName()

Returns the current domain name

#### Comments

 This is a convenience wrapper of the Win32 function LookupAccountSid()


---

<!-- page: win32api__GetEnvironmentVariableW_meth.html -->

## win32api.GetEnvironmentVariableW

 string = GetEnvironmentVariableW(Name)

Retrieves the unicode value of an environment variable.

#### Parameters

- Name : str

 The variable to retrieve

#### Win32 API References

- Search for GetEnvironmentVariableW at [msdn](https://learn.microsoft.com/en-ca/search/?terms=GetEnvironmentVariableW), [google](https://www.google.com/search?q=GetEnvironmentVariableW) or [google groups](https://groups.google.com/groups?q=GetEnvironmentVariableW).

#### Return Value

Returns None if environment variable is not found


---

<!-- page: win32api__GetEnvironmentVariable_meth.html -->

## win32api.GetEnvironmentVariable

 str = GetEnvironmentVariable(variable)

Retrieves the value of an environment variable.

#### Parameters

- variable : str

 The variable to get

#### Win32 API References

- Search for GetEnvironmentVariable at [msdn](https://learn.microsoft.com/en-ca/search/?terms=GetEnvironmentVariable), [google](https://www.google.com/search?q=GetEnvironmentVariable) or [google groups](https://groups.google.com/groups?q=GetEnvironmentVariable).

#### Return Value

Returns None if environment variable is not found


---

<!-- page: win32api__GetFileAttributes_meth.html -->

## win32api.GetFileAttributes

 int = GetFileAttributes(pathName)

Retrieves the attributes for the named file.

#### Parameters

- pathName : string/bytes

 The name of the file whose attributes are to be returned. This calls the Windows GetFileAttributesW function.

#### Win32 API References

- Search for GetFileAttributes at [msdn](https://learn.microsoft.com/en-ca/search/?terms=GetFileAttributes), [google](https://www.google.com/search?q=GetFileAttributes) or [google groups](https://groups.google.com/groups?q=GetFileAttributes).

- Search for GetFileAttributesW at [msdn](https://learn.microsoft.com/en-ca/search/?terms=GetFileAttributesW), [google](https://www.google.com/search?q=GetFileAttributesW) or [google groups](https://groups.google.com/groups?q=GetFileAttributesW).

#### Return Value

The return value is a combination of the win32con.FILE_ATTRIBUTE_* constants.
An exception is raised on failure.


---

<!-- page: win32api__GetFileVersionInfo_meth.html -->

## win32api.GetFileVersionInfo

 GetFileVersionInfo(Filename, SubBlock)

Retrieve version info for specified file

#### Parameters

- Filename : string/unicode

 File to query for version info

- SubBlock : string/unicode

 Information to return: \\ for VS_FIXEDFILEINFO, \\VarFileInfo\\Translation for languages/codepages available


---

<!-- page: win32api__GetFocus_meth.html -->

## win32api.GetFocus

 int = GetFocus()

Retrieves the handle of the keyboard focus window associated with the thread that called the method.

#### Win32 API References

- Search for GetFocus at [msdn](https://learn.microsoft.com/en-ca/search/?terms=GetFocus), [google](https://www.google.com/search?q=GetFocus) or [google groups](https://groups.google.com/groups?q=GetFocus).

#### Return Value

The method raises an exception if no window with the focus exists.


---

<!-- page: win32api__GetFullPathName_meth.html -->

## win32api.GetFullPathName

 string = GetFullPathName(fileName)

Returns the full path of a (possibly relative) path

#### Parameters

- fileName : string

 The file name.

#### Comments

 Please use win32file::GetFullPathName instead - it has better Unicode semantics.


---

<!-- page: win32api__GetHandleInformation_meth.html -->

## win32api.GetHandleInformation

 int = GetHandleInformation(Object)

Retrieves a handle's flags.

#### Parameters

- Object : PyHANDLE

 Handle to an object

#### Return Value

Returns a combination of HANDLE_FLAG_INHERIT, HANDLE_FLAG_PROTECT_FROM_CLOSE


---

<!-- page: win32api__GetKeyState_meth.html -->

## win32api.GetKeyState

 int = GetKeyState(key)

Retrieves the status of the specified key.

#### Parameters

- key : int

 Specifies a virtual key. If the desired virtual key is a letter or digit (A through Z, a through z, or 0 through 9), key must be set to the ASCII value of that character. For other keys, it must be a virtual-key code.

#### Comments

 The key status returned from this function changes as a given thread reads key messages from its message queue. The status does not reflect the interrupt-level state associated with the hardware. Use the win32api::GetAsyncKeyState method to retrieve that information.

#### Win32 API References

- Search for GetKeyState at [msdn](https://learn.microsoft.com/en-ca/search/?terms=GetKeyState), [google](https://www.google.com/search?q=GetKeyState) or [google groups](https://groups.google.com/groups?q=GetKeyState).

#### Return Value

The return value specifies the status of the given virtual key. If the high-order bit is 1, the key is down; otherwise, it is up. If the low-order bit is 1, the key is toggled. A key, such as the CAPS LOCK key, is toggled if it is turned on. The key is off and untoggled if the low-order bit is 0. A toggle key's indicator light (if any) on the keyboard will be on when the key is toggled, and off when the key is untoggled.


---

<!-- page: win32api__GetKeyboardLayoutList_meth.html -->

## win32api.GetKeyboardLayoutList

 (int,..) = GetKeyboardLayoutList()

Returns a sequence of all locale ids currently loaded


---

<!-- page: win32api__GetKeyboardLayoutName_meth.html -->

## win32api.GetKeyboardLayoutName

 int = GetKeyboardLayoutName()

Retrieves the name of the active input locale identifier (formerly called the keyboard layout).


---

<!-- page: win32api__GetKeyboardLayout_meth.html -->

## win32api.GetKeyboardLayout

 int = GetKeyboardLayout(threadId)

retrieves the active input locale identifier (formerly called the keyboard layout) for the specified thread.

#### Parameters

- threadId=0 : int

#### Comments

 If the idThread parameter is zero, the input locale identifier for the active thread is returned.


---

<!-- page: win32api__GetKeyboardState_meth.html -->

## win32api.GetKeyboardState

 string = GetKeyboardState()

Retrieves the status of the 256 virtual keys on the keyboard.

#### Win32 API References

- Search for GetKeyboardState at [msdn](https://learn.microsoft.com/en-ca/search/?terms=GetKeyboardState), [google](https://www.google.com/search?q=GetKeyboardState) or [google groups](https://groups.google.com/groups?q=GetKeyboardState).

#### Return Value

The return value is a string of exactly 256 characters. Each character represents the bitmask for a key - see the Win32 documentation for more details.


---

<!-- page: win32api__GetLastError_meth.html -->

## win32api.GetLastError

 int = GetLastError()

Retrieves the calling thread's last error code value.

#### Win32 API References

- Search for GetLastError at [msdn](https://learn.microsoft.com/en-ca/search/?terms=GetLastError), [google](https://www.google.com/search?q=GetLastError) or [google groups](https://groups.google.com/groups?q=GetLastError).


---

<!-- page: win32api__GetLastInputInfo_meth.html -->

## win32api.GetLastInputInfo

 int = GetLastInputInfo()

Returns time of last input event in tick count

#### Win32 API References

- Search for GetLastInputInfo at [msdn](https://learn.microsoft.com/en-ca/search/?terms=GetLastInputInfo), [google](https://www.google.com/search?q=GetLastInputInfo) or [google groups](https://groups.google.com/groups?q=GetLastInputInfo).


---

<!-- page: win32api__GetLocalTime_meth.html -->

## win32api.GetLocalTime

 tuple = GetLocalTime()

Returns the current local time


---

<!-- page: win32api__GetLogicalDriveStrings_meth.html -->

## win32api.GetLogicalDriveStrings

 string = GetLogicalDriveStrings()

Returns a string with all logical drives currently mapped.

#### Win32 API References

- Search for GetLogicalDriveStrings at [msdn](https://learn.microsoft.com/en-ca/search/?terms=GetLogicalDriveStrings), [google](https://www.google.com/search?q=GetLogicalDriveStrings) or [google groups](https://groups.google.com/groups?q=GetLogicalDriveStrings).

#### Return Value

The return value is a single string, with each drive letter NULL terminated.
Use "s.split('\\0')" to split into components.


---

<!-- page: win32api__GetLogicalDrives_meth.html -->

## win32api.GetLogicalDrives

 int = GetLogicalDrives()

Returns a bitmask representing the currently available disk drives.

#### Win32 API References

- Search for GetLogicalDrives at [msdn](https://learn.microsoft.com/en-ca/search/?terms=GetLogicalDrives), [google](https://www.google.com/search?q=GetLogicalDrives) or [google groups](https://groups.google.com/groups?q=GetLogicalDrives).


---

<!-- page: win32api__GetLongPathNameW_meth.html -->

## win32api.GetLongPathNameW

 PyUnicode = GetLongPathNameW(fileName)

Converts the specified path to its long form.

#### Parameters

- fileName : PyUnicode

 The file name.

#### Comments

 This function may raise a NotImplementedError exception if the version of Windows does not support this function.


---

<!-- page: win32api__GetModuleFileNameW_meth.html -->

## win32api.GetModuleFileNameW

 PyUnicode = GetModuleFileNameW(hModule)

Retrieves the unicode filename of the specified module.

#### Parameters

- hModule : PyHANDLE

 Specifies the handle to the module.

#### Win32 API References

- Search for GetModuleFileName at [msdn](https://learn.microsoft.com/en-ca/search/?terms=GetModuleFileName), [google](https://www.google.com/search?q=GetModuleFileName) or [google groups](https://groups.google.com/groups?q=GetModuleFileName).


---

<!-- page: win32api__GetModuleHandle_meth.html -->

## win32api.GetModuleHandle

 int = GetModuleHandle(fileName)

Returns the handle of an already loaded DLL.

#### Parameters

- fileName=None : string

 Specifies the file name of the module to load.

#### Win32 API References

- Search for GetModuleHandle at [msdn](https://learn.microsoft.com/en-ca/search/?terms=GetModuleHandle), [google](https://www.google.com/search?q=GetModuleHandle) or [google groups](https://groups.google.com/groups?q=GetModuleHandle).


---

<!-- page: win32api__GetMonitorInfo_meth.html -->

## win32api.GetMonitorInfo

 dict = GetMonitorInfo(hMonitor)

Retrieves information for a monitor by handle

#### Parameters

- hMonitor : PyHANDLE

 Handle to a monitor

#### Comments

 Accepts keyword args

#### Return Value

Returns a dictionary representing a MONITORINFOEX structure


---

<!-- page: win32api__GetNativeSystemInfo_meth.html -->

## win32api.GetNativeSystemInfo

 tuple = GetNativeSystemInfo()

Retrieves information about the current system for a Wow64 process.

#### Win32 API References

- Search for GetNativeSystemInfo at [msdn](https://learn.microsoft.com/en-ca/search/?terms=GetNativeSystemInfo), [google](https://www.google.com/search?q=GetNativeSystemInfo) or [google groups](https://groups.google.com/groups?q=GetNativeSystemInfo).

#### Return Value

The return value is a tuple of 9 values, which corresponds to the Win32 SYSTEM_INFO structure. The element names are:
wProcessorArchitecture
dwPageSize
lpMinimumApplicationAddress
lpMaximumApplicationAddress
 dwActiveProcessorMask
dwNumberOfProcessors
 dwProcessorType
dwAllocationGranularity
(wProcessorLevel,wProcessorRevision)


---

<!-- page: win32api__GetProcAddress_meth.html -->

## win32api.GetProcAddress

 int = GetProcAddress(hModule, functionName )

Returns the address of the specified exported dynamic-link library (DLL) function.

#### Parameters

- hModule : PyHANDLE

 Specifies the handle to the module.

- functionName : PyResourceId

 Specifies the name of the procedure, or its ordinal value

#### Win32 API References

- Search for GetProcAddress at [msdn](https://learn.microsoft.com/en-ca/search/?terms=GetProcAddress), [google](https://www.google.com/search?q=GetProcAddress) or [google groups](https://groups.google.com/groups?q=GetProcAddress).


---

<!-- page: win32api__GetProfileSection_meth.html -->

## win32api.GetProfileSection

 list = GetProfileSection(section, iniName )

Retrieves all entries from a section in an INI file.

#### Parameters

- section : string

 The section in the INI file to retrieve a entries for.

- iniName=None : string

 The name of the INI file. If None, the system INI file is used.

#### Comments

 This function is obsolete, applications should use the registry instead.

#### Win32 API References

- Search for GetProfileSection at [msdn](https://learn.microsoft.com/en-ca/search/?terms=GetProfileSection), [google](https://www.google.com/search?q=GetProfileSection) or [google groups](https://groups.google.com/groups?q=GetProfileSection).

#### Return Value

The return value is a list of strings.


---

<!-- page: win32api__GetProfileVal_meth.html -->

## win32api.GetProfileVal

 int/string = GetProfileVal(section, entry , defValue , iniName )

Retrieves entries from a windows INI file. This method encapsulates GetProfileString, GetProfileInt, GetPrivateProfileString and GetPrivateProfileInt.

#### Parameters

- section : string

 The section in the INI file to retrieve a value for.

- entry : string

 The entry within the section in the INI file to retrieve a value for.

- defValue : int/string

 The default value. The type of this parameter determines the methods return type.

- iniName=None : string

 The name of the INI file. If None, the system INI file is used.

#### Comments

 This function is obsolete, applications should use the registry instead.

#### Win32 API References

- Search for GetProfileString at [msdn](https://learn.microsoft.com/en-ca/search/?terms=GetProfileString), [google](https://www.google.com/search?q=GetProfileString) or [google groups](https://groups.google.com/groups?q=GetProfileString).

- Search for GetProfileInt at [msdn](https://learn.microsoft.com/en-ca/search/?terms=GetProfileInt), [google](https://www.google.com/search?q=GetProfileInt) or [google groups](https://groups.google.com/groups?q=GetProfileInt).

- Search for GetPrivateProfileString at [msdn](https://learn.microsoft.com/en-ca/search/?terms=GetPrivateProfileString), [google](https://www.google.com/search?q=GetPrivateProfileString) or [google groups](https://groups.google.com/groups?q=GetPrivateProfileString).

- Search for GetPrivateProfileInt at [msdn](https://learn.microsoft.com/en-ca/search/?terms=GetPrivateProfileInt), [google](https://www.google.com/search?q=GetPrivateProfileInt) or [google groups](https://groups.google.com/groups?q=GetPrivateProfileInt).

#### Return Value

The return value is the same type as the default parameter.


---

<!-- page: win32api__GetPwrCapabilities_meth.html -->

## win32api.GetPwrCapabilities

 dict = GetPwrCapabilities()

Retrieves system's power capabilities

#### Win32 API References

- Search for GetPwrCapabilities at [msdn](https://learn.microsoft.com/en-ca/search/?terms=GetPwrCapabilities), [google](https://www.google.com/search?q=GetPwrCapabilities) or [google groups](https://groups.google.com/groups?q=GetPwrCapabilities).

#### Return Value

Returns a dict representing a SYSTEM_POWER_CAPABILITIES struct


---

<!-- page: win32api__GetShortPathName_meth.html -->

## win32api.GetShortPathName

 string = GetShortPathName(path)

Obtains the short path form of the specified path.

#### Parameters

- path : string/unicode

 If a unicode object is passed, GetShortPathNameW will be called and a unicode object returned.

#### Comments

 The short path name is an 8.3 compatible file name. As the input path does not need to be absolute, the returned name may be longer than the input path.

#### Win32 API References

- Search for GetShortPathName at [msdn](https://learn.microsoft.com/en-ca/search/?terms=GetShortPathName), [google](https://www.google.com/search?q=GetShortPathName) or [google groups](https://groups.google.com/groups?q=GetShortPathName).


---

<!-- page: win32api__GetStdHandle_meth.html -->

## win32api.GetStdHandle

 GetStdHandle(handle)

Returns a handle for the standard input, standard output, or standard error device

#### Parameters

- handle : int

 input, output, or error device


---

<!-- page: win32api__GetSysColor_meth.html -->

## win32api.GetSysColor

 int = GetSysColor(index)

Returns the current system color for the specified element.

#### Parameters

- index : int

 The Id of the element to return. See the API for full details.

#### Win32 API References

- Search for GetSysColor at [msdn](https://learn.microsoft.com/en-ca/search/?terms=GetSysColor), [google](https://www.google.com/search?q=GetSysColor) or [google groups](https://groups.google.com/groups?q=GetSysColor).

#### Return Value

The return value is a windows RGB color representation.


---

<!-- page: win32api__GetSystemCpuSetInformation_meth.html -->

## win32api.GetSystemCpuSetInformation

 list = GetSystemCpuSetInformation()

Returns CPU Set information for all logical processors.

#### Comments

 This function retrieves CPU topology information including efficiency class (P-core vs E-core), scheduling class, NUMA node, cache topology, and processor state flags.

#### Win32 API References

- Search for GetSystemCpuSetInformation at [msdn](https://learn.microsoft.com/en-ca/search/?terms=GetSystemCpuSetInformation), [google](https://www.google.com/search?q=GetSystemCpuSetInformation) or [google groups](https://groups.google.com/groups?q=GetSystemCpuSetInformation).

#### Return Value

A list of PySYSTEM_CPU_SET_INFORMATION objects, one for each logical processor.


---

<!-- page: win32api__GetSystemDefaultLCID_meth.html -->

## win32api.GetSystemDefaultLCID

 int = GetSystemDefaultLCID()

Retrieves the system default locale identifier.

#### Win32 API References

- Search for GetSystemDefaultLCID at [msdn](https://learn.microsoft.com/en-ca/search/?terms=GetSystemDefaultLCID), [google](https://www.google.com/search?q=GetSystemDefaultLCID) or [google groups](https://groups.google.com/groups?q=GetSystemDefaultLCID).


---

<!-- page: win32api__GetSystemDefaultLangID_meth.html -->

## win32api.GetSystemDefaultLangID

 int = GetSystemDefaultLangID()

Retrieves the system default language identifier.

#### Win32 API References

- Search for GetSystemDefaultLangID at [msdn](https://learn.microsoft.com/en-ca/search/?terms=GetSystemDefaultLangID), [google](https://www.google.com/search?q=GetSystemDefaultLangID) or [google groups](https://groups.google.com/groups?q=GetSystemDefaultLangID).


---

<!-- page: win32api__GetSystemDirectory_meth.html -->

## win32api.GetSystemDirectory

 string = GetSystemDirectory()

Returns the path of the Windows system directory.

#### Win32 API References

- Search for GetSystemDirectory at [msdn](https://learn.microsoft.com/en-ca/search/?terms=GetSystemDirectory), [google](https://www.google.com/search?q=GetSystemDirectory) or [google groups](https://groups.google.com/groups?q=GetSystemDirectory).


---

<!-- page: win32api__GetSystemFileCacheSize_meth.html -->

## win32api.GetSystemFileCacheSize

 tuple = GetSystemFileCacheSize()

Returns the amount of memory reserved for file cache

#### Return Value

Returns a tuple containing the minimum and maximum cache sizes, and flags (combination of win32con.MM_WORKING_SET_* flags)


---

<!-- page: win32api__GetSystemInfo_meth.html -->

## win32api.GetSystemInfo

 tuple = GetSystemInfo()

Retrieves information about the current system.

#### Win32 API References

- Search for GetSystemInfo at [msdn](https://learn.microsoft.com/en-ca/search/?terms=GetSystemInfo), [google](https://www.google.com/search?q=GetSystemInfo) or [google groups](https://groups.google.com/groups?q=GetSystemInfo).

#### Return Value

The return value is a tuple of 9 values, which corresponds to the Win32 SYSTEM_INFO structure. The element names are:
wProcessorArchitecture
dwPageSize
lpMinimumApplicationAddress
lpMaximumApplicationAddress
 dwActiveProcessorMask
dwNumberOfProcessors
 dwProcessorType
dwAllocationGranularity
(wProcessorLevel,wProcessorRevision)


---

<!-- page: win32api__GetSystemMetrics_meth.html -->

## win32api.GetSystemMetrics

 int = GetSystemMetrics(index)

Retrieves various system metrics and system configuration settings.

#### Parameters

- index : int

 Which metric is being requested. See the API documentation for a full list.

#### Win32 API References

- Search for GetSystemMetrics at [msdn](https://learn.microsoft.com/en-ca/search/?terms=GetSystemMetrics), [google](https://www.google.com/search?q=GetSystemMetrics) or [google groups](https://groups.google.com/groups?q=GetSystemMetrics).


---

<!-- page: win32api__GetSystemPowerStatus_meth.html -->

## win32api.GetSystemPowerStatus

 dict = GetSystemPowerStatus()

Retrieves the power status of the system

#### Win32 API References

- Search for GetSystemPowerStatus at [msdn](https://learn.microsoft.com/en-ca/search/?terms=GetSystemPowerStatus), [google](https://www.google.com/search?q=GetSystemPowerStatus) or [google groups](https://groups.google.com/groups?q=GetSystemPowerStatus).

#### Return Value

Returns a dict representing a SYSTEM_POWER_STATUS struct


---

<!-- page: win32api__GetSystemTime_meth.html -->

## win32api.GetSystemTime

 tuple = GetSystemTime()

Returns the current system time


---

<!-- page: win32api__GetTempFileName_meth.html -->

## win32api.GetTempFileName

 tuple = GetTempFileName(path, prefix , nUnique )

Returns creates a temporary filename of the following form: path\\preuuuu.tmp.

#### Parameters

- path : string

 Specifies the path where the method creates the temporary filename. Applications typically specify a period (.) or the result of the GetTempPath function for this parameter.

- prefix : string

 Specifies the temporary filename prefix.

- nUnique : int

 Specifies an nteger used in creating the temporary filename. If this parameter is nonzero, it is appended to the temporary filename. If this parameter is zero, Windows uses the current system time to create a number to append to the filename.

#### Win32 API References

- Search for GetTempFileName at [msdn](https://learn.microsoft.com/en-ca/search/?terms=GetTempFileName), [google](https://www.google.com/search?q=GetTempFileName) or [google groups](https://groups.google.com/groups?q=GetTempFileName).

#### Return Value

The return value is a tuple of (string, int), where string is the filename, and rc is the unique number used to generate the filename.


---

<!-- page: win32api__GetTempPath_meth.html -->

## win32api.GetTempPath

 string = GetTempPath()

Retrieves the path of the directory designated for temporary files.


---

<!-- page: win32api__GetThreadLocale_meth.html -->

## win32api.GetThreadLocale

 int = GetThreadLocale()

Returns the current thread's locale.


---

<!-- page: win32api__GetTickCount_meth.html -->

## win32api.GetTickCount

 int = GetTickCount()

Returns the (64bit) number of milliseconds since windows started. Uses Win API GetTickCount64().


---

<!-- page: win32api__GetTimeFormat_meth.html -->

## win32api.GetTimeFormat

 string = GetTimeFormat(locale, flags , time , format )

Formats a time as a time string for a specified locale. The function formats either a specified time or the local system time.

#### Parameters

- locale : int

- flags : int

- time : PyDateTime

 The time to use, or None to use the current time.

- format : string

 May be None


---

<!-- page: win32api__GetTimeZoneInformation_meth.html -->

## win32api.GetTimeZoneInformation

 tuple = GetTimeZoneInformation(times_as_tuples)

Retrieves the system time-zone information.

#### Parameters

- times_as_tuples=? : bool

 If true, the SYSTEMTIME elements are returned as tuples instead of a time object. Defaults to True, because this function returns SYSTEMTIME information with members which datetime treats as invalid. In other words, using False will result in ValueErrors instead of returning.

#### Return Value

The return value is a tuple of (rc, tzinfo), where rc is the integer return code from ::GetTimezoneInformation(), which may be

| | value | description
| |

---

 |

---

| | TIME_ZONE_ID_STANDARD | if in standard time
| | TIME_ZONE_ID_DAYLIGHT | if in daylight savings time
| | TIME_ZONE_ID_UNKNOWN | if the timezone in question doesn't use daylight savings time, (eg. indiana time). tzinfo is a tuple of:

#### Items

- [0] int : bias

 Specifies the current bias, in minutes, for local time translation on this computer. The bias is the difference, in minutes, between Coordinated Universal Time (UTC) and local time. All translations between UTC and local time are based on the following formula:

UTC = local time + bias

- [1] unicode : standardName

 Specifies a string associated with standard time on this operating system. For example, this member could contain "EST" to indicate Eastern Standard Time. This string is not used by the operating system, so anything stored there using the SetTimeZoneInformation function is returned unchanged by the GetTimeZoneInformation function. This string can be empty.

- [2] PyDateTime/tuple : standardTime

 Specifies a SYSTEMTIME object that contains a date and local time when the transition from daylight saving time to standard time occurs on this operating system. If this date is not specified, the wMonth member in the SYSTEMTIME structure must be zero. If this date is specified, the DaylightDate value in the TIME_ZONE_INFORMATION structure must also be specified.
To select the correct day in the month, set the wYear member to zero, the wDayOfWeek member to an appropriate weekday, and the wDay member to a value in the range 1 through 5. Using this notation, the first Sunday in April can be specified, as can the last Thursday in October (5 is equal to "the last").

- [3] int : standardBias

 Specifies a bias value to be used during local time translations that occur during standard time. This member is ignored if a value for the StandardDate member is not supplied.
This value is added to the value of the Bias member to form the bias used during standard time. In most time zones, the value of this member is zero.

- [4] unicode : daylightName

- [5] PyDateTime/tuple : daylightTime

- [6] int : daylightBias

 Specifies a bias value to be used during local time translations that occur during daylight saving time. This member is ignored if a value for the DaylightDate member is not supplied.
This value is added to the value of the Bias member to form the bias used during daylight saving time. In most time zones, the value of this member is 60.


---

<!-- page: win32api__GetUserDefaultLCID_meth.html -->

## win32api.GetUserDefaultLCID

 int = GetUserDefaultLCID()

Retrieves the user default locale identifier.

#### Win32 API References

- Search for GetUserDefaultLCID at [msdn](https://learn.microsoft.com/en-ca/search/?terms=GetUserDefaultLCID), [google](https://www.google.com/search?q=GetUserDefaultLCID) or [google groups](https://groups.google.com/groups?q=GetUserDefaultLCID).


---

<!-- page: win32api__GetUserDefaultLangID_meth.html -->

## win32api.GetUserDefaultLangID

 int = GetUserDefaultLangID()

Retrieves the user default language identifier.

#### Win32 API References

- Search for GetUserDefaultLangID at [msdn](https://learn.microsoft.com/en-ca/search/?terms=GetUserDefaultLangID), [google](https://www.google.com/search?q=GetUserDefaultLangID) or [google groups](https://groups.google.com/groups?q=GetUserDefaultLangID).


---

<!-- page: win32api__GetUserNameEx_meth.html -->

## win32api.GetUserNameEx

 string = GetUserNameEx(NameFormat)

Returns the current user name in format from EXTENDED_NAME_FORMAT enum

#### Parameters

- NameFormat : int

 EXTENDED_NAME_FORMAT value, win32con.Name*

#### Win32 API References

- Search for GetUserNameEx at [msdn](https://learn.microsoft.com/en-ca/search/?terms=GetUserNameEx), [google](https://www.google.com/search?q=GetUserNameEx) or [google groups](https://groups.google.com/groups?q=GetUserNameEx).


---

<!-- page: win32api__GetUserName_meth.html -->

## win32api.GetUserName

 string = GetUserName()

Returns the current user name

#### Win32 API References

- Search for GetUserName at [msdn](https://learn.microsoft.com/en-ca/search/?terms=GetUserName), [google](https://www.google.com/search?q=GetUserName) or [google groups](https://groups.google.com/groups?q=GetUserName).


---

<!-- page: win32api__GetVersionEx_meth.html -->

## win32api.GetVersionEx

 tuple = GetVersionEx(format)

Returns the current version of Windows, and information about the environment.

#### Parameters

- format=0 : int

 The format of the version info to return. May be 0 (for OSVERSIONINFO) or 1 (for OSVERSIONINFOEX)

#### Return Value

The return value is a tuple with the following information.

#### Items

- [0] int : majorVersion

 Identifies the major version number of the operating system.

- [1] int : minorVersion

 Identifies the minor version number of the operating system.

- [2] int : buildNumber

 Identifies the build number of the operating system in the low-order word. (The high-order word contains the major and minor version numbers.)

- [3] int : platformId

 Identifies the platform supported by the operating system. May be one of VER_PLATFORM_WIN32s, VER_PLATFORM_WIN32_WINDOWS or VER_PLATFORM_WIN32_NT

- [4] string : version

 Contains arbitrary additional information about the operating system.

#### Return Value

or if the format param is 1, the return value is a tuple with:

#### Items

- [0] int : majorVersion

 Identifies the major version number of the operating system.

- [1] int : minorVersion

 Identifies the minor version number of the operating system.

- [2] int : buildNumber

 Identifies the build number of the operating system in the low-order word. (The high-order word contains the major and minor version numbers.)

- [3] int : platformId

 Identifies the platform supported by the operating system. May be one of VER_PLATFORM_WIN32s, VER_PLATFORM_WIN32_WINDOWS or VER_PLATFORM_WIN32_NT

- [4] string : version

 Contains arbitrary additional information about the operating system.

- [5] int : wServicePackMajor

 Major version number of the latest Service Pack installed on the system. For example, for Service Pack 3, the major version number is 3. If no Service Pack has been installed, the value is zero.

- [6] int : wServicePackMinor

 Minor version number of the latest Service Pack installed on the system. For example, for Service Pack 3, the minor version number is 0.

- [7] int : wSuiteMask

 Bit flags that identify the product suites available on the system. This member can be a combination of the VER_SUITE_* values.

- [8] int : wProductType

 Additional information about the system. This member can be one of the VER_NT_* values.

- [9] int : wReserved


---

<!-- page: win32api__GetVersion_meth.html -->

## win32api.GetVersion

 int = GetVersion()

Returns the current version of Windows, and information about the environment.

#### Return Value

The return value's low word is the major/minor version of Windows. The high word is 0 if the platform is Windows NT, or 1 if Win32s on Windows 3.1


---

<!-- page: win32api__GetVolumeInformation_meth.html -->

## win32api.GetVolumeInformation

 tuple = GetVolumeInformation(path)

Returns information about a file system and colume whose root directory is specified.

#### Parameters

- path : string

 The root path of the volume on which information is being requested.

#### Return Value

The return is a tuple of:
string - Volume Name
long - Volume serial number.
long - Maximum Component Length of a file name.
long - Sys Flags - other flags specific to the file system. See the api for details.
string - File System Name


---

<!-- page: win32api__GetWindowLong_meth.html -->

## win32api.GetWindowLong

 int = GetWindowLong(hwnd, offset )

Retrieves a long value at the specified offset into the extra window memory of the given window.

#### Parameters

- hwnd : PyHANDLE

 The handle to the window.

- offset : int

 Specifies the zero-based byte offset of the value to change. Valid values are in the range zero through the number of bytes of extra window memory, minus four (for example, if 12 or more bytes of extra memory were specified, a value of 8 would be an index to the third long integer), or one of the GWL_ constants.

#### Comments

 This function calls the GetWindowLongPtr Api function


---

<!-- page: win32api__GetWindowsDirectory_meth.html -->

## win32api.GetWindowsDirectory

 string = GetWindowsDirectory()

Returns the path of the Windows directory.


---

<!-- page: win32api__GlobalMemoryStatusEx_meth.html -->

## win32api.GlobalMemoryStatusEx

 dict = GlobalMemoryStatusEx()

Returns physical and virtual memory usage

#### Return Value

Returns a dictionary representing a MEMORYSTATUSEX structure


---

<!-- page: win32api__GlobalMemoryStatus_meth.html -->

## win32api.GlobalMemoryStatus

 dict = GlobalMemoryStatus()

Returns systemwide memory usage

#### Return Value

Returns a dictionary representing a MEMORYSTATUS structure


---

<!-- page: win32api__HIBYTE_meth.html -->

## win32api.HIBYTE

 int = HIBYTE(val)

An interface to the win32api HIBYTE macro.

#### Parameters

- val : int

 The value to retrieve the HIBYTE from.

#### Comments

 This is simply a wrapper to a C++ macro.


---

<!-- page: win32api__HIWORD_meth.html -->

## win32api.HIWORD

 int = HIWORD(val)

An interface to the win32api HIWORD macro.

#### Parameters

- val : int

 The value to retrieve the HIWORD from.

#### Comments

 This is simply a wrapper to a C++ macro.


---

<!-- page: win32api__InitiateSystemShutdown_meth.html -->

## win32api.InitiateSystemShutdown

 InitiateSystemShutdown(computerName, message, timeOut, bForceClose, bRebootAfterShutdown)

Initiates a shutdown and optional restart of the specified computer.

#### Parameters

- computerName : string/PyUnicode

 Specifies the name of the computer to shut-down, or None

- message : string/PyUnicode

 Message to display in a dialog box

- timeOut : int

 Specifies the time (in seconds) that the dialog box should be displayed. While this dialog box is displayed, the shutdown can be stopped by the AbortSystemShutdown function. If dwTimeout is zero, the computer shuts down without displaying the dialog box, and the shutdown cannot be stopped by AbortSystemShutdown.

- bForceClose : int

 Specifies whether applications with unsaved changes are to be forcibly closed. If this parameter is TRUE, such applications are closed. If this parameter is FALSE, a dialog box is displayed prompting the user to close the applications.

- bRebootAfterShutdown : int

 Specifies whether the computer is to restart immediately after shutting down. If this parameter is TRUE, the computer is to restart. If this parameter is FALSE, the system flushes all caches to disk, clears the screen, and displays a message indicating that it is safe to power down.

#### Win32 API References

- Search for InitiateSystemShutdown at [msdn](https://learn.microsoft.com/en-ca/search/?terms=InitiateSystemShutdown), [google](https://www.google.com/search?q=InitiateSystemShutdown) or [google groups](https://groups.google.com/groups?q=InitiateSystemShutdown).


---

<!-- page: win32api__LOBYTE_meth.html -->

## win32api.LOBYTE

 int = LOBYTE(val)

An interface to the win32api LOBYTE macro.

#### Parameters

- val : int

 The value to retrieve the LOBYTE from.

#### Comments

 This is simply a wrapper to a C++ macro.


---

<!-- page: win32api__LOWORD_meth.html -->

## win32api.LOWORD

 int = LOWORD(val)

An interface to the win32api LOWORD macro.

#### Parameters

- val : int

 The value to retrieve the LOWORD from.

#### Comments

 This is simply a wrapper to a C++ macro.


---

<!-- page: win32api__LoadCursor_meth.html -->

## win32api.LoadCursor

 PyHANDLE = LoadCursor(hInstance, cursorid )

Loads a cursor.

#### Parameters

- hInstance : PyHANDLE

 Handle to the instance to load the resource from, or None to load a standard system cursor

- cursorid : PyResourceId

 The ID of the cursor. Can be a resource id or for system cursors, one of win32con.IDC_*

#### Win32 API References

- Search for LoadCursor at [msdn](https://learn.microsoft.com/en-ca/search/?terms=LoadCursor), [google](https://www.google.com/search?q=LoadCursor) or [google groups](https://groups.google.com/groups?q=LoadCursor).


---

<!-- page: win32api__LoadKeyboardLayout_meth.html -->

## win32api.LoadKeyboardLayout

 int = LoadKeyboardLayout(KLID, Flags )

Loads a new locale id

#### Parameters

- KLID : string

 Hex string containing a locale id, eg "00000409"

- Flags=0 : int

 Combination of win32con.KLF_* constants

#### Return Value

Returns the numeric locale id that was loaded


---

<!-- page: win32api__LoadLibraryEx_meth.html -->

## win32api.LoadLibraryEx

 PyHANDLE = LoadLibraryEx(fileName, handle , handle )

Loads the specified DLL, and returns the handle.

#### Parameters

- fileName : string

 Specifies the file name of the module to load.

- handle : PyHANDLE

 Reserved - must be zero

- handle : flags

 Specifies the action to take when loading the module.

#### Win32 API References

- Search for LoadLibraryEx at [msdn](https://learn.microsoft.com/en-ca/search/?terms=LoadLibraryEx), [google](https://www.google.com/search?q=LoadLibraryEx) or [google groups](https://groups.google.com/groups?q=LoadLibraryEx).


---

<!-- page: win32api__LoadLibrary_meth.html -->

## win32api.LoadLibrary

 int = LoadLibrary(fileName)

Loads the specified DLL, and returns the handle.

#### Parameters

- fileName : string

 Specifies the file name of the module to load.

#### Win32 API References

- Search for LoadLibrary at [msdn](https://learn.microsoft.com/en-ca/search/?terms=LoadLibrary), [google](https://www.google.com/search?q=LoadLibrary) or [google groups](https://groups.google.com/groups?q=LoadLibrary).


---

<!-- page: win32api__LoadResource_meth.html -->

## win32api.LoadResource

 string = LoadResource(handle, type , name , language )

Finds and loads a resource from a PE file.

#### Parameters

- handle : PyHANDLE

 The handle of the module containing the resource. Use None for currrent process executable.

- type : PyResourceId

 The type of resource to load.

- name : PyResourceId

 The name or Id of the resource to load.

- language=NEUTRAL : int

 Language to use, defaults to LANG_NEUTRAL.


---

<!-- page: win32api__LoadString_meth.html -->

## win32api.LoadString

 PyUnicode = LoadString(handle, stringId , numChars )

Loads a string from a resource file.

#### Parameters

- handle : PyHANDLE

 The handle of the module containing the resource.

- stringId : int

 The ID of the string to load.

- numChars=1024 : int

 Number of characters to allocate for the return buffer.


---

<!-- page: win32api__MAKELANGID_meth.html -->

## win32api.MAKELANGID

 int = MAKELANGID(PrimaryLanguage, SubLanguage )

Creates a language identifier from a primary language identifier and a sublanguage identifier.

#### Parameters

- PrimaryLanguage : int

 Primary language identifier

- SubLanguage : int

 The sublanguage identifier

#### Comments

 This is simply a wrapper to a C++ macro.


---

<!-- page: win32api__MAKELONG_meth.html -->

## win32api.MAKELONG

 int = MAKELONG(low, high )

creates a LONG value by concatenating the specified values.

#### Parameters

- low : int

 Specifies the low-order byte of the new value.

- high : int

 Specifies the high-order byte of the new value.

#### Comments

 This is simply a wrapper to a C++ macro.


---

<!-- page: win32api__MAKEWORD_meth.html -->

## win32api.MAKEWORD

 int = MAKEWORD(low, high )

creates a WORD value by concatenating the specified values.

#### Parameters

- low : int

 Specifies the low-order byte of the new value.

- high : int

 Specifies the high-order byte of the new value.

#### Comments

 This is simply a wrapper to a C++ macro.


---

<!-- page: win32api__MapVirtualKey_meth.html -->

## win32api.MapVirtualKey

 int = MapVirtualKey(vk, type , hlayout )

Translates (maps) a virtual-key code into a scan code or character value, or translates a scan code into a virtual-key code.

#### Parameters

- vk : int

 The virtual key code.

- type : int

 The type of conversion to make - see the API

- hlayout=None : handle

 The keyboard layout to use. If not specified, the API function MapVirtualKey will be called. If it is specified MapVirtualKeyEx will be called.

#### Comments

 implemented by calling the unicode versions of the API (MapVirtualKeyW/MapVirtualKeyExW)


---

<!-- page: win32api__MessageBeep_meth.html -->

## win32api.MessageBeep

 int = MessageBeep(type)

Plays a predefined waveform sound.

#### Parameters

- type=win32con.MB_OK : int

 Specifies the sound type, as identified by an entry in the [sounds] section of the registry. This parameter can be one of MB_ICONASTERISK, MB_ICONEXCLAMATION, MB_ICONHAND, MB_ICONQUESTION or MB_OK.

#### Comments

 The waveform sound for each sound type is identified by an entry in the [sounds] section of the registry.


---

<!-- page: win32api__MessageBox_meth.html -->

## win32api.MessageBox

 int = MessageBox(hwnd, message , title , style , language )

Display a message box.

#### Parameters

- hwnd : PyHANDLE

 The handle of the parent window. See the comments section.

- message : string

 The message to be displayed in the message box.

- title : string/None

 The title for the message box. If None, the applications title will be used.

- style=win32con.MB_OK : int

 The style of the message box.

- language=win32api.MAKELANGID(LANG_NEUTRAL,SUBLANG_DEFAULT) : int

 The language ID to use.

#### Comments

 Normally, a program in a GUI environment will use one of the MessageBox methods supplied by the GUI (eg, win32ui::MessageBox or PyCWnd::MessageBox)

#### Return Value

An integer identifying the button pressed to dismiss the dialog.


---

<!-- page: win32api__MonitorFromPoint_meth.html -->

## win32api.MonitorFromPoint

 PyHANDLE = MonitorFromPoint(pt, Flags )

Finds monitor that contains a point

#### Parameters

- pt : (int, int)

 Tuple of 2 ints (x,y) specifying screen coordinates

- Flags=0 : int

 Flags that determine default behaviour, one of MONITOR_DEFAULTTONEAREST,MONITOR_DEFAULTTONULL,MONITOR_DEFAULTTOPRIMARY

#### Comments

 Accepts keyword arguments

#### Return Value

Returns None if no monitor was found


---

<!-- page: win32api__MonitorFromRect_meth.html -->

## win32api.MonitorFromRect

 PyHANDLE = MonitorFromRect(rc, Flags )

Finds monitor that has largest intersection with a rectangle

#### Parameters

- rc : PyRECT

 Rectangle to be examined

- Flags=0 : int

 Flags that determine default behaviour, one of MONITOR_DEFAULTTONEAREST,MONITOR_DEFAULTTONULL,MONITOR_DEFAULTTOPRIMARY

#### Comments

 Accepts keyword arguments

#### Return Value

Returns None if no monitor was found


---

<!-- page: win32api__MonitorFromWindow_meth.html -->

## win32api.MonitorFromWindow

 PyHANDLE = MonitorFromWindow(hwnd, Flags )

Finds monitor that contains a window

#### Parameters

- hwnd : PyHANDLE

 Handle to a window

- Flags=0 : int

 Flags that determine default behaviour, one of MONITOR_DEFAULTTONEAREST,MONITOR_DEFAULTTONULL,MONITOR_DEFAULTTOPRIMARY

#### Comments

 Accepts keyword arguments

#### Return Value

Returns None if no monitor was found


---

<!-- page: win32api__MoveFileEx_meth.html -->

## win32api.MoveFileEx

 MoveFileEx(srcName, destName, flag)

Renames a file.

#### Parameters

- srcName : string

 The name of the source file.

- destName : string

 The name of the destination file. May be None.

- flag : int

 Flags indicating how the move is to be performed. See the API for full details.

#### Comments

 This method can move files across volumes.
 If destName is None, and flags contains win32con.MOVEFILE_DELAY_UNTIL_REBOOT, the file will be deleted next reboot.

#### Win32 API References

- Search for MoveFileEx at [msdn](https://learn.microsoft.com/en-ca/search/?terms=MoveFileEx), [google](https://www.google.com/search?q=MoveFileEx) or [google groups](https://groups.google.com/groups?q=MoveFileEx).


---

<!-- page: win32api__MoveFile_meth.html -->

## win32api.MoveFile

 MoveFile(srcName, destName)

Renames a file, or a directory (including its children).

#### Parameters

- srcName : string

 The name of the source file.

- destName : string

 The name of the destination file.

#### Comments

 This method can not move files across volumes.

#### Win32 API References

- Search for MoveFile. at [msdn](https://learn.microsoft.com/en-ca/search/?terms=MoveFile.), [google](https://www.google.com/search?q=MoveFile.) or [google groups](https://groups.google.com/groups?q=MoveFile.).


---

<!-- page: win32api__OpenProcess_meth.html -->

## win32api.OpenProcess

 PyHANDLE = OpenProcess(reqdAccess, bInherit , pid )

Retrieves a handle to an existing process

#### Parameters

- reqdAccess : int

 The required access.

- bInherit : int

 Specifies whether the returned handle can be inherited by a new process created by the current process. If TRUE, the handle is inheritable.

- pid : int

 The process ID


---

<!-- page: win32api__OpenThread_meth.html -->

## win32api.OpenThread

 PyHANDLE = OpenThread(reqdAccess, bInherit , pid )

Retrieves a handle to an existing thread

#### Parameters

- reqdAccess : int

 The required access.

- bInherit : int

 Specifies whether the returned handle can be inherited by a new process created by the current process. If TRUE, the handle is inheritable.

- pid : int

 The thread ID


---

<!-- page: win32api__OutputDebugString_meth.html -->

## win32api.OutputDebugString

 OutputDebugString(msg)

Sends a string to the Windows debugging device.

#### Parameters

- msg : string

 The string to write.


---

<!-- page: win32api__PostMessage_meth.html -->

## win32api.PostMessage

 PostMessage(hwnd, idMessage, wParam, lParam)

Post a message to a window.

#### Parameters

- hwnd : PyHANDLE

 The hWnd of the window to receive the message.

- idMessage : int

 The ID of the message to post.

- wParam=None : int

 The wParam for the message

- lParam=None : int

 The lParam for the message

#### Win32 API References

- Search for PostMessage at [msdn](https://learn.microsoft.com/en-ca/search/?terms=PostMessage), [google](https://www.google.com/search?q=PostMessage) or [google groups](https://groups.google.com/groups?q=PostMessage).


---

<!-- page: win32api__PostQuitMessage_meth.html -->

## win32api.PostQuitMessage

 PostQuitMessage(exitCode)

Post a quit message to an app.

#### Parameters

- exitCode=0 : int

 The exit code

#### Win32 API References

- Search for PostQuitMessage at [msdn](https://learn.microsoft.com/en-ca/search/?terms=PostQuitMessage), [google](https://www.google.com/search?q=PostQuitMessage) or [google groups](https://groups.google.com/groups?q=PostQuitMessage).


---

<!-- page: win32api__PostThreadMessage_meth.html -->

## win32api.PostThreadMessage

 PostThreadMessage(tid, idMessage, wParam, lParam)

Post a message to the specified thread.

#### Parameters

- tid : int

 Identifier of the thread to which the message will be posted.

- idMessage : int

 The ID of the message to post.

- wParam=None : int/str

 The wParam for the message

- lParam=None : int/str

 The lParam for the message

#### Win32 API References

- Search for PostThreadMessage at [msdn](https://learn.microsoft.com/en-ca/search/?terms=PostThreadMessage), [google](https://www.google.com/search?q=PostThreadMessage) or [google groups](https://groups.google.com/groups?q=PostThreadMessage).


---

<!-- page: win32api__RGB_meth.html -->

## win32api.RGB

 int = RGB(red, green , blue )

An interface to the win32api RGB macro.

#### Parameters

- red : int

 The red value

- green : int

 The green value

- blue : int

 The blue value

#### Comments

 This is simply a wrapper to a C++ macro.


---

<!-- page: win32api__RegCloseKey_meth.html -->

## win32api.RegCloseKey

 RegCloseKey(key)

Closes a previously opened registry key.

#### Parameters

- key : PyHKEY/int

 The key to be closed.

#### Win32 API References

- Search for RegCloseKey at [msdn](https://learn.microsoft.com/en-ca/search/?terms=RegCloseKey), [google](https://www.google.com/search?q=RegCloseKey) or [google groups](https://groups.google.com/groups?q=RegCloseKey).


---

<!-- page: win32api__RegConnectRegistry_meth.html -->

## win32api.RegConnectRegistry

 int = RegConnectRegistry(computerName, key )

Establishes a connection to a predefined registry handle on another computer.

#### Parameters

- computerName : string

 The name of the remote computer, of the form \\\\computername. If None, the local computer is used.

- key : int

 The predefined handle. May be win32con.HKEY_LOCAL_MACHINE or win32con.HKEY_USERS.

#### Win32 API References

- Search for RegConnectRegistry at [msdn](https://learn.microsoft.com/en-ca/search/?terms=RegConnectRegistry), [google](https://www.google.com/search?q=RegConnectRegistry) or [google groups](https://groups.google.com/groups?q=RegConnectRegistry).

#### Return Value

The return value is the handle of the opened key. If the function fails, an exception is raised.


---

<!-- page: win32api__RegCopyTree_meth.html -->

## win32api.RegCopyTree

 RegCopyTree(KeySrc, SubKey, KeyDest)

Copies an entire registry key to another location

#### Parameters

- KeySrc : PyHKEY

 Registry key to be copied

- SubKey : PyUnicode

 Subkey to be copied, can be None

- KeyDest : PyHKEY

 The destination key

#### Comments

 Accepts keyword args.


---

<!-- page: win32api__RegCreateKeyEx_meth.html -->

## win32api.RegCreateKeyEx

 PyHKEY, int = RegCreateKeyEx(Key, SubKey , samDesired , Class , Options , SecurityAttributes , Transaction )

Extended version of RegCreateKey

#### Parameters

- Key : PyHKEY/int

 Registry key or one of win32con.HKEY_* values

- SubKey : PyUnicode

 Name of subkey to open or create.

- samDesired : int

 Access allowed to handle, combination of win32con.KEY_* constants. Can also contain standard access rights such as DELETE, WRITE_OWNER, etc.

- Class=None : PyUnicode

 Name of registry key class

- Options=REG_OPTION_NON_VOLATILE : int

 One of the winnt.REG_OPTION_* values

- SecurityAttributes=None : PySECURITY_ATTRIBUTES

 Specifies security for key and handle inheritance

- Transaction=None : PyHANDLE

 Handle to a transaction as returned by win32transaction::CreateTransaction

#### Comments

 Implemented only as Unicode (RegCreateKeyExW). Accepts keyword arguments.

 If a transaction handle is passed in, RegCreateKeyTransacted will be called

#### Win32 API References

- Search for RegCreateKeyEx at [msdn](https://learn.microsoft.com/en-ca/search/?terms=RegCreateKeyEx), [google](https://www.google.com/search?q=RegCreateKeyEx) or [google groups](https://groups.google.com/groups?q=RegCreateKeyEx).

- Search for RegCreateKeyTransacted at [msdn](https://learn.microsoft.com/en-ca/search/?terms=RegCreateKeyTransacted), [google](https://www.google.com/search?q=RegCreateKeyTransacted) or [google groups](https://groups.google.com/groups?q=RegCreateKeyTransacted).

#### Return Value

Returns registry handle and flag indicating if key was opened or created (REG_CREATED_NEW_KEY or REG_OPENED_EXISTING_KEY)


---

<!-- page: win32api__RegCreateKey_meth.html -->

## win32api.RegCreateKey

 PyHKEY = RegCreateKey(key, subKey )

Creates the specified key, or opens the key if it already exists.

#### Parameters

- key : PyHKEY/int

 An already open key, or any one of the following win32con constants:
HKEY_CLASSES_ROOT
HKEY_CURRENT_USER
HKEY_LOCAL_MACHINE
HKEY_USERS

- subKey : string

 The name of a key that this method opens or creates. This key must be a subkey of the key identified by the key parameter. If key is one of the predefined keys, subKey may be None. In that case, the handle returned is the same hkey handle passed in to the function.

#### Win32 API References

- Search for RegCreateKey at [msdn](https://learn.microsoft.com/en-ca/search/?terms=RegCreateKey), [google](https://www.google.com/search?q=RegCreateKey) or [google groups](https://groups.google.com/groups?q=RegCreateKey).

#### Return Value

The return value is the handle of the opened key. If the function fails, an exception is raised.


---

<!-- page: win32api__RegDeleteKeyEx_meth.html -->

## win32api.RegDeleteKeyEx

 RegDeleteKeyEx(Key, SubKey, samDesired, Transaction)

Deletes a registry key from 32 or 64 bit registry view

#### Parameters

- Key : PyHKEY/int

 Registry key or one of win32con.HKEY_* values

- SubKey : PyUnicode

 Name of subkey to be deleted.

- samDesired=0 : int

 Can be KEY_WOW64_32KEY or KEY_WOW64_64KEY to specify alternate registry view

- Transaction=None : PyHANDLE

 Handle to a transaction as returned by win32transaction::CreateTransaction

#### Comments

 Accepts keyword args.

 Key to be deleted cannot contain subkeys

 If a transaction handle is specified, RegDeleteKeyTransacted is called

#### Win32 API References

- Search for RegDeleteKeyEx at [msdn](https://learn.microsoft.com/en-ca/search/?terms=RegDeleteKeyEx), [google](https://www.google.com/search?q=RegDeleteKeyEx) or [google groups](https://groups.google.com/groups?q=RegDeleteKeyEx).

- Search for RegDeleteKeyTransacted at [msdn](https://learn.microsoft.com/en-ca/search/?terms=RegDeleteKeyTransacted), [google](https://www.google.com/search?q=RegDeleteKeyTransacted) or [google groups](https://groups.google.com/groups?q=RegDeleteKeyTransacted).


---

<!-- page: win32api__RegDeleteKey_meth.html -->

## win32api.RegDeleteKey

 RegDeleteKey(key, subKey)

Deletes the specified key. This method can not delete keys with subkeys.

#### Parameters

- key : PyHKEY/int

 An already open key, or any one of the following win32con constants:
HKEY_CLASSES_ROOT
HKEY_CURRENT_USER
HKEY_LOCAL_MACHINE
HKEY_USERS

- subKey : string

 The name of the key to delete. This key must be a subkey of the key identified by the key parameter. This value must not be None, and the key may not have subkeys.

#### Comments

 If the method succeeds, the entire key, including all of its values, is removed. If the method fails, and exception is raised.

#### Win32 API References

- Search for RegDeleteKey at [msdn](https://learn.microsoft.com/en-ca/search/?terms=RegDeleteKey), [google](https://www.google.com/search?q=RegDeleteKey) or [google groups](https://groups.google.com/groups?q=RegDeleteKey).


---

<!-- page: win32api__RegDeleteTree_meth.html -->

## win32api.RegDeleteTree

 RegDeleteTree(Key, SubKey)

Recursively deletes a key's subkeys and values

#### Parameters

- Key : PyHKEY

 Handle to a registry key

- SubKey : PyUnicode

 Name of subkey to be deleted, or None for all subkeys and values

#### Comments

 Accepts keyword args.


---

<!-- page: win32api__RegDeleteValue_meth.html -->

## win32api.RegDeleteValue

 RegDeleteValue(key, value)

Removes a named value from the specified registry key.

#### Parameters

- key : PyHKEY/int

 An already open key, or any one of the following win32con constants:
HKEY_CLASSES_ROOT
HKEY_CURRENT_USER
HKEY_LOCAL_MACHINE
HKEY_USERS

- value : string

 The name of the value to remove.

#### Win32 API References

- Search for RegDeleteValue at [msdn](https://learn.microsoft.com/en-ca/search/?terms=RegDeleteValue), [google](https://www.google.com/search?q=RegDeleteValue) or [google groups](https://groups.google.com/groups?q=RegDeleteValue).


---

<!-- page: win32api__RegEnumKeyExW_meth.html -->

## win32api.RegEnumKeyExW

 tuple = RegEnumKeyExW(Key)

Unicode version of RegEnumKeyEx

#### Parameters

- Key : PyHKEY

 Registry handle opened with KEY_ENUMERATE_SUB_KEYS, or one of win32con.HKEY_* constants

#### Return Value

Returns subkeys as tuples of (name, reserved, class, last write time). Reserved will always be 0.


---

<!-- page: win32api__RegEnumKey_meth.html -->

## win32api.RegEnumKey

 string = RegEnumKey(key, index )

Enumerates subkeys of the specified open registry key. The function retrieves the name of one subkey each time it is called.

#### Parameters

- key : PyHKEY/int

 An already open key, or any one of the following win32con constants:
HKEY_CLASSES_ROOT
HKEY_CURRENT_USER
HKEY_LOCAL_MACHINE
HKEY_USERS

- index : int

 The index of the key to retrieve.

#### Win32 API References

- Search for RegEnumKey at [msdn](https://learn.microsoft.com/en-ca/search/?terms=RegEnumKey), [google](https://www.google.com/search?q=RegEnumKey) or [google groups](https://groups.google.com/groups?q=RegEnumKey).


---

<!-- page: win32api__RegEnumValue_meth.html -->

## win32api.RegEnumValue

 (string,object,type) = RegEnumValue(key, index )

Enumerates values of the specified open registry key. The function retrieves the name of one subkey each time it is called.

#### Parameters

- key : PyHKEY/int

 An already open key, or any one of the following win32con constants:
HKEY_CLASSES_ROOT
HKEY_CURRENT_USER
HKEY_LOCAL_MACHINE
HKEY_USERS

- index : int

 The index of the key to retrieve.

#### Comments

 This function is typically called repeatedly, until an exception is raised, indicating no more values.

#### Win32 API References

- Search for PyRegEnumValue at [msdn](https://learn.microsoft.com/en-ca/search/?terms=PyRegEnumValue), [google](https://www.google.com/search?q=PyRegEnumValue) or [google groups](https://groups.google.com/groups?q=PyRegEnumValue).


---

<!-- page: win32api__RegFlushKey_meth.html -->

## win32api.RegFlushKey

 RegFlushKey(key)

Writes all the attributes of the specified key to the registry.

#### Parameters

- key : PyHKEY/int

 An already open key, or any one of the following win32con constants:
HKEY_CLASSES_ROOT
HKEY_CURRENT_USER
HKEY_LOCAL_MACHINE
HKEY_USERS

#### Comments

 It is not necessary to call RegFlushKey to change a key. Registry changes are flushed to disk by the registry using its lazy flusher. Registry changes are also flushed to disk at system shutdown.
Unlike win32api::RegCloseKey, the RegFlushKey method returns only when all the data has been written to the registry.
An application should only call RegFlushKey if it requires absolute certainty that registry changes are on disk. If you don't know whether a RegFlushKey call is required, it probably isn't.

#### Win32 API References

- Search for RegFlushKey at [msdn](https://learn.microsoft.com/en-ca/search/?terms=RegFlushKey), [google](https://www.google.com/search?q=RegFlushKey) or [google groups](https://groups.google.com/groups?q=RegFlushKey).


---

<!-- page: win32api__RegGetKeySecurity_meth.html -->

## win32api.RegGetKeySecurity

 PySECURITY_DESCRIPTOR = RegGetKeySecurity(key, security_info )

Retrieves the security on the specified registry key.

#### Parameters

- key : PyHKEY/int

 Handle to an open key for which the security descriptor is set.

- security_info : int

 Specifies the components of the security descriptor to retrieve. The value can be a combination of the *_SECURITY_INFORMATION constants.

#### Win32 API References

- Search for RegGetKeySecurity at [msdn](https://learn.microsoft.com/en-ca/search/?terms=RegGetKeySecurity), [google](https://www.google.com/search?q=RegGetKeySecurity) or [google groups](https://groups.google.com/groups?q=RegGetKeySecurity).


---

<!-- page: win32api__RegLoadKey_meth.html -->

## win32api.RegLoadKey

 RegLoadKey(key, subKey, filename)

The RegLoadKey method creates a subkey under HKEY_USER or HKEY_LOCAL_MACHINE and stores registration information from a specified file into that subkey.

#### Parameters

- key : PyHKEY/int

 An already open key, or any one of the following win32con constants:
HKEY_CLASSES_ROOT
HKEY_CURRENT_USER
HKEY_LOCAL_MACHINE
HKEY_USERS

- subKey : string

 The name of the key to delete. This key must be a subkey of the key identified by the key parameter. This value must not be None, and the key may not have subkeys.

- filename : string

 The name of the file to load registry data from. This file must have been created with the win32api::RegSaveKey function. Under the file allocation table (FAT) file system, the filename may not have an extension.

#### Comments

 A call to RegLoadKey fails if the calling process does not have the SE_RESTORE_PRIVILEGE privilege.
If hkey is a handle returned by win32api::RegConnectRegistry, then the path specified in fileName is relative to the remote computer.

#### Win32 API References

- Search for RegLoadKey at [msdn](https://learn.microsoft.com/en-ca/search/?terms=RegLoadKey), [google](https://www.google.com/search?q=RegLoadKey) or [google groups](https://groups.google.com/groups?q=RegLoadKey).


---

<!-- page: win32api__RegNotifyChangeKeyValue_meth.html -->

## win32api.RegNotifyChangeKeyValue

 RegNotifyChangeKeyValue(key, bWatchSubTree, dwNotifyFilter, hKey, fAsynchronous)

Receive notification of registry changes

#### Parameters

- key : PyHKEY/int

 Handle to an open registry key

- bWatchSubTree : int

 Boolean, notify of changes to subkeys if True

- dwNotifyFilter : int

 Combination of REG_NOTIFY_CHANGE_* constants

- hKey : PyHANDLE

 Event handle to be signalled, use None if fAsynchronous is False

- fAsynchronous : int

 Boolean, function returns immediately if True, waits for change if False


---

<!-- page: win32api__RegOpenCurrentUser_meth.html -->

## win32api.RegOpenCurrentUser

 PyHKEY = RegOpenCurrentUser(samDesired)

Opens HKEY_CURRENT_USER for impersonated user

#### Parameters

- samDesired=MAXIMUM_ALLOWED : int

 Desired access, combination of win32con.KEY_*

#### Win32 API References

- Search for RegOpenCurrentUser at [msdn](https://learn.microsoft.com/en-ca/search/?terms=RegOpenCurrentUser), [google](https://www.google.com/search?q=RegOpenCurrentUser) or [google groups](https://groups.google.com/groups?q=RegOpenCurrentUser).


---

<!-- page: win32api__RegOpenKeyEx_meth.html -->

## win32api.RegOpenKeyEx

 PyHKEY = RegOpenKeyEx(key, subKey , reserved , sam )

Opens the specified key.

#### Parameters

- key : PyHKEY/int

 An already open key, or any one of the following win32con constants:
HKEY_CLASSES_ROOT
HKEY_CURRENT_USER
HKEY_LOCAL_MACHINE
HKEY_USERS

- subKey : string

 The name of a key that this method opens. This key must be a subkey of the key identified by the key parameter. If key is one of the predefined keys, subKey may be None. In that case, the handle returned is the same key handle passed in to the function.

- reserved=0 : int

 Reserved. Must be zero.

- sam=KEY_READ : int

 Specifies an access mask that describes the desired security access for the new key. This parameter can be a combination of the following win32con constants:
KEY_ALL_ACCESS
KEY_CREATE_LINK
KEY_CREATE_SUB_KEY
KEY_ENUMERATE_SUB_KEYS
KEY_EXECUTE
KEY_NOTIFY
KEY_QUERY_VALUE
KEY_READ
KEY_SET_VALUE
KEY_WRITE

#### Win32 API References

- Search for RegOpenKeyEx at [msdn](https://learn.microsoft.com/en-ca/search/?terms=RegOpenKeyEx), [google](https://www.google.com/search?q=RegOpenKeyEx) or [google groups](https://groups.google.com/groups?q=RegOpenKeyEx).

#### Return Value

The return value is the handle of the opened key. If the function fails, an exception is raised.


---

<!-- page: win32api__RegOpenKeyTransacted_meth.html -->

## win32api.RegOpenKeyTransacted

 PyHKEY = RegOpenKeyTransacted(Key, SubKey , samDesired , Transaction , Options )

Opens a registry key as part of a transaction

#### Parameters

- Key : PyHKEY/int

 Registry key or one of win32con.HKEY_* values

- SubKey : PyUnicode

 Name of subkey to open. Can be None to reopen an existing key.

- samDesired : int

 Access allowed to handle, combination of win32con.KEY_* constants. Can also contain standard access rights such as DELETE, WRITE_OWNER, etc.

- Transaction : PyHANDLE

 Handle to a transaction as returned by win32transaction::CreateTransaction

- Options=0 : int

 Reserved, use only 0

#### Comments

 Accepts keyword arguments.

#### Win32 API References

- Search for RegOpenKeyTransacted at [msdn](https://learn.microsoft.com/en-ca/search/?terms=RegOpenKeyTransacted), [google](https://www.google.com/search?q=RegOpenKeyTransacted) or [google groups](https://groups.google.com/groups?q=RegOpenKeyTransacted).

#### Return Value

Returns a transacted registry handle. Note that operations on subkeys are not automatically transacted.


---

<!-- page: win32api__RegOpenKey_meth.html -->

## win32api.RegOpenKey

 PyHKEY = RegOpenKey()

Opens the specified key.

#### Comments

 This funcion is implemented using win32api::RegOpenKeyEx, by taking advantage of default parameters. See win32api::RegOpenKeyEx for more details.


---

<!-- page: win32api__RegOverridePredefKey_meth.html -->

## win32api.RegOverridePredefKey

 RegOverridePredefKey(Key, NewKey)

Redirects one of the predefined keys to different key

#### Parameters

- Key : PyHKEY

 One of the predefined registry keys (win32con.HKEY_*)

- NewKey : PyHKEY

 Registry key to which it will be redirected. Pass None to restore original key.

#### Win32 API References

- Search for RegOverridePredefKey at [msdn](https://learn.microsoft.com/en-ca/search/?terms=RegOverridePredefKey), [google](https://www.google.com/search?q=RegOverridePredefKey) or [google groups](https://groups.google.com/groups?q=RegOverridePredefKey).


---

<!-- page: win32api__RegQueryInfoKeyW_meth.html -->

## win32api.RegQueryInfoKeyW

 dict = RegQueryInfoKeyW(Key)

Returns information about an open registry key

#### Parameters

- Key : PyHKEY

 Handle to a registry key, or one of win32con.HKEY_* constants

#### Win32 API References

- Search for RegQueryInfoKeyW at [msdn](https://learn.microsoft.com/en-ca/search/?terms=RegQueryInfoKeyW), [google](https://www.google.com/search?q=RegQueryInfoKeyW) or [google groups](https://groups.google.com/groups?q=RegQueryInfoKeyW).


---

<!-- page: win32api__RegQueryInfoKey_meth.html -->

## win32api.RegQueryInfoKey

 (int, int, long) = RegQueryInfoKey(key)

Returns the number of subkeys, the number of values a key has, and if available the last time the key was modified as 100's of nanoseconds since Jan 1, 1600.

#### Parameters

- key : PyHKEY/int

 An already open key, or or any one of the following win32con constants:
HKEY_CLASSES_ROOT
HKEY_CURRENT_USER
HKEY_LOCAL_MACHINE
HKEY_USERS

#### Win32 API References

- Search for RegQueryInfoKey at [msdn](https://learn.microsoft.com/en-ca/search/?terms=RegQueryInfoKey), [google](https://www.google.com/search?q=RegQueryInfoKey) or [google groups](https://groups.google.com/groups?q=RegQueryInfoKey).


---

<!-- page: win32api__RegQueryValueEx_meth.html -->

## win32api.RegQueryValueEx

 (object,type) = RegQueryValueEx(key, valueName )

Retrieves the type and data for a specified value name associated with an open registry key.

#### Parameters

- key : PyHKEY/int

 An already open key, or any one of the following win32con constants:
HKEY_CLASSES_ROOT
HKEY_CURRENT_USER
HKEY_LOCAL_MACHINE
HKEY_USERS

- valueName : string

 The name of the value to query.

#### Comments

 Values in the registry have name, type, and data components. This method retrieves the data for the given value.

#### Win32 API References

- Search for RegQueryValueEx at [msdn](https://learn.microsoft.com/en-ca/search/?terms=RegQueryValueEx), [google](https://www.google.com/search?q=RegQueryValueEx) or [google groups](https://groups.google.com/groups?q=RegQueryValueEx).


---

<!-- page: win32api__RegQueryValue_meth.html -->

## win32api.RegQueryValue

 string = RegQueryValue(key, subKey )

The RegQueryValue method retrieves the value associated with the unnamed value for a specified key in the registry.

#### Parameters

- key : PyHKEY/int

 An already open key, or any one of the following win32con constants:
HKEY_CLASSES_ROOT
HKEY_CURRENT_USER
HKEY_LOCAL_MACHINE
HKEY_USERS

- subKey : string

 The name of the subkey with which the value is associated. If this parameter is None or empty, the function retrieves the value set by the win32api::RegSetValue method for the key identified by key.

#### Comments

 Values in the registry have name, type, and data components. This method retrieves the data for a key's first value that has a NULL name. But the underlying API call doesn't return the type, Lame Lame Lame, DONT USE THIS!!!

#### Win32 API References

- Search for RegQueryValue at [msdn](https://learn.microsoft.com/en-ca/search/?terms=RegQueryValue), [google](https://www.google.com/search?q=RegQueryValue) or [google groups](https://groups.google.com/groups?q=RegQueryValue).


---

<!-- page: win32api__RegRestoreKey_meth.html -->

## win32api.RegRestoreKey

 RegRestoreKey(Key, File, Flags)

Restores a key and subkeys from a saved registry file

#### Parameters

- Key : PyHKEY

 Handle to registry key to be restored. Can also be one of win32con.HKEY_* values.

- File : PyUnicode

 File from which to restore registry data

- Flags=0 : int

 One of REG_FORCE_RESTORE,REG_NO_LAZY_FLUSH,REG_REFRESH_HIVE,REG_WHOLE_HIVE_VOLATILE (from winnt)

#### Comments

 Implemented only as Unicode (RegRestoreKeyW). Accepts keyword arguments.

 Requires SeBackupPrivilege and SeRestorePrivilege

#### Win32 API References

- Search for RegRestoreKey at [msdn](https://learn.microsoft.com/en-ca/search/?terms=RegRestoreKey), [google](https://www.google.com/search?q=RegRestoreKey) or [google groups](https://groups.google.com/groups?q=RegRestoreKey).


---

<!-- page: win32api__RegSaveKeyEx_meth.html -->

## win32api.RegSaveKeyEx

 RegSaveKeyEx(Key, File, SecurityAttributes, Flags)

Extended version of RegSaveKey

#### Parameters

- Key : PyHKEY

 Handle to a registry key or one of HKEY_CURRENT_CONFIG, HKEY_CURRENT_USER

- File : PyUnicode

 Name of file in which to save data. File must not already exist.

- SecurityAttributes=None : PySECURITY_ATTRIBUTES

 Specifies security for the file to be created

- Flags=REG_LATEST_FORMAT : int

 One of REG_STANDARD_FORMAT,REG_LATEST_FORMAT,REG_NO_COMPRESSION (from winnt.py)

#### Comments

 Implemented only as Unicode (RegSaveKeyExW). Accepts keyword arguments.

 SE_BACKUP_NAME privilege must be enabled.

#### Win32 API References

- Search for RegSaveKeyEx at [msdn](https://learn.microsoft.com/en-ca/search/?terms=RegSaveKeyEx), [google](https://www.google.com/search?q=RegSaveKeyEx) or [google groups](https://groups.google.com/groups?q=RegSaveKeyEx).


---

<!-- page: win32api__RegSaveKey_meth.html -->

## win32api.RegSaveKey

 RegSaveKey(key, filename, sa)

The RegSaveKey method saves the specified key, and all its subkeys to the specified file.

#### Parameters

- key : PyHKEY/int

 An already open key, or any one of the following win32con constants:
HKEY_CLASSES_ROOT
HKEY_CURRENT_USER
HKEY_LOCAL_MACHINE
HKEY_USERS

- filename : string

 The name of the file to save registry data to. This file cannot already exist. If this filename includes an extension, it cannot be used on file allocation table (FAT) file systems by the win32api::RegLoadKey, win32api::RegReplaceKey , or win32api::RegRestoreKey methods.

- sa=None : PySECURITY_ATTRIBUTES

 The security attributes of the created file.

#### Comments

 If key represents a key on a remote computer, the path described by fileName is relative to the remote computer.
The caller of this method must possess the SeBackupPrivilege security privilege.

#### Win32 API References

- Search for RegSaveKey at [msdn](https://learn.microsoft.com/en-ca/search/?terms=RegSaveKey), [google](https://www.google.com/search?q=RegSaveKey) or [google groups](https://groups.google.com/groups?q=RegSaveKey).


---

<!-- page: win32api__RegSetKeySecurity_meth.html -->

## win32api.RegSetKeySecurity

 RegSetKeySecurity(key, security_info, sd)

Sets the security on the specified registry key.

#### Parameters

- key : PyHKEY/int

 Handle to an open key for which the security descriptor is set.

- security_info : int

 Specifies the components of the security descriptor to set. The value can be a combination of the *_SECURITY_INFORMATION constants.

- sd : PySECURITY_DESCRIPTOR

 The new security descriptor for the key

#### Comments

 If key is one of the predefined keys, the predefined key should be closed with win32api::RegCloseKey. That ensures that the new security information is in effect the next time the predefined key is referenced.

#### Win32 API References

- Search for PyRegSetKeySecurity at [msdn](https://learn.microsoft.com/en-ca/search/?terms=PyRegSetKeySecurity), [google](https://www.google.com/search?q=PyRegSetKeySecurity) or [google groups](https://groups.google.com/groups?q=PyRegSetKeySecurity).


---

<!-- page: win32api__RegSetValueEx_meth.html -->

## win32api.RegSetValueEx

 RegSetValueEx(key, valueName, reserved, type, value)

Stores data in the value field of an open registry key.

#### Parameters

- key : PyHKEY/int

 An already open key, or any one of the following win32con constants:
HKEY_CLASSES_ROOT
HKEY_CURRENT_USER
HKEY_LOCAL_MACHINE
HKEY_USERS

- valueName : string

 The name of the value to set. If a value with this name is not already present in the key, the method adds it to the key.
If this parameter is None or an empty string and the type parameter is the win32api.REG_SZ type, this function sets the same value the win32api::RegSetValue method would set.

- reserved : any

 Place holder for reserved argument. Zero will always be passed to the API function.

- type : int

 Type of data.

| | Value | Meaning
| |

---

 |

---

| | REG_BINARY | Binary data in any form.
| | REG_DWORD | A 32-bit number.
| | REG_DWORD_LITTLE_ENDIAN | A 32-bit number in little-endian format. This is equivalent to REG_DWORD.
In little-endian format, a multi-byte value is stored in memory from the lowest byte (the little end) to the highest byte. For example, the value 0x12345678 is stored as (0x78 0x56 0x34 0x12) in little-endian format.
| | REG_QWORD | A 64-bit number.
| | REG_QWORD_LITTLE_ENDIAN | A 64-bit number in little-endian format. This is equivalent to REG_QWORD.
In little-endian format, a multi-byte value is stored in memory from the lowest byte (the little end) to the highest byte. For example, the value 0x12345678 is stored as (0x78 0x56 0x34 0x12) in little-endian format. Windows NT is designed to run on little-endian computer architectures. A user may connect to computers that have big-endian architectures, such as some UNIX systems.
| | REG_DWORD_BIG_ENDIAN | A 32-bit number in big-endian format. In big-endian format, a multi-byte value is stored in memory from the highest byte (the big end) to the lowest byte. For example, the value 0x12345678 is stored as (0x12 0x34 0x56 0x78) in big-endian format.
| | REG_EXPAND_SZ | A null-terminated string that contains unexpanded references to environment variables (for example, %PATH%). It will be a Unicode or ANSI string depending on whether you use the Unicode or ANSI functions.
| | REG_LINK | A Unicode symbolic link.
| | REG_MULTI_SZ | An array of null-terminated strings, terminated by two null characters.
| | REG_NONE | No defined value type.
| | REG_RESOURCE_LIST | A device-driver resource list.
| | REG_SZ | A null-terminated string. It will be a Unicode or ANSI string depending on whether you use the Unicode or ANSI functions
- value : registry data

 The value to be stored with the specified value name.

#### Comments

 This method can also set additional value and type information for the specified key.
The key identified by the key parameter must have been opened with KEY_SET_VALUE access. To open the key, use the win32api::RegCreateKeyEx or win32api::RegOpenKeyEx methods.
Value lengths are limited by available memory. Long values (more than 2048 bytes) should be stored as files with the filenames stored in the configuration registry. This helps the registry perform efficiently.
The key identified by the key parameter must have been opened with KEY_SET_VALUE access.

#### Win32 API References

- Search for RegSetValueEx at [msdn](https://learn.microsoft.com/en-ca/search/?terms=RegSetValueEx), [google](https://www.google.com/search?q=RegSetValueEx) or [google groups](https://groups.google.com/groups?q=RegSetValueEx).


---

<!-- page: win32api__RegSetValue_meth.html -->

## win32api.RegSetValue

 RegSetValue(key, subKey, type, value)

Associates a value with a specified key. Currently, only strings are supported.

#### Parameters

- key : PyHKEY/int

 An already open key, or any one of the following win32con constants:
HKEY_CLASSES_ROOT
HKEY_CURRENT_USER
HKEY_LOCAL_MACHINE
HKEY_USERS

- subKey : string

 The name of the subkey with which the value is associated. This parameter can be None or empty, in which case the value will be added to the key identified by the key parameter.

- type : int

 Type of data. Must be win32con.REG_SZ

- value : string

 The value to associate with the key.

#### Comments

 If the key specified by the lpszSubKey parameter does not exist, the RegSetValue function creates it.
Value lengths are limited by available memory. Long values (more than 2048 bytes) should be stored as files with the filenames stored in the configuration registry. This helps the registry perform efficiently.
The key identified by the key parameter must have been opened with KEY_SET_VALUE access.

#### Win32 API References

- Search for RegSetValue at [msdn](https://learn.microsoft.com/en-ca/search/?terms=RegSetValue), [google](https://www.google.com/search?q=RegSetValue) or [google groups](https://groups.google.com/groups?q=RegSetValue).


---

<!-- page: win32api__RegUnLoadKey_meth.html -->

## win32api.RegUnLoadKey

 RegUnLoadKey(key, subKey)

The RegUnLoadKey function unloads the specified registry key and its subkeys from the registry. The key should have been created by a previous call to win32api::RegLoadKey.

#### Parameters

- key : PyHKEY/int

 An already open key, or any one of the following win32con constants:
HKEY_USERS
HKEY_LOCAL_MACHINE

- subKey : string

 The name of the key to unload. This key must be a subkey of the key identified by the key parameter. This value must not be None.

#### Comments

 A call to RegUnLoadKey fails if the calling process does not have the SE_RESTORE_PRIVILEGE privilege.
If hkey is a handle returned by win32api::RegConnectRegistry, then the path specified in fileName is relative to the remote computer.

#### Win32 API References

- Search for RegUnLoadKey at [msdn](https://learn.microsoft.com/en-ca/search/?terms=RegUnLoadKey), [google](https://www.google.com/search?q=RegUnLoadKey) or [google groups](https://groups.google.com/groups?q=RegUnLoadKey).


---

<!-- page: win32api__RegisterWindowMessage_meth.html -->

## win32api.RegisterWindowMessage

 RegisterWindowMessage(msgString)

The RegisterWindowMessage method, given a string, returns a system wide unique message ID, suitable for sending messages between applications who both register the same string.

#### Parameters

- msgString : string

 The name of the message to register. All applications that register this message string will get the same message. ID back. It will be unique in the system and suitable for applications to use to exchange messages.

#### Comments

 Only use RegisterWindowMessage when more than one application must process the
 same message. For sending private messages within a window class, an application
 can use any integer in the range WM_USER through 0x7FFF. (Messages in this range
 are private to a window class, not to an application. For example, predefined
 control classes such as BUTTON, EDIT, LISTBOX, and COMBOBOX may use values in
 this range.)

#### Win32 API References

- Search for RegisterWindowMessage at [msdn](https://learn.microsoft.com/en-ca/search/?terms=RegisterWindowMessage), [google](https://www.google.com/search?q=RegisterWindowMessage) or [google groups](https://groups.google.com/groups?q=RegisterWindowMessage).


---

<!-- page: win32api__SearchPath_meth.html -->

## win32api.SearchPath

 int = SearchPath(path, fileName , fileExt )

Searches a path for the specified file.

#### Parameters

- path : string

 The path to search. If None, searches the standard paths.

- fileName : string

 The name of the file to search for.

- fileExt=None : string

 specifies an extension to be added to the filename when searching for the file. The first character of the filename extension must be a period (.). The extension is added only if the specified filename does not end with an extension. If a filename extension is not required or if the filename contains an extension, this parameter can be None.

#### Win32 API References

- Search for SearchPath at [msdn](https://learn.microsoft.com/en-ca/search/?terms=SearchPath), [google](https://www.google.com/search?q=SearchPath) or [google groups](https://groups.google.com/groups?q=SearchPath).

#### Return Value

The return value is a tuple of (string, int). string is the full path name located. int is the offset in the string of the base name of the file.


---

<!-- page: win32api__SendMessage_meth.html -->

## win32api.SendMessage

 SendMessage(hwnd, idMessage, wParam, lParam)

Send a message to a window.

#### Parameters

- hwnd : PyHANDLE

 The hWnd of the window to receive the message.

- idMessage : int

 The ID of the message to send.

- wParam=None : int/string

 The wParam for the message

- lParam=None : int/string

 The lParam for the message

#### Win32 API References

- Search for SendMessage at [msdn](https://learn.microsoft.com/en-ca/search/?terms=SendMessage), [google](https://www.google.com/search?q=SendMessage) or [google groups](https://groups.google.com/groups?q=SendMessage).


---

<!-- page: win32api__SetClassLong_meth.html -->

## win32api.SetClassLong

 int = SetClassLong(hwnd, offset , val )

Replaces the specified 32 or 64 bit value at the specified offset into the extra class memory for the window.

#### Parameters

- hwnd : PyHANDLE

 The handle to the window.

- offset : int

 Specifies the zero-based byte offset of the value to change. Valid values are in the range zero through the number of bytes of extra window memory, minus four (for example, if 12 or more bytes of extra memory were specified, a value of 8 would be an index to the third long integer), or one of the GWL_ constants.

- val : int

 Specifies the long value to place in the window's reserved memory.

#### Comments

 This function calls the SetClassLongPtr Api function


---

<!-- page: win32api__SetClassWord_meth.html -->

## win32api.SetClassWord

 int = SetClassWord(hwnd, offset , val )

#### Parameters

- hwnd : int

 The handle to the window.

- offset : int

 Specifies the zero-based byte offset of the value to change. Valid values are in the range zero through the number of bytes of extra window memory, minus four (for example, if 12 or more bytes of extra memory were specified, a value of 8 would be an index to the third long integer), or one of the GWL_ constants.

- val : int

 Specifies the long value to place in the window's reserved memory.

#### Comments

 This function is obsolete, use win32api::SetClassLong instead


---

<!-- page: win32api__SetConsoleCtrlHandler_meth.html -->

## win32api.SetConsoleCtrlHandler

 SetConsoleCtrlHandler(ctrlHandler, bAdd)

Adds or removes an application-defined HandlerRoutine function from the list of handler functions for the calling process.

#### Parameters

- ctrlHandler : callable

 The function to call. This function should accept one param - the type of signal.

- bAdd : int

 True if the handler is being added, false if removed.

#### Comments

 Note that the implementation is a single CtrlHandler in C, which keeps a list of the handlers added by this function. So although this function uses the same semantics as the Win32 function (ie, last registered first called, and first to return True stops the calls) the true order of all Python and C implemented CtrlHandlers may not match what would happen if all were implemented in C.
This handler must acquire the Python lock before it can call any of the registered handlers. This means the handler may not be called until the current Python thread yields the lock.
 A console process can use the win32api::GenerateConsoleCtrlEvent function to send a CTRL+C or CTRL+BREAK signal to a console process group.
The system generates CTRL_CLOSE_EVENT, CTRL_LOGOFF_EVENT, and CTRL_SHUTDOWN_EVENT signals when the user closes the console, logs off, or shuts down the system so that the process has an opportunity to clean up before termination.

#### Win32 API References

- Search for SetConsoleCtrlHandler at [msdn](https://learn.microsoft.com/en-ca/search/?terms=SetConsoleCtrlHandler), [google](https://www.google.com/search?q=SetConsoleCtrlHandler) or [google groups](https://groups.google.com/groups?q=SetConsoleCtrlHandler).


---

<!-- page: win32api__SetConsoleTitle_meth.html -->

## win32api.SetConsoleTitle

 SetConsoleTitle(title)

Sets the title for the current console.

#### Parameters

- title : string

 The new title

#### Win32 API References

- Search for SetConsoleTitle at [msdn](https://learn.microsoft.com/en-ca/search/?terms=SetConsoleTitle), [google](https://www.google.com/search?q=SetConsoleTitle) or [google groups](https://groups.google.com/groups?q=SetConsoleTitle).


---

<!-- page: win32api__SetCursorPos_meth.html -->

## win32api.SetCursorPos

 SetCursorPos(x,y)

The SetCursorPos function moves the cursor to the specified screen coordinates.

#### Parameters

- x,y : (int, int)

 The new position.

#### Win32 API References

- Search for SetCursorPos at [msdn](https://learn.microsoft.com/en-ca/search/?terms=SetCursorPos), [google](https://www.google.com/search?q=SetCursorPos) or [google groups](https://groups.google.com/groups?q=SetCursorPos).


---

<!-- page: win32api__SetCursor_meth.html -->

## win32api.SetCursor

 PyHANDLE = SetCursor(hCursor)

Set the cursor to the HCURSOR object.

#### Parameters

- hCursor : PyHANDLE

 The new cursor. Can be None to remove cursor.

#### Win32 API References

- Search for SetCursor at [msdn](https://learn.microsoft.com/en-ca/search/?terms=SetCursor), [google](https://www.google.com/search?q=SetCursor) or [google groups](https://groups.google.com/groups?q=SetCursor).

#### Return Value

The result is the previous cursor if there was one.


---

<!-- page: win32api__SetDllDirectory_meth.html -->

## win32api.SetDllDirectory

 SetDllDirectory(PathName)

Modifies the application-specific DLL search path

#### Parameters

- PathName : PyUnicode

 Directory to be added to search path, can be None to restore defaults

#### Win32 API References

- Search for SetDllDirectory at [msdn](https://learn.microsoft.com/en-ca/search/?terms=SetDllDirectory), [google](https://www.google.com/search?q=SetDllDirectory) or [google groups](https://groups.google.com/groups?q=SetDllDirectory).


---

<!-- page: win32api__SetEnvironmentVariableW_meth.html -->

## win32api.SetEnvironmentVariableW

 SetEnvironmentVariableW(Name, Value)

Creates, deletes, or changes the value of an environment variable.

#### Parameters

- Name : str

 Name of the environment variable

- Value : str

 Value to be set, or None to remove variable

#### Win32 API References

- Search for SetEnvironmentVariable at [msdn](https://learn.microsoft.com/en-ca/search/?terms=SetEnvironmentVariable), [google](https://www.google.com/search?q=SetEnvironmentVariable) or [google groups](https://groups.google.com/groups?q=SetEnvironmentVariable).


---

<!-- page: win32api__SetErrorMode_meth.html -->

## win32api.SetErrorMode

 int = SetErrorMode(errorMode)

Controls whether the system will handle the specified types of serious errors, or whether the process will handle them.

#### Parameters

- errorMode : int

 A set of bit flags that specify the process error mode

#### Win32 API References

- Search for SetErrorMode at [msdn](https://learn.microsoft.com/en-ca/search/?terms=SetErrorMode), [google](https://www.google.com/search?q=SetErrorMode) or [google groups](https://groups.google.com/groups?q=SetErrorMode).

#### Return Value

The result is an integer containing the old error flags.


---

<!-- page: win32api__SetFileAttributes_meth.html -->

## win32api.SetFileAttributes

 int = SetFileAttributes(pathName, attrs )

Sets the named file's attributes.

#### Parameters

- pathName : string

 The name of the file.

- attrs : int

 The attributes to set. Must be a combination of the win32con.FILE_ATTRIBUTE_* constants.


---

<!-- page: win32api__SetHandleInformation_meth.html -->

## win32api.SetHandleInformation

 SetHandleInformation(Object, Mask, Flags)

Sets a handles's flags

#### Parameters

- Object : PyHANDLE

 Handle to an object

- Mask : int

 Bitmask specifying which flags should be set

- Flags : int

 Bitmask of flag values to be set. Valid Flags are HANDLE_FLAG_INHERIT, HANDLE_FLAG_PROTECT_FROM_CLOSE


---

<!-- page: win32api__SetLastError_meth.html -->

## win32api.SetLastError

 int = SetLastError()

Sets the calling thread's last error code value.

#### Win32 API References

- Search for SetLastError at [msdn](https://learn.microsoft.com/en-ca/search/?terms=SetLastError), [google](https://www.google.com/search?q=SetLastError) or [google groups](https://groups.google.com/groups?q=SetLastError).


---

<!-- page: win32api__SetLocalTime_meth.html -->

## win32api.SetLocalTime

 SetLocalTime(SystemTime)

Changes the system's local time

#### Parameters

- SystemTime : PyDateTime

 The local time to be set. Can also be a time tuple.


---

<!-- page: win32api__SetStdHandle_meth.html -->

## win32api.SetStdHandle

 SetStdHandle(handle, handle)

Set the handle for the standard input, standard output, or standard error device

#### Parameters

- handle : int

 input, output, or error device

- handle : PyHANDLE/int

 A previously opened handle to be a standard handle


---

<!-- page: win32api__SetSysColors_meth.html -->

## win32api.SetSysColors

 SetSysColors(Elements, RgbValues)

Changes color of various window elements

#### Parameters

- Elements : tuple

 A tuple of ints, COLOR_* constants indicating which window element to change

- RgbValues : tuple

 An equal length tuple of ints representing RGB values (see win32api::RGB)


---

<!-- page: win32api__SetSystemFileCacheSize_meth.html -->

## win32api.SetSystemFileCacheSize

 SetSystemFileCacheSize(MinimumFileCacheSize, MaximumFileCacheSize, Flags)

Sets the amount of memory reserved for file cache

#### Parameters

- MinimumFileCacheSize : long

 Minimum size in bytes.

- MaximumFileCacheSize : long

 Maximum size in bytes.

- Flags=0 : int

 Combination of win32con.MM_WORKING_SET_* flags

#### Comments

 Requires SE_INCREASE_QUOTA_NAME priv

 Pass -1 for both min and max to flush file cache.

 Accepts keyword args.


---

<!-- page: win32api__SetSystemPowerState_meth.html -->

## win32api.SetSystemPowerState

 SetSystemPowerState(Suspend, Force)

Initiates low power mode to make system sleep or hibernate

#### Parameters

- Suspend : boolean

 True - system is suspended. False - initiates hibernation.

- Force : boolean

 True - power state occurs unconditionally. False - applications are queried for permission.

#### Comments

 SE_SHUTDOWN_NAME privilege must be enabled.

#### Win32 API References

- Search for SetSystemPowerState at [msdn](https://learn.microsoft.com/en-ca/search/?terms=SetSystemPowerState), [google](https://www.google.com/search?q=SetSystemPowerState) or [google groups](https://groups.google.com/groups?q=SetSystemPowerState).


---

<!-- page: win32api__SetSystemTime_meth.html -->

## win32api.SetSystemTime

 int = SetSystemTime(year, month , dayOfWeek , day , hour , minute , second , millseconds )

Returns the current system time

#### Parameters

- year : int

- month : int

- dayOfWeek : int

- day : int

- hour : int

- minute : int

- second : int

- millseconds : int


---

<!-- page: win32api__SetThreadLocale_meth.html -->

## win32api.SetThreadLocale

 SetThreadLocale(lcid)

Sets the current thread's locale.

#### Parameters

- lcid : int

 The new LCID


---

<!-- page: win32api__SetTimeZoneInformation_meth.html -->

## win32api.SetTimeZoneInformation

 tuple = SetTimeZoneInformation(tzi)

Sets the system time-zone information.

#### Parameters

- tzi : tuple

 A tuple with the timezone info

#### Comments

 The tuple is of form:

#### Items

- [0] int : Bias

- [1] string : StandardName

- [2] SYSTEMTIME tuple : StandardDate

- [3] int : StandardBias

- [4] string : DaylightName

- [5] SYSTEMTIME tuple : DaylightDate

- [6] int : DaylightBias


---

<!-- page: win32api__SetWindowLong_meth.html -->

## win32api.SetWindowLong

 int = SetWindowLong(hwnd, offset , val )

Places a long value at the specified offset into the extra window memory of the given window.

#### Parameters

- hwnd : int

 The handle to the window.

- offset : int

 Specifies the zero-based byte offset of the value to change. Valid values are in the range zero through the number of bytes of extra window memory, minus four (for example, if 12 or more bytes of extra memory were specified, a value of 8 would be an index to the third long integer), or one of the GWL_ constants.

- val : int

 Specifies the long value to place in the window's reserved memory.

#### Comments

 This function calls the SetWindowLongPtr Api function


---

<!-- page: win32api__SetWindowWord_meth.html -->

## win32api.SetWindowWord

 int = SetWindowWord(hwnd, offset , val )

#### Parameters

- hwnd : PyHANDLE

 The handle to the window.

- offset : int

 Specifies the zero-based byte offset of the value to change. Valid values are in the range zero through the number of bytes of extra window memory, minus four (for example, if 12 or more bytes of extra memory were specified, a value of 8 would be an index to the third long integer), or one of the GWL_ constants.

- val : int

 Specifies the long value to place in the window's reserved memory.

#### Comments

 This function is obsolete, use win32api::SetWindowLong instead


---

<!-- page: win32api__ShellExecute_meth.html -->

## win32api.ShellExecute

 int = ShellExecute(hwnd, op , file , params , dir , bShow )

Opens or prints a file.

#### Parameters

- hwnd : PyHANDLE

 The handle of the parent window, or 0 for no parent. This window receives any message boxes an application produces (for example, for error reporting).

- op : string

 The operation to perform. May be "open", "print", or None, which defaults to "open".

- file : string

 The name of the file to open.

- params : string

 The parameters to pass, if the file name contains an executable. Should be None for a document file.

- dir : string

 The initial directory for the application.

- bShow : int

 Specifies whether the application is shown when it is opened. If the lpszFile parameter specifies a document file, this parameter is zero.

#### Win32 API References

- Search for ShellExecute at [msdn](https://learn.microsoft.com/en-ca/search/?terms=ShellExecute), [google](https://www.google.com/search?q=ShellExecute) or [google groups](https://groups.google.com/groups?q=ShellExecute).

#### Return Value

The instance handle of the application that was run. (This handle could also be the handle of a dynamic data exchange [DDE] server application.) If there is an error, the method raises an exception.


---

<!-- page: win32api__ShowCursor_meth.html -->

## win32api.ShowCursor

 int = ShowCursor(show)

The ShowCursor method displays or hides the cursor.

#### Parameters

- show : int

 Visiblilty flag

#### Comments

 This function sets an internal display counter that determines whether the cursor should be displayed. The cursor is displayed only if the display count is greater than or equal to 0. If a mouse is installed, the initial display count is 0. If no mouse is installed, the display count is -1.

#### Win32 API References

- Search for ShowCursor at [msdn](https://learn.microsoft.com/en-ca/search/?terms=ShowCursor), [google](https://www.google.com/search?q=ShowCursor) or [google groups](https://groups.google.com/groups?q=ShowCursor).

#### Return Value

The return value specifies the new display counter


---

<!-- page: win32api__Sleep_meth.html -->

## win32api.Sleep

 int = Sleep(time, bAlterable )

Suspends execution of the current thread for the specified time.

#### Parameters

- time : int

 The number of milli-seconds to sleep for,

- bAlterable=0 : int

 Specifies whether the function may terminate early due to an I/O completion callback function.

#### Win32 API References

- Search for Sleep at [msdn](https://learn.microsoft.com/en-ca/search/?terms=Sleep), [google](https://www.google.com/search?q=Sleep) or [google groups](https://groups.google.com/groups?q=Sleep).

- Search for SleepEx at [msdn](https://learn.microsoft.com/en-ca/search/?terms=SleepEx), [google](https://www.google.com/search?q=SleepEx) or [google groups](https://groups.google.com/groups?q=SleepEx).

#### Return Value

The return value is zero if the specified time interval expired.


---

<!-- page: win32api__TerminateProcess_meth.html -->

## win32api.TerminateProcess

 TerminateProcess(handle, exitCode)

Kills a process

#### Parameters

- handle : PyHANDLE

 The handle of the process to terminate.

- exitCode : int

 The exit code for the process.

#### Comments

 See also win32api::OpenProcess


---

<!-- page: win32api__ToAsciiEx_meth.html -->

## win32api.ToAsciiEx

 bytes = ToAsciiEx(vk, scancode , keyboardstate , flags , hlayout )

Translates the specified virtual-key code and keyboard state to the corresponding character or characters.

#### Parameters

- vk : int

 The virtual key code.

- scancode : int

 The scan code.

- keyboardstate : bytes

 A string of exactly 256 characters.

- flags=0 : int

- hlayout=None : handle

 The keyboard layout to use


---

<!-- page: win32api__UpdateResource_meth.html -->

## win32api.UpdateResource

 UpdateResource(handle, type, name, data, language)

Updates a resource in a PE file.

#### Parameters

- handle : PyHANDLE

 The update-file handle.

- type : PyResourceId

 The type of resource to update

- name : PyResourceId

 The id/name of the resource to update

- data : string

 The data to place into the resource.

- language=NEUTRAL : int

 Language to use, defaults to LANG_NEUTRAL.


---

<!-- page: win32api__VkKeyScanEx_meth.html -->

## win32api.VkKeyScanEx

 int = VkKeyScanEx(char, hkl )

Translates a character to the corresponding virtual-key code and shift state.

#### Parameters

- char : string or unicode

 A byte or unicode string of length 1. If a byte string is passed VkKeyScanExA will be called, otherwise VkKeyScanExW will be called.

- hkl : PyHANDLE

 Handle to a keyboard layout at returned by win32api::LoadKeyboardLayout

#### Win32 API References

- Search for VkKeyScanExA at [msdn](https://learn.microsoft.com/en-ca/search/?terms=VkKeyScanExA), [google](https://www.google.com/search?q=VkKeyScanExA) or [google groups](https://groups.google.com/groups?q=VkKeyScanExA).

- Search for VkKeyScanExW at [msdn](https://learn.microsoft.com/en-ca/search/?terms=VkKeyScanExW), [google](https://www.google.com/search?q=VkKeyScanExW) or [google groups](https://groups.google.com/groups?q=VkKeyScanExW).


---

<!-- page: win32api__VkKeyScan_meth.html -->

## win32api.VkKeyScan

 int = VkKeyScan(char, char )

Translates a character to the corresponding virtual-key code and shift state.

#### Parameters

- char : string or unicode

 A byte or unicode string of length 1. If a byte string is passed VkKeyScanA will be called, otherwise VkKeyScanW will be called.

- char : chr

 Specifies a character

#### Win32 API References

- Search for VkKeyScanA at [msdn](https://learn.microsoft.com/en-ca/search/?terms=VkKeyScanA), [google](https://www.google.com/search?q=VkKeyScanA) or [google groups](https://groups.google.com/groups?q=VkKeyScanA).

- Search for VkKeyScanW at [msdn](https://learn.microsoft.com/en-ca/search/?terms=VkKeyScanW), [google](https://www.google.com/search?q=VkKeyScanW) or [google groups](https://groups.google.com/groups?q=VkKeyScanW).


---

<!-- page: win32api__WinExec_meth.html -->

## win32api.WinExec

 WinExec(cmdLine, show)

Runs the specified application.

#### Parameters

- cmdLine : string

 The command line to execute.

- show=win32con.SW_SHOWNORMAL : int

 The initial state of the applications window.

#### Win32 API References

- Search for WinExec at [msdn](https://learn.microsoft.com/en-ca/search/?terms=WinExec), [google](https://www.google.com/search?q=WinExec) or [google groups](https://groups.google.com/groups?q=WinExec).


---

<!-- page: win32api__WinHelp_meth.html -->

## win32api.WinHelp

 WinHelp(hwnd, hlpFile, cmd, data)

Invokes the Windows Help system.

#### Parameters

- hwnd : int

 The handle of the window requesting help.

- hlpFile : string

 The name of the help file.

- cmd : int

 The type of help. See the api for full details.

- data=0 : int/string

 Additional data specific to the help call.

#### Win32 API References

- Search for WinHelp at [msdn](https://learn.microsoft.com/en-ca/search/?terms=WinHelp), [google](https://www.google.com/search?q=WinHelp) or [google groups](https://groups.google.com/groups?q=WinHelp).

#### Return Value

The method raises an exception if an error occurs.


---

<!-- page: win32api__WriteProfileSection_meth.html -->

## win32api.WriteProfileSection

 list = WriteProfileSection(section, data , iniName )

Writes a complete section to an INI file or registry.

#### Parameters

- section : string

 The section in the INI file to be written.

- data : string

 The data to write. Can be None to delete the section. Otherwise, must be string, with each entry terminated with '\\0', followed by another terminating '\\0'

- iniName=None : string

 Name of INI file. If specified, WritePrivateProfileSection will be called.

#### Comments

 This function is obsolete, applications should use the registry instead.

#### Win32 API References

- Search for WriteProfileSection at [msdn](https://learn.microsoft.com/en-ca/search/?terms=WriteProfileSection), [google](https://www.google.com/search?q=WriteProfileSection) or [google groups](https://groups.google.com/groups?q=WriteProfileSection).

- Search for WritePrivateProfileSection at [msdn](https://learn.microsoft.com/en-ca/search/?terms=WritePrivateProfileSection), [google](https://www.google.com/search?q=WritePrivateProfileSection) or [google groups](https://groups.google.com/groups?q=WritePrivateProfileSection).


---

<!-- page: win32api__WriteProfileVal_meth.html -->

## win32api.WriteProfileVal

 WriteProfileVal(section, entry, value, iniName)

Writes a value to a Windows INI file.

#### Parameters

- section : string

 The section in the INI file to write to.

- entry : string

 The entry within the section in the INI file to write to.

- value : int/string

 The value to write.

- iniName=None : string

 The name of the INI file. If None, the system INI file is used.

#### Comments

 This function is obsolete, applications should use the registry instead.

#### Win32 API References

- Search for WritePrivateProfileString at [msdn](https://learn.microsoft.com/en-ca/search/?terms=WritePrivateProfileString), [google](https://www.google.com/search?q=WritePrivateProfileString) or [google groups](https://groups.google.com/groups?q=WritePrivateProfileString).

- Search for WriteProfileString at [msdn](https://learn.microsoft.com/en-ca/search/?terms=WriteProfileString), [google](https://www.google.com/search?q=WriteProfileString) or [google groups](https://groups.google.com/groups?q=WriteProfileString).


---

<!-- page: win32api__keybd_event_meth.html -->

## win32api.keybd_event

 keybd_event(bVk, bScan, dwFlags, dwExtraInfo)

Simulate a keyboard event

#### Parameters

- bVk : BYTE

 Virtual-key code

- bScan : BYTE

 Hardware scan code

- dwFlags=0 : DWORD

 Flags specifying various function options

- dwExtraInfo=0 : DWORD

 Additional data associated with keystroke

#### Win32 API References

- Search for keybd_event at [msdn](https://learn.microsoft.com/en-ca/search/?terms=keybd_event), [google](https://www.google.com/search?q=keybd_event) or [google groups](https://groups.google.com/groups?q=keybd_event).


---

<!-- page: win32api__mouse_event_meth.html -->

## win32api.mouse_event

 mouse_event(dwFlags, dx, dy, dwData, dwExtraInfo)

Simulate a mouse event

#### Parameters

- dwFlags=0 : DWORD

 Flags specifying various function options

- dx : DWORD

 Horizontal position of mouse

- dy : DWORD

 Vertical position of mouse

- dwData : DWORD

 Flag specific parameter

- dwExtraInfo=0 : DWORD

 Additional data associated with mouse event

#### Win32 API References

- Search for mouse_event at [msdn](https://learn.microsoft.com/en-ca/search/?terms=mouse_event), [google](https://www.google.com/search?q=mouse_event) or [google groups](https://groups.google.com/groups?q=mouse_event).
