"""
纯 Win32 API 计算器——Python + ctypes，零第三方依赖

ctypes 调 Win32 的关键坑（本文件逐条示范正确写法）：

1. gdi32.CreateSolidBrush 属于 gdi32.dll，不是 user32
2. wintypes 不导出 WNDCLASSW / PAINTSTRUCT，需手动定义
3. wintypes 不导出 HCURSOR（HICON 已导出），用 wintypes.HANDLE 替代
4. wintypes 不导出 LRESULT，用 ctypes.c_int64 替代（64 位）
5. DefWindowProcW 必须声明 argtypes/restype，否则 64 位截断
6. IDC_ARROW 等是 MAKEINTRESOURCE 数值资源，**不能传字符串** "IDC_ARROW"
   —— 传字符串时 LoadCursorW 返回 NULL，窗口类光标为空
7. 给 WM_SETTEXT 传 ctypes.cast(c_wchar_p(s), c_void_p).value 会拿到
   **临时对象的地址**（use-after-free）；应直接用 SetWindowTextW
8. WNDPROC 回调里不能让 Python 异常逃逸，必须自己兜住
9. CreateWindowExW 传的是**窗口**尺寸，要用 AdjustWindowRect 由客户区反推
"""
import ctypes
from ctypes import wintypes, windll

user32 = windll.user32
kernel32 = windll.kernel32
gdi32 = windll.gdi32

# ─── 窗口 / 控件样式 ───
WS_OVERLAPPEDWINDOW = 0x00CF0000
WS_CHILD = 0x40000000
WS_VISIBLE = 0x10000000
WS_BORDER = 0x00800000
ES_READONLY = 0x0800
ES_RIGHT = 0x0002

# ─── 消息 ───
WM_CREATE = 0x0001
WM_DESTROY = 0x0002
WM_PAINT = 0x000F
WM_COMMAND = 0x0111

# ─── 资源 / 绘制常量 ───
IDC_ARROW = 32512          # MAKEINTRESOURCE 数值资源 ID，不是字符串！
COLOR_WINDOW = 5           # hbrBackground = COLOR_WINDOW + 1
TRANSPARENT = 1            # SetBkMode

# ─── 控件 ID ───
IDC_DISPLAY = 1000
IDC_BUTTON_0 = 1001
IDC_BUTTON_1 = 1002
IDC_BUTTON_2 = 1003
IDC_BUTTON_3 = 1004
IDC_BUTTON_4 = 1005
IDC_BUTTON_5 = 1006
IDC_BUTTON_6 = 1007
IDC_BUTTON_7 = 1008
IDC_BUTTON_8 = 1009
IDC_BUTTON_9 = 1010
IDC_BUTTON_ADD = 1011
IDC_BUTTON_SUB = 1012
IDC_BUTTON_MUL = 1013
IDC_BUTTON_DIV = 1014
IDC_BUTTON_EQ = 1015
IDC_BUTTON_CLR = 1016
IDC_BUTTON_DOT = 1017

# ─── 布局（客户区坐标）───
PAD = 10
DISPLAY_W, DISPLAY_H = 260, 40
BTN_W, BTN_H = 50, 30
STATUS_Y = 258            # 状态栏（WM_PAINT 绘制）顶部
STATUS_H = 25
CLIENT_W = 280
CLIENT_H = STATUS_Y + STATUS_H + PAD

# ─── 回调类型（必须先定义，结构体依赖它）───
WNDPROC = ctypes.WINFUNCTYPE(
    ctypes.c_int64,       # LRESULT
    wintypes.HWND,        # hWnd
    wintypes.UINT,        # uMsg
    wintypes.WPARAM,      # wParam
    wintypes.LPARAM       # lParam
)


# ─── 结构体（wintypes 不导出这些）───
class WNDCLASSW(ctypes.Structure):
    _fields_ = [
        ("style", wintypes.UINT),
        ("lpfnWndProc", WNDPROC),
        ("cbClsExtra", ctypes.c_int),
        ("cbWndExtra", ctypes.c_int),
        ("hInstance", wintypes.HINSTANCE),
        ("hIcon", wintypes.HANDLE),        # wintypes.HICON 已导出，用 HANDLE 等价
        ("hCursor", wintypes.HANDLE),      # wintypes 无 HCURSOR，用 HANDLE
        ("hbrBackground", wintypes.HBRUSH),
        ("lpszMenuName", wintypes.LPCWSTR),
        ("lpszClassName", wintypes.LPCWSTR),
    ]


class PAINTSTRUCT(ctypes.Structure):
    _fields_ = [
        ("hdc", wintypes.HDC),
        ("fErase", wintypes.BOOL),
        ("rcPaint", wintypes.RECT),
        ("fRestore", wintypes.BOOL),
        ("fIncUpdate", wintypes.BOOL),
        ("rgbReserved", ctypes.c_byte * 32),
    ]


