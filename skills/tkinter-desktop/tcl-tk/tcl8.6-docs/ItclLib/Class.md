### NAME

Itcl_CreateClass, Itcl_DeleteClass, Itcl_FindClass, Itcl_IsClass,
Itcl_IsClassNamespace — Manipulate classes.

### SYNOPSIS

**#include <itclInt.h>**  
  
int  
**Itcl_CreateClass**(*interp, path, info, rPtr*)  
  
int  
**Itcl_DeleteClass**(*interp, cdefnPtr*)  
  
ItclClass *  
**Itcl_FindClass**(*interp, path, autoload*)  
  
int  
**Itcl_IsClass**(*cmd*)  
  
int  
**Itcl_IsClassNamespace**(*namesp*)  

### ARGUMENTS

[Tcl_Interp](../TclLib/Interp.md) ***interp** (in)     Interpreter to modify.

const char ***path** (in)     Path of the class.

ItclObjectInfo ***info** (in)     TODO.

ItclClass ****rPtr** (in/out)     The address of the pointer to modify.

ItclClass ***cdefnPtr** (in)     Pointer to class info struct.

int **autoload** (in)     Flag value for if the class should be autoloaded

[Tcl_Command](../TclLib/CrtObjCmd.md) **cmd** (in)     Command to check.

[Tcl_Namespace](../TclLib/Namespace.md) ***namesp** (in)     Namespace to
check.

### DESCRIPTION

### KEYWORDS

[class](../Keywords/C.htm#class), [find](../Keywords/F.htm#find)

Copyright © 1993-1998 Lucent Technologies, Inc.
