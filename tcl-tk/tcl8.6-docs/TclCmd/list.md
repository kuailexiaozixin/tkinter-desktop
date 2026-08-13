
### NAME

list — Create a list

### SYNOPSIS

**list**
?
*arg arg ...*
?

### DESCRIPTION

This command returns a list comprised of all the
*arg*
s,
or an empty string if no
*arg*
s are specified.
Braces and backslashes get added as necessary, so that the
**[lindex](lindex.md)**
 command
may be used on the result to re-extract the original arguments, and also
so that
**[eval](eval.md)**
 may be used to execute the resulting list, with

*arg1*
 comprising the command's name and the other
*arg*
s comprising
its arguments.
**List**
 produces slightly different results than

**[concat](concat.md)**
:
**[concat](concat.md)**
 removes one level of grouping before forming
the list, while
**list**
 works directly from the original arguments.

### EXAMPLE

The command

```
list a b "c d e  " "  f {g h}"
```

will return

```
a b {c d e  } {  f {g h}}
```

while **[concat](concat.md)** with the same arguments will return

```
a b c d e f {g h}
```

### SEE ALSO

**[lappend](lappend.md)**
,
**[lindex](lindex.md)**
,
**[linsert](linsert.md)**
,
**[llength](llength.md)**
,
**[lrange](lrange.md)**
,
**[lrepeat](lrepeat.md)**
,
**[lreplace](lreplace.md)**
,
**[lsearch](lsearch.md)**
,
**[lset](lset.md)**
,
**[lsort](lsort.md)**

### KEYWORDS

element
,
list
,
quoting
