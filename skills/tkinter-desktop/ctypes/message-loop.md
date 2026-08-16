# 消息循环与窗口过程详解

## 消息循环

### 标准消息循环

```python
msg = wintypes.MSG()
while user32.GetMessageW(ctypes.byref(msg), None, 0, 0) > 0:
    user32.TranslateMessage(ctypes.byref(msg))
    user32.DispatchMessageW(ctypes.byref(msg))
user32.PostQuitMessage(0)
```

- `GetMessageW`：从线程消息队列获取消息，队列空时阻塞。返回 0 表示收到 `WM_QUIT`，返回 -1 表示错误。
- `TranslateMessage`：将虚拟键消息转换为字符消息（`WM_CHAR`）。
- `DispatchMessageW`：将消息分发给对应窗口的 `WndProc`。

### 带加速键的消息循环

```python
while user32.GetMessageW(ctypes.byref(msg), None, 0, 0) > 0:
    # 先尝试加速键翻译
    if not user32.TranslateAcceleratorW(hwnd, h_accel, ctypes.byref(msg)):
        user32.TranslateMessage(ctypes.byref(msg))
        user32.DispatchMessageW(ctypes.byref(msg))
```

### 模型对话框消息循环

```python
# 局部消息循环，直到对话框关闭
while user32.GetMessageW(ctypes.byref(msg), None, 0, 0) > 0:
    if not user32.IsDialogMessageW(hwnd_dlg, ctypes.byref(msg)):
        user32.TranslateMessage(ctypes.byref(msg))
        user32.DispatchMessageW(ctypes.byref(msg))
```

## 窗口过程 (WndProc)

### 标准 WndProc 模板

```python
WNDPROC = ctypes.WINFUNCTYPE(ctypes.c_int64, wintypes.HWND, wintypes.UINT, wintypes.WPARAM, wintypes.LPARAM)

def wnd_proc(hwnd, msg, wparam, lparam):
    # 系统命令
    if msg == 0x0112:  # WM_SYSCOMMAND
        cmd = wparam & 0xFFF0
        if cmd == 0xF060:  # SC_CLOSE
            user32.DestroyWindow(hwnd)
            return 0

    # 窗口销毁
    if msg == 0x0002:   # WM_DESTROY
        user32.PostQuitMessage(0)
        return 0

    # 窗口绘制
    if msg == 0x000F:   # WM_PAINT
        ps = wintypes.PAINTSTRUCT()
        hdc = user32.BeginPaint(hwnd, ctypes.byref(ps))
        # ... 绘制逻辑
        user32.EndPaint(hwnd, ctypes.byref(ps))
        return 0

    # 窗口大小改变
    if msg == 0x0005:   # WM_SIZE
        w = lparam & 0xFFFF
        h = (lparam >> 16) & 0xFFFF
        # ... 调整子窗口大小
        return 0

    # 命令（菜单、加速键、控件通知）
    if msg == 0x0111:   # WM_COMMAND
        cmd_id = wparam & 0xFFFF
        # ... 处理命令
        return 0

    # 默认处理
    return user32.DefWindowProcW(hwnd, msg, wparam, lparam)

WndProc = WNDPROC(wnd_proc)
```

### 窗口过程注意事项

1. **返回值类型**：`LRESULT` 在 64 位系统上是 `c_int64`。
2. **消息常量**：使用十六进制字面量（如 `0x0002`）避免 `windows.h` 依赖。
3. **wParam / lParam 解包**：
   - `WM_SIZE`：`lparam & 0xFFFF` = 宽，`(lparam >> 16) & 0xFFFF` = 高
   - `WM_COMMAND`：`wparam & 0xFFFF` = 控件/菜单 ID，`(wparam >> 16) & 0xFFFF` = 通知代码
4. **DefWindowProcW**：未处理的消息必须交回系统处理，否则窗口行为异常。

## 常用消息速查

