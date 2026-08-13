# 官方示例源码 · win32/Demos

> 来源 https://github.com/mhammond/pywin32/tree/main/win32/Demos （共 72 个 .py，全文内联）


---

## win32/Demos/BackupRead_BackupWrite.py

```python
## demonstrates using BackupRead and BackupWrite to copy all of a file's data streams

import ntsecuritycon
import pythoncom
import pywintypes
import win32api
import win32con
import win32file
import win32security
from win32com import storagecon

all_sd_info = (
    win32security.DACL_SECURITY_INFORMATION
    | win32security.DACL_SECURITY_INFORMATION
    | win32security.OWNER_SECURITY_INFORMATION
    | win32security.GROUP_SECURITY_INFORMATION
)

tempdir = win32api.GetTempPath()
tempfile = win32api.GetTempFileName(tempdir, "bkr")[0]
outfile = win32api.GetTempFileName(tempdir, "out")[0]
print("Filename:", tempfile, "Output file:", outfile)

f = open(tempfile, "w")
f.write("some random junk" + "x" * 100)
f.close()

## add a couple of alternate data streams
f = open(tempfile + ":streamdata", "w")
f.write("data written to alternate stream" + "y" * 100)
f.close()

f = open(tempfile + ":anotherstream", "w")
f.write("z" * 100)
f.close()

## add Summary Information, which is stored as a separate stream
m = storagecon.STGM_READWRITE | storagecon.STGM_SHARE_EXCLUSIVE | storagecon.STGM_DIRECT
pss = pythoncom.StgOpenStorageEx(
    tempfile, m, storagecon.STGFMT_FILE, 0, pythoncom.IID_IPropertySetStorage, None
)
ps = pss.Create(
    pythoncom.FMTID_SummaryInformation,
    pythoncom.IID_IPropertyStorage,
    0,
    storagecon.STGM_READWRITE | storagecon.STGM_SHARE_EXCLUSIVE,
)
ps.WriteMultiple(
    (storagecon.PIDSI_KEYWORDS, storagecon.PIDSI_COMMENTS), ("keywords", "comments")
)
ps = None
pss = None

## add a custom security descriptor to make sure we don't
##   get a default that would always be the same for both files in temp dir
new_sd = pywintypes.SECURITY_DESCRIPTOR()
sid = win32security.LookupAccountName("", "EveryOne")[0]
acl = pywintypes.ACL()
acl.AddAccessAllowedAce(1, win32con.GENERIC_READ, sid)
acl.AddAccessAllowedAce(1, ntsecuritycon.FILE_APPEND_DATA, sid)
acl.AddAccessAllowedAce(1, win32con.GENERIC_WRITE, sid)
acl.AddAccessAllowedAce(1, ntsecuritycon.FILE_ALL_ACCESS, sid)

new_sd.SetSecurityDescriptorDacl(True, acl, False)
win32security.SetFileSecurity(tempfile, win32security.DACL_SECURITY_INFORMATION, new_sd)


sa = pywintypes.SECURITY_ATTRIBUTES()
sa.bInheritHandle = True
h = win32file.CreateFile(
    tempfile,
    win32con.GENERIC_ALL,
    win32con.FILE_SHARE_READ,
    sa,
    win32con.OPEN_EXISTING,
    win32file.FILE_FLAG_BACKUP_SEMANTICS,
    None,
)

outh = win32file.CreateFile(
    outfile,
    win32con.GENERIC_ALL,
    win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE,
    sa,
    win32con.OPEN_EXISTING,
    win32file.FILE_FLAG_BACKUP_SEMANTICS,
    None,
)

ctxt = 0
outctxt = 0
buf = None
readsize = 100

while 1:
    bytes_read, buf, ctxt = win32file.BackupRead(h, readsize, buf, False, True, ctxt)
    if bytes_read == 0:
        break
    bytes_written, outctxt = win32file.BackupWrite(
        outh, bytes_read, buf, False, True, outctxt
    )
    print("Written:", bytes_written, "Context:", outctxt)
win32file.BackupRead(h, 0, buf, True, True, ctxt)
win32file.BackupWrite(outh, 0, b"", True, True, outctxt)
win32file.CloseHandle(h)
win32file.CloseHandle(outh)

assert open(tempfile).read() == open(outfile).read(), "File contents differ !"
assert open(tempfile + ":streamdata").read() == open(outfile + ":streamdata").read(), (
    "streamdata contents differ !"
)
assert (
    open(tempfile + ":anotherstream").read() == open(outfile + ":anotherstream").read()
), "anotherstream contents differ !"
assert (
    memoryview(win32security.GetFileSecurity(tempfile, all_sd_info))[:]
    == memoryview(win32security.GetFileSecurity(outfile, all_sd_info))[:]
), "Security descriptors are different !"
## also should check Summary Info programatically

```


---

## win32/Demos/BackupSeek_streamheaders.py

```python
## demonstrates using BackupSeek to enumerate data streams for a file
import struct

import pythoncom
import pywintypes
import win32api
import win32con
import win32file
from win32com import storagecon

stream_types = {
    win32con.BACKUP_DATA: "Standard data",
    win32con.BACKUP_EA_DATA: "Extended attribute data",
    win32con.BACKUP_SECURITY_DATA: "Security descriptor data",
    win32con.BACKUP_ALTERNATE_DATA: "Alternative data streams",
    win32con.BACKUP_LINK: "Hard link information",
    win32con.BACKUP_PROPERTY_DATA: "Property data",
    win32con.BACKUP_OBJECT_ID: "Objects identifiers",
    win32con.BACKUP_REPARSE_DATA: "Reparse points",
    win32con.BACKUP_SPARSE_BLOCK: "Sparse file",
}

tempdir = win32api.GetTempPath()
tempfile = win32api.GetTempFileName(tempdir, "bkr")[0]
print("Filename:", tempfile)

f = open(tempfile, "w")
f.write("some random junk" + "x" * 100)
f.close()

f = open(tempfile + ":streamdata", "w")
f.write("data written to alternate stream" + "y" * 100)
f.close()

f = open(tempfile + ":anotherstream", "w")
f.write("z" * 200)
f.close()

## add Summary Information, which is stored as a separate stream
m = storagecon.STGM_READWRITE | storagecon.STGM_SHARE_EXCLUSIVE | storagecon.STGM_DIRECT
pss = pythoncom.StgOpenStorageEx(
    tempfile, m, storagecon.STGFMT_FILE, 0, pythoncom.IID_IPropertySetStorage, None
)
ps = pss.Create(
    pythoncom.FMTID_SummaryInformation,
    pythoncom.IID_IPropertyStorage,
    0,
    storagecon.STGM_READWRITE | storagecon.STGM_SHARE_EXCLUSIVE,
)
ps.WriteMultiple(
    (storagecon.PIDSI_KEYWORDS, storagecon.PIDSI_COMMENTS), ("keywords", "comments")
)
ps = None
pss = None

sa = pywintypes.SECURITY_ATTRIBUTES()
sa.bInheritHandle = False
h = win32file.CreateFile(
    tempfile,
    win32con.GENERIC_ALL,
    win32con.FILE_SHARE_READ,
    sa,
    win32con.OPEN_EXISTING,
    win32file.FILE_FLAG_BACKUP_SEMANTICS,
    None,
)


""" stream header:
typedef struct _WIN32_STREAM_ID {
    DWORD dwStreamId;  DWORD dwStreamAttributes;  LARGE_INTEGER Size;
    DWORD dwStreamNameSize;  WCHAR cStreamName[ANYSIZE_ARRAY];
}
"""

win32_stream_id_format = "LLQL"
win32_stream_id_size = struct.calcsize(win32_stream_id_format)


def parse_stream_header(h, ctxt, data):
    stream_type, stream_attributes, stream_size, stream_name_size = struct.unpack(
        win32_stream_id_format, data
    )
    print(
        "\nType:",
        stream_type,
        stream_types[stream_type],
        "Attributes:",
        stream_attributes,
        "Size:",
        stream_size,
        "Name len:",
        stream_name_size,
    )
    if stream_name_size > 0:
        ## ??? sdk says this size is in characters, but it appears to be number of bytes ???
        bytes_read, stream_name_buf, ctxt = win32file.BackupRead(
            h, stream_name_size, None, False, True, ctxt
        )
        stream_name = pywintypes.UnicodeFromRaw(stream_name_buf[:])
    else:
        stream_name = "Unnamed"
    print("Name:" + stream_name)
    return (
        ctxt,
        stream_type,
        stream_attributes,
        stream_size,
        stream_name_size,
        stream_name,
    )


ctxt = 0
win32_stream_id_buf = (
    None  ## gets rebound to a writable buffer on first call and reused
)
while 1:
    bytes_read, win32_stream_id_buf, ctxt = win32file.BackupRead(
        h, win32_stream_id_size, win32_stream_id_buf, False, True, ctxt
    )
    if bytes_read == 0:
        break
    (
        ctxt,
        stream_type,
        stream_attributes,
        stream_size,
        stream_name_size,
        stream_name,
    ) = parse_stream_header(h, ctxt, win32_stream_id_buf[:])
    if stream_size > 0:
        bytes_moved = win32file.BackupSeek(h, stream_size, ctxt)
        print("Moved: ", bytes_moved)

win32file.BackupRead(h, win32_stream_id_size, win32_stream_id_buf, True, True, ctxt)
win32file.CloseHandle(h)

```


---

## win32/Demos/CopyFileEx.py

```python
import win32api
import win32file


def ProgressRoutine(
    TotalFileSize,
    TotalBytesTransferred,
    StreamSize,
    StreamBytesTransferred,
    StreamNumber,
    CallbackReason,
    SourceFile,
    DestinationFile,
    Data,
):
    print(Data)
    print(
        TotalFileSize,
        TotalBytesTransferred,
        StreamSize,
        StreamBytesTransferred,
        StreamNumber,
        CallbackReason,
        SourceFile,
        DestinationFile,
    )
    ##if TotalBytesTransferred > 100000:
    ##    return win32file.PROGRESS_STOP
    return win32file.PROGRESS_CONTINUE


temp_dir = win32api.GetTempPath()
fsrc = win32api.GetTempFileName(temp_dir, "cfe")[0]
fdst = win32api.GetTempFileName(temp_dir, "cfe")[0]
print(fsrc, fdst)

f = open(fsrc, "w")
f.write("xxxxxxxxxxxxxxxx\n" * 32768)
f.close()
## add a couple of extra data streams
f = open(fsrc + ":stream_y", "w")
f.write("yyyyyyyyyyyyyyyy\n" * 32768)
f.close()
f = open(fsrc + ":stream_z", "w")
f.write("zzzzzzzzzzzzzzzz\n" * 32768)
f.close()

operation_desc = "Copying " + fsrc + " to " + fdst
win32file.CopyFileEx(
    fsrc,
    fdst,
    ProgressRoutine,
    Data=operation_desc,
    Cancel=False,
    CopyFlags=win32file.COPY_FILE_RESTARTABLE,
    Transaction=None,
)

```


---

## win32/Demos/CreateFileTransacted_MiniVersion.py

```python
"""
This demonstrates the creation of miniversions of a file during a transaction.
The FSCTL_TXFS_CREATE_MINIVERSION control code saves any changes to a new
miniversion (effectively a savepoint within a transaction).
"""

import os
import struct

import win32api
import win32con
import win32file
import win32transaction
import winerror
import winioctlcon


def demo():
    """
    Definition of buffer used with FSCTL_TXFS_CREATE_MINIVERSION:
    typedef struct _TXFS_CREATE_MINIVERSION_INFO{
        USHORT StructureVersion;
        USHORT StructureLength;
        ULONG BaseVersion;
        USHORT MiniVersion;}
    """
    buf_fmt = "HHLH0L"  ## buffer size must include struct padding
    buf_size = struct.calcsize(buf_fmt)

    tempdir = win32api.GetTempPath()
    tempfile = win32api.GetTempFileName(tempdir, "cft")[0]
    print("Demonstrating transactions on tempfile", tempfile)
    f = open(tempfile, "w")
    f.write("This is original file.\n")
    f.close()

    trans = win32transaction.CreateTransaction(
        Description="Test creating miniversions of a file"
    )
    hfile = win32file.CreateFileW(
        tempfile,
        win32con.GENERIC_READ | win32con.GENERIC_WRITE,
        win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE,
        None,
        win32con.OPEN_EXISTING,
        0,
        None,
        Transaction=trans,
    )

    win32file.WriteFile(hfile, b"This is first miniversion.\n")
    buf = win32file.DeviceIoControl(
        hfile, winioctlcon.FSCTL_TXFS_CREATE_MINIVERSION, None, buf_size, None
    )
    struct_ver, struct_len, base_ver, ver_1 = struct.unpack(buf_fmt, buf)

    win32file.SetFilePointer(hfile, 0, win32con.FILE_BEGIN)
    win32file.WriteFile(hfile, b"This is second miniversion!\n")
    buf = win32file.DeviceIoControl(
        hfile, winioctlcon.FSCTL_TXFS_CREATE_MINIVERSION, None, buf_size, None
    )
    struct_ver, struct_len, base_ver, ver_2 = struct.unpack(buf_fmt, buf)
    hfile.Close()

    ## miniversions can't be opened with write access
    hfile_0 = win32file.CreateFileW(
        tempfile,
        win32con.GENERIC_READ,
        win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE,
        None,
        win32con.OPEN_EXISTING,
        0,
        None,
        Transaction=trans,
        MiniVersion=base_ver,
    )
    print("version:", base_ver, win32file.ReadFile(hfile_0, 100))
    hfile_0.Close()

    hfile_1 = win32file.CreateFileW(
        tempfile,
        win32con.GENERIC_READ,
        win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE,
        None,
        win32con.OPEN_EXISTING,
        0,
        None,
        Transaction=trans,
        MiniVersion=ver_1,
    )
    print("version:", ver_1, win32file.ReadFile(hfile_1, 100))
    hfile_1.Close()

    hfile_2 = win32file.CreateFileW(
        tempfile,
        win32con.GENERIC_READ,
        win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE,
        None,
        win32con.OPEN_EXISTING,
        0,
        None,
        Transaction=trans,
        MiniVersion=ver_2,
    )
    print("version:", ver_2, win32file.ReadFile(hfile_2, 100))
    hfile_2.Close()

    ## MiniVersions are destroyed when transaction is committed or rolled back
    win32transaction.CommitTransaction(trans)

    os.unlink(tempfile)


if __name__ == "__main__":
    # When run on CI, this fails with NOT_SUPPORTED, so don't have that cause "failure"
    try:
        demo()
    except win32file.error as e:
        if e.winerror == winerror.ERROR_NOT_SUPPORTED:
            print("These features are not supported by this filesystem.")
        else:
            raise

```


---

## win32/Demos/EvtFormatMessage.py

```python
import sys

import win32evtlog


def main():
    path = "System"
    num_events = 5
    if len(sys.argv) > 2:
        path = sys.argv[1]
        num_events = int(sys.argv[2])
    elif len(sys.argv) > 1:
        path = sys.argv[1]

    query = win32evtlog.EvtQuery(path, win32evtlog.EvtQueryForwardDirection)
    events = win32evtlog.EvtNext(query, num_events)
    context = win32evtlog.EvtCreateRenderContext(win32evtlog.EvtRenderContextSystem)

    for i, event in enumerate(events, 1):
        result = win32evtlog.EvtRender(
            event, win32evtlog.EvtRenderEventValues, Context=context
        )

        print(f"Event {i}")

        level_value, level_variant = result[win32evtlog.EvtSystemLevel]
        if level_variant != win32evtlog.EvtVarTypeNull:
            if level_value == 1:
                print("    Level: CRITICAL")
            elif level_value == 2:
                print("    Level: ERROR")
            elif level_value == 3:
                print("    Level: WARNING")
            elif level_value == 4:
                print("    Level: INFO")
            elif level_value == 5:
                print("    Level: VERBOSE")
            else:
                print("    Level: UNKNOWN")

        time_created_value, time_created_variant = result[
            win32evtlog.EvtSystemTimeCreated
        ]
        if time_created_variant != win32evtlog.EvtVarTypeNull:
            print(f"    Timestamp: {time_created_value.isoformat()}")

        computer_value, computer_variant = result[win32evtlog.EvtSystemComputer]
        if computer_variant != win32evtlog.EvtVarTypeNull:
            print(f"    FQDN: {computer_value}")

        provider_name_value, provider_name_variant = result[
            win32evtlog.EvtSystemProviderName
        ]
        if provider_name_variant != win32evtlog.EvtVarTypeNull:
            print(f"    Provider: {provider_name_value}")

            try:
                metadata = win32evtlog.EvtOpenPublisherMetadata(provider_name_value)
            # pywintypes.error: (2, 'EvtOpenPublisherMetadata', 'The system cannot find the file specified.')
            except Exception:
                pass
            else:
                try:
                    message = win32evtlog.EvtFormatMessage(
                        metadata, event, win32evtlog.EvtFormatMessageEvent
                    )
                # pywintypes.error: (15027, 'EvtFormatMessage: allocated 0, need buffer of size 0', 'The message resource is present but the message was not found in the message table.')
                except Exception:
                    pass
                else:
                    try:
                        print(f"    Message: {message}")
                    except UnicodeEncodeError:
                        # Obscure error when run under subprocess.Popen(), presumably due to
                        # not knowing the correct encoding for the console.
                        # > UnicodeEncodeError: \'charmap\' codec can\'t encode character \'\\u200e\' in position 57: character maps to <undefined>\r\n'
                        # Can't reproduce when running manually, so it seems more a subprocess.Popen()
                        # than ours:
                        print(f" Failed to decode: {message!r}")


if __name__ == "__main__":
    main()

```


---

## win32/Demos/EvtSubscribe_pull.py

```python
## Demonstrates how to create a "pull" subscription
import win32con
import win32event
import win32evtlog

query_text = '*[System[Provider[@Name="Microsoft-Windows-Winlogon"]]]'

h = win32event.CreateEvent(None, 0, 0, None)
s = win32evtlog.EvtSubscribe(
    "System",
    win32evtlog.EvtSubscribeStartAtOldestRecord,
    SignalEvent=h,
    Query=query_text,
)

while 1:
    while 1:
        events = win32evtlog.EvtNext(s, 10)
        if len(events) == 0:
            break
        ##for event in events:
        ##	print(win32evtlog.EvtRender(event, win32evtlog.EvtRenderEventXml))
        print("retrieved %s events" % len(events))
    while 1:
        print("waiting...")
        w = win32event.WaitForSingleObjectEx(h, 2000, True)
        if w == win32con.WAIT_OBJECT_0:
            break

```


---

## win32/Demos/EvtSubscribe_push.py

```python
## Demonstrates a "push" subscription with a callback function
from __future__ import annotations

from time import sleep

import win32evtlog

query_text = '*[System[Provider[@Name="Microsoft-Windows-Winlogon"]]]'


def c(reason, context, evt):
    if reason == win32evtlog.EvtSubscribeActionError:
        print("EvtSubscribeActionError")
    elif reason == win32evtlog.EvtSubscribeActionDeliver:
        print("EvtSubscribeActionDeliver")
    else:
        print("??? Unknown action ???", reason)
    context.append(win32evtlog.EvtRender(evt, win32evtlog.EvtRenderEventXml))
    return 0


evttext: list[str] = []
s = win32evtlog.EvtSubscribe(
    "System",
    win32evtlog.EvtSubscribeStartAtOldestRecord,
    Query="*",
    Callback=c,
    Context=evttext,
)

sleep(0.001)
print("\n".join(evttext))

```


---

## win32/Demos/FileSecurityTest.py

```python
# Contributed by Kelly Kranabetter.
import os
import sys

import ntsecuritycon
import pywintypes
import win32security
import winerror

# get security information
# name=r"c:\autoexec.bat"
# name= r"g:\!workgrp\lim"
name = sys.argv[0]

if not os.path.exists(name):
    print(name, "does not exist!")
    sys.exit()

print("On file ", name, "\n")

# get owner SID
print("OWNER")
try:
    sd = win32security.GetFileSecurity(name, win32security.OWNER_SECURITY_INFORMATION)
    sid = sd.GetSecurityDescriptorOwner()
    print("  ", win32security.LookupAccountSid(None, sid))
except pywintypes.error as exc:
    # in automation and network shares we see:
    # pywintypes.error: (1332, 'LookupAccountName', 'No mapping between account names and security IDs was done.')
    if exc.winerror != winerror.ERROR_NONE_MAPPED:
        raise
    print("No owner information is available")

# get group SID
try:
    print("GROUP")
    sd = win32security.GetFileSecurity(name, win32security.GROUP_SECURITY_INFORMATION)
    sid = sd.GetSecurityDescriptorGroup()
    print("  ", win32security.LookupAccountSid(None, sid))
except pywintypes.error as exc:
    if exc.winerror != winerror.ERROR_NONE_MAPPED:
        raise
    print("No group information is available")

# get ACEs
sd = win32security.GetFileSecurity(name, win32security.DACL_SECURITY_INFORMATION)
dacl = sd.GetSecurityDescriptorDacl()
if dacl is None:
    print("No Discretionary ACL")
else:
    for ace_no in range(0, dacl.GetAceCount()):
        ace = dacl.GetAce(ace_no)
        print("ACE", ace_no)

        print("  -Type")
        for i in (
            "ACCESS_ALLOWED_ACE_TYPE",
            "ACCESS_DENIED_ACE_TYPE",
            "SYSTEM_AUDIT_ACE_TYPE",
            "SYSTEM_ALARM_ACE_TYPE",
        ):
            if getattr(ntsecuritycon, i) == ace[0][0]:
                print("    ", i)

        print("  -Flags", hex(ace[0][1]))
        for i in (
            "OBJECT_INHERIT_ACE",
            "CONTAINER_INHERIT_ACE",
            "NO_PROPAGATE_INHERIT_ACE",
            "INHERIT_ONLY_ACE",
            "SUCCESSFUL_ACCESS_ACE_FLAG",
            "FAILED_ACCESS_ACE_FLAG",
        ):
            if getattr(ntsecuritycon, i) & ace[0][1] == getattr(ntsecuritycon, i):
                print("    ", i)

        print("  -mask", hex(ace[1]))

        # files and directories do permissions differently
        permissions_file = (
            "DELETE",
            "READ_CONTROL",
            "WRITE_DAC",
            "WRITE_OWNER",
            "SYNCHRONIZE",
            "FILE_GENERIC_READ",
            "FILE_GENERIC_WRITE",
            "FILE_GENERIC_EXECUTE",
            "FILE_DELETE_CHILD",
        )
        permissions_dir = (
            "DELETE",
            "READ_CONTROL",
            "WRITE_DAC",
            "WRITE_OWNER",
            "SYNCHRONIZE",
            "FILE_ADD_SUBDIRECTORY",
            "FILE_ADD_FILE",
            "FILE_DELETE_CHILD",
            "FILE_LIST_DIRECTORY",
            "FILE_TRAVERSE",
            "FILE_READ_ATTRIBUTES",
            "FILE_WRITE_ATTRIBUTES",
            "FILE_READ_EA",
            "FILE_WRITE_EA",
        )
        permissions_dir_inherit = (
            "DELETE",
            "READ_CONTROL",
            "WRITE_DAC",
            "WRITE_OWNER",
            "SYNCHRONIZE",
            "GENERIC_READ",
            "GENERIC_WRITE",
            "GENERIC_EXECUTE",
            "GENERIC_ALL",
        )
        if os.path.isfile(name):
            permissions = permissions_file
        else:
            permissions = permissions_dir
            # directories also contain an ACE that is inherited by children (files) within them
            if (
                ace[0][1] & ntsecuritycon.OBJECT_INHERIT_ACE
                == ntsecuritycon.OBJECT_INHERIT_ACE
                and ace[0][1] & ntsecuritycon.INHERIT_ONLY_ACE
                == ntsecuritycon.INHERIT_ONLY_ACE
            ):
                permissions = permissions_dir_inherit

        calc_mask = 0  # calculate the mask so we can see if we are printing all of the permissions
        for i in permissions:
            if getattr(ntsecuritycon, i) & ace[1] == getattr(ntsecuritycon, i):
                calc_mask |= getattr(ntsecuritycon, i)
                print("    ", i)
        print("  ", "Calculated Check Mask=", hex(calc_mask))
        print("  -SID\n    ", win32security.LookupAccountSid(None, ace[2]))

```


---

## win32/Demos/GetSaveFileName.py

```python
import os

import win32con
import win32gui

filter = "Python Scripts\0*.py;*.pyw;*.pys\0Text files\0*.txt\0"
customfilter = "Other file types\0*.*\0"

fname, customfilter, flags = win32gui.GetSaveFileNameW(
    InitialDir=os.environ["temp"],
    Flags=win32con.OFN_ALLOWMULTISELECT | win32con.OFN_EXPLORER,
    File="somefilename",
    DefExt="py",
    Title="GetSaveFileNameW",
    Filter=filter,
    CustomFilter=customfilter,
    FilterIndex=1,
)

print(f"save file names: {fname!r}")
print(f"filter used: {customfilter!r}")
print(f"Flags: {flags}")
for k, v in win32con.__dict__.items():
    if k.startswith("OFN_") and flags & v:
        print("\t" + k)

fname, customfilter, flags = win32gui.GetOpenFileNameW(
    InitialDir=os.environ["temp"],
    Flags=win32con.OFN_ALLOWMULTISELECT | win32con.OFN_EXPLORER,
    File="somefilename",
    DefExt="py",
    Title="GetOpenFileNameW",
    Filter=filter,
    CustomFilter=customfilter,
    FilterIndex=0,
)

print(f"open file names: {fname!r}")
print(f"filter used: {customfilter!r}")
print(f"Flags: {flags}")
for k, v in win32con.__dict__.items():
    if k.startswith("OFN_") and flags & v:
        print("\t" + k)

```


---

## win32/Demos/NetValidatePasswordPolicy.py

```python
"""A demo of using win32net.NetValidatePasswordPolicy.

Example usage:

% NetValidatePasswordPolicy.py --password=foo change
which might return:

> Result of 'change' validation is 0: The operation completed successfully.

or depending on the policy:

> Result of 'change' validation is 2245: The password does not meet the
> password policy requirements. Check the minimum password length,
> password complexity and password history requirements.

Adding --user doesn't seem to change the output (even the PasswordLastSet seen
when '-f' is used doesn't depend on the username), but theoretically it will
also check the password history for the specified user.

% NetValidatePasswordPolicy.py auth

which always (with and without '-m') seems to return:

> Result of 'auth' validation is 2701: Password must change at next logon
"""

import optparse
import sys
from pprint import pprint

import win32api
import win32net
import win32netcon


def main():
    parser = optparse.OptionParser(
        "%prog [options] auth|change ...",
        description="A win32net.NetValidatePasswordPolicy demo.",
    )

    parser.add_option(
        "-u",
        "--username",
        action="store",
        help="The username to pass to the function (only for the 'change' command)",
    )

    parser.add_option(
        "-p",
        "--password",
        action="store",
        help="The clear-text password to pass to the function "
        "(only for the 'change' command)",
    )

    parser.add_option(
        "-m",
        "--password-matched",
        action="store_false",
        default=True,
        help="Used to specify the password does NOT match (ie, "
        "uses False for the PasswordMatch/PasswordMatched "
        "arg, both 'auth' and 'change' commands)",
    )

    parser.add_option(
        "-s",
        "--server",
        action="store",
        help="The name of the server to execute the command on",
    )

    parser.add_option(
        "-f",
        "--show_fields",
        action="store_true",
        default=False,
        help="Print the NET_VALIDATE_PERSISTED_FIELDS returned",
    )

    options, args = parser.parse_args()

    if not args:
        args = ["auth"]

    for arg in args:
        if arg == "auth":
            input = {
                "PasswordMatched": options.password_matched,
            }
            val_type = win32netcon.NetValidateAuthentication
        elif arg == "change":
            input = {
                "ClearPassword": options.password,
                "PasswordMatch": options.password_matched,
                "UserAccountName": options.username,
            }
            val_type = win32netcon.NetValidatePasswordChange
        else:
            parser.error("Invalid arg - must be 'auth' or 'change'")

        try:
            fields, status = win32net.NetValidatePasswordPolicy(
                options.server, None, val_type, input
            )
        except win32net.error as exc:
            print("NetValidatePasswordPolicy failed: ", exc)
            return 1

        if options.show_fields:
            print("NET_VALIDATE_PERSISTED_FIELDS fields:")
            pprint(fields)

        print(
            f"Result of {arg!r} validation is {status}:",
            win32api.FormatMessage(status).strip(),
        )

    return 0


if __name__ == "__main__":
    sys.exit(main())

```


---

## win32/Demos/OpenEncryptedFileRaw.py

```python
import os

import win32api
import win32file
import winerror


def ReadCallback(input_buffer, data, buflen):
    fnamein, fnameout, f = data
    # print(fnamein, fnameout, buflen)
    f.write(input_buffer)
    return winerror.ERROR_SUCCESS


def WriteCallback(output_buffer, data, buflen):
    fnamebackup, fnameout, f = data
    file_data = f.read(buflen)
    ## returning 0 as len terminates WriteEncryptedFileRaw
    output_len = len(file_data)
    output_buffer[:output_len] = file_data
    return winerror.ERROR_SUCCESS, output_len


tmp_dir = win32api.GetTempPath()
dst_dir = win32api.GetTempFileName(tmp_dir, "oef")[0]
os.remove(dst_dir)
os.mkdir(dst_dir)
print("Destination dir:", dst_dir)

## create an encrypted file
fname = win32api.GetTempFileName(dst_dir, "ref")[0]
print("orig file:", fname)
f = open(fname, "w")
f.write("xxxxxxxxxxxxxxxx\n" * 32768)
f.close()
## add a couple of extra data streams
f = open(fname + ":stream_y", "w")
f.write("yyyyyyyyyyyyyyyy\n" * 32768)
f.close()
f = open(fname + ":stream_z", "w")
f.write("zzzzzzzzzzzzzzzz\n" * 32768)
f.close()
win32file.EncryptFile(fname)

## backup raw data of encrypted file
bkup_fname = win32api.GetTempFileName(dst_dir, "bef")[0]
print("backup file:", bkup_fname)
f = open(bkup_fname, "wb")
ctxt = win32file.OpenEncryptedFileRaw(fname, 0)
try:
    win32file.ReadEncryptedFileRaw(ReadCallback, (fname, bkup_fname, f), ctxt)
finally:
    ## if context is not closed, file remains locked even if calling process is killed
    win32file.CloseEncryptedFileRaw(ctxt)
    f.close()

## restore data from backup to new encrypted file
dst_fname = win32api.GetTempFileName(dst_dir, "wef")[0]
print("restored file:", dst_fname)
f = open(bkup_fname, "rb")
ctxtout = win32file.OpenEncryptedFileRaw(dst_fname, win32file.CREATE_FOR_IMPORT)
try:
    win32file.WriteEncryptedFileRaw(WriteCallback, (bkup_fname, dst_fname, f), ctxtout)
finally:
    win32file.CloseEncryptedFileRaw(ctxtout)
    f.close()

```


---

## win32/Demos/RegCreateKeyTransacted.py

```python
import win32api
import win32con
import win32transaction

keyname = "Pywin32 test transacted registry functions"
subkeyname = "test transacted subkey"
classname = "Transacted Class"

trans = win32transaction.CreateTransaction(Description="test RegCreateKeyTransacted")
key, disp = win32api.RegCreateKeyEx(
    win32con.HKEY_CURRENT_USER,
    keyname,
    samDesired=win32con.KEY_ALL_ACCESS,
    Class=classname,
)
## clean up any existing keys
for subk in win32api.RegEnumKeyExW(key):
    win32api.RegDeleteKey(key, subk[0])

## reopen key in transacted mode
transacted_key = win32api.RegOpenKeyTransacted(
    Key=win32con.HKEY_CURRENT_USER,
    SubKey=keyname,
    Transaction=trans,
    samDesired=win32con.KEY_ALL_ACCESS,
)
subkey, disp = win32api.RegCreateKeyEx(
    transacted_key,
    subkeyname,
    Transaction=trans,
    samDesired=win32con.KEY_ALL_ACCESS,
    Class=classname,
)

## Newly created key should not be visible from non-transacted handle
subkeys = [s[0] for s in win32api.RegEnumKeyExW(key)]
assert subkeyname not in subkeys

transacted_subkeys = [s[0] for s in win32api.RegEnumKeyExW(transacted_key)]
assert subkeyname in transacted_subkeys

## Key should be visible to non-transacted handle after commit
win32transaction.CommitTransaction(trans)
subkeys = [s[0] for s in win32api.RegEnumKeyExW(key)]
assert subkeyname in subkeys

## test transacted delete
del_trans = win32transaction.CreateTransaction(
    Description="test RegDeleteKeyTransacted"
)
win32api.RegDeleteKeyEx(key, subkeyname, Transaction=del_trans)
## subkey should still show up for non-transacted handle
subkeys = [s[0] for s in win32api.RegEnumKeyExW(key)]
assert subkeyname in subkeys
## ... and should be gone after commit
win32transaction.CommitTransaction(del_trans)
subkeys = [s[0] for s in win32api.RegEnumKeyExW(key)]
assert subkeyname not in subkeys

win32api.RegDeleteKey(win32con.HKEY_CURRENT_USER, keyname)

```


---

## win32/Demos/RegRestoreKey.py

```python
import os

import ntsecuritycon
import win32api
import win32con
import win32security
import winnt

temp_dir = win32api.GetTempPath()
fname = win32api.GetTempFileName(temp_dir, "rsk")[0]
print(fname)
## file can't exist
os.remove(fname)

## enable backup and restore privs
required_privs = (
    (
        win32security.LookupPrivilegeValue("", ntsecuritycon.SE_BACKUP_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
    (
        win32security.LookupPrivilegeValue("", ntsecuritycon.SE_RESTORE_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
)
ph = win32api.GetCurrentProcess()
th = win32security.OpenProcessToken(
    ph, win32con.TOKEN_READ | win32con.TOKEN_ADJUST_PRIVILEGES
)
adjusted_privs = win32security.AdjustTokenPrivileges(th, 0, required_privs)

try:
    sa = win32security.SECURITY_ATTRIBUTES()
    my_sid = win32security.GetTokenInformation(th, ntsecuritycon.TokenUser)[0]
    sa.SECURITY_DESCRIPTOR.SetSecurityDescriptorOwner(my_sid, 0)

    k, disp = win32api.RegCreateKeyEx(
        win32con.HKEY_CURRENT_USER,
        "Python test key",
        SecurityAttributes=sa,
        samDesired=win32con.KEY_ALL_ACCESS,
        Class="some class",
        Options=0,
    )
    win32api.RegSetValue(k, None, win32con.REG_SZ, "Default value for python test key")

    subk, disp = win32api.RegCreateKeyEx(
        k,
        "python test subkey",
        SecurityAttributes=sa,
        samDesired=win32con.KEY_ALL_ACCESS,
        Class="some other class",
        Options=0,
    )
    win32api.RegSetValue(subk, None, win32con.REG_SZ, "Default value for subkey")

    win32api.RegSaveKeyEx(
        k, fname, Flags=winnt.REG_STANDARD_FORMAT, SecurityAttributes=sa
    )

    restored_key, disp = win32api.RegCreateKeyEx(
        win32con.HKEY_CURRENT_USER,
        "Python test key(restored)",
        SecurityAttributes=sa,
        samDesired=win32con.KEY_ALL_ACCESS,
        Class="restored class",
        Options=0,
    )
    win32api.RegRestoreKey(restored_key, fname)
finally:
    win32security.AdjustTokenPrivileges(th, 0, adjusted_privs)

```


