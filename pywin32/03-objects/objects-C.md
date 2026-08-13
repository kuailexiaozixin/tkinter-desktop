# pywin32 对象文档 · 分卷 C

> 共 11 个对象，来源 https://mhammond.github.io/pywin32/<Object>.html


---

<!-- object: CHARFORMAT -->


<!-- page: CHARFORMAT.html -->

---

## CHARFORMAT Object

 Describes a CHARFORMAT tuple

#### Items

- [0] int : mask

 The mask to use. Bits in this mask indicate which of the following parameter are interpreted. Must be a combination the win32con.CFM_* constants.

- [1] int : effects

 The effects to use. Must be a combination the win32con.CFE_* constants.

- [2] int : yHeight

 The y height.

- [3] int : yOffset

 Character offset from the baseline. If this member is positive, the character is a superscript; if it is negative, the character is a subscript.

- [4] int : colorText

 The color to use.

- [5] int : bCharSet

 The charset. See the LOGFONT structure for details.

- [6] int : bPitchAndFamily

 The charset. See the LOGFONT structure for details.

- [7] string : faceName

 The font name.

#### Comments

 Executing d=win32ui.CreateFontDialog(); d.DoModal(); print(d.GetCharFormat()) will print a valid CHARFORMAT tuple.


---

<!-- object: COMMTIMEOUTS -->


<!-- page: COMMTIMEOUTS.html -->

---

## COMMTIMEOUTS Object

 A tuple representing a COMMTIMEOUTS structure.

#### Items

- [0] int : ReadIntervalTimeout

- [1] int : ReadTotalTimeoutMultiplier

- [2] int : ReadTotalTimeoutConstant

- [3] int : WriteTotalTimeoutMultiplier

- [4] int : WriteTotalTimeoutConstant


---

<!-- object: COMPONENT -->


<!-- page: COMPONENT.html -->

---

## COMPONENT Object

 A dictionary containing data to fill a COMPPOS struct

#### Properties

- int ID
 Id of component, ignored when adding a new component

- int ComponentType
 One of shellcon.COMP_TYPE_* values

- bool Checked
 True indicates item is currently displayed

- bool fDirty
 Indicates if unsaved changes exist

- bool NoScroll
 True disables scrolling

- dict Pos
 COMPPOS dictionary determining window size and placement

- PyUNICODE FriendlyName
 String of at most MAX_PATH-1 characters, truncated if longer

- PyUNICODE Source
 String of at most INTERNET_MAX_URL_LENGTH-1 characters

- PyUNICODE SubscribedURL
 String of at most INTERNET_MAX_URL_LENGTH-1 characters

- int CurItemState
 One of shellcon.IS_* flags

- dict Original
 COMPSTATEINFO dictionary

- dict Restored
 COMPSTATEINFO dictionary

- int Size
 Size of structure, ignored on input


---

<!-- object: COMPONENTSOPT -->


<!-- page: COMPONENTSOPT.html -->

---

## COMPONENTSOPT Object

 A dictionary containing data to fill a COMPONENTSOPT struct

#### Properties

- bool EnableComponents
 True if components are enabled

- bool ActiveDesktop
 True if Active Desktop is enabled

- int Size
 Size of structure, ignored on input


---

<!-- object: COMPPOS -->


<!-- page: COMPPOS.html -->

---

## COMPPOS Object

 A dictionary containing data to fill a COMPPOS struct

#### Properties

- int Left

- int Top

- int Width

- int Height

- int Index

- int CanResize

- int CanResizeX

- int CanResizeY

- int PreferredLeftPercent

- int PreferredTopPercent

- int Size
 Size of structure, ignored on input


---

<!-- object: COMPSTATEINFO -->


<!-- page: COMPSTATEINFO.html -->

---

## COMPSTATEINFO Object

 A dictionary containing data to fill a COMPSTATEINFO struct

#### Properties

- int Left
 Specified as screen coordinates

- int Top
 Specified as screen coordinates

- int Width
 Measured in pixels

- int Height
 Measured in pixels

- int dwItemState
 One of IS_NORMAL, IS_FULLSCREEN IS_SPLIT

- int Size
 Size of structure, ignored on input


---

<!-- object: CREATESTRUCT -->


<!-- page: CREATESTRUCT.html -->

---

