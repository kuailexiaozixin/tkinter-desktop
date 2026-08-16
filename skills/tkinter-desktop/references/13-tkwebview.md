# 17 · tkwebview 参考手册（内嵌 WebView2 内核的轻量控件）

> **定位**：本文件是 `tkinter-desktop` 技能下「可选第三方增强」的专属参考。tkwebview 是用于在 tkinter 程序里**内嵌真实浏览器内核**的控件，是 `tkwebview2` 的**轻量替代**：它用 C 直接封装 `webview/webview` + `webviewpy`，**不依赖 `pywebview` / `pythonnet`**，因此 EXE 体积几乎不增长。
>
> 内容综合自官方 PyPI（https://pypi.org/project/tkwebview/）与 GitHub 仓库（https://github.com/Smart-Space/tkwebview）整理。**作者：Smart-Space｜许可证：MIT｜要求 Python >= 3.7**。
>
> 同族对照：**tkwebview2**（见 `03-ui-design.md`「tkwebview2 / tkwebview」一节）功能更全（完整 Edge/Chromium 内核 + JS↔Python 双向 + devtools）但拉入 `pythonnet`+`pywebview` 重链、EXE +6MB；**tkwebview** 更轻、能力更受限。两者最终都依赖系统级 **WebView2 Runtime**（Edge 内核，~100–150MB，Win10/11 通常已预装，缺了可由 `install_runtime()` 下载）——**该内核是系统组件，不进 EXE**。

---

## 0 · 何时引入 / 何时不引入

**引入场景**（ttk/Canvas 都搞不定时才上）：
- 要在桌面程序里嵌入**真实网页 / 现代 HTML+CSS+JS**（合规报表、OAuth 登录页、嵌入 ECharts/D3 图表、在线地图、富文本/Markdown 渲染等）。
- 需要 JS 调用 Python（如前端按钮触发本地计算）但**不需要**完整内核能力的场合。

**不引入**：
- 纯展示型内容 → 用 ttk/Canvas 即可，别为"能显示网页"而引内核。
- 要完整现代 Web 标准 + devtools + 双向互操作 → 改用 `tkwebview2`（代价是 +6MB 与 .NET 依赖链）。

**选型小结**：要最小体积增量、能接受纯 C 封装的有限能力 → **tkwebview**；要完整 Edge 内核能力 → **tkwebview2**。

---

## 1 · 重要限制（务必先看，避免踩坑）

> 以下均来自官方 README 原文，是 tkwebview 的硬约束，不是可选项。

1. **无事件回调（event callback）**：tkwebview 当前没有 DOM 事件回调机制；但它**具备十分重要的「JS 调用 Python」能力**（`bindjs`），足以覆盖绝大多数交互需求。
2. **难以操作原始 web 控件**：因经过封装，无法直接操控底层 web 控件——好处是简单易用，坏处是灵活度低。
3. **仅提供 Windows 平台的二进制链接库**（32 位未测试）。理论上 `webview` 可跨平台，但作者只发布了 Windows 二进制；跨平台代码须写在其维护的 C++ 库 `Smart-Space/webview` 中。
4. **Windows 焦点陷阱（最常见坑）**：在 tkinter 界面中，**WebView2 拥有最高级渲染优先级**——一旦 webview 获得焦点，除非离开整个窗口，否则**其它控件无法再获取焦点**。
   - **解法**：给所有控件绑定 `<Button-1>`，用 `event.widget.focus_force()` 强制夺回焦点；若某控件自身还需要 `<Button-1>`，用 `bind(..., add=True)` 追加而非覆盖。
5. **`navigate(url)` 的 url 必须以协议开头**（http / https / file …），否则不导航。

---

## 2 · 安装

```bash
pip install tkwebview
```

---

## 3 · 核心类：`TkWebview`（本质是一个 Frame）

```python
TkWebview(master, **kwargs)
```

- tkwebview 的核心类，**本质上是一个 tkinter `Frame`**，可以像 Frame 一样 `pack`/`grid`/`place` 布局。
- `master` 给定 → **控件模式**（嵌入 tkinter 窗口）：
  ```python
  web = TkWebview(master=root)
  web.pack(fill="both", expand=True)
  ```
