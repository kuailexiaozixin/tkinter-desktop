---
name: pywin32
description: >
  在 Tkinter 应用中通过 pywin32（win32gui / win32api / win32con / win32ui）构建原生
  UI 与系统能力的技能。覆盖原生 Win32 控件嵌入 tkinter（Edit/Button/ComboBox/
  TreeView/ListView 及子类化响应）、系统对话框（文件/颜色/字体）、系统托盘图标、
  COM 自动化驱动其它程序、嵌入 ActiveX/WebBrowser、DPI 与视觉样式；并打通 tkinter
  与 pywin32 的窗口句柄衔接。实战指南见本技能正文；6771 页 pywin32 离线文档全集
  （00-sources/01-repo-docs/02-modules/03-objects/04-constants/05-overviews）
  索引与检索见 README.md。
  当用户需要在 tkinter 中用 pywin32 拼装原生控件、调系统对话框/托盘、做 COM 自动化、
  或查询任意 pywin32 模块/对象/常量时使用本技能。
  触发词：pywin32、win32gui、win32api、win32con、win32ui、原生控件、系统托盘、
  COM、pywin32 离线文档、任务栏图标。
version: "1.0.0"
author: agent
agent_created: true
platform: windows
---

# pywin32 — 在 Tkinter 中构建原生 UI

> **一句话**：pywin32 是 Windows 桌面开发最强大、最完整的原生能力宝库，封装 54 个模块、
> 数百对象与常量，几乎覆盖全部 Windows API。本技能教你**在 tkinter 程序里用 pywin32
> 拼装真正的原生 Win32 控件、调用系统对话框/托盘、做 COM 自动化**，并以 6771 页离线
> 文档全集支撑任意模块/对象/常量的精确查询。


## 适用场景

| 场景 | pywin32 方案 |
|------|-------------|
| 嵌入原生控件（Edit/Button/ComboBox/TreeView/ListView） | `win32gui.CreateWindowEx` |
| 系统文件/颜色/字体对话框 | `win32gui.GetOpenFileNameW` 等 |
| 系统消息框 | `win32gui.MessageBox` / `win32api.MessageBox` |
| 系统托盘图标 | `Shell_NotifyIcon`（需隐藏窗口 + HICON） |
| 用 tkinter 按钮驱动其它程序 | `win32com.client.Dispatch`（COM 自动化） |
| 嵌入 ActiveX / WebBrowser | `win32ui` + `CreateControl` |
| 任务栏图标 / 窗口枚举 / 消息框 | `win32gui` / `win32api` |

> 与兄弟子技能 `ctypes` 的分工：需要**对象化封装/COM/高抽象**时优先 pywin32；
> 需要**零依赖标准库 P/Invoke 任意 DLL** 时用 ctypes（两者都鼓励，按任务选顺手那条）。

---

---

## 实战指南（在 tkinter 中调用 pywin32 构建原生 UI）

本篇讲清楚一件事：**如何在一个 tkinter 程序里直接调用 pywin32（Win32 API / COM），
把 Windows 原生的「控件 / 组件」当成 tkinter 的子窗口来拼装界面**——既保留 tkinter
快速搭界面的优势，又能用上 tkinter 没有的原生能力（TreeView、ListView、系统对话框、
通知区图标、ActiveX、COM 自动化等）。

> **为什么必须重视 pywin32**：它是 Windows 桌面开发最强大、最完整的原生能力宝库，
> 封装了 **54 个模块、数百个对象与常量**（`win32gui` / `win32api` / `win32ui` / `win32con` /
> `shell` / `pythoncom` / `win32com` …），几乎覆盖 Windows 全部原生 API——窗口与控件、GDI
> 绘制、系统托盘、文件/颜色/字体通用对话框、COM 自动化（驱动 Excel/Word/Outlook）、ActiveX
> 嵌入、注册表、服务、网络、安全等。凡是 tkinter 原生做不到的，几乎都能用 pywin32 直接实现；
> 这是把 tkinter 桌面程序提升到「专业 Windows 应用」级别的关键手段。

底层所有 Win32 函数签名、常量、对象方法，详见下文「文档路由」与本目录文档库索引（README.md）：

