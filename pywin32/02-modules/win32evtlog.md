# 模块 win32evtlog

> 来源：https://mhammond.github.io/pywin32/win32evtlog.html （及其成员页，已全部内联）

## Module win32evtlog

 A module, encapsulating the Windows Win32 event log API.

#### Methods

- ReadEventLog

 Reads some event log records.

- ClearEventLog

 Clears the event log

- BackupEventLog

 Backs up the event log

- CloseEventLog

 Closes the eventlog

- DeregisterEventSource

 Deregisters an Event Source

- NotifyChangeEventLog

 Lets an application receive notification when an event is written to the event log file specified by the hEventLog parameter. When the event is written to the event log file, the function causes the event object specified by the hEvent parameter to become signaled.

- GetNumberOfEventLogRecords

 Returns the number of event log records.

- GetOldestEventLogRecord

 Returns the number of event log records.

- OpenEventLog

 Opens an event log.

- RegisterEventSource

 Registers an Event Source

- OpenBackupEventLog

 Opens a previously saved event log.

- ReportEvent

 Reports an event

- EvtOpenChannelEnum

 Begins an enumeration of event channels

- EvtFormatMessage

 Formats a message string.

- EvtNextChannelPath

 Retrieves a channel path from an enumeration

- EvtOpenLog

 Opens an event log or exported log archive

- EvtClearLog

 Clears an event log and optionally exports events to an archive

- EvtExportLog

 Exports events from a channel or log file

- EvtArchiveExportedLog

 Localizes an exported event log file

- EvtGetExtendedStatus

 Returns additional error info from last Evt* call

- EvtQuery

 Opens a query over a log channel or exported log file

- EvtNext

 Returns events from a query

- EvtSeek

 Changes the current position in a result set

- EvtCreateRenderContext

 Creates a render context

- EvtRender

 Formats an event into XML text or a Python Dict of key/values

- EvtSubscribe

 Requests notification for events

- EvtCreateBookmark

 Creates a bookmark

- EvtUpdateBookmark

 Repositions a bookmark to an event

- EvtGetChannelConfigProperty

 Retreives channel configuration information

- EvtOpenChannelConfig

 Opens channel configuration

- EvtOpenSession

 Creates a session used to access the Event Log on another machine

- EvtOpenPublisherEnum

 Begins an enumeration of event publishers

- EvtNextPublisherId

 Returns the next publisher from an enumeration

- EvtOpenPublisherMetadata

 Opens a publisher to retrieve properties using win32evtlog::EvtGetPublisherMetadataProperty

- EvtGetPublisherMetadataProperty

 Retrieves a property from an event publisher

- EvtOpenEventMetadataEnum

 Enumerates the events that a publisher provides

- EvtNextEventMetadata

 Retrieves the next item from an event metadata enumeration

- EvtGetEventMetadataProperty

 Retrieves a property from an event publisher

- EvtGetLogInfo

 Retrieves log file or channel information

- EvtGetEventInfo

 Retrieves information about the source of an event

- EvtGetObjectArraySize

 Returns the size of an array of event objects

- EvtGetObjectArrayProperty

 Retrieves an item from an object array


---

# win32evtlog 成员详细文档（共 42 项）


---

<!-- page: win32evtlog__BackupEventLog_meth.html -->

## win32evtlog.BackupEventLog

 BackupEventLog(handle, eventLogName)

Backs up the event log

#### Parameters

- handle : int

 Handle to the event log to backup.

- eventLogName : PyUnicode

 The name of the event log to save to


---

<!-- page: win32evtlog__ClearEventLog_meth.html -->

## win32evtlog.ClearEventLog

 ClearEventLog(handle, eventLogName)

Clears the event log

#### Parameters

- handle : int

 Handle to the event log to clear.

- eventLogName : PyUnicode

 The name of the event log to save to, or None


---

<!-- page: win32evtlog__CloseEventLog_meth.html -->

## win32evtlog.CloseEventLog

 CloseEventLog(handle)

Closes the eventlog

#### Parameters

- handle : int

 Handle to the event log to close


---

<!-- page: win32evtlog__DeregisterEventSource_meth.html -->

## win32evtlog.DeregisterEventSource

 DeregisterEventSource(handle)

Deregisters an Event Source

#### Parameters

- handle : int

 Identifies the event log whose handle was returned by win32evtlog::RegisterEventSource


---

<!-- page: win32evtlog__EvtArchiveExportedLog_meth.html -->