- `master=None` → **独立模式**（单独开一个 webview 窗口，类似 `webviewpy`）：
  ```python
  web = TkWebview()          # master 默认 None
  web.set_size(800, 400)
  web.set_title("TkWebview Test")
  # 独立模式需要显式开启 UI 循环：
  tkwebview.webview.run()
  ```
  > 注意：独立模式要运行 UI 循环须调用 `tkwebview.webview.run()`；而**嵌入控件模式**仍走普通 `root.mainloop()`。

---

## 4 · 完整 API 清单

### 控件模式 / 独立模式通用

| 方法 | 说明 |
|---|---|
| `bindjs(name, fn, is_async_return=False)` | 绑定名为 `name` 的 JS 函数指向 `fn`；JS 中用 `window.name` 调用（见 §5）。 |
| `unbindjs(name)` | 解除绑定名为 `name` 的 JS 函数。 |
| `dispatch(fn)` | 在子线程中调度 `fn` 到主线程/GUI 上运行。 |
| `eval(js)` | 执行 JS 代码。 |
| `navigate(url)` | 导航到 `url`（须以 `http/https/file...` 协议开头）。 |
| `init(js)` | 在页面内容之前注入 JS 代码（最靠前）。 |
| `set_html(html)` | 设置 HTML 内容。 |
| `version()` | 返回 `webview/webview` 的版本。 |

### Windows Only（仅 Windows 实现的导航控制）

| 方法 | 说明 |
|---|---|
| `reload()` | 重新加载。 |
| `go_back()` | 后退一页。 |
| `go_forward()` | 前进一页。 |
| `stop()` | 停止加载。 |

### 独立模式专有

| 方法 | 说明 |
|---|---|
| `set_title(title)` | 设置窗口标题。 |
| `destroy_webview()` | 关闭 webview 窗口（独立模式）/ 销毁本控件（控件模式）。 |
| `get_window()` | 返回窗口 ID（Windows=HWND，Linux=GtkWindow 指针，Cocoa=NSWindow 指针）；控件模式返回上层组件 ID。 |
| `set_size(width, height)` | 设置窗口大小（独立模式）/ 尝试修改控件大小（控件模式）。 |

> ⚠️ **`set_size` 在嵌入（控件）模式下存在限制**：原始 `set_size` 无法满足嵌入状态下的尺寸修改，作者为此单独维护了一个基于 webview 的 C++ 库。嵌入时更可靠的做法是依赖 tkinter 的 `pack(fill="both", expand=True)` / `grid(sticky="nsew")` 让 Frame 自适应，而非手动 `set_size`。

---

## 5 · 用法示例（官方 `test.py` 整理版）

下面示例演示**两种模式** + **焦点陷阱解法** + **JS↔Python 双向调用**（同步 `count` 与异步 `compute`）。