- `win32gui` → [02-modules/win32gui.md](02-modules/win32gui.md)
- `win32ui`  → [02-modules/win32ui.md](02-modules/win32ui.md)
- `win32api` → [02-modules/win32api.md](02-modules/win32api.md)
- `pythoncom` / COM → [02-modules/pythoncom.md](02-modules/pythoncom.md)
- `shell`（通知区、文件对话框）→ [02-modules/shell.md](02-modules/shell.md)
- ActiveX 控件 → [02-modules/axcontrol.md](02-modules/axcontrol.md)

---

### 目录

1. [核心原理：tkinter 控件本身就是原生窗口](#1-核心原理tkinter-控件本身就是原生窗口)
2. [什么时候该混用 pywin32](#2-什么时候该混用-pywin32)
3. [原生 Win32 控件嵌入 tkinter](#3-原生-win32-控件嵌入-tkinter)
4. [系统对话框、通知区与 COM 自动化](#4-系统对话框通知区与-com-自动化)
5. [进阶：嵌入 ActiveX / WebBrowser](#5-进阶嵌入-activex--webbrowser)
6. [DPI 与视觉样式](#6-dpi-与视觉样式)
7. [必读坑位](#7-必读坑位)

---

### 1. 核心原理：tkinter 控件本身就是原生窗口

Windows 上 tkinter 的每一个 widget（Tk/Toplevel/Frame/…）底层都是一个真实的 Win32 窗口。
拿到它的 HWND 之后，就可以用 `win32gui.CreateWindowEx` 把**任意原生 Win32 控件**作为它的
子窗口创建出来——这些原生控件与 tkinter 自身控件处在同一棵窗口树里，可以随 tkinter 一起
缩放、销毁，外观也由系统统一绘制。

```python
import tkinter as tk
import win32gui, win32con

root = tk.Tk()
host = tk.Frame(root, bg="systemButtonFace")
host.pack(fill="both", expand=True)

## 关键：必须先把窗口“实现”出来，HWND 才有效
root.update_idletasks(); root.update()
hwnd = host.winfo_id()          # Windows 下返回该 Frame 的真实 HWND（其它平台为 0）

edit = win32gui.CreateWindowEx(
    0, "Edit", "原生 Edit 控件",
    win32con.WS_CHILD | win32con.WS_VISIBLE | win32con.WS_BORDER,
    8, 8, 360, 28, hwnd, 0, None, None)

root.mainloop()
```

> 这句 `host.winfo_id()` 是整个方案的钥匙。所有原生控件都必须创建在 **tkinter 已实现的
> 窗口**之下；若在 `root.mainloop()` 之前、`root.update()` 之前就拿 HWND，会得到无效值。

详细用法、缩放、TreeView/ListView、子类化、DPI 见下文第 3、6 节。

---

### 2. 什么时候该混用 pywin32

| 需求 | tkinter 原生 | 用 pywin32 更合适 |
|------|--------------|------------------|
| 普通按钮/输入框/表格 | ✅ 直接用 ttk | — |
| **文件/颜色/字体选择框** | ❌ 没有 | ✅ `win32ui.CreateFileDialog` 等（见第 4 节） |
| **系统通知区（托盘）图标** | ❌ 没有 | ✅ `win32gui.Shell_NotifyIcon` |
| **资源管理器式 TreeView / ListView** | ⚠️ ttk.Treeview 可替代但风格不同 | ✅ 原生 `SysTreeView32` / `SysListView32`（见第 3 节） |
| **嵌入网页 / ActiveX（IE、PDF、OCX）** | ❌ 没有 | ✅ `win32ui.CreateControl`（第 5 节） |
| **驱动 Excel / Word / Outlook 的 UI** | ❌ 没有 | ✅ `win32com.client.Dispatch` |
| **自绘、拖放、截获窗口消息** | ⚠️ 有限 | ✅ `win32gui.SetWindowLong(GWL_WNDPROC, ...)` |

---

### 3. 原生 Win32 控件嵌入 tkinter

核心一句话：**用 `win32gui.CreateWindowEx` 创建原生控件，把 tkinter 控件的 HWND
（`widget.winfo_id()`）作为父窗口句柄。** 下面每个片段都已在 Python 3.13 + pywin32 实测。
所有 `win32gui` / `win32con` 细节以
[02-modules/win32gui.md](02-modules/win32gui.md) 为准。

#### 3.1 最小可运行骨架（Edit / Button / Static）

```python
import tkinter as tk
import win32gui, win32con

root = tk.Tk()
root.title("tkinter + 原生 Win32 控件")
root.geometry("440x320")

host = tk.Frame(root, bg="systemButtonFace")
host.pack(fill="both", expand=True)

## 必须先让 Frame 的真实窗口被创建
root.update_idletasks(); root.update()
hwnd = host.winfo_id()

edit = win32gui.CreateWindowEx(
    0, "Edit", "原生 Edit 控件",
    win32con.WS_CHILD | win32con.WS_VISIBLE | win32con.WS_BORDER,
    8, 8, 400, 28, hwnd, 0x1001, None, None)

btn = win32gui.CreateWindowEx(
    0, "Button", "原生 Button",
    win32con.WS_CHILD | win32con.WS_VISIBLE,
    8, 44, 140, 28, hwnd, 0x1002, None, None)

static = win32gui.CreateWindowEx(
    0, "Static", "原生 Static 标签",
    win32con.WS_CHILD | win32con.WS_VISIBLE,
    160, 50, 240, 20, hwnd, 0x1003, None, None)

## 读写原生控件内容（示例：取 Edit 文本写入 Static）
text = win32gui.GetWindowText(edit)
win32gui.SetWindowText(static, f"当前内容：{text}")

## 原生按钮点击的响应方式见 3.5 节（子类化自己创建的控件）
root.mainloop()
```

控件类名（Win32 预定义）：`Edit`、`Button`、`Static`、`ComboBox`、`ListBox`、`ScrollBar`。
这些**不需要** `InitCommonControls`，直接可用。

#### 3.2 随 Frame 缩放（必做）

原生子控件不会自动跟随 tkinter 布局，父 Frame 尺寸变化时要用 `<Configure>` 同步：

```python
def on_configure(e):
    # e.width/e.height 是 Frame 客户区尺寸
    win32gui.MoveWindow(edit, 8, 8, max(40, e.width - 16), 28, True)
    win32gui.MoveWindow(btn, 8, 44, 140, 28, True)
    win32gui.MoveWindow(static, 160, 50, max(40, e.width - 168), 20, True)

host.bind("<Configure>", on_configure)
```

`win32gui.MoveWindow(hwnd, x, y, w, h, bRepaint)` 最后一个参数 `True` 立即重绘。

#### 3.3 ComboBox / ListBox

```python
combo = win32gui.CreateWindowEx(
    win32con.WS_EX_CLIENTEDGE, "ComboBox", "",
    win32con.WS_CHILD | win32con.WS_VISIBLE | win32con.CBS_DROPDOWNLIST,
    8, 84, 200, 200, hwnd, 0x1004, None, None)
## 逐项添加
for item in ("选项 A", "选项 B", "选项 C"):
    win32gui.SendMessage(combo, win32con.CB_ADDSTRING, 0, item)
win32gui.SendMessage(combo, win32con.CB_SETCURSEL, 0, 0)
```

`ComboBox` 是 Win32 公共控件，但 `CBS_*` 风格常量在 `win32con` 里直接可用，无需额外初始化。

#### 3.4 高级公共控件：TreeView / ListView

`SysTreeView32` / `SysListView32` 属于 `comctl32`，**必须先初始化公共控件库**，否则创建出来是
空白/失败。用 `ctypes` 调 `InitCommonControlsEx`：

```python
import ctypes

class INITCOMMONCONTROLSEX(ctypes.Structure):
    _fields_ = [("dwSize", ctypes.c_uint), ("dwICC", ctypes.c_uint)]

## ICC_TREEVIEW_CLASSES=0x2, ICC_LISTVIEW_CLASSES=0x1
iccx = INITCOMMONCONTROLSEX(ctypes.sizeof(INITCOMMONCONTROLSEX), 0x2 | 0x1)
ctypes.windll.comctl32.InitCommonControlsEx(ctypes.byref(iccx))

## 之后即可创建（风格见 win32con：TVS_*, LVS_*）
tree = win32gui.CreateWindowEx(
    0, "SysTreeView32", "",
    win32con.WS_CHILD | win32con.WS_VISIBLE | win32con.WS_BORDER
    | 0x00000200,   # TVS_HASLINES 等可用 win32con 常量组合
    8, 120, 400, 160, hwnd, 0x1005, None, None)
```

> `TVS_*` / `LVS_*` / `TVM_*` / `LVM_*` 等常量在 `win32con` 中；消息常量（如 `TVM_INSERTITEM`）
> 同样在 `win32con`。需要逐项/逐列操作时用 `win32gui.SendMessage` 配合对应结构体。
> 常量全集见 [04-constants](04-constants)。

#### 3.5 响应原生按钮点击（子类化自己创建的控件）

不要子类化 tkinter 顶层（会破坏 Tcl/Tk 消息循环）。**只子类化你自己 `CreateWindowEx` 出来的
控件**，用 `ctypes` 提供真正的 `WNDPROC`：

```python
import ctypes, ctypes.wintypes as w, win32con

## wintypes 无 LRESULT（见 18 §2 规则②），用 ctypes.c_int64 替代
WNDPROC = ctypes.WINFUNCTYPE(ctypes.c_int64, w.HWND, w.UINT, w.WPARAM, w.LPARAM)

user32 = ctypes.windll.user32
## 必须声明签名：第 3 个参数是指针（64 位），不声明会被 ctypes 当成 c_int 截断 -> OverflowError
user32.SetWindowLongPtrW.argtypes = [w.HWND, ctypes.c_int, ctypes.c_void_p]
user32.SetWindowLongPtrW.restype  = ctypes.c_void_p
user32.CallWindowProcW.argtypes   = [ctypes.c_void_p, w.HWND, w.UINT, w.WPARAM, w.LPARAM]
user32.CallWindowProcW.restype    = ctypes.c_int64

def btn_proc(hwnd, msg, wp, lp):
    if msg == win32con.WM_LBUTTONUP:
        print("原生按钮被点击，hwnd =", hwnd)
    # 其余消息交还给原窗口过程
    return user32.CallWindowProcW(old_proc, hwnd, msg, wp, lp)

btn_wndproc = WNDPROC(btn_proc)
old_proc = user32.SetWindowLongPtrW(
    btn, win32con.GWL_WNDPROC, ctypes.cast(btn_wndproc, ctypes.c_void_p).value)
```

要点：
- `old_proc` 必须保存并在新过程里 `CallWindowProcW` 回退，否则控件失效。
- `WNDPROC` 回调对象（`btn_wndproc`）要保持在引用中，避免被 GC 回收导致崩溃。
- `WM_*` 常量见 `win32con`（[04-constants](04-constants)）。

#### 3.6 清理

父 tkinter 窗口销毁时，其下的原生子控件会一并销毁，通常无需手动清理。若在主窗口存活期间
要移除某个控件：`win32gui.DestroyWindow(child_hwnd)`。注意不要对已销毁的 HWND 再操作。

---

### 4. 系统对话框、通知区与 COM 自动化

本节约覆盖 tkinter 自身没有、但 Windows 桌面程序常需的四类能力：通用对话框、消息框、通知区图标、
以及用 COM 驱动其它程序的 UI。`win32ui` / `win32gui` / `shell` / `pythoncom` 细节以
[本 README](README.md) 为准。

#### 4.1 通用对话框（文件 / 颜色 / 字体）

`win32ui` 封装了 MFC 风格的通用对话框，调用 `.DoModal()` 后取结果：

```python
import tkinter as tk
import win32ui

def pick_file():
    dlg = win32ui.CreateFileDialog(1)        # 1=打开, 0=保存
    dlg.SetOFNTitle("选择一个文件")
    if dlg.DoModal() == 1:                   # 1 == IDOK
        path = dlg.GetPathName()
        print("选中：", path)

def pick_color():
    dlg = win32ui.CreateColorDialog()
    if dlg.DoModal() == 1:
        rgb = dlg.GetColor()                 # 0xBBGGRR
        print("颜色：", hex(rgb))

root = tk.Tk()
tk.Button(root, text="打开文件", command=pick_file).pack(padx=10, pady=10)
tk.Button(root, text="选择颜色", command=pick_color).pack(padx=10, pady=10)
root.mainloop()
```

- `win32ui.CreateFileDialog` / `CreateColorDialog` / `CreateFontDialog` 均已验证存在。
- `DoModal()` 返回 `1` 表示用户点了“确定”；`GetPathName()` / `GetColor()` 取结果。
- 这些是**模态**对话框，会阻塞当前线程直到用户关闭——对 tkinter 主线程来说完全正常
  （tkinter 自己的 `tkinter.filedialog` 也是阻塞的）。

#### 4.2 系统消息框

```python
import win32gui, win32con

win32gui.MessageBox(
    0,                          # 父窗口 HWND，0=桌面
    "操作已完成。",
    "提示",
    win32con.MB_OK | win32con.MB_ICONINFORMATION)
```

风格常量（`MB_*`）见 `win32con`；返回值（`IDOK`/`IDCANCEL` 等）也来自 `win32con`。
需要把消息框挂到某个 tkinter 窗口下时，传该窗口的 `winfo_id()` 即可。

#### 4.3 通知区（系统托盘）图标

托盘需要一个**隐藏的消息窗口**来接收回调。下面的骨架用 `win32gui` 注册一个窗口类并创建
隐藏窗口，再用 `Shell_NotifyIcon` 添加图标：

```python
import tkinter as tk
import win32api, win32con, win32gui

## 1) 注册一个最小隐藏窗口类
wc = win32gui.WNDCLASS()
wc.hInstance = win32api.GetModuleHandle(None)
wc.lpszClassName = "TrayIconHost"
wc.lpfnWndProc = {win32con.WM_DESTROY: lambda *a: None}
wc.style = win32con.CS_VREDRAW | win32con.CS_HREDRAW
atom = win32gui.RegisterClass(wc)

## 2) 创建隐藏窗口
hwnd = win32gui.CreateWindow(
    atom, "tray", 0, 0, 0, 0, 0, 0, 0, win32api.GetModuleHandle(None), None)

## 3) 准备图标（这里用 tkinter 自带或自绘一个 .ico 的 HICON）
hicon = win32gui.LoadIcon(0, win32con.IDI_APPLICATION)

## 4) 添加托盘图标
nid = (hwnd, 0, win32gui.NIF_ICON | win32gui.NIF_MESSAGE | win32gui.NIF_TIP,
       win32con.WM_USER + 20, hicon, "我的应用")
win32gui.Shell_NotifyIcon(win32gui.NIM_ADD, nid)

## tkinter 主窗口照常运行；退出前 NIM_DELETE 移除图标
root = tk.Tk()
root.mainloop()
win32gui.Shell_NotifyIcon(win32gui.NIM_DELETE, nid)
```

- `Shell_NotifyIcon` 经实测存在于 `win32gui`（[02-modules/win32gui.md](02-modules/win32gui.md)）。
- 单击/右键菜单需要在 `lpfnWndProc` 里处理 `WM_USER+20` 消息（`win32gui.NIM_MODIFY` 更新）。
- `shell.md`（[02-modules/shell.md](02-modules/shell.md)）有更多
  `shell32` 能力（如文件夹选择 `SHBrowseForFolder`）。

#### 4.4 COM 自动化：用 tkinter 按钮驱动其它程序

`win32com.client.Dispatch` 直接创建/连接已注册 COM 组件，最典型的是驱动 Office：

```python
import tkinter as tk
import win32com.client

def open_excel():
    xl = win32com.client.Dispatch("Excel.Application")
    xl.Visible = True
    wb = xl.Workbooks.Add()
    ws = wb.Worksheets(1)
    ws.Cells(1, 1).Value = "来自 tkinter 按钮的一行"
    ws.Cells(2, 1).Value = "第二个单元格"

root = tk.Tk()
tk.Button(root, text="启动 Excel 并写数据", command=open_excel).pack(padx=20, pady=20)
root.mainloop()
```

- `Dispatch("ProgID")` 启动/连接；`GetActiveObject("Excel.Application")` 可连接已运行实例。
- COM 基础见 [02-modules/pythoncom.md](02-modules/pythoncom.md)。
- **线程注意**：COM 默认 STA。在后台线程用 COM 前先
  `pythoncom.CoInitializeEx(pythoncom.COINIT_APARTMENTTHREADED)`；操作结果用 `root.after(0, ...)`
  或 `queue` 送回主线程更新 tkinter UI。

---

### 5. 进阶：嵌入 ActiveX / WebBrowser

把网页或 OCX 控件（如 IE WebBrowser `{8856F961-340A-11D0-A96B-00C04FD705A2}`）放进 tkinter：

```python
import win32ui, win32con
## 注意：CreateControl 的父窗口必须是 win32ui 的 PyCWnd，不能传裸 HWND
wb = win32ui.CreateControl(
    "{8856F961-340A-11D0-A96B-00C04FD705A2}",   # WebBrowser CLSID
    "WebBrowser",
    win32con.WS_CHILD | win32con.WS_VISIBLE,
    (0, 0, 480, 360),
    pycwnd_host,                                # 必须是 PyCWnd
    1001)
```

获取 `pycwnd_host` 的稳妥办法：用 `win32ui` 自建一个承载窗口，再用
`win32gui.SetParent(pycwnd_host.GetSafeHwnd(), frame.winfo_id())` 把它嵌进 tkinter Frame；
或直接用现代替代方案（WebView2 / cef）承载网页内容。ActiveX 接口细节见
[02-modules/axcontrol.md](02-modules/axcontrol.md)。

---

### 6. DPI 与视觉样式

1. **DPI 感知**：进程启动早期（import tkinter 之前）设置
   `ctypes.windll.shcore.SetProcessDpiAwareness(1)`（与
   [`../../examples/pygubu-designer/run.py`](../../examples/pygubu-designer/run.py) 一致）。
2. **comctl32 v6 主题**：TreeView/ListView/Button 等要渲染成现代风格，进程需带
   `Microsoft.Windows.Common-Controls` v6 的 manifest（PyInstaller 打包时配
   `manifest`；或直接给 python 解释器配 manifest）。缺它会回退成经典 9x 风格。
3. **字体**：原生控件默认用系统字体，与 tkinter ttk 主题可能不一致，可用
   `win32gui.SendMessage(edit, win32con.WM_SETFONT, font_handle, 1)` 统一。

---

### 7. 必读坑位

- **平台守卫**：`win32gui`/`win32ui` 只在 Windows 可用，代码入口加 `if sys.platform != "win32": return`。
- **先 `update()` 再拿 HWND**：未实现的窗口 `winfo_id()` 返回 0 / NULL，创建子控件必失败。
- **HWND 生命周期**：原生子控件随父 tkinter 窗口销毁而销毁；主窗口销毁后不要再操作其 HWND。
- **缩放**：父 Frame 变化时要 `win32gui.MoveWindow` 同步子控件，否则会“钉”在原位。
- **线程**：tkinter 与 COM 都不是线程安全的。后台任务用 `threading` + `root.after(0, cb)` 或
  `queue.Queue` 把结果送回主线程；COM 线程需 `pythoncom.CoInitializeEx(COINIT_APARTMENTTHREADED)`。
- **不要子类化 tkinter 自己的顶层窗口**：容易破坏 Tcl/Tk 的内部消息循环；要子类化就子类化
  **你自己用 `CreateWindowEx` 创建的控件**。

> 所有示例均在 Python 3.13 + pywin32（本机已装）下实测可创建/嵌入。常量名（`WS_CHILD` 等）
> 来自 `win32con`，函数签名见 [本 README](README.md) 上部索引与各 `0x-*` 子目录。

---

## 文档路由（本目录：6771 页离线文档全集）

| 需要查 | 打开 |
|--------|------|
| 覆盖来源、目录结构、检索指引 | `README.md` |
| 某函数/API（如 `win32api.MessageBox`） | `02-modules/<模块名>.md` |
| 某对象的方法/属性 | `03-objects/objects-<字母>.md` |
| 某常量分组 | `04-constants/constants-<模块>.md` |
| 可运行官方示例全文 | `01-repo-docs/demos__*.md` |
| 专题/教程/杂项 | `05-overviews/` |
| 指定来源页（GitHub/PyPI/官方站/GitCode） | `00-sources/` |
| 在 tkinter 中拼装原生 UI 的实战指南 | 本技能「实战指南」章节 |

> 全部文档已纯文本化、无"请访问某网址"占位，离线可直接检索。
