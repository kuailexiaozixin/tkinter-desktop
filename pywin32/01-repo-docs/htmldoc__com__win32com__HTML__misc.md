# com/win32com/HTML/misc.html

> 来源：https://github.com/mhammond/pywin32/blob/main/com/win32com/HTML/misc.html
> （该文档在 mhammond.github.io 文档站已 404，仅仓库内存在，此处为全文转录）

## Misc stuff I don't know where to put anywhere else

#### Client Side Dispatch

Using win32com.client.Dispatch automatically invokes all the win32com client side "smarts", including automatic usage of generated .py files etc.

If you wish to avoid that, and use truly "dynamic" objects (ie, there is generated .py support available, but you wish to avoid it), you can use win32com.client.dynamic.Dispatch

_print_details_() method
 If win32com.client.dynamic.Dispatch is used, the objects have a _print_details_() method available, which prints all relevant knowledge about an object (for example, all methods and properties). For objects that do not expose runtime type information, _print_details_ may not list anything.
