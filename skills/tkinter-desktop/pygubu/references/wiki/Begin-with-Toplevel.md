* Start your application with a Toplevel widget; on the Design screen within the Containers tab, click Toplevel.
* Every time you want to add a new page to your application, ensure that nothing is selected in the Object/Widget Tree, and add another Toplevel widget.
* Tinker does not have a ttk variant of Toplevel; the designer will always give you a tk.Toplevel widget.
* Most designers will always want their Toplevel widgets in the root position of the Object/Widget Tree.
* When you have several Toplevel widgets, use the drop-down on the code generation screen to specify which loads first when your application launches in the code generation screen.
* The initial windows size and its other properties are controlled by the first loaded Toplevel widget; see its General Properties and the Custom section at the bottom.

On the internet, you may find old references to TkApplication; it is deprecated; use Toplevel instead.