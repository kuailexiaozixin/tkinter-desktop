# 模块 win32console

> 来源：https://mhammond.github.io/pywin32/win32console.html （及其成员页，已全部内联）

## Module win32console

 Interface to the Windows Console functions for dealing with character-mode applications

#### Methods

- CreateConsoleScreenBuffer

 Creates a new console handle

- GetConsoleDisplayMode

 Returns the current console's display mode

- AttachConsole

 Attaches calling process to console of another process

- AllocConsole

 Creates a new console for the calling process

- FreeConsole

 Detaches process from its console

- GetConsoleProcessList

 Returns pids of all processes attached to current console

- GetConsoleCP

 Returns the input code page for calling process's console

- GetConsoleOutputCP

 Returns the output code page for calling process's console

- SetConsoleCP

 Sets the input code page for calling process's console

- SetConsoleOutputCP

 Sets the output code page for calling process's console

- GetConsoleSelectionInfo

 Returns info on text selection within the current console

- AddConsoleAlias

 Creates a new console alias

- GetConsoleAliases

 Retrieves aliases defined under specified executable

- GetConsoleAliasExes

 Lists all executables that have console aliases defined

- GetConsoleWindow

 Returns a handle to the console's window, or 0 if none exists

- GetNumberOfConsoleFonts

 Returns the number of fonts available to the console

- SetConsoleTitle

 Sets the title of calling process's console

- GetConsoleTitle

 Returns the title of console to which calling process is attached

- GenerateConsoleCtrlEvent

 Sends a control signal to a group of processes attached to a common console

- GetStdHandle

 Returns one of calling process's standard handles


---

# win32console 成员详细文档（共 20 项）


---

<!-- page: win32console__AddConsoleAlias_meth.html -->

## win32console.AddConsoleAlias

 AddConsoleAlias(Source, Target, ExeName)

Creates a new console alias

#### Parameters

- Source : PyUNICODE

 The string to be mapped to the target string

- Target : PyUNICODE

 String to be substituted for Source. If None, alias is removed

- ExeName : PyUNICODE

 Name of executable that will use alias


---

<!-- page: win32console__AllocConsole_meth.html -->

## win32console.AllocConsole

 AllocConsole()

Creates a new console for the calling process

#### Comments

 Calling process must not already be attached to another console


---

<!-- page: win32console__AttachConsole_meth.html -->

## win32console.AttachConsole

 AttachConsole(ProcessId)

Attaches to console of another process

#### Parameters

- ProcessId : int

 Pid of another process, or ATTACH_PARENT_PROCESS

#### Comments

 Calling process must not already be attached to another console


---

<!-- page: win32console__CreateConsoleScreenBuffer_meth.html -->

## win32console.CreateConsoleScreenBuffer

 PyConsoleScreenBuffer = CreateConsoleScreenBuffer(DesiredAccess, ShareMode , SecurityAttributes , Flags )

Creates a new console screen buffer

#### Parameters

- DesiredAccess=GENERIC_READ and GENERIC_WRITE : int

 GENERIC_READ and/or GENERIC_WRITE

- ShareMode=FILE_SHARE_READ and FILE_SHARE_WRITE : int

 FILE_SHARE_READ and/or FILE_SHARE_WRITE

- SecurityAttributes=None : PySECURITY_ATTRIBUTES

 Specifies security descriptor and inheritance for handle

- Flags=CONSOLE_TEXTMODE_BUFFER : int

 CONSOLE_TEXTMODE_BUFFER is currently only valid flag


---

<!-- page: win32console__FreeConsole_meth.html -->

## win32console.FreeConsole

 FreeConsole()

Detaches process from its current console


---

<!-- page: win32console__GenerateConsoleCtrlEvent_meth.html -->

## win32console.GenerateConsoleCtrlEvent

 GenerateConsoleCtrlEvent(CtrlEvent, ProcessGroupId)

Sends a control signal to a group of processes attached to a common console

#### Parameters

- CtrlEvent : int

 Signal to be sent to specified process group - CTRL_C_EVENT or CTRL_BREAK_EVENT

- ProcessGroupId=0 : int

 Pid of a process group, use 0 for calling process


---

<!-- page: win32console__GetConsoleAliasExes_meth.html -->

