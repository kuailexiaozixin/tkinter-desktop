
### NAME

tkerror — Command invoked to process background errors

### SYNOPSIS

**tkerror**
*message*

### DESCRIPTION

Note: as of Tk 4.1 the
**tkerror**
 command has been renamed to

**[bgerror](../TclCmd/bgerror.md)**
 because the event loop (which is what usually invokes
it) is now part of Tcl.  For backward compatibility
the
**[bgerror](../TclCmd/bgerror.md)**
 provided by the current Tk version still
tries to call
**tkerror**
 if there is one (or an auto loadable one),
so old script defining that error handler should still work, but you
should anyhow modify your scripts to use
**[bgerror](../TclCmd/bgerror.md)**
 instead
of
**tkerror**
 because that support for the old name might vanish
in the near future. If that call fails,
**[bgerror](../TclCmd/bgerror.md)**

posts a dialog showing the error and offering to see the stack trace
to the user. If you want your own error management you should
directly override
**[bgerror](../TclCmd/bgerror.md)**
 instead of
**tkerror**
.
Documentation for
**[bgerror](../TclCmd/bgerror.md)**
 is available as part of Tcl's
documentation.

### KEYWORDS

background error
,
reporting
