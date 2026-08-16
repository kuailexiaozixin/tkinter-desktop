### NAME

Tk_NameOfImage — Return name of image.

### SYNOPSIS

**#include <tk.h>**  
const char *  
**Tk_NameOfImage**(*imageMaster*)  

### ARGUMENTS

[Tk_ImageMaster](../TkLib/GetImage.md) **imageMaster** (in)     Token for
image, which was passed to image manager's *createProc* when the image was
created.

### DESCRIPTION

This procedure is invoked by image managers to find out the name of an image.
Given the token for the image, it returns the string name for the image.

*[Tk_ImageModel](../TkLib/GetImage.md)* is synonym for *[Tk_ImageMaster](../TkLib/GetImage.md)*

### KEYWORDS

[image manager](../Keywords/I.htm#image manager), [image
name](../Keywords/I.htm#image name)

Copyright © 1995-1996 Sun Microsystems, Inc.
