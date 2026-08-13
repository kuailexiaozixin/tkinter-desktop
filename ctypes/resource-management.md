# 句柄生命周期与泄漏排查

## 核心原则

Windows 句柄（HWND、HDC、HMENU、HICON、HPEN、HBRUSH、HFILE 等）是操作系统资源。
Python 的垃圾回收器无法感知这些句柄。每个创建/获取的句柄都必须显式释放。

## 配对规则

| 获取函数 | 释放函数 | 资源类型 |
|---------|---------|---------|
| `CreateWindowEx` | `DestroyWindow` | 窗口 |
| `CreateMenu` | `DestroyMenu` | 菜单 |
| `CreatePopupMenu` | `DestroyMenu` | 弹出菜单 |
| `CreateDC` | `DeleteDC` | 设备上下文 |
| `GetDC` | `ReleaseDC` | 设备上下文 |
| `CreatePen` | `DeleteObject` | GDI 对象 |
| `CreateSolidBrush` | `DeleteObject` | GDI 对象 |
| `CreateFontIndirect` | `DeleteObject` | GDI 对象 |
| `CreateBitmap` | `DeleteObject` | GDI 对象 |
| `CreateFile` | `CloseHandle` | 文件/设备 |
| `GlobalAlloc` | `GlobalFree` | 全局内存 |
| `GlobalLock` | `GlobalUnlock` | 全局内存 |
| `CreateIconIndirect` | `DestroyIcon` | 图标 |
| `CreateCursor` | `DestroyCursor` | 光标 |
| `SetTimer` | `KillTimer` | 定时器 |
| `CreateEvent` | `CloseHandle` | 事件对象 |
| `CreateMutex` | `CloseHandle` | 互斥体 |
| `CreateThread` | `CloseHandle` | 线程句柄 |

## Python 上下文管理器模板

```python
from contextlib import contextmanager

@contextmanager
def win32_handle(create_func, destroy_func, *args, **kwargs):
    """通用 Win32 句柄管理器"""
    handle = create_func(*args, **kwargs)
    try:
        yield handle
    finally:
        if handle:
            destroy_func(handle)

@contextmanager
def device_context(hwnd):
    """HDC 管理器"""
    hdc = user32.GetDC(hwnd)
    try:
        yield hdc
    finally:
        if hdc:
            user32.ReleaseDC(hwnd, hdc)

@contextmanager
def paint_dc(hwnd):
    """BeginPaint / EndPaint 管理器（仅在 WM_PAINT 中使用）"""
    ps = wintypes.PAINTSTRUCT()
    hdc = user32.BeginPaint(hwnd, ctypes.byref(ps))
    try:
        yield hdc, ps
    finally:
        user32.EndPaint(hwnd, ctypes.byref(ps))

@contextmanager
def gdi_object(hdc, create_func, *args, **kwargs):
    """GDI 对象选择进 DC 并在退出时恢复"""
    old_obj = gdi32.SelectObject(hdc, create_func(*args, **kwargs))
    try:
        yield old_obj
    finally:
        if old_obj:
            gdi32.SelectObject(hdc, old_obj)
        gdi32.DeleteObject(create_func(*args, **kwargs))

@contextmanager
def global_buffer(size):
    """GlobalAlloc 缓冲区"""
    hglob = kernel32.GlobalAlloc(0x0040, size)  # GHND = GMEM_MOVEABLE | GMEM_ZEROINIT
    try:
        ptr = kernel32.GlobalLock(hglob)
        if not ptr:
            raise OSError("GlobalLock failed")
        yield ctypes.string_at(ptr, size)
    finally:
        kernel32.GlobalUnlock(hglob)
        if hglob:
            kernel32.GlobalFree(hglob)
```

## 常见泄漏场景

### 场景 1：WM_PAINT 中 BeginPaint 未 EndPaint

```python
# 错误示范
def wnd_proc(hwnd, msg, wparam, lparam):
    if msg == WM_PAINT:
        ps = wintypes.PAINTSTRUCT()
        hdc = user32.BeginPaint(hwnd, ctypes.byref(ps))
        # ... 忘记 EndPaint
        return 0

# 正确
def wnd_proc(hwnd, msg, wparam, lparam):
    if msg == WM_PAINT:
        ps = wintypes.PAINTSTRUCT()
        hdc = user32.BeginPaint(hwnd, ctypes.byref(ps))
        try:
            # ... 绘制
            pass
        finally:
            user32.EndPaint(hwnd, ctypes.byref(ps))
        return 0
```

### 场景 2：CreateFile 后异常未 CloseHandle

```python
def read_file(path):
    h_file = kernel32.CreateFileW(path, 0x80000000, 1, None, 3, 0x80, None)
    if h_file == INVALID_HANDLE_VALUE:
        raise OSError("CreateFile failed")
    try:
        size = kernel32.GetFileSize(h_file, None)
        buf = ctypes.create_string_buffer(size)
        bytes_read = wintypes.DWORD(0)
        kernel32.ReadFile(h_file, buf, size, ctypes.byref(bytes_read), None)
        return buf.raw[:bytes_read.value]
    finally:
        kernel32.CloseHandle(h_file)
```

### 场景 3：GDI 对象泄漏

```python
# 每次循环都 CreatePen 但不 DeleteObject
def draw_loop(hdc):
    for color in colors:
        hpen = gdi32.CreatePen(PS_SOLID, 1, color)
        gdi32.SelectObject(hdc, hpen)
        # ... 绘制
        gdi32.DeleteObject(hpen)  # 必须释放
```

### 场景 4：窗口过程回调被 GC

```python
def wnd_proc(hwnd, msg, wparam, lparam):
    # ...

# 错误：WndProc 是局部变量，创建窗口后可能被回收
WndProc = WNDPROC(wnd_proc)  # 必须保持全局引用
```

## 排查工具

1. **GDI 对象计数**：Task Manager → Details → Select Columns → GDI Objects
2. **句柄计数**：Task Manager → Details → Select Columns → Handles
3. **Win32 API 错误检查**：调用后立即 `GetLastError()` 检查错误码
4. **泄漏检测**：使用 Windows Performance Toolkit 或 Visual Studio Diagnostic Tools

## 错误处理

```python
INVALID_HANDLE_VALUE = ctypes.c_void_p(-1).value
NULL = 0

def check_handle(handle, msg="Win32 call failed"):
    if not handle or handle == INVALID_HANDLE_VALUE:
        err = kernel32.GetLastError()
        raise OSError(f"{msg} (error code: {err})")
    return handle

def check_bool(result, msg="Win32 call failed"):
    if not result:
        err = kernel32.GetLastError()
        raise OSError(f"{msg} (error code: {err})")
    return result
```