---

## win32/Demos/SystemParametersInfo.py

```python
import glob
import os
import time

import win32api
import win32con
import win32gui

for pname in (
    ## Set actions all take an unsigned int in pvParam
    "SPI_GETMOUSESPEED",
    "SPI_GETACTIVEWNDTRKTIMEOUT",
    "SPI_GETCARETWIDTH",
    "SPI_GETFOREGROUNDFLASHCOUNT",
    "SPI_GETFOREGROUNDLOCKTIMEOUT",
    ## Set actions all take an unsigned int in uiParam
    "SPI_GETWHEELSCROLLLINES",
    "SPI_GETKEYBOARDDELAY",
    "SPI_GETKEYBOARDSPEED",
    "SPI_GETMOUSEHOVERHEIGHT",
    "SPI_GETMOUSEHOVERWIDTH",
    "SPI_GETMOUSEHOVERTIME",
    "SPI_GETSCREENSAVETIMEOUT",
    "SPI_GETMENUSHOWDELAY",
    "SPI_GETBORDER",
    "SPI_GETFONTSMOOTHINGCONTRAST",
    "SPI_GETFONTSMOOTHINGTYPE",
    "SPI_GETFOCUSBORDERHEIGHT",
    "SPI_GETFOCUSBORDERWIDTH",
    "SPI_GETMOUSECLICKLOCKTIME",
):
    print(pname)
    cget = getattr(win32con, pname)
    cset = getattr(win32con, pname.replace("_GET", "_SET"))
    orig_value = win32gui.SystemParametersInfo(cget)
    print("\toriginal setting:", orig_value)
    # Some values are clamped to an upper bound
    # (like SPI_SETKEYBOARDDELAY, SPI_SETKEYBOARDSPEED, SPI_SETMOUSESPEED)
    # SPI_SETMOUSESPEED specifically ranges [0-3]
    # https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-systemparametersinfoa#SPI_SETKEYBOARDDELAY
    # Some values won't accept 0
    new_value = orig_value + (1 if orig_value < 2 else -1)
    win32gui.SystemParametersInfo(cset, new_value)
    new_value = win32gui.SystemParametersInfo(cget)
    print("\tnew value:", new_value)
    assert new_value != orig_value
    win32gui.SystemParametersInfo(cset, orig_value)
    assert win32gui.SystemParametersInfo(cget) == orig_value


# change to opposite, check that it was changed and change back
for pname in (
    # these take a boolean value in pvParam
    "SPI_GETFLATMENU",
    "SPI_GETDROPSHADOW",
    "SPI_GETKEYBOARDCUES",
    "SPI_GETMENUFADE",
    "SPI_GETCOMBOBOXANIMATION",
    "SPI_GETCURSORSHADOW",
    "SPI_GETGRADIENTCAPTIONS",
    "SPI_GETHOTTRACKING",
    "SPI_GETLISTBOXSMOOTHSCROLLING",
    "SPI_GETMENUANIMATION",
    "SPI_GETSELECTIONFADE",
    "SPI_GETTOOLTIPANIMATION",
    "SPI_GETTOOLTIPFADE",
    "SPI_GETUIEFFECTS",
    "SPI_GETACTIVEWINDOWTRACKING",
    "SPI_GETACTIVEWNDTRKZORDER",
    # these take a boolean in uiParam
    "SPI_GETFONTSMOOTHING",
    "SPI_GETICONTITLEWRAP",
    "SPI_GETBEEP",
    "SPI_GETBLOCKSENDINPUTRESETS",
    "SPI_GETKEYBOARDPREF",
    "SPI_GETMENUDROPALIGNMENT",
    "SPI_GETDRAGFULLWINDOWS",
    "SPI_GETSHOWIMEUI",
    # Can be changed, but will always return True,
    # so don't include in demo since we can't know the value to revert
    # https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-systemparametersinfoa#SPI_GETSCREENSAVEACTIVE
    # "SPI_GETSCREENSAVEACTIVE",
):
    print(pname)
    cget = getattr(win32con, pname)
    cset = getattr(win32con, pname.replace("_GET", "_SET"))
    orig_value = win32gui.SystemParametersInfo(cget)
    print(orig_value)
    win32gui.SystemParametersInfo(cset, not orig_value)
    new_value = win32gui.SystemParametersInfo(cget)
    print(new_value)
    assert orig_value != new_value
    win32gui.SystemParametersInfo(cset, orig_value)
    assert win32gui.SystemParametersInfo(cget) == orig_value


print("SPI_GETICONTITLELOGFONT")
lf = win32gui.SystemParametersInfo(win32con.SPI_GETICONTITLELOGFONT)
orig_height = lf.lfHeight
orig_italic = lf.lfItalic
print("Height:", orig_height, "Italic:", orig_italic)
lf.lfHeight += 2
lf.lfItalic = not lf.lfItalic
win32gui.SystemParametersInfo(win32con.SPI_SETICONTITLELOGFONT, lf)
new_lf = win32gui.SystemParametersInfo(win32con.SPI_GETICONTITLELOGFONT)
print("New Height:", new_lf.lfHeight, "New Italic:", new_lf.lfItalic)
assert new_lf.lfHeight == orig_height + 2
assert new_lf.lfItalic != orig_italic

lf.lfHeight = orig_height
lf.lfItalic = orig_italic
win32gui.SystemParametersInfo(win32con.SPI_SETICONTITLELOGFONT, lf)
new_lf = win32gui.SystemParametersInfo(win32con.SPI_GETICONTITLELOGFONT)
assert new_lf.lfHeight == orig_height
assert new_lf.lfItalic == orig_italic


print("SPI_GETMOUSEHOVERWIDTH, SPI_GETMOUSEHOVERHEIGHT, SPI_GETMOUSEHOVERTIME")
w = win32gui.SystemParametersInfo(win32con.SPI_GETMOUSEHOVERWIDTH)
h = win32gui.SystemParametersInfo(win32con.SPI_GETMOUSEHOVERHEIGHT)
t = win32gui.SystemParametersInfo(win32con.SPI_GETMOUSEHOVERTIME)
print("w,h,t:", w, h, t)

win32gui.SystemParametersInfo(win32con.SPI_SETMOUSEHOVERWIDTH, w + 1)
win32gui.SystemParametersInfo(win32con.SPI_SETMOUSEHOVERHEIGHT, h + 2)
win32gui.SystemParametersInfo(win32con.SPI_SETMOUSEHOVERTIME, t + 3)
new_w = win32gui.SystemParametersInfo(win32con.SPI_GETMOUSEHOVERWIDTH)
new_h = win32gui.SystemParametersInfo(win32con.SPI_GETMOUSEHOVERHEIGHT)
new_t = win32gui.SystemParametersInfo(win32con.SPI_GETMOUSEHOVERTIME)
print("new w,h,t:", new_w, new_h, new_t)
assert new_w == w + 1
assert new_h == h + 2
assert new_t == t + 3

win32gui.SystemParametersInfo(win32con.SPI_SETMOUSEHOVERWIDTH, w)
win32gui.SystemParametersInfo(win32con.SPI_SETMOUSEHOVERHEIGHT, h)
win32gui.SystemParametersInfo(win32con.SPI_SETMOUSEHOVERTIME, t)
new_w = win32gui.SystemParametersInfo(win32con.SPI_GETMOUSEHOVERWIDTH)
new_h = win32gui.SystemParametersInfo(win32con.SPI_GETMOUSEHOVERHEIGHT)
new_t = win32gui.SystemParametersInfo(win32con.SPI_GETMOUSEHOVERTIME)
assert new_w == w
assert new_h == h
assert new_t == t


print("SPI_SETDOUBLECLKWIDTH, SPI_SETDOUBLECLKHEIGHT")
x = win32api.GetSystemMetrics(win32con.SM_CXDOUBLECLK)
y = win32api.GetSystemMetrics(win32con.SM_CYDOUBLECLK)
print("x,y:", x, y)
win32gui.SystemParametersInfo(win32con.SPI_SETDOUBLECLKWIDTH, x + 1)
win32gui.SystemParametersInfo(win32con.SPI_SETDOUBLECLKHEIGHT, y + 2)
new_x = win32api.GetSystemMetrics(win32con.SM_CXDOUBLECLK)
new_y = win32api.GetSystemMetrics(win32con.SM_CYDOUBLECLK)
print("new x,y:", new_x, new_y)
assert new_x == x + 1
assert new_y == y + 2
win32gui.SystemParametersInfo(win32con.SPI_SETDOUBLECLKWIDTH, x)
win32gui.SystemParametersInfo(win32con.SPI_SETDOUBLECLKHEIGHT, y)
new_x = win32api.GetSystemMetrics(win32con.SM_CXDOUBLECLK)
new_y = win32api.GetSystemMetrics(win32con.SM_CYDOUBLECLK)
assert new_x == x
assert new_y == y


print("SPI_SETDRAGWIDTH, SPI_SETDRAGHEIGHT")
dw = win32api.GetSystemMetrics(win32con.SM_CXDRAG)
dh = win32api.GetSystemMetrics(win32con.SM_CYDRAG)
print("dw,dh:", dw, dh)
win32gui.SystemParametersInfo(win32con.SPI_SETDRAGWIDTH, dw + 1)
win32gui.SystemParametersInfo(win32con.SPI_SETDRAGHEIGHT, dh + 2)
new_dw = win32api.GetSystemMetrics(win32con.SM_CXDRAG)
new_dh = win32api.GetSystemMetrics(win32con.SM_CYDRAG)
print("new dw,dh:", new_dw, new_dh)
assert new_dw == dw + 1
assert new_dh == dh + 2
win32gui.SystemParametersInfo(win32con.SPI_SETDRAGWIDTH, dw)
win32gui.SystemParametersInfo(win32con.SPI_SETDRAGHEIGHT, dh)
new_dw = win32api.GetSystemMetrics(win32con.SM_CXDRAG)
new_dh = win32api.GetSystemMetrics(win32con.SM_CYDRAG)
assert new_dw == dw
assert new_dh == dh


orig_wallpaper = win32gui.SystemParametersInfo(Action=win32con.SPI_GETDESKWALLPAPER)
print("Original: ", orig_wallpaper)
for bmp in glob.glob(os.path.join(os.environ["windir"], "*.bmp")):
    print(bmp)
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, Param=bmp)
    print(win32gui.SystemParametersInfo(Action=win32con.SPI_GETDESKWALLPAPER))
    time.sleep(1)

win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, Param=orig_wallpaper)

```


---

## win32/Demos/c_extension/setup.py

```python
# A sample distutils script to show to build your own
# extension module which extends pywintypes or pythoncom.
#
# Use 'python -m build' to build this extension.
import os
from setuptools import Extension, setup
from sysconfig import get_paths

sources = ["win32_extension.cpp"]
lib_dir = get_paths()["platlib"]

# Specify the directory where the PyWin32 .h and .lib files are installed.
# If you are doing a win32com extension, you will also need to add
# win32com\Include and win32com\Libs.
ext = Extension(
    "win32_extension",
    sources,
    include_dirs=[os.path.join(lib_dir, "win32", "include")],
    library_dirs=[os.path.join(lib_dir, "win32", "libs")],
)

setup(
    name="win32 extension sample",
    version="0.1",
    ext_modules=[ext],
)

```


---

## win32/Demos/dde/ddeclient.py

```python
# 'Request' example added jjk  11/20/98

import win32ui  # isort: skip # Must be imported before dde !
import dde

server = dde.CreateServer()
server.Create("TestClient")

conversation = dde.CreateConversation(server)

conversation.ConnectTo("RunAny", "RunAnyCommand")
conversation.Exec("DoSomething")
conversation.Exec("DoSomethingElse")

conversation.ConnectTo("RunAny", "ComputeStringLength")
s = "abcdefghi"
sl = conversation.Request(s)
print(f'length of "{s}" is {sl}')

```


---

## win32/Demos/dde/ddeserver.py

```python
# 'Request' example added jjk  11/20/98

import win32ui  # isort: skip # Must be imported before dde !
import dde
from pywin.mfc import object


class MySystemTopic(object.Object):
    def __init__(self):
        object.Object.__init__(self, dde.CreateServerSystemTopic())

    def Exec(self, cmd):
        print("System Topic asked to exec", cmd)


class MyOtherTopic(object.Object):
    def __init__(self, topicName):
        object.Object.__init__(self, dde.CreateTopic(topicName))

    def Exec(self, cmd):
        print("Other Topic asked to exec", cmd)


class MyRequestTopic(object.Object):
    def __init__(self, topicName):
        topic = dde.CreateTopic(topicName)
        topic.AddItem(dde.CreateStringItem(""))
        object.Object.__init__(self, topic)

    def Request(self, aString):
        print("Request Topic asked to compute length of:", aString)
        return str(len(aString))


server = dde.CreateServer()
server.AddTopic(MySystemTopic())
server.AddTopic(MyOtherTopic("RunAnyCommand"))
server.AddTopic(MyRequestTopic("ComputeStringLength"))
server.Create("RunAny")

while 1:
    win32ui.PumpWaitingMessages(0, -1)

```


---

## win32/Demos/desktopmanager.py

```python
# Demonstrates using a taskbar icon to create and navigate between desktops

import _thread
import io
import time
import traceback

import pywintypes
import win32api
import win32con
import win32gui
import win32process
import win32service

## "Shell_TrayWnd" is class of system tray window, broadcasts "TaskbarCreated" when initialized


def desktop_name_dlgproc(hwnd, msg, wparam, lparam):
    """Handles messages from the desktop name dialog box"""
    if msg in (win32con.WM_CLOSE, win32con.WM_DESTROY):
        win32gui.DestroyWindow(hwnd)
    elif msg == win32con.WM_COMMAND:
        if wparam == win32con.IDOK:
            desktop_name = win32gui.GetDlgItemText(hwnd, 72)
            print("new desktop name: ", desktop_name)
            win32gui.DestroyWindow(hwnd)
            create_desktop(desktop_name)

        elif wparam == win32con.IDCANCEL:
            win32gui.DestroyWindow(hwnd)


def get_new_desktop_name(parent_hwnd):
    """Create a dialog box to ask the user for name of desktop to be created"""
    msgs = {
        win32con.WM_COMMAND: desktop_name_dlgproc,
        win32con.WM_CLOSE: desktop_name_dlgproc,
        win32con.WM_DESTROY: desktop_name_dlgproc,
    }
    # dlg item [type, caption, id, (x,y,cx,cy), style, ex style
    style = (
        win32con.WS_BORDER
        | win32con.WS_VISIBLE
        | win32con.WS_CAPTION
        | win32con.WS_SYSMENU
    )  ## |win32con.DS_SYSMODAL
    h = win32gui.CreateDialogIndirect(
        win32api.GetModuleHandle(None),
        [
            ["One ugly dialog box !", (100, 100, 200, 100), style, 0],
            [
                "Button",
                "Create",
                win32con.IDOK,
                (10, 10, 30, 20),
                win32con.WS_VISIBLE
                | win32con.WS_TABSTOP
                | win32con.BS_HOLLOW
                | win32con.BS_DEFPUSHBUTTON,
            ],
            [
                "Button",
                "Never mind",
                win32con.IDCANCEL,
                (45, 10, 50, 20),
                win32con.WS_VISIBLE | win32con.WS_TABSTOP | win32con.BS_HOLLOW,
            ],
            ["Static", "Desktop name:", 71, (10, 40, 70, 10), win32con.WS_VISIBLE],
            ["Edit", "", 72, (75, 40, 90, 10), win32con.WS_VISIBLE],
        ],
        parent_hwnd,
        msgs,
    )  ## parent_hwnd, msgs)

    win32gui.EnableWindow(h, True)
    hcontrol = win32gui.GetDlgItem(h, 72)
    win32gui.EnableWindow(hcontrol, True)
    win32gui.SetFocus(hcontrol)


def new_icon(hdesk, desktop_name):
    """Runs as a thread on each desktop to create a new tray icon and handle its messages"""
    global id
    id += 1
    hdesk.SetThreadDesktop()
    ## apparently the threads can't use same hinst, so each needs its own window class
    windowclassname = "PythonDesktopManager" + desktop_name
    wc = win32gui.WNDCLASS()
    wc.hInstance = win32api.GetModuleHandle(None)
    wc.lpszClassName = windowclassname
    wc.style = win32con.CS_VREDRAW | win32con.CS_HREDRAW | win32con.CS_GLOBALCLASS
    wc.hCursor = win32gui.LoadCursor(0, win32con.IDC_ARROW)
    wc.hbrBackground = win32con.COLOR_WINDOW
    wc.lpfnWndProc = icon_wndproc
    windowclass = win32gui.RegisterClass(wc)
    style = win32con.WS_OVERLAPPED | win32con.WS_SYSMENU
    hwnd = win32gui.CreateWindow(
        windowclass,
        "dm_" + desktop_name,
        win32con.WS_SYSMENU,
        0,
        0,
        win32con.CW_USEDEFAULT,
        win32con.CW_USEDEFAULT,
        0,
        0,
        wc.hInstance,
        None,
    )
    win32gui.UpdateWindow(hwnd)
    flags = win32gui.NIF_ICON | win32gui.NIF_MESSAGE | win32gui.NIF_TIP
    notify_info = (
        hwnd,
        id,
        flags,
        win32con.WM_USER + 20,
        hicon,
        "Desktop Manager (%s)" % desktop_name,
    )
    window_info[hwnd] = notify_info
    ## wait for explorer to initialize system tray for new desktop
    tray_found = 0
    while not tray_found:
        try:
            tray_found = win32gui.FindWindow("Shell_TrayWnd", None)
        except win32gui.error:
            traceback.print_exc
            time.sleep(0.5)
    win32gui.Shell_NotifyIcon(win32gui.NIM_ADD, notify_info)
    win32gui.PumpMessages()


def create_desktop(desktop_name, start_explorer=1):
    """Creates a new desktop and spawns a thread running on it
    Will also start a new icon thread on an existing desktop
    """
    sa = pywintypes.SECURITY_ATTRIBUTES()
    sa.bInheritHandle = 1

    try:
        hdesk = win32service.CreateDesktop(
            desktop_name, 0, win32con.MAXIMUM_ALLOWED, sa
        )
    except win32service.error:
        traceback.print_exc()
        errbuf = io.StringIO()
        traceback.print_exc(None, errbuf)
        win32api.MessageBox(0, errbuf.getvalue(), "Desktop creation failed")
        return
    if start_explorer:
        s = win32process.STARTUPINFO()
        s.lpDesktop = desktop_name
        prc_info = win32process.CreateProcess(
            None,
            "Explorer.exe",
            None,
            None,
            True,
            win32con.CREATE_NEW_CONSOLE,
            None,
            "c:\\",
            s,
        )

    th = _thread.start_new_thread(new_icon, (hdesk, desktop_name))
    hdesk.SwitchDesktop()


def icon_wndproc(hwnd, msg, wp, lp):
    """Window proc for the tray icons"""
    if lp == win32con.WM_LBUTTONDOWN:
        ## popup menu won't disappear if you don't do this
        win32gui.SetForegroundWindow(hwnd)

        curr_desktop = win32service.OpenInputDesktop(0, True, win32con.MAXIMUM_ALLOWED)
        curr_desktop_name = win32service.GetUserObjectInformation(
            curr_desktop, win32con.UOI_NAME
        )
        winsta = win32service.GetProcessWindowStation()
        desktops = winsta.EnumDesktops()
        m = win32gui.CreatePopupMenu()
        desktop_cnt = len(desktops)
        ## *don't* create an item 0
        for d in range(1, desktop_cnt + 1):
            mf_flags = win32con.MF_STRING
            ## if you switch to winlogon yourself, there's nothing there and you're stuck
            if desktops[d - 1].lower() in ("winlogon", "disconnect"):
                mf_flags |= win32con.MF_GRAYED | win32con.MF_DISABLED
            if desktops[d - 1] == curr_desktop_name:
                mf_flags |= win32con.MF_CHECKED
            win32gui.AppendMenu(m, mf_flags, d, desktops[d - 1])
        win32gui.AppendMenu(m, win32con.MF_STRING, desktop_cnt + 1, "Create new ...")
        win32gui.AppendMenu(m, win32con.MF_STRING, desktop_cnt + 2, "Exit")

        x, y = win32gui.GetCursorPos()
        d = win32gui.TrackPopupMenu(
            m,
            win32con.TPM_LEFTBUTTON | win32con.TPM_RETURNCMD | win32con.TPM_NONOTIFY,
            x,
            y,
            0,
            hwnd,
            None,
        )
        win32gui.PumpWaitingMessages()
        win32gui.DestroyMenu(m)
        if d == desktop_cnt + 1:  ## Create new
            get_new_desktop_name(hwnd)
        elif d == desktop_cnt + 2:  ## Exit
            win32gui.PostQuitMessage(0)
            win32gui.Shell_NotifyIcon(win32gui.NIM_DELETE, window_info[hwnd])
            del window_info[hwnd]
            origin_desktop.SwitchDesktop()
        elif d > 0:
            hdesk = win32service.OpenDesktop(
                desktops[d - 1], 0, 0, win32con.MAXIMUM_ALLOWED
            )
            hdesk.SwitchDesktop()
        return 0
    else:
        return win32gui.DefWindowProc(hwnd, msg, wp, lp)


window_info = {}
origin_desktop = win32service.OpenInputDesktop(0, True, win32con.MAXIMUM_ALLOWED)
origin_desktop_name = win32service.GetUserObjectInformation(
    origin_desktop, win32service.UOI_NAME
)

hinst = win32api.GetModuleHandle(None)
try:
    hicon = win32gui.LoadIcon(hinst, 1)  ## python.exe and pythonw.exe
except win32gui.error:
    hicon = win32gui.LoadIcon(hinst, 135)  ## pythonwin's icon
id = 0

create_desktop(str(origin_desktop_name), 0)

## wait for first thread to initialize its icon
while not window_info:
    time.sleep(1)

## exit when last tray icon goes away
while window_info:
    win32gui.PumpWaitingMessages()
    time.sleep(3)

```


---

## win32/Demos/eventLogDemo.py

```python
import win32api  # To translate NT Sids to account names.
import win32con
import win32evtlog
import win32evtlogutil
import win32security


def ReadLog(computer, logType="Application", dumpEachRecord=0):
    # read the entire log back.
    h = win32evtlog.OpenEventLog(computer, logType)
    numRecords = win32evtlog.GetNumberOfEventLogRecords(h)
    # print(f"There are {numRecords} records")

    num = 0
    while 1:
        objects = win32evtlog.ReadEventLog(
            h,
            win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ,
            0,
        )
        if not objects:
            break
        for object in objects:
            # get it for testing purposes, but don't print it.
            msg = win32evtlogutil.SafeFormatMessage(object, logType)
            if object.Sid is not None:
                try:
                    domain, user, typ = win32security.LookupAccountSid(
                        computer, object.Sid
                    )
                    sidDesc = f"{domain}/{user}"
                except win32security.error:
                    sidDesc = str(object.Sid)
                user_desc = f"Event associated with user {sidDesc}"
            else:
                user_desc = None
            if dumpEachRecord:
                print(
                    "Event record from {!r} generated at {}".format(
                        object.SourceName, object.TimeGenerated.Format()
                    )
                )
                if user_desc:
                    print(user_desc)
                try:
                    print(msg)
                except UnicodeError:
                    print("(unicode error printing message: repr() follows...)")
                    print(repr(msg))

        num += len(objects)

    if numRecords == num:
        print("Successfully read all", numRecords, "records")
    else:
        print(
            "Couldn't get all records - reported %d, but found %d" % (numRecords, num)
        )
        print(
            "(Note that some other app may have written records while we were running!)"
        )
    win32evtlog.CloseEventLog(h)


def usage():
    print("Writes an event to the event log.")
    print("-w : Don't write any test records.")
    print("-r : Don't read the event log")
    print("-c : computerName : Process the log on the specified computer")
    print("-v : Verbose")
    print("-t : LogType - Use the specified log - default = 'Application'")


def test():
    import getopt
    import sys

    opts, args = getopt.getopt(sys.argv[1:], "rwh?c:t:v")
    computer = None
    do_read = do_write = 1

    logType = "Application"
    verbose = 0

    if len(args) > 0:
        print("Invalid args")
        usage()
        return 1
    for opt, val in opts:
        if opt == "-t":
            logType = val
        if opt == "-c":
            computer = val
        if opt in ["-h", "-?"]:
            usage()
            return
        if opt == "-r":
            do_read = 0
        if opt == "-w":
            do_write = 0
        if opt == "-v":
            verbose += 1
    if do_write:
        ph = win32api.GetCurrentProcess()
        th = win32security.OpenProcessToken(ph, win32con.TOKEN_READ)
        my_sid = win32security.GetTokenInformation(th, win32security.TokenUser)[0]

        win32evtlogutil.ReportEvent(
            logType,
            2,
            strings=["The message text for event 2", "Another insert"],
            data=b"Raw\0Data",
            sid=my_sid,
        )
        win32evtlogutil.ReportEvent(
            logType,
            1,
            eventType=win32evtlog.EVENTLOG_WARNING_TYPE,
            strings=["A warning", "An even more dire warning"],
            data=b"Raw\0Data",
            sid=my_sid,
        )
        win32evtlogutil.ReportEvent(
            logType,
            1,
            eventType=win32evtlog.EVENTLOG_INFORMATION_TYPE,
            strings=["An info", "Too much info"],
            data=b"Raw\0Data",
            sid=my_sid,
        )
        print("Successfully wrote 3 records to the log")

    if do_read:
        ReadLog(computer, logType, verbose > 0)


if __name__ == "__main__":
    test()

```


---

## win32/Demos/getfilever.py

```python
import os

import win32api

ver_strings = (
    "Comments",
    "InternalName",
    "ProductName",
    "CompanyName",
    "LegalCopyright",
    "ProductVersion",
    "FileDescription",
    "LegalTrademarks",
    "PrivateBuild",
    "FileVersion",
    "OriginalFilename",
    "SpecialBuild",
)
fname = os.environ["comspec"]
d = win32api.GetFileVersionInfo(fname, "\\")
## backslash as parm returns dictionary of numeric info corresponding to VS_FIXEDFILEINFO struc
for n, v in d.items():
    print(n, v)

pairs = win32api.GetFileVersionInfo(fname, "\\VarFileInfo\\Translation")
## \VarFileInfo\Translation returns list of available (language, codepage) pairs that can be used to retreive string info
## any other must be of the form \StringfileInfo\%04X%04X\parm_name, middle two are language/codepage pair returned from above
for lang, codepage in pairs:
    print("lang:", lang, "codepage:", codepage)
    for ver_string in ver_strings:
        str_info = f"\\StringFileInfo\\{lang:04X}{codepage:04X}\\{ver_string}"
        # print(str_inf)
        print(ver_string, repr(win32api.GetFileVersionInfo(fname, str_info)))

```


---

## win32/Demos/mmapfile_demo.py

```python
import os
import tempfile

import mmapfile
import win32api
import winerror

system_info = win32api.GetSystemInfo()
page_size = system_info[1]
alloc_size = system_info[7]

fname = tempfile.mktemp()
mapping_name = os.path.split(fname)[1]
fsize = 8 * page_size
print(fname, fsize, mapping_name)

m1 = mmapfile.mmapfile(File=fname, Name=mapping_name, MaximumSize=fsize)
m1.seek(100)
m1.write_byte(b"?")
m1.seek(-1, 1)
assert m1.read_byte() == b"?"

## A reopened named mapping should have exact same size as original mapping
m2 = mmapfile.mmapfile(Name=mapping_name, File=None, MaximumSize=fsize * 2)
assert m2.size() == m1.size()
m1.seek(0, 0)
m1.write(fsize * b"s")
assert m2.read(fsize) == fsize * b"s"

move_src = 100
move_dest = 500
move_size = 150

m2.seek(move_src, 0)
assert m2.tell() == move_src
m2.write(b"m" * move_size)
m2.move(move_dest, move_src, move_size)
m2.seek(move_dest, 0)
assert m2.read(move_size) == b"m" * move_size
##    m2.write('x'* (fsize+1))

m2.close()
m1.resize(fsize * 2)
assert m1.size() == fsize * 2
m1.seek(fsize)
m1.write(b"w" * fsize)
m1.flush()
m1.close()
os.remove(fname)


## Test a file with size larger than 32 bits
## need 10 GB free on drive where your temp folder lives
fname_large = tempfile.mktemp()
mapping_name = "Pywin32_large_mmap"
offsetdata = b"This is start of offset"

## Deliberately use odd numbers to test rounding logic
fsize = (1024 * 1024 * 1024 * 10) + 333
offset = (1024 * 1024 * 32) + 42
view_size = (1024 * 1024 * 16) + 111

## round mapping size and view size up to multiple of system page size
if fsize % page_size:
    fsize += page_size - (fsize % page_size)
if view_size % page_size:
    view_size += page_size - (view_size % page_size)
## round offset down to multiple of allocation granularity
offset -= offset % alloc_size

m1 = None
m2 = None
try:
    try:
        m1 = mmapfile.mmapfile(fname_large, mapping_name, fsize, 0, offset * 2)
    except mmapfile.error as exc:
        # if we don't have enough disk-space, that's OK.
        if exc.winerror != winerror.ERROR_DISK_FULL:
            raise
        print("skipping large file test - need", fsize, "available bytes.")
    else:
        m1.seek(offset)
        m1.write(offsetdata)

        ## When reopening an existing mapping without passing a file handle, you have
        ##  to specify a positive size even though it's ignored
        m2 = mmapfile.mmapfile(
            File=None,
            Name=mapping_name,
            MaximumSize=1,
            FileOffset=offset,
            NumberOfBytesToMap=view_size,
        )
        assert m2.read(len(offsetdata)) == offsetdata
finally:
    if m1 is not None:
        m1.close()
    if m2 is not None:
        m2.close()
    if os.path.exists(fname_large):
        os.remove(fname_large)

```


---

## win32/Demos/pipes/cat.py

```python
"""cat.py
a version of unix cat, tweaked to show off runproc.py
"""

import sys

data = sys.stdin.read(1)
sys.stdout.write(data)
sys.stdout.flush()
while data:
    data = sys.stdin.read(1)
    sys.stdout.write(data)
    sys.stdout.flush()
# Just here to have something to read from stderr.
sys.stderr.write("Blah...")

# end of cat.py

```


---

## win32/Demos/pipes/runproc.py

```python
"""runproc.py

start a process with three inherited pipes.
Try to write to and read from those.
"""

import msvcrt
import os

import win32api
import win32con
import win32file
import win32pipe
import win32process
import win32security


class Process:
    def run(self, cmdline):
        # security attributes for pipes
        sAttrs = win32security.SECURITY_ATTRIBUTES()
        sAttrs.bInheritHandle = 1

        # create pipes
        hStdin_r, self.hStdin_w = win32pipe.CreatePipe(sAttrs, 0)
        self.hStdout_r, hStdout_w = win32pipe.CreatePipe(sAttrs, 0)
        self.hStderr_r, hStderr_w = win32pipe.CreatePipe(sAttrs, 0)

        # set the info structure for the new process.
        StartupInfo = win32process.STARTUPINFO()
        StartupInfo.hStdInput = hStdin_r
        StartupInfo.hStdOutput = hStdout_w
        StartupInfo.hStdError = hStderr_w
        StartupInfo.dwFlags = win32process.STARTF_USESTDHANDLES
        # Mark doesn't support wShowWindow yet.
        # StartupInfo.dwFlags = StartupInfo.dwFlags | win32process.STARTF_USESHOWWINDOW
        # StartupInfo.wShowWindow = win32con.SW_HIDE

        # Create new output read handles and the input write handle. Set
        # the inheritance properties to FALSE. Otherwise, the child inherits
        # the these handles; resulting in non-closeable handles to the pipes
        # being created.
        pid = win32api.GetCurrentProcess()

        tmp = win32api.DuplicateHandle(
            pid,
            self.hStdin_w,
            pid,
            0,
            0,  # non-inheritable!!
            win32con.DUPLICATE_SAME_ACCESS,
        )
        # Close the inhertible version of the handle
        win32file.CloseHandle(self.hStdin_w)
        self.hStdin_w = tmp
        tmp = win32api.DuplicateHandle(
            pid,
            self.hStdout_r,
            pid,
            0,
            0,  # non-inheritable!
            win32con.DUPLICATE_SAME_ACCESS,
        )
        # Close the inhertible version of the handle
        win32file.CloseHandle(self.hStdout_r)
        self.hStdout_r = tmp

        # start the process.
        hProcess, hThread, dwPid, dwTid = win32process.CreateProcess(
            None,  # program
            cmdline,  # command line
            None,  # process security attributes
            None,  # thread attributes
            1,  # inherit handles, or USESTDHANDLES won't work.
            # creation flags. Don't access the console.
            0,  # Don't need anything here.
            # If you're in a GUI app, you should use
            # CREATE_NEW_CONSOLE here, or any subprocesses
            # might fall victim to the problem described in:
            # KB article: Q156755, cmd.exe requires
            # an NT console in order to perform redirection..
            None,  # no new environment
            None,  # current directory (stay where we are)
            StartupInfo,
        )
        # normally, we would save the pid etc. here...

        # Child is launched. Close the parents copy of those pipe handles
        # that only the child should have open.
        # You need to make sure that no handles to the write end of the
        # output pipe are maintained in this process or else the pipe will
        # not close when the child process exits and the ReadFile will hang.
        win32file.CloseHandle(hStderr_w)
        win32file.CloseHandle(hStdout_w)
        win32file.CloseHandle(hStdin_r)

        self.stdin = os.fdopen(msvcrt.open_osfhandle(self.hStdin_w, 0), "wb")
        self.stdin.write("hmmmmm\r\n")
        self.stdin.flush()
        self.stdin.close()

        self.stdout = os.fdopen(msvcrt.open_osfhandle(self.hStdout_r, 0), "rb")
        print(f"Read on stdout: {self.stdout.read()!r}")

        self.stderr = os.fdopen(msvcrt.open_osfhandle(self.hStderr_r, 0), "rb")
        print(f"Read on stderr: {self.stderr.read()!r}")


if __name__ == "__main__":
    p = Process()
    exe = win32api.GetModuleFileName(0)
    p.run(exe + " cat.py")

# end of runproc.py

```


