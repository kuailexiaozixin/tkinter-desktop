# Control variable properties and their usage

Some interactive tkinter widgets have properties named **variable** or **textvarible**. Those properties can contain **control variables**, objects used to control the value behind the widget. 

To define a variable, just put the variable's name in the property editor. Use the combo box to specify the type: StringVar, IntVar, DoubleVar or BooleanVar; StringVar is the default. See the tkinter documentation about how a widget manages each type.

You can link a "tkvariable" to a slider or entry widget and then programmatically access the changing value. These variables will be uninitialized until the user first operates the control.

In code, you can retrieve a reference of the tkinter variable using the builder method **get_variable(name)**

***

### An example with a set of radio buttons.
![controlvariables_001](https://user-images.githubusercontent.com/8467919/158869458-57fbabf2-f837-4d51-968b-526bb940e7ad.png)

![controlvariables_002](https://user-images.githubusercontent.com/8467919/158869487-1f21c2f5-b25e-4ce7-aca9-863d7ce4a94f.png)

![controlvariables_003](https://user-images.githubusercontent.com/8467919/158869499-21f01d7d-baf6-442c-abb0-940e1052668c.png)

![controlvariables_004](https://user-images.githubusercontent.com/8467919/158869515-38225e61-4abc-4443-98d6-b99bba38a6b5.png)

Add the following line to the generated Python code.
  
`print('current value is '  , self.builder.get_variable('radiovar').get())  `

When you pull the slider back and forth with the mouse, it will print different numbers.

Interface file: [controlvariables.ui](../blob/master/examples/control_variables/controlvariables.ui)

Full example code: [controlvariables.py](../blob/master/examples/control_variables/controlvariables.py)