# ─── 函数签名（不声明则 64 位句柄/返回值会被截断）───
user32.DefWindowProcW.argtypes = [wintypes.HWND, wintypes.UINT, wintypes.WPARAM, wintypes.LPARAM]
user32.DefWindowProcW.restype = ctypes.c_int64  # LRESULT

user32.CreateWindowExW.argtypes = [
    wintypes.DWORD, wintypes.LPCWSTR, wintypes.LPCWSTR,
    wintypes.DWORD, wintypes.INT, wintypes.INT, wintypes.INT, wintypes.INT,
    wintypes.HWND, wintypes.HMENU, wintypes.HINSTANCE, wintypes.LPVOID
]
user32.CreateWindowExW.restype = wintypes.HWND

user32.RegisterClassW.argtypes = [ctypes.POINTER(WNDCLASSW)]
user32.RegisterClassW.restype = wintypes.ATOM

user32.LoadCursorW.argtypes = [wintypes.HINSTANCE, wintypes.LPCWSTR]
user32.LoadCursorW.restype = wintypes.HANDLE  # HCURSOR = HANDLE

user32.SetWindowTextW.argtypes = [wintypes.HWND, wintypes.LPCWSTR]
user32.SetWindowTextW.restype = wintypes.BOOL

user32.AdjustWindowRect.argtypes = [ctypes.POINTER(wintypes.RECT), wintypes.DWORD, wintypes.BOOL]
user32.AdjustWindowRect.restype = wintypes.BOOL

user32.BeginPaint.argtypes = [wintypes.HWND, ctypes.POINTER(PAINTSTRUCT)]
user32.BeginPaint.restype = wintypes.HDC
user32.EndPaint.argtypes = [wintypes.HWND, ctypes.POINTER(PAINTSTRUCT)]
user32.EndPaint.restype = wintypes.BOOL
user32.FillRect.argtypes = [wintypes.HDC, ctypes.POINTER(wintypes.RECT), wintypes.HBRUSH]
user32.FillRect.restype = ctypes.c_int
user32.InvalidateRect.argtypes = [wintypes.HWND, ctypes.POINTER(wintypes.RECT), wintypes.BOOL]
user32.InvalidateRect.restype = wintypes.BOOL

# CreateSolidBrush / DeleteObject / TextOutW 在 gdi32，不在 user32
gdi32.CreateSolidBrush.argtypes = [wintypes.COLORREF]
gdi32.CreateSolidBrush.restype = wintypes.HBRUSH
gdi32.DeleteObject.argtypes = [wintypes.HGDIOBJ]
gdi32.DeleteObject.restype = wintypes.BOOL
gdi32.TextOutW.argtypes = [wintypes.HDC, ctypes.c_int, ctypes.c_int, wintypes.LPCWSTR, ctypes.c_int]
gdi32.TextOutW.restype = wintypes.BOOL
gdi32.SetBkMode.argtypes = [wintypes.HDC, ctypes.c_int]
gdi32.SetBkMode.restype = ctypes.c_int
gdi32.SetTextColor.argtypes = [wintypes.HDC, wintypes.COLORREF]
gdi32.SetTextColor.restype = wintypes.COLORREF


def RGB(r, g, b):
    return r | (g << 8) | (b << 16)


# ─── 全局状态 ───
h_display = None
current_input = "0"
prev_value = 0.0
operator = None
reset_next = False
WndProc = None            # 保持全局引用，防止回调被 GC


def set_display_text(hwnd_display, text):
    """安全设置文本。

    不要用 SendMessageW(WM_SETTEXT, 0, cast(c_wchar_p(s), c_void_p).value)：
    那个 c_wchar_p 是临时对象，取到 .value 后即可被回收，属于 use-after-free。
    SetWindowTextW 声明了 LPCWSTR，ctypes 会在调用期间保持缓冲区存活。
    """
    user32.SetWindowTextW(hwnd_display, text)


def to_float(text):
    """把显示串安全转成 float —— "."、"Error"、"" 都不能让它抛异常。"""
    try:
        return float(text)
    except (ValueError, TypeError):
        return 0.0


def fmt(value):
    """5.0 -> "5"；2.5 -> "2.5"；避免整数结果显示成 5.0。"""
    if value != value or value in (float("inf"), float("-inf")):
        return "Error"
    if float(value).is_integer() and abs(value) < 1e16:
        return str(int(value))
    return f"{value:.10g}"


