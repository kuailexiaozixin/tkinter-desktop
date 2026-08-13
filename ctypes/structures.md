# 必须手动定义的 ctypes 结构体

> **wintypes 已导出**：`RECT`、`MSG`、`POINT`、`SIZE`、`HWND`、`HANDLE`/`HICON`、`WPARAM`/`LPARAM`、`UINT`、`BOOL`、`DWORD`、`ATOM`、`HINSTANCE`、`LPCWSTR` 等——可直接用 `wintypes.RECT` 等，无需手动定义。
> **以下结构体 wintypes 不导出，必须手动 `ctypes.Structure` 定义**：`WNDCLASSW`、`WNDCLASSEXW`、`PAINTSTRUCT`。
> **缺失的句柄/类型**：`HCURSOR`、`LRESULT`、`LPSECURITY_ATTRIBUTES` 也未导出，前者用 `wintypes.HANDLE` 替代，后两者用 `ctypes.c_int64` / `wintypes.LPVOID` 替代（见 `common-apis.md`）。

## WNDCLASSW

```python
class WNDCLASSW(ctypes.Structure):
    _fields_ = [
        ("style", wintypes.UINT),
        ("lpfnWndProc", WNDPROC),          # 回调类型，见下方
        ("cbClsExtra", ctypes.c_int),
        ("cbWndExtra", ctypes.c_int),
        ("hInstance", wintypes.HINSTANCE),
        ("hIcon", wintypes.HANDLE),        # wintypes.HICON 已导出（=HANDLE 别名），用 HANDLE 亦可
        ("hCursor", wintypes.HANDLE),      # wintypes 确实无 HCURSOR，用 HANDLE 替代
        ("hbrBackground", wintypes.HBRUSH),
        ("lpszMenuName", wintypes.LPCWSTR),
        ("lpszClassName", wintypes.LPCWSTR),
    ]
```

## WNDCLASSEXW

```python
class WNDCLASSEXW(ctypes.Structure):
    _fields_ = [
        ("cbSize", wintypes.UINT),
        ("style", wintypes.UINT),
        ("lpfnWndProc", WNDPROC),
        ("cbClsExtra", ctypes.c_int),
        ("cbWndExtra", ctypes.c_int),
        ("hInstance", wintypes.HINSTANCE),
        ("hIcon", wintypes.HANDLE),
        ("hCursor", wintypes.HANDLE),
        ("hbrBackground", wintypes.HBRUSH),
        ("lpszMenuName", wintypes.LPCWSTR),
        ("lpszClassName", wintypes.LPCWSTR),
        ("hIconSm", wintypes.HANDLE),      # wintypes.HICON 已导出，用 HANDLE 亦可
    ]
```

## MSG

```python
class POINT(ctypes.Structure):
    _fields_ = [
        ("x", wintypes.LONG),
        ("y", wintypes.LONG),
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

## PAINTSTRUCT

```python
class PAINTSTRUCT(ctypes.Structure):
    _fields_ = [
        ("hdc", wintypes.HDC),
        ("fErase", wintypes.BOOL),
        ("rcPaint", wintypes.RECT),
        ("fRestore", wintypes.BOOL),
        ("fIncUpdate", wintypes.BOOL),
        ("rgbReserved", wintypes.BYTE * 32),
    ]
```

## RECT

```python
class RECT(ctypes.Structure):
    _fields_ = [
        ("left", wintypes.LONG),
        ("top", wintypes.LONG),
        ("right", wintypes.LONG),
        ("bottom", wintypes.LONG),
    ]
```

## WNDPROC 回调类型

```python
# 必须先定义再用于结构体
WNDPROC = ctypes.WINFUNCTYPE(
    ctypes.c_int64,       # LRESULT
    wintypes.HWND,        # hWnd
    wintypes.UINT,        # uMsg
    wintypes.WPARAM,      # wParam
    wintypes.LPARAM       # lParam
)
```

## 关键提醒

1. **`wintypes` 不导出的结构体**：`WNDCLASSW`、`WNDCLASSEXW`、`PAINTSTRUCT`（必须手动 `ctypes.Structure`）。
   注意：`RECT` / `MSG` / `POINT` / `SIZE` **已在 wintypes 中导出**，可直接用 `wintypes.RECT`、`wintypes.MSG` 等，无需手动定义；`HICON` 也已导出（=`HANDLE` 别名）。真正缺失的句柄/类型是 `HCURSOR` 与 `LRESULT`。
2. **使用替代**：
   - `HCURSOR` → `wintypes.HANDLE`（HICON 已导出，可直接用 `wintypes.HICON`）
   - `LRESULT` → `ctypes.c_int64`
3. **回调类型必须先定义**：`WNDPROC` 必须在 `WNDCLASSW` 类定义**之前**创建
4. **保持引用**：`WndProc = WNDPROC(wnd_proc)` 必须赋值给全局变量，防止 GC
