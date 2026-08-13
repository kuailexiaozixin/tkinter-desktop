# 模块 win32event

> 来源：https://mhammond.github.io/pywin32/win32event.html （及其成员页，已全部内联）

## Module win32event

 A module which provides an interface to the win32 event/wait API

#### Methods

- CancelWaitableTimer

 Cancels a waiting timer.

- CreateEvent

 Creates a waitable event

- CreateMutex

 Creates a mutex

- CreateSemaphore

 Creates a semaphore, or opens an existing one

- CreateWaitableTimer

 Creates a waitable timer, or opens an existing one

- CreateWaitableTimerEx

 Creates or opens a waitable timer object and returns a handle to the object

- MsgWaitForMultipleObjects

 Returns when a message arrives of an event is signalled

- MsgWaitForMultipleObjectsEx

 Returns when a message arrives of an event is signalled

- OpenEvent

 Returns a handle of an existing named event object.

- OpenMutex

 Returns a handle of an existing named mutex object.

- OpenSemaphore

 Returns a handle of an existing named semaphore object.

- OpenWaitableTimer

 Opens an existing named waitable timer object

- PulseEvent

 Provides a single operation that sets (to signaled) the state of the specified event object and then resets it (to nonsignaled) after releasing the appropriate number of waiting threads.

- ReleaseMutex

 Releases a mutex.

- ReleaseSemaphore

 Releases a semaphore.

- ResetEvent

 Resets an event

- SetEvent

 Sets an event

- SetWaitableTimer

 Sets a waitable timer.

- WaitForMultipleObjects

 Returns when an event is signalled

- WaitForMultipleObjectsEx

 Returns when an event is signalled

- WaitForSingleObject

 Returns when an event is signalled

- WaitForSingleObjectEx

 Returns when an event is signalled

- WaitForInputIdle

 Waits until the given process is waiting for user input with no input pending, or until the time-out interval has elapsed


---

# win32event 成员详细文档（共 23 项）


---

<!-- page: win32event__CancelWaitableTimer_meth.html -->

## win32event.CancelWaitableTimer

 CancelWaitableTimer()

Cancels a waiting timer.


---

<!-- page: win32event__CreateEvent_meth.html -->

## win32event.CreateEvent

 PyHANDLE = CreateEvent(EventAttributes, bManualReset , bInitialState , Name )

Creates a waitable event

#### Parameters

- EventAttributes : PySECURITY_ATTRIBUTES

 The security attributes, or None

- bManualReset : bool

 flag for manual-reset event

- bInitialState : bool

 flag for initial state

- Name : PyUnicode

 event-object name, or None

#### Return Value

The result is a handle to the created object


---

<!-- page: win32event__CreateMutex_meth.html -->

## win32event.CreateMutex

 PyHANDLE = CreateMutex(MutexAttributes, InitialOwner , Name )

Creates a mutex

#### Parameters

- MutexAttributes : PySECURITY_ATTRIBUTES

 Specifies inheritance and security descriptor for object, or None for defaults

- InitialOwner : bool

 flag for initial ownership

- Name : PyUnicode

 Mutex-object name, or None

#### Return Value

The result is a handle to the created object


---

<!-- page: win32event__CreateSemaphore_meth.html -->

## win32event.CreateSemaphore

 PyHANDLE = CreateSemaphore(SemaphoreAttributes, InitialCount , MaximumCount , SemaphoreName )

Creates a semaphore, or opens an existing one

#### Parameters

- SemaphoreAttributes : PySECURITY_ATTRIBUTES

 Specifies inheritance and security descriptor for object, or None for defaults

- InitialCount : int

 Initial count

- MaximumCount : int

 Maximum count

- SemaphoreName : str

 Semaphore-object name, or None

#### Win32 API References

