---
name: tcl-tk
description: >
  在 Python / Tkinter 应用中直接调用底层 Tcl/Tk 命令的桥接技能。覆盖 tkinter 与 Tcl
  解释器的全部桥接接口——独立 Tcl 解释器（tkinter.Tcl）、widget.tk、eval/call、
  Tcl 变量读写（getvar/globalsetvar）、Python↔Tcl 类型转换、createcommand 回调、
  evalfile 加载 .tcl 脚本；以及调用 tkinter 未封装的高级 Tk 能力（ttk::style 底层、
  wm 高级操作、虚拟事件/bindtags、clipboard/selection/grab、option 数据库）。
  以 Tcl/Tk 8.6 官方文档镜像（tcl8.6-docs）为权威参考。
  当用户需要在 tkinter 中执行 Tcl 命令、调用 tkinter 未封装的 Tk 功能、读写 Tcl 变量、
  把 Python 函数暴露给 Tcl 解释器、或编写/执行 .tcl 脚本时使用本技能。
  触发词：Tcl、tkinter 调用 Tcl、widget.tk、tk.eval、tk.call、Tcl()、createcommand、
  evalfile、ttk::style、虚拟事件、Tcl 变量、tkinter 底层。
version: "1.0.0"
author: agent
agent_created: true
platform: windows
---

# tcl-tk — 在 Tkinter 中调用 Tcl/Tk

> **一句话**：tkinter 本身就是 Tk 的 Python 绑定，每个控件背后都挂着一个 Tcl/Tk 解释器。
> 本技能教你**越过 tkinter 的封装、直接用 Tcl/Tk 命令**，从而调用 tkinter 未暴露的高级能力。

## 适用场景

| 场景 | 用到的桥接接口 |
|------|----------------|
| 调用 tkinter 未封装的 Tk 命令（ttk::style 底层、wm 高级操作等） | `widget.tk.eval/call` |
| 读写 Tcl 全局变量 / 与 Tk 变量联动 | `tk.globalsetvar/globalgetvar` |
| 执行一段 Tcl 脚本片段 | `tk.eval(tcl_string)` |
| 加载并执行 `.tcl` 脚本文件 | `tk.evalfile(path)` |
| 把 Python 函数暴露给 Tcl 调用 | `tk.createcommand(name, func)` |
| 脱离 GUI 跑纯 Tcl 脚本（无窗口） | `tkinter.Tcl()` 独立解释器 |
| 解析 Tcl 列表 / 转义字符串 | `tk.splitlist` / `tk.call` |
| 深度定制 ttk 主题 / 样式 | `ttk::style` 子命令（`tk.call('ttk::style', ...)`） |

---

## Tcl 语法速查（给不熟 Tcl 的读者）

调用 `eval/call` 前，先掌握 Tcl 最小语法，否则读不懂命令串：

| 语法 | 示例 | 说明 |
|------|------|------|
| 命令 = 单词序列 | `set x 42` | 第一个词是命令名，后续是参数 |
| 变量替换 `$name` | `set y $x` | 取变量 `x` 的值 |
| 命令替换 `[cmd]` | `set z [expr {$x+1}]` | 括号内命令结果作为值 |
| 双引号分组 `"..."` | `puts "hi $name"` | 保留内部 `$` / `[` 替换 |
| 花括号分组 `{...}` | `set s {a b c}` | **不**做 `$` / `[` 替换，原样 |
| 列表 `{a b c}` | `splitlist` | Tcl 列表 = 空格分隔单词，可花括号分组 |
| 注释 `#` | `# 注释` | 仅在命令位置开头生效 |

> **铁律**：传给 `eval` 的字符串里，`$` / `[` / 引号 / 花括号都有特殊含义。**只要参数可能含这些字符，就用 `call` 以独立 token 传入，避免手工拼接字符串**（见下文「陷阱与铁律」）。

读官方命令页时先看它的语法签名行（如 `wm geometry window ?newGeometry?`），问号表示可选参数。

---

## 核心接口（均经运行期验证，Tk 8.6 / Tcl 8.6）

### 1. 两种解释器入口

**A. `tkinter.Tcl()` — 独立 Tcl 解释器（无 GUI）**
```python
import tkinter as tk
tcl = tk.Tcl()                      # 创建独立 Tcl 解释器，无窗口
tcl.eval('set x 42')                # 执行 Tcl 脚本
tcl.eval('expr {$x * 2}')           # -> '84'
```
适合：纯 Tcl 脚本、数据处理、测试 Tcl 命令，**不需要窗口**。