---

## win32/Demos/print_desktop.py

```python
import pywintypes
import win32api
import win32con
import win32gui
import win32print

pname = win32print.GetDefaultPrinter()
print(pname)
p = win32print.OpenPrinter(pname)
print("Printer handle: ", p)
print_processor = win32print.GetPrinter(p, 2)["pPrintProcessor"]
## call with last parm set to 0 to get total size needed for printer's DEVMODE
dmsize = win32print.DocumentProperties(0, p, pname, None, None, 0)
## dmDriverExtra should be total size - fixed size
driverextra = (
    dmsize - pywintypes.DEVMODEType().Size
)  ## need a better way to get DEVMODE.dmSize
dm = pywintypes.DEVMODEType(driverextra)
dm.Fields = dm.Fields | win32con.DM_ORIENTATION | win32con.DM_COPIES
dm.Orientation = win32con.DMORIENT_LANDSCAPE
dm.Copies = 2
win32print.DocumentProperties(
    0, p, pname, dm, dm, win32con.DM_IN_BUFFER | win32con.DM_OUT_BUFFER
)

pDC = win32gui.CreateDC(print_processor, pname, dm)
printerwidth = win32print.GetDeviceCaps(pDC, win32con.PHYSICALWIDTH)
printerheight = win32print.GetDeviceCaps(pDC, win32con.PHYSICALHEIGHT)

hwnd = win32gui.GetDesktopWindow()
l, t, r, b = win32gui.GetWindowRect(hwnd)
desktopheight = b - t
desktopwidth = r - l
dDC = win32gui.GetWindowDC(hwnd)

dcDC = win32gui.CreateCompatibleDC(dDC)
dcBM = win32gui.CreateCompatibleBitmap(dDC, desktopwidth, desktopheight)
win32gui.SelectObject(dcDC, dcBM)
win32gui.StretchBlt(
    dcDC,
    0,
    0,
    desktopwidth,
    desktopheight,
    dDC,
    0,
    0,
    desktopwidth,
    desktopheight,
    win32con.SRCCOPY,
)

pcDC = win32gui.CreateCompatibleDC(pDC)
pcBM = win32gui.CreateCompatibleBitmap(pDC, printerwidth, printerheight)
win32gui.SelectObject(pcDC, pcBM)
win32gui.StretchBlt(
    pcDC,
    0,
    0,
    printerwidth,
    printerheight,
    dcDC,
    0,
    0,
    desktopwidth,
    desktopheight,
    win32con.SRCCOPY,
)

win32print.StartDoc(pDC, ("desktop.bmp", None, None, 0))
win32print.StartPage(pDC)
win32gui.StretchBlt(
    pDC,
    0,
    0,
    int(printerwidth * 0.9),
    int(printerheight * 0.9),
    pcDC,
    0,
    0,
    printerwidth,
    printerheight,
    win32con.SRCCOPY,
)

font = win32gui.LOGFONT()
font.lfHeight = int(printerheight / 20)
font.lfWidth = font.lfHeight
font.lfWeight = 150
font.lfItalic = 1
font.lfUnderline = 1
hf = win32gui.CreateFontIndirect(font)
win32gui.SelectObject(pDC, hf)
win32gui.SetBkMode(pDC, win32con.TRANSPARENT)
win32gui.SetTextColor(pDC, win32api.RGB(0, 255, 0))
win32gui.DrawText(
    pDC,
    "Printed by Python!",
    -1,
    (0, 0, int(printerwidth * 0.9), int(printerheight * 0.9)),
    win32con.DT_RIGHT | win32con.DT_BOTTOM | win32con.DT_SINGLELINE,
)
win32print.EndPage(pDC)
win32print.EndDoc(pDC)

win32print.ClosePrinter(p)
win32gui.DeleteObject(dcBM)
win32gui.DeleteObject(pcBM)
win32gui.DeleteObject(hf)
win32gui.DeleteDC(dDC)
win32gui.DeleteDC(dcDC)
win32gui.DeleteDC(pDC)
win32gui.DeleteDC(pcDC)

```


---

## win32/Demos/rastest.py

```python
# rastest.py - test/demonstrate the win32ras module.
# Much of the code here contributed by Jethro Wright.

import os
import sys

import win32event
import win32ras

# Build a little dictionary of RAS states to decent strings.
# eg win32ras.RASCS_OpenPort -> "OpenPort"
stateMap = {
    val: name[6:] for name, val in win32ras.__dict__.items() if name[:6] == "RASCS_"
}

# Use a lock so the callback can tell the main thread when it is finished.
callbackEvent = win32event.CreateEvent(None, 0, 0, None)


def Callback(hras, msg, state, error, exterror):
    # print("Callback called with ", hras, msg, state, error, exterror)
    stateName = stateMap.get(state, "Unknown state?")
    print("Status is %s (%04lx), error code is %d" % (stateName, state, error))
    finished = state in [win32ras.RASCS_Connected]
    if finished:
        win32event.SetEvent(callbackEvent)
    if error != 0 or int(state) == win32ras.RASCS_Disconnected:
        # we know for sure this is a good place to hangup....
        print("Detected call failure: %s" % win32ras.GetErrorString(error))
        HangUp(hras)
        win32event.SetEvent(callbackEvent)


def ShowConnections():
    print("All phone-book entries:")
    for (name,) in win32ras.EnumEntries():
        print(" ", name)
    print("Current Connections:")
    for con in win32ras.EnumConnections():
        print(" ", con)


def EditEntry(entryName):
    try:
        win32ras.EditPhonebookEntry(0, None, entryName)
    except win32ras.error as xxx_todo_changeme:
        (rc, function, msg) = xxx_todo_changeme.args
        print("Can not edit/find the RAS entry -", msg)


def HangUp(hras):
    #       trap potential, irrelevant errors from win32ras....
    try:
        win32ras.HangUp(hras)
    except:
        print("Tried to hang up gracefully on error, but didn't work....")
    return None


def Connect(entryName, bUseCallback):
    if bUseCallback:
        theCallback = Callback
        win32event.ResetEvent(callbackEvent)
    else:
        theCallback = None
    # In order to *use* the username/password of a particular dun entry,
    # one must explicitly get those params under Win95 ...
    # It's unclear whether that's even still necessary.
    try:
        dp, b = win32ras.GetEntryDialParams(None, entryName)
    except:
        print("Couldn't find DUN entry: %s" % entryName)
    else:
        hras, rc = win32ras.Dial(
            None, None, (entryName, "", "", dp[3], dp[4], ""), theCallback
        )
        # hras, rc = win32ras.Dial(None, None, (entryName, ),theCallback)
        # print(hras, rc)
        if not bUseCallback and rc != 0:
            print("Could not dial the RAS connection:", win32ras.GetErrorString(rc))
            hras = HangUp(hras)
        # don't wait here if there's no need to....
        elif (
            bUseCallback
            and win32event.WaitForSingleObject(callbackEvent, 60000)
            != win32event.WAIT_OBJECT_0
        ):
            print("Gave up waiting for the process to complete!")
            # sdk docs state one must explicitly hangup, even if there's an error....
            # https://learn.microsoft.com/en-us/windows/win32/api/ras/nf-ras-rasdialw#remarks
            try:
                cs = win32ras.GetConnectStatus(hras)
            except:
                # on error, attempt a hang up anyway....
                hras = HangUp(hras)
            else:
                if int(cs[0]) == win32ras.RASCS_Disconnected:
                    hras = HangUp(hras)
    return hras, rc


def Disconnect(rasEntry):
    # Need to find the entry
    name = rasEntry.lower()
    for hcon, entryName, devName, devType in win32ras.EnumConnections():
        if entryName.lower() == name:
            win32ras.HangUp(hcon)
            print("Disconnected from", rasEntry)
            break
    else:
        print("Could not find an open connection to", entryName)


usage = """
Usage: %s [-s] [-l] [-c connection] [-d connection]
-l : List phone-book entries and current connections.
-s : Show status while connecting/disconnecting (uses callbacks)
-c : Connect to the specified phonebook name.
-d : Disconnect from the specified phonebook name.
-e : Edit the specified phonebook entry.
"""


def main():
    import getopt

    try:
        opts, args = getopt.getopt(sys.argv[1:], "slc:d:e:")
    except getopt.error as why:
        print(why)
        print(
            usage
            % (
                os.path.basename(
                    sys.argv[0],
                )
            )
        )
        return

    bCallback = 0
    if args or not opts:
        print(
            usage
            % (
                os.path.basename(
                    sys.argv[0],
                )
            )
        )
        return
    for opt, val in opts:
        if opt == "-s":
            bCallback = 1
        if opt == "-l":
            ShowConnections()
        if opt == "-c":
            hras, rc = Connect(val, bCallback)
            if hras is not None:
                print(f"hras: 0x{hras:8x}, rc: 0x{rc:04x}")
        if opt == "-d":
            Disconnect(val)
        if opt == "-e":
            EditEntry(val)


if __name__ == "__main__":
    main()

```


---

## win32/Demos/security/GetTokenInformation.py

```python
"""Lists various types of information about current user's access token,
including UAC status."""

import win32api
import win32con
import win32security
from security_enums import (
    SECURITY_IMPERSONATION_LEVEL,
    TOKEN_ELEVATION_TYPE,
    TOKEN_GROUP_ATTRIBUTES,
    TOKEN_PRIVILEGE_ATTRIBUTES,
    TOKEN_TYPE,
)


def dump_token(th):
    token_type = win32security.GetTokenInformation(th, win32security.TokenType)
    print("TokenType:", token_type, TOKEN_TYPE.lookup_name(token_type))
    if token_type == win32security.TokenImpersonation:
        imp_lvl = win32security.GetTokenInformation(
            th, win32security.TokenImpersonationLevel
        )
        print(
            "TokenImpersonationLevel:",
            imp_lvl,
            SECURITY_IMPERSONATION_LEVEL.lookup_name(imp_lvl),
        )

    print(
        "TokenSessionId:",
        win32security.GetTokenInformation(th, win32security.TokenSessionId),
    )

    privs = win32security.GetTokenInformation(th, win32security.TokenPrivileges)
    print("TokenPrivileges:")
    for priv_luid, priv_flags in privs:
        flag_names, unk = TOKEN_PRIVILEGE_ATTRIBUTES.lookup_flags(priv_flags)
        flag_desc = " ".join(flag_names)
        if unk:
            flag_desc += f"({unk})"

        priv_name = win32security.LookupPrivilegeName("", priv_luid)
        priv_desc = win32security.LookupPrivilegeDisplayName("", priv_name)
        print("\t", priv_name, priv_desc, priv_flags, flag_desc)

    print("TokenGroups:")
    groups = win32security.GetTokenInformation(th, win32security.TokenGroups)
    for group_sid, group_attr in groups:
        flag_names, unk = TOKEN_GROUP_ATTRIBUTES.lookup_flags(group_attr)
        flag_desc = " ".join(flag_names)
        if unk:
            flag_desc += f"({unk})"
        if group_attr & TOKEN_GROUP_ATTRIBUTES.SE_GROUP_LOGON_ID:
            sid_desc = "Logon sid"
        else:
            sid_desc = win32security.LookupAccountSid("", group_sid)
        print("\t", group_sid, sid_desc, group_attr, flag_desc)

    print(
        "TokenElevation:",
        win32security.GetTokenInformation(th, win32security.TokenElevation),
    )
    print(
        "TokenHasRestrictions:",
        win32security.GetTokenInformation(th, win32security.TokenHasRestrictions),
    )
    print(
        "TokenMandatoryPolicy",
        win32security.GetTokenInformation(th, win32security.TokenMandatoryPolicy),
    )
    print(
        "TokenVirtualizationAllowed:",
        win32security.GetTokenInformation(th, win32security.TokenVirtualizationAllowed),
    )
    print(
        "TokenVirtualizationEnabled:",
        win32security.GetTokenInformation(th, win32security.TokenVirtualizationEnabled),
    )

    elevation_type = win32security.GetTokenInformation(
        th, win32security.TokenElevationType
    )
    print(
        "TokenElevationType:",
        elevation_type,
        TOKEN_ELEVATION_TYPE.lookup_name(elevation_type),
    )
    if elevation_type != win32security.TokenElevationTypeDefault:
        lt = win32security.GetTokenInformation(th, win32security.TokenLinkedToken)
        print("TokenLinkedToken:", lt)
    else:
        lt = None
    return lt


ph = win32api.GetCurrentProcess()
th = win32security.OpenProcessToken(ph, win32con.MAXIMUM_ALLOWED)
lt = dump_token(th)
if lt:
    print("\n\nlinked token info:")
    dump_token(lt)

```


---

## win32/Demos/security/account_rights.py

```python
import ntsecuritycon
import win32api
import win32con
import win32security

new_privs = (
    (
        win32security.LookupPrivilegeValue("", ntsecuritycon.SE_SECURITY_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
    (
        win32security.LookupPrivilegeValue("", ntsecuritycon.SE_CREATE_PERMANENT_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
    (
        win32security.LookupPrivilegeValue("", "SeEnableDelegationPrivilege"),
        win32con.SE_PRIVILEGE_ENABLED,
    ),  ##doesn't seem to be in ntsecuritycon.py ?
)

ph = win32api.GetCurrentProcess()
th = win32security.OpenProcessToken(
    ph, win32security.TOKEN_ALL_ACCESS
)  ##win32con.TOKEN_ADJUST_PRIVILEGES)
win32security.AdjustTokenPrivileges(th, 0, new_privs)

policy_handle = win32security.GetPolicyHandle("", win32security.POLICY_ALL_ACCESS)
tmp_sid = win32security.LookupAccountName("", "tmp")[0]

privs = [
    ntsecuritycon.SE_DEBUG_NAME,
    ntsecuritycon.SE_TCB_NAME,
    ntsecuritycon.SE_RESTORE_NAME,
    ntsecuritycon.SE_REMOTE_SHUTDOWN_NAME,
]
win32security.LsaAddAccountRights(policy_handle, tmp_sid, privs)

privlist = win32security.LsaEnumerateAccountRights(policy_handle, tmp_sid)
for priv in privlist:
    print(priv)

privs = [ntsecuritycon.SE_DEBUG_NAME, ntsecuritycon.SE_TCB_NAME]
win32security.LsaRemoveAccountRights(policy_handle, tmp_sid, 0, privs)

privlist = win32security.LsaEnumerateAccountRights(policy_handle, tmp_sid)
for priv in privlist:
    print(priv)

win32security.LsaClose(policy_handle)

```


---

## win32/Demos/security/explicit_entries.py

```python
import os

import ntsecuritycon
import win32api
import win32con
import win32security
from security_enums import ACCESS_MODE, ACE_FLAGS, TRUSTEE_FORM, TRUSTEE_TYPE

fname = os.path.join(win32api.GetTempPath(), "win32security_test.txt")
f = open(fname, "w")
f.write("Hello from Python\n")
f.close()
print("Testing on file", fname)

new_privs = (
    (
        win32security.LookupPrivilegeValue("", ntsecuritycon.SE_SECURITY_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
    (
        win32security.LookupPrivilegeValue("", ntsecuritycon.SE_SHUTDOWN_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
    (
        win32security.LookupPrivilegeValue("", ntsecuritycon.SE_RESTORE_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
    (
        win32security.LookupPrivilegeValue("", ntsecuritycon.SE_TAKE_OWNERSHIP_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
    (
        win32security.LookupPrivilegeValue("", ntsecuritycon.SE_CREATE_PERMANENT_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
    (
        win32security.LookupPrivilegeValue("", "SeEnableDelegationPrivilege"),
        win32con.SE_PRIVILEGE_ENABLED,
    ),  ##doesn't seem to be in ntsecuritycon.py ?
)

ph = win32api.GetCurrentProcess()
th = win32security.OpenProcessToken(
    ph, win32security.TOKEN_ALL_ACCESS
)  ##win32con.TOKEN_ADJUST_PRIVILEGES)
win32security.AdjustTokenPrivileges(th, 0, new_privs)

all_security_info = (
    win32security.OWNER_SECURITY_INFORMATION
    | win32security.GROUP_SECURITY_INFORMATION
    | win32security.DACL_SECURITY_INFORMATION
    | win32security.SACL_SECURITY_INFORMATION
)

sd = win32security.GetFileSecurity(fname, all_security_info)

old_sacl = sd.GetSecurityDescriptorSacl()
if old_sacl is None:
    old_sacl = win32security.ACL()
old_dacl = sd.GetSecurityDescriptorDacl()
if old_dacl is None:
    old_dacl = win32security.ACL()

my_sid = win32security.GetTokenInformation(th, ntsecuritycon.TokenUser)[0]
tmp_sid = win32security.LookupAccountName("", "tmp")[0]
pwr_sid = win32security.LookupAccountName("", "Power Users")[0]


## MultipleTrustee,MultipleTrusteeOperation,TrusteeForm,TrusteeType,Identifier
## first two are ignored
my_trustee = {}
my_trustee["MultipleTrustee"] = None
my_trustee["MultipleTrusteeOperation"] = 0
my_trustee["TrusteeForm"] = TRUSTEE_FORM.TRUSTEE_IS_SID
my_trustee["TrusteeType"] = TRUSTEE_TYPE.TRUSTEE_IS_USER
my_trustee["Identifier"] = my_sid

tmp_trustee = {}
tmp_trustee["MultipleTrustee"] = None
tmp_trustee["MultipleTrusteeOperation"] = 0
tmp_trustee["TrusteeForm"] = TRUSTEE_FORM.TRUSTEE_IS_NAME
tmp_trustee["TrusteeType"] = TRUSTEE_TYPE.TRUSTEE_IS_USER
tmp_trustee["Identifier"] = "rupole\\tmp"

pwr_trustee = {}
pwr_trustee["MultipleTrustee"] = None
pwr_trustee["MultipleTrusteeOperation"] = 0
pwr_trustee["TrusteeForm"] = TRUSTEE_FORM.TRUSTEE_IS_SID
pwr_trustee["TrusteeType"] = TRUSTEE_TYPE.TRUSTEE_IS_USER
pwr_trustee["Identifier"] = pwr_sid

expl_list = []
expl_list.append(
    {
        "Trustee": my_trustee,
        "Inheritance": ACE_FLAGS.NO_INHERITANCE,
        "AccessMode": ACCESS_MODE.SET_AUDIT_SUCCESS,  ##|ACCESS_MODE.SET_AUDIT_FAILURE,
        "AccessPermissions": win32con.GENERIC_ALL,
    }
)

expl_list.append(
    {
        "Trustee": my_trustee,
        "Inheritance": ACE_FLAGS.NO_INHERITANCE,
        "AccessMode": ACCESS_MODE.SET_AUDIT_FAILURE,
        "AccessPermissions": win32con.GENERIC_ALL,
    }
)

expl_list.append(
    {
        "Trustee": tmp_trustee,
        "Inheritance": ACE_FLAGS.NO_INHERITANCE,
        "AccessMode": ACCESS_MODE.SET_AUDIT_SUCCESS,
        "AccessPermissions": win32con.GENERIC_ALL,
    }
)

expl_list.append(
    {
        "Trustee": tmp_trustee,
        "Inheritance": ACE_FLAGS.NO_INHERITANCE,
        "AccessMode": ACCESS_MODE.SET_AUDIT_FAILURE,
        "AccessPermissions": win32con.GENERIC_ALL,
    }
)
old_sacl.SetEntriesInAcl(expl_list)

expl_list = []
expl_list.append(
    {
        "Trustee": tmp_trustee,
        "Inheritance": ACE_FLAGS.NO_INHERITANCE,
        "AccessMode": ACCESS_MODE.DENY_ACCESS,
        "AccessPermissions": win32con.DELETE,
    }
)

expl_list.append(
    {
        "Trustee": tmp_trustee,
        "Inheritance": ACE_FLAGS.NO_INHERITANCE,
        "AccessMode": ACCESS_MODE.GRANT_ACCESS,
        "AccessPermissions": win32con.WRITE_OWNER,
    }
)
expl_list.append(
    {
        "Trustee": pwr_trustee,
        "Inheritance": ACE_FLAGS.NO_INHERITANCE,
        "AccessMode": ACCESS_MODE.GRANT_ACCESS,
        "AccessPermissions": win32con.GENERIC_READ,
    }
)
expl_list.append(
    {
        "Trustee": my_trustee,
        "Inheritance": ACE_FLAGS.NO_INHERITANCE,
        "AccessMode": ACCESS_MODE.GRANT_ACCESS,
        "AccessPermissions": win32con.GENERIC_ALL,
    }
)

old_dacl.SetEntriesInAcl(expl_list)
sd.SetSecurityDescriptorSacl(1, old_sacl, 1)
sd.SetSecurityDescriptorDacl(1, old_dacl, 1)
sd.SetSecurityDescriptorOwner(pwr_sid, 1)

win32security.SetFileSecurity(fname, all_security_info, sd)

```


---

## win32/Demos/security/get_policy_info.py

```python
import win32security

policy_handle = win32security.GetPolicyHandle("rupole", win32security.POLICY_ALL_ACCESS)

# mod_nbr, mod_time = win32security.LsaQueryInformationPolicy(policy_handle,win32security.PolicyModificationInformation)
# print(mod_nbr, mod_time)

(
    domain_name,
    dns_domain_name,
    dns_forest_name,
    domain_guid,
    domain_sid,
) = win32security.LsaQueryInformationPolicy(
    policy_handle, win32security.PolicyDnsDomainInformation
)
print(domain_name, dns_domain_name, dns_forest_name, domain_guid, domain_sid)

event_audit_info = win32security.LsaQueryInformationPolicy(
    policy_handle, win32security.PolicyAuditEventsInformation
)
print(event_audit_info)

domain_name, sid = win32security.LsaQueryInformationPolicy(
    policy_handle, win32security.PolicyPrimaryDomainInformation
)
print(domain_name, sid)

domain_name, sid = win32security.LsaQueryInformationPolicy(
    policy_handle, win32security.PolicyAccountDomainInformation
)
print(domain_name, sid)

server_role = win32security.LsaQueryInformationPolicy(
    policy_handle, win32security.PolicyLsaServerRoleInformation
)
print("server role: ", server_role)

win32security.LsaClose(policy_handle)

```


---

## win32/Demos/security/list_rights.py

```python
import ntsecuritycon
import win32api
import win32con
import win32security

new_privs = (
    (
        win32security.LookupPrivilegeValue("", ntsecuritycon.SE_SECURITY_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
    (
        win32security.LookupPrivilegeValue("", ntsecuritycon.SE_CREATE_PERMANENT_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
    (
        win32security.LookupPrivilegeValue("", "SeEnableDelegationPrivilege"),
        win32con.SE_PRIVILEGE_ENABLED,
    ),  ##doesn't seem to be in ntsecuritycon.py ?
)

ph = win32api.GetCurrentProcess()
th = win32security.OpenProcessToken(
    ph, win32security.TOKEN_ALL_ACCESS
)  ##win32con.TOKEN_ADJUST_PRIVILEGES)
win32security.AdjustTokenPrivileges(th, 0, new_privs)

policy_handle = win32security.GetPolicyHandle("", win32security.POLICY_ALL_ACCESS)

sidlist = win32security.LsaEnumerateAccountsWithUserRight(
    policy_handle, ntsecuritycon.SE_RESTORE_NAME
)
for sid in sidlist:
    print(win32security.LookupAccountSid("", sid))

win32security.LsaClose(policy_handle)

```


---

## win32/Demos/security/localized_names.py

```python
# A Python port of the MS knowledge base article Q157234
# "How to deal with localized and renamed user and group names"
# https://www.betaarchive.com/wiki/index.php?title=Microsoft_KB_Archive/157234

import sys

import pywintypes
from ntsecuritycon import (
    DOMAIN_ALIAS_RID_ADMINS,
    DOMAIN_USER_RID_ADMIN,
    SECURITY_BUILTIN_DOMAIN_RID,
    SECURITY_NT_AUTHORITY,
)
from win32net import NetUserModalsGet
from win32security import LookupAccountSid


def LookupAliasFromRid(TargetComputer, Rid):
    # Sid is the same regardless of machine, since the well-known
    # BUILTIN domain is referenced.
    sid = pywintypes.SID()
    sid.Initialize(SECURITY_NT_AUTHORITY, 2)

    for i, r in enumerate((SECURITY_BUILTIN_DOMAIN_RID, Rid)):
        sid.SetSubAuthority(i, r)

    name, domain, typ = LookupAccountSid(TargetComputer, sid)
    return name


def LookupUserGroupFromRid(TargetComputer, Rid):
    # get the account domain Sid on the target machine
    # note: if you were looking up multiple sids based on the same
    # account domain, only need to call this once.
    umi2 = NetUserModalsGet(TargetComputer, 2)
    domain_sid = umi2["domain_id"]

    SubAuthorityCount = domain_sid.GetSubAuthorityCount()

    # create and init new sid with acct domain Sid + acct Rid
    sid = pywintypes.SID()
    sid.Initialize(domain_sid.GetSidIdentifierAuthority(), SubAuthorityCount + 1)

    # copy existing subauthorities from account domain Sid into
    # new Sid
    for i in range(SubAuthorityCount):
        sid.SetSubAuthority(i, domain_sid.GetSubAuthority(i))

    # append Rid to new Sid
    sid.SetSubAuthority(SubAuthorityCount, Rid)

    name, domain, typ = LookupAccountSid(TargetComputer, sid)
    return name


def main():
    if len(sys.argv) == 2:
        targetComputer = sys.argv[1]
    else:
        targetComputer = None

    name = LookupUserGroupFromRid(targetComputer, DOMAIN_USER_RID_ADMIN)
    print(f"'Administrator' user name = {name}")

    name = LookupAliasFromRid(targetComputer, DOMAIN_ALIAS_RID_ADMINS)
    print(f"'Administrators' local group/alias name = {name}")


if __name__ == "__main__":
    main()

```


---

## win32/Demos/security/lsaregevent.py

```python
import win32event
import win32security

evt = win32event.CreateEvent(None, 0, 0, None)
win32security.LsaRegisterPolicyChangeNotification(
    win32security.PolicyNotifyAuditEventsInformation, evt
)
print("Waiting for you change Audit policy in Management console ...")
ret_code = win32event.WaitForSingleObject(evt, 1000000000)
## should come back when you change Audit policy in Management console ...
print(ret_code)
win32security.LsaUnregisterPolicyChangeNotification(
    win32security.PolicyNotifyAuditEventsInformation, evt
)

```


---

## win32/Demos/security/lsastore.py

```python
import win32security

policy_handle = win32security.GetPolicyHandle("", win32security.POLICY_ALL_ACCESS)
privatedata = "some sensitive data"
keyname = "tmp"
win32security.LsaStorePrivateData(policy_handle, keyname, privatedata)
retrieveddata = win32security.LsaRetrievePrivateData(policy_handle, keyname)
assert retrieveddata == privatedata

## passing None deletes key
win32security.LsaStorePrivateData(policy_handle, keyname, None)
win32security.LsaClose(policy_handle)

```


---

## win32/Demos/security/query_information.py

```python
import win32api
import win32security
import winerror
from ntsecuritycon import TOKEN_QUERY, TokenUser


# This is a Python implementation of win32api.GetDomainName()
def GetDomainName():
    try:
        tok = win32security.OpenThreadToken(win32api.GetCurrentThread(), TOKEN_QUERY, 1)
    except win32api.error as details:
        if details[0] != winerror.ERROR_NO_TOKEN:
            raise
        # attempt to open the process token, since no thread token
        # exists
        tok = win32security.OpenProcessToken(win32api.GetCurrentProcess(), TOKEN_QUERY)
    sid, attr = win32security.GetTokenInformation(tok, TokenUser)
    win32api.CloseHandle(tok)

    name, dom, typ = win32security.LookupAccountSid(None, sid)
    return dom


if __name__ == "__main__":
    print("Domain name is", GetDomainName())

```


---

## win32/Demos/security/regsave_sa.py

```python
fname = "h:\\tmp.reg"

import os

import ntsecuritycon
import pywintypes
import win32api
import win32con
import win32security

## regsave will not overwrite a file
if os.path.isfile(fname):
    os.remove(fname)

new_privs = (
    (
        win32security.LookupPrivilegeValue("", ntsecuritycon.SE_SECURITY_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
    (
        win32security.LookupPrivilegeValue("", ntsecuritycon.SE_TCB_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
    (
        win32security.LookupPrivilegeValue("", ntsecuritycon.SE_BACKUP_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
    (
        win32security.LookupPrivilegeValue("", ntsecuritycon.SE_RESTORE_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
)
ph = win32api.GetCurrentProcess()
th = win32security.OpenProcessToken(
    ph, win32security.TOKEN_ALL_ACCESS | win32con.TOKEN_ADJUST_PRIVILEGES
)
win32security.AdjustTokenPrivileges(th, 0, new_privs)
my_sid = win32security.GetTokenInformation(th, ntsecuritycon.TokenUser)[0]

hklm = win32api.RegOpenKey(
    win32con.HKEY_LOCAL_MACHINE, None, 0, win32con.KEY_ALL_ACCESS
)
skey = win32api.RegOpenKey(hklm, "SYSTEM", 0, win32con.KEY_ALL_ACCESS)

sa = pywintypes.SECURITY_ATTRIBUTES()
sd = pywintypes.SECURITY_DESCRIPTOR()
sa.SECURITY_DESCRIPTOR = sd
acl = pywintypes.ACL()

pwr_sid = win32security.LookupAccountName("", "Power Users")[0]
acl.AddAccessAllowedAce(
    win32con.ACL_REVISION,
    win32con.GENERIC_READ | win32con.ACCESS_SYSTEM_SECURITY,
    my_sid,
)
sd.SetSecurityDescriptorDacl(1, acl, 0)
sd.SetSecurityDescriptorOwner(pwr_sid, 0)
sa.bInheritHandle = 1
assert sa.SECURITY_DESCRIPTOR is sd

win32api.RegSaveKey(skey, fname, sa)

```


---

## win32/Demos/security/regsecurity.py

```python
import ntsecuritycon
import win32api
import win32con
import win32security

new_privs = (
    (
        win32security.LookupPrivilegeValue("", ntsecuritycon.SE_SECURITY_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
    (
        win32security.LookupPrivilegeValue("", ntsecuritycon.SE_TCB_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
)
ph = win32api.GetCurrentProcess()
th = win32security.OpenProcessToken(
    ph, win32security.TOKEN_ALL_ACCESS | win32con.TOKEN_ADJUST_PRIVILEGES
)

win32security.AdjustTokenPrivileges(th, 0, new_privs)
hkey = win32api.RegOpenKey(
    win32con.HKEY_LOCAL_MACHINE, None, 0, win32con.KEY_ALL_ACCESS
)
win32api.RegCreateKey(hkey, "SYSTEM\\NOTMP")
notmpkey = win32api.RegOpenKey(
    hkey, "SYSTEM\\notmp", 0, win32con.ACCESS_SYSTEM_SECURITY
)

tmp_sid = win32security.LookupAccountName("", "tmp")[0]
sacl = win32security.ACL()
sacl.AddAuditAccessAce(win32security.ACL_REVISION, win32con.GENERIC_ALL, tmp_sid, 1, 1)

sd = win32security.SECURITY_DESCRIPTOR()
sd.SetSecurityDescriptorSacl(1, sacl, 1)
win32api.RegSetKeySecurity(notmpkey, win32con.SACL_SECURITY_INFORMATION, sd)

```


---

## win32/Demos/security/sa_inherit.py

```python
import pywintypes
import win32security

sa = pywintypes.SECURITY_ATTRIBUTES()
tmp_sid = win32security.LookupAccountName("", "tmp")[0]
sa.SetSecurityDescriptorOwner(tmp_sid, 0)
sid = sa.SECURITY_DESCRIPTOR.GetSecurityDescriptorOwner()
print(win32security.LookupAccountSid("", sid))

```


---

## win32/Demos/security/security_enums.py

