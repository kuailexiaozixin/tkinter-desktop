
### NAME

tell — Return current access position for an open channel

### SYNOPSIS

**tell**
*channelId*

### DESCRIPTION

Returns an integer string giving the current access position in

*channelId*
.  This value returned is a byte offset that can be passed to

**[seek](seek.md)**
 in order to set the channel to a particular position.  Note
that this value is in terms of bytes, not characters like
**[read](read.md)**
.
The value returned is -1 for channels that do not support
seeking.

*ChannelId* must be an identifier for an open channel such as a Tcl standard channel (**stdin**, **stdout**, or **stderr**), the return value from an invocation of **[open](open.md)** or **[socket](socket.md)**, or the result of a channel creation command provided by a Tcl extension.

### EXAMPLE

Read a line from a file channel only if it starts with
**foobar**
:

```
# Save the offset in case we need to undo the read...
set offset [tell $chan]
if {[read $chan 6] eq "foobar"} {
    gets $chan line
} else {
    set line {}
    # Undo the read...
    seek $chan $offset
}
```

### SEE ALSO

**[file](file.md)**
,
**[open](open.md)**
,
**[close](close.md)**
,
**[gets](gets.md)**
,
**[seek](seek.md)**
,
**Tcl_StandardChannels**

### KEYWORDS

access position
,
channel
,
seeking
