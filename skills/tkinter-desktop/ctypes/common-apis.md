# 高频 Win32 API 签名速查

## 使用前必读

1. **`wintypes` 不导出以下类型**，必须手动用 `ctypes` 定义或替代：
   - `WNDCLASSW`、`WNDCLASSEXW`、`PAINTSTRUCT` → 必须手动 `ctypes.Structure` 定义，见 `structures.md`
   - 注意：`RECT` / `MSG` / `POINT` / `SIZE` **已在 wintypes 中导出**，可直接用 `wintypes.RECT` 等，无需手动定义
   - `HCURSOR` → 用 `wintypes.HANDLE` 替代（`HICON` 已导出，可直接用 `wintypes.HICON`）
   - `LRESULT` → 用 `ctypes.c_int64` 替代
2. **GDI 函数属于 gdi32.dll**，不是 user32.dll
3. **所有回调函数必须声明 argtypes/restype**，否则 64 位系统会溢出

## kernel32.dll

```python
kernel32 = windll.kernel32

# 内存管理
kernel32.GlobalAlloc.argtypes = [wintypes.UINT, ctypes.c_size_t]
kernel32.GlobalAlloc.restype = wintypes.HGLOBAL
kernel32.GlobalFree.argtypes = [wintypes.HGLOBAL]
kernel32.GlobalFree.restype = wintypes.HGLOBAL
kernel32.GlobalLock.argtypes = [wintypes.HGLOBAL]
kernel32.GlobalLock.restype = wintypes.LPVOID
kernel32.GlobalUnlock.argtypes = [wintypes.HGLOBAL]

# 模块与实例
kernel32.GetModuleHandleW.argtypes = [wintypes.LPCWSTR]
kernel32.GetModuleHandleW.restype = wintypes.HINSTANCE
kernel32.GetModuleFileNameW.argtypes = [wintypes.HINSTANCE, wintypes.LPWSTR, wintypes.DWORD]
kernel32.GetModuleFileNameW.restype = wintypes.DWORD

# 文件 I/O
kernel32.CreateFileW.argtypes = [
    wintypes.LPCWSTR, wintypes.DWORD, wintypes.DWORD,
    wintypes.LPVOID, wintypes.DWORD, wintypes.DWORD, wintypes.HANDLE
]
kernel32.CreateFileW.restype = wintypes.HANDLE
kernel32.ReadFile.argtypes = [
    wintypes.HANDLE, wintypes.LPVOID, wintypes.DWORD,
    ctypes.POINTER(wintypes.DWORD), wintypes.LPVOID
]
kernel32.ReadFile.restype = wintypes.BOOL
kernel32.WriteFile.argtypes = [
    wintypes.HANDLE, wintypes.LPCVOID, wintypes.DWORD,
    ctypes.POINTER(wintypes.DWORD), wintypes.LPVOID
]
kernel32.WriteFile.restype = wintypes.BOOL
kernel32.GetFileSize.argtypes = [wintypes.HANDLE, ctypes.POINTER(wintypes.DWORD)]
kernel32.GetFileSize.restype = wintypes.DWORD
kernel32.CloseHandle.argtypes = [wintypes.HANDLE]
kernel32.CloseHandle.restype = wintypes.BOOL

# 系统信息
kernel32.GetSystemMetrics.argtypes = [wintypes.INT]
kernel32.GetSystemMetrics.restype = wintypes.INT
kernel32.GetTickCount64.argtypes = []
kernel32.GetTickCount64.restype = wintypes.ULONGLONG
kernel32.GetLastError.argtypes = []
kernel32.GetLastError.restype = wintypes.DWORD

# 事件与同步
kernel32.CreateEventW.argtypes = [
    wintypes.LPSECURITY_ATTRIBUTES, wintypes.BOOL, wintypes.BOOL, wintypes.LPCWSTR
]
kernel32.CreateEventW.restype = wintypes.HANDLE
kernel32.SetEvent.argtypes = [wintypes.HANDLE]
kernel32.SetEvent.restype = wintypes.BOOL
kernel32.ResetEvent.argtypes = [wintypes.HANDLE]
kernel32.ResetEvent.restype = wintypes.BOOL
kernel32.WaitForSingleObject.argtypes = [wintypes.HANDLE, wintypes.DWORD]
kernel32.WaitForSingleObject.restype = wintypes.DWORD
```

