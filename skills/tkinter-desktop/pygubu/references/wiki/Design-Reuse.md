Suppose we have a custom widget, and we want to incorporate it into pygubu-designer.

Our widget is called *TimeWidget* and lives in the module: **timewidget.py**. This, in turn,
is part of our timer application, and its main module is **timerapp.py**.
All of them are located in our project folder called *custom_widget*.

The directory structure is as follows:

```
custom_widget/
  timewidget.py
  timerapp.py
```

In the first instance, we will make pygubu-designer to recognize our widget
so that it can be used to create interfaces, regardless of the
specific options of the widget.

The code for TimeWidget can be seen [here](https://github.com/alejandroautalan/pygubu-designer/blob/master/examples/custom_widget/timewidget.py).
It is a class that derives from ttk.Frame
and allows you to enter hours, minutes and seconds.
We respect how widgets are created in tkinter
using the methods **configure** and **cget** to define and access
their widget options; this will help not write much code when adding
a widget pygubu-designer.

Next, we create a module that will be responsible for registering our
widget in pygubu and pygubu-designer.
The name of this module must be somehow unique not to collide
with standard widgets and those who come incorporated with pygubu.

The name chosen in this case is **timerappwidgets.py**.

```
custom_widget /
  timewidget.py
  timerapp.py
  timerappwidgets.py
```
It, the module, can be used to register more than one custom widget that we
have in our application.

The module code is as follows:

```python
from pygubu import BuilderObject, register_widget
from timewidget import TimeWidget


class TimeWidgetBuilder(BuilderObject):
    class_ = TimeWidget


register_widget('timerappwidgets.timewidget', TimeWidgetBuilder,
                'TimeWidget', ('ttk', 'Timer App Widgets'))

```

Inside the module, we define the class that will build our widget when
pygubu requires.
First, we import two objects: BuilderObject and register_widget.

**BuilderObject** is the basis of all builders. The widget class allows us to describe our widget's characteristics (If it is a container, whether to accept
children, etc.). In this case, we only define the _class__ attribute, which
indicates to the builder the widget class it has to build.

**register_widget** is a function that, as its name suggests, allows
register our widget on pygubu.
Its definition is as follows:

`` `
def register_widget (classname, builder, label = None, tags = None):
`` `

**classname**: the unique name of our widget. By convention, we use
_buildermodule.widgetname_ to define our widget.
This attribute is saved in the _.ui_ file generated.
This parameter is critical because pygubu uses this to find
the module responsible for registering the builder class.

**builder**: the builder class, in our case TimeWidgetBuilder.

**label**: name displayed in the interface of pygubu-designer.

**tags**: are used to position the widget in the container widgets
of pygubu-designer. In this case, we use `('ttk', 'Timer App Widgets')`, "ttk" to
position in the branch "ttk" and "Timer App Widgets" our sub-branch. If it were a
widget in which we use only tkinter classes, it could be defined as
`('Tk', 'Timer App Widgets')`.

After completing the definition of the module builder, add it to the
preferences of pygubu-designer, in **Edit > Settings > Custom Widgets**.

