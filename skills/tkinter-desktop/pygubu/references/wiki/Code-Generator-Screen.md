# Overview
A code generator interface example:
![code-generator-screen](https://user-images.githubusercontent.com/3482471/162582837-09f6920c-e022-43eb-b5b4-48e9fc2131fa.png)
*Xubuntu 20.04 screen-shot of pygubu-designer v0.25*

## Code
Clicking this tab opens this screen.

## Template
These control the template used to generate boilerplate Python code generated.

### Application
Select to generate **longer** code for your standalone application.

Pros: 
* Where you can and need to add Python code is very obvious.

### Code Script
Select to generate **longer** code for your standalone application.

Pros, 
* Your app will run a tiny bit faster.
* No dependency on the pygubu runtime and a *.ui design file.

### Custom Widget
It allows you to create compound widgets and will make the required classes to incorporate the widget in the designer palette. **Development is incomplete;** adding your custom widgets to the designer palette is currently a [manual process](https://github.com/alejandroautalan/pygubu-designer/wiki/Design-Reuse).

## Options
### Main widget
If you have several top-level widgets, use this drop-down to select which first loads when your application runs.

### Class Name
Control the class name that contains your UI code. The initial default has your project name.

### Import Tk Variables
When using the "Application" option to generate code, you can check to include the tk variables. It makes their existence more evident to someone writing Python code.

### Use ttk style definitions file
**Documentation is needed here.**

## Generate
Push Generate to produce your Python code. If you design or change any option described on this wiki page, you must push Generate again. 

Your Python code appears in the preview pane. You can copy the code to the Clipboard or Save it to a file.

## Messages
Messages inform you of warnings or errors.
If there are any, the count will appear.
The 'Messages' label functions as a toggle; click it to open the message pane.