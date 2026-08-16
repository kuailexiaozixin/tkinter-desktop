
### NAME

linsert — Insert elements into a list

### SYNOPSIS

**linsert**
*list index*
?
*element element ...*
?

### DESCRIPTION

This command produces a new list from
*list*
 by inserting all of the

*element*
 arguments just before the
*index*
'th element of

*list*
.  Each
*element*
 argument will become a separate element of
the new list.  If
*index*
 is less than or equal to zero, then the new
elements are inserted at the beginning of the list, and if
*index*
 is
greater or equal to the length of
*list*
, it is as if it was
**end**
.
As with
**[string index](string.md)**
, the
*index*
 value supports both simple index
arithmetic and end-relative indexing.

Subject to the restrictions that indices must refer to locations inside the list and that the *element*s will always be inserted in order, insertions are done so that when *index* is start-relative, the first *element* will be at that index in the resulting list, and when *index* is end-relative, the last *element* will be at that index in the resulting list.

### EXAMPLE

Putting some values into a list, first indexing from the start and
then indexing from the end, and then chaining them together:

```
set oldList {the fox jumps over the dog}
set midList [linsert $oldList 1 quick]
set newList [linsert $midList end-1 lazy]
# The old lists still exist though...
set newerList [linsert [linsert $oldList end-1 quick] 1 lazy]
```

### SEE ALSO

**[list](list.md)**
,
**[lappend](lappend.md)**
,
**[lindex](lindex.md)**
,
**[llength](llength.md)**
,
**[lsearch](lsearch.md)**
,
**[lset](lset.md)**
,
**[lsort](lsort.md)**
,
**[lrange](lrange.md)**
,
**[lreplace](lreplace.md)**
,
**[string](string.md)**

### KEYWORDS

element
,
insert
,
list