## user32.dll

```python
user32 = windll.user32

# 窗口类
# 注意：WNDCLASSEXW 需手动定义，见 structures.md
user32.RegisterClassExW.argtypes = [ctypes.POINTER(WNDCLASSEXW)]
user32.RegisterClassExW.restype = wintypes.ATOM
user32.RegisterClassW.argtypes = [ctypes.POINTER(WNDCLASSW)]
user32.RegisterClassW.restype = wintypes.ATOM
user32.UnregisterClassW.argtypes = [wintypes.LPCWSTR, wintypes.HINSTANCE]
user32.UnregisterClassW.restype = wintypes.BOOL

# 窗口创建与销毁
user32.CreateWindowExW.argtypes = [
    wintypes.DWORD, wintypes.LPCWSTR, wintypes.LPCWSTR,
    wintypes.DWORD, wintypes.INT, wintypes.INT, wintypes.INT, wintypes.INT,
    wintypes.HWND, wintypes.HMENU, wintypes.HINSTANCE, wintypes.LPVOID
]
user32.CreateWindowExW.restype = wintypes.HWND
user32.DestroyWindow.argtypes = [wintypes.HWND]
user32.DestroyWindow.restype = wintypes.BOOL
user32.ShowWindow.argtypes = [wintypes.HWND, wintypes.INT]
user32.ShowWindow.restype = wintypes.BOOL
user32.UpdateWindow.argtypes = [wintypes.HWND]
user32.UpdateWindow.restype = wintypes.BOOL

# 消息循环
user32.GetMessageW.argtypes = [
    ctypes.POINTER(wintypes.MSG), wintypes.HWND, wintypes.UINT, wintypes.UINT
]
user32.GetMessageW.restype = wintypes.BOOL
user32.TranslateMessage.argtypes = [ctypes.POINTER(wintypes.MSG)]
user32.TranslateMessage.restype = wintypes.BOOL
user32.DispatchMessageW.argtypes = [ctypes.POINTER(wintypes.MSG)]
user32.DispatchMessageW.restype = ctypes.c_int64  # LRESULT
user32.PostQuitMessage.argtypes = [wintypes.INT]
user32.PostMessageW.argtypes = [wintypes.HWND, wintypes.UINT, wintypes.WPARAM, wintypes.LPARAM]
user32.PostMessageW.restype = wintypes.BOOL
user32.SendMessageW.argtypes = [wintypes.HWND, wintypes.UINT, wintypes.WPARAM, wintypes.LPARAM]
user32.SendMessageW.restype = ctypes.c_int64  # LRESULT

# 默认窗口过程
user32.DefWindowProcW.argtypes = [
    wintypes.HWND, wintypes.UINT, wintypes.WPARAM, wintypes.LPARAM
]
user32.DefWindowProcW.restype = ctypes.c_int64  # LRESULT

# 设备上下文
user32.BeginPaint.argtypes = [wintypes.HWND, ctypes.POINTER(wintypes.PAINTSTRUCT)]
user32.BeginPaint.restype = wintypes.HDC
user32.EndPaint.argtypes = [wintypes.HWND, ctypes.POINTER(wintypes.PAINTSTRUCT)]
user32.EndPaint.restype = wintypes.BOOL
user32.GetDC.argtypes = [wintypes.HWND]
user32.GetDC.restype = wintypes.HDC
user32.ReleaseDC.argtypes = [wintypes.HWND, wintypes.HDC]
user32.ReleaseDC.restype = wintypes.INT

# 菜单
user32.CreateMenu.argtypes = []
user32.CreateMenu.restype = wintypes.HMENU
user32.CreatePopupMenu.argtypes = []
user32.CreatePopupMenu.restype = wintypes.HMENU
user32.AppendMenuW.argtypes = [wintypes.HMENU, wintypes.UINT, wintypes.UINT_PTR, wintypes.LPCWSTR]
user32.AppendMenuW.restype = wintypes.BOOL
user32.SetMenu.argtypes = [wintypes.HWND, wintypes.HMENU]
user32.SetMenu.restype = wintypes.BOOL
user32.GetSystemMenu.argtypes = [wintypes.HWND, wintypes.BOOL]
user32.GetSystemMenu.restype = wintypes.HMENU
user32.DrawMenuBar.argtypes = [wintypes.HWND]
user32.DrawMenuBar.restype = wintypes.BOOL

# 光标
user32.LoadCursorW.argtypes = [wintypes.HINSTANCE, wintypes.LPCWSTR]
user32.LoadCursorW.restype = wintypes.HANDLE  # wintypes 无 HCURSOR，用 HANDLE 替代

# 通用对话框（comdlg32.dll）
comdlg32 = windll.comdlg32
comdlg32.GetOpenFileNameW.argtypes = [ctypes.POINTER(OPENFILENAMEW)]
comdlg32.GetOpenFileNameW.restype = wintypes.BOOL
comdlg32.GetSaveFileNameW.argtypes = [ctypes.POINTER(OPENFILENAMEW)]
comdlg32.GetSaveFileNameW.restype = wintypes.BOOL
comdlg32.ChooseFontW.argtypes = [ctypes.POINTER(CHOOSEFONTW)]
comdlg32.ChooseFontW.restype = wintypes.BOOL
```

