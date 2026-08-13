
### NAME

flush — Flush buffered output for a channel

### SYNOPSIS

**flush**
*channelId*

### DESCRIPTION

Flushes any output that has been buffered for
*channelId*
.

*ChannelId* must be an identifier for an open channel such as a Tcl standard channel (**stdout** or **stderr**), the return value from an invocation of **[open](open.md)** or **[socket](socket.md)**, or the result of a channel creation command provided by a Tcl extension. The channel must have been opened for writing.

If the channel is in blocking mode the command does not return until all the buffered output has been flushed to the channel. If the channel is in nonblocking mode, the command may return before all buffered output has been flushed; the remainder will be flushed in the background as fast as the underlying file or device is able to absorb it.

### EXAMPLE

Prompt for the user to type some information in on the console:

```
puts -nonewline "Please type your name: "
flush stdout
gets stdin name
puts "Hello there, $name!"
```

### SEE ALSO

**[file](file.md)**
,
**[open](open.md)**
,
**[socket](socket.md)**
,
**Tcl_StandardChannels**

### KEYWORDS

blocking
,
buffer
,
channel
,
flush
,
nonblocking
,
output
