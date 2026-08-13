# Overview

Once you save your UI file, the project settings dialog becomes available. This is because it is necessary to calculate the paths relative to the directory where the *.ui file is stored.

## 1 - General

This section is used to document your project.

**Name**: This is the name of your project

**Description**: Put here your notes or design ideas.

![project-settings-1-general](images/project-settings-1-general.png)

## 2 - Code

In this section you can specify wich type of code generation you will use for the project.

![project-settings-2-code](images/project-settings-2-code.png)

**Template**: The code generation template

Main widget: the target widget.

**Module Namespace**: is a namespace string specifying where inside your project python namespace the code generated module will live. I you have a simple plain script, then this can be empty. If you have a more complex project, this can be for example: "myproject.dialogs" or "myproject.widgets" etc.

**Module Name**: is the name of the python module that will be generated.

**Class Name**: The name of the generated class, for example: HelloWorldApp

**Outupt direcory**: path in where the module files will be stored.

**Builder Namespace**: This is enabled for Custom Widget templates. The builder namespace is a python like namespace string but used to uniquely identify the builder class inside the *.ui file.

**Builder directory**: This is enabled for Custom Widget templates. Path in where to store builder modules.

Checkbutton Options:

- ***Regenerate code when saving the project***
- ***Add i18n support***. This will mark translatable generated strings to be identified for translation using gettext or another tool.
- ***All IDs as class attributes***: When unchecked, only "named" widgets are setup as attributes of the class. When active, all widgets will be setup as attributes.
- ***Import tk variables***: setup all defined tk variables to be accesible as instance attributes.
- ***Use ttk style definitions file***: atomatically import and setup the style file if defined.
- ***Add window centering code***: utility to add additional function to center the window.

## 3 - Styles

Here you can create or setup an style definition file.

A style definition file is a python module with a specific function inside, used to define styles for your application.

When a style definition file is setup, you can edit your file with your preferred editor and the style changes will be shown in the Preview Panel.

To generate a new styles module, click on buton with the plus sign, select location, name and you will have a file like the following:

```python
"""
= This file is used for defining Ttk styles.

All style definitions should live in the function named:

   def setup_ttk_styles()

Use an instance of the ttk.Style class to define styles.

As this is a python module, now you can import any other
module that you need.


== In Pygubu Designer

Pygubu Designer will need to know which style definition file
you wish to use in your project.

To specify a style definition file in Pygubu Designer:
Go to: Project -> Settings -> Styles -> Browse (button)

Assuming that you have specified a style definition file,
- Use the 'style' combobox drop-down menu in Pygubu Designer
  to select a style that you have defined.
- Changes made to the chosen style definition file will be
  automatically reflected in Pygubu Designer.


The code below shows the minimal example definition file.

"""

import tkinter as tk
import tkinter.ttk as ttk


def setup_ttk_styles(master=None):
    my_font = ("helvetica", 12, "bold")

    style = ttk.Style(master)

    style.configure("primary.TButton",
                    font=my_font,
                    background="#4582EC",
                    foreground="white")
```

![project-settings-3-styles](images/project-settings-3-styles.png)

## 4 - Custom widgets

In this section you can specify wich custom widget builders will be available for this project.

![project-settings-4-custom-widgets](images/project-settings-4-custom-widgets.png)