## win32evtlog.EvtArchiveExportedLog

 EvtArchiveExportedLog(LogFilePath, Locale, Session, Flags)

Localizes an exported event log file

#### Parameters

- LogFilePath : str

 Filename of an exported log file

- Locale : int

 Locale id

- Session=None : PyEVT_HANDLE

 Handle to a remote session (see win32evtlog::EvtOpenSession), or None for local machine.

- Flags=0 : int

 Reserved

#### Comments

 Accepts keyword args


---

<!-- page: win32evtlog__EvtClearLog_meth.html -->

## win32evtlog.EvtClearLog

 EvtClearLog(ChannelPath, TargetFilePath, Session, Flags)

Clears an event log and optionally exports events to an archive

#### Parameters

- ChannelPath : str

 Name of event log to be cleared

- TargetFilePath=None : str

 Name of file in which cleared events will be archived, or None

- Session=None : PyEVT_HANDLE

 Handle to a remote session (see win32evtlog::EvtOpenSession), or None for local machine.

- Flags=0 : int

 Reserved, use only 0

#### Comments

 Accepts keyword args


---

<!-- page: win32evtlog__EvtCreateBookmark_meth.html -->

## win32evtlog.EvtCreateBookmark

 PyEVT_HANDLE = EvtCreateBookmark(BookmarkXML)

Creates a bookmark

#### Parameters

- BookmarkXML=None : str

 XML representation of a bookmark as returned by win32evtlog::EvtRender, or None for a new bookmark

#### Comments

 Accepts keyword args


---

<!-- page: win32evtlog__EvtCreateRenderContext_meth.html -->

## win32evtlog.EvtCreateRenderContext

 PyEVT_HANDLE = EvtCreateRenderContext(Flags)

Creates a render context

#### Parameters

- Flags : int

 EvtRenderContextSystem or EvtRenderContextUser. EvtRenderContextValues not currently supported

#### Comments

 Accepts keyword args


---

<!-- page: win32evtlog__EvtExportLog_meth.html -->

## win32evtlog.EvtExportLog

 EvtExportLog(Path, TargetFilePath, Flags, Query, Session)

Exports events from a channel or log file

#### Parameters

- Path : str

 Path of a live event log channel or exported log file

- TargetFilePath : str

 File to create, cannot already exist

- Flags : int

 Combination of EvtExportLog* flags specifying the type of path

- Query=None : str

 Selects specific events to export

- Session=None : PyEVT_HANDLE

 Handle to a remote session (see win32evtlog::EvtOpenSession), or None for local machine.

#### Comments

 Accepts keyword args


---

<!-- page: win32evtlog__EvtFormatMessage_meth.html -->

## win32evtlog.EvtFormatMessage

 str,list = EvtFormatMessage(Metadata, Event , Flags , ResourceId )

Formats a message string.

#### Parameters

- Metadata : PyEVT_HANDLE

 Handle to provider metadata returned by win32evtlog::EvtOpenPublisherMetadata

- Event : PyEVT_HANDLE

 Handle to an event

- Flags : int

 Type of message to format. EvtFormatMessageEvent or EvtFormatMessageLevel or EvtFormatMessageTask or EvtFormatMessageOpcode or EvtFormatMessageKeyword or EvtFormatMessageChannel or EvtFormatMessageProvider or EvtFormatMessageId or EvtFormatMessageXml. If set to EvtFormatMessageId, callers should also set the 'ResourceId' parameter

- ResourceId=0 : int

 The resource identifier of a message string returned by win32evtlog::EvtGetPublisherMetadataProperty. Only set this if flags = EvtFormatMessageId.

#### Comments

 Accepts keyword args

#### Return Value

Returns a formatted message string, or a list of strings if Flags=EvtFormatMessageKeyword


---

<!-- page: win32evtlog__EvtGetChannelConfigProperty_meth.html -->

## win32evtlog.EvtGetChannelConfigProperty

 (object, int) = EvtGetChannelConfigProperty(ChannelConfig, PropertyId , Flags )

Retreives channel configuration information

#### Parameters

- ChannelConfig : PyEVT_HANDLE

 Config handle as returned by win32evtlog::EvtOpenChannelConfig

- PropertyId : int

 Property to retreive, one of EvtChannel* constants

- Flags=0 : int

 Reserved, use only 0

#### Comments

 Accepts keyword args

 Returns the value and type of value (EvtVarType*)


