# native-win32 — 纯 Win32 API 计算器（ctypes 原生窗口示例）

> 本目录展示**不使用 tkinter** 的纯 Win32 原生窗口开发——作为对比参照和
> ctypes 编程的学习起点。

## 文件

| 文件 | 说明 |
|------|------|
| `calculator.py` | 440 行纯 Win32 API 计算器：窗口注册 → WNDPROC 回调 → 控件创建 → GDI 状态栏绘制 → 消息循环 |

## 运行

```bash
python calculator.py
```

弹出原生 Windows 风格的计算器窗口（非 tkinter 渲染）。

## 可借鉴要点

1. **完整消息驱动骨架**——RegisterClassW → CreateWindowExW → ShowWindow → GetMessageW 循环
2. **WNDPROC 全局引用防 GC**——回调必须赋值给模块级变量（`WndProc`）
3. **控件 ID 体系**——IDC_DISPLAY / IDC_BUTTON_0~9 / IDC_BUTTON_ADD 等
4. **WM_COMMAND 处理**——wparam 低 16 位 = 控件 ID，高 16 位 = 通知码
5. **WM_PAINT GDI 绘制**——BeginPaint/EndPaint + CreateSolidBrush/FillRect 画状态栏 + TextOutW 输出文字
6. **gdi32.dll 归属**——CreateSolidBrush/DeleteObject/TextOutW 在 gdi32 不在 user32
7. **GetMessageW 返回值判定**——返回 `0` 是 WM_QUIT（正常退出），返回 `-1` 是调用出错（须 raise，不能当退出）

## 与 tkinter 的关系

本示例是**"底层能力参考"**——当你需要在 tkinter 应用中调用 Win32 API
（高 DPI、任务栏图标、单实例锁定、系统托盘等）时，
先理解这里的 ctypes 模式，再通过 `root.winfo_id()` 获取 HWND 进行互操作。
详见 `ctypes/SKILL.md` §3 "tkinter ↔ Win32 互操作模式"。
