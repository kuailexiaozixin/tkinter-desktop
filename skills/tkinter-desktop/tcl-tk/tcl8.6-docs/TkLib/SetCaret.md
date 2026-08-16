### NAME

Tk_SetCaretPos — set the display caret location

### SYNOPSIS

**#include <tk.h>**  
int  
**Tk_SetCaretPos**(*tkwin, x, y, height*)  

### ARGUMENTS

[Tk_Window](../TkLib/WindowId.md) **tkwin** (in)     Token for window.

int **x** (in)     Window-relative x coordinate.

int **y** (in)     Window-relative y coordinate.

int **h** (in)     Height of the caret in the window.

### DESCRIPTION

**Tk_SetCaretPos** sets the caret location for the display of the specified
[Tk_Window](../TkLib/WindowId.md) *tkwin*. The caret is the per-display cursor
location used for indicating global focus (e.g. to comply with Microsoft
Accessibility guidelines), as well as for location of the over-the-spot XIM (X
Input Methods) or Windows IME windows.

### KEYWORDS

[caret](../Keywords/C.htm#caret), [cursor](../Keywords/C.htm#cursor)

Copyright © 2002 ActiveState Corporation.