| 消息 | 值 | 用途 |
|------|-----|------|
| `WM_CREATE` | 0x0001 | 窗口创建后，初始化子窗口 |
| `WM_DESTROY` | 0x0002 | 窗口正在销毁，退出消息循环 |
| `WM_MOVE` | 0x0003 | 窗口移动 |
| `WM_SIZE` | 0x0005 | 窗口大小改变 |
| `WM_ACTIVATE` | 0x0006 | 窗口激活/停用 |
| `WM_PAINT` | 0x000F | 窗口需要重绘 |
| `WM_CLOSE` | 0x0010 | 用户请求关闭窗口 |
| `WM_QUIT` | 0x0012 | 退出消息（不在 WndProc 中处理） |
| `WM_ERASEBKGND` | 0x0014 | 擦除背景，返回 1 阻止闪烁 |
| `WM_KEYDOWN` | 0x0100 | 虚拟键按下 |
| `WM_KEYUP` | 0x0101 | 虚拟键释放 |
| `WM_CHAR` | 0x0102 | 字符输入 |
| `WM_COMMAND` | 0x0111 | 菜单、加速键、控件通知 |
| `WM_SYSCOMMAND` | 0x0112 | 系统命令（最大化、最小化、关闭等） |
| `WM_TIMER` | 0x0113 | 定时器消息 |
| `WM_HSCROLL` | 0x0114 | 水平滚动条 |
| `WM_VSCROLL` | 0x0115 | 垂直滚动条 |
| `WM_INITMENU` | 0x0116 | 菜单即将显示 |
| `WM_INITMENUPOPUP` | 0x0117 | 弹出菜单即将显示 |
| `WM_MENUSELECT` | 0x011F | 用户选择菜单项 |
| `WM_NOTIFY` | 0x004E | 控件通知（richedit、listview 等） |
| `WM_CONTEXTMENU` | 0x007B | 右键上下文菜单 |
| `WM_CTLCOLORSTATIC` | 0x0138 | 自定义 STATIC 控件颜色 |

## 控件通知码

```python
# 常用控件通知码
EN_CHANGE = 0x0300      # EDIT/RICHEDIT 内容改变
EN_UPDATE = 0x0301      # EDIT/RICHEDIT 准备显示
EN_ERRSPACE = 0x0302    # EDIT/RICHEDIT 内存不足
EN_MAXTEXT = 0x0501     # 内容达到最大长度
EN_MSGFILTER = 0x0700   # 键盘/鼠标消息过滤
EN_SELCHANGE = 0x0702   # 选择改变
EN_REQUESTRESIZE = 0x0703  # 请求调整大小

# RichEdit 特有
EM_GETSEL = 0x00B0
EM_SETSEL = 0x00B1
EM_GETRECT = 0x00B2
EM_SETRECT = 0x00B3
EM_SETRECTNP = 0x00B4
EM_SCROLL = 0x00B5
EM_LINESCROLL = 0x00B6
EM_SCROLLCARET = 0x00B7
EM_GETMODIFY = 0x00B8
EM_SETMODIFY = 0x00B9
EM_GETLINECOUNT = 0x00BA
EM_LINEINDEX = 0x00BB
EM_SETHANDLE = 0x00BC
EM_GETHANDLE = 0x00BD
EM_GETTHUMB = 0x00BE
EM_LINELENGTH = 0x00C1
EM_REPLACESEL = 0x00C2
EM_GETLINE = 0x00C4
EM_LIMITTEXT = 0x00C5
EM_CANUNDO = 0x00C6
EM_UNDO = 0x00C7
EM_EMPTYUNDOBUFFER = 0x00CD
EM_SETREADONLY = 0x00D1
EM_GETSELTEXT = 0x00E0
EM_EXGETSEL = 0x00E4
EM_EXLIMITTEXT = 0x00E5
EM_EXLINEFROMCHAR = 0x00E6
EM_SETMARGINS = 0x00D3
EM_GETMARGINS = 0x00D4
EM_SETWORDBREAKPROC = 0x00D6
EM_GETWORDBREAKPROC = 0x00D7
EM_SETPASSWORDCHAR = 0x00CC
EM_GETPASSWORDCHAR = 0x00D2
EM_SETTABSTOPS = 0x00CB
```