```python
import ntsecuritycon
import win32security
import winnt


class Enum:
    def __init__(self, *const_names):
        """Accepts variable number of constant names that can be found in either
        win32security, ntsecuritycon, or winnt."""
        for const_name in const_names:
            try:
                const_val = getattr(win32security, const_name)
            except AttributeError:
                try:
                    const_val = getattr(ntsecuritycon, const_name)
                except AttributeError:
                    try:
                        const_val = getattr(winnt, const_name)
                    except AttributeError:
                        raise AttributeError(
                            'Constant "%s" not found in win32security, ntsecuritycon, or winnt.'
                            % const_name
                        )
            setattr(self, const_name, const_val)

    def lookup_name(self, const_val):
        """Looks up the name of a particular value."""
        for k, v in self.__dict__.items():
            if v == const_val:
                return k
        raise AttributeError("Value %s not found in enum" % const_val)

    def lookup_flags(self, flags):
        """Returns the names of all recognized flags in input, and any flags not found in the enum."""
        flag_names = []
        unknown_flags = flags
        for k, v in self.__dict__.items():
            if flags & v == v:
                flag_names.append(k)
                unknown_flags &= ~v
        return flag_names, unknown_flags


TOKEN_INFORMATION_CLASS = Enum(
    "TokenUser",
    "TokenGroups",
    "TokenPrivileges",
    "TokenOwner",
    "TokenPrimaryGroup",
    "TokenDefaultDacl",
    "TokenSource",
    "TokenType",
    "TokenImpersonationLevel",
    "TokenStatistics",
    "TokenRestrictedSids",
    "TokenSessionId",
    "TokenGroupsAndPrivileges",
    "TokenSessionReference",
    "TokenSandBoxInert",
    "TokenAuditPolicy",
    "TokenOrigin",
    "TokenElevationType",
    "TokenLinkedToken",
    "TokenElevation",
    "TokenHasRestrictions",
    "TokenAccessInformation",
    "TokenVirtualizationAllowed",
    "TokenVirtualizationEnabled",
    "TokenIntegrityLevel",
    "TokenUIAccess",
    "TokenMandatoryPolicy",
    "TokenLogonSid",
)

TOKEN_TYPE = Enum("TokenPrimary", "TokenImpersonation")

TOKEN_ELEVATION_TYPE = Enum(
    "TokenElevationTypeDefault", "TokenElevationTypeFull", "TokenElevationTypeLimited"
)

POLICY_AUDIT_EVENT_TYPE = Enum(
    "AuditCategorySystem",
    "AuditCategoryLogon",
    "AuditCategoryObjectAccess",
    "AuditCategoryPrivilegeUse",
    "AuditCategoryDetailedTracking",
    "AuditCategoryPolicyChange",
    "AuditCategoryAccountManagement",
    "AuditCategoryDirectoryServiceAccess",
    "AuditCategoryAccountLogon",
)

POLICY_INFORMATION_CLASS = Enum(
    "PolicyAuditLogInformation",
    "PolicyAuditEventsInformation",
    "PolicyPrimaryDomainInformation",
    "PolicyPdAccountInformation",
    "PolicyAccountDomainInformation",
    "PolicyLsaServerRoleInformation",
    "PolicyReplicaSourceInformation",
    "PolicyDefaultQuotaInformation",
    "PolicyModificationInformation",
    "PolicyAuditFullSetInformation",
    "PolicyAuditFullQueryInformation",
    "PolicyDnsDomainInformation",
)

POLICY_LSA_SERVER_ROLE = Enum("PolicyServerRoleBackup", "PolicyServerRolePrimary")

## access modes for opening a policy handle - this is not a real enum
POLICY_ACCESS_MODES = Enum(
    "POLICY_VIEW_LOCAL_INFORMATION",
    "POLICY_VIEW_AUDIT_INFORMATION",
    "POLICY_GET_PRIVATE_INFORMATION",
    "POLICY_TRUST_ADMIN",
    "POLICY_CREATE_ACCOUNT",
    "POLICY_CREATE_SECRET",
    "POLICY_CREATE_PRIVILEGE",
    "POLICY_SET_DEFAULT_QUOTA_LIMITS",
    "POLICY_SET_AUDIT_REQUIREMENTS",
    "POLICY_AUDIT_LOG_ADMIN",
    "POLICY_SERVER_ADMIN",
    "POLICY_LOOKUP_NAMES",
    "POLICY_NOTIFICATION",
    "POLICY_ALL_ACCESS",
    "POLICY_READ",
    "POLICY_WRITE",
    "POLICY_EXECUTE",
)

## EventAuditingOptions flags - not a real enum
POLICY_AUDIT_EVENT_OPTIONS_FLAGS = Enum(
    "POLICY_AUDIT_EVENT_UNCHANGED",
    "POLICY_AUDIT_EVENT_SUCCESS",
    "POLICY_AUDIT_EVENT_FAILURE",
    "POLICY_AUDIT_EVENT_NONE",
)

# AceType in ACE_HEADER - not a real enum
ACE_TYPE = Enum(
    "ACCESS_MIN_MS_ACE_TYPE",
    "ACCESS_ALLOWED_ACE_TYPE",
    "ACCESS_DENIED_ACE_TYPE",
    "SYSTEM_AUDIT_ACE_TYPE",
    "SYSTEM_ALARM_ACE_TYPE",
    "ACCESS_MAX_MS_V2_ACE_TYPE",
    "ACCESS_ALLOWED_COMPOUND_ACE_TYPE",
    "ACCESS_MAX_MS_V3_ACE_TYPE",
    "ACCESS_MIN_MS_OBJECT_ACE_TYPE",
    "ACCESS_ALLOWED_OBJECT_ACE_TYPE",
    "ACCESS_DENIED_OBJECT_ACE_TYPE",
    "SYSTEM_AUDIT_OBJECT_ACE_TYPE",
    "SYSTEM_ALARM_OBJECT_ACE_TYPE",
    "ACCESS_MAX_MS_OBJECT_ACE_TYPE",
    "ACCESS_MAX_MS_V4_ACE_TYPE",
    "ACCESS_MAX_MS_ACE_TYPE",
    "ACCESS_ALLOWED_CALLBACK_ACE_TYPE",
    "ACCESS_DENIED_CALLBACK_ACE_TYPE",
    "ACCESS_ALLOWED_CALLBACK_OBJECT_ACE_TYPE",
    "ACCESS_DENIED_CALLBACK_OBJECT_ACE_TYPE",
    "SYSTEM_AUDIT_CALLBACK_ACE_TYPE",
    "SYSTEM_ALARM_CALLBACK_ACE_TYPE",
    "SYSTEM_AUDIT_CALLBACK_OBJECT_ACE_TYPE",
    "SYSTEM_ALARM_CALLBACK_OBJECT_ACE_TYPE",
    "SYSTEM_MANDATORY_LABEL_ACE_TYPE",
    "ACCESS_MAX_MS_V5_ACE_TYPE",
)

# bit flags for AceFlags - not a real enum
ACE_FLAGS = Enum(
    "CONTAINER_INHERIT_ACE",
    "FAILED_ACCESS_ACE_FLAG",
    "INHERIT_ONLY_ACE",
    "INHERITED_ACE",
    "NO_PROPAGATE_INHERIT_ACE",
    "OBJECT_INHERIT_ACE",
    "SUCCESSFUL_ACCESS_ACE_FLAG",
    "NO_INHERITANCE",
    "SUB_CONTAINERS_AND_OBJECTS_INHERIT",
    "SUB_CONTAINERS_ONLY_INHERIT",
    "SUB_OBJECTS_ONLY_INHERIT",
)

# used in SetEntriesInAcl - very similar to ACE_TYPE
ACCESS_MODE = Enum(
    "NOT_USED_ACCESS",
    "GRANT_ACCESS",
    "SET_ACCESS",
    "DENY_ACCESS",
    "REVOKE_ACCESS",
    "SET_AUDIT_SUCCESS",
    "SET_AUDIT_FAILURE",
)

# Bit flags in PSECURITY_DESCRIPTOR->Control - not a real enum
SECURITY_DESCRIPTOR_CONTROL_FLAGS = Enum(
    "SE_DACL_AUTO_INHERITED",  ## win2k and up
    "SE_SACL_AUTO_INHERITED",  ## win2k and up
    "SE_DACL_PROTECTED",  ## win2k and up
    "SE_SACL_PROTECTED",  ## win2k and up
    "SE_DACL_DEFAULTED",
    "SE_DACL_PRESENT",
    "SE_GROUP_DEFAULTED",
    "SE_OWNER_DEFAULTED",
    "SE_SACL_PRESENT",
    "SE_SELF_RELATIVE",
    "SE_SACL_DEFAULTED",
)

# types of SID
SID_NAME_USE = Enum(
    "SidTypeUser",
    "SidTypeGroup",
    "SidTypeDomain",
    "SidTypeAlias",
    "SidTypeWellKnownGroup",
    "SidTypeDeletedAccount",
    "SidTypeInvalid",
    "SidTypeUnknown",
    "SidTypeComputer",
    "SidTypeLabel",
)

## bit flags, not a real enum
TOKEN_ACCESS_PRIVILEGES = Enum(
    "TOKEN_ADJUST_DEFAULT",
    "TOKEN_ADJUST_GROUPS",
    "TOKEN_ADJUST_PRIVILEGES",
    "TOKEN_ALL_ACCESS",
    "TOKEN_ASSIGN_PRIMARY",
    "TOKEN_DUPLICATE",
    "TOKEN_EXECUTE",
    "TOKEN_IMPERSONATE",
    "TOKEN_QUERY",
    "TOKEN_QUERY_SOURCE",
    "TOKEN_READ",
    "TOKEN_WRITE",
)

SECURITY_IMPERSONATION_LEVEL = Enum(
    "SecurityAnonymous",
    "SecurityIdentification",
    "SecurityImpersonation",
    "SecurityDelegation",
)

POLICY_SERVER_ENABLE_STATE = Enum("PolicyServerEnabled", "PolicyServerDisabled")

POLICY_NOTIFICATION_INFORMATION_CLASS = Enum(
    "PolicyNotifyAuditEventsInformation",
    "PolicyNotifyAccountDomainInformation",
    "PolicyNotifyServerRoleInformation",
    "PolicyNotifyDnsDomainInformation",
    "PolicyNotifyDomainEfsInformation",
    "PolicyNotifyDomainKerberosTicketInformation",
    "PolicyNotifyMachineAccountPasswordInformation",
)

TRUSTED_INFORMATION_CLASS = Enum(
    "TrustedDomainNameInformation",
    "TrustedControllersInformation",
    "TrustedPosixOffsetInformation",
    "TrustedPasswordInformation",
    "TrustedDomainInformationBasic",
    "TrustedDomainInformationEx",
    "TrustedDomainAuthInformation",
    "TrustedDomainFullInformation",
    "TrustedDomainAuthInformationInternal",
    "TrustedDomainFullInformationInternal",
    "TrustedDomainInformationEx2Internal",
    "TrustedDomainFullInformation2Internal",
)

TRUSTEE_FORM = Enum(
    "TRUSTEE_IS_SID",
    "TRUSTEE_IS_NAME",
    "TRUSTEE_BAD_FORM",
    "TRUSTEE_IS_OBJECTS_AND_SID",
    "TRUSTEE_IS_OBJECTS_AND_NAME",
)

TRUSTEE_TYPE = Enum(
    "TRUSTEE_IS_UNKNOWN",
    "TRUSTEE_IS_USER",
    "TRUSTEE_IS_GROUP",
    "TRUSTEE_IS_DOMAIN",
    "TRUSTEE_IS_ALIAS",
    "TRUSTEE_IS_WELL_KNOWN_GROUP",
    "TRUSTEE_IS_DELETED",
    "TRUSTEE_IS_INVALID",
    "TRUSTEE_IS_COMPUTER",
)

## SE_OBJECT_TYPE - securable objects
SE_OBJECT_TYPE = Enum(
    "SE_UNKNOWN_OBJECT_TYPE",
    "SE_FILE_OBJECT",
    "SE_SERVICE",
    "SE_PRINTER",
    "SE_REGISTRY_KEY",
    "SE_LMSHARE",
    "SE_KERNEL_OBJECT",
    "SE_WINDOW_OBJECT",
    "SE_DS_OBJECT",
    "SE_DS_OBJECT_ALL",
    "SE_PROVIDER_DEFINED_OBJECT",
    "SE_WMIGUID_OBJECT",
    "SE_REGISTRY_WOW64_32KEY",
)

PRIVILEGE_FLAGS = Enum(
    "SE_PRIVILEGE_ENABLED_BY_DEFAULT",
    "SE_PRIVILEGE_ENABLED",
    "SE_PRIVILEGE_USED_FOR_ACCESS",
)

# Group flags used with TokenGroups
TOKEN_GROUP_ATTRIBUTES = Enum(
    "SE_GROUP_MANDATORY",
    "SE_GROUP_ENABLED_BY_DEFAULT",
    "SE_GROUP_ENABLED",
    "SE_GROUP_OWNER",
    "SE_GROUP_USE_FOR_DENY_ONLY",
    "SE_GROUP_INTEGRITY",
    "SE_GROUP_INTEGRITY_ENABLED",
    "SE_GROUP_LOGON_ID",
    "SE_GROUP_RESOURCE",
)

# Privilege flags returned by TokenPrivileges
TOKEN_PRIVILEGE_ATTRIBUTES = Enum(
    "SE_PRIVILEGE_ENABLED_BY_DEFAULT",
    "SE_PRIVILEGE_ENABLED",
    "SE_PRIVILEGE_REMOVED",
    "SE_PRIVILEGE_USED_FOR_ACCESS",
)

```


---

## win32/Demos/security/set_file_audit.py

```python
import os

import ntsecuritycon
import win32api
import win32con
import win32security
from win32security import (
    ACL_REVISION_DS,
    CONTAINER_INHERIT_ACE,
    DACL_SECURITY_INFORMATION,
    GROUP_SECURITY_INFORMATION,
    OBJECT_INHERIT_ACE,
    OWNER_SECURITY_INFORMATION,
    PROTECTED_DACL_SECURITY_INFORMATION,
    SACL_SECURITY_INFORMATION,
    SE_FILE_OBJECT,
)

## SE_SECURITY_NAME needed to access SACL, SE_RESTORE_NAME needed to change owner to someone other than yourself
new_privs = (
    (
        win32security.LookupPrivilegeValue("", ntsecuritycon.SE_SECURITY_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
    (
        win32security.LookupPrivilegeValue("", ntsecuritycon.SE_RESTORE_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
)
ph = win32api.GetCurrentProcess()
th = win32security.OpenProcessToken(
    ph, win32security.TOKEN_ALL_ACCESS | win32con.TOKEN_ADJUST_PRIVILEGES
)
modified_privs = win32security.AdjustTokenPrivileges(th, 0, new_privs)

## look up a few sids that should be available on most systems
my_sid = win32security.GetTokenInformation(th, ntsecuritycon.TokenUser)[0]
pwr_sid = win32security.LookupAccountName("", "Power Users")[0]
admin_sid = win32security.LookupAccountName("", "Administrators")[0]
everyone_sid = win32security.LookupAccountName("", "EveryOne")[0]

## create a dir and set security so Everyone has read permissions, and all files and subdirs inherit its ACLs
temp_dir = win32api.GetTempPath()
dir_name = win32api.GetTempFileName(temp_dir, "sfa")[0]
os.remove(dir_name)
os.mkdir(dir_name)
dir_dacl = win32security.ACL()
dir_dacl.AddAccessAllowedAceEx(
    ACL_REVISION_DS,
    CONTAINER_INHERIT_ACE | OBJECT_INHERIT_ACE,
    win32con.GENERIC_READ,
    everyone_sid,
)
## make sure current user has permissions on dir
dir_dacl.AddAccessAllowedAceEx(
    ACL_REVISION_DS,
    CONTAINER_INHERIT_ACE | OBJECT_INHERIT_ACE,
    win32con.GENERIC_ALL,
    my_sid,
)
## keep dir from inheriting any permissions so it only has ACEs explicitly set here
win32security.SetNamedSecurityInfo(
    dir_name,
    SE_FILE_OBJECT,
    OWNER_SECURITY_INFORMATION
    | GROUP_SECURITY_INFORMATION
    | DACL_SECURITY_INFORMATION
    | PROTECTED_DACL_SECURITY_INFORMATION,
    pwr_sid,
    pwr_sid,
    dir_dacl,
    None,
)

## Create a file in the dir and add some specific permissions to it
fname = win32api.GetTempFileName(dir_name, "sfa")[0]
print(fname)
file_sd = win32security.GetNamedSecurityInfo(
    fname, SE_FILE_OBJECT, DACL_SECURITY_INFORMATION | SACL_SECURITY_INFORMATION
)
file_dacl = file_sd.GetSecurityDescriptorDacl()
file_sacl = file_sd.GetSecurityDescriptorSacl()

if file_dacl is None:
    file_dacl = win32security.ACL()
if file_sacl is None:
    file_sacl = win32security.ACL()

file_dacl.AddAccessDeniedAce(file_dacl.GetAclRevision(), win32con.DELETE, admin_sid)
file_dacl.AddAccessDeniedAce(file_dacl.GetAclRevision(), win32con.DELETE, my_sid)
file_dacl.AddAccessAllowedAce(file_dacl.GetAclRevision(), win32con.GENERIC_ALL, pwr_sid)
file_sacl.AddAuditAccessAce(
    file_dacl.GetAclRevision(), win32con.GENERIC_ALL, my_sid, True, True
)

win32security.SetNamedSecurityInfo(
    fname,
    SE_FILE_OBJECT,
    DACL_SECURITY_INFORMATION | SACL_SECURITY_INFORMATION,
    None,
    None,
    file_dacl,
    file_sacl,
)

win32security.AdjustTokenPrivileges(th, 0, modified_privs)

```


---

## win32/Demos/security/set_file_owner.py

```python
fname = r"h:\tmp.txt"

import ntsecuritycon
import win32api
import win32con
import win32security

new_privs = (
    (
        win32security.LookupPrivilegeValue("", ntsecuritycon.SE_SECURITY_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
    (
        win32security.LookupPrivilegeValue("", ntsecuritycon.SE_SHUTDOWN_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
    (
        win32security.LookupPrivilegeValue("", ntsecuritycon.SE_TCB_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
    (
        win32security.LookupPrivilegeValue("", ntsecuritycon.SE_RESTORE_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
    (
        win32security.LookupPrivilegeValue("", ntsecuritycon.SE_TAKE_OWNERSHIP_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
    (
        win32security.LookupPrivilegeValue("", ntsecuritycon.SE_CREATE_PERMANENT_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
    (
        win32security.LookupPrivilegeValue("", "SeEnableDelegationPrivilege"),
        win32con.SE_PRIVILEGE_ENABLED,
    ),  ##doesn't seem to be in ntsecuritycon.py ?
)

ph = win32api.GetCurrentProcess()
th = win32security.OpenProcessToken(
    ph, win32security.TOKEN_ALL_ACCESS | win32con.TOKEN_ADJUST_PRIVILEGES
)
win32security.AdjustTokenPrivileges(th, 0, new_privs)

all_security_info = (
    win32security.OWNER_SECURITY_INFORMATION
    | win32security.GROUP_SECURITY_INFORMATION
    | win32security.DACL_SECURITY_INFORMATION
    | win32security.SACL_SECURITY_INFORMATION
)

sd = win32security.GetFileSecurity(fname, all_security_info)
old_dacl = sd.GetSecurityDescriptorDacl()
old_sacl = sd.GetSecurityDescriptorSacl()
old_group = sd.GetSecurityDescriptorGroup()

new_sd = win32security.SECURITY_DESCRIPTOR()
print(
    "relative, valid, size: ",
    new_sd.IsSelfRelative(),
    new_sd.IsValid(),
    new_sd.GetLength(),
)

my_sid = win32security.GetTokenInformation(th, ntsecuritycon.TokenUser)[0]
tmp_sid = win32security.LookupAccountName("", "tmp")[0]

new_sd.SetSecurityDescriptorSacl(1, old_sacl, 1)
new_sd.SetSecurityDescriptorDacl(1, old_dacl, 1)
new_sd.SetSecurityDescriptorOwner(tmp_sid, 0)
new_sd.SetSecurityDescriptorGroup(old_group, 0)

win32security.SetFileSecurity(fname, all_security_info, new_sd)

```


---

## win32/Demos/security/set_policy_info.py

```python
import win32security

policy_handle = win32security.GetPolicyHandle("rupole", win32security.POLICY_ALL_ACCESS)

event_audit_info = win32security.LsaQueryInformationPolicy(
    policy_handle, win32security.PolicyAuditEventsInformation
)
print(event_audit_info)

new_audit_info = list(event_audit_info[1])
new_audit_info[win32security.AuditCategoryPolicyChange] = (
    win32security.POLICY_AUDIT_EVENT_SUCCESS | win32security.POLICY_AUDIT_EVENT_FAILURE
)
new_audit_info[win32security.AuditCategoryAccountLogon] = (
    win32security.POLICY_AUDIT_EVENT_SUCCESS | win32security.POLICY_AUDIT_EVENT_FAILURE
)
new_audit_info[win32security.AuditCategoryLogon] = (
    win32security.POLICY_AUDIT_EVENT_SUCCESS | win32security.POLICY_AUDIT_EVENT_FAILURE
)

win32security.LsaSetInformationPolicy(
    policy_handle, win32security.PolicyAuditEventsInformation, (1, new_audit_info)
)

win32security.LsaClose(policy_handle)

```


---

## win32/Demos/security/setkernelobjectsecurity.py

```python
import win32api
import win32con
import win32security

## You need SE_RESTORE_NAME to be able to set the owner of a security descriptor to anybody
## other than yourself or your primary group.  Most admin logins don't have it by default, so
## enabling it may fail
new_privs = (
    (
        win32security.LookupPrivilegeValue("", win32security.SE_SECURITY_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
    (
        win32security.LookupPrivilegeValue("", win32security.SE_TCB_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
    (
        win32security.LookupPrivilegeValue("", win32security.SE_SHUTDOWN_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
    (
        win32security.LookupPrivilegeValue("", win32security.SE_RESTORE_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
    (
        win32security.LookupPrivilegeValue("", win32security.SE_TAKE_OWNERSHIP_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
    (
        win32security.LookupPrivilegeValue("", win32security.SE_CREATE_PERMANENT_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
    (
        win32security.LookupPrivilegeValue("", win32security.SE_ENABLE_DELEGATION_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
    (
        win32security.LookupPrivilegeValue("", win32security.SE_CHANGE_NOTIFY_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
    (
        win32security.LookupPrivilegeValue("", win32security.SE_DEBUG_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
    (
        win32security.LookupPrivilegeValue(
            "", win32security.SE_PROF_SINGLE_PROCESS_NAME
        ),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
    (
        win32security.LookupPrivilegeValue("", win32security.SE_SYSTEM_PROFILE_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
    (
        win32security.LookupPrivilegeValue("", win32security.SE_LOCK_MEMORY_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
)

all_info = (
    win32security.OWNER_SECURITY_INFORMATION
    | win32security.GROUP_SECURITY_INFORMATION
    | win32security.DACL_SECURITY_INFORMATION
    | win32security.SACL_SECURITY_INFORMATION
)

pid = win32api.GetCurrentProcessId()
ph = win32api.OpenProcess(win32con.PROCESS_ALL_ACCESS, 0, pid)
## PROCESS_ALL_ACCESS does not contain ACCESS_SYSTEM_SECURITY (neccessy to do SACLs)
th = win32security.OpenProcessToken(
    ph, win32security.TOKEN_ALL_ACCESS
)  ##win32con.TOKEN_ADJUST_PRIVILEGES)
old_privs = win32security.GetTokenInformation(th, win32security.TokenPrivileges)
desired_privs = tuple((e[0], win32con.SE_PRIVILEGE_ENABLED) for e in old_privs)
modified_privs = win32security.AdjustTokenPrivileges(
    th, 0, desired_privs
)  # Will (partially) fail for new_privs (unless they are a subset of current ones)
gle = win32api.GetLastError()
if gle != 0:
    print("AdjustTokenPrivileges error:", gle)
# print(modified_privs)
my_sid = win32security.GetTokenInformation(th, win32security.TokenUser)[0]
pwr_sid = win32security.LookupAccountName("", "Power Users")[0]
## reopen process with ACCESS_SYSTEM_SECURITY now that sufficent privs are enabled
ph = win32api.OpenProcess(
    win32con.PROCESS_ALL_ACCESS | win32con.ACCESS_SYSTEM_SECURITY, 0, pid
)

sd = win32security.GetKernelObjectSecurity(ph, all_info)
dacl = sd.GetSecurityDescriptorDacl()
if dacl is None:
    dacl = win32security.ACL()
sacl = sd.GetSecurityDescriptorSacl()
if sacl is None:
    sacl = win32security.ACL()

dacl_ace_cnt = dacl.GetAceCount()
sacl_ace_cnt = sacl.GetAceCount()

dacl.AddAccessAllowedAce(
    dacl.GetAclRevision(), win32con.ACCESS_SYSTEM_SECURITY | win32con.WRITE_DAC, my_sid
)
sacl.AddAuditAccessAce(sacl.GetAclRevision(), win32con.GENERIC_ALL, my_sid, 1, 1)
sd.SetSecurityDescriptorDacl(1, dacl, 0)
sd.SetSecurityDescriptorSacl(1, sacl, 0)
sd.SetSecurityDescriptorGroup(pwr_sid, 0)
sd.SetSecurityDescriptorOwner(pwr_sid, 0)

win32security.SetKernelObjectSecurity(ph, all_info, sd)
new_sd = win32security.GetKernelObjectSecurity(ph, all_info)

if new_sd.GetSecurityDescriptorDacl().GetAceCount() != dacl_ace_cnt + 1:
    print("New dacl doesn't contain extra ace ????")
if new_sd.GetSecurityDescriptorSacl().GetAceCount() != sacl_ace_cnt + 1:
    print("New Sacl doesn't contain extra ace ????")
if (
    win32security.LookupAccountSid("", new_sd.GetSecurityDescriptorOwner())[0]
    != "Power Users"
):
    print("Owner not successfully set to Power Users !!!!!")
if (
    win32security.LookupAccountSid("", new_sd.GetSecurityDescriptorGroup())[0]
    != "Power Users"
):
    print("Group not successfully set to Power Users !!!!!")

sd.SetSecurityDescriptorSacl(0, None, 0)
win32security.SetKernelObjectSecurity(ph, win32security.SACL_SECURITY_INFORMATION, sd)
new_sd_1 = win32security.GetKernelObjectSecurity(
    ph, win32security.SACL_SECURITY_INFORMATION
)
if new_sd_1.GetSecurityDescriptorSacl() is not None:
    print("Unable to set Sacl to NULL !!!!!!!!")

```


---

## win32/Demos/security/setnamedsecurityinfo.py

```python
import win32api
import win32con
import win32process
import win32security

fname, tmp = win32api.GetTempFileName(win32api.GetTempPath(), "tmp")
print(fname)
## You need SE_RESTORE_NAME to be able to set the owner of a security descriptor to anybody
## other than yourself or your primary group.  Most admin logins don't have it by default, so
## enabling it may fail
new_privs = (
    (
        win32security.LookupPrivilegeValue("", win32security.SE_SECURITY_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
    (
        win32security.LookupPrivilegeValue("", win32security.SE_TCB_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
    (
        win32security.LookupPrivilegeValue("", win32security.SE_SHUTDOWN_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
    (
        win32security.LookupPrivilegeValue("", win32security.SE_RESTORE_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
    (
        win32security.LookupPrivilegeValue("", win32security.SE_TAKE_OWNERSHIP_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
    (
        win32security.LookupPrivilegeValue("", win32security.SE_CREATE_PERMANENT_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
    (
        win32security.LookupPrivilegeValue("", win32security.SE_ENABLE_DELEGATION_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
    (
        win32security.LookupPrivilegeValue("", win32security.SE_CHANGE_NOTIFY_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
    (
        win32security.LookupPrivilegeValue("", win32security.SE_DEBUG_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
    (
        win32security.LookupPrivilegeValue(
            "", win32security.SE_PROF_SINGLE_PROCESS_NAME
        ),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
    (
        win32security.LookupPrivilegeValue("", win32security.SE_SYSTEM_PROFILE_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
    (
        win32security.LookupPrivilegeValue("", win32security.SE_LOCK_MEMORY_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
)

all_info = (
    win32security.OWNER_SECURITY_INFORMATION
    | win32security.GROUP_SECURITY_INFORMATION
    | win32security.DACL_SECURITY_INFORMATION
    | win32security.SACL_SECURITY_INFORMATION
)

ph = win32process.GetCurrentProcess()
th = win32security.OpenProcessToken(
    ph, win32security.TOKEN_ALL_ACCESS
)  ##win32con.TOKEN_ADJUST_PRIVILEGES)
win32security.AdjustTokenPrivileges(th, 0, new_privs)
my_sid = win32security.GetTokenInformation(th, win32security.TokenUser)[0]
pwr_sid = win32security.LookupAccountName("", "Power Users")[0]

sd = win32security.GetNamedSecurityInfo(fname, win32security.SE_FILE_OBJECT, all_info)
dacl = sd.GetSecurityDescriptorDacl()
if dacl is None:
    dacl = win32security.ACL()
sacl = sd.GetSecurityDescriptorSacl()
if sacl is None:
    sacl = win32security.ACL()

dacl_ace_cnt = dacl.GetAceCount()
sacl_ace_cnt = sacl.GetAceCount()

dacl.AddAccessAllowedAce(
    dacl.GetAclRevision(), win32con.ACCESS_SYSTEM_SECURITY | win32con.WRITE_DAC, my_sid
)
sacl.AddAuditAccessAce(sacl.GetAclRevision(), win32con.GENERIC_ALL, my_sid, 1, 1)

win32security.SetNamedSecurityInfo(
    fname, win32security.SE_FILE_OBJECT, all_info, pwr_sid, pwr_sid, dacl, sacl
)
new_sd = win32security.GetNamedSecurityInfo(
    fname, win32security.SE_FILE_OBJECT, all_info
)

## could do additional checking to make sure added ACE contains expected info
if new_sd.GetSecurityDescriptorDacl().GetAceCount() != dacl_ace_cnt + 1:
    print("New dacl doesn't contain extra ace ????")
if new_sd.GetSecurityDescriptorSacl().GetAceCount() != sacl_ace_cnt + 1:
    print("New Sacl doesn't contain extra ace ????")
if (
    win32security.LookupAccountSid("", new_sd.GetSecurityDescriptorOwner())[0]
    != "Power Users"
):
    print("Owner not successfully set to Power Users !!!!!")
if (
    win32security.LookupAccountSid("", new_sd.GetSecurityDescriptorGroup())[0]
    != "Power Users"
):
    print("Group not successfully set to Power Users !!!!!")

win32security.SetNamedSecurityInfo(
    fname,
    win32security.SE_FILE_OBJECT,
    win32security.SACL_SECURITY_INFORMATION,
    None,
    None,
    None,
    None,
)
new_sd_1 = win32security.GetNamedSecurityInfo(
    fname, win32security.SE_FILE_OBJECT, win32security.SACL_SECURITY_INFORMATION
)
if new_sd_1.GetSecurityDescriptorSacl() is not None:
    print("Unable to set Sacl to NULL !!!!!!!!")

```


---

## win32/Demos/security/setsecurityinfo.py

```python
import win32api
import win32con
import win32security

## You need SE_RESTORE_NAME to be able to set the owner of a security descriptor to anybody
## other than yourself or your primary group.  Most admin logins don't have it by default, so
## enabling it may fail
new_privs = (
    (
        win32security.LookupPrivilegeValue("", win32security.SE_SECURITY_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
    (
        win32security.LookupPrivilegeValue("", win32security.SE_TCB_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
    (
        win32security.LookupPrivilegeValue("", win32security.SE_SHUTDOWN_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
    (
        win32security.LookupPrivilegeValue("", win32security.SE_RESTORE_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
    (
        win32security.LookupPrivilegeValue("", win32security.SE_TAKE_OWNERSHIP_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
    (
        win32security.LookupPrivilegeValue("", win32security.SE_CREATE_PERMANENT_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
    (
        win32security.LookupPrivilegeValue("", win32security.SE_ENABLE_DELEGATION_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
    (
        win32security.LookupPrivilegeValue("", win32security.SE_CHANGE_NOTIFY_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
    (
        win32security.LookupPrivilegeValue("", win32security.SE_DEBUG_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
    (
        win32security.LookupPrivilegeValue(
            "", win32security.SE_PROF_SINGLE_PROCESS_NAME
        ),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
    (
        win32security.LookupPrivilegeValue("", win32security.SE_SYSTEM_PROFILE_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
    (
        win32security.LookupPrivilegeValue("", win32security.SE_LOCK_MEMORY_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
)

all_info = (
    win32security.OWNER_SECURITY_INFORMATION
    | win32security.GROUP_SECURITY_INFORMATION
    | win32security.DACL_SECURITY_INFORMATION
    | win32security.SACL_SECURITY_INFORMATION
)

pid = win32api.GetCurrentProcessId()
ph = win32api.OpenProcess(win32con.PROCESS_ALL_ACCESS, 0, pid)
## PROCESS_ALL_ACCESS does not contain ACCESS_SYSTEM_SECURITY (neccessy to do SACLs)
th = win32security.OpenProcessToken(
    ph, win32security.TOKEN_ALL_ACCESS
)  ##win32con.TOKEN_ADJUST_PRIVILEGES)
old_privs = win32security.AdjustTokenPrivileges(th, 0, new_privs)
my_sid = win32security.GetTokenInformation(th, win32security.TokenUser)[0]
pwr_sid = win32security.LookupAccountName("", "Power Users")[0]
## reopen process with ACCESS_SYSTEM_SECURITY now that sufficent privs are enabled
ph = win32api.OpenProcess(
    win32con.PROCESS_ALL_ACCESS | win32con.ACCESS_SYSTEM_SECURITY, 0, pid
)

sd = win32security.GetSecurityInfo(ph, win32security.SE_KERNEL_OBJECT, all_info)
dacl = sd.GetSecurityDescriptorDacl()
if dacl is None:
    dacl = win32security.ACL()
sacl = sd.GetSecurityDescriptorSacl()
if sacl is None:
    sacl = win32security.ACL()

dacl_ace_cnt = dacl.GetAceCount()
sacl_ace_cnt = sacl.GetAceCount()

dacl.AddAccessAllowedAce(
    dacl.GetAclRevision(), win32con.ACCESS_SYSTEM_SECURITY | win32con.WRITE_DAC, my_sid
)
sacl.AddAuditAccessAce(sacl.GetAclRevision(), win32con.GENERIC_ALL, my_sid, 1, 1)

win32security.SetSecurityInfo(
    ph, win32security.SE_KERNEL_OBJECT, all_info, pwr_sid, pwr_sid, dacl, sacl
)
new_sd = win32security.GetSecurityInfo(ph, win32security.SE_KERNEL_OBJECT, all_info)

if new_sd.GetSecurityDescriptorDacl().GetAceCount() != dacl_ace_cnt + 1:
    print("New dacl doesn't contain extra ace ????")
if new_sd.GetSecurityDescriptorSacl().GetAceCount() != sacl_ace_cnt + 1:
    print("New Sacl doesn't contain extra ace ????")
if (
    win32security.LookupAccountSid("", new_sd.GetSecurityDescriptorOwner())[0]
    != "Power Users"
):
    print("Owner not successfully set to Power Users !!!!!")
if (
    win32security.LookupAccountSid("", new_sd.GetSecurityDescriptorGroup())[0]
    != "Power Users"
):
    print("Group not successfully set to Power Users !!!!!")

win32security.SetSecurityInfo(
    ph,
    win32security.SE_KERNEL_OBJECT,
    win32security.SACL_SECURITY_INFORMATION,
    None,
    None,
    None,
    None,
)
new_sd_1 = win32security.GetSecurityInfo(
    ph, win32security.SE_KERNEL_OBJECT, win32security.SACL_SECURITY_INFORMATION
)
if new_sd_1.GetSecurityDescriptorSacl() is not None:
    print("Unable to set Sacl to NULL !!!!!!!!")

```


---

## win32/Demos/security/setuserobjectsecurity.py

