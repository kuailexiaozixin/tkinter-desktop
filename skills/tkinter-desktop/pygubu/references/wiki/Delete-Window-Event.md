# How to capture Delete Window Event

To capture the window delete event, you call the ***protocol*** method in the top-level widget of your UI and pass a callback function of the widget.
Finally, you need to call the to ***destroy*** method on the top-level widget inside the callback.


Example when the root widget of your UI is a Frame:

[demo1.py](https://github.com/alejandroautalan/pygubu-designer/blob/master/examples/windowdeleteevent/demo1.py)

[demo1.ui](https://github.com/alejandroautalan/pygubu-designer/blob/master/examples/windowdeleteevent/demo1.ui)


```python

class Application:
    def __init__(self, master):
        self.builder = builder = pygubu.Builder()
        builder.add_from_file('demo1.ui')
        self.mainwindow = builder.get_object('mainwindow', master)
        # Connect Delete event to a toplevel window
        master.protocol("WM_DELETE_WINDOW", self.on_close_window)
        
    def on_close_window(self, event=None):
        print('On close window')
        
        # Call destroy on top-level to finish program
        self.mainwindow.master.destroy()


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    root.mainloop()

```


Example when the root widget of your UI is a Toplevel:

[demo2.py](https://github.com/alejandroautalan/pygubu-designer/blob/master/examples/windowdeleteevent/demo2.py)

[demo2.ui](https://github.com/alejandroautalan/pygubu-designer/blob/master/examples/windowdeleteevent/demo2.ui)

```python

class Application:
    def __init__(self):
        self.builder = builder = pygubu.Builder()
        builder.add_from_file('demo2.ui')
        self.mainwindow = builder.get_object('mainwindow')

        # Connect Delete event to a toplevel window
        self.mainwindow.protocol("WM_DELETE_WINDOW", self.on_close_window)
        
    def on_close_window(self, event=None):
        print('On close window')
        
        # Call destroy on top-level to finish program
        self.mainwindow.destroy()
        
    def run(self):
        self.mainwindow.mainloop()


if __name__ == '__main__':
    app = Application()
    app.run()
```

