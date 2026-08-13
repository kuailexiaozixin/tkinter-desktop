### NAME

TCL_MEM_DEBUG — Compile-time flag to enable Tcl memory debugging

### DESCRIPTION

When Tcl is compiled with **TCL_MEM_DEBUG** defined, a powerful set of memory
debugging aids is included in the compiled binary. This includes C and Tcl
functions which can aid with debugging memory leaks, memory allocation
overruns, and other memory related errors.

### ENABLING MEMORY DEBUGGING

To enable memory debugging, Tcl should be recompiled from scratch with
**TCL_MEM_DEBUG** defined (e.g. by passing the *\--enable-symbols=mem* flag to
the *configure* script when building). This will also compile in a non-stub
version of **[Tcl_InitMemory](../TclLib/DumpActiveMemory.md)** to add the
**[memory](../TclCmd/memory.md)** command to Tcl.

**TCL_MEM_DEBUG** must be either left defined for all modules or undefined for
all modules that are going to be linked together. If they are not, link errors
will occur, with either **Tcl_DbCkfree** and **Tcl_DbCkalloc** or
**[Tcl_Alloc](../TclLib/Alloc.md)** and **[Tcl_Free](../TclLib/Alloc.md)**
being undefined.

Once memory debugging support has been compiled into Tcl, the C functions
**[Tcl_ValidateAllMemory](../TclLib/DumpActiveMemory.md)** , and
**[Tcl_DumpActiveMemory](../TclLib/DumpActiveMemory.md)** , and the Tcl
**[memory](../TclCmd/memory.md)** command can be used to validate and examine
memory usage.

### GUARD ZONES

When memory debugging is enabled, whenever a call to
**[ckalloc](../TclLib/Alloc.md)** is made, slightly more memory than requested
is allocated so the memory debugging code can keep track of the allocated
memory, and eight-byte “guard zones” are placed in front of and behind the
space that will be returned to the caller. (The sizes of the guard zones are
defined by the C #define **LOW_GUARD_SIZE** and #define **HIGH_GUARD_SIZE** in
the file *generic/tclCkalloc.c* — it can be extended if you suspect large
overwrite problems, at some cost in performance.) A known pattern is written
into the guard zones and, on a call to **[ckfree](../TclLib/Alloc.md)** , the
guard zones of the space being freed are checked to see if either zone has been
modified in any way. If one has been, the guard bytes and their new contents
are identified, and a “low guard failed” or “high guard failed” message is
issued. The “guard failed” message includes the address of the memory packet
and the file name and line number of the code that called
**[ckfree](../TclLib/Alloc.md)**. This allows you to detect the common sorts
of one-off problems, where not enough space was allocated to contain the data
written, for example.

### DEBUGGING DIFFICULT MEMORY CORRUPTION PROBLEMS

Normally, Tcl compiled with memory debugging enabled will make it easy to
isolate a corruption problem. Turning on memory validation with the memory
command can help isolate difficult problems. If you suspect (or know) that
corruption is occurring before the Tcl interpreter comes up far enough for you
to issue commands, you can set **MEM_VALIDATE** define, recompile tclCkalloc.c
and rebuild Tcl. This will enable memory validation from the first call to
**[ckalloc](../TclLib/Alloc.md)** , again, at a large performance impact.

If you are desperate and validating memory on every call to
**[ckalloc](../TclLib/Alloc.md)** and **[ckfree](../TclLib/Alloc.md)** is not
enough, you can explicitly call
**[Tcl_ValidateAllMemory](../TclLib/DumpActiveMemory.md)** directly at any
point. It takes a *char ** and an *int* which are normally the filename and
line number of the caller, but they can actually be anything you want. Remember
to remove the calls after you find the problem.

### SEE ALSO

**[ckalloc](../TclLib/Alloc.md)** , **[memory](../TclCmd/memory.md)** ,
**[Tcl_ValidateAllMemory](../TclLib/DumpActiveMemory.md)** ,
**[Tcl_DumpActiveMemory](../TclLib/DumpActiveMemory.md)**

### KEYWORDS

[memory](../Keywords/M.htm#memory), [debug](../Keywords/D.htm#debug)

Copyright © 1992-1999 Karl Lehenbauer & Mark Diekhans.  
Copyright © 2000 Scriptics Corporation.