---

<!-- page: win32evtlog__EvtGetEventInfo_meth.html -->

## win32evtlog.EvtGetEventInfo

 (object, int) = EvtGetEventInfo(Event, PropertyId )

Retrieves information about the source of an event

#### Parameters

- Event : PyEVT_HANDLE

 Handle to an event

- PropertyId : int

 Property to retreive, EvtEvent*

#### Comments

 Accepts keyword args

 Returns the value and type of value (EvtVarType*)


---

<!-- page: win32evtlog__EvtGetEventMetadataProperty_meth.html -->

## win32evtlog.EvtGetEventMetadataProperty

 (object, int) = EvtGetEventMetadataProperty(EventMetadata, PropertyId , Flags )

Retrieves a property from an event publisher

#### Parameters

- EventMetadata : PyEVT_HANDLE

 Event metadata handle as returned by win32evtlog::EvtNextEventMetadata

- PropertyId : int

 Property to retreive, EventMetadata*

- Flags=0 : int

 Reserved, use only 0

#### Comments

 Accepts keyword args

#### Return Value

Returns the value and type of value (EvtVarType*).


---

<!-- page: win32evtlog__EvtGetExtendedStatus_meth.html -->

## win32evtlog.EvtGetExtendedStatus

 str = EvtGetExtendedStatus()

Returns additional error info from last Evt* call


---

<!-- page: win32evtlog__EvtGetLogInfo_meth.html -->

## win32evtlog.EvtGetLogInfo

 (object, int) = EvtGetLogInfo(Log, PropertyId )

Retrieves log file or channel information

#### Parameters

- Log : PyEVT_HANDLE

 Event log handle as returned by win32evtlog::EvtOpenLog

- PropertyId : int

 Property to retreive, EvtLog*

#### Comments

 Accepts keyword args

 Returns the value and type of value (EvtVarType*)


---

<!-- page: win32evtlog__EvtGetObjectArrayProperty_meth.html -->

## win32evtlog.EvtGetObjectArrayProperty

 (object, int) = EvtGetObjectArrayProperty(ObjectArray, PropertyId , ArrayIndex , Flags )

Retrieves an item from an object array

#### Parameters

- ObjectArray : PyEVT_HANDLE

 Handle to an array of objects as returned by win32evtlog::EvtGetPublisherMetadataProperty for some ProperyId's

- PropertyId : int

 Type of property contained in the array

- ArrayIndex : int

 Zero-based index of item to retrieve

- Flags=0 : int

 Reserved, use only 0

#### Comments

 Accepts keyword args

#### Return Value

Returns the value and type of value (EvtVarType*)


---

<!-- page: win32evtlog__EvtGetObjectArraySize_meth.html -->

## win32evtlog.EvtGetObjectArraySize

 int = EvtGetObjectArraySize(ObjectArray)

Returns the size of an array of event objects

#### Parameters

- ObjectArray : PyEVT_HANDLE

 Handle to an array of objects as returned by win32evtlog::EvtGetPublisherMetadataProperty for some ProperyId's

#### Comments

 Accepts keyword args


---

<!-- page: win32evtlog__EvtGetPublisherMetadataProperty_meth.html -->

## win32evtlog.EvtGetPublisherMetadataProperty

 (object, int) = EvtGetPublisherMetadataProperty(PublisherMetadata, PropertyId , Flags )

Retrieves a property from an event publisher

#### Parameters

- PublisherMetadata : PyEVT_HANDLE

 Publisher handle as returned by win32evtlog::EvtOpenPublisherMetadata

- PropertyId : int

 Property to retreive, EvtPublisherMetadata*

- Flags=0 : int

 Reserved, use only 0

#### Comments

 Accepts keyword args

#### Return Value

Returns the value and type of value (EvtVarType*) Some properties return a handle (type EvtVarTypeEvtHandle) which can be iterated using win32evtlog::EvtGetObjectArraySize and win32evtlog::EvtGetObjectArrayProperty.


---

<!-- page: win32evtlog__EvtNextChannelPath_meth.html -->

## win32evtlog.EvtNextChannelPath

 str = EvtNextChannelPath(ChannelEnum)

Retrieves a channel path from an enumeration

#### Parameters

- ChannelEnum : PyEVT_HANDLE

 Handle to an enumeration as returned by win32evtlog::EvtOpenChannelEnum

#### Comments

 Accepts keyword args

#### Return Value

Returns None at end of enumeration


