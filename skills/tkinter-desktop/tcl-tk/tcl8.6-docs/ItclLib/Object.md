### NAME

Itcl_CreateObject, Itcl_DeleteObject, Itcl_FindObject, Itcl_IsObject,
Itcl_IsObjectIsa — Manipulate an class instance.

### SYNOPSIS

**#include <itclInt.h>**  
  
void  
**[Itcl_PreserveData](../ItclLib/Preserve.md)**(*cdata*)  
  
void  
**[Itcl_ReleaseData](../ItclLib/Preserve.md)**(*cdata*)  
  
void  
**[Itcl_EventuallyFree](../ItclLib/Preserve.md)**(*cdata, fproc*)  

### ARGUMENTS

Tcl_FreeProc ***fproc** (in)     Address of function to call when the block is
to be freed.

void ***clientData** (in)     Arbitrary one-word value.

### DESCRIPTION

### KEYWORDS

[free](../Keywords/F.htm#free), [memory](../Keywords/M.htm#memory)

Copyright © 1993-1998 Lucent Technologies, Inc.