```python
import win32con
import win32process
import win32security

new_privs = (
    (
        win32security.LookupPrivilegeValue("", win32security.SE_SECURITY_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
    (
        win32security.LookupPrivilegeValue("", win32security.SE_TCB_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
    (
        win32security.LookupPrivilegeValue("", win32security.SE_SHUTDOWN_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
    (
        win32security.LookupPrivilegeValue("", win32security.SE_RESTORE_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
    (
        win32security.LookupPrivilegeValue("", win32security.SE_TAKE_OWNERSHIP_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
    (
        win32security.LookupPrivilegeValue("", win32security.SE_CREATE_PERMANENT_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
    (
        win32security.LookupPrivilegeValue("", win32security.SE_ENABLE_DELEGATION_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
    (
        win32security.LookupPrivilegeValue("", win32security.SE_CHANGE_NOTIFY_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
    (
        win32security.LookupPrivilegeValue("", win32security.SE_DEBUG_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
    (
        win32security.LookupPrivilegeValue(
            "", win32security.SE_PROF_SINGLE_PROCESS_NAME
        ),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
    (
        win32security.LookupPrivilegeValue("", win32security.SE_SYSTEM_PROFILE_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
    (
        win32security.LookupPrivilegeValue("", win32security.SE_LOCK_MEMORY_NAME),
        win32con.SE_PRIVILEGE_ENABLED,
    ),
)

all_info = (
    win32security.OWNER_SECURITY_INFORMATION
    | win32security.GROUP_SECURITY_INFORMATION
    | win32security.DACL_SECURITY_INFORMATION
    | win32security.SACL_SECURITY_INFORMATION
)
info = (
    win32security.OWNER_SECURITY_INFORMATION
    | win32security.GROUP_SECURITY_INFORMATION
    | win32security.DACL_SECURITY_INFORMATION
)

ph = win32process.GetCurrentProcess()
th = win32security.OpenProcessToken(
    ph, win32security.TOKEN_ALL_ACCESS
)  ##win32con.TOKEN_ADJUST_PRIVILEGES)
win32security.AdjustTokenPrivileges(th, 0, new_privs)
my_sid = win32security.GetTokenInformation(th, win32security.TokenUser)[0]
pwr_sid = win32security.LookupAccountName("", "Power Users")[0]

h = win32process.GetProcessWindowStation()
sd = win32security.GetUserObjectSecurity(h, info)
dacl = sd.GetSecurityDescriptorDacl()
ace_cnt = dacl.GetAceCount()

dacl.AddAccessAllowedAce(
    dacl.GetAclRevision(), win32con.ACCESS_SYSTEM_SECURITY | win32con.WRITE_DAC, my_sid
)
sd.SetSecurityDescriptorDacl(1, dacl, 0)
sd.SetSecurityDescriptorGroup(pwr_sid, 0)
sd.SetSecurityDescriptorOwner(pwr_sid, 0)

win32security.SetUserObjectSecurity(h, info, sd)
new_sd = win32security.GetUserObjectSecurity(h, info)
assert new_sd.GetSecurityDescriptorDacl().GetAceCount() == ace_cnt + 1, (
    "Did not add an ace to the Dacl !!!!!!"
)
assert (
    win32security.LookupAccountSid("", new_sd.GetSecurityDescriptorOwner())[0]
    == "Power Users"
), "Owner not successfully set to Power Users !!!!!"
assert (
    win32security.LookupAccountSid("", new_sd.GetSecurityDescriptorGroup())[0]
    == "Power Users"
), "Group not successfully set to Power Users !!!!!"

```


---

## win32/Demos/security/sspi/fetch_url.py

```python
"""
Fetches a URL from a web-server supporting NTLM authentication
eg, IIS.

If no arguments are specified, a default of http://localhost/localstart.asp
is used.  This script does follow simple 302 redirections, so pointing at the
root of an IIS server is should work.
"""

import http.client  # sorry, this demo needs 2.3+
import optparse
import urllib.error
import urllib.parse
import urllib.request
from base64 import decodestring, encodestring

from sspi import ClientAuth

options = None  # set to optparse options object


def open_url(host, url):
    h = http.client.HTTPConnection(host)
    #    h.set_debuglevel(9)
    h.putrequest("GET", url)
    h.endheaders()
    resp = h.getresponse()
    print("Initial response is", resp.status, resp.reason)
    body = resp.read()
    if resp.status == 302:  # object moved
        url = "/" + resp.msg["location"]
        resp.close()
        h.putrequest("GET", url)
        h.endheaders()
        resp = h.getresponse()
        print("After redirect response is", resp.status, resp.reason)
    if options.show_headers:
        print("Initial response headers:")
        for name, val in resp.msg.items():
            print(f" {name}: {val}")
    if options.show_body:
        print(body)
    if resp.status == 401:
        # 401: Unauthorized - here is where the real work starts
        auth_info = None
        if options.user or options.domain or options.password:
            auth_info = options.user, options.domain, options.password
        ca = ClientAuth("NTLM", auth_info=auth_info)
        auth_scheme = ca.pkg_info["Name"]
        data = None
        while 1:
            err, out_buf = ca.authorize(data)
            data = out_buf[0].Buffer
            # Encode it as base64 as required by HTTP
            auth = encodestring(data).replace("\012", "")
            h.putrequest("GET", url)
            h.putheader("Authorization", auth_scheme + " " + auth)
            h.putheader("Content-Length", "0")
            h.endheaders()
            resp = h.getresponse()
            if options.show_headers:
                print("Token dance headers:")
                for name, val in resp.msg.items():
                    print(f" {name}: {val}")

            if err == 0:
                break
            else:
                if resp.status != 401:
                    print("Eeek - got response", resp.status)
                    cl = resp.msg.get("content-length")
                    if cl:
                        print(repr(resp.read(int(cl))))
                    else:
                        print("no content!")

                assert resp.status == 401, resp.status

            assert not resp.will_close, "NTLM is per-connection - must not close"
            schemes = [
                s.strip() for s in resp.msg.get("WWW-Authenticate", "").split(",")
            ]
            for scheme in schemes:
                if scheme.startswith(auth_scheme):
                    data = decodestring(scheme[len(auth_scheme) + 1 :])
                    break
            else:
                print(f"Could not find scheme '{auth_scheme}' in schemes {schemes!r}")
                break

            resp.read()
    print("Final response status is", resp.status, resp.reason)
    if resp.status == 200:
        # Worked!
        # Check we can read it again without re-authenticating.
        if resp.will_close:
            print(
                "EEEK - response will close, but NTLM is per connection - it must stay open"
            )
        body = resp.read()
        if options.show_body:
            print("Final response body:")
            print(body)
        h.putrequest("GET", url)
        h.endheaders()
        resp = h.getresponse()
        print("Second fetch response is", resp.status, resp.reason)
        if options.show_headers:
            print("Second response headers:")
            for name, val in resp.msg.items():
                print(f" {name}: {val}")

        resp.read(int(resp.msg.get("content-length", 0)))
    elif resp.status == 500:
        print("Error text")
        print(resp.read())
    else:
        if options.show_body:
            cl = resp.msg.get("content-length")
            print(resp.read(int(cl)))


if __name__ == "__main__":
    parser = optparse.OptionParser(description=__doc__)

    parser.add_option(
        "",
        "--show-body",
        action="store_true",
        help="print the body of each response as it is received",
    )

    parser.add_option(
        "",
        "--show-headers",
        action="store_true",
        help="print the headers of each response as it is received",
    )

    parser.add_option("", "--user", action="store", help="The username to login with")

    parser.add_option(
        "", "--password", action="store", help="The password to login with"
    )

    parser.add_option("", "--domain", action="store", help="The domain to login to")

    options, args = parser.parse_args()
    if not args:
        print("Run with --help for usage details")
        args = ["http://localhost/localstart.asp"]
    for url in args:
        scheme, netloc, path, params, query, fragment = urllib.parse.urlparse(url)
        if (scheme != "http") or params or query or fragment:
            parser.error("Scheme must be http, URL must be simple")

        print(f"Opening '{path}' from '{netloc}'")
        r = open_url(netloc, path)

```


---

## win32/Demos/security/sspi/simple_auth.py

```python
# A demo of basic SSPI authentication.
# There is a 'client' context and a 'server' context - typically these will
# be on different machines (here they are in the same process, but the same
# concepts apply)
import sspi
import sspicon
import win32api
import win32security


def lookup_ret_code(err):
    for k, v in sspicon.__dict__.items():
        if k[0:6] in ("SEC_I_", "SEC_E_") and v == err:
            return k


"""
pkg_name='Kerberos'
sspiclient=SSPIClient(pkg_name, win32api.GetUserName(),  ## target spn is ourself
    None, None,   ## use none for client name and authentication information for current context
    ## 'username', ('username','domain.com','passwd'),
    sspicon.ISC_REQ_INTEGRITY|sspicon.ISC_REQ_SEQUENCE_DETECT|sspicon.ISC_REQ_REPLAY_DETECT|    \
        sspicon.ISC_REQ_DELEGATE|sspicon.ISC_REQ_CONFIDENTIALITY|sspicon.ISC_REQ_USE_SESSION_KEY)
sspiserver=SSPIServer(pkg_name, None,
    sspicon.ASC_REQ_INTEGRITY|sspicon.ASC_REQ_SEQUENCE_DETECT|sspicon.ASC_REQ_REPLAY_DETECT|   \
        sspicon.ASC_REQ_DELEGATE|sspicon.ASC_REQ_CONFIDENTIALITY|sspicon.ASC_REQ_STREAM|sspicon.ASC_REQ_USE_SESSION_KEY)
"""

pkg_name = "NTLM"

# Setup the 2 contexts.
sspiclient = sspi.ClientAuth(pkg_name)
sspiserver = sspi.ServerAuth(pkg_name)

# Perform the authentication dance, each loop exchanging more information
# on the way to completing authentication.
sec_buffer = None
while 1:
    err, sec_buffer = sspiclient.authorize(sec_buffer)
    err, sec_buffer = sspiserver.authorize(sec_buffer)
    if err == 0:
        break

# The server can now impersonate the client.  In this demo the 2 users will
# always be the same.
sspiserver.ctxt.ImpersonateSecurityContext()
print("Impersonated user: ", win32api.GetUserNameEx(win32api.NameSamCompatible))
sspiserver.ctxt.RevertSecurityContext()
print("Reverted to self: ", win32api.GetUserName())

pkg_size_info = sspiclient.ctxt.QueryContextAttributes(sspicon.SECPKG_ATTR_SIZES)
# Now sign some data
msg = "some data to be encrypted ......"

sigsize = pkg_size_info["MaxSignature"]
sigbuf = win32security.PySecBufferDescType()
sigbuf.append(win32security.PySecBufferType(len(msg), sspicon.SECBUFFER_DATA))
sigbuf.append(win32security.PySecBufferType(sigsize, sspicon.SECBUFFER_TOKEN))
sigbuf[0].Buffer = msg
sspiclient.ctxt.MakeSignature(0, sigbuf, 1)
sspiserver.ctxt.VerifySignature(sigbuf, 1)

# And finally encrypt some.
trailersize = pkg_size_info["SecurityTrailer"]
encbuf = win32security.PySecBufferDescType()
encbuf.append(win32security.PySecBufferType(len(msg), sspicon.SECBUFFER_DATA))
encbuf.append(win32security.PySecBufferType(trailersize, sspicon.SECBUFFER_TOKEN))
encbuf[0].Buffer = msg
sspiclient.ctxt.EncryptMessage(0, encbuf, 1)
print(f"Encrypted data: {encbuf[0].Buffer!r}")
sspiserver.ctxt.DecryptMessage(encbuf, 1)
print(f"Encrypted data: {encbuf[0].Buffer}")

```


---

## win32/Demos/security/sspi/socket_server.py

```python
"""A sample socket server and client using SSPI authentication and encryption.

You must run with either 'client' or 'server' as arguments.  A server must be
running before a client can connect.

To use with Kerberos you should include in the client options
--target-spn=username, where 'username' is the user under which the server is
being run.

Running either the client or server as a different user can be informative.
A command-line such as the following may be useful:
`runas /user:{user} {fqp}\\python.exe {fqp}\\socket_server.py --wait client|server`

{fqp} should specify the relevant fully-qualified path names.

To use 'runas' with Kerberos, the client program will need to
specify --target-spn with the username under which the *server* is running.

See the SSPI documentation for more details.
"""

import http.client  # sorry, this demo needs 2.3+
import optparse
import socketserver
import struct
import traceback

import sspi
import win32api

options = None  # set to optparse object.


def GetUserName():
    try:
        return win32api.GetUserName()
    except win32api.error as details:
        # Seeing 'access denied' errors here for non-local users (presumably
        # without permission to login locally).  Get the fully-qualified
        # username, although a side-effect of these permission-denied errors
        # is a lack of Python codecs - so printing the Unicode value fails.
        # So just return the repr(), and avoid codecs completely.
        return repr(win32api.GetUserNameEx(win32api.NameSamCompatible))


# Send a simple "message" over a socket - send the number of bytes first,
# then the string.  Ditto for receive.
def _send_msg(s, m):
    s.send(struct.pack("i", len(m)))
    s.send(m)


def _get_msg(s):
    size_data = s.recv(struct.calcsize("i"))
    if not size_data:
        return None
    cb = struct.unpack("i", size_data)[0]
    return s.recv(cb)


class SSPISocketServer(socketserver.TCPServer):
    def __init__(self, *args, **kw):
        socketserver.TCPServer.__init__(self, *args, **kw)
        self.sa = sspi.ServerAuth(options.package)

    def verify_request(self, sock, ca):
        # Do the sspi auth dance
        self.sa.reset()
        while 1:
            data = _get_msg(sock)
            if data is None:
                return False
            try:
                err, sec_buffer = self.sa.authorize(data)
            except sspi.error as details:
                print("FAILED to authorize client:", details)
                return False

            if err == 0:
                break
            _send_msg(sock, sec_buffer[0].Buffer)
        return True

    def process_request(self, request, client_address):
        # An example using the connection once it is established.
        print("The server is running as user", GetUserName())
        self.sa.ctxt.ImpersonateSecurityContext()
        try:
            print("Having conversation with client as user", GetUserName())
            while 1:
                # we need to grab 2 bits of data - the encrypted data, and the
                # 'key'
                data = _get_msg(request)
                key = _get_msg(request)
                if data is None or key is None:
                    break
                data = self.sa.decrypt(data, key)
                print(f"Client sent: {data!r}")
        finally:
            self.sa.ctxt.RevertSecurityContext()
        self.close_request(request)
        print("The server is back to user", GetUserName())


def serve():
    s = SSPISocketServer(("localhost", options.port), None)
    print("Running test server...")
    s.serve_forever()


def sspi_client():
    c = http.client.HTTPConnection("localhost", options.port)
    c.connect()
    # Do the auth dance.
    ca = sspi.ClientAuth(options.package, targetspn=options.target_spn)
    data = None
    while 1:
        err, out_buf = ca.authorize(data)
        _send_msg(c.sock, out_buf[0].Buffer)
        if err == 0:
            break
        data = _get_msg(c.sock)
    print("Auth dance complete - sending a few encryted messages")
    # Assume out data is sensitive - encrypt the message.
    for data in "Hello from the client".split():
        blob, key = ca.encrypt(data)
        _send_msg(c.sock, blob)
        _send_msg(c.sock, key)
    c.sock.close()
    print("Client completed.")


if __name__ == "__main__":
    parser = optparse.OptionParser("%prog [options] client|server", description=__doc__)

    parser.add_option(
        "",
        "--package",
        action="store",
        default="NTLM",
        help="The SSPI package to use (eg, Kerberos) - default is NTLM",
    )

    parser.add_option(
        "",
        "--target-spn",
        action="store",
        help="""The target security provider name to use. The
                      string contents are security-package specific.  For
                      example, 'Kerberos' or 'Negotiate' require the server
                      principal name (SPN) (ie, the username) of the remote
                      process.  For NTLM this must be blank.""",
    )

    parser.add_option(
        "",
        "--port",
        action="store",
        default="8181",
        help="The port number to use (default=8181)",
    )

    parser.add_option(
        "",
        "--wait",
        action="store_true",
        help="""Cause the program to wait for input just before
                              terminating. Useful when using via runas to see
                              any error messages before termination.
                           """,
    )

    options, args = parser.parse_args()
    try:
        options.port = int(options.port)
    except (ValueError, TypeError):
        parser.error("--port must be an integer")

    try:
        try:
            if not args:
                args = [""]
            if args[0] == "client":
                sspi_client()
            elif args[0] == "server":
                serve()
            else:
                parser.error(
                    "You must supply 'client' or 'server' - use --help for details"
                )
        except KeyboardInterrupt:
            pass
        except SystemExit:
            pass
        except:
            traceback.print_exc()
    finally:
        if options.wait:
            input("Press enter to continue")

```


---

## win32/Demos/security/sspi/validate_password.py

```python
# Demonstrates how to validate a password.
# See also MSKB article Q180548
#
# To use with Kerberos you need to jump through the 'targetspn' hoops.

import sys

import win32security
from sspi import ClientAuth, ServerAuth


def validate(username, password, domain=""):
    auth_info = username, domain, password
    ca = ClientAuth("NTLM", auth_info=auth_info)
    sa = ServerAuth("NTLM")

    data = err = None
    while err != 0:
        err, data = ca.authorize(data)
        err, data = sa.authorize(data)
    # If we get here without exception, we worked!


if __name__ == "__main__":
    if len(sys.argv) not in [2, 3, 4]:
        print(f"Usage: {__file__} username [password [domain]]")
        sys.exit(1)

    # password and domain are optional!
    password = None
    if len(sys.argv) >= 3:
        password = sys.argv[2]
    domain = ""
    if len(sys.argv) >= 4:
        domain = sys.argv[3]
    try:
        validate(sys.argv[1], password, domain)
        print("Validated OK")
    except win32security.error as details:
        hr, func, msg = details
        print("Validation failed: %s (%d)" % (msg, hr))

```


---

## win32/Demos/service/nativePipeTestService.py

```python
# This is an example of a service hosted by python.exe rather than
# pythonservice.exe.

# Note that it is very rare that using python.exe is a better option
# than the default pythonservice.exe - the latter has better error handling
# so that if Python itself can't be initialized or there are very early
# import errors, you will get error details written to the event log.  When
# using python.exe instead, you are forced to wait for the interpreter startup
# and imports to succeed before you are able to effectively setup your own
# error handling.

# So in short, please make sure you *really* want to do this, otherwise just
# stick with the default.

import os
import sys

import servicemanager
import win32serviceutil
from pipeTestService import TestPipeService


class NativeTestPipeService(TestPipeService):
    _svc_name_ = "PyNativePipeTestService"
    _svc_display_name_ = "Python Native Pipe Test Service"
    _svc_description_ = "Tests Python.exe hosted services"
    # tell win32serviceutil we have a custom executable and custom args
    # so registration does the right thing.
    _exe_name_ = sys.executable
    _exe_args_ = '"' + os.path.abspath(sys.argv[0]) + '"'


def main():
    if len(sys.argv) == 1:
        # service must be starting...
        print("service is starting...")
        print("(execute this script with '--help' if that isn't what you want)")

        # for the sake of debugging etc, we use win32traceutil to see
        # any unhandled exceptions and print statements.
        import win32traceutil

        print("service is still starting...")

        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(NativeTestPipeService)
        # Now ask the service manager to fire things up for us...
        servicemanager.StartServiceCtrlDispatcher()
        print("service done!")
    else:
        win32serviceutil.HandleCommandLine(NativeTestPipeService)


if __name__ == "__main__":
    try:
        main()
    except (SystemExit, KeyboardInterrupt):
        raise
    except:
        print("Something went bad!")
        import traceback

        traceback.print_exc()

```


---

## win32/Demos/service/pipeTestService.py

```python
# A Demo of services and named pipes.

# A multi-threaded service that simply echos back its input.

# * Install as a service using "pipeTestService.py install"
# * Use Control Panel to change the user name of the service
#   to a real user name (ie, NOT the SystemAccount)
# * Start the service.
# * Run the "pipeTestServiceClient.py" program as the client pipe side.

import _thread
import traceback

import pywintypes

# Old versions of the service framework would not let you import this
# module at the top-level.  Now you can, and can check 'servicemanager.Debugging()'
# and 'servicemanager.RunningAsService()' to check your context.
import servicemanager
import win32con
import win32service
import win32serviceutil
import winerror

# # Use "import *" to keep this looking as much as a "normal" service
# as possible.  Real code shouldn't do this.
from ntsecuritycon import *
from win32api import *
from win32event import *
from win32file import *
from win32pipe import *


def ApplyIgnoreError(fn, args):
    try:
        return fn(*args)
    except error:  # Ignore win32api errors.
        return None


class TestPipeService(win32serviceutil.ServiceFramework):
    _svc_name_ = "PyPipeTestService"
    _svc_display_name_ = "Python Pipe Test Service"
    _svc_description_ = "Tests Python service framework by receiving and echoing messages over a named pipe"

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = CreateEvent(None, 0, 0, None)
        self.overlapped = pywintypes.OVERLAPPED()
        self.overlapped.hEvent = CreateEvent(None, 0, 0, None)
        self.thread_handles = []

    def CreatePipeSecurityObject(self):
        # Create a security object giving World read/write access,
        # but only "Owner" modify access.
        sa = pywintypes.SECURITY_ATTRIBUTES()
        sidEveryone = pywintypes.SID()
        sidEveryone.Initialize(SECURITY_WORLD_SID_AUTHORITY, 1)
        sidEveryone.SetSubAuthority(0, SECURITY_WORLD_RID)
        sidCreator = pywintypes.SID()
        sidCreator.Initialize(SECURITY_CREATOR_SID_AUTHORITY, 1)
        sidCreator.SetSubAuthority(0, SECURITY_CREATOR_OWNER_RID)

        acl = pywintypes.ACL()
        acl.AddAccessAllowedAce(FILE_GENERIC_READ | FILE_GENERIC_WRITE, sidEveryone)
        acl.AddAccessAllowedAce(FILE_ALL_ACCESS, sidCreator)

        sa.SetSecurityDescriptorDacl(1, acl, 0)
        return sa

    # The functions executed in their own thread to process a client request.
    def DoProcessClient(self, pipeHandle, tid):
        try:
            try:
                # Create a loop, reading large data.  If we knew the data stream was
                # was small, a simple ReadFile would do.
                d = b""
                hr = winerror.ERROR_MORE_DATA
                while hr == winerror.ERROR_MORE_DATA:
                    hr, thisd = ReadFile(pipeHandle, 256)
                    d += thisd
                print("Read", d)
                ok = 1
            except error:
                # Client disconnection - do nothing
                ok = 0

            # A secure service would handle (and ignore!) errors writing to the
            # pipe, but for the sake of this demo we don't (if only to see what errors
            # we can get when our clients break at strange times :-)
            if ok:
                msg = (
                    "%s (on thread %d) sent me %s"
                    % (GetNamedPipeHandleState(pipeHandle, False, True)[4], tid, d)
                ).encode("ascii")
                WriteFile(pipeHandle, msg)
        finally:
            ApplyIgnoreError(DisconnectNamedPipe, (pipeHandle,))
            ApplyIgnoreError(CloseHandle, (pipeHandle,))

    def ProcessClient(self, pipeHandle):
        try:
            procHandle = GetCurrentProcess()
            th = DuplicateHandle(
                procHandle,
                GetCurrentThread(),
                procHandle,
                0,
                0,
                win32con.DUPLICATE_SAME_ACCESS,
            )
            try:
                self.thread_handles.append(th)
                try:
                    return self.DoProcessClient(pipeHandle, th)
                except:
                    traceback.print_exc()
            finally:
                self.thread_handles.remove(th)
        except:
            traceback.print_exc()

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        # Write an event log record - in debug mode we will also
        # see this message printed.
        servicemanager.LogMsg(
            servicemanager.EVENTLOG_INFORMATION_TYPE,
            servicemanager.PYS_SERVICE_STARTED,
            (self._svc_name_, ""),
        )

        num_connections = 0
        while 1:
            pipeHandle = CreateNamedPipe(
                "\\\\.\\pipe\\PyPipeTest",
                PIPE_ACCESS_DUPLEX | FILE_FLAG_OVERLAPPED,
                PIPE_TYPE_MESSAGE | PIPE_READMODE_BYTE,
                PIPE_UNLIMITED_INSTANCES,  # max instances
                0,
                0,
                6000,
                self.CreatePipeSecurityObject(),
            )
            try:
                hr = ConnectNamedPipe(pipeHandle, self.overlapped)
            except error as details:
                print("Error connecting pipe!", details)
                CloseHandle(pipeHandle)
                break
            if hr == winerror.ERROR_PIPE_CONNECTED:
                # Client is already connected - signal event
                SetEvent(self.overlapped.hEvent)
            rc = WaitForMultipleObjects(
                (self.hWaitStop, self.overlapped.hEvent), 0, INFINITE
            )
            if rc == WAIT_OBJECT_0:
                # Stop event
                break
            else:
                # Pipe event - spawn thread to deal with it.
                _thread.start_new_thread(self.ProcessClient, (pipeHandle,))
                num_connections += 1

        # Sleep to ensure that any new threads are in the list, and then
        # wait for all current threads to finish.
        # What is a better way?
        Sleep(500)
        while self.thread_handles:
            self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING, 5000)
            print("Waiting for %d threads to finish..." % (len(self.thread_handles)))
            WaitForMultipleObjects(self.thread_handles, 1, 3000)
        # Write another event log record.
        servicemanager.LogMsg(
            servicemanager.EVENTLOG_INFORMATION_TYPE,
            servicemanager.PYS_SERVICE_STOPPED,
            (self._svc_name_, " after processing %d connections" % (num_connections,)),
        )


if __name__ == "__main__":
    win32serviceutil.HandleCommandLine(TestPipeService)

```


---

## win32/Demos/service/pipeTestServiceClient.py

```python
# A Test Program for pipeTestService.py
#
# Install and start the Pipe Test service, then run this test
# either from the same machine, or from another using the "-s" param.
#
# Eg: pipeTestServiceClient.py -s server_name Hi There
# Should work.

import os
import sys
import traceback

import pywintypes
import win32api
import winerror

# # Use "import *" to keep this looking as much as a "normal" service
# as possible.  Real code shouldn't do this.
from win32event import *
from win32file import *
from win32pipe import *

verbose = 0

# def ReadFromPipe(pipeName):
# Could (Should?) use CallNamedPipe, but this technique allows variable size
# messages (whereas you must supply a buffer size for CallNamedPipe!
#       hPipe = CreateFile(pipeName, GENERIC_WRITE, 0, None, OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, 0)
#       more = 1
#       while more:
#               hr = ReadFile(hPipe, 256)
#               if hr==0:
#                       more = 0
#               except win32api.error (hr, fn, desc):
#                       if hr==winerror.ERROR_MORE_DATA:
#                               data = dat
#


def CallPipe(fn, args):
    ret = None
    retryCount = 0
    while retryCount < 8:  # Keep looping until user cancels.
        retryCount += 1
        try:
            return fn(*args)
        except win32api.error as exc:
            if exc.winerror == winerror.ERROR_PIPE_BUSY:
                win32api.Sleep(5000)
                continue
            else:
                raise

    raise RuntimeError("Could not make a connection to the server")


def testClient(server, msg):
    if verbose:
        print("Sending", msg)
    data = CallPipe(
        CallNamedPipe,
        ("\\\\%s\\pipe\\PyPipeTest" % server, msg, 256, NMPWAIT_WAIT_FOREVER),
    )
    if verbose:
        print("Server sent back '%s'" % data)
    print("Sent and received a message!")


def testLargeMessage(server, size=4096):
    if verbose:
        print("Sending message of size %d" % (size))
    msg = "*" * size
    data = CallPipe(
        CallNamedPipe,
        ("\\\\%s\\pipe\\PyPipeTest" % server, msg, 512, NMPWAIT_WAIT_FOREVER),
    )
    if len(data) - size:
        print("Sizes are all wrong - send %d, got back %d" % (size, len(data)))


def stressThread(server, numMessages, wait):
    try:
        try:
            for i in range(numMessages):
                r = CallPipe(
                    CallNamedPipe,
                    (
                        "\\\\%s\\pipe\\PyPipeTest" % server,
                        "#" * 512,
                        1024,
                        NMPWAIT_WAIT_FOREVER,
                    ),
                )
        except:
            traceback.print_exc()
            print("Failed after %d messages" % i)
    finally:
        SetEvent(wait)


def stressTestClient(server, numThreads, numMessages):
    import _thread

    thread_waits = []
    for t_num in range(numThreads):
        # Note I could just wait on thread handles (after calling DuplicateHandle)
        # See the service itself for an example of waiting for the clients...
        wait = CreateEvent(None, 0, 0, None)
        thread_waits.append(wait)
        _thread.start_new_thread(stressThread, (server, numMessages, wait))
    # Wait for all threads to finish.
    WaitForMultipleObjects(thread_waits, 1, INFINITE)


def main():
    import getopt

    server = "."
    thread_count = 0
    msg_count = 500
    try:
        opts, args = getopt.getopt(sys.argv[1:], "s:t:m:vl")
        for o, a in opts:
            if o == "-s":
                server = a
            if o == "-m":
                msg_count = int(a)
            if o == "-t":
                thread_count = int(a)
            if o == "-v":
                global verbose
                verbose = 1
            if o == "-l":
                testLargeMessage(server)
        msg = " ".join(args).encode("mbcs")
    except getopt.error as msg:
        print(msg)
        my_name = os.path.split(sys.argv[0])[1]
        print(
            "Usage: %s [-v] [-s server] [-t thread_count=0] [-m msg_count=500] msg ..."
            % my_name
        )
        print("       -v = verbose")
        print(
            "       Specifying a value for -t will stress test using that many threads."
        )
        return
    testClient(server, msg)
    if thread_count > 0:
        print(
            "Spawning %d threads each sending %d messages..."
            % (thread_count, msg_count)
        )
        stressTestClient(server, thread_count, msg_count)


if __name__ == "__main__":
    main()

```


---

## win32/Demos/service/serviceEvents.py

```python
# A Demo of a service that takes advantage of the additional notifications
# available in later Windows versions.

# Note that all output is written as event log entries - so you must install
# and start the service, then look at the event log for messages as events
# are generated.

# Events are generated for USB device insertion and removal, power state
# changes and hardware profile events - so try putting your computer to
# sleep and waking it, inserting a memory stick, etc then check the event log

# Most event notification support lives around win32gui
import servicemanager
import win32con
import win32event
import win32gui
import win32gui_struct
import win32service
import win32serviceutil

GUID_DEVINTERFACE_USB_DEVICE = "{A5DCBF10-6530-11D2-901F-00C04FB951ED}"


class EventDemoService(win32serviceutil.ServiceFramework):
    _svc_name_ = "PyServiceEventDemo"
    _svc_display_name_ = "Python Service Event Demo"
    _svc_description_ = (
        "Demonstrates a Python service which takes advantage of the extra notifications"
    )

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        # register for a device notification - we pass our service handle
        # instead of a window handle.
        filter = win32gui_struct.PackDEV_BROADCAST_DEVICEINTERFACE(
            GUID_DEVINTERFACE_USB_DEVICE
        )
        self.hdn = win32gui.RegisterDeviceNotification(
            self.ssh, filter, win32con.DEVICE_NOTIFY_SERVICE_HANDLE
        )

    # Override the base class so we can accept additional events.
    def GetAcceptedControls(self):
        # say we accept them all.
        rc = win32serviceutil.ServiceFramework.GetAcceptedControls(self)
        rc |= (
            win32service.SERVICE_ACCEPT_PARAMCHANGE
            | win32service.SERVICE_ACCEPT_NETBINDCHANGE
            | win32service.SERVICE_CONTROL_DEVICEEVENT
            | win32service.SERVICE_ACCEPT_HARDWAREPROFILECHANGE
            | win32service.SERVICE_ACCEPT_POWEREVENT
            | win32service.SERVICE_ACCEPT_SESSIONCHANGE
        )
        return rc

    # All extra events are sent via SvcOtherEx (SvcOther remains as a
    # function taking only the first args for backwards compat)
    def SvcOtherEx(self, control, event_type, data):
        # This is only showing a few of the extra events - see the MSDN
        # docs for "HandlerEx callback" for more info.
        if control == win32service.SERVICE_CONTROL_DEVICEEVENT:
            info = win32gui_struct.UnpackDEV_BROADCAST(data)
            msg = f"A device event occurred: {event_type:x} - {info}"
        elif control == win32service.SERVICE_CONTROL_HARDWAREPROFILECHANGE:
            msg = f"A hardware profile changed: type={event_type}, data={data}"
        elif control == win32service.SERVICE_CONTROL_POWEREVENT:
            msg = "A power event: setting %s" % data
        elif control == win32service.SERVICE_CONTROL_SESSIONCHANGE:
            # data is a single elt tuple, but this could potentially grow
            # in the future if the win32 struct does
            msg = f"Session event: type={event_type}, data={data}"
        else:
            msg = "Other event: code=%d, type=%s, data=%s" % (control, event_type, data)

        servicemanager.LogMsg(
            servicemanager.EVENTLOG_INFORMATION_TYPE,
            0xF000,  #  generic message
            (msg, ""),
        )

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        # do nothing at all - just wait to be stopped
        win32event.WaitForSingleObject(self.hWaitStop, win32event.INFINITE)
        # Write a stop message.
        servicemanager.LogMsg(
            servicemanager.EVENTLOG_INFORMATION_TYPE,
            servicemanager.PYS_SERVICE_STOPPED,
            (self._svc_name_, ""),
        )


if __name__ == "__main__":
    win32serviceutil.HandleCommandLine(EventDemoService)

```


---

## win32/Demos/timer_demo.py

```python
# -*- Mode: Python; tab-width: 4 -*-
#

# This module, and the timer.pyd core timer support, were written by
# Sam Rushing (rushing@nightmare.com)

import time

# Timers are based on Windows messages.  So we need
# to do the event-loop thing!
import timer
import win32event
import win32gui

# glork holds a simple counter for us.


class glork:
    def __init__(self, delay=1000, max=10):
        self.x = 0
        self.max = max
        self.id = timer.set_timer(delay, self.increment)
        # Could use the threading module, but this is
        # a win32 extension test after all! :-)
        self.event = win32event.CreateEvent(None, 0, 0, None)

    def increment(self, id, time):
        print("x = %d" % self.x)
        self.x += 1
        # if we've reached the max count,
        # kill off the timer.
        if self.x > self.max:
            # we could have used 'self.id' here, too
            timer.kill_timer(id)
            win32event.SetEvent(self.event)


# create a counter that will count from '1' thru '10', incrementing
# once a second, and then stop.


def demo(delay=1000, stop=10):
    g = glork(delay, stop)
    # Timers are message based - so we need
    # To run a message loop while waiting for our timers
    # to expire.
    start_time = time.time()
    while 1:
        # We can't simply give a timeout of 30 seconds, as
        # we may continouusly be recieving other input messages,
        # and therefore never expire.
        rc = win32event.MsgWaitForMultipleObjects(
            (g.event,),  # list of objects
            0,  # wait all
            500,  # timeout
            win32event.QS_ALLEVENTS,  # type of input
        )
        if rc == win32event.WAIT_OBJECT_0:
            # Event signalled.
            break
        elif rc == win32event.WAIT_OBJECT_0 + 1:
            # Message waiting.
            if win32gui.PumpWaitingMessages():
                raise RuntimeError("We got an unexpected WM_QUIT message!")
        else:
            # This wait timed-out.
            if time.time() - start_time > 30:
                raise RuntimeError("We timed out waiting for the timers to expire!")


if __name__ == "__main__":
    demo()

```


