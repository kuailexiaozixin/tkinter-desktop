# 模块 timer

> 来源：https://mhammond.github.io/pywin32/timer.html （及其成员页，已全部内联）

## Module timer

 Extension that wraps Win32 Timer functions

#### Methods

- set_timer

 Creates a timer that executes a callback function

- kill_timer

 Stops a timer


---

# timer 成员详细文档（共 2 项）


---

<!-- page: timer__kill_timer_meth.html -->

## timer.kill_timer

 boolean = kill_timer(IDEvent)

Creates a timer that executes a callback function

#### Parameters

- IDEvent : int

 Timer id as returned by timer::set_timer

#### Comments

 Uses the KillTimer API function.


---

<!-- page: timer__set_timer_meth.html -->

## timer.set_timer

 int = set_timer(Elapse, TimerFunc )

Creates a timer that executes a callback function

#### Parameters

- Elapse : int

 Timer period, in milliseconds

- TimerFunc : function

 Callback function. Will be called with with 2 int args: (timer_id, time)

#### Comments

 Uses the SetTimer function.

#### Return Value

Returns the id of the timer, which can be passed to kill_timer to stop it.