```python
import tkinter as tk
from tkinter import Entry
import tkwebview                      # 核心类：tkwebview.TkWebview
import ctypes
from threading import Thread
from time import sleep

# 高 DPI 感知（必须在 Tk() 前，见 ctypes/SKILL.md）
ScaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0) / 100
ctypes.windll.shcore.SetProcessDpiAwareness(1)

def get_url(event):
    # url 必须以协议开头（https/http/file…）
    web.navigate(e.get())

count_num = 0
def count(req):                       # 同步：收参数，返回结果
    global count_num
    count_num += req
    return str(count_num)

def compute(returner, num1, num2):    # 异步：首参是 returner，算完调 returner(result)
    def _(_1, _2):
        sleep(1)
        returner(_1 * _2)
    Thread(target=_, args=(num1, num2)).start()

root = tk.Tk()
root.tk.call("tk", "scaling", ScaleFactor)
root.geometry("800x400")

e = Entry(root, font="微软雅黑 18", relief="solid")
e.pack(fill="x", padx=10, pady=5)
e.bind("<Return>", get_url)

html = """
<div>
  <button id="increment">+</button>
  <button id="decrement">−</button>
  <span>Counter: <span id="counterResult">0</span></span>
</div>
<script type="module">
  const increment = document.getElementById("increment");
  const decrement = document.getElementById("decrement");
  const counterResult = document.getElementById("counterResult");
  const compute = document.getElementById("compute");
  const computeResult = document.getElementById("computeResult");
  increment.addEventListener("click", async () => {
    counterResult.textContent = await window.count(1);     // 调 Python
  });
  decrement.addEventListener("click", async () => {
    counterResult.textContent = await window.count(-1);
  });
  compute.addEventListener("click", async () => {
    compute.disabled = true;
    computeResult.textContent = await window.compute(6, 7);  // 调 Python（异步）
    compute.disabled = false;
  });
</script>"""

# 控件模式（嵌入 tkinter）；独立模式把 master 去掉即可
web = tkwebview.TkWebview(master=root)
web.pack(fill="both", expand=True)

web.set_html(html)
web.bindjs("count", count)                       # 同步绑定
web.bindjs("compute", compute, is_async_return=True)  # 异步绑定

# ===== 焦点陷阱解法（必加）=====
# WebView2 获焦后其它控件无法再聚焦，给所有控件强制夺回焦点
root.bind_all("<Button-1>", lambda ev: ev.widget.focus_force())
# 若某控件自身还要 <Button-1>，用 add=True 追加：
# e.bind("<Button-1>", other_handler, add=True)

root.bind("<Alt-Left>",  lambda ev: web.go_back())
root.bind("<Alt-Right>", lambda ev: web.go_forward())
root.bind("<F5>",        lambda ev: web.reload())
root.bind("<Escape>",    lambda ev: web.stop())

root.mainloop()
```

---

## 6 · JS ↔ Python 绑定（`bindjs`）

- **签名**：`bindjs(name, fn, is_async_return=False)`
- JS 侧通过 `window.<name>(...args)` 调用，Python 侧 `fn` 接收这些参数。
- **同步模式**（`is_async_return=False`）：`fn` 接收 JS 传来的参数，直接 `return` 结果即可。
- **异步模式**（`is_async_return=True`）：`fn` 第一个参数位会收到一个 `returner` 函数；异步处理完结果后调用 `returner(result)` 把结果回传 JS（如上例 `compute`）。
- 解绑：`unbindjs(name)`。

> 这是 tkwebview 与 Python 通信的**唯一官方通道**（无事件回调）。需要 DOM 事件驱动 Python 时，在页面 JS 里 `window.<name>(...)` 即可。

---

## 7 · 打包与体积（实测）

tkwebview 是 C 扩展、自带平台 DLL（`.tkwebview/platform/...`，运行时经 `ctypes.CDLL` 加载）。

**实测体积（PyInstaller `--onefile --windowed`，Python 3.13.14）**：

| 版本 | EXE 体积 | 增量 |
|---|---|---|
| 纯标准库基线 | 9.90 MB | — |
| 引入 **tkwebview** | 10.06 MB | **+0.2 MB**（可忽略） |
| 真实应用复测（announcement-downloader，基线 15.88 MB，已含 pygubu/requests/win32/sqlite） | 15.88 MB | **+0.01 MB**（几乎为零） |

**打包注意（重要）**：
- tkwebview 通过 `ctypes.CDLL` 在运行期加载其原生 DLL，**PyInstaller `--onefile` 不一定会自动收集这个 ctypes 加载的 DLL**——构建可能"成功"但运行期报找不到 DLL。
  - 对策：加 `--collect-binaries tkwebview`，或显式 `--add-binary "路径/to/平台dll;tkwebview/platform/win32"`；打完后务必在**干净环境**里实际启动验证。
- 真正的浏览器内核 **WebView2 Runtime 是系统组件、不进 EXE**；目标机缺内核时可由 `install_runtime()` 自动下载（运行期联网）。
- 完整打包细则见 `08-packaging.md`「第三方美化库打包」一节；与 `tkwebview2` 的体积/能力取舍见 `03-ui-design.md`「tkwebview2 / tkwebview」一节。

---

## 8 · 一句话总结

> tkwebview = **几乎零体积代价**的「在 tkinter 里嵌网页」方案，靠 `bindjs` 做 JS→Python 通信；代价是**能力受限（无事件回调、难控原始控件、仅 Windows 二进制）**且必须处理 **Windows 焦点陷阱**。要完整内核能力就换 `tkwebview2`。