**B. `widget.tk` — 现有 Tk 应用的 Tcl 解释器**
```python
import tkinter as tk
root = tk.Tk()
w = tk.Button(root, text='Hi')
tcl = w.tk                          # _tkinter.tkapp，即 root 背后的 Tcl 解释器
tcl.eval('wm title . "我的窗口"')   # 直接操作 Tk 主窗口
```
每个 `Tk` 根窗口与所有 `Tk` 控件共享同一个 Tcl 解释器（`widget.tk` 指向它）。

### 2. 执行 Tcl 命令：`eval` vs `call`

| 方法 | 说明 | 推荐 |
|------|------|------|
| `tcl.eval(tcl_string)` | 把整段 Tcl 脚本当字符串解析执行 | 复杂脚本、多命令 |
| `tcl.call('cmd', arg1, arg2)` | 把参数作为**独立 token** 传给 Tcl 命令，自动转义 | **推荐**——免手工转义，防注入 |

```python
tcl.call('string', 'toupper', 'abc')   # -> 'ABC'
# call 会自动转义参数，含空格/引号也安全：
tcl.call('set', 'name', 'He said "hi"')  # 参数原样，不破坏 Tcl 语法
```
**铁律**：只要参数可能含空格/引号/`$`/`[`，一律用 `call` 而非字符串拼接 `eval`。

### 3. Tcl 变量读写

```python
tcl.setvar('myname', 'Tcl')            # 设置局部/全局变量
tcl.getvar('myname')                   # -> 'Tcl'
tcl.globalsetvar('g', 5)               # 设置全局变量
tcl.globalgetvar('g')                  # -> '5'
```
与 tkinter 变量类联动：`tk.StringVar/IntVar/DoubleVar/BooleanVar` 底层就是 Tcl 变量。
```python
sv = tk.StringVar(root, 'hello')
sv.get()                               # -> 'hello'
root.tk.globalgetvar('PY_VAR0')        # -> 'hello'（StringVar 绑定的 Tcl 变量）
```

### 4. 类型转换

```python
tcl.getboolean('true')    # -> True
tcl.getint('  42  ')      # -> 42
tcl.getdouble('3.14')     # -> 3.14
tcl.splitlist('a b c')    # -> ('a', 'b', 'c')（Tcl 列表 -> Python tuple）
tcl.splitlist('{a b} c')  # -> ('a b', 'c')（花括号分组保留）
```
`tk.call` 的返回值是字符串；需要数字/布尔时用 `getint/getboolean/getdouble` 转换。

### 5. 回调：`createcommand`（Python 函数 -> Tcl 命令）

```python
def my_func(x):
    return 'pypy' + str(x)
root.tk.createcommand('py_cmd', my_func)
root.tk.eval('py_cmd 7')     # -> 'pypy7'
```
用途：让 Tcl 脚本/命令回调 Python 逻辑（如 Tcl 侧的事件、after、ttk style 查询等）。
注意：回调在 Tk 主线程执行；不能跨线程调用 UI 操作。

### 6. 加载 `.tcl` 脚本

```python
tcl.evalfile('path/to/script.tcl')   # 加载并执行 Tcl 文件
```
或 `tcl.eval(open('f.tcl').read())`。

---

## Python ↔ Tcl 类型转换速查

| Python | Tcl | 说明 |
|--------|-----|------|
| `int` | 整数字符串 | `call` 自动转 |
| `float` | 浮点字符串 | 同上 |
| `str` | 字符串（自动转义） | `call` 安全 |
| `bool` | `1`/`0` | 用 `getboolean` 读回 |
| `None` | 空字符串 | 注意 |
| `tuple`/`list` | Tcl list | Tcl 列表经 `call`/`splitlist` 自动转 Python **tuple**；写回用 `tcl.call('list', *items)` |
| `bytes` | 二进制串 | 谨慎，Tcl 8.6 默认按字节 |

---

## 常见场景（调用 tkinter 未封装能力）

### ttk::style 底层定制
```python
# 读取当前主题
root.tk.call('ttk::style', 'theme', 'use')      # -> 主题名
# 设置 ttk 元素选项
root.tk.call('ttk::style', 'configure', '.', 'font', '{TkDefaultFont 10}')
```
参考 `tcl8.6-docs/TkCmd/ttk_style.md` 全部子命令。

