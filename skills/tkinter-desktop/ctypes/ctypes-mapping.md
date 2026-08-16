# ctypes 与 Win32 类型映射

## ⚠️ 重要说明

`ctypes.wintypes` **不导出**以下类型，必须手动定义或替代：

| 缺失类型 | 替代方案 | 参考 |
|---------|---------|------|
| `WNDCLASSW` | 手动 `ctypes.Structure` | `structures.md` |
| `WNDCLASSEXW` | 手动 `ctypes.Structure` | `structures.md` |
| `MSG` | 手动 `ctypes.Structure` | `structures.md` |
| `PAINTSTRUCT` | 手动 `ctypes.Structure` | `structures.md` |
| `RECT` | 手动 `ctypes.Structure` | `structures.md` |
| `HICON` | `wintypes.HANDLE` | - |
| `HCURSOR` | `wintypes.HANDLE` | - |
| `LRESULT` | `ctypes.c_int64` | - |

## 基础类型

| Win32 C 类型 | 含义 | ctypes 等价 | 说明 |
|-------------|------|------------|------|
| `BOOL` | 布尔整数 | `ctypes.c_int` / `wintypes.BOOL` | 非 0 为真 |
| `BYTE` | 8 位无符号 | `ctypes.c_ubyte` / `wintypes.BYTE` | |
| `WORD` | 16 位无符号 | `ctypes.c_uint16` / `wintypes.WORD` | |
| `DWORD` | 32 位无符号 | `ctypes.c_uint32` / `wintypes.DWORD` | |
| `LONG` | 32 位有符号 | `ctypes.c_int32` / `wintypes.LONG` | |
| `LONGLONG` | 64 位有符号 | `ctypes.c_int64` | |
| `ULONGLONG` | 64 位无符号 | `ctypes.c_uint64` | |
| `CHAR` | 8 位字符 | `ctypes.c_char` | |
| `WCHAR` | 16 位宽字符 | `ctypes.c_wchar` | |
| `UINT` | 无符号整数 | `ctypes.c_uint` / `wintypes.UINT` | |
| `INT` | 有符号整数 | `ctypes.c_int` / `wintypes.INT` | |
| `FLOAT` | 单精度浮点 | `ctypes.c_float` | |
| `DOUBLE` | 双精度浮点 | `ctypes.c_double` | |
| `HANDLE` | 通用句柄 | `wintypes.HANDLE` / `ctypes.c_void_p` | 实际为 `void*` |
| `HWND` | 窗口句柄 | `wintypes.HWND` | |
| `HINSTANCE` | 实例句柄 | `wintypes.HINSTANCE` | |
| `HMENU` | 菜单句柄 | `wintypes.HMENU` | |
| `HDC` | 设备上下文句柄 | `wintypes.HDC` | |
| `HFILE` | 文件句柄 | `wintypes.HFILE` | 旧式，推荐用 `HANDLE` |
| `HRESULT` | COM 结果码 | `wintypes.HRESULT` | |

## 指针与字符串

| Win32 C 类型 | 含义 | ctypes 等价 | 说明 |
|-------------|------|------------|------|
| `LPSTR` | ANSI 字符串指针 | `ctypes.c_char_p` / `wintypes.LPSTR` | |
| `LPCSTR` | const ANSI 字符串 | `wintypes.LPCSTR` | |
| `LPWSTR` | 宽字符串指针 | `wintypes.LPWSTR` | |
| `LPCWSTR` | const 宽字符串 | `wintypes.LPCWSTR` | Python `str` 可直接传递 |
| `LPVOID` | 无类型指针 | `ctypes.c_void_p` | |
| `PVOID` | 无类型指针 | `ctypes.c_void_p` | |
| `LPLONG` | LONG 指针 | `ctypes.POINTER(wintypes.LONG)` | 使用 `ctypes.byref()` |
| `LPDWORD` | DWORD 指针 | `ctypes.POINTER(wintypes.DWORD)` | 输出参数常用 |
| `LPBOOL` | BOOL 指针 | `ctypes.POINTER(wintypes.BOOL)` | |

## 回调函数

### WNDPROC（窗口过程）

```python
import ctypes
from ctypes import wintypes

# 必须先定义 WNDPROC，再定义 WNDCLASSW
WNDPROC = ctypes.WINFUNCTYPE(
    ctypes.c_int64,      # LRESULT
    wintypes.HWND,       # hWnd
    wintypes.UINT,       # uMsg
    wintypes.WPARAM,     # wParam
    wintypes.LPARAM      # lParam
)

def wnd_proc(hwnd, msg, wparam, lparam):
    # ... 处理消息
    return user32.DefWindowProcW(hwnd, msg, wparam, lparam)

# 必须保持引用，防止被 GC
WndProc = WNDPROC(wnd_proc)
wc = WNDCLASSW()
wc.lpfnWndProc = WndProc
```

### DialogProc（对话框过程）