## win32console.GetConsoleAliasExes

 PyUNICODE = GetConsoleAliasExes()

Lists all executables that have console aliases defined

#### Return Value

Returns a unicode string containing executable names separated by NULLS


---

<!-- page: win32console__GetConsoleAliases_meth.html -->

## win32console.GetConsoleAliases

 PyUNICODE = GetConsoleAliases(ExeName)

Retrieves aliases defined under specified executable

#### Parameters

- ExeName : PyUNICODE

 Name of executable for which to return aliases

#### Return Value

Returns a unicode string containing null-terminated pairs of aliases and their target text of the form "alias1=replacementtext1\\0alias2=replacementtext2\\0"


---

<!-- page: win32console__GetConsoleCP_meth.html -->

## win32console.GetConsoleCP

 int = GetConsoleCP()

Returns the input code page for calling process's console


---

<!-- page: win32console__GetConsoleDisplayMode_meth.html -->

## win32console.GetConsoleDisplayMode

 int = GetConsoleDisplayMode()

Returns the current console's display mode

#### Return Value

CONSOLE_FULLSCREEN,CONSOLE_FULLSCREEN_HARDWARE


---

<!-- page: win32console__GetConsoleOutputCP_meth.html -->

## win32console.GetConsoleOutputCP

 int = GetConsoleOutputCP()

Returns the output code page for calling process's console


---

<!-- page: win32console__GetConsoleProcessList_meth.html -->

## win32console.GetConsoleProcessList

 (int,...) = GetConsoleProcessList()

Returns pids of all processes attached to current console


---

<!-- page: win32console__GetConsoleSelectionInfo_meth.html -->

## win32console.GetConsoleSelectionInfo

 dict = GetConsoleSelectionInfo()

Returns info on text selection within the current console

#### Return Value

Returns a dictionary containing {Flags:int, SelectionAnchor: PyCOORD, Selection:PySMALL_RECT} Flags will contain a combination of CONSOLE_NO_SELECTION,CONSOLE_SELECTION_IN_PROGRESS,CONSOLE_SELECTION_NOT_EMPTY,CONSOLE_MOUSE_SELECTION,CONSOLE_MOUSE_DOWN


---

<!-- page: win32console__GetConsoleTitle_meth.html -->

## win32console.GetConsoleTitle

 PyUNICODE = GetConsoleTitle()

Returns the title of the console window


---

<!-- page: win32console__GetConsoleWindow_meth.html -->

## win32console.GetConsoleWindow

 int = GetConsoleWindow()

Returns a handle to the console's window, or 0 if none exists

#### Return Value

This function may raise NotImplementedError if it does not exist on the platform, or a PyHANDLE object with a value of 0. It will never raise a win32 exception.


---

<!-- page: win32console__GetNumberOfConsoleFonts_meth.html -->

## win32console.GetNumberOfConsoleFonts

 int = GetNumberOfConsoleFonts()

Returns the number of fonts available to the console

#### Comments

 Function is not documented in MSDN and may not be supported starting Windows 10


---

<!-- page: win32console__GetStdHandle_meth.html -->

## win32console.GetStdHandle

 PyConsoleScreenBuffer = GetStdHandle(StdHandle)

Returns one of calling process's standard handles

#### Parameters

- StdHandle : int

 Specifies the handle to return - STD_INPUT_HANDLE, STD_OUTPUT_HANDLE, or STD_ERROR_HANDLE

#### Return Value

Returns a PyConsoleScreenBuffer wrapping the handle, or None if specified handle does not exist


---

<!-- page: win32console__SetConsoleCP_meth.html -->

## win32console.SetConsoleCP

 SetConsoleCP(CodePageId)

Sets the input code page for calling process's console

#### Parameters

- CodePageId : int

 The code page to set


---

<!-- page: win32console__SetConsoleOutputCP_meth.html -->

## win32console.SetConsoleOutputCP

 SetConsoleOutputCP(CodePageID)

Sets the output code page for calling process's console

#### Parameters

- CodePageID : int

 The code page to set


---

<!-- page: win32console__SetConsoleTitle_meth.html -->

## win32console.SetConsoleTitle

 SetConsoleTitle(ConsoleTitle)

Sets the title of the console window

#### Parameters

- ConsoleTitle : PyUNICODE

 New title for the console