## CREATESTRUCT Object

 A representation of a Windows CREATESTRUCT structure.

#### Parameters

- createParams : int

- hInstance : int

- hMenu : int

- hwndParent : int

- cy, cx, y, x : (int, int, int, int)

- style : int

- lpszName : int

 A string cast to a long.

- lpszClass : int

 A string cast to a long!?

- dwExStyle : int

#### Comments

 Note that the strings are passed as longs, which are there address in memory. This is due to the internal mechanics of passing this structure around.


---

<!-- object: CopyProgressRoutine -->


<!-- page: CopyProgressRoutine.html -->

---

## CopyProgressRoutine Object

 Python function used as a callback for win32file::CopyFileEx and win32file::MoveFileWithProgress
 Function will receive 9 parameters:
 (TotalFileSize, TotalBytesTransferred, StreamSize, StreamBytesTransferred, StreamNumber, CallbackReason, SourceFile, DestinationFile, Data)
 SourceFile and DestinationFile are PyHANDLEs. Data is the context object passed to the calling function. All others are longs.
 CallbackReason will be one of CALLBACK_CHUNK_FINISHED or CALLBACK_STREAM_SWITCH
 Your implementation of this function must return one of the PROGRESS_* constants.


---

<!-- object: com_error -->


<!-- page: com_error.html -->

---

## com_error Object

 An exception raised when a COM exception occurs.

#### Comments

 This error is defined in the pywintypes module, but is also available via pythoncom.com_error.

 This exception is derived from the standard Python Exception object.

 Instances of these exception can be accessed via indexing or via attribute access. Attribute access is more forwards compatible with Python 3, so is recommended.

 See also error

#### Items

- [0] int : hresult

 The COM hresult

- [1] string : strerror

 The error message

- [2] None/tuple : excepinfo

 An optional EXCEPINFO tuple.

- [3] None/int : argerror

 The index of the argument in error, or (usually) None or -1


---

<!-- object: connection -->


<!-- page: connection.html -->

---

## connection Object

 An object representing an ODBC connection

#### Methods

- setautocommit

 Sets the autocommit mode.

- commit

 Commits a transaction.

- rollback

 Rollsback a transaction.

- cursor

 Creates a cursor object

- close

 Closes the connection.


<!-- page: connection__close_meth.html -->

## connection.close

 close()

Closes the connection.


<!-- page: connection__commit_meth.html -->

## connection.commit

 commit()

Commits a transaction.


<!-- page: connection__cursor_meth.html -->

## connection.cursor

 cursor()

Creates a cursor object


<!-- page: connection__rollback_meth.html -->

## connection.rollback

 rollback()

Rollsback a transaction.


<!-- page: connection__setautocommit_meth.html -->

## connection.setautocommit

 setautocommit(c)

Sets the autocommit mode.

#### Parameters

- c : int

 The boolean autocommit mode.


---

<!-- object: cursor -->


<!-- page: cursor.html -->

---

## cursor Object

 An object representing an ODBC cursor.

#### Methods

- close

 Closes the cursor

- execute

 Execute some SQL

- fetchone

 Fetch one row of data

- fetchmany

 Fetch many rows of data

- fetchall

 Fetch all the rows of data

- setinputsizes

- setoutputsize


<!-- page: cursor__close_meth.html -->

## cursor.close

 close()

Closes the cursor

#### Comments

 This method does nothing!! I presume it should!?!?!


<!-- page: cursor__execute_meth.html -->

## cursor.execute

 int = execute(sql, [var, ...] )

Execute some SQL

#### Parameters

- sql : string

 The SQL to execute

- [var, ...]=[] : sequence

 Input variables.


<!-- page: cursor__fetchall_meth.html -->

## cursor.fetchall

 [data, ...] = fetchall()

Fetch all rows of data


<!-- page: cursor__fetchmany_meth.html -->

## cursor.fetchmany

 [data, ...] = fetchmany()

Fetch many rows of data


<!-- page: cursor__fetchone_meth.html -->

## cursor.fetchone

 data = fetchone()

Fetch one row of data


<!-- page: cursor__setinputsizes_meth.html -->

## cursor.setinputsizes

 setinputsizes()


<!-- page: cursor__setoutputsize_meth.html -->

## cursor.setoutputsize

 setoutputsize()