---

## win32/Demos/win32clipboardDemo.py

```python
# win32clipboardDemo.py
#
# Demo/test of the win32clipboard module.
import win32con
from win32clipboard import (
    CloseClipboard,
    EmptyClipboard,
    EnumClipboardFormats,
    GetClipboardData,
    GetClipboardFormatName,
    IsClipboardFormatAvailable,
    OpenClipboard,
    RegisterClipboardFormat,
    SetClipboardData,
    SetClipboardText,
)

if not __debug__:
    print("WARNING: The test code in this module uses assert")
    print("This instance of Python has asserts disabled, so many tests will be skipped")

# Build map of CF_* constants to names.
cf_names = {
    val: name
    for name, val in win32con.__dict__.items()
    if name[:3] == "CF_" and name != "CF_SCREENFONTS"  # CF_SCREEN_FONTS==CF_TEXT!?!?
}


def TestEmptyClipboard():
    OpenClipboard()
    try:
        EmptyClipboard()
        assert EnumClipboardFormats(0) == 0, (
            "Clipboard formats were available after emptying it!"
        )
    finally:
        CloseClipboard()


def TestText():
    OpenClipboard()
    try:
        text = "Hello from Python"
        text_bytes = text.encode("latin1")
        SetClipboardText(text)
        got = GetClipboardData(win32con.CF_TEXT)
        # CF_TEXT always gives us 'bytes' back .
        assert got == text_bytes, f"Didn't get the correct result back - '{got!r}'."
    finally:
        CloseClipboard()

    OpenClipboard()
    try:
        # CF_UNICODE text always gives unicode objects back.
        got = GetClipboardData(win32con.CF_UNICODETEXT)
        assert got == text, f"Didn't get the correct result back - '{got!r}'."
        assert isinstance(got, str), f"Didn't get the correct result back - '{got!r}'."

        # CF_OEMTEXT is a bytes-based format.
        got = GetClipboardData(win32con.CF_OEMTEXT)
        assert got == text_bytes, f"Didn't get the correct result back - '{got!r}'."

        # Unicode tests
        EmptyClipboard()
        text = "Hello from Python unicode"
        text_bytes = text.encode("latin1")
        # Now set the Unicode value
        SetClipboardData(win32con.CF_UNICODETEXT, text)
        # Get it in Unicode.
        got = GetClipboardData(win32con.CF_UNICODETEXT)
        assert got == text, f"Didn't get the correct result back - '{got!r}'."
        assert isinstance(got, str), f"Didn't get the correct result back - '{got!r}'."

        # Close and open the clipboard to ensure auto-conversions take place.
    finally:
        CloseClipboard()

    OpenClipboard()
    try:
        # Make sure I can still get the text as bytes
        got = GetClipboardData(win32con.CF_TEXT)
        assert got == text_bytes, f"Didn't get the correct result back - '{got!r}'."
        # Make sure we get back the correct types.
        got = GetClipboardData(win32con.CF_UNICODETEXT)
        assert isinstance(got, str), f"Didn't get the correct result back - '{got!r}'."
        got = GetClipboardData(win32con.CF_OEMTEXT)
        assert got == text_bytes, f"Didn't get the correct result back - '{got!r}'."
        print("Clipboard text tests worked correctly")
    finally:
        CloseClipboard()


def TestClipboardEnum():
    OpenClipboard()
    try:
        # Enumerate over the clipboard types
        enum = 0
        while 1:
            enum = EnumClipboardFormats(enum)
            if enum == 0:
                break
            assert IsClipboardFormatAvailable(enum), (
                "Have format, but clipboard says it is not available!"
            )
            n = cf_names.get(enum, "")
            if not n:
                try:
                    n = GetClipboardFormatName(enum)
                except error:
                    n = f"unknown ({enum})"

            print("Have format", n)
        print("Clipboard enumerator tests worked correctly")
    finally:
        CloseClipboard()


class Foo:
    def __init__(self, **kw):
        self.__dict__.update(kw)

    def __lt__(self, other):
        return self.__dict__ < other.__dict__

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


def TestCustomFormat():
    OpenClipboard()
    try:
        # Just for the fun of it pickle Python objects through the clipboard
        fmt = RegisterClipboardFormat("Python Pickle Format")
        import pickle

        pickled_object = Foo(a=1, b=2, Hi=3)
        SetClipboardData(fmt, pickle.dumps(pickled_object))
        # Now read it back.
        data = GetClipboardData(fmt)
        loaded_object = pickle.loads(data)
        assert pickle.loads(data) == pickled_object, "Didn't get the correct data!"

        print("Clipboard custom format tests worked correctly")
    finally:
        CloseClipboard()


if __name__ == "__main__":
    TestEmptyClipboard()
    TestText()
    TestCustomFormat()
    TestClipboardEnum()
    # And leave it empty at the end!
    TestEmptyClipboard()

```


---

## win32/Demos/win32clipboard_bitmapdemo.py

```python
import win32api
import win32clipboard
import win32con
import win32gui


class ViewerWindow:
    def __init__(self):
        self.hwndNextViewer = None

    def OnPaint(self, hwnd, msg, wp, lp):
        dc, ps = win32gui.BeginPaint(hwnd)
        wndrect = win32gui.GetClientRect(hwnd)
        wndwidth = wndrect[2] - wndrect[0]
        wndheight = wndrect[3] - wndrect[1]
        win32clipboard.OpenClipboard()
        try:
            try:
                hbitmap = win32clipboard.GetClipboardData(win32clipboard.CF_BITMAP)
            except TypeError:
                font = win32gui.LOGFONT()
                font.lfHeight = 15  # int(wndheight/20)
                font.lfWidth = 15  # font.lfHeight
                #            font.lfWeight=150
                hf = win32gui.CreateFontIndirect(font)
                win32gui.SelectObject(dc, hf)
                win32gui.SetBkMode(dc, win32con.TRANSPARENT)
                win32gui.SetTextColor(dc, win32api.RGB(0, 0, 0))
                win32gui.DrawText(
                    dc,
                    "No bitmaps are in the clipboard\n(try pressing the PrtScn button)",
                    -1,
                    (0, 0, wndwidth, wndheight),
                    win32con.DT_CENTER,
                )
            else:
                bminfo = win32gui.GetObject(hbitmap)
                dcDC = win32gui.CreateCompatibleDC(None)
                win32gui.SelectObject(dcDC, hbitmap)
                win32gui.StretchBlt(
                    dc,
                    0,
                    0,
                    wndwidth,
                    wndheight,
                    dcDC,
                    0,
                    0,
                    bminfo.bmWidth,
                    bminfo.bmHeight,
                    win32con.SRCCOPY,
                )
                win32gui.DeleteDC(dcDC)
                win32gui.EndPaint(hwnd, ps)
        finally:
            win32clipboard.CloseClipboard()
        return 0

    def OnDrawClipboard(self, hwnd, msg, wp, lp):
        win32gui.InvalidateRect(hwnd, None, True)

    def OnChangeCBChain(self, hwnd, msg, wp, lp):
        # If the next window is closing, repair the chain.
        if wp == self.hwndNextViewer:
            self.hwndNextViewer = lp
        # Otherwise, pass the message to the next link.
        elif self.hwndNextViewer:
            win32gui.SendMessage(self.hwndNextViewer, msg, wp, lp)

    def OnCreate(self, hwnd, msg, wp, lp):
        self.hwndNextViewer = win32gui.SetClipboardViewer(hwnd)

    def OnClose(self, hwnd, msg, wp, lp):
        win32clipboard.ChangeClipboardChain(hwnd, self.hwndNextViewer)
        win32gui.DestroyWindow(hwnd)
        win32gui.PostQuitMessage(0)

    def go(self):
        wndproc = {
            win32con.WM_PAINT: self.OnPaint,
            win32con.WM_CLOSE: self.OnClose,
            win32con.WM_CREATE: self.OnCreate,
            win32con.WM_DRAWCLIPBOARD: self.OnDrawClipboard,
            win32con.WM_CHANGECBCHAIN: self.OnChangeCBChain,
        }

        wc = win32gui.WNDCLASS()
        wc.lpszClassName = "test_win32clipboard_bmp"
        wc.style = win32con.CS_GLOBALCLASS | win32con.CS_VREDRAW | win32con.CS_HREDRAW
        wc.hbrBackground = win32con.COLOR_WINDOW + 1
        wc.lpfnWndProc = wndproc
        class_atom = win32gui.RegisterClass(wc)
        hwnd = win32gui.CreateWindowEx(
            0,
            class_atom,
            "ClipboardViewer",
            win32con.WS_CAPTION
            | win32con.WS_VISIBLE
            | win32con.WS_THICKFRAME
            | win32con.WS_SYSMENU,
            100,
            100,
            900,
            900,
            0,
            0,
            0,
            None,
        )
        win32clipboard.SetClipboardViewer(hwnd)
        win32gui.PumpMessages()
        win32gui.UnregisterClass(class_atom, None)


if __name__ == "__main__":
    w = ViewerWindow()
    w.go()

```


---

## win32/Demos/win32comport_demo.py

```python
# This is a simple serial port terminal demo.
#
# Its primary purpose is to demonstrate the native serial port access offered via
# win32file.

# It uses 3 threads:
# - The main thread, which cranks up the other 2 threads, then simply waits for them to exit.
# - The user-input thread - blocks waiting for a keyboard character, and when found sends it
#   out the COM port.  If the character is Ctrl+C, it stops, signalling the COM port thread to stop.
# - The COM port thread is simply listening for input on the COM port, and prints it to the screen.

# This demo uses userlapped IO, so that none of the read or write operations actually block (however,
# in this sample, the very next thing we do _is_ block - so it shows off the concepts even though it
# doesn't exploit them.

import msvcrt  # For the getch() function.
import sys
import threading

import win32con  # constants.
from win32event import (  # We use events and the WaitFor[Multiple]Objects functions.
    INFINITE,
    WAIT_OBJECT_0,
    CreateEvent,
    SetEvent,
    WaitForMultipleObjects,
    WaitForSingleObject,
)
from win32file import (  # The base COM port and file IO functions.
    CBR_115200,
    EV_RXCHAR,
    NOPARITY,
    ONESTOPBIT,
    OVERLAPPED,
    PURGE_RXABORT,
    PURGE_RXCLEAR,
    PURGE_TXABORT,
    PURGE_TXCLEAR,
    ClearCommError,
    CreateFile,
    GetCommModemStatus,
    GetCommState,
    PurgeComm,
    ReadFile,
    SetCommMask,
    SetCommState,
    SetCommTimeouts,
    SetupComm,
    WaitCommEvent,
    WriteFile,
    error,
)


def FindModem():
    # Snoop over the comports, seeing if it is likely we have a modem.
    for i in range(1, 5):
        port = "COM%d" % (i,)
        try:
            handle = CreateFile(
                port,
                win32con.GENERIC_READ | win32con.GENERIC_WRITE,
                0,  # exclusive access
                None,  # no security
                win32con.OPEN_EXISTING,
                win32con.FILE_ATTRIBUTE_NORMAL,
                None,
            )
            # It appears that an available COM port will always success here,
            # just return 0 for the status flags.  We only care that it has _any_ status
            # flags (and therefore probably a real modem)
            if GetCommModemStatus(handle) != 0:
                return port
        except error:
            pass  # No port, or modem status failed.
    return None


# A basic synchronous COM port file-like object
class SerialTTY:
    def __init__(self, port):
        if isinstance(port, int):
            port = "COM%d" % (port,)
        self.handle = CreateFile(
            port,
            win32con.GENERIC_READ | win32con.GENERIC_WRITE,
            0,  # exclusive access
            None,  # no security
            win32con.OPEN_EXISTING,
            win32con.FILE_ATTRIBUTE_NORMAL | win32con.FILE_FLAG_OVERLAPPED,
            None,
        )
        # Tell the port we want a notification on each char.
        SetCommMask(self.handle, EV_RXCHAR)
        # Setup a 4k buffer
        SetupComm(self.handle, 4096, 4096)
        # Remove anything that was there
        PurgeComm(
            self.handle, PURGE_TXABORT | PURGE_RXABORT | PURGE_TXCLEAR | PURGE_RXCLEAR
        )
        # Setup for overlapped IO.
        timeouts = 0xFFFFFFFF, 0, 1000, 0, 1000
        SetCommTimeouts(self.handle, timeouts)
        # Setup the connection info.
        dcb = GetCommState(self.handle)
        dcb.BaudRate = CBR_115200
        dcb.ByteSize = 8
        dcb.Parity = NOPARITY
        dcb.StopBits = ONESTOPBIT
        SetCommState(self.handle, dcb)
        print(f"Connected to {port} at {dcb.BaudRate} baud")

    def _UserInputReaderThread(self):
        overlapped = OVERLAPPED()
        overlapped.hEvent = CreateEvent(None, 1, 0, None)
        try:
            while 1:
                ch = msvcrt.getch()
                if ord(ch) == 3:
                    break
                WriteFile(self.handle, ch, overlapped)
                # Wait for the write to complete.
                WaitForSingleObject(overlapped.hEvent, INFINITE)
        finally:
            SetEvent(self.eventStop)

    def _ComPortThread(self):
        overlapped = OVERLAPPED()
        overlapped.hEvent = CreateEvent(None, 1, 0, None)
        while 1:
            # XXX - note we could _probably_ just use overlapped IO on the win32file.ReadFile() statement
            # XXX but this tests the COM stuff!
            rc, mask = WaitCommEvent(self.handle, overlapped)
            if rc == 0:  # Character already ready!
                SetEvent(overlapped.hEvent)
            rc = WaitForMultipleObjects(
                [overlapped.hEvent, self.eventStop], 0, INFINITE
            )
            if rc == WAIT_OBJECT_0:
                # Some input - read and print it
                flags, comstat = ClearCommError(self.handle)
                rc, data = ReadFile(self.handle, comstat.cbInQue, overlapped)
                WaitForSingleObject(overlapped.hEvent, INFINITE)
                sys.stdout.write(data)
            else:
                # Stop the thread!
                # Just incase the user input thread uis still going, close it
                sys.stdout.close()
                break

    def Run(self):
        self.eventStop = CreateEvent(None, 0, 0, None)
        # Start the reader and writer threads.
        user_thread = threading.Thread(target=self._UserInputReaderThread)
        user_thread.start()
        com_thread = threading.Thread(target=self._ComPortThread)
        com_thread.start()
        user_thread.join()
        com_thread.join()


if __name__ == "__main__":
    print("Serial port terminal demo - press Ctrl+C to exit")
    if len(sys.argv) <= 1:
        port = FindModem()
        if port is None:
            print("No COM port specified, and no modem could be found")
            print("Please re-run this script with the name of a COM port (eg COM3)")
            sys.exit(1)
    else:
        port = sys.argv[1]

    tty = SerialTTY(port)
    tty.Run()

```


---

## win32/Demos/win32console_demo.py

```python
import time

import win32con
import win32console

virtual_keys = {k: v for k, v in win32con.__dict__.items() if k.startswith("VK_")}

free_console = True
try:
    win32console.AllocConsole()
except win32console.error as exc:
    if exc.winerror != 5:
        raise
    ## only free console if one was created successfully
    free_console = False

stdout = win32console.GetStdHandle(win32console.STD_OUTPUT_HANDLE)
stdin = win32console.GetStdHandle(win32console.STD_INPUT_HANDLE)
newbuffer = win32console.CreateConsoleScreenBuffer()
newbuffer.SetConsoleActiveScreenBuffer()
newbuffer.SetConsoleTextAttribute(
    win32console.FOREGROUND_RED
    | win32console.FOREGROUND_INTENSITY
    | win32console.BACKGROUND_GREEN
    | win32console.BACKGROUND_INTENSITY
)
newbuffer.WriteConsole("This is a new screen buffer\n")

## test setting screen buffer and window size
## screen buffer size cannot be smaller than window size
window_size = newbuffer.GetConsoleScreenBufferInfo()["Window"]
coord = win32console.PyCOORDType(X=window_size.Right + 20, Y=window_size.Bottom + 20)
newbuffer.SetConsoleScreenBufferSize(coord)

window_size.Right += 10
window_size.Bottom += 10
newbuffer.SetConsoleWindowInfo(Absolute=True, ConsoleWindow=window_size)

## write some records to the input queue
x = win32console.PyINPUT_RECORDType(win32console.KEY_EVENT)
x.Char = "X"
x.KeyDown = True
x.RepeatCount = 1
x.VirtualKeyCode = 0x58
x.ControlKeyState = win32con.SHIFT_PRESSED

z = win32console.PyINPUT_RECORDType(win32console.KEY_EVENT)
z.Char = "Z"
z.KeyDown = True
z.RepeatCount = 1
z.VirtualKeyCode = 0x5A
z.ControlKeyState = win32con.SHIFT_PRESSED

stdin.WriteConsoleInput([x, z, x])

newbuffer.SetConsoleTextAttribute(
    win32console.FOREGROUND_RED
    | win32console.FOREGROUND_INTENSITY
    | win32console.BACKGROUND_GREEN
    | win32console.BACKGROUND_INTENSITY
)
newbuffer.WriteConsole("Press some keys, click some characters with the mouse\n")

newbuffer.SetConsoleTextAttribute(
    win32console.FOREGROUND_BLUE
    | win32console.FOREGROUND_INTENSITY
    | win32console.BACKGROUND_RED
    | win32console.BACKGROUND_INTENSITY
)
newbuffer.WriteConsole('Hit "End" key to quit\n')

breakout = False
while not breakout:
    input_records = stdin.ReadConsoleInput(10)
    for input_record in input_records:
        if input_record.EventType == win32console.KEY_EVENT:
            if input_record.KeyDown:
                if input_record.Char == "\0":
                    newbuffer.WriteConsole(
                        virtual_keys.get(
                            input_record.VirtualKeyCode,
                            "VirtualKeyCode: %s" % input_record.VirtualKeyCode,
                        )
                    )
                else:
                    newbuffer.WriteConsole(input_record.Char)
                if input_record.VirtualKeyCode == win32con.VK_END:
                    breakout = True
                    break
        elif input_record.EventType == win32console.MOUSE_EVENT:
            if input_record.EventFlags == 0:  ## 0 indicates a button event
                if input_record.ButtonState != 0:  ## exclude button releases
                    pos = input_record.MousePosition
                    # switch the foreground and background colors of the character that was clicked
                    attr = newbuffer.ReadConsoleOutputAttribute(
                        Length=1, ReadCoord=pos
                    )[0]
                    new_attr = attr
                    if attr & win32console.FOREGROUND_BLUE:
                        new_attr = (
                            new_attr & ~win32console.FOREGROUND_BLUE
                        ) | win32console.BACKGROUND_BLUE
                    if attr & win32console.FOREGROUND_RED:
                        new_attr = (
                            new_attr & ~win32console.FOREGROUND_RED
                        ) | win32console.BACKGROUND_RED
                    if attr & win32console.FOREGROUND_GREEN:
                        new_attr = (
                            new_attr & ~win32console.FOREGROUND_GREEN
                        ) | win32console.BACKGROUND_GREEN

                    if attr & win32console.BACKGROUND_BLUE:
                        new_attr = (
                            new_attr & ~win32console.BACKGROUND_BLUE
                        ) | win32console.FOREGROUND_BLUE
                    if attr & win32console.BACKGROUND_RED:
                        new_attr = (
                            new_attr & ~win32console.BACKGROUND_RED
                        ) | win32console.FOREGROUND_RED
                    if attr & win32console.BACKGROUND_GREEN:
                        new_attr = (
                            new_attr & ~win32console.BACKGROUND_GREEN
                        ) | win32console.FOREGROUND_GREEN
                    newbuffer.WriteConsoleOutputAttribute((new_attr,), pos)
        else:
            newbuffer.WriteConsole(str(input_record))
    time.sleep(0.1)

stdout.SetConsoleActiveScreenBuffer()
newbuffer.Close()
if free_console:
    win32console.FreeConsole()

```


---

## win32/Demos/win32cred_demo.py

```python
"""
Demonstrates prompting for credentials, saving, and loggging on with marshalled credential.
Also shows how to load user's profile
"""

import win32api
import win32con
import win32cred
import win32net
import win32profile
import win32security

## Prompt for a username/pwd for local computer
uiinfo = {
    "MessageText": "Enter credentials for local machine",
    "CaptionText": "win32cred_demo.py",
}
target, pwd, save = win32cred.CredUIPromptForCredentials(
    TargetName=win32api.GetComputerName(),
    AuthError=0,
    Flags=win32cred.CREDUI_FLAGS_DO_NOT_PERSIST
    | win32cred.CREDUI_FLAGS_SHOW_SAVE_CHECK_BOX,
    Save=False,
    UiInfo=uiinfo,
)

attrs = [
    {"Keyword": "attr1", "Flags": 0, "Value": "unicode data"},
    {"Keyword": "attr2", "Flags": 0, "Value": b"character data"},
]
cred = {
    "Comment": "Created by win32cred_demo.py",
    "UserName": target,
    "TargetAlias": None,
    "TargetName": target,
    "CredentialBlob": pwd,
    "Flags": win32cred.CRED_FLAGS_USERNAME_TARGET,
    "Persist": win32cred.CRED_PERSIST_ENTERPRISE,
    "Type": win32cred.CRED_TYPE_DOMAIN_PASSWORD,
    "Attributes": attrs,
}
win32cred.CredWrite(cred)
pwd = None
print(win32cred.CredRead(target, win32cred.CRED_TYPE_DOMAIN_PASSWORD))

## Marshal saved credential and use it to log on
mc = win32cred.CredMarshalCredential(win32cred.UsernameTargetCredential, target)

# As of pywin32 301 this no longer works for markh and unclear when it stopped, or
# even if it ever did! # Fails in Python 2.7 too, so not a Python 3 regression.
try:
    th = win32security.LogonUser(
        mc,
        None,
        "",
        win32con.LOGON32_LOGON_INTERACTIVE,
        win32con.LOGON32_PROVIDER_DEFAULT,
    )
    win32security.ImpersonateLoggedOnUser(th)
    print("GetUserName:", win32api.GetUserName())
    win32security.RevertToSelf()

    ## Load user's profile.  (first check if user has a roaming profile)
    username, domain = win32cred.CredUIParseUserName(target)
    user_info_4 = win32net.NetUserGetInfo(None, username, 4)
    profilepath = user_info_4["profile"]
    ## LoadUserProfile apparently doesn't like an empty string
    if not profilepath:
        profilepath = None

    ## leave Flags in since 2.3 still chokes on some types of optional keyword args
    hk = win32profile.LoadUserProfile(
        th, {"UserName": username, "Flags": 0, "ProfilePath": profilepath}
    )
    ## Get user's environment variables in a form that can be passed to win32process.CreateProcessAsUser
    env = win32profile.CreateEnvironmentBlock(th, False)

    ## Cleanup should probably be in a finally block
    win32profile.UnloadUserProfile(th, hk)
    th.Close()
except win32security.error as exc:
    print("Failed to login for some reason", exc)

```


---

## win32/Demos/win32fileDemo.py

```python
# This is a "demo" of win32file - it used to be more a test case than a
# demo, so has been moved to the test directory.

import os

# Please contribute your favourite simple little demo.
import win32api
import win32con
import win32file


# A very simple demo - note that this does no more than you can do with
# builtin Python file objects, so for something as simple as this, you
# generally *should* use builtin Python objects.  Only use win32file etc
# when you need win32 specific features not available in Python.
def SimpleFileDemo():
    testName = os.path.join(win32api.GetTempPath(), "win32file_demo_test_file")
    if os.path.exists(testName):
        os.unlink(testName)
    # Open the file for writing.
    handle = win32file.CreateFile(
        testName, win32file.GENERIC_WRITE, 0, None, win32con.CREATE_NEW, 0, None
    )
    test_data = b"Hello\0there"
    win32file.WriteFile(handle, test_data)
    handle.Close()
    # Open it for reading.
    handle = win32file.CreateFile(
        testName, win32file.GENERIC_READ, 0, None, win32con.OPEN_EXISTING, 0, None
    )
    rc, data = win32file.ReadFile(handle, 1024)
    handle.Close()
    if data == test_data:
        print("Successfully wrote and read a file")
    else:
        raise Exception("Got different data back???")
    os.unlink(testName)


if __name__ == "__main__":
    SimpleFileDemo()

```


---

## win32/Demos/win32gui_demo.py

```python
# The start of a win32gui generic demo.
# Feel free to contribute more demos back ;-)

import math
import random
import time

import win32api
import win32con
import win32gui


def _MyCallback(hwnd, extra):
    hwnds, classes = extra
    hwnds.append(hwnd)
    classes[win32gui.GetClassName(hwnd)] = 1


def TestEnumWindows():
    windows = []
    classes = {}
    win32gui.EnumWindows(_MyCallback, (windows, classes))
    print(
        "Enumerated a total of %d windows with %d classes"
        % (len(windows), len(classes))
    )
    if "tooltips_class32" not in classes:
        print("Hrmmmm - I'm very surprised to not find a 'tooltips_class32' class.")


def OnPaint_1(hwnd, msg, wp, lp):
    dc, ps = win32gui.BeginPaint(hwnd)
    win32gui.SetGraphicsMode(dc, win32con.GM_ADVANCED)
    br = win32gui.CreateSolidBrush(win32api.RGB(255, 0, 0))
    win32gui.SelectObject(dc, br)
    angle = win32gui.GetWindowLong(hwnd, win32con.GWL_USERDATA)
    win32gui.SetWindowLong(hwnd, win32con.GWL_USERDATA, angle + 2)
    r_angle = angle * (math.pi / 180)
    win32gui.SetWorldTransform(
        dc,
        {
            "M11": math.cos(r_angle),
            "M12": math.sin(r_angle),
            "M21": math.sin(r_angle) * -1,
            "M22": math.cos(r_angle),
            "Dx": 250,
            "Dy": 250,
        },
    )
    win32gui.MoveToEx(dc, 250, 250)
    win32gui.BeginPath(dc)
    win32gui.Pie(dc, 10, 70, 200, 200, 350, 350, 75, 10)
    win32gui.Chord(dc, 200, 200, 850, 0, 350, 350, 75, 10)
    win32gui.LineTo(dc, 300, 300)
    win32gui.LineTo(dc, 100, 20)
    win32gui.LineTo(dc, 20, 100)
    win32gui.LineTo(dc, 400, 0)
    win32gui.LineTo(dc, 0, 400)
    win32gui.EndPath(dc)
    win32gui.StrokeAndFillPath(dc)
    win32gui.EndPaint(hwnd, ps)
    return 0


wndproc_1 = {win32con.WM_PAINT: OnPaint_1}


def OnPaint_2(hwnd, msg, wp, lp):
    dc, ps = win32gui.BeginPaint(hwnd)
    win32gui.SetGraphicsMode(dc, win32con.GM_ADVANCED)
    l, t, r, b = win32gui.GetClientRect(hwnd)

    for x in range(25):
        vertices = (
            {
                "x": int(random.random() * r),
                "y": int(random.random() * b),
                "Red": int(random.random() * 0xFF00),
                "Green": 0,
                "Blue": 0,
                "Alpha": 0,
            },
            {
                "x": int(random.random() * r),
                "y": int(random.random() * b),
                "Red": 0,
                "Green": int(random.random() * 0xFF00),
                "Blue": 0,
                "Alpha": 0,
            },
            {
                "x": int(random.random() * r),
                "y": int(random.random() * b),
                "Red": 0,
                "Green": 0,
                "Blue": int(random.random() * 0xFF00),
                "Alpha": 0,
            },
        )
        mesh = ((0, 1, 2),)
        win32gui.GradientFill(dc, vertices, mesh, win32con.GRADIENT_FILL_TRIANGLE)
    win32gui.EndPaint(hwnd, ps)
    return 0


wndproc_2 = {win32con.WM_PAINT: OnPaint_2}


def TestSetWorldTransform():
    wc = win32gui.WNDCLASS()
    wc.lpszClassName = "test_win32gui_1"
    wc.style = win32con.CS_GLOBALCLASS | win32con.CS_VREDRAW | win32con.CS_HREDRAW
    wc.hbrBackground = win32con.COLOR_WINDOW + 1
    wc.lpfnWndProc = wndproc_1
    class_atom = win32gui.RegisterClass(wc)
    hwnd = win32gui.CreateWindow(
        wc.lpszClassName,
        "Spin the Lobster!",
        win32con.WS_CAPTION | win32con.WS_VISIBLE,
        100,
        100,
        900,
        900,
        0,
        0,
        0,
        None,
    )
    for x in range(500):
        win32gui.InvalidateRect(hwnd, None, True)
        win32gui.PumpWaitingMessages()
        time.sleep(0.01)
    win32gui.DestroyWindow(hwnd)
    win32gui.UnregisterClass(wc.lpszClassName, None)


def TestGradientFill():
    wc = win32gui.WNDCLASS()
    wc.lpszClassName = "test_win32gui_2"
    wc.style = win32con.CS_GLOBALCLASS | win32con.CS_VREDRAW | win32con.CS_HREDRAW
    wc.hbrBackground = win32con.COLOR_WINDOW + 1
    wc.lpfnWndProc = wndproc_2
    class_atom = win32gui.RegisterClass(wc)
    hwnd = win32gui.CreateWindowEx(
        0,
        class_atom,
        "Kaleidoscope",
        win32con.WS_CAPTION
        | win32con.WS_VISIBLE
        | win32con.WS_THICKFRAME
        | win32con.WS_SYSMENU,
        100,
        100,
        900,
        900,
        0,
        0,
        0,
        None,
    )
    s = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
    win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, s | win32con.WS_EX_LAYERED)
    win32gui.SetLayeredWindowAttributes(hwnd, 0, 175, win32con.LWA_ALPHA)
    for x in range(30):
        win32gui.InvalidateRect(hwnd, None, True)
        win32gui.PumpWaitingMessages()
        time.sleep(0.3)
    win32gui.DestroyWindow(hwnd)
    win32gui.UnregisterClass(class_atom, None)


print("Enumerating all windows...")
TestEnumWindows()
print("Testing drawing functions ...")
TestSetWorldTransform()
TestGradientFill()
print("All tests done!")

```


---

## win32/Demos/win32gui_devicenotify.py

```python
# Demo RegisterDeviceNotification etc.  Creates a hidden window to receive
# notifications.  See serviceEvents.py for an example of a service doing
# that.
import sys
import time

import win32con
import win32file
import win32gui
import win32gui_struct
import winnt

# These device GUIDs are from Ioevent.h in the Windows SDK.  Ideally they
# could be collected somewhere for pywin32...
GUID_DEVINTERFACE_USB_DEVICE = "{A5DCBF10-6530-11D2-901F-00C04FB951ED}"


# WM_DEVICECHANGE message handler.
def OnDeviceChange(hwnd, msg, wp, lp):
    # Unpack the 'lp' into the appropriate DEV_BROADCAST_* structure,
    # using the self-identifying data inside the DEV_BROADCAST_HDR.
    info = win32gui_struct.UnpackDEV_BROADCAST(lp)
    print("Device change notification:", wp, str(info))
    if (
        wp == win32con.DBT_DEVICEQUERYREMOVE
        and info.devicetype == win32con.DBT_DEVTYP_HANDLE
    ):
        # Our handle is stored away in the structure - just close it
        print("Device being removed - closing handle")
        win32file.CloseHandle(info.handle)
        # and cancel our notifications - if it gets plugged back in we get
        # the same notification and try and close the same handle...
        win32gui.UnregisterDeviceNotification(info.hdevnotify)
    return True


def TestDeviceNotifications(dir_names):
    wc = win32gui.WNDCLASS()
    wc.lpszClassName = "test_devicenotify"
    wc.style = win32con.CS_GLOBALCLASS | win32con.CS_VREDRAW | win32con.CS_HREDRAW
    wc.hbrBackground = win32con.COLOR_WINDOW + 1
    wc.lpfnWndProc = {win32con.WM_DEVICECHANGE: OnDeviceChange}
    class_atom = win32gui.RegisterClass(wc)
    hwnd = win32gui.CreateWindow(
        wc.lpszClassName,
        "Testing some devices",
        # no need for it to be visible.
        win32con.WS_CAPTION,
        100,
        100,
        900,
        900,
        0,
        0,
        0,
        None,
    )

    hdevs = []
    # Watch for all USB device notifications
    filter = win32gui_struct.PackDEV_BROADCAST_DEVICEINTERFACE(
        GUID_DEVINTERFACE_USB_DEVICE
    )
    hdev = win32gui.RegisterDeviceNotification(
        hwnd, filter, win32con.DEVICE_NOTIFY_WINDOW_HANDLE
    )
    hdevs.append(hdev)
    # and create handles for all specified directories
    for d in dir_names:
        hdir = win32file.CreateFile(
            d,
            winnt.FILE_LIST_DIRECTORY,
            winnt.FILE_SHARE_READ | winnt.FILE_SHARE_WRITE | winnt.FILE_SHARE_DELETE,
            None,  # security attributes
            win32con.OPEN_EXISTING,
            win32con.FILE_FLAG_BACKUP_SEMANTICS
            | win32con.FILE_FLAG_OVERLAPPED,  # required privileges: SE_BACKUP_NAME and SE_RESTORE_NAME.
            None,
        )

        filter = win32gui_struct.PackDEV_BROADCAST_HANDLE(hdir)
        hdev = win32gui.RegisterDeviceNotification(
            hwnd, filter, win32con.DEVICE_NOTIFY_WINDOW_HANDLE
        )
        hdevs.append(hdev)

    # now start a message pump and wait for messages to be delivered.
    print("Watching", len(hdevs), "handles - press Ctrl+C to terminate, or")
    print("add and remove some USB devices...")
    if not dir_names:
        print("(Note you can also pass paths to watch on the command-line - eg,")
        print("pass the root of an inserted USB stick to see events specific to")
        print("that volume)")
    while 1:
        win32gui.PumpWaitingMessages()
        time.sleep(0.01)
    win32gui.DestroyWindow(hwnd)
    win32gui.UnregisterClass(wc.lpszClassName, None)


if __name__ == "__main__":
    # optionally pass device/directory names to watch for notifications.
    # Eg, plug in a USB device - assume it connects as E: - then execute:
    # % win32gui_devicenotify.py E:
    # Then remove and insert the device.
    TestDeviceNotifications(sys.argv[1:])

```


