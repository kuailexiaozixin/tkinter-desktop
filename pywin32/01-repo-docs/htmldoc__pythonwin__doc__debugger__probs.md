# pythonwin/doc/debugger/probs.html

> 来源：https://github.com/mhammond/pywin32/blob/main/pythonwin/doc/debugger/probs.html
> （该文档在 mhammond.github.io 文档站已 404，仅仓库内存在，此处为全文转录）

## Pythonwin Debugger Known Problems

This document lists the currently known problems with the pywin.debugger package.

You may also wish to view the debugger overview, the debugger tutorial, or the general debugger documentation.

#### Closing the main debugger application while debugging may cause strange results.

This is particularly true when debugging non-Pythonwin applications. I have made some efforts in this area, but it is pretty hard and complex.

Closing the debugger dialog, selecting "End/Close" from one of the property pages, or "Close" from the debugging toolbar should always work as expected.

#### Debugging the bottom call-stack does not work as expected.

If you are ever debugging a function that is the only function in the call-stack (ie you are at the bottom stack), then the functions "run" "step out" and "step over" may not work as expected - each of these operations may function as a single-step.

You will need to single-step out of this entire function.

#### Output window does not show function arguments

This is a restriction in the core Python interpreter, caused by the introduction of keyword arguments. When Python supports it again, so will I.
