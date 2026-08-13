### NAME

Tk_AddOption — Add an option to the option database

### SYNOPSIS

**#include <tk.h>**  
void  
**Tk_AddOption**(*tkwin, name, value, priority*)  

### ARGUMENTS

[Tk_Window](../TkLib/WindowId.md) **tkwin** (in)     Token for window.

const char ***name** (in)     Multi-element name of option.

const char ***value** (in)     Value of option.

int **priority** (in)     Overall priority level to use for option.

### DESCRIPTION

This procedure is invoked to add an option to the database associated with
*tkwin* 's main window. *Name* contains the option being specified and consists
of names and/or classes separated by asterisks or dots, in the usual X format.
*Value* contains the text string to associate with *name* ; this value will be
returned in calls to **[Tk_GetOption](../TkLib/GetOption.md)**. *Priority*
specifies the priority of the value; when options are queried using
**[Tk_GetOption](../TkLib/GetOption.md)** , the value with the highest
priority is returned. *Priority* must be between 0 and **TK_MAX_PRIO** (100).
Some common priority values are:

**TK_WIDGET_DEFAULT_PRIO** (20)     Used for default values hard-coded into
widgets.

**TK_STARTUP_FILE_PRIO** (40)     Used for options specified in application-
specific startup files.

**TK_USER_DEFAULT_PRIO** (60)     Used for options specified in user-specific
defaults files, such as **.Xdefaults** , resource databases loaded into the X
server, or user-specific startup files.

**TK_INTERACTIVE_PRIO** (80)     Used for options specified interactively after
the application starts running.

### KEYWORDS

[class](../Keywords/C.htm#class), [name](../Keywords/N.htm#name),
[option](../Keywords/O.htm#option), [add](../Keywords/A.htm#add)

Copyright © 1998-2000 by Scriptics Corporation.