## gdi32.dll

```python
gdi32 = windll.gdi32

# 绘图对象
gdi32.CreatePen.argtypes = [wintypes.INT, wintypes.INT, wintypes.COLORREF]
gdi32.CreatePen.restype = wintypes.HPEN
gdi32.CreateSolidBrush.argtypes = [wintypes.COLORREF]
gdi32.CreateSolidBrush.restype = wintypes.HBRUSH
gdi32.SelectObject.argtypes = [wintypes.HDC, wintypes.HGDIOBJ]
gdi32.SelectObject.restype = wintypes.HGDIOBJ
gdi32.DeleteObject.argtypes = [wintypes.HGDIOBJ]
gdi32.DeleteObject.restype = wintypes.BOOL

# 文本输出
gdi32.TextOutW.argtypes = [wintypes.HDC, wintypes.INT, wintypes.INT, wintypes.LPCWSTR, wintypes.INT]
gdi32.TextOutW.restype = wintypes.BOOL
gdi32.SetTextColor.argtypes = [wintypes.HDC, wintypes.COLORREF]
gdi32.SetTextColor.restype = wintypes.COLORREF
gdi32.SetBkMode.argtypes = [wintypes.HDC, wintypes.INT]
gdi32.SetBkMode.restype = wintypes.INT
gdi32.SetBkColor.argtypes = [wintypes.HDC, wintypes.COLORREF]
gdi32.SetBkColor.restype = wintypes.COLORREF

# 位图传输
gdi32.BitBlt.argtypes = [
    wintypes.HDC, wintypes.INT, wintypes.INT, wintypes.INT, wintypes.INT,
    wintypes.HDC, wintypes.INT, wintypes.INT, wintypes.DWORD
]
gdi32.BitBlt.restype = wintypes.BOOL
```

## 通用对话框结构体

### OPENFILENAMEW