---

<!-- page: win32evtlog__EvtNextEventMetadata_meth.html -->

## win32evtlog.EvtNextEventMetadata

 PyEVT_HANDLE = EvtNextEventMetadata(EventMetadataEnum, Flags )

Retrieves the next item from an event metadata enumeration

#### Parameters

- EventMetadataEnum : PyEVT_HANDLE

 Enumeration handle as returned by win32evtlog::EvtOpenEventMetadataEnum

- Flags=0 : int

 Reserved, use only 0

#### Comments

 Accepts keyword args


---

<!-- page: win32evtlog__EvtNextPublisherId_meth.html -->

## win32evtlog.EvtNextPublisherId

 str = EvtNextPublisherId(PublisherEnum)

Returns the next publisher from an enumeration

#### Parameters

- PublisherEnum : PyEVT_HANDLE

 Handle to an enumeration as returned by win32evtlog::EvtOpenPublisherEnum

#### Comments

 Accepts keyword args

#### Return Value

Returns None at end of enumeration


---

<!-- page: win32evtlog__EvtNext_meth.html -->

## win32evtlog.EvtNext

 (PyEVT_HANDLE,...) = EvtNext(ResultSet, Count , Timeout , Flags )

Returns events from a query

#### Parameters

- ResultSet : PyEVT_HANDLE

 Handle to event query or subscription

- Count : int

 Number of events to return

- Timeout=-1 : int

 Time to wait in milliseconds, use -1 for infinite

- Flags=0 : int

 Reserved, use only 0

#### Comments

 Accepts keyword args

#### Return Value

Returns a tuple of handles to events. If no items are available, returns an empty tuple instead of raising an exception.


---

<!-- page: win32evtlog__EvtOpenChannelConfig_meth.html -->

## win32evtlog.EvtOpenChannelConfig

 PyEVT_HANDLE = EvtOpenChannelConfig(ChannelPath, Session , Flags )

Opens channel configuration

#### Parameters

- ChannelPath : str

 Channel to be opened

- Session=None : PyEVT_HANDLE

 Session handle as returned by win32evtlog::EvtOpenSession, or None for local machine

- Flags=0 : int

 Reserved, use only 0

#### Comments

 Accepts keyword args


---

<!-- page: win32evtlog__EvtOpenChannelEnum_meth.html -->

## win32evtlog.EvtOpenChannelEnum

 PyEVT_HANDLE = EvtOpenChannelEnum(Session, Flags )

Begins an enumeration of event channels

#### Parameters

- Session=None : PyEVT_HANDLE

 Handle to a remote session (see win32evtlog::EvtOpenSession), or None for local machine.

- Flags=0 : int

 Reserved, use only 0

#### Comments

 Accepts keyword args


---

<!-- page: win32evtlog__EvtOpenEventMetadataEnum_meth.html -->

## win32evtlog.EvtOpenEventMetadataEnum

 PyEVT_HANDLE = EvtOpenEventMetadataEnum(PublisherMetadata, Flags )

Enumerates the events that a publisher provides

#### Parameters

- PublisherMetadata : PyEVT_HANDLE

 Publisher handle as returned by win32evtlog::EvtOpenPublisherMetadata

- Flags=0 : int

 Reserved, use only 0

#### Comments

 Accepts keyword args


---

<!-- page: win32evtlog__EvtOpenLog_meth.html -->

## win32evtlog.EvtOpenLog

 PyEVT_HANDLE = EvtOpenLog(Path, Flags , Session )

Opens an event log or exported log archive

#### Parameters

- Path : str

 Event log name or Path of an export file

- Flags : int

 EvtOpenChannelPath (1) or EvtOpenFilePath (2)

- Session=None : PyEVT_HANDLE

 Handle to a remote session (see win32evtlog::EvtOpenSession), or None for local machine.

#### Comments

 Accepts keyword args


---

<!-- page: win32evtlog__EvtOpenPublisherEnum_meth.html -->

## win32evtlog.EvtOpenPublisherEnum

 PyEVT_HANDLE = EvtOpenPublisherEnum(Session, Flags )

Begins an enumeration of event publishers

#### Parameters

- Session=None : PyEVT_HANDLE

 Handle to a remote session (see win32evtlog::EvtOpenSession), or None for local machine.

- Flags=0 : int

 Reserved, use only 0

#### Comments

 Accepts keyword args


---

<!-- page: win32evtlog__EvtOpenPublisherMetadata_meth.html -->

