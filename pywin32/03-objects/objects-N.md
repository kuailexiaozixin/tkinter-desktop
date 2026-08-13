# pywin32 对象文档 · 分卷 N

> 共 3 个对象，来源 https://mhammond.github.io/pywin32/<Object>.html


---

<!-- object: NCB -->


<!-- page: NCB.html -->

---

## NCB Object

 A Python object that encapsulates a Win32 NCB structure.

#### Properties

- int Command

- int Retcode

- int Lsn

- int Num

- int Bufflen
 read-only

- string Callname
 - The strings need to be space padded to 16 chars exactly

- string Name
 - The strings need to be space padded to 16 chars exactly

- string Rto
 - The strings need to be space padded to 16 chars exactly

- string Sto
 - The strings need to be space padded to 16 chars exactly

- int Lana_num

- int Cmd_cplt

- int Event

- int Post


---

<!-- object: NT_CONSOLE_PROPS -->


<!-- page: NT_CONSOLE_PROPS.html -->

---

## NT_CONSOLE_PROPS Object

 Dictionary containing information for a NT_CONSOLE_PROPS struct

#### Properties

- int Signature
 The type of data block, one of shellcon.*_SIG values

- int FillAttribute
 Character attributes for fill operations

- int PopupFillAttribute
 Fill attributes for popups

- (int,int) ScreenBufferSize
 Size of console screen buffer, in character cells

- (int,int) WindowSize
 Size of console window in character cells

- (int,int) WindowOrigin
 Window position, in screen coordinates

- int nFont
 Number of font to be displayed. See win32console::GetNumberOfConsoleFonts

- int InputBufferSize
 Size of console's input buffer

- (int,int) FontSize
 Size of font

- int FontFamily
 Font family

- int FontWeight
 Controls thickness of displayed font

- str FaceName
 Name of font face, 31 characters at most

- int CursorSize
 Relative size of cursor, expressed as percent of character size

- bool FullScreen
 Causes console to run in full screen mode

- bool QuickEdit

- bool InsertMode

- bool AutoPosition
 Lets system determine window placement

- int HistoryBufferSize
 Size of command line history buffer

- int NumberOfHistoryBuffers

- bool HistoryNoDup

- tuple ColorTable
 Tuple of 16 ints containing console's color attributes

- int Size
 Size of structure, ignored on input


---

<!-- object: NT_FE_CONSOLE_PROPS -->


<!-- page: NT_FE_CONSOLE_PROPS.html -->

---

## NT_FE_CONSOLE_PROPS Object

 Dictionary containing information for a NT_FE_CONSOLE_PROPS struct

#### Properties

- int Signature
 The type of data block, one of shellcon.*_SIG values

- int CodePage
 The codepage to be used for console text

- int Size
 Size of structure, ignored on input
