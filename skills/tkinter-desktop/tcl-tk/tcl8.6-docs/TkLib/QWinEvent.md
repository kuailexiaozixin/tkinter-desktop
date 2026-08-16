### NAME

Tk_CollapseMotionEvents, Tk_QueueWindowEvent — Add a window event to the Tcl
event queue

### SYNOPSIS

**#include <tk.h>**  
int  
**Tk_CollapseMotionEvents**(*display, collapse*)  
**Tk_QueueWindowEvent**(*eventPtr, position*)  

### ARGUMENTS

Display ***display** (in)     Display for which to control motion event
collapsing.

int **collapse** (in)     Indicates whether motion events should be collapsed
or not.

XEvent ***eventPtr** (in)     An event to add to the event queue. It is
important that all unused fields of the structure be set to zero.

Tcl_QueuePosition **position** (in)     Where to add the new event in the
queue: **TCL_QUEUE_TAIL** , **TCL_QUEUE_HEAD** , or **TCL_QUEUE_MARK**.

### DESCRIPTION

**Tk_QueueWindowEvent** places a window event on Tcl's internal event queue for
eventual servicing. It creates a [Tcl_Event](../TclLib/Notifier.md) structure,
copies the event into that structure, and calls
**[Tcl_QueueEvent](../TclLib/Notifier.md)** to add the event to the queue.
When the event is eventually removed from the queue it is processed just like
all window events.

When multiple motion events are received for the same window in rapid
succession, they are collapsed by default. This behavior can be controlled with
**Tk_CollapseMotionEvents**. **Tk_CollapseMotionEvents** always returns the
previous value for collapse behavior on the *display*.

The *position* argument to **Tk_QueueWindowEvent** has the same significance as
for **[Tcl_QueueEvent](../TclLib/Notifier.md)** ; see the documentation for
**[Tcl_QueueEvent](../TclLib/Notifier.md)** for details.

### KEYWORDS

[callback](../Keywords/C.htm#callback), [clock](../Keywords/C.htm#clock),
[handler](../Keywords/H.htm#handler), [modal timeout](../Keywords/M.htm#modal
timeout), [events](../Keywords/E.htm#events)

Copyright © 1995-1996 Sun Microsystems, Inc.