## win32evtlog.EvtOpenPublisherMetadata

 PyEVT_HANDLE = EvtOpenPublisherMetadata(PublisherIdentity, Session , LogFilePath , Locale , Flags )

Opens a publisher to retrieve properties using win32evtlog::EvtGetPublisherMetadataProperty

#### Parameters

- PublisherIdentity : str

 Publisher id as returned by win32evtlog::EvtNextPublisherId

- Session=None : PyEVT_HANDLE

 Handle to remote session, or None for local machine

- LogFilePath=None : str

 Log file from which to retrieve publisher, or None for locally registered publisher

- Locale=0 : int

 Locale to use for retrieved properties, use 0 for current locale

- Flags=0 : int

 Reserved, use only 0

#### Comments

 Accepts keyword args


---

<!-- page: win32evtlog__EvtOpenSession_meth.html -->

## win32evtlog.EvtOpenSession

 PyEVT_HANDLE = EvtOpenSession(Login, LoginClass , Timeout , Flags )

Creates a session used to access the Event Log on another machine

#### Parameters

- Login : PyEVT_RPC_LOGIN

 Credentials to be used to access remote machine

- LoginClass=EvtRpcLogin : int

 Type of login to perform, EvtRpcLogin is only defined value

- Timeout=0 : int

 Reserved, use only 0

- Flags=0 : int

 Reserved, use only 0

#### Comments

 Accepts keyword args


---

<!-- page: win32evtlog__EvtQuery_meth.html -->

## win32evtlog.EvtQuery

 PyEVT_HANDLE = EvtQuery(Path, Flags , Query , Session )

Opens a query over a log channel or exported log file

#### Parameters

- Path : str

 Log channel or exported log file, depending on Flags

- Flags : int

 Combination of EVT_QUERY_FLAGS (EvtQuery*)

- Query=None : str

 Selects events to return, None or '*' for all events

- Session=None : PyEVT_HANDLE

 Handle to a remote session (see win32evtlog::EvtOpenSession), or None for local machine.

#### Comments

 Accepts keyword args


---

<!-- page: win32evtlog__EvtRender_meth.html -->

## win32evtlog.EvtRender

 str = EvtRender(Event, Flags , Context )

Formats an event into XML text or a Python Dict of key/values

#### Parameters

- Event : PyEVT_HANDLE

 Handle to an event or bookmark

- Flags : int

 EvtRenderEventValues or EvtRenderEventXml or EvtRenderBookmark indicating type of handle

- Context=None : PyEVT_HANDLE

 Handle to a render context returned by win32evtlog::EvtCreateRenderContext

#### Comments

 Accepts keyword args

 Rendering event values


---

<!-- page: win32evtlog__EvtSeek_meth.html -->

## win32evtlog.EvtSeek

 EvtSeek(ResultSet, Position, Flags, Bookmark, Timeout)

Changes the current position in a result set

#### Parameters

- ResultSet : PyEVT_HANDLE

 Handle to event query or subscription

- Position : int

 Offset (base from which to seek is specified by Flags)

- Flags : int

 EvtSeekRelative* flag indicating seek origin

- Bookmark=None : PyEVT_HANDLE

 Used as seek origin only if Flags contains EvtSeekRelativeToBookmark

- Timeout=0 : int

 Reserved, use only 0

#### Comments

 Accepts keyword args


---

<!-- page: win32evtlog__EvtSubscribe_meth.html -->

## win32evtlog.EvtSubscribe

 PyEVT_HANDLE = EvtSubscribe(ChannelPath, Flags , SignalEvent , Callback , Context , Query , Session , Bookmark )

Requests notification for events

#### Parameters

- ChannelPath : str

 Name of an event log channel

- Flags : int

 Combination of EvtSubscribe* flags determining how subscription is initiated

- SignalEvent=None : Py_HANDLE

 An event handle to be set when events are available (see win32event::CreateEvent)

- Callback=None : function

 Python function to be called with each event

- Context=None : object

 Arbitrary object to be passed to the callback function

- Query=None : str

 XML query used to select specific events, use None or '*' for all events

- Session=None : PyEVT_HANDLE

 Handle to a session on another machine, or None for local

- Bookmark=None : PyEVT_HANDLE

 If Flags contains EvtSubscribeStartAfterBookmark, used as starting point

