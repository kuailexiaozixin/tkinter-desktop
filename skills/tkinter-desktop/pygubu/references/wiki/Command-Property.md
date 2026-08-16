# Command Properties

Some tk widgets have **command** properties. These properties accept a function callback that will be called when the user interacts with the widget.

## Using callbacks in pygubu

To define a callback for a widget simply enter the name of the function (or method) in the command property editor.

In code, you must call the method **connect_callbacks** of the **builder** object, specifying which functions to connect.

You can pass a dictionary of key:value pairs, where the key is the callback name as was specified on the UI definition, and value is the real python function.

Alternatively, you can pass an object with the same method names as defined in the UI file, and the connection will be made automatically.


### Example 1: Using function callbacks

Configure the callback names in the UI definition:

Set 1° button callback name:

![command_001](https://user-images.githubusercontent.com/8467919/158870860-ed6e1811-b24d-4209-9044-22d4d5a28bc5.png)

Set 2° button callback name:

![command_002](https://user-images.githubusercontent.com/8467919/158870873-cf169146-f345-40b8-bf40-cc6293245b78.png)

Set 3° button callback name:

![command_003](https://user-images.githubusercontent.com/8467919/158870886-23ee35d5-e6d9-48bc-bb47-6acd8ab0b0ee.png)


Example dir: [command_properties](https://github.com/alejandroautalan/pygubu-designer/blob/master/examples/command_properties)

File: [command_properties.py](https://github.com/alejandroautalan/pygubu-designer/blob/master/examples/command_properties/command_properties.py)


```python

    ...

def on_button1_click():
    messagebox.showinfo("Message", "You clicked Button 1")


def on_button2_click():
    messagebox.showinfo("Message", "You clicked Button 2")


def on_button3_click():
    messagebox.showinfo("Message", "You clicked Button 3")


class MyApplication:
    def __init__(self, master=None):
            ...

            # Configure callbacks
            callbacks = {
                'on_button1_clicked': on_button1_click,
                'on_button2_clicked': on_button2_click,
                'on_button3_clicked': on_button3_click
            }

            builder.connect_callbacks(callbacks)
    ...

```

### Example 2: Using object methods

Example dir: [command_properties](https://github.com/alejandroautalan/pygubu-designer/blob/master/examples/command_properties)

File: [command_properties2.py](https://github.com/alejandroautalan/pygubu-designer/blob/master/examples/command_properties/command_properties2.py)


```python

    ...

class MyApplication:
    def __init__(self, master=None):
            ...

            # Connect method callbacks
            builder.connect_callbacks(self)

        # define the method callbacks
        def on_button1_clicked(self):
            messagebox.showinfo('Message', 'You clicked Button 1')

        def on_button2_clicked(self):
            messagebox.showinfo('Message', 'You clicked Button 2')

        def on_button3_clicked(self):
            messagebox.showinfo('Message', 'You clicked Button 3')
    ...

```