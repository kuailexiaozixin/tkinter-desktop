# Image property

Some tk widgets have an **image** property. In pygubu, this property accepts an image file name that will be used when the widget is created.

## Using images in pygubu

To define an image, use the image selector located to the right of the property editor. The image name will be used as the 'key' for the selected image and saved into the *.ui file.

By default, the builder will search for images in the same directory of the specified ui file. Alternatively, you can specify different resource folders using the method **add_resource_path(path)**. Those additional paths will be used to search for an image.

You must call **add_resource_path** before creating any widget that requires your custom image.

In code you can retrieve a reference of the tkinter image using the method **get_image(name)**

The image types you can use will depend on the tk version installed.


### Example 1: Using image property

![image_property_001](https://user-images.githubusercontent.com/8467919/158870159-4b2a61f7-03e3-44b5-b65e-a4f3ff2d1988.png)

Full example code [here](https://github.com/alejandroautalan/pygubu-designer/tree/master/examples/image_property).


```python

    ...

    def __init__(self, master=None):
        # 1: Create a builder
        self.builder = builder = pygubu.Builder()

        # 2: Load an ui file
        builder.add_from_file(PROJECT_UI)

        # 3: Set images path before creating any widget
        builder.add_resource_path(PROJECT_PATH)

        # 4: Create the widget using self.master as parent
        self.mainwindow = builder.get_object("mainwindow", master)
    ...

```
