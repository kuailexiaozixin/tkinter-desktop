### NAME

Tk_RestrictEvents — filter and selectively delay X events

### SYNOPSIS

**#include <tk.h>**  
Tk_RestrictProc *  
**Tk_RestrictEvents**(*proc, arg, prevArgPtr*)  

### ARGUMENTS

Tk_RestrictProc ***proc** (in)     Predicate procedure to call to filter
incoming X events. NULL means do not restrict events at all.

ClientData **arg** (in)     Arbitrary argument to pass to *proc*.

ClientData ***prevArgPtr** (out)     Pointer to place to save argument to
previous restrict procedure.

### DESCRIPTION

This procedure is useful in certain situations where applications are only
prepared to receive certain X events. After **Tk_RestrictEvents** is called,
**[Tcl_DoOneEvent](../TclLib/DoOneEvent.md)** (and hence
**[Tk_MainLoop](../TkLib/MainLoop.md)**) will filter X input events through
*proc*. *Proc* indicates whether a given event is to be processed immediately,
deferred until some later time (e.g. when the event restriction is lifted), or
discarded. *Proc* is a procedure with arguments and result that match the type
**Tk_RestrictProc** :

    
    
    typedef Tk_RestrictAction **Tk_RestrictProc**(
            ClientData *arg* ,
            XEvent **eventPtr*);

The *arg* argument is a copy of the *arg* passed to **Tk_RestrictEvents** ; it
may be used to provide *proc* with information it needs to filter events. The
*eventPtr* points to an event under consideration. *Proc* returns a restrict
action (enumerated type **Tk_RestrictAction**) that indicates what
**[Tcl_DoOneEvent](../TclLib/DoOneEvent.md)** should do with the event. If the
return value is **TK_PROCESS_EVENT** , then the event will be handled
immediately. If the return value is **TK_DEFER_EVENT** , then the event will be
left on the event queue for later processing. If the return value is
**TK_DISCARD_EVENT** , then the event will be removed from the event queue and
discarded without being processed.

**Tk_RestrictEvents** uses its return value and *prevArgPtr* to return
information about the current event restriction procedure (a NULL return value
means there are currently no restrictions). These values may be used to restore
the previous restriction state when there is no longer any need for the current
restriction.

There are very few places where **Tk_RestrictEvents** is needed. In most cases,
the best way to restrict events is by changing the bindings with the
**[bind](../TkCmd/bind.md)** Tcl command or by calling
**[Tk_CreateEventHandler](../TkLib/EventHndlr.md)** and
**[Tk_DeleteEventHandler](../TkLib/EventHndlr.md)** from C. The main place
where **Tk_RestrictEvents** must be used is when performing synchronous actions
(for example, if you need to wait for a particular event to occur on a
particular window but you do not want to invoke any handlers for any other
events). The “obvious” solution in these situations is to call **XNextEvent**
or **XWindowEvent** , but these procedures cannot be used because Tk keeps its
own event queue that is separate from the X event queue. Instead, call
**Tk_RestrictEvents** to set up a filter, then call
**[Tcl_DoOneEvent](../TclLib/DoOneEvent.md)** to retrieve the desired
event(s).

### KEYWORDS

[delay](../Keywords/D.htm#delay), [event](../Keywords/E.htm#event),
[filter](../Keywords/F.htm#filter),
[restriction](../Keywords/R.htm#restriction)

Copyright © 1990 The Regents of the University of California.  
Copyright © 1994-1996 Sun Microsystems, Inc.
