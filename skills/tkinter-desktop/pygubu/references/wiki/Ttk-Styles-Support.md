# Overview

Pygubu designer now supports to use custom ttk styles defined by the user
(Since version 0.23). This is an initial attempt to support ttk styles.

The process to define your custom styles in pygubu-designers is as follows.

## Create a style definition file

This is a python file where you will write your styles.

To create a new file:
- Navigate to Edit > Preferences.
- Click on Tkk Styles tab, then click 'Create New'
- Enter the filename to save your styles.
- Save and close the preferences dialog window.

![Captura de pantalla_2022-04-09_16-33-01-pygubu005](https://user-images.githubusercontent.com/3482471/162589224-c610de72-40bb-4697-83dc-fa981b9ff6d8.png)

## The style definition file

Open the created file with your favorite editor. This is a regular python file, so use python syntax.

It will contain the following:
- Description of how to use the file.
- An example ttk style definition.

```python
# --------------------
# This file is used for defining Ttk styles.
# Use the 'style' object to define styles.

# Pygubu Designer will need to know which style definition file
# you wish to use in your project.

# To specify a style definition file in Pygubu Designer:
# Go to: Edit -> Preferences -> Ttk Styles -> Browse (button)

# In Pygubu Designer:
# Assuming that you have specified a style definition file,
# - Use the 'style' combobox drop-down menu in Pygubu Designer
#   to select a style that you have defined.
# - Changes made to the chosen style definition file will be
#   automatically reflected in Pygubu Designer.
# --------------------

# Example code:
style.configure('MySpecialButton.TButton',
                font=('helvetica', 12, 'bold'),
                background='green', foreground='white')
```

As you see in the example, you must use the **style** object to create ttk style definitions.
Pygubu Designer will monitor this file and load the changes automatically.

![Captura de pantalla_2022-04-09_16-30-26-pygubu003](https://user-images.githubusercontent.com/3482471/162589252-cdca9212-0518-4962-a9bf-1a86b289515e.png)

## Style naming

It is recommended that you end your style name with the ttk style class associated to the widget.
For example, to create a style for blue Labels:

``` python
# the ttk style class for Label is TLabel:
style.configure('MyBlueLabels.TLabel', foreground='blue')
```

In design time, you will have the style available for select in labels using the **style** property.

![Captura de pantalla_2022-04-09_16-31-43-pygubu004](https://user-images.githubusercontent.com/3482471/162589266-27966ba3-4a73-407e-8829-c551d965812e.png)

## Using the styles in the generated code

To include the style definitions in your generated code, make sure you have checked the option **Use ttk style definitions file**.

This will include the code from definitions file in a method called **setup_ttk_styles** that is called from the **\_\_init\_\_** method of the application class.

![Captura de pantalla_2022-04-09_17-01-11](https://user-images.githubusercontent.com/3482471/162590023-42589f9a-a053-4da8-b630-ab24fbe71a31.png)