```python
class OPENFILENAMEW(ctypes.Structure):
    _fields_ = [
        ("lStructSize", wintypes.DWORD),
        ("hwndOwner", wintypes.HWND),
        ("hInstance", wintypes.HINSTANCE),
        ("lpstrFilter", wintypes.LPCWSTR),
        ("lpstrCustomFilter", wintypes.LPWSTR),
        ("nMaxCustFilter", wintypes.DWORD),
        ("nFilterIndex", wintypes.DWORD),
        ("lpstrFile", wintypes.LPWSTR),
        ("nMaxFile", wintypes.DWORD),
        ("lpstrFileTitle", wintypes.LPWSTR),
        ("nMaxFileTitle", wintypes.DWORD),
        ("lpstrInitialDir", wintypes.LPCWSTR),
        ("lpstrTitle", wintypes.LPCWSTR),
        ("Flags", wintypes.DWORD),
        ("nFileOffset", wintypes.WORD),
        ("nFileExtension", wintypes.WORD),
        ("lpstrDefExt", wintypes.LPCWSTR),
        ("lCustData", wintypes.LPARAM),
        ("lpfnHook", wintypes.LPVOID),
        ("lpTemplateName", wintypes.LPCWSTR),
        ("pvReserved", wintypes.LPVOID),
        ("dwReserved", wintypes.DWORD),
        ("FlagsEx", wintypes.DWORD),
    ]

def show_open_dialog(hwnd_owner=None):
    buf = (wintypes.WCHAR * 260)()
    ofn = OPENFILENAMEW()
    ofn.lStructSize = ctypes.sizeof(OPENFILENAMEW)
    ofn.hwndOwner = hwnd_owner
    ofn.lpstrFilter = "所有文件\0*.*\0文本文件\0*.txt\0\0"
    ofn.lpstrFile = ctypes.cast(buf, wintypes.LPWSTR)
    ofn.nMaxFile = 260
    ofn.Flags = 0x00001000  # OFN_FILEMUSTEXIST

    if comdlg32.GetOpenFileNameW(ctypes.byref(ofn)):
        return buf.value
    return None
```

## 常量速查

```python
# 窗口样式
WS_OVERLAPPEDWINDOW = 0x00CF0000
WS_POPUP = 0x80000000
WS_CHILD = 0x40000000
WS_VISIBLE = 0x10000000
WS_BORDER = 0x00800000
WS_CAPTION = 0x00C00000
WS_SYSMENU = 0x00080000
WS_THICKFRAME = 0x00040000
WS_MINIMIZEBOX = 0x00020000
WS_MAXIMIZEBOX = 0x00010000
WS_VSCROLL = 0x00200000
WS_HSCROLL = 0x00100000
WS_TABSTOP = 0x00010000

# 消息
WM_NULL = 0x0000
WM_CREATE = 0x0001
WM_DESTROY = 0x0002
WM_MOVE = 0x0003
WM_SIZE = 0x0005
WM_ACTIVATE = 0x0006
WM_PAINT = 0x000F
WM_CLOSE = 0x0010
WM_QUIT = 0x0012
WM_ERASEBKGND = 0x0014
WM_KEYDOWN = 0x0100
WM_KEYUP = 0x0101
WM_CHAR = 0x0102
WM_COMMAND = 0x0111
WM_SYSCOMMAND = 0x0112
WM_TIMER = 0x0113
WM_HSCROLL = 0x0114
WM_VSCROLL = 0x0115
WM_INITMENU = 0x0116
WM_INITMENUPOPUP = 0x0117
WM_NOTIFY = 0x004E
WM_CONTEXTMENU = 0x007B

# 系统命令
SC_CLOSE = 0xF060
SC_MAXIMIZE = 0xF030
SC_MINIMIZE = 0xF020
SC_RESTORE = 0xF120
SC_SIZE = 0xF000
SC_MOVE = 0xF010

# 菜单标志
MF_STRING = 0x0000
MF_SEPARATOR = 0x0800
MF_CHECKED = 0x0008
MF_ENABLED = 0x0000
MF_DISABLED = 0x0002
MF_GRAYED = 0x0001

# 对话框标志
OFN_FILEMUSTEXIST = 0x00001000
OFN_OVERWRITEPROMPT = 0x00000002
OFN_PATHMUSTEXIST = 0x00000800
OFN_EXPLORER = 0x00080000

# 显示模式
SW_HIDE = 0
SW_SHOWNORMAL = 1
SW_SHOWMAXIMIZED = 3
SW_RESTORE = 9

# 虚拟键
VK_BACK = 0x08
VK_RETURN = 0x0D
VK_ESCAPE = 0x1B

# 通用控件类
WC_EDIT = "EDIT"
WC_BUTTON = "BUTTON"
WC_STATIC = "STATIC"
WC_RICHEDIT50W = "RICHEDIT50W"
```