```python
DLGPROC = ctypes.WINFUNCTYPE(
    ctypes.c_int64,      # INT_PTR
    wintypes.HWND,
    wintypes.UINT,
    wintypes.WPARAM,
    wintypes.LPARAM
)
```

## 结构体对齐

Win32 结构体默认使用 `#pragma pack(8)`。在 ctypes 中：

```python
class WNDCLASSW(ctypes.Structure):
    _fields_ = [
        ("style", wintypes.UINT),
        ("lpfnWndProc", WNDPROC),
        ("cbClsExtra", ctypes.c_int),
        ("cbWndExtra", ctypes.c_int),
        ("hInstance", wintypes.HINSTANCE),
        ("hIcon", wintypes.HANDLE),      # wintypes.HICON 已导出，用 HANDLE 等价
        ("hCursor", wintypes.HANDLE),    # wintypes 无 HCURSOR，用 HANDLE
        ("hbrBackground", wintypes.HBRUSH),
        ("lpszMenuName", wintypes.LPCWSTR),
        ("lpszClassName", wintypes.LPCWSTR),
    ]

class POINT(ctypes.Structure):
    _fields_ = [
        ("x", wintypes.LONG),
        ("y", wintypes.LONG),
    ]

class RECT(ctypes.Structure):
    _fields_ = [
        ("left", wintypes.LONG),
        ("top", wintypes.LONG),
        ("right", wintypes.LONG),
        ("bottom", wintypes.LONG),
    ]

class MSG(ctypes.Structure):
    _fields_ = [
        ("hwnd", wintypes.HWND),
        ("message", wintypes.UINT),
        ("wParam", wintypes.WPARAM),
        ("lParam", wintypes.LPARAM),
        ("time", wintypes.DWORD),
        ("pt", POINT),
    ]
```

## 函数签名声明

```python
user32 = windll.user32
kernel32 = windll.kernel32
gdi32 = windll.gdi32  # GDI 函数在 gdi32，不是 user32

# 声明函数签名
user32.MessageBoxW.argtypes = [
    wintypes.HWND,
    wintypes.LPCWSTR,
    wintypes.LPCWSTR,
    wintypes.UINT
]
user32.MessageBoxW.restype = wintypes.INT

user32.CreateWindowExW.argtypes = [
    wintypes.DWORD,      # dwExStyle
    wintypes.LPCWSTR,     # lpClassName
    wintypes.LPCWSTR,     # lpWindowName
    wintypes.DWORD,       # dwStyle
    wintypes.INT,         # x
    wintypes.INT,         # y
    wintypes.INT,         # nWidth
    wintypes.INT,         # nHeight
    wintypes.HWND,        # hWndParent
    wintypes.HMENU,       # hMenu
    wintypes.HINSTANCE,   # hInstance
    wintypes.LPVOID       # lpParam
]
user32.CreateWindowExW.restype = wintypes.HWND

user32.GetMessageW.argtypes = [
    ctypes.POINTER(wintypes.MSG), wintypes.HWND, wintypes.UINT, wintypes.UINT
]
user32.GetMessageW.restype = wintypes.BOOL

# DefWindowProcW 必须声明，否则 64 位 lparam 溢出
user32.DefWindowProcW.argtypes = [
    wintypes.HWND, wintypes.UINT, wintypes.WPARAM, wintypes.LPARAM
]
user32.DefWindowProcW.restype = ctypes.c_int64  # LRESULT

# GDI 函数在 gdi32
gdi32.CreateSolidBrush.argtypes = [wintypes.COLORREF]
gdi32.CreateSolidBrush.restype = wintypes.HBRUSH
gdi32.SetTextColor.argtypes = [wintypes.HDC, wintypes.COLORREF]
gdi32.SetTextColor.restype = wintypes.COLORREF
```

## 常见陷阱

1. **c_int64  vs  c_long**：64 位 Windows 上 `LRESULT` 是 64 位，用 `c_int64`。
2. **字符串编码**：Python `str` 传给 W 函数时 ctypes 自动转 UTF-16；传给 A 函数需 `encode('mbcs')`。
3. **结构体初始化**：`ctypes.byref(wc)` 传递指针，`ctypes.pointer(wc)` 创建指针对象。
4. **句柄空值**：Win32 句柄失败返回 `NULL` 或 `INVALID_HANDLE_VALUE`（`-1`），需检查：
   ```python
   INVALID_HANDLE_VALUE = ctypes.c_void_p(-1).value
   if handle == INVALID_HANDLE_VALUE:
       raise OSError("Failed")
   ```
5. **回调生命周期**：`WNDPROC`、`TIMERPROC` 等回调必须保持全局引用，否则被 GC 后崩溃。
6. **DLL 归属**：GDI 函数（`CreateSolidBrush`、`SetTextColor`、`SetBkMode` 等）属于 **gdi32.dll**，不是 user32。
