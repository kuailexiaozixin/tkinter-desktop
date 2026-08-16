
### NAME

break — Abort looping command

### SYNOPSIS

**break**

### DESCRIPTION

This command is typically invoked inside the body of a looping command
such as
**[for](for.md)**
 or
**[foreach](foreach.md)**
 or
**[while](while.md)**
.
It returns a 3 (
**[TCL_BREAK](catch.md)**
) result code, which causes a break exception
to occur.
The exception causes the current script to be aborted
out to the innermost containing loop command, which then
aborts its execution and returns normally.
Break exceptions are also handled in a few other situations, such
as the
**[catch](catch.md)**
 command, Tk event bindings, and the outermost
scripts of procedure bodies.

### EXAMPLE

Print a line for each of the integers from 0 to 5:

```
for {set x 0} {$x<10} {incr x} {
    if {$x > 5} {
        break
    }
    puts "x is $x"
}
```

### SEE ALSO

**[catch](catch.md)**
,
**[continue](continue.md)**
,
**[for](for.md)**
,
**[foreach](foreach.md)**
,
**[return](return.md)**
,
**[while](while.md)**

### KEYWORDS

abort
,
break
,
loop