![Captura de pantalla_2022-03-26_21-56-40](https://user-images.githubusercontent.com/3482471/160262743-b42fff61-8d84-4569-a8b4-08d7491249ee.png)

After this, you must restart pygubu-designer to see the new widget available for creating interfaces.

![Captura de pantalla_2022-03-26_22-02-12](https://user-images.githubusercontent.com/3482471/160262521-f6c500b7-a1be-4fb5-80f7-e8a930aae8f1.png)

## Adding widget custom properties

TODO ... ;)

## Files

All example files are located [here](https://github.com/alejandroautalan/pygubu-designer/blob/master/examples/custom_widget).

# Another Example

## Requirement 1

I want to use the DateEntry widget from [tkcalendar](https:///pypi.org/project/tkcalendar) in pygubu-designer.

### Roadmap

* Identify widget class name: **DateEntry**
* Define your builder class name: **DateEntryBuilder**
* Define your builder module name: **tkcalendarwidgets.py**
* Define unique identifier for widget (common pattern: builder_module_name.widget_name): **tkcalendarwidgets.dateentry**

### Project structure

```
myapp/
    tkcalendarwidgets.py
    main.ui
    myapp.py
```

Where tkcalendarwidgets.py has the definition of the builder classes:

```python
# file: tkcalendarwidgets.py

from tkcalendar import Calendar, DateEntry
from pygubu import BuilderObject, register_widget


class DateEntryBuilder(BuilderObject):
    class_ = DateEntry


register_widget('tkcalendarwidgets.dateentry', DateEntryBuilder,
                'DateEntry', ('ttk', 'My Tkcalendar widgets'))
```
Here I register the builder class with **tkcalendarwidgets.dateentry** where **tkcalendarwidgets** is the python module name and **dateentry** a unique widget name that I chose.
(Remember, if you change the class name of the builder, you will need to manually modify the XML UI file or create a new one)

Once the tkcalendarwidgets module is done: open pygubu-designer go to Edit > Preferences > Custom Widgets click '+' add button, select tkcalendarwidgets.py module.

![preferences1](https://user-images.githubusercontent.com/8467919/158917640-9e7a3713-7cbe-4553-85f5-ba0b1b5ffcb0.png)

Close and restart pygubu-designer; the new widget will be available in the widget toolbar.

![toolbar1](https://user-images.githubusercontent.com/8467919/158917605-81d88837-33aa-4f2d-91e2-95de889d5660.png)

Now edit and create your main UI file.

Files for this section [here](https://github.com/alejandroautalan/pygubu-designer/tree/master/examples/integration_with_tkcalendar/myapp1).


## Requirement 2
The DateEntry widget has some options that I want to change, for example:

    DateEntry(top, width=12, background='darkblue',foreground='white', borderwidth=2, year=2010)

### Option 1 - Quick and dirty: try to use code

In code, you can get a reference to the widget and modify its properties.

```python
# file: myapp.py

# ...

class MyApp:
    def __init__(self):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.mainwindow = builder.get_object('mainwindow')
        builder.connect_callbacks(self)
        
        dateentry = builder.get_object('dateentry_1')
        dateentry.configure(width=12,
                            background='darkblue',
                            foreground='white',
                            borderwidth=2)
    
# ...
```

### Option 2 - The widget uses some standard tk options for configuration

If the widget uses some standard tk options to configure itself, you can define them
in the Builder class. 
Documentation for DateEntry says that it supports the following options.

Standar options: **cursor**, **font**, **borderwidth**, **state**, **foreground**, **background**,
**selectbackground**, **selectforeground**

Specific options: **disabledbackground**, **disabledforeground**

Note: this option name is common to Tk and already defined in pygubu-designer.
So you can add them to the class definition, and pygubu-designer will display them.

Edit the builder class and add the **OPTIONS_STANDARD** and **OPTIONS_SPECIFIC** properties.


```python
# file: tkcalendarwidgets.py

# ...

class DateEntryBuilder(BuilderObject):
    class_ = DateEntry
    
    OPTIONS_STANDARD = ('cursor', 'font', 'borderwidth', 'state',
                        'foreground', 'background', 'selectbackground',
                        'selectforeground')
    OPTIONS_SPECIFIC =  ('disabledbackground', 'disabledforeground')
    properties = OPTIONS_STANDARD + OPTIONS_SPECIFIC

# ...
```

Rerun the designer. Now you can edit the specified properties in the main interface:

![screen1](https://user-images.githubusercontent.com/8467919/158917503-c533b9a3-7c7d-4310-9d39-9e532a8c0ab3.png)

Files for this section [here](https://github.com/alejandroautalan/pygubu-designer/tree/master/examples/integration_with_tkcalendar/myapp2).

### Option 3 - Widget custom options

DateEntry also supports custom options; some of them are year, month, day, headersbackground, headersforeground.
Custom options requires additional configurations, read the next section.

## Requirement 3 - Custom widget options

DateEntry also supports custom options; some of them are year, month, day, headersbackground, headersforeground, date_pattern.

How to edit them? First, you need to identify the type of property.

Pygubu-designer supports the following property editors:

- entry: any text
- alphanumentry: alphanumeric text
- commandentry: command editor
- choice: simple choice selector
- choice_key: choice selector implemented with pygubu combobox widget.
- spinbox: spinbox editor
- text: text area editor
- checkbutton: check button editor
- naturalnumber: entry for natural number input
- integernumber: entry for integer numbers
- realnumber: entry for real number input
- geometryentry: Tk geometry
- colorentry: color editor
- dimensionentry: Tk dimension editor
- twodimensionentry: Tk dimension editor (two dimensions)
- fourdimensionentry: Tk dimension editor (four dimensions)
- fontentry: 
- imageentry: 
- pixelcoordinateentry: 
- relativeentry:
- stickyentry: sticky editor
- tkvarentry: tk variable name editor

So back to our properties. Let us define an editor for them (Note: we are keeping things simple here):

    year: naturalnumber
    month: naturalnumber
    day: naturalnumber
    headersbackground: colorentry
    headersforeground: colorentry
    date_pattern: choice, allowed values: "MM/dd/yy", "MM/dd/yyyy", "dd/MM/yyyy"

Now lets define them in code:

```python
# file: tkcalendarwidgets.py

# ...

class DateEntryBuilder(BuilderObject):
    class_ = DateEntry

    OPTIONS_STANDARD = (
        "cursor",
        "font",
        "borderwidth",
        "state",
        "foreground",
        "background",
        "selectbackground",
        "selectforeground",
    )
    OPTIONS_SPECIFIC = ("disabledbackground", "disabledforeground")
    OPTIONS_CUSTOM = (
        "year",
        "month",
        "day",
        "date_pattern",
        "headersbackground",
        "headersforeground",
    )
    ro_properties = ("year", "month", "day")
    properties = OPTIONS_STANDARD + OPTIONS_SPECIFIC + OPTIONS_CUSTOM
    virtual_events = ("<<DateEntrySelected>>",)
    
    def _process_property_value(self, pname, value):
        if pname in ("year", "month", "day"):
            return int(value)
        return super()._process_property_value(pname, value)

# ...
```
The properties year, month and day are only allowed at construction time, so they are marked as "read only" properties.

```python
    ro_properties = ("year", "month", "day")
```

Also they are required to be **int** type so we need to process them before construction:

```python
    def _process_property_value(self, pname, value):
        if pname in ("year", "month", "day"):
            return int(value)
        return super()._process_property_value(pname, value)
```

With all this done, now we register the custom properties with the function **register_custom_property**:

```python
. . .

# Register custom property
# Params:
# Builder id
# Property name
# Editor name and options. Using a choice here to input only allowed values.
# Tooltip help
register_custom_property(
    _builder_id,
    "date_pattern",
    "choice",
    values=("", "MM/dd/yy", "MM/dd/yyyy", "dd/MM/yyyy"),
    state="readonly",
    help="Date pattern",
)
register_custom_property(
    _builder_id,
    "year",
    "naturalnumber",
)
register_custom_property(
    _builder_id,
    "month",
    "naturalnumber",
)
register_custom_property(
    _builder_id,
    "day",
    "naturalnumber",
)
register_custom_property(
    _builder_id,
    "headersbackground",
    "colorentry",
)
register_custom_property(
    _builder_id,
    "headersforeground",
    "colorentry",
)
```

Final result in designer:

![Captura de pantalla_2022-07-30_20-51-16](https://user-images.githubusercontent.com/3482471/182003909-7464e5ce-ddee-4e01-b5f5-3761299da843.png)


Files for this section [here](https://github.com/alejandroautalan/pygubu-designer/tree/master/examples/integration_with_tkcalendar/myapp3).