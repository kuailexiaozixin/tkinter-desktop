### NAME

Itcl_InitStack, Itcl_DeleteStack, Itcl_PushStack, Itcl_PopStack,
Itcl_PeekStack, Itcl_GetStackValue, Itcl_GetStackSize — Manipulate an Itcl
stack object.

### SYNOPSIS

**#include <itcl.h>**  
  
int  
**Itcl_InitStack**(*stack*)  
  
int  
**Itcl_DeleteStack**(*stack*)  
  
int  
**Itcl_PushStack**(*cdata, stack*)  
  
void *  
**Itcl_PopStack**(*stack*)  
  
void *  
**Itcl_PeekStack**(*stack*)  
  
void *  
**Itcl_GetStackValue**(*stack, pos*)  
  
int  
**Itcl_GetStackSize**(*stack*)  

### ARGUMENTS

Itcl_Stack ***stack** (in)     Stack info structure.

int **pos** (in)     position in stack order from the top.

void ***clientData** (in)     Arbitrary one-word value to save in the stack.

### DESCRIPTION

**Itcl_InitStack** initializes a stack structure and **Itcl_DeleteStack**
deletes it. **Itcl_PushStack** pushes the *cdata* value onto the stack.
**Itcl_PopStack** removes and returns the top most *cdata* value.
**Itcl_PeekStack** returns the top most value, but does not remove it.
**Itcl_GetStackValue** gets a value at some index within the stack. Index "0"
is the first value pushed onto the stack. **Itcl_GetStackSize** returns the
count of entries on the stack.

### KEYWORDS

[stack](../Keywords/S.htm#stack)

Copyright © 1993-1998 Lucent Technologies, Inc.
