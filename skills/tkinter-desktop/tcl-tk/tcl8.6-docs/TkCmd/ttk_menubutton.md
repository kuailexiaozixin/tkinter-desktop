
### NAME

ttk::menubutton — Widget that pops down a menu when pressed

### SYNOPSIS

**ttk::menubutton**
*pathName*
?
*options*
?

### DESCRIPTION

A
**ttk::menubutton**
 widget displays a textual label and/or image,
and displays a menu when pressed.

### STANDARD OPTIONS

**[-class, undefined, undefined](ttk_widget.md#M-class)**
**[-compound, compound, Compound](ttk_widget.md#M-compound)**
**[-cursor, cursor, Cursor](ttk_widget.md#M-cursor)**
**[-image, image, Image](ttk_widget.md#M-image)**
**[-state, state, State](ttk_widget.md#M-state)**
**[-style, style, Style](ttk_widget.md#M-style)**
**[-takefocus, takeFocus, TakeFocus](ttk_widget.md#M-takefocus)**
**[-text, text, Text](ttk_widget.md#M-text)**
**[-textvariable, textVariable, Variable](ttk_widget.md#M-textvariable)**
**[-underline, underline, Underline](ttk_widget.md#M-underline)**
**[-width, width, Width](ttk_widget.md#M-width)**

### WIDGET-SPECIFIC OPTIONS

Command-Line Name: **-direction**
Database Name: **direction**
Database Class: **Direction**
Specifies where the menu is to be popped up relative
to the menubutton.
One of: **above**, **below**, **left**, **right**,
or **flush**.  The default is **below**.
**flush** pops the menu up directly over the menubutton.
Command-Line Name: **-menu**
Database Name: **[menu](menu.md)**
Database Class: **[Menu](menu.md)**
Specifies the path name of the menu associated with the menubutton.
To be on the safe side, the menu ought to be a direct child of the
menubutton.

### WIDGET COMMAND

Menubutton widgets support the standard

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

### STANDARD STYLES

**Ttk::menubutton**
 widgets support the
**Toolbutton**
 style in all
standard themes, which is useful for creating widgets for toolbars.

### STYLING OPTIONS

The class name for a
**ttk::menubutton**
 is
**TMenubutton**
.

Dynamic states: **active**, **disabled**, **readonly**.

**TMenubutton** styling options configurable with **[ttk::style](ttk_style.md)** are:

**-arrowsize** *amount* **-background** *color* **-compound** *compound* **-foreground** *color* **-font** *font* **-padding** *padding* **-relief** *relief* **-width** *amount*

Some options are only available for specific themes.

See the **[ttk::style](ttk_style.md)** manual page for information on how to configure ttk styles.

### SEE ALSO

**[ttk::widget](ttk_widget.md)**
,
**[menu](menu.md)**
,
**[menubutton](menubutton.md)**

### KEYWORDS

widget
,
button
,
menu