### wm 高级操作
```python
root.tk.call('wm', 'attributes', '.', '-topmost', '1')   # 置顶
root.tk.call('wm', 'geometry', '.', '800x600+100+50')
```
参考 `tcl8.6-docs/TkCmd/wm.md`。

### 虚拟事件 / bindtags
```python
root.tk.call('bind', '<<CustomEvent>>', 'puts {fired}')  # 绑虚拟事件
```
参考 `tcl8.6-docs/TkCmd/bind.md`、`bindtags.md`。

### clipboard / selection / grab
```python
root.tk.call('clipboard', 'clear')
root.tk.call('clipboard', 'append', '--', 'text')
```
参考 `tcl8.6-docs/TkCmd/clipboard.md`、`selection.md`、`grab.md`。

---

## 陷阱与铁律

1. **主线程规则**：Tk/Tcl 必须在主线程操作。`createcommand` 回调、`after` 都在主线程执行；跨线程直接调 tkinter 会崩溃或抛异常。
2. **eval 注入**：用户输入进 Tcl 命令，**必须用 `call`（独立 token），禁止字符串拼接 `eval`**，否则 `$`/`[`/引号会造成代码注入或语法错误。
3. **返回值是字符串**：`call/eval` 返回 `str`，数字/布尔需 `getint/getboolean` 转换。
4. **列表转换**：Tcl 列表 ↔ Python 用 `splitlist`（返回 tuple）与 `call('list',...)`，不要手动 split 字符串（Tcl 列表含转义/花括号）。
5. **编码**：中文文本走 `call` 自动处理 UTF-8；避免手工 encode/decode。
6. **`tk.split` 不存在**：`_tkinter.tkapp` 没有 `.split` 方法，用 `tcl.eval('split ...')` 或 `splitlist`。

---

## 与 references/official-docs 的分工

`tkinter-desktop` 主技能的 `references/official-docs/` 是 tkinter 官方转档（Python 视角），本技能的 `tcl8.6-docs/` 是 Tcl/Tk 官方文档镜像（底层命令视角）。两者互补，按问题视角选择：

| 问题视角 | 查哪里 |
|---------|--------|
| 「Python 里怎么调」— tkinter 封装的方法/选项/事件 | `references/official-docs/tkinter-core.md` / `tkinter-ttk.md` |
| 「底层命令怎么定义」— 某 Tcl/Tk 命令的子命令/选项/语法 | `tcl8.6-docs/TclCmd/`、`tcl8.6-docs/TkCmd/` 对应命令页 |
| tkinter 没封装的底层能力（ttk::style 元素、wm 高级、虚拟事件、clipboard…） | **本技能 + `tcl8.6-docs/`**（主技能转档覆盖不到） |

> 规则：**先查 `11-official-docs` 的 tkinter 视角；确认 tkinter 没封装、或需要直接操纵底层命令时，才进入本技能与 `tcl8.6-docs`。** 两者对同一命令的描述应一致（同源 8.6），如冲突以 `tcl8.6-docs`（命令权威定义）为准。

---

## 权威参考（tcl8.6-docs 官方文档镜像）

本技能所有 Tcl/Tk 命令的**权威定义**以 Tcl/Tk 8.6 官方文档本地镜像为准：
`./tcl8.6-docs/`

| 需要查 | 打开 |
|--------|------|
| Tcl 命令全集（tclsh 实现） | `tcl8.6-docs/TclCmd/contents.md` |
| Tk 命令全集（wish 实现） | `tcl8.6-docs/TkCmd/contents.md` |
| ttk::style / 主题 | `tcl8.6-docs/TkCmd/ttk_style.md` |
| wm / winfo / grab | `tcl8.6-docs/TkCmd/wm.md`、`winfo.md`、`grab.md` |
| event / bind / bindtags | `tcl8.6-docs/TkCmd/event.md`、`bind.md`、`bindtags.md` |
| clipboard / selection | `tcl8.6-docs/TkCmd/clipboard.md`、`selection.md` |
| option 数据库 | `tcl8.6-docs/TkCmd/option.md` |
| 解释器（tclsh/wish） | `tcl8.6-docs/UserCmd/contents.md` |

> 命令定义以镜像为准；写代码前先查对应命令页确认子命令与选项，避免用错。
