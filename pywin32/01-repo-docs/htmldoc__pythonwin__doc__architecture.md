# pythonwin/doc/architecture.html

> 来源：https://github.com/mhammond/pywin32/blob/main/pythonwin/doc/architecture.html
> （该文档在 mhammond.github.io 文档站已 404，仅仓库内存在，此处为全文转录）

## Pythonwin's architecture.

### Introduction

This document describes the general architecture of Pythonwin. It describes the general design and interface to MFC.

After reading this, you should read the document and view architecture documentation.

### Objects, types, etc.

For each MFC object created, there are usually 3 "objects" floating around. Although this may initially seem confusing, it does provide significant flexibility.

In general this complexity is hidden from view. The programmer usually only ever deals with a single object, and this object manages all others. However, an understanding if the implementation will assist in advanced programming techniques.

There is a quick example which shows all this in action.

#### C++ objects

For every window, toolbar, document etc. that exists in Pythonwin, there is a C++ object. In some cases this object may be a standard MFC object, as found in the MFC DLL's. In other cases, the C++ object will be derived from a standard MFC object, and can be found in win32ui.pyd.

Often, these C++ objects will not be aware that there is Python support behind them.

#### win32ui types.

The win32ui module provides a large number of types, each one usually associated with an MFC C++ object.. The naming conventions for these objects is of the form "Py{MFC_Name}" - eg, PyCDocument provides the functionality of an MFC CDocument, PyCDialog for a CDialog.

There is a form of inheritance used for these objects. Each object provides methods from its derived class. A PyCDialog is derived from a PyCWnd, and therefore has all PyCWnd methods available. However, this is as far as the inheritance extends, as Python types are more restrictive than Python classes.

Each method that a win32ui type provides is generally just code for extracting Python arguments and making the call to the associated C++ object.

These objects and methods are defined in Pythonwin.hlp (available from the Pythonwin help menu.)

#### "Object" base class

In object.py, there is a base class "Object". This provides 2 key functions.

- Its constructor (__init__ method) registers the class with a win32ui type object (see below). This allows all virtual methods (see below) to be handled by a class method.
- It allows itself to look exactly like the underlying win32ui type. It does this by storing the win32ui object in self._obj_, and providing a __getattr__ method. See the standard Python documentation for information on __getattr__ in a Python class.

The end result of this is that a class derived from "Object" looks just like a win32ui object, and can be used as such. In fact, there is rarely a reason to use the underlying object directly.

#### Python Classes

If you like you can skip this, and jump straight to the example below. It makes more sense in action!

Pythonwin provides support for many "virtual" functions. A "virtual" function is defined as a virtual C++ MFC function which has deferred its implementation to a Python object. To explain, I will use the example of a document.

In Python, it is possible to create a PyCDialog object by using win32ui.CreateDialog(). This will create both a PyCDialog object, and a C++ CDialog object. For dialogs to be useful to a programmer, it must be possible to define a method to be called when the dialog initialises (i.e., when the C++ OnInitDialog virtual method is called). Normally, a programmer would initialise the values of controls etc. at this time. To support this, the C++ OnInitDialog implementation calls Python to handle the call. In this example, OnInitDialog is a "virtual" function.

Each win32ui type supports being "attached" to a Python class instance. When a virtual function is called, the Python class instance associated with the object is checked to see if it has a method with the same name. If so, the method is called.

More details on this can be found in the document and view architecture documentation.

#### Example of this in action

```
>>> import win32ui # import the base win32ui module.
>>> import dialog # import dialog.py
>>> d=dialog.Dialog(win32ui.IDD_SIMPLE_INPUT)
>>> d
<Dialog instance at 886c78>
```

This creates an instance of class Dialog, defined in dialog.py. Dialog is derived from Object (via Wnd). To see the underlying win32ui type:

```
>>> d._obj_
object 'PyCDialog' - assoc is 002F3278, vf=True, ch=0, mh=2, kh=0
>>>
```

This output shows the C++ CDialog object is at address`0x002F3278`, that there is a virtual function handler (i.e., the class instance "d"), that 2 messages have hooks, and no command or keyboard handlers are installed.

Even though the DoModal() method is implemented in the underlying win32ui type, the class object can be used just like the win32ui object. Thus:

```
>>> d.DoModal()
1
>>>
```

To see virtual functions in action

```
```
>>> class MyDialog(dialog.Dialog):
... def OnInitDialog(self, msg):
... self.GetDlgItem(win32ui.IDC_PROMPT1).SetWindowText("Hello")
... return 1
...
>>> d=MyDialog(win32ui.IDD_SIMPLE_INPUT)
>>> d.DoModal()
1
```


```

Note the prompt on the dialog box is now "Hello".
