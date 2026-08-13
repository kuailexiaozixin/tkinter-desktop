
### NAME

lappend — Append list elements onto a variable

### SYNOPSIS

**lappend**
*varName*
?
*value value value ...*
?

### DESCRIPTION

This command treats the variable given by
*varName*
 as a list
and appends each of the
*value*
 arguments to that list as a separate
element, with spaces between elements.
If
*varName*
 does not exist, it is created as a list with elements
given by the
*value*
 arguments.

**Lappend**
 is similar to
**[append](append.md)**
 except that the
*value*
s
are appended as list elements rather than raw text.
This command provides a relatively efficient way to build up
large lists.  For example,
“
**lappend a $b**
”
is much more efficient than
“
**set a [concat $a [list $b]]**
”
when
**$a**
 is long.

### EXAMPLE

Using
**lappend**
 to build up a list of numbers.

```
% set var 1
1
% lappend var 2
1 2
% lappend var 3 4 5
1 2 3 4 5
```

### SEE ALSO

**[list](list.md)**
,
**[lindex](lindex.md)**
,
**[linsert](linsert.md)**
,
**[llength](llength.md)**
,
**[lset](lset.md)**
,
**[lsort](lsort.md)**
,
**[lrange](lrange.md)**

### KEYWORDS

append
,
element
,
list
,
variable
