
### NAME

lreverse — Reverse the order of a list

### SYNOPSIS

**lreverse**
*list*

### DESCRIPTION

The
**lreverse**
 command returns a list that has the same elements as its
input list,
*list*
, except with the elements in the reverse order.

### EXAMPLES

```
lreverse {a a b c}
      → c b a a
lreverse {a b {c d} e f}
      → f e {c d} b a
```

### SEE ALSO

**[list](list.md)**
,
**[lsearch](lsearch.md)**
,
**[lsort](lsort.md)**

### KEYWORDS

element
,
list
,
reverse