---

## win32/Demos/win32gui_dialog.py

```python
# A demo of a fairly complex dialog.
#
# Features:
# * Uses a "dynamic dialog resource" to build the dialog.
# * Uses a ListView control.
# * Dynamically resizes content.
# * Uses a second worker thread to fill the list.
# * Demonstrates support for windows XP themes.

import array
import os
import queue
import struct

import commctrl
import win32api
import win32con
import win32gui
import win32gui_struct
import winerror

IDC_SEARCHTEXT = 1024
IDC_BUTTON_SEARCH = 1025
IDC_BUTTON_DISPLAY = 1026
IDC_LISTBOX = 1027

WM_SEARCH_RESULT = win32con.WM_USER + 512
WM_SEARCH_FINISHED = win32con.WM_USER + 513


class _WIN32MASKEDSTRUCT:
    def __init__(self, **kw):
        full_fmt = ""
        for name, fmt, default, mask in self._struct_items_:
            self.__dict__[name] = None
            if fmt == "z":
                full_fmt += "pi"
            else:
                full_fmt += fmt
        for name, val in kw.items():
            if name not in self.__dict__:
                raise ValueError(f"LVITEM structures do not have an item '{name}'")
            self.__dict__[name] = val

    def __setattr__(self, attr, val):
        if not attr.startswith("_") and attr not in self.__dict__:
            raise AttributeError(attr)
        self.__dict__[attr] = val

    def toparam(self):
        self._buffs = []
        full_fmt = ""
        vals = []
        mask = 0
        # calc the mask
        for name, fmt, default, this_mask in self._struct_items_:
            if this_mask is not None and self.__dict__.get(name) is not None:
                mask |= this_mask
        self.mask = mask
        for name, fmt, default, this_mask in self._struct_items_:
            val = self.__dict__[name]
            if fmt == "z":
                fmt = "Pi"
                if val is None:
                    vals.append(0)
                    vals.append(0)
                else:
                    # Note this demo still works with byte strings.  An
                    # alternate strategy would be to use unicode natively
                    # and use the 'W' version of the messages - eg,
                    # LVM_SETITEMW etc.
                    val += "\x00"
                    if isinstance(val, str):
                        val = val.encode("mbcs")
                    str_buf = array.array("b", val)
                    vals.append(str_buf.buffer_info()[0])
                    vals.append(len(val))
                    self._buffs.append(str_buf)  # keep alive during the call.
            else:
                if val is None:
                    val = default
                vals.append(val)
            full_fmt += fmt
        return struct.pack(*(full_fmt,) + tuple(vals))


# NOTE: See the win32gui_struct module for an alternative way of dealing
# with these structures
class LVITEM(_WIN32MASKEDSTRUCT):
    _struct_items_ = [
        ("mask", "I", 0, None),
        ("iItem", "i", 0, None),
        ("iSubItem", "i", 0, None),
        ("state", "I", 0, commctrl.LVIF_STATE),
        ("stateMask", "I", 0, None),
        ("text", "z", None, commctrl.LVIF_TEXT),
        ("iImage", "i", 0, commctrl.LVIF_IMAGE),
        ("lParam", "i", 0, commctrl.LVIF_PARAM),
        ("iIdent", "i", 0, None),
    ]


class LVCOLUMN(_WIN32MASKEDSTRUCT):
    _struct_items_ = [
        ("mask", "I", 0, None),
        ("fmt", "i", 0, commctrl.LVCF_FMT),
        ("cx", "i", 0, commctrl.LVCF_WIDTH),
        ("text", "z", None, commctrl.LVCF_TEXT),
        ("iSubItem", "i", 0, commctrl.LVCF_SUBITEM),
        ("iImage", "i", 0, commctrl.LVCF_IMAGE),
        ("iOrder", "i", 0, commctrl.LVCF_ORDER),
    ]


class DemoWindowBase:
    def __init__(self):
        win32gui.InitCommonControls()
        self.hinst = win32gui.dllhandle
        self.list_data = {}

    def _RegisterWndClass(self):
        className = "PythonDocSearch"
        message_map = {}
        wc = win32gui.WNDCLASS()
        wc.SetDialogProc()  # Make it a dialog class.
        wc.hInstance = self.hinst
        wc.lpszClassName = className
        wc.style = win32con.CS_VREDRAW | win32con.CS_HREDRAW
        wc.hCursor = win32gui.LoadCursor(0, win32con.IDC_ARROW)
        wc.hbrBackground = win32con.COLOR_WINDOW + 1
        wc.lpfnWndProc = message_map  # could also specify a wndproc.
        # C code: wc.cbWndExtra = DLGWINDOWEXTRA + sizeof(HBRUSH) + (sizeof(COLORREF));
        wc.cbWndExtra = win32con.DLGWINDOWEXTRA + struct.calcsize("Pi")
        icon_flags = win32con.LR_LOADFROMFILE | win32con.LR_DEFAULTSIZE

        ## load icon from executable
        this_app = win32api.GetModuleHandle(None)
        try:
            wc.hIcon = win32gui.LoadIcon(this_app, 1)  ## python.exe and pythonw.exe
        except win32gui.error:
            wc.hIcon = win32gui.LoadIcon(this_app, 135)  ## pythonwin's icon
        try:
            classAtom = win32gui.RegisterClass(wc)
        except win32gui.error as err_info:
            if err_info.winerror != winerror.ERROR_CLASS_ALREADY_EXISTS:
                raise
        return className

    def _GetDialogTemplate(self, dlgClassName):
        style = (
            win32con.WS_THICKFRAME
            | win32con.WS_POPUP
            | win32con.WS_VISIBLE
            | win32con.WS_CAPTION
            | win32con.WS_SYSMENU
            | win32con.DS_SETFONT
            | win32con.WS_MINIMIZEBOX
        )
        cs = win32con.WS_CHILD | win32con.WS_VISIBLE
        title = "Dynamic Dialog Demo"

        # Window frame and title
        dlg = [
            [
                title,
                (0, 0, 210, 250),
                style,
                None,
                (8, "MS Sans Serif"),
                None,
                dlgClassName,
            ],
        ]

        # ID label and text box
        dlg.append([130, "Enter something", -1, (5, 5, 200, 9), cs | win32con.SS_LEFT])
        s = cs | win32con.WS_TABSTOP | win32con.WS_BORDER
        dlg.append(["EDIT", None, IDC_SEARCHTEXT, (5, 15, 200, 12), s])

        # Search/Display Buttons
        # (x positions don't matter here)
        s = cs | win32con.WS_TABSTOP
        dlg.append(
            [
                128,
                "Fill List",
                IDC_BUTTON_SEARCH,
                (5, 35, 50, 14),
                s | win32con.BS_DEFPUSHBUTTON,
            ]
        )
        s = win32con.BS_PUSHBUTTON | s
        dlg.append([128, "Display", IDC_BUTTON_DISPLAY, (100, 35, 50, 14), s])

        # List control.
        # Can't make this work :(
        ##        s = cs | win32con.WS_TABSTOP
        ##        dlg.append(['SysListView32', "Title", IDC_LISTBOX, (5, 505, 200, 200), s])

        return dlg

    def _DoCreate(self, fn):
        message_map = {
            win32con.WM_SIZE: self.OnSize,
            win32con.WM_COMMAND: self.OnCommand,
            win32con.WM_NOTIFY: self.OnNotify,
            win32con.WM_INITDIALOG: self.OnInitDialog,
            win32con.WM_CLOSE: self.OnClose,
            win32con.WM_DESTROY: self.OnDestroy,
            WM_SEARCH_RESULT: self.OnSearchResult,
            WM_SEARCH_FINISHED: self.OnSearchFinished,
        }
        dlgClassName = self._RegisterWndClass()
        template = self._GetDialogTemplate(dlgClassName)
        return fn(self.hinst, template, 0, message_map)

    def _SetupList(self):
        child_style = (
            win32con.WS_CHILD
            | win32con.WS_VISIBLE
            | win32con.WS_BORDER
            | win32con.WS_HSCROLL
            | win32con.WS_VSCROLL
        )
        child_style |= (
            commctrl.LVS_SINGLESEL | commctrl.LVS_SHOWSELALWAYS | commctrl.LVS_REPORT
        )
        self.hwndList = win32gui.CreateWindow(
            "SysListView32",
            None,
            child_style,
            0,
            0,
            100,
            100,
            self.hwnd,
            IDC_LISTBOX,
            self.hinst,
            None,
        )

        child_ex_style = win32gui.SendMessage(
            self.hwndList, commctrl.LVM_GETEXTENDEDLISTVIEWSTYLE, 0, 0
        )
        child_ex_style |= commctrl.LVS_EX_FULLROWSELECT
        win32gui.SendMessage(
            self.hwndList, commctrl.LVM_SETEXTENDEDLISTVIEWSTYLE, 0, child_ex_style
        )

        # Add an image list - use the builtin shell folder icon - this
        # demonstrates that the problem with alpha-blending of icons
        # present on XP is not a problem anymore.
        il = win32gui.ImageList_Create(
            win32api.GetSystemMetrics(win32con.SM_CXSMICON),
            win32api.GetSystemMetrics(win32con.SM_CYSMICON),
            commctrl.ILC_COLOR32 | commctrl.ILC_MASK,
            1,  # initial size
            0,
        )  # cGrow

        shell_dll = os.path.join(win32api.GetSystemDirectory(), "shell32.dll")
        large, small = win32gui.ExtractIconEx(shell_dll, 4, 1)
        win32gui.ImageList_ReplaceIcon(il, -1, small[0])
        win32gui.DestroyIcon(small[0])
        win32gui.DestroyIcon(large[0])
        win32gui.SendMessage(
            self.hwndList, commctrl.LVM_SETIMAGELIST, commctrl.LVSIL_SMALL, il
        )

        # Setup the list control columns.
        lvc = LVCOLUMN(
            mask=commctrl.LVCF_FMT
            | commctrl.LVCF_WIDTH
            | commctrl.LVCF_TEXT
            | commctrl.LVCF_SUBITEM
        )
        lvc.fmt = commctrl.LVCFMT_LEFT
        lvc.iSubItem = 1
        lvc.text = "Title"
        lvc.cx = 200
        win32gui.SendMessage(self.hwndList, commctrl.LVM_INSERTCOLUMN, 0, lvc.toparam())
        lvc.iSubItem = 0
        lvc.text = "Order"
        lvc.cx = 50
        win32gui.SendMessage(self.hwndList, commctrl.LVM_INSERTCOLUMN, 0, lvc.toparam())

        win32gui.UpdateWindow(self.hwnd)

    def ClearListItems(self):
        win32gui.SendMessage(self.hwndList, commctrl.LVM_DELETEALLITEMS)
        self.list_data = {}

    def AddListItem(self, data, *columns):
        num_items = win32gui.SendMessage(self.hwndList, commctrl.LVM_GETITEMCOUNT)
        item = LVITEM(text=columns[0], iItem=num_items)
        new_index = win32gui.SendMessage(
            self.hwndList, commctrl.LVM_INSERTITEM, 0, item.toparam()
        )
        col_no = 1
        for col in columns[1:]:
            item = LVITEM(text=col, iItem=new_index, iSubItem=col_no)
            win32gui.SendMessage(self.hwndList, commctrl.LVM_SETITEM, 0, item.toparam())
            col_no += 1
        self.list_data[new_index] = data

    def OnInitDialog(self, hwnd, msg, wparam, lparam):
        self.hwnd = hwnd
        # centre the dialog
        desktop = win32gui.GetDesktopWindow()
        l, t, r, b = win32gui.GetWindowRect(self.hwnd)
        dt_l, dt_t, dt_r, dt_b = win32gui.GetWindowRect(desktop)
        centre_x, centre_y = win32gui.ClientToScreen(
            desktop, ((dt_r - dt_l) // 2, (dt_b - dt_t) // 2)
        )
        win32gui.MoveWindow(
            hwnd, centre_x - (r // 2), centre_y - (b // 2), r - l, b - t, 0
        )
        self._SetupList()
        l, t, r, b = win32gui.GetClientRect(self.hwnd)
        self._DoSize(r - l, b - t, 1)

    def _DoSize(self, cx, cy, repaint=1):
        # right-justify the textbox.
        ctrl = win32gui.GetDlgItem(self.hwnd, IDC_SEARCHTEXT)
        l, t, r, b = win32gui.GetWindowRect(ctrl)
        l, t = win32gui.ScreenToClient(self.hwnd, (l, t))
        r, b = win32gui.ScreenToClient(self.hwnd, (r, b))
        win32gui.MoveWindow(ctrl, l, t, cx - l - 5, b - t, repaint)
        # The button.
        ctrl = win32gui.GetDlgItem(self.hwnd, IDC_BUTTON_DISPLAY)
        l, t, r, b = win32gui.GetWindowRect(ctrl)
        l, t = win32gui.ScreenToClient(self.hwnd, (l, t))
        r, b = win32gui.ScreenToClient(self.hwnd, (r, b))
        list_y = b + 10
        w = r - l
        win32gui.MoveWindow(ctrl, cx - 5 - w, t, w, b - t, repaint)

        # The list control
        win32gui.MoveWindow(self.hwndList, 0, list_y, cx, cy - list_y, repaint)
        # The last column of the list control.
        new_width = cx - win32gui.SendMessage(
            self.hwndList, commctrl.LVM_GETCOLUMNWIDTH, 0
        )
        win32gui.SendMessage(self.hwndList, commctrl.LVM_SETCOLUMNWIDTH, 1, new_width)

    def OnSize(self, hwnd, msg, wparam, lparam):
        x = win32api.LOWORD(lparam)
        y = win32api.HIWORD(lparam)
        self._DoSize(x, y)
        return 1

    def OnSearchResult(self, hwnd, msg, wparam, lparam):
        try:
            while 1:
                params = self.result_queue.get(0)
                self.AddListItem(*params)
        except queue.Empty:
            pass

    def OnSearchFinished(self, hwnd, msg, wparam, lparam):
        print("OnSearchFinished")

    def OnNotify(self, hwnd, msg, wparam, lparam):
        info = win32gui_struct.UnpackNMITEMACTIVATE(lparam)
        if info.code == commctrl.NM_DBLCLK:
            print("Double click on item", info.iItem + 1)
        return 1

    def OnCommand(self, hwnd, msg, wparam, lparam):
        id = win32api.LOWORD(wparam)
        if id == IDC_BUTTON_SEARCH:
            self.ClearListItems()

            def fill_slowly(q, hwnd):
                import time

                for i in range(20):
                    q.put(("whatever", str(i + 1), "Search result " + str(i)))
                    win32gui.PostMessage(hwnd, WM_SEARCH_RESULT, 0, 0)
                    time.sleep(0.25)
                win32gui.PostMessage(hwnd, WM_SEARCH_FINISHED, 0, 0)

            import threading

            self.result_queue = queue.Queue()
            thread = threading.Thread(
                target=fill_slowly, args=(self.result_queue, self.hwnd)
            )
            thread.start()
        elif id == IDC_BUTTON_DISPLAY:
            print("Display button selected")
            sel = win32gui.SendMessage(
                self.hwndList, commctrl.LVM_GETNEXTITEM, -1, commctrl.LVNI_SELECTED
            )
            print("The selected item is", sel + 1)

    # These function differ based on how the window is used, so may be overridden
    def OnClose(self, hwnd, msg, wparam, lparam):
        raise NotImplementedError

    def OnDestroy(self, hwnd, msg, wparam, lparam):
        pass


# An implementation suitable for use with the Win32 Window functions (ie, not
# a true dialog)
class DemoWindow(DemoWindowBase):
    def CreateWindow(self):
        # Create the window via CreateDialogBoxIndirect - it can then
        # work as a "normal" window, once a message loop is established.
        self._DoCreate(win32gui.CreateDialogIndirect)

    def OnClose(self, hwnd, msg, wparam, lparam):
        win32gui.DestroyWindow(hwnd)

    # We need to arrange to a WM_QUIT message to be sent to our
    # PumpMessages() loop.
    def OnDestroy(self, hwnd, msg, wparam, lparam):
        win32gui.PostQuitMessage(0)  # Terminate the app.


# An implementation suitable for use with the Win32 Dialog functions.
class DemoDialog(DemoWindowBase):
    def DoModal(self):
        return self._DoCreate(win32gui.DialogBoxIndirect)

    def OnClose(self, hwnd, msg, wparam, lparam):
        win32gui.EndDialog(hwnd, 0)


def DemoModal():
    w = DemoDialog()
    w.DoModal()


def DemoCreateWindow():
    w = DemoWindow()
    w.CreateWindow()
    # PumpMessages runs until PostQuitMessage() is called by someone.
    win32gui.PumpMessages()


if __name__ == "__main__":
    DemoModal()
    DemoCreateWindow()

```


---

## win32/Demos/win32gui_menu.py

```python
# Demonstrates some advanced menu concepts using win32gui.
# This creates a taskbar icon which has some fancy menus (but note that
# selecting the menu items does nothing useful - see win32gui_taskbar.py
# for examples of this.

# NOTE: This is a work in progress.  Todo:
# * The "Checked" menu items don't work correctly - I'm not sure why.
# * No support for GetMenuItemInfo.

# Based on Andy McKay's demo code.

import os
import struct
import sys

import win32con
from win32api import GetSystemDirectory, GetSystemMetrics
from win32gui import (
    LOWORD,
    NIF_ICON,
    NIF_MESSAGE,
    NIF_TIP,
    NIM_ADD,
    NIM_DELETE,
    WNDCLASS,
    CheckMenuItem,
    CheckMenuRadioItem,
    CreateCompatibleBitmap,
    CreateCompatibleDC,
    CreateFontIndirect,
    CreatePopupMenu,
    CreateWindow,
    DeleteDC,
    DestroyIcon,
    DestroyWindow,
    DrawIconEx,
    ExtTextOut,
    FillRect,
    GetCursorPos,
    GetDC,
    GetMenuDefaultItem,
    GetMenuState,
    GetModuleHandle,
    GetSysColor,
    GetSysColorBrush,
    GetTextExtentPoint32,
    InsertMenu,
    InsertMenuItem,
    LoadIcon,
    LoadImage,
    PostMessage,
    PostQuitMessage,
    PumpMessages,
    PyGetMemory,
    PyMakeBuffer,
    PySetMemory,
    RegisterClass,
    ReleaseDC,
    SelectObject,
    SetBkColor,
    SetBkMode,
    SetForegroundWindow,
    SetMenuDefaultItem,
    SetTextColor,
    Shell_NotifyIcon,
    SystemParametersInfo,
    TrackPopupMenu,
    UpdateWindow,
)
from win32gui_struct import (
    EmptyMENUITEMINFO,
    PackMENUITEMINFO,
    UnpackMENUITEMINFO,
)

this_dir = os.path.split(sys.argv[0])[0]


class MainWindow:
    def __init__(self):
        message_map = {
            win32con.WM_DESTROY: self.OnDestroy,
            win32con.WM_COMMAND: self.OnCommand,
            win32con.WM_USER + 20: self.OnTaskbarNotify,
            # owner-draw related handlers.
            win32con.WM_MEASUREITEM: self.OnMeasureItem,
            win32con.WM_DRAWITEM: self.OnDrawItem,
        }
        # Register the Window class.
        wc = WNDCLASS()
        hinst = wc.hInstance = GetModuleHandle(None)
        wc.lpszClassName = "PythonTaskbarDemo"
        wc.lpfnWndProc = message_map  # could also specify a wndproc.
        classAtom = RegisterClass(wc)
        # Create the Window.
        style = win32con.WS_OVERLAPPED | win32con.WS_SYSMENU
        self.hwnd = CreateWindow(
            classAtom,
            "Taskbar Demo",
            style,
            0,
            0,
            win32con.CW_USEDEFAULT,
            win32con.CW_USEDEFAULT,
            0,
            0,
            hinst,
            None,
        )
        UpdateWindow(self.hwnd)
        iconPathName = os.path.abspath(os.path.join(sys.prefix, "pyc.ico"))
        if not os.path.isfile(iconPathName):
            # Look in the source tree.
            iconPathName = os.path.abspath(
                os.path.join(os.path.split(sys.executable)[0], "..\\PC\\pyc.ico")
            )
        if os.path.isfile(iconPathName):
            icon_flags = win32con.LR_LOADFROMFILE | win32con.LR_DEFAULTSIZE
            hicon = LoadImage(
                hinst, iconPathName, win32con.IMAGE_ICON, 0, 0, icon_flags
            )
        else:
            iconPathName = None
            print("Can't find a Python icon file - using default")
            hicon = LoadIcon(0, win32con.IDI_APPLICATION)
        self.iconPathName = iconPathName

        # Load up some information about menus needed by our owner-draw code.
        # The font to use on the menu.
        ncm = SystemParametersInfo(win32con.SPI_GETNONCLIENTMETRICS)
        self.font_menu = CreateFontIndirect(ncm["lfMenuFont"])
        # spacing for our ownerdraw menus - not sure exactly what constants
        # should be used (and if you owner-draw all items on the menu, it
        # doesn't matter!)
        self.menu_icon_height = GetSystemMetrics(win32con.SM_CYMENU) - 4
        self.menu_icon_width = self.menu_icon_height
        self.icon_x_pad = 8  # space from end of icon to start of text.
        # A map we use to stash away data we need for ownerdraw.  Keyed
        # by integer ID - that ID will be set in dwTypeData of the menu item.
        self.menu_item_map = {}

        # Finally, create the menu
        self.createMenu()

        flags = NIF_ICON | NIF_MESSAGE | NIF_TIP
        nid = (self.hwnd, 0, flags, win32con.WM_USER + 20, hicon, "Python Demo")
        Shell_NotifyIcon(NIM_ADD, nid)
        print("Please right-click on the Python icon in the taskbar")

    def createMenu(self):
        self.hmenu = menu = CreatePopupMenu()
        # Create our 'Exit' item with the standard, ugly 'close' icon.
        item, extras = PackMENUITEMINFO(
            text="Exit", hbmpItem=win32con.HBMMENU_MBAR_CLOSE, wID=1000
        )
        InsertMenuItem(menu, 0, 1, item)
        # Create a 'text only' menu via InsertMenuItem rather then
        # AppendMenu, just to prove we can!
        item, extras = PackMENUITEMINFO(text="Text only item", wID=1001)
        InsertMenuItem(menu, 0, 1, item)

        load_bmp_flags = win32con.LR_LOADFROMFILE | win32con.LR_LOADTRANSPARENT
        # These images are "over sized", so we load them scaled.
        hbmp = LoadImage(
            0,
            os.path.join(this_dir, "images/smiley.bmp"),
            win32con.IMAGE_BITMAP,
            20,
            20,
            load_bmp_flags,
        )

        # Create a top-level menu with a bitmap
        item, extras = PackMENUITEMINFO(
            text="Menu with bitmap", hbmpItem=hbmp, wID=1002
        )
        InsertMenuItem(menu, 0, 1, item)

        # Owner-draw menus mainly from:
        # https://learn.microsoft.com/en-ca/windows/win32/menurc/using-menus
        # and:
        # https://www.codeguru.com/cplusplus/owner-drawn-menu-with-icons/

        # Create one with an icon - this is *lots* more work - we do it
        # owner-draw!  The primary reason is to handle transparency better -
        # converting to a bitmap causes the background to be incorrect when
        # the menu item is selected.  I can't see a simpler way.
        # First, load the icon we want to use.
        ico_x = GetSystemMetrics(win32con.SM_CXSMICON)
        ico_y = GetSystemMetrics(win32con.SM_CYSMICON)
        if self.iconPathName:
            hicon = LoadImage(
                0,
                self.iconPathName,
                win32con.IMAGE_ICON,
                ico_x,
                ico_y,
                win32con.LR_LOADFROMFILE,
            )
        else:
            shell_dll = os.path.join(GetSystemDirectory(), "shell32.dll")
            large, small = win32gui.ExtractIconEx(shell_dll, 4, 1)
            hicon = small[0]
            DestroyIcon(large[0])

        # Stash away the text and hicon in our map, and add the owner-draw
        # item to the menu.
        index = 0
        self.menu_item_map[index] = (hicon, "Menu with owner-draw icon")
        item, extras = PackMENUITEMINFO(
            fType=win32con.MFT_OWNERDRAW, dwItemData=index, wID=1009
        )
        InsertMenuItem(menu, 0, 1, item)

        # Add another icon-based icon - but this time using HBMMENU_CALLBACK
        # in the hbmpItem elt, so we only need to draw the icon (ie, not the
        # text or checkmark)
        index = 1
        self.menu_item_map[index] = (hicon, None)
        item, extras = PackMENUITEMINFO(
            text="Menu with o-d icon 2",
            dwItemData=index,
            hbmpItem=win32con.HBMMENU_CALLBACK,
            wID=1010,
        )
        InsertMenuItem(menu, 0, 1, item)

        # Add another icon-based icon - this time by converting
        # via bitmap.  Note the icon background when selected is ugly :(
        hdcBitmap = CreateCompatibleDC(0)
        hdcScreen = GetDC(0)
        hbm = CreateCompatibleBitmap(hdcScreen, ico_x, ico_y)
        hbmOld = SelectObject(hdcBitmap, hbm)
        SetBkMode(hdcBitmap, win32con.TRANSPARENT)
        # Fill the background.
        brush = GetSysColorBrush(win32con.COLOR_MENU)
        FillRect(hdcBitmap, (0, 0, 16, 16), brush)
        # unclear if brush needs to be freed.  Best clue I can find is:
        # "GetSysColorBrush returns a cached brush instead of allocating a new
        # one." - implies no DeleteObject.
        # draw the icon
        DrawIconEx(hdcBitmap, 0, 0, hicon, ico_x, ico_y, 0, 0, win32con.DI_NORMAL)
        SelectObject(hdcBitmap, hbmOld)
        DeleteDC(hdcBitmap)
        item, extras = PackMENUITEMINFO(
            text="Menu with icon", hbmpItem=hbm.Detach(), wID=1011
        )
        InsertMenuItem(menu, 0, 1, item)

        # Create a sub-menu, and put a few funky ones there.
        self.sub_menu = sub_menu = CreatePopupMenu()
        # A 'checkbox' menu.
        item, extras = PackMENUITEMINFO(
            fState=win32con.MFS_CHECKED, text="Checkbox menu", hbmpItem=hbmp, wID=1003
        )
        InsertMenuItem(sub_menu, 0, 1, item)
        # A 'radio' menu.
        InsertMenu(sub_menu, 0, win32con.MF_BYPOSITION, win32con.MF_SEPARATOR, None)
        item, extras = PackMENUITEMINFO(
            fType=win32con.MFT_RADIOCHECK,
            fState=win32con.MFS_CHECKED,
            text="Checkbox menu - bullet 1",
            hbmpItem=hbmp,
            wID=1004,
        )
        InsertMenuItem(sub_menu, 0, 1, item)
        item, extras = PackMENUITEMINFO(
            fType=win32con.MFT_RADIOCHECK,
            fState=win32con.MFS_UNCHECKED,
            text="Checkbox menu - bullet 2",
            hbmpItem=hbmp,
            wID=1005,
        )
        InsertMenuItem(sub_menu, 0, 1, item)
        # And add the sub-menu to the top-level menu.
        item, extras = PackMENUITEMINFO(text="Sub-Menu", hSubMenu=sub_menu)
        InsertMenuItem(menu, 0, 1, item)

        # Set 'Exit' as the default option.
        SetMenuDefaultItem(menu, 1000, 0)

    def OnDestroy(self, hwnd, msg, wparam, lparam):
        nid = (self.hwnd, 0)
        Shell_NotifyIcon(NIM_DELETE, nid)
        PostQuitMessage(0)  # Terminate the app.

    def OnTaskbarNotify(self, hwnd, msg, wparam, lparam):
        if lparam == win32con.WM_RBUTTONUP:
            print("You right clicked me.")
            # display the menu at the cursor pos.
            pos = GetCursorPos()
            SetForegroundWindow(self.hwnd)
            TrackPopupMenu(
                self.hmenu, win32con.TPM_LEFTALIGN, pos[0], pos[1], 0, self.hwnd, None
            )
            PostMessage(self.hwnd, win32con.WM_NULL, 0, 0)
        elif lparam == win32con.WM_LBUTTONDBLCLK:
            print("You double-clicked me")
            # find the default menu item and fire it.
            cmd = GetMenuDefaultItem(self.hmenu, False, 0)
            if cmd == -1:
                print("Can't find a default!")
            # and just pretend it came from the menu
            self.OnCommand(hwnd, win32con.WM_COMMAND, cmd, 0)
        return 1

    def OnCommand(self, hwnd, msg, wparam, lparam):
        id = LOWORD(wparam)
        if id == 1000:
            print("Goodbye")
            DestroyWindow(self.hwnd)
        elif id in (1003, 1004, 1005):
            # Our 'checkbox' and 'radio' items
            state = GetMenuState(self.sub_menu, id, win32con.MF_BYCOMMAND)
            if state == -1:
                raise RuntimeError("No item found")
            if state & win32con.MF_CHECKED:
                check_flags = win32con.MF_UNCHECKED
                print("Menu was checked - unchecking")
            else:
                check_flags = win32con.MF_CHECKED
                print("Menu was unchecked - checking")

            if id == 1003:
                # simple checkbox
                rc = CheckMenuItem(
                    self.sub_menu, id, win32con.MF_BYCOMMAND | check_flags
                )
            else:
                # radio button - must pass the first and last IDs in the
                # "group", and the ID in the group that is to be selected.
                rc = CheckMenuRadioItem(
                    self.sub_menu, 1004, 1005, id, win32con.MF_BYCOMMAND
                )
            # Get and check the new state - first the simple way...
            new_state = GetMenuState(self.sub_menu, id, win32con.MF_BYCOMMAND)
            if new_state & win32con.MF_CHECKED != check_flags:
                raise RuntimeError("The new item didn't get the new checked state!")
            # Now the long-winded way via GetMenuItemInfo...
            buf, extras = EmptyMENUITEMINFO()
            win32gui.GetMenuItemInfo(self.sub_menu, id, False, buf)
            (
                fType,
                fState,
                wID,
                hSubMenu,
                hbmpChecked,
                hbmpUnchecked,
                dwItemData,
                text,
                hbmpItem,
            ) = UnpackMENUITEMINFO(buf)

            if fState & win32con.MF_CHECKED != check_flags:
                raise RuntimeError("The new item didn't get the new checked state!")
        else:
            print("OnCommand for ID", id)

    # Owner-draw related functions.  We only have 1 owner-draw item, but
    # we pretend we have more than that :)
    def OnMeasureItem(self, hwnd, msg, wparam, lparam):
        ## Last item of MEASUREITEMSTRUCT is a ULONG_PTR
        fmt = "5iP"
        buf = PyMakeBuffer(struct.calcsize(fmt), lparam)
        data = struct.unpack(fmt, buf)
        ctlType, ctlID, itemID, itemWidth, itemHeight, itemData = data

        hicon, text = self.menu_item_map[itemData]
        if text is None:
            # Only drawing icon due to HBMMENU_CALLBACK
            cx = self.menu_icon_width
            cy = self.menu_icon_height
        else:
            # drawing the lot!
            dc = GetDC(hwnd)
            oldFont = SelectObject(dc, self.font_menu)
            cx, cy = GetTextExtentPoint32(dc, text)
            SelectObject(dc, oldFont)
            ReleaseDC(hwnd, dc)

            cx += GetSystemMetrics(win32con.SM_CXMENUCHECK)
            cx += self.menu_icon_width + self.icon_x_pad

            cy = GetSystemMetrics(win32con.SM_CYMENU)

        new_data = struct.pack(fmt, ctlType, ctlID, itemID, cx, cy, itemData)
        PySetMemory(lparam, new_data)
        return True

    def OnDrawItem(self, hwnd, msg, wparam, lparam):
        ## lparam is a DRAWITEMSTRUCT
        fmt = "5i2P4iP"
        data = struct.unpack(fmt, PyGetMemory(lparam, struct.calcsize(fmt)))
        (
            ctlType,
            ctlID,
            itemID,
            itemAction,
            itemState,
            hwndItem,
            hDC,
            left,
            top,
            right,
            bot,
            itemData,
        ) = data

        rect = left, top, right, bot
        hicon, text = self.menu_item_map[itemData]

        if text is None:
            # This means the menu-item had HBMMENU_CALLBACK - so all we
            # draw is the icon.  rect is the entire area we should use.
            DrawIconEx(
                hDC, left, top, hicon, right - left, bot - top, 0, 0, win32con.DI_NORMAL
            )
        else:
            # If the user has selected the item, use the selected
            # text and background colors to display the item.
            selected = itemState & win32con.ODS_SELECTED
            if selected:
                crText = SetTextColor(hDC, GetSysColor(win32con.COLOR_HIGHLIGHTTEXT))
                crBkgnd = SetBkColor(hDC, GetSysColor(win32con.COLOR_HIGHLIGHT))

            each_pad = self.icon_x_pad // 2
            x_icon = left + GetSystemMetrics(win32con.SM_CXMENUCHECK) + each_pad
            x_text = x_icon + self.menu_icon_width + each_pad

            # Draw text first, specifying a complete rect to fill - this sets
            # up the background (but overwrites anything else already there!)
            # Select the font, draw it, and restore the previous font.
            hfontOld = SelectObject(hDC, self.font_menu)
            ExtTextOut(hDC, x_text, top + 2, win32con.ETO_OPAQUE, rect, text)
            SelectObject(hDC, hfontOld)

            # Icon image next.  Icons are transparent - no need to handle
            # selection specially.
            DrawIconEx(
                hDC,
                x_icon,
                top + 2,
                hicon,
                self.menu_icon_width,
                self.menu_icon_height,
                0,
                0,
                win32con.DI_NORMAL,
            )

            # Return the text and background colors to their
            # normal state (not selected).
            if selected:
                SetTextColor(hDC, crText)
                SetBkColor(hDC, crBkgnd)


def main():
    w = MainWindow()
    PumpMessages()


if __name__ == "__main__":
    main()

```


---

## win32/Demos/win32gui_taskbar.py