def calculate():
    """执行挂起的运算，结果写回 current_input。"""
    global prev_value, operator, reset_next, current_input

    if current_input == "Error":
        return
    curr = to_float(current_input)
    try:
        if operator == "+":
            result = prev_value + curr
        elif operator == "-":
            result = prev_value - curr
        elif operator == "*":
            result = prev_value * curr
        elif operator == "/":
            if curr == 0:
                current_input = "Error"      # 除零应报错，不是静默返回 0
                operator = None
                reset_next = True
                return
            result = prev_value / curr
        else:
            result = curr
        current_input = fmt(result)
    except (ArithmeticError, ValueError):
        current_input = "Error"
    operator = None
    reset_next = True


def apply_operator(op):
    """按下 + - * / 时的统一处理（含中间结果刷新）。"""
    global prev_value, operator, reset_next

    if current_input == "Error":
        return
    if operator and not reset_next:
        calculate()
        set_display_text(h_display, current_input)   # 原实现漏了这行：连算不刷新
    prev_value = to_float(current_input)
    operator = op
    reset_next = True


def paint_status(hwnd):
    """WM_PAINT：用 GDI 在底部画一条状态栏，演示 gdi32 的正确用法。"""
    ps = PAINTSTRUCT()
    hdc = user32.BeginPaint(hwnd, ctypes.byref(ps))
    try:
        rect = wintypes.RECT(0, STATUS_Y, CLIENT_W, STATUS_Y + STATUS_H)
        brush = gdi32.CreateSolidBrush(RGB(240, 240, 240))   # gdi32，不是 user32
        try:
            user32.FillRect(hdc, ctypes.byref(rect), brush)
        finally:
            gdi32.DeleteObject(brush)                        # GDI 对象必须释放

        gdi32.SetBkMode(hdc, TRANSPARENT)
        gdi32.SetTextColor(hdc, RGB(70, 70, 70))
        pending = f"{fmt(prev_value)} {operator}" if operator else "就绪"
        text = f"状态: {pending}"
        gdi32.TextOutW(hdc, PAD, STATUS_Y + 5, text, len(text))
    finally:
        user32.EndPaint(hwnd, ctypes.byref(ps))


def refresh_status(hwnd):
    """只让状态栏区域失效，避免整窗重绘导致闪烁。"""
    rect = wintypes.RECT(0, STATUS_Y, CLIENT_W, STATUS_Y + STATUS_H)
    user32.InvalidateRect(hwnd, ctypes.byref(rect), True)


def on_command(hwnd, ctrl_id):
    """WM_COMMAND 分发。"""
    global current_input, prev_value, operator, reset_next

    if IDC_BUTTON_0 <= ctrl_id <= IDC_BUTTON_9:
        digit = str(ctrl_id - IDC_BUTTON_0)
        if reset_next or current_input in ("0", "Error"):
            current_input = digit
            reset_next = False
        else:
            current_input += digit
        set_display_text(h_display, current_input)

    elif ctrl_id == IDC_BUTTON_DOT:
        if reset_next or current_input == "Error":
            current_input = "0."
            reset_next = False
        elif "." not in current_input:
            current_input += "."
        set_display_text(h_display, current_input)

    elif ctrl_id == IDC_BUTTON_ADD:
        apply_operator("+")
        refresh_status(hwnd)
    elif ctrl_id == IDC_BUTTON_SUB:
        apply_operator("-")
        refresh_status(hwnd)
    elif ctrl_id == IDC_BUTTON_MUL:
        apply_operator("*")
        refresh_status(hwnd)
    elif ctrl_id == IDC_BUTTON_DIV:
        apply_operator("/")
        refresh_status(hwnd)

    elif ctrl_id == IDC_BUTTON_EQ:
        if operator:
            calculate()
            set_display_text(h_display, current_input)
            refresh_status(hwnd)

    elif ctrl_id == IDC_BUTTON_CLR:
        current_input = "0"
        prev_value = 0.0
        operator = None
        reset_next = False
        set_display_text(h_display, "0")
        refresh_status(hwnd)


def wnd_proc(hwnd, msg, wparam, lparam):
    """窗口过程。注意：Python 异常绝不能从 ctypes 回调里逃逸。"""
    global h_display

    try:
        if msg == WM_CREATE:
            h_display = user32.CreateWindowExW(
                0, "EDIT", "",
                WS_CHILD | WS_VISIBLE | WS_BORDER | ES_RIGHT | ES_READONLY,
                PAD, PAD, DISPLAY_W, DISPLAY_H,
                hwnd, IDC_DISPLAY, kernel32.GetModuleHandleW(None), None
            )
            if not h_display:
                return -1               # 让 CreateWindowExW 失败，而不是留个半成品窗口
            set_display_text(h_display, current_input)
            return 0

        if msg == WM_COMMAND:
            on_command(hwnd, wparam & 0xFFFF)   # 低 16 位 = 控件 ID
            return 0

        if msg == WM_PAINT:
            paint_status(hwnd)
            return 0

        if msg == WM_DESTROY:
            user32.PostQuitMessage(0)
            return 0

    except Exception:                    # 回调里兜住一切，否则进程行为不可预期
        import traceback
        traceback.print_exc()
        return 0

    return user32.DefWindowProcW(hwnd, msg, wparam, lparam)


