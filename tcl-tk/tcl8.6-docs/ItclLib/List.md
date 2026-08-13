### NAME

Itcl_InitList, Itcl_DeleteList, Itcl_CreateListElem, Itcl_DeleteListElem,
Itcl_InsertList, Itcl_InsertListElem, Itcl_AppendList, Itcl_AppendListElem,
Itcl_SetListValue — Manipulate an Itcl list object.

### SYNOPSIS

**#include <itcl.h>**  
  
void  
**Itcl_InitList**(*list*)  
  
void  
**Itcl_DeleteList**(*list*)  
  
Itcl_ListElem *  
**Itcl_CreateListElem**(*list*)  
  
Itcl_ListElem *  
**Itcl_DeleteListElem**(*elem*)  
  
Itcl_ListElem *  
**Itcl_InsertList**(*list, clientData*)  
  
Itcl_ListElem *  
**Itcl_InsertListElem**(*elem, clientData*)  
  
Itcl_ListElem *  
**Itcl_AppendList**(*list, clientData*)  
  
Itcl_ListElem *  
**Itcl_AppendListElem**(*elem, clientData*)  
  
void  
**Itcl_SetListValue**(*elem, clientData*)  

### ARGUMENTS

Itcl_List ***list** (in)     List info structure.

Itcl_ListElem ***elem** (in)     List element info structure.

void ***clientData** (in)     Arbitrary one-word value to save in the list.

### DESCRIPTION

### KEYWORDS

[list](../Keywords/L.htm#list)

Copyright © 1993-1998 Lucent Technologies, Inc.