```python
# Creates a task-bar icon.  Run from Python.exe to see the
# messages printed.
import os
import sys

import win32api
import win32con
import win32gui
import winerror


class MainWindow:
    def __init__(self):
        msg_TaskbarRestart = win32gui.RegisterWindowMessage("TaskbarCreated")
        message_map = {
            msg_TaskbarRestart: self.OnRestart,
            win32con.WM_DESTROY: self.OnDestroy,
            win32con.WM_COMMAND: self.OnCommand,
            win32con.WM_USER + 20: self.OnTaskbarNotify,
        }
        # Register the Window class.
        wc = win32gui.WNDCLASS()
        hinst = wc.hInstance = win32api.GetModuleHandle(None)
        wc.lpszClassName = "PythonTaskbarDemo"
        wc.style = win32con.CS_VREDRAW | win32con.CS_HREDRAW
        wc.hCursor = win32api.LoadCursor(0, win32con.IDC_ARROW)
        wc.hbrBackground = win32con.COLOR_WINDOW
        wc.lpfnWndProc = message_map  # could also specify a wndproc.

        # Don't blow up if class already registered to make testing easier
        try:
            classAtom = win32gui.RegisterClass(wc)
        except win32gui.error as err_info:
            if err_info.winerror != winerror.ERROR_CLASS_ALREADY_EXISTS:
                raise

        # Create the Window.
        style = win32con.WS_OVERLAPPED | win32con.WS_SYSMENU
        self.hwnd = win32gui.CreateWindow(
            wc.lpszClassName,
            "Taskbar Demo",
            style,
            0,
            0,
            win32con.CW_USEDEFAULT,
            win32con.CW_USEDEFAULT,
            0,
            0,
            hinst,
            None,
        )
        win32gui.UpdateWindow(self.hwnd)
        self._DoCreateIcons()

    def _DoCreateIcons(self):
        # Try and find a custom icon
        hinst = win32api.GetModuleHandle(None)
        iconPathName = os.path.abspath(
            os.path.join(os.path.split(sys.executable)[0], "pyc.ico")
        )
        if not os.path.isfile(iconPathName):
            # Look in the source tree.
            iconPathName = os.path.abspath(
                os.path.join(os.path.split(sys.executable)[0], "..\\PC\\pyc.ico")
            )
        if os.path.isfile(iconPathName):
            icon_flags = win32con.LR_LOADFROMFILE | win32con.LR_DEFAULTSIZE
            hicon = win32gui.LoadImage(
                hinst, iconPathName, win32con.IMAGE_ICON, 0, 0, icon_flags
            )
        else:
            print("Can't find a Python icon file - using default")
            hicon = win32gui.LoadIcon(0, win32con.IDI_APPLICATION)

        flags = win32gui.NIF_ICON | win32gui.NIF_MESSAGE | win32gui.NIF_TIP
        nid = (self.hwnd, 0, flags, win32con.WM_USER + 20, hicon, "Python Demo")
        try:
            win32gui.Shell_NotifyIcon(win32gui.NIM_ADD, nid)
        except win32gui.error:
            # This is common when windows is starting, and this code is hit
            # before the taskbar has been created.
            print("Failed to add the taskbar icon - is explorer running?")
            # but keep running anyway - when explorer starts, we get the
            # TaskbarCreated message.

    def OnRestart(self, hwnd, msg, wparam, lparam):
        self._DoCreateIcons()

    def OnDestroy(self, hwnd, msg, wparam, lparam):
        nid = (self.hwnd, 0)
        win32gui.Shell_NotifyIcon(win32gui.NIM_DELETE, nid)
        win32gui.PostQuitMessage(0)  # Terminate the app.

    def OnTaskbarNotify(self, hwnd, msg, wparam, lparam):
        if lparam == win32con.WM_LBUTTONUP:
            print("You clicked me.")
        elif lparam == win32con.WM_LBUTTONDBLCLK:
            print("You double-clicked me - goodbye")
            win32gui.DestroyWindow(self.hwnd)
        elif lparam == win32con.WM_RBUTTONUP:
            print("You right clicked me.")
            menu = win32gui.CreatePopupMenu()
            win32gui.AppendMenu(menu, win32con.MF_STRING, 1023, "Display Dialog")
            win32gui.AppendMenu(menu, win32con.MF_STRING, 1024, "Say Hello")
            win32gui.AppendMenu(menu, win32con.MF_STRING, 1025, "Exit program")
            pos = win32gui.GetCursorPos()
            # See https://learn.microsoft.com/en-us/windows/win32/api/_menurc/
            win32gui.SetForegroundWindow(self.hwnd)
            win32gui.TrackPopupMenu(
                menu, win32con.TPM_LEFTALIGN, pos[0], pos[1], 0, self.hwnd, None
            )
            win32gui.PostMessage(self.hwnd, win32con.WM_NULL, 0, 0)
        return 1

    def OnCommand(self, hwnd, msg, wparam, lparam):
        id = win32api.LOWORD(wparam)
        if id == 1023:
            import win32gui_dialog

            win32gui_dialog.DemoModal()
        elif id == 1024:
            print("Hello")
        elif id == 1025:
            print("Goodbye")
            win32gui.DestroyWindow(self.hwnd)
        else:
            print("Unknown command -", id)


def main():
    w = MainWindow()
    win32gui.PumpMessages()


if __name__ == "__main__":
    main()

```


---

## win32/Demos/win32netdemo.py

```python
import getopt
import sys
import traceback
from collections.abc import Callable

import win32api
import win32net
import win32netcon
import win32security

verbose_level = 0

server = None  # Run on local machine.


def verbose(msg):
    if verbose_level:
        print(msg)


def CreateUser():
    "Creates a new test user, then deletes the user"
    testName = "PyNetTestUser"
    try:
        win32net.NetUserDel(server, testName)
        print("Warning - deleted user before creating it!")
    except win32net.error:
        pass

    d = {}
    d["name"] = testName
    d["password"] = "deleteme"
    d["priv"] = win32netcon.USER_PRIV_USER
    d["comment"] = "Delete me - created by Python test code"
    d["flags"] = win32netcon.UF_NORMAL_ACCOUNT | win32netcon.UF_SCRIPT
    win32net.NetUserAdd(server, 1, d)
    try:
        try:
            win32net.NetUserChangePassword(server, testName, "wrong", "new")
            print("ERROR: NetUserChangePassword worked with a wrong password!")
        except win32net.error:
            pass
        win32net.NetUserChangePassword(server, testName, "deleteme", "new")
    finally:
        win32net.NetUserDel(server, testName)
    print("Created a user, changed their password, and deleted them!")


def UserEnum():
    "Enumerates all the local users"
    resume = 0
    nuser = 0
    while 1:
        data, total, resume = win32net.NetUserEnum(
            server, 3, win32netcon.FILTER_NORMAL_ACCOUNT, resume
        )
        verbose(
            "Call to NetUserEnum obtained %d entries of %d total" % (len(data), total)
        )
        for user in data:
            verbose("Found user %s" % user["name"])
            nuser += 1
        if not resume:
            break
    assert nuser, "Could not find any users!"
    print("Enumerated all the local users")


def GroupEnum():
    "Enumerates all the domain groups"
    nmembers = 0
    resume = 0
    while 1:
        data, total, resume = win32net.NetGroupEnum(server, 1, resume)
        # print(f"Call to NetGroupEnum obtained {len(data)} entries of {total} total")
        for group in data:
            verbose("Found group {name}:{comment} ".format(**group))
            memberresume = 0
            while 1:
                memberdata, total, memberresume = win32net.NetGroupGetUsers(
                    server, group["name"], 0, resume
                )
                for member in memberdata:
                    verbose(" Member {name}".format(**member))
                    nmembers += 1
                if memberresume == 0:
                    break
        if not resume:
            break
    assert nmembers, "Couldn't find a single member in a single group!"
    print("Enumerated all the groups")


def LocalGroupEnum():
    "Enumerates all the local groups"
    resume = 0
    nmembers = 0
    while 1:
        data, total, resume = win32net.NetLocalGroupEnum(server, 1, resume)
        for group in data:
            verbose("Found group {name}:{comment} ".format(**group))
            memberresume = 0
            while 1:
                memberdata, total, memberresume = win32net.NetLocalGroupGetMembers(
                    server, group["name"], 2, resume
                )
                for member in memberdata:
                    # Just for the sake of it, we convert the SID to a username
                    username, domain, type = win32security.LookupAccountSid(
                        server, member["sid"]
                    )
                    nmembers += 1
                    verbose(" Member {} ({})".format(username, member["domainandname"]))
                if memberresume == 0:
                    break
        if not resume:
            break
    assert nmembers, "Couldn't find a single member in a single group!"
    print("Enumerated all the local groups")


def ServerEnum():
    "Enumerates all servers on the network"
    resume = 0
    while 1:
        data, total, resume = win32net.NetServerEnum(
            server, 100, win32netcon.SV_TYPE_ALL, None, resume
        )
        for s in data:
            verbose("Found server %s" % s["name"])
            # Now loop over the shares.
            shareresume = 0
            while 1:
                sharedata, total, shareresume = win32net.NetShareEnum(
                    server, 2, shareresume
                )
                for share in sharedata:
                    verbose(
                        " %(netname)s (%(path)s):%(remark)s - in use by %(current_uses)d users"
                        % share
                    )
                if not shareresume:
                    break
        if not resume:
            break
    print("Enumerated all the servers on the network")


def LocalGroup(uname=None):
    "Creates a local group, adds some members, deletes them, then removes the group"
    level = 3
    if uname is None:
        uname = win32api.GetUserName()
    if uname.find("\\") < 0:
        uname = win32api.GetDomainName() + "\\" + uname
    group = "python_test_group"
    # delete the group if it already exists
    try:
        win32net.NetLocalGroupDel(server, group)
        print("WARNING: existing local group '%s' has been deleted.")
    except win32net.error:
        pass
    group_data = {"name": group}
    win32net.NetLocalGroupAdd(server, 1, group_data)
    try:
        u = {"domainandname": uname}
        win32net.NetLocalGroupAddMembers(server, group, level, [u])
        mem, tot, res = win32net.NetLocalGroupGetMembers(server, group, level)
        print("members are", mem)
        if mem[0]["domainandname"] != uname:
            print(f"ERROR: LocalGroup just added {uname}, but members are {mem!r}")
        # Convert the list of dicts to a list of strings.
        win32net.NetLocalGroupDelMembers(
            server, group, [m["domainandname"] for m in mem]
        )
    finally:
        win32net.NetLocalGroupDel(server, group)
    print("Created a local group, added and removed members, then deleted the group")


def GetInfo(userName=None):
    "Dumps level 3 information about the current user"
    if userName is None:
        userName = win32api.GetUserName()
    print("Dumping level 3 information about user")
    info = win32net.NetUserGetInfo(server, userName, 3)
    for key, val in info.items():
        verbose(f"{key}={val}")


def SetInfo(userName=None):
    "Attempts to change the current users comment, then set it back"
    if userName is None:
        userName = win32api.GetUserName()
    oldData = win32net.NetUserGetInfo(server, userName, 3)
    try:
        d = oldData | {"usr_comment": "Test comment"}
        win32net.NetUserSetInfo(server, userName, 3, d)
        new = win32net.NetUserGetInfo(server, userName, 3)["usr_comment"]
        if str(new) != "Test comment":
            raise RuntimeError("Could not read the same comment back - got %s" % new)
        print("Changed the data for the user")
    finally:
        win32net.NetUserSetInfo(server, userName, 3, oldData)


def SetComputerInfo():
    "Doesn't actually change anything, just make sure we could ;-)"
    info = win32net.NetWkstaGetInfo(None, 502)
    # *sob* - but we can't!  Why not!!!
    # win32net.NetWkstaSetInfo(None, 502, info)


def usage(tests):
    import os

    print("Usage: %s [-s server ] [-v] [Test ...]" % os.path.basename(sys.argv[0]))
    print("  -v : Verbose - print more information")
    print("  -s : server - execute the tests against the named server")
    print("  -c : include the CreateUser test by default")
    print("where Test is one of:")
    for t in tests:
        print(t.__name__, ":", t.__doc__)
    print()
    print("If not tests are specified, all tests are run")
    sys.exit(1)


def main():
    tests = [ob for ob in globals().values() if isinstance(ob, Callable) and ob.__doc__]
    opts, args = getopt.getopt(sys.argv[1:], "s:hvc")
    create_user = False
    for opt, val in opts:
        if opt == "-s":
            global server
            server = val
        if opt == "-h":
            usage(tests)
        if opt == "-v":
            global verbose_level
            verbose_level += 1
        if opt == "-c":
            create_user = True

    if len(args) == 0:
        print("Running all tests - use '-h' to see command-line options...")
        dotests = tests
        if not create_user:
            dotests.remove(CreateUser)
    else:
        dotests = []
        for arg in args:
            for t in tests:
                if t.__name__ == arg:
                    dotests.append(t)
                    break
            else:
                print("Test '%s' unknown - skipping" % arg)
    if not dotests:
        print("Nothing to do!")
        usage(tests)
    for test in dotests:
        try:
            test()
        except:
            print("Test %s failed" % test.__name__)
            traceback.print_exc()


if __name__ == "__main__":
    main()

```


---

## win32/Demos/win32rcparser_demo.py

```python
# A demo of the win32rcparser module and using win32gui

import os

import commctrl
import win32api
import win32con
import win32gui
import win32rcparser

this_dir = os.path.abspath(os.path.dirname(__file__))
g_rcname = os.path.abspath(
    os.path.join(this_dir, "..", "test", "win32rcparser", "test.rc")
)

if not os.path.isfile(g_rcname):
    raise RuntimeError(f"Can't locate test.rc (should be at '{g_rcname}')")


class DemoWindow:
    def __init__(self, dlg_template):
        self.dlg_template = dlg_template

    def CreateWindow(self):
        self._DoCreate(win32gui.CreateDialogIndirect)

    def DoModal(self):
        return self._DoCreate(win32gui.DialogBoxIndirect)

    def _DoCreate(self, fn):
        message_map = {
            win32con.WM_INITDIALOG: self.OnInitDialog,
            win32con.WM_CLOSE: self.OnClose,
            win32con.WM_DESTROY: self.OnDestroy,
            win32con.WM_COMMAND: self.OnCommand,
        }
        return fn(0, self.dlg_template, 0, message_map)

    def OnInitDialog(self, hwnd, msg, wparam, lparam):
        self.hwnd = hwnd
        # centre the dialog
        desktop = win32gui.GetDesktopWindow()
        l, t, r, b = win32gui.GetWindowRect(self.hwnd)
        dt_l, dt_t, dt_r, dt_b = win32gui.GetWindowRect(desktop)
        centre_x, centre_y = win32gui.ClientToScreen(
            desktop, ((dt_r - dt_l) // 2, (dt_b - dt_t) // 2)
        )
        win32gui.MoveWindow(
            hwnd, centre_x - (r // 2), centre_y - (b // 2), r - l, b - t, 0
        )

    def OnCommand(self, hwnd, msg, wparam, lparam):
        # Needed to make OK/Cancel work - no other controls are handled.
        id = win32api.LOWORD(wparam)
        if id in [win32con.IDOK, win32con.IDCANCEL]:
            win32gui.EndDialog(hwnd, id)

    def OnClose(self, hwnd, msg, wparam, lparam):
        win32gui.EndDialog(hwnd, 0)

    def OnDestroy(self, hwnd, msg, wparam, lparam):
        pass


def DemoModal():
    # Load the .rc file.
    resources = win32rcparser.Parse(g_rcname)
    for id, ddef in resources.dialogs.items():
        print("Displaying dialog", id)
        w = DemoWindow(ddef)
        w.DoModal()


if __name__ == "__main__":
    flags = 0
    for flag in """ICC_DATE_CLASSES ICC_ANIMATE_CLASS ICC_ANIMATE_CLASS
                   ICC_BAR_CLASSES ICC_COOL_CLASSES ICC_DATE_CLASSES
                   ICC_HOTKEY_CLASS ICC_INTERNET_CLASSES ICC_LISTVIEW_CLASSES
                   ICC_PAGESCROLLER_CLASS ICC_PROGRESS_CLASS ICC_TAB_CLASSES
                   ICC_TREEVIEW_CLASSES ICC_UPDOWN_CLASS ICC_USEREX_CLASSES
                   ICC_WIN95_CLASSES  """.split():
        flags |= getattr(commctrl, flag)
    win32gui.InitCommonControlsEx(flags)
    # Need to do this go get rich-edit working.
    win32api.LoadLibrary("riched20.dll")
    DemoModal()

```


---

## win32/Demos/win32servicedemo.py

```python
import win32con
import win32service


def EnumServices():
    resume = 0
    accessSCM = win32con.GENERIC_READ
    accessSrv = win32service.SC_MANAGER_ALL_ACCESS

    # Open Service Control Manager
    hscm = win32service.OpenSCManager(None, None, accessSCM)

    # Enumerate Service Control Manager DB

    typeFilter = win32service.SERVICE_WIN32
    stateFilter = win32service.SERVICE_STATE_ALL

    statuses = win32service.EnumServicesStatus(hscm, typeFilter, stateFilter)
    for short_name, desc, status in statuses:
        print(short_name, desc, status)


EnumServices()

```


---

## win32/Demos/win32ts_logoff_disconnected.py

```python
"""Finds any disconnected terminal service sessions and logs them off"""

import pywintypes
import win32ts
import winerror

sessions = win32ts.WTSEnumerateSessions(win32ts.WTS_CURRENT_SERVER_HANDLE)
for session in sessions:
    """
    WTS_CONNECTSTATE_CLASS: WTSActive,WTSConnected,WTSConnectQuery,WTSShadow,WTSDisconnected,
          WTSIdle,WTSListen,WTSReset,WTSDown,WTSInit
    """
    if session["State"] == win32ts.WTSDisconnected:
        sessionid = session["SessionId"]
        username = win32ts.WTSQuerySessionInformation(
            win32ts.WTS_CURRENT_SERVER_HANDLE, sessionid, win32ts.WTSUserName
        )
        print("Logging off disconnected user:", username)
        try:
            win32ts.WTSLogoffSession(win32ts.WTS_CURRENT_SERVER_HANDLE, sessionid, True)
        except pywintypes.error as e:
            if e.winerror == winerror.ERROR_ACCESS_DENIED:
                print("Can't kill that session:", e.strerror)
            else:
                raise

```


---

## win32/Demos/win32wnet/testwnet.py

```python
import os

import win32api
import win32wnet
from winnetwk import *

possible_shares = []


def _doDumpHandle(handle, level=0):
    indent = " " * level
    while 1:
        items = win32wnet.WNetEnumResource(handle, 0)
        if len(items) == 0:
            break
        for item in items:
            try:
                if item.dwDisplayType == RESOURCEDISPLAYTYPE_SHARE:
                    print(indent + "Have share with name:", item.lpRemoteName)
                    possible_shares.append(item)
                elif item.dwDisplayType == RESOURCEDISPLAYTYPE_GENERIC:
                    print(
                        indent + "Have generic resource with name:", item.lpRemoteName
                    )
                else:
                    # Try generic!
                    print(indent + "Enumerating " + item.lpRemoteName, end=" ")
                    k = win32wnet.WNetOpenEnum(
                        RESOURCE_GLOBALNET, RESOURCETYPE_ANY, 0, item
                    )
                    print()
                    _doDumpHandle(k, level + 1)
                    win32wnet.WNetCloseEnum(
                        k
                    )  # could do k.Close(), but this is a good test!
            except win32wnet.error as details:
                print(indent + "Couldn't enumerate this resource: " + details.strerror)


def TestOpenEnum():
    print("Enumerating all resources on the network - this may take some time...")
    handle = win32wnet.WNetOpenEnum(RESOURCE_GLOBALNET, RESOURCETYPE_ANY, 0, None)

    try:
        _doDumpHandle(handle)
    finally:
        handle.Close()
    print("Finished dumping all resources.")


def findUnusedDriveLetter():
    existing = [
        x[0].lower() for x in win32api.GetLogicalDriveStrings().split("\0") if x
    ]
    handle = win32wnet.WNetOpenEnum(RESOURCE_REMEMBERED, RESOURCETYPE_DISK, 0, None)
    try:
        while 1:
            items = win32wnet.WNetEnumResource(handle, 0)
            if len(items) == 0:
                break
            xtra = [i.lpLocalName[0].lower() for i in items if i.lpLocalName]
            existing.extend(xtra)
    finally:
        handle.Close()
    for maybe in "defghijklmnopqrstuvwxyz":
        if maybe not in existing:
            return maybe
    raise RuntimeError("All drive mappings are taken?")


def TestConnection():
    if len(possible_shares) == 0:
        print("Couldn't find any potential shares to connect to")
        return
    localName = findUnusedDriveLetter() + ":"
    for share in possible_shares:
        print("Attempting connection of", localName, "to", share.lpRemoteName)
        try:
            win32wnet.WNetAddConnection2(share.dwType, localName, share.lpRemoteName)
        except win32wnet.error as details:
            print("Couldn't connect: " + details.strerror)
            continue
        # Have a connection.
        try:
            fname = os.path.join(localName + "\\", os.listdir(localName + "\\")[0])
            try:
                print(
                    "Universal name of '{}' is '{}'".format(
                        fname, win32wnet.WNetGetUniversalName(fname)
                    )
                )
            except win32wnet.error as details:
                print(f"Couldn't get universal name of '{fname}': {details.strerror}")
            print("User name for this connection is", win32wnet.WNetGetUser(localName))
        finally:
            win32wnet.WNetCancelConnection2(localName, 0, 0)
        # and do it again, but this time by using the more modern
        # NETRESOURCE way.
        nr = win32wnet.NETRESOURCE()
        nr.dwType = share.dwType
        nr.lpLocalName = localName
        nr.lpRemoteName = share.lpRemoteName
        win32wnet.WNetAddConnection2(nr)
        win32wnet.WNetCancelConnection2(localName, 0, 0)

        # and one more time using WNetAddConnection3
        win32wnet.WNetAddConnection3(0, nr)
        win32wnet.WNetCancelConnection2(localName, 0, 0)

        # Only do the first share that succeeds.
        break


def TestGetUser():
    u = win32wnet.WNetGetUser()
    print(f"Current global user is {u!r}")
    if u != win32wnet.WNetGetUser(None):
        raise RuntimeError("Default value didn't seem to work!")


TestGetUser()
TestOpenEnum()
TestConnection()

```


---

## win32/Demos/win32wnet/winnetwk.py

```python
# Generated by h2py from d:\mssdk\include\winnetwk.h
WNNC_NET_MSNET = 0x00010000
WNNC_NET_LANMAN = 0x00020000
WNNC_NET_NETWARE = 0x00030000
WNNC_NET_VINES = 0x00040000
WNNC_NET_10NET = 0x00050000
WNNC_NET_LOCUS = 0x00060000
WNNC_NET_SUN_PC_NFS = 0x00070000
WNNC_NET_LANSTEP = 0x00080000
WNNC_NET_9TILES = 0x00090000
WNNC_NET_LANTASTIC = 0x000A0000
WNNC_NET_AS400 = 0x000B0000
WNNC_NET_FTP_NFS = 0x000C0000
WNNC_NET_PATHWORKS = 0x000D0000
WNNC_NET_LIFENET = 0x000E0000
WNNC_NET_POWERLAN = 0x000F0000
WNNC_NET_BWNFS = 0x00100000
WNNC_NET_COGENT = 0x00110000
WNNC_NET_FARALLON = 0x00120000
WNNC_NET_APPLETALK = 0x00130000
WNNC_NET_INTERGRAPH = 0x00140000
WNNC_NET_SYMFONET = 0x00150000
WNNC_NET_CLEARCASE = 0x00160000
WNNC_NET_FRONTIER = 0x00170000
WNNC_NET_BMC = 0x00180000
WNNC_NET_DCE = 0x00190000
WNNC_NET_DECORB = 0x00200000
WNNC_NET_PROTSTOR = 0x00210000
WNNC_NET_FJ_REDIR = 0x00220000
WNNC_NET_DISTINCT = 0x00230000
WNNC_NET_TWINS = 0x00240000
WNNC_NET_RDR2SAMPLE = 0x00250000
RESOURCE_CONNECTED = 0x00000001
RESOURCE_GLOBALNET = 0x00000002
RESOURCE_REMEMBERED = 0x00000003
RESOURCE_RECENT = 0x00000004
RESOURCE_CONTEXT = 0x00000005
RESOURCETYPE_ANY = 0x00000000
RESOURCETYPE_DISK = 0x00000001
RESOURCETYPE_PRINT = 0x00000002
RESOURCETYPE_RESERVED = 0x00000008
RESOURCETYPE_UNKNOWN = 0xFFFFFFFF
RESOURCEUSAGE_CONNECTABLE = 0x00000001
RESOURCEUSAGE_CONTAINER = 0x00000002
RESOURCEUSAGE_NOLOCALDEVICE = 0x00000004
RESOURCEUSAGE_SIBLING = 0x00000008
RESOURCEUSAGE_ATTACHED = 0x00000010
RESOURCEUSAGE_ALL = (
    RESOURCEUSAGE_CONNECTABLE | RESOURCEUSAGE_CONTAINER | RESOURCEUSAGE_ATTACHED
)
RESOURCEUSAGE_RESERVED = 0x80000000
RESOURCEDISPLAYTYPE_GENERIC = 0x00000000
RESOURCEDISPLAYTYPE_DOMAIN = 0x00000001
RESOURCEDISPLAYTYPE_SERVER = 0x00000002
RESOURCEDISPLAYTYPE_SHARE = 0x00000003
RESOURCEDISPLAYTYPE_FILE = 0x00000004
RESOURCEDISPLAYTYPE_GROUP = 0x00000005
RESOURCEDISPLAYTYPE_NETWORK = 0x00000006
RESOURCEDISPLAYTYPE_ROOT = 0x00000007
RESOURCEDISPLAYTYPE_SHAREADMIN = 0x00000008
RESOURCEDISPLAYTYPE_DIRECTORY = 0x00000009
RESOURCEDISPLAYTYPE_TREE = 0x0000000A
RESOURCEDISPLAYTYPE_NDSCONTAINER = 0x0000000B
NETPROPERTY_PERSISTENT = 1
CONNECT_UPDATE_PROFILE = 0x00000001
CONNECT_UPDATE_RECENT = 0x00000002
CONNECT_TEMPORARY = 0x00000004
CONNECT_INTERACTIVE = 0x00000008
CONNECT_PROMPT = 0x00000010
CONNECT_NEED_DRIVE = 0x00000020
CONNECT_REFCOUNT = 0x00000040
CONNECT_REDIRECT = 0x00000080
CONNECT_LOCALDRIVE = 0x00000100
CONNECT_CURRENT_MEDIA = 0x00000200
CONNECT_DEFERRED = 0x00000400
CONNECT_RESERVED = 0xFF000000
CONNDLG_RO_PATH = 0x00000001
CONNDLG_CONN_POINT = 0x00000002
CONNDLG_USE_MRU = 0x00000004
CONNDLG_HIDE_BOX = 0x00000008
CONNDLG_PERSIST = 0x00000010
CONNDLG_NOT_PERSIST = 0x00000020
DISC_UPDATE_PROFILE = 0x00000001
DISC_NO_FORCE = 0x00000040
UNIVERSAL_NAME_INFO_LEVEL = 0x00000001
REMOTE_NAME_INFO_LEVEL = 0x00000002
WNFMT_MULTILINE = 0x01
WNFMT_ABBREVIATED = 0x02
WNFMT_INENUM = 0x10
WNFMT_CONNECTION = 0x20
NETINFO_DLL16 = 0x00000001
NETINFO_DISKRED = 0x00000004
NETINFO_PRINTERRED = 0x00000008
RP_LOGON = 0x01
RP_INIFILE = 0x02
PP_DISPLAYERRORS = 0x01
WNCON_FORNETCARD = 0x00000001
WNCON_NOTROUTED = 0x00000002
WNCON_SLOWLINK = 0x00000004
WNCON_DYNAMIC = 0x00000008

```


---

## win32/Demos/winprocess.py

```python
"""
Windows Process Control

winprocess.run launches a child process and returns the exit code.
Optionally, it can:
  redirect stdin, stdout & stderr to files
  run the command as another user
  limit the process's running time
  control the process window (location, size, window state, desktop)
Works on Windows NT, 2000 & XP. Requires Mark Hammond's win32
extensions.

This code is free for any purpose, with no warranty of any kind.
-- John B. Dell'Aquila <jbd@alum.mit.edu>
"""

import msvcrt
import os

import win32api
import win32con
import win32event
import win32gui
import win32process
import win32security


def logonUser(loginString):
    """
    Login as specified user and return handle.
    loginString:  'Domain\nUser\nPassword'; for local
        login use . or empty string as domain
        e.g. '.\nadministrator\nsecret_password'
    """
    domain, user, passwd = loginString.split("\n")
    return win32security.LogonUser(
        user,
        domain,
        passwd,
        win32con.LOGON32_LOGON_INTERACTIVE,
        win32con.LOGON32_PROVIDER_DEFAULT,
    )


class Process:
    """
    A Windows process.
    """

    def __init__(
        self,
        cmd,
        login=None,
        hStdin=None,
        hStdout=None,
        hStderr=None,
        show=1,
        xy=None,
        xySize=None,
        desktop=None,
    ):
        """
        Create a Windows process.
        cmd:     command to run
        login:   run as user 'Domain\nUser\nPassword'
        hStdin, hStdout, hStderr:
                 handles for process I/O; default is caller's stdin,
                 stdout & stderr
        show:    wShowWindow (0=SW_HIDE, 1=SW_NORMAL, ...)
        xy:      window offset (x, y) of upper left corner in pixels
        xySize:  window size (width, height) in pixels
        desktop: lpDesktop - name of desktop e.g. 'winsta0\\default'
                 None = inherit current desktop
                 '' = create new desktop if necessary

        User calling login requires additional privileges:
          Act as part of the operating system [not needed on Windows XP]
          Increase quotas
          Replace a process level token
        Login string must EITHER be an administrator's account
        (ordinary user can't access current desktop - see Microsoft
        Q165194) OR use desktop='' to run another desktop invisibly
        (may be very slow to startup & finalize).
        """
        si = win32process.STARTUPINFO()
        si.dwFlags = win32con.STARTF_USESTDHANDLES ^ win32con.STARTF_USESHOWWINDOW
        if hStdin is None:
            si.hStdInput = win32api.GetStdHandle(win32api.STD_INPUT_HANDLE)
        else:
            si.hStdInput = hStdin
        if hStdout is None:
            si.hStdOutput = win32api.GetStdHandle(win32api.STD_OUTPUT_HANDLE)
        else:
            si.hStdOutput = hStdout
        if hStderr is None:
            si.hStdError = win32api.GetStdHandle(win32api.STD_ERROR_HANDLE)
        else:
            si.hStdError = hStderr
        si.wShowWindow = show
        if xy is not None:
            si.dwX, si.dwY = xy
            si.dwFlags ^= win32con.STARTF_USEPOSITION
        if xySize is not None:
            si.dwXSize, si.dwYSize = xySize
            si.dwFlags ^= win32con.STARTF_USESIZE
        if desktop is not None:
            si.lpDesktop = desktop
        procArgs = (
            None,  # appName
            cmd,  # commandLine
            None,  # processAttributes
            None,  # threadAttributes
            1,  # bInheritHandles
            win32process.CREATE_NEW_CONSOLE,  # dwCreationFlags
            None,  # newEnvironment
            None,  # currentDirectory
            si,
        )  # startupinfo
        if login is not None:
            hUser = logonUser(login)
            win32security.ImpersonateLoggedOnUser(hUser)
            procHandles = win32process.CreateProcessAsUser(hUser, *procArgs)
            win32security.RevertToSelf()
        else:
            procHandles = win32process.CreateProcess(*procArgs)
        self.hProcess, self.hThread, self.PId, self.TId = procHandles

    def wait(self, mSec=None):
        """
        Wait for process to finish or for specified number of
        milliseconds to elapse.
        """
        if mSec is None:
            mSec = win32event.INFINITE
        return win32event.WaitForSingleObject(self.hProcess, mSec)

    def kill(self, gracePeriod=5000):
        """
        Kill process. Try for an orderly shutdown via WM_CLOSE.  If
        still running after gracePeriod (5 sec. default), terminate.
        """
        win32gui.EnumWindows(self.__close__, 0)
        if self.wait(gracePeriod) != win32event.WAIT_OBJECT_0:
            win32process.TerminateProcess(self.hProcess, 0)
            win32api.Sleep(100)  # wait for resources to be released

    def __close__(self, hwnd, dummy):
        """
        EnumWindows callback - sends WM_CLOSE to any window
        owned by this process.
        """
        TId, PId = win32process.GetWindowThreadProcessId(hwnd)
        if PId == self.PId:
            win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)

    def exitCode(self):
        """
        Return process exit code.
        """
        return win32process.GetExitCodeProcess(self.hProcess)


def run(cmd, mSec=None, stdin=None, stdout=None, stderr=None, **kw):
    """
    Run cmd as a child process and return exit code.
    mSec:  terminate cmd after specified number of milliseconds
    stdin, stdout, stderr:
           file objects for child I/O (use hStdin etc. to attach
           handles instead of files); default is caller's stdin,
           stdout & stderr;
    kw:    see Process.__init__ for more keyword options
    """
    if stdin is not None:
        kw["hStdin"] = msvcrt.get_osfhandle(stdin.fileno())
    if stdout is not None:
        kw["hStdout"] = msvcrt.get_osfhandle(stdout.fileno())
    if stderr is not None:
        kw["hStderr"] = msvcrt.get_osfhandle(stderr.fileno())
    child = Process(cmd, **kw)
    if child.wait(mSec) != win32event.WAIT_OBJECT_0:
        child.kill()
        raise OSError("process timeout exceeded")
    return child.exitCode()


if __name__ == "__main__":
    # Pipe commands to a shell and display the output in notepad
    print("Testing winprocess.py...")

    import tempfile

    timeoutSeconds = 15
    cmdString = (
        """\
REM      Test of winprocess.py piping commands to a shell.\r
REM      This 'notepad' process will terminate in %d seconds.\r
vol\r
net user\r
_this_is_a_test_of_stderr_\r
"""
        % timeoutSeconds
    )

    cmd_name = tempfile.mktemp()
    out_name = cmd_name + ".txt"
    try:
        cmd = open(cmd_name, "w+b")
        out = open(out_name, "w+b")
        cmd.write(cmdString.encode("mbcs"))
        cmd.seek(0)
        print(
            "CMD.EXE exit code:",
            run("cmd.exe", show=0, stdin=cmd, stdout=out, stderr=out),
        )
        cmd.close()
        print(
            "NOTEPAD exit code:",
            run(
                "notepad.exe %s" % out.name,
                show=win32con.SW_MAXIMIZE,
                mSec=timeoutSeconds * 1000,
            ),
        )
        out.close()
    finally:
        for n in (cmd_name, out_name):
            try:
                os.unlink(cmd_name)
            except OSError:
                pass

```