#### Comments

 Accepts keyword args

 The method used to receive events is determined by the parameters passed in. To create a push subscription, define a callback function that will be called with each event. The function will receive 3 args: First is an integer specifying why the function was called (EvtSubscribeActionError or EvtSubscribeActionDeliver) Second is the context object passed to EvtSubscribe. Third is the handle to an event log record (if not called due to an error) If an event handle is passed in, a pull subscription is created. The event handle will be signalled when events are available, and the subscription handle can be passed to win32evtlog::EvtNext to obtain the events.


---

<!-- page: win32evtlog__EvtUpdateBookmark_meth.html -->

## win32evtlog.EvtUpdateBookmark

 PyEVT_HANDLE = EvtUpdateBookmark(Bookmark, Event )

Repositions a bookmark to an event

#### Parameters

- Bookmark : PyEVT_HANDLE

 Handle to a bookmark

- Event : PyEVT_HANDLE

 Handle to an event

#### Comments

 Accepts keyword args


---

<!-- page: win32evtlog__GetNumberOfEventLogRecords_meth.html -->

## win32evtlog.GetNumberOfEventLogRecords

 int = GetNumberOfEventLogRecords(handle)

Returns the number of event log records.

#### Parameters

- handle : int

 Handle to the event log to query.


---

<!-- page: win32evtlog__GetOldestEventLogRecord_meth.html -->

## win32evtlog.GetOldestEventLogRecord

 int = GetOldestEventLogRecord()

Returns the number of event log records.

#### Return Value

The result is the absolute record number of the oldest record in the given event log.


---

<!-- page: win32evtlog__NotifyChangeEventLog_meth.html -->

## win32evtlog.NotifyChangeEventLog

 NotifyChangeEventLog(handle, handle)

Lets an application receive notification when an event is written to the event log file specified by the hEventLog parameter. When the event is written to the event log file, the function causes the event object specified by the hEvent parameter to become signaled.

#### Parameters

- handle : int

 Handle to an event log file, obtained by calling win32evtlog::OpenEventLog function. When an event is written to this log file, the event specified by hEvent becomes signaled.

- handle : int

 A handle to a Win32 event. This is the event that becomes signaled when an event is written to the event log file specified by the hEventLog parameter.


---

<!-- page: win32evtlog__OpenBackupEventLog_meth.html -->

## win32evtlog.OpenBackupEventLog

 PyEVTLOG_HANDLE = OpenBackupEventLog(serverName, fileName )

Opens a previously saved event log.

#### Parameters

- serverName : PyUnicode

 The server name, or None

- fileName : PyUnicode

 The filename to open


---

<!-- page: win32evtlog__OpenEventLog_meth.html -->

## win32evtlog.OpenEventLog

 PyEVTLOG_HANDLE = OpenEventLog(serverName, sourceName )

Opens an event log.

#### Parameters

- serverName : PyUnicode

 The server name, or None

- sourceName : PyUnicode

 specifies the name of the source that the returned handle will reference. The source name must be a subkey of a logfile entry under the EventLog key in the registry.


---

<!-- page: win32evtlog__ReadEventLog_meth.html -->

## win32evtlog.ReadEventLog

 [object,...] = ReadEventLog(Handle, Flags , Offset , Size )

Reads some event log records.

#### Parameters

- Handle : Py_HANDLE

 Handle to a an opened event log (see win32evtlog::OpenEventLog)

- Flags : int

 Reading flags

- Offset : int

 Record offset to read (in SEEK mode).

- Size=4096 : int

 Output buffer size.

#### Return Value

If there are no event log records available, then an empty list is returned.


---

<!-- page: win32evtlog__RegisterEventSource_meth.html -->

## win32evtlog.RegisterEventSource

 int = RegisterEventSource(serverName, sourceName )

Registers an Event Source

#### Parameters

- serverName : PyUnicode

 The server name, or None

- sourceName : PyUnicode

 The source name


---

<!-- page: win32evtlog__ReportEvent_meth.html -->

## win32evtlog.ReportEvent

 ReportEvent(EventLog, Type, Category, EventID, UserSid, Strings, RawData)

Reports an event

#### Parameters

- EventLog : PyHANDLE

 Handle to an event log

- Type : int

 win32con.EVENTLOG_* value

- Category : int

 Source-specific event category

- EventID : int

 Source-specific event identifier

- UserSid : PySID

 Sid of current user, can be None

- Strings : sequence

 Sequence of unicode strings to be inserted in message

- RawData : str

 Binary data for event, can be None
