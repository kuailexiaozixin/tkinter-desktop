# Creating a Menu

Before a menu can become visible, some py code must be added manually into the app.py file e.g.:

```python
self.mainmenu = builder.get_object('Menu_1')      # Menu_1 = std name
self.mainwindow.configure(menu=self.mainmenu)
```


To create a menu, you can use the following widgets: Menu, Menuitem.Command, Menuitem.Checkbutton, Menuitem.Radiobutton, Menuitem.Submenu and Menuitem.Separator.

See the following example:

![menu_01](https://user-images.githubusercontent.com/8467919/158724836-8fc1230f-cb98-4e2c-8e9d-61faf27bec18.png)

Interface file: [menu.ui](https://github.com/alejandroautalan/pygubu-designer/blob/master/examples/toplevel_menu/menu.ui)

## Adding the menu to the main window

```python

    # menu.py
    import tkinter as tk
    from tkinter import messagebox
    import pygubu
  
    class MyApplication:
  
        def __init__(self, master=None):
            #1: Create a builder
            self.builder = builder = pygubu.Builder()
  
            #2: Load an ui file
            builder.add_from_file('menu.ui')
  
            #3: Create the widget using self.master as parent
            self.mainwindow = builder.get_object('mainwindow', master)
  
            # Set main menu
            self.mainmenu = builder.get_object('mainmenu', self.mainwindow)
            self.mainwindow.configure(menu=self.mainmenu)

    ...

    if __name__ == '__main__':
        app = MyApplication()
        app.run()
```

## Reacting to menu clicks

To respond to menu actions, you must set the callback function name on the **command** property of the Menuitem widget.

Remember to call the function **connect_callbacks** on the builder object to connect the callbacks defined.

Additionally, for Menuitems, there is an additional property called **command_id_arg**. If it is set True, the callback function is called with the widget **Id** as an extra argument. No extra argument is added to the call if it is set False.

_Example 1_, configuring callback function with extra argument:

![menu_02](https://user-images.githubusercontent.com/8467919/158724878-a7a5a00c-561f-45f6-bb6d-676512ea8efe.png)

Code:

```python

    ...
    class MyApplication:
        def __init__(self, master=None):
            ...
            # Configure callbacks
            builder.connect_callbacks(self)

        def on_mfile_item_clicked(self, itemid):
            if itemid == 'mfile_open':
                messagebox.showinfo('File', 'You clicked Open menuitem')

            if itemid == 'mfile_quit':
                messagebox.showinfo('File', 'You clicked Quit menuitem. Byby')
                self.quit();
    ...
```

_Example 2_, configuring callback function with no additional arguments:

![menu_03](https://user-images.githubusercontent.com/8467919/158724918-3588c044-165c-4eaf-8cc2-440ea19120f6.png)

Code:

```python

    ...
    class MyApplication:
        def __init__(self, master=None):
            ...
            # Configure callbacks
            builder.connect_callbacks(self)

        def on_about_clicked(self):
                messagebox.showinfo('About', 'You clicked About menuitem')
    ...
```

Full example code: [menu.py](https://github.com/alejandroautalan/pygubu-designer/tree/master/examples/toplevel_menu)