def create_buttons(hwnd_parent):
    """创建计算器按钮。"""
    rows = [
        ("7", "8", "9", "/"),
        ("4", "5", "6", "*"),
        ("1", "2", "3", "-"),
        ("0", ".", "=", "+"),
    ]
    id_of = {
        "0": IDC_BUTTON_0, "1": IDC_BUTTON_1, "2": IDC_BUTTON_2, "3": IDC_BUTTON_3,
        "4": IDC_BUTTON_4, "5": IDC_BUTTON_5, "6": IDC_BUTTON_6, "7": IDC_BUTTON_7,
        "8": IDC_BUTTON_8, "9": IDC_BUTTON_9,
        "+": IDC_BUTTON_ADD, "-": IDC_BUTTON_SUB, "*": IDC_BUTTON_MUL,
        "/": IDC_BUTTON_DIV, "=": IDC_BUTTON_EQ, ".": IDC_BUTTON_DOT,
    }

    hinst = kernel32.GetModuleHandleW(None)
    top = 60
    for r, row in enumerate(rows):
        for c, label in enumerate(row):
            user32.CreateWindowExW(
                0, "BUTTON", label,
                WS_CHILD | WS_VISIBLE | WS_BORDER,
                PAD + c * (BTN_W + 10), top + r * (BTN_H + 10), BTN_W, BTN_H,
                hwnd_parent, id_of[label], hinst, None
            )
    # C 键单独一行，占两格宽
    user32.CreateWindowExW(
        0, "BUTTON", "C",
        WS_CHILD | WS_VISIBLE | WS_BORDER,
        PAD, top + len(rows) * (BTN_H + 10), BTN_W * 2 + 10, BTN_H,
        hwnd_parent, IDC_BUTTON_CLR, hinst, None
    )


def main():
    global WndProc

    hinst = kernel32.GetModuleHandleW(None)

    # ① 注册窗口类
    wc = WNDCLASSW()
    WndProc = WNDPROC(wnd_proc)        # 必须保持全局引用！
    wc.lpfnWndProc = WndProc
    wc.hInstance = hinst
    wc.lpszClassName = "PureWin32Calculator"
    wc.hbrBackground = COLOR_WINDOW + 1
    # IDC_ARROW 是数值资源，要 cast 成 LPCWSTR；传 "IDC_ARROW" 字符串会返回 NULL
    wc.hCursor = user32.LoadCursorW(None, ctypes.cast(IDC_ARROW, wintypes.LPCWSTR))
    if not wc.hCursor:
        raise OSError(f"LoadCursorW 失败: {ctypes.get_last_error()}")

    if not user32.RegisterClassW(ctypes.byref(wc)):
        raise OSError(f"RegisterClassW 失败: {ctypes.get_last_error()}")

    # ② 由客户区尺寸反推窗口尺寸（否则按钮会被边框和标题栏挤掉）
    rect = wintypes.RECT(0, 0, CLIENT_W, CLIENT_H)
    user32.AdjustWindowRect(ctypes.byref(rect), WS_OVERLAPPEDWINDOW, False)
    win_w = rect.right - rect.left
    win_h = rect.bottom - rect.top

    # ③ 创建主窗口
    hwnd = user32.CreateWindowExW(
        0, "PureWin32Calculator", "纯 Win32 计算器",
        WS_OVERLAPPEDWINDOW,
        100, 100, win_w, win_h,
        None, None, hinst, None
    )
    if not hwnd:
        raise OSError(f"CreateWindowExW 失败: {ctypes.get_last_error()}")

    create_buttons(hwnd)
    user32.ShowWindow(hwnd, 1)         # SW_SHOWNORMAL
    user32.UpdateWindow(hwnd)

    # ④ 消息循环（GetMessageW 出错返回 -1，必须区别于 0）
    msg = wintypes.MSG()
    while True:
        ret = user32.GetMessageW(ctypes.byref(msg), None, 0, 0)
        if ret == 0:                   # WM_QUIT
            break
        if ret == -1:                  # 错误
            raise OSError(f"GetMessageW 失败: {ctypes.get_last_error()}")
        user32.TranslateMessage(ctypes.byref(msg))
        user32.DispatchMessageW(ctypes.byref(msg))


if __name__ == "__main__":
    main()
