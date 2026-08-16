# pythonwin/doc/docview.html

> 来源：https://github.com/mhammond/pywin32/blob/main/pythonwin/doc/docview.html
> （该文档在 mhammond.github.io 文档站已 404，仅仓库内存在，此处为全文转录）

## Documents and Views in Pythonwin

### Introduction

This document describes the document/view architecture of Pythonwin. It is assumed you have read the Pythonwin architecture documentation and are somewhat familiar with the standard MFC architecture.

Wherever possible, Pythonwin and the samples have followed the same architecture as MFC. This has advantages and disadvantages. Often the MFC architecture does not seem to fit with small, short GUI utilities, due to the reliance on "document" based applications. On the positive, Pythonwin can leverage off the full MFC functionality. This means minimal code to get full-blown application support.

### Document and View - Control Flow

[This needs lots more work. There where 2 flow-charts, which were semi-useless!]

The creation of the frame and views are typically done via the PyCWnd.LoadFrame method. During this call, the windows are created, and virtual functions pass control back to Python. The LoadFrame flow is shown in the separate diagram.

### Object Oriented Documents

Sam Rushing once asked me "there needs to be a way to create 'object-oriented' documents, by that I mean a document with an object associated with it rather than a string. Currently the only way to open a document forces you to use a string (or None)."

The most obvious path to take would seem to override "OpenDocumentFile" or some such, and pass an object rather than a file name. The document could then load itself from the object, and all would be happy. Unfortunately, the tight integration with MFC means this can not work, and led to Sam's frustration above.

On the other hand, the "OpenDocumentFile" method is provided for integration with a standard MDI interface, and the Windows explorer. Obviously, it is not possible to select "File/Open", and load an object based document.

However, I didn't have an easy answer for him.

#### MFC's OLE Implementation

The closest example to the "right" way to do it seemed to be the MFC OLE implementation. When you have an object embedded in another document, and the user wants to edit the object, MFC must load the object without a simple "file name" parameter. MFC's approach is this:

- A normal blank document is created (via OnNewDocument)
- COLEServerDoc's OLE XPersistStorage::Load() method is called, with an "object" (the OLE storage pointer)
- The Documents OnOpenEmbedding() method is called.

- OnOpenDocument is called, with a NULL file name parameter.
- Serialize is called.

Instead of changing the meaning of the existing functions, MFC adds new definitions for derived classes, such as OnOpenEmbedding

#### Back to our example

The cleanest thing seems to be to duplicate the functionality of "OpenDocumentFile" - such as "OpenObject". You would do this by:

- Check to see if there is already a document representing the document open. If so, switch to it and return.
- Create a new document object.
- Create a frame for the document
- Call OnNewDocument to initialise the document.
- Set the documents title
- Call InitialUpdateFrame for the initial display.

#### "objdoc.py".

In the Pythonwin demos directory, there is a file "objdoc.py".

This module defines a template, which has an "OpenObject" method, and takes any Python object as an argument. If window with the object is already open, it is switched to. If not, a edit window is created, and the objects "repr" is written to the window.

### Standard virtual function specification.

I'm not sure where to stick this!

In general, the C++ virtual function handlers follow the same general logic. If no handler is defined, the base class is called. If a Python handler is defined, the base C++ class is not called. In the latter case, it is up to the Python programmer to ensure the base class is called if necessary. This is normally done by calling the method in the underlying _obj_.