- Search for CreateSemaphore at [msdn](https://learn.microsoft.com/en-ca/search/?terms=CreateSemaphore), [google](https://www.google.com/search?q=CreateSemaphore) or [google groups](https://groups.google.com/groups?q=CreateSemaphore).

#### Return Value

The result is a handle to the object


---

<!-- page: win32event__CreateWaitableTimerEx_meth.html -->

## win32event.CreateWaitableTimerEx

 PyHANDLE = CreateWaitableTimerEx(TimerAttributes, TimerName , Flags , DesiredAccess )

Creates or opens a waitable timer object and returns a handle to the object

#### Parameters

- TimerAttributes : PySECURITY_ATTRIBUTES

 Specifies inheritance and security descriptor for object, or None for defaults

- TimerName : str

 Timer object name, or None

- Flags : int

 Flags

- DesiredAccess : int

 The access mask for the timer object

#### Win32 API References

- Search for CreateWaitableTimerEx at [msdn](https://learn.microsoft.com/en-ca/search/?terms=CreateWaitableTimerEx), [google](https://www.google.com/search?q=CreateWaitableTimerEx) or [google groups](https://groups.google.com/groups?q=CreateWaitableTimerEx).

#### Return Value

The result is a handle to the object


---

<!-- page: win32event__CreateWaitableTimer_meth.html -->

## win32event.CreateWaitableTimer

 PyHANDLE = CreateWaitableTimer(TimerAttributes, ManualReset , TimerName )

Creates a waitable timer, or opens an existing one

#### Parameters

- TimerAttributes : PySECURITY_ATTRIBUTES

 Specifies inheritance and security descriptor for object, or None for defaults

- ManualReset : bool

 True for manual reset timer, or False to create a synchronization timer

- TimerName : str

 Timer object name, or None

#### Win32 API References

- Search for CreateWaitableTimer at [msdn](https://learn.microsoft.com/en-ca/search/?terms=CreateWaitableTimer), [google](https://www.google.com/search?q=CreateWaitableTimer) or [google groups](https://groups.google.com/groups?q=CreateWaitableTimer).

#### Return Value

The result is a handle to the object


---

<!-- page: win32event__MsgWaitForMultipleObjectsEx_meth.html -->

## win32event.MsgWaitForMultipleObjectsEx

 int = MsgWaitForMultipleObjectsEx(handleList, milliseconds , wakeMask , waitFlags )

Returns when a message arrives of an event is signalled

#### Parameters

- handleList : [PyHANDLE, ...]

 A sequence of handles to wait on.

- milliseconds : int

 time-out interval in milliseconds

- wakeMask : int

 type of input events to wait for

- waitFlags : int

 wait flags

#### Comments

 This method will no longer raise a COM E_NOTIMPL exception as it is no longer dynamically loaded.


---

<!-- page: win32event__MsgWaitForMultipleObjects_meth.html -->

## win32event.MsgWaitForMultipleObjects

 int = MsgWaitForMultipleObjects(handleList, bWaitAll , milliseconds , wakeMask )

Returns when a message arrives of an event is signalled

#### Parameters

- handleList : [PyHANDLE, ...]

 A sequence of handles to wait on.

- bWaitAll : bool

 If true, waits for all handles in the list.

- milliseconds : int

 time-out interval in milliseconds

- wakeMask : int

 type of input events to wait for. One of the win32event.QS_ constants.

#### Comments

 Note that if bWaitAll is TRUE, the function will return when there is input in the queue, and all events are signalled. This is rarely what you want! If input is waiting, the result is win32event.WAIT_OBJECT_0+len(handles))


---

<!-- page: win32event__OpenEvent_meth.html -->

## win32event.OpenEvent

 PyHANDLE = OpenEvent(desiredAccess, bInheritHandle , name )

Returns a handle of an existing named event object.

#### Parameters

- desiredAccess : int

 access flag - one of win32event::EVENT_ALL_ACCESS , win32event::EVENT_MODIFY_STATE , or (NT only) win32event::SYNCHRONIZE

- bInheritHandle : bool

 inherit flag

- name : PyUnicode

 name of event to open.


---

<!-- page: win32event__OpenMutex_meth.html -->

## win32event.OpenMutex

 PyHANDLE = OpenMutex(desiredAccess, bInheritHandle , name )

Returns a handle of an existing named mutex object.

#### Parameters

- desiredAccess : int

 access flag

- bInheritHandle : bool

 inherit flag

- name : PyUnicode

 name of mutex to open.


---

<!-- page: win32event__OpenSemaphore_meth.html -->

## win32event.OpenSemaphore

 PyHANDLE = OpenSemaphore(desiredAccess, bInheritHandle , name )

Returns a handle of an existing named semaphore object.

#### Parameters

- desiredAccess : int

 access flag

- bInheritHandle : bool

 inherit flag

- name : PyUnicode

 name of semaphore to open.


---

<!-- page: win32event__OpenWaitableTimer_meth.html -->

## win32event.OpenWaitableTimer

 PyHANDLE = OpenWaitableTimer(desiredAccess, bInheritHandle , timerName )

Opens an existing named waitable timer object

#### Parameters

- desiredAccess : int

 access flag

- bInheritHandle : bool

 inherit flag

- timerName : str

 pointer to timer object name


---

<!-- page: win32event__PulseEvent_meth.html -->

## win32event.PulseEvent

 PulseEvent(hEvent)

Provides a single operation that sets (to signaled) the state of the specified event object and then resets it (to nonsignaled) after releasing the appropriate number of waiting threads.

#### Parameters

- hEvent : PyHANDLE

 handle of event object


---

<!-- page: win32event__ReleaseMutex_meth.html -->

## win32event.ReleaseMutex

 ReleaseMutex(hEvent)

Releases a mutex.

#### Parameters

- hEvent : PyHANDLE

 handle of mutex object


---

<!-- page: win32event__ReleaseSemaphore_meth.html -->

## win32event.ReleaseSemaphore

 int = ReleaseSemaphore(hEvent, lReleaseCount )

Releases a semaphore.

#### Parameters

- hEvent : PyHANDLE

 handle of the semaphore object

- lReleaseCount : int

 amount to add to current count

#### Return Value

The result is the previous count of the semaphore.


---

<!-- page: win32event__ResetEvent_meth.html -->

## win32event.ResetEvent

 ResetEvent(hEvent)

Resets an event

#### Parameters

- hEvent : PyHANDLE

 handle of event object


---

<!-- page: win32event__SetEvent_meth.html -->

## win32event.SetEvent

 SetEvent(hEvent)

Sets an event

#### Parameters

- hEvent : PyHANDLE

 handle of event object


---

<!-- page: win32event__SetWaitableTimer_meth.html -->

## win32event.SetWaitableTimer

 SetWaitableTimer(handle, dueTime, period, func, param, resume_state)

Sets a waitable timer.

#### Parameters

- handle : PyHANDLE

 handle to timer

- dueTime : long

 timer due time

- period : int

 timer interval

- func : object

 completion routine - must be None

- param : object

 completion routine parameter - must be None

- resume_state : bool

 resume state


---

<!-- page: win32event__WaitForInputIdle_meth.html -->

## win32event.WaitForInputIdle

 int = WaitForInputIdle(hProcess, milliseconds )

Waits until the given process is waiting for user input with no input pending, or until the time-out interval has elapsed

#### Parameters

- hProcess : PyHANDLE

 handle of process to wait for

- milliseconds : int

 time-out interval in milliseconds

#### Return Value

The return value indicates wether the process is ready or wether it timed out. This value can be one of the following.

| | Value | Meaning
| |

---

 |

---

| | 0 | The process is ready.
| | WAIT_TIMEOUT | The time-out interval elapsed, and the process is not ready.


---

<!-- page: win32event__WaitForMultipleObjectsEx_meth.html -->

## win32event.WaitForMultipleObjectsEx

 int = WaitForMultipleObjectsEx(handleList, bWaitAll , milliseconds , bAlertable )

Returns when an event is signalled

#### Parameters

- handleList : [PyHANDLE, ...]

 A sequence of handles to wait on.

- bWaitAll : bool

 wait flag

- milliseconds : int

 time-out interval in milliseconds

- bAlertable : bool

 alertable wait flag.


---

<!-- page: win32event__WaitForMultipleObjects_meth.html -->

## win32event.WaitForMultipleObjects

 int = WaitForMultipleObjects(handleList, bWaitAll , milliseconds )

Returns when an event is signalled

#### Parameters

- handleList : [PyHANDLE, ...]

 A sequence of handles to wait on.

- bWaitAll : bool

 wait flag

- milliseconds : int

 time-out interval in milliseconds


---

<!-- page: win32event__WaitForSingleObjectEx_meth.html -->

## win32event.WaitForSingleObjectEx

 int = WaitForSingleObjectEx(hHandle, milliseconds , bAlertable )

Returns when an event is signalled

#### Parameters

- hHandle : PyHANDLE

 handle of object to wait for

- milliseconds : int

 time-out interval in milliseconds

- bAlertable : bool

 alertable wait flag.

#### Return Value

See win32event::WaitForSingleObject for return values.


---

<!-- page: win32event__WaitForSingleObject_meth.html -->

## win32event.WaitForSingleObject

 int = WaitForSingleObject(hHandle, milliseconds )

Returns when an event is signalled

#### Parameters

- hHandle : PyHANDLE

 handle of object to wait for

- milliseconds : int

 time-out interval in milliseconds

#### Return Value

If the function succeeds, the return value indicates the event that caused the function to return. This value can be one of the following.

| | Value | Meaning
| |

---

 |

---

| | WAIT_ABANDONED | The specified object is a mutex object that was not released by the thread that owned the mutex object before the owning thread terminated. Ownership of the mutex object is granted to the calling thread, and the mutex is set to nonsignaled.
| | WAIT_OBJECT_0 | The state of the specified object is signaled.
| | WAIT_TIMEOUT | The time-out interval elapsed, and the object's state is nonsignaled.
