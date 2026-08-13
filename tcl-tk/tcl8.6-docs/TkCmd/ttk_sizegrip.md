
### NAME

ttk::sizegrip — Bottom-right corner resize widget

### SYNOPSIS

**ttk::sizegrip**
*pathName*
?
*options*
?

### DESCRIPTION

A
**ttk::sizegrip**
 widget (also known as a
*grow box*
)
allows the user to resize the containing toplevel window
by pressing and dragging the grip.

### STANDARD OPTIONS

**[-class, undefined, undefined](ttk_widget.md#M-class)**
**[-cursor, cursor, Cursor](ttk_widget.md#M-cursor)**
**[-style, style, Style](ttk_widget.md#M-style)**
**[-takefocus, takeFocus, TakeFocus](ttk_widget.md#M-takefocus)**

### WIDGET COMMAND

Sizegrip widgets support the standard

**cget**
,
**configure**
,
**identify**
,
**instate**
, and
**state**

methods.  No other widget methods are used.

### PLATFORM-SPECIFIC NOTES

On macOS, toplevel windows automatically include a built-in
size grip by default.
Adding a
**ttk::sizegrip**
 there is harmless, since
the built-in grip will just mask the widget.

### EXAMPLES

Using pack:

```
pack [ttk::frame $top.statusbar] -side bottom -fill x
pack [ttk::sizegrip $top.statusbar.grip] -side right -anchor se
```

Using grid:

```
grid [ttk::sizegrip $top.statusbar.grip] \
    -row $lastRow -column $lastColumn -sticky se
# ... optional: add vertical scrollbar in $lastColumn,
# ... optional: add horizontal scrollbar in $lastRow
```

### BUGS

If the containing toplevel's position was specified
relative to the right or bottom of the screen
(e.g.,
“
**wm geometry ...**
*w*
**x**
*h*
**-**
*x*
**-**
*y*
”
instead of
“
**wm geometry ...**
*w*
**x**
*h*
**+**
*x*
**+**
*y*
”),
the sizegrip widget will not resize the window.

**ttk::sizegrip** widgets only support “southeast” resizing.

### STYLING OPTIONS

The class name for a
**ttk::sizegrip**
 is
**TSizegrip**
.

**TSizegrip** styling options configurable with **[ttk::style](ttk_style.md)** are:

**-background** *color*

Some options are only available for specific themes.

See the **[ttk::style](ttk_style.md)** manual page for information on how to configure ttk styles.

### SEE ALSO

**[ttk::widget](ttk_widget.md)**

### KEYWORDS

widget
,
sizegrip
,
grow box
