# tkinter-designer — Figma → Tkinter 代码生成器（vendored 范本）

> 上游：<https://github.com/ParthJadhav/Tkinter-Designer>（BSD-3-Clause，vendored 供研读）
> 本目录是**工具类示例**，不是业务应用示例。它回答的问题是：
> **「设计稿（Figma）怎么变成可运行的 tkinter 代码？」**

---

## 1. 它是什么

Tkinter Designer 通过 Figma REST API 拉取设计稿节点树，把矩形/文本/图片/按钮等元素
翻译成**绝对定位（`Canvas` + `place`）的 tkinter 代码**，并把切图导出成 `assets/`。

```
Figma 设计稿 ──REST API──> node 树 ──elements──> Jinja2 模板 ──> build/gui.py + build/assets/
```

一句话定位：**pixel-perfect 的一次性代码生成器**。生成的是"静态版式 + 图片素材"，
业务逻辑要自己补。

---

## 2. 目录结构

| 路径 | 说明 |
|------|------|
| `tkdesigner/cli.py` | 命令行入口（`argparse`）：`-o/--output` `-f/--force` `-t/--template` `--theme` + `file_url` `token` |
| `tkdesigner/designer.py` | 核心编排：调 Figma API → 遍历节点 → 渲染模板 → 落盘 |
| `tkdesigner/template.py` | **最值得读的文件**：三套 Jinja2 代码模板 + 公共运行时头 |
| `tkdesigner/figma/` | Figma 领域模型：`node.py` `frame.py` `vector_elements.py` `custom_elements.py` `endpoints.py` |
| `tkdesigner/utils.py` | `parse_figma_url()` 解析 file_key / node_id |
| `tkdesigner/constants.py` | 常量 |
| `gui/gui.py` | 生成器**自身的 GUI**（用它自己的风格写的：Canvas + place + PNG 切图） |
| `tests/` | pytest 用例：`test_cli.py` `test_generation.py` `test_utils.py` |
| `docs/` | 上游文档（已精简为中/英 + build 说明） |

---

## 3. 三种生成模板（`-t` 参数）

`template.py` 里定义了三套模板，共享同一个 `COMMON_TEMPLATE_HEADER`：

| `-t` 值 | 产物形态 | 适用 |
|---------|----------|------|
| `script`（默认） | 模块级 `window = Tk()` + 一路 `place`，`if __name__` 里 `mainloop()` | 单窗口小工具 |
| `class` | `class GeneratedApp:` 封装 `self.window` / `self.canvas`，带 `run()` | 要接业务逻辑、要被测试 |
| `pages` | 每个 Figma frame → 一个 `Frame` 子类，`GeneratedApp` 用 `tkraise()` 切页 + 自动生成 `< Back` / `Next >` | 多页向导/多屏应用 |

> **选型建议**：交付项目一律用 `-t class` 或 `-t pages`。`script` 模式生成的是模块级
> 全局变量，无法被 `smoke_test_gui.py` 无头导入测试，违反本技能的可测性要求。

---

## 4. `COMMON_TEMPLATE_HEADER` 里可直接抠走的零件

这段公共头是本示例**对本技能最有价值的部分**，五个函数都能原样搬进自己的项目：

```python
def enable_dpi_awareness():          # Windows 高 DPI：shcore.SetProcessDpiAwareness(1)
def center_window(window, w, h):     # 窗口居中（update_idletasks + winfo_screenwidth）
def relative_to_assets(path):        # 资源路径 = OUTPUT_PATH / ASSETS_PATH / path
def load_photo_image(path):          # PhotoImage 优先，失败回落 PIL；并 append 到 IMAGE_REFS 防 GC
def create_rounded_rectangle(...)    # Canvas 圆角矩形（12 点 polygon + smooth=True）
class ImageButton(Label):            # 图片按钮：Label + cursor="hand2" + <Button-1> 绑定
def apply_theme(window):             # ttk.Style(window).theme_use(THEME)，异常静默
```

要点解释：

- **`IMAGE_REFS` 全局列表**——tkinter 的 `PhotoImage` 一旦被 GC 图片就变空白，
  这是新手最高频的 bug。上游用一个模块级 list 兜住所有引用。本技能
  `references/04-widgets-and-patterns.md` 的"图片引用保活"就是这个套路。
- **`relative_to_assets` + `OUTPUT_PATH = Path(__file__).parent`**——打包成 EXE 后
  `__file__` 会指向解包目录，配合 `sys._MEIPASS` 才正确（见 `gui/gui.py` 里的
  `os.chdir(getattr(sys, "_MEIPASS", os.getcwd()))`）。本技能
  `references/08-packaging.md` 的资源路径规则与此一致。
- **`enable_dpi_awareness()` 在模块导入时就执行**（文件末尾裸调用）——必须在
  `Tk()` 创建**之前**调用才生效。

---

## 5. 运行方式

### 5.1 命令行生成

```bash
# 先装依赖（本技能默认零依赖，此示例是例外）
pip install -r requirements.txt        # jinja2 / Pillow / requests / urllib3

# 生成（URL 含 ? & 时务必加引号）
set FIGMA_TOKEN=figd_xxxxxxxx
python -m tkdesigner.cli "https://www.figma.com/file/<KEY>/<NAME>?node-id=0%3A1" -o ./out -t class --theme clam
# → ./out/build/gui.py + ./out/build/assets/
```

### 5.2 图形界面

```bash
python gui/gui.py
```

三个输入框：Figma 文件 URL、Token、输出目录，点 `Generate`。

### 5.3 跑上游测试

```bash
pip install pytest
python -m pytest tests/ -q
```

---

## 6. 依赖与许可（重要）

| 项 | 值 |
|----|-----|
| 运行期依赖 | `jinja2>=3.1,<4`、`Pillow>=11,<13`、`requests>=2.31,<3`、`urllib3>=1.26.18,<2` |
| 许可 | BSD-3-Clause（见 `LICENSE`） |
| 需要外部账号 | **是**——必须有 Figma 账号 + Personal Access Token |
| 是否影响交付项目 | **否**——它只在开发期生成代码，生成物是纯标准库 tkinter（除非用到 PIL 回落分支） |

> ⚠️ 本技能的铁律是「交付项目零第三方运行期依赖」。Tkinter Designer 属于
> **开发期工具**，它的依赖不进交付包。但生成的 `gui.py` 里保留了
> `try: from PIL import Image, ImageTk / except ImportError:` 的回落，
> 只要素材是 PNG/GIF，就能纯标准库运行——交付前请确认这一点。

---

## 7. 与本技能其它 UI 路线的关系

| 路线 | 代表 | 布局方式 | 何时用 |
|------|------|----------|--------|
| 手写 ttk + grid/pack | `examples/inventory-manager/` | 业务系统 CRUD，手写 ttk 可缩放 | **默认路线**，业务系统首选 |
| pygubu `.ui` + Builder | `../pygubu/`（子技能） | 声明式 XML，仍是 grid/pack | 要可视化拖拽 + 保持可缩放 |
| **Tkinter Designer** | 本目录 | `Canvas` + `place` 绝对坐标 | 设计稿像素级还原、固定尺寸窗口 |

**关键取舍**：Tkinter Designer 生成的窗口一律 `window.resizable(False, False)`，
因为绝对定位不能自适应。所以它适合**登录页、启动页、单屏工具、仪表盘大屏**这类
固定尺寸场景；**不适合**需要拉伸、需要响应式的业务主窗口。

---

## 8. 可借鉴要点清单（做自己的 App 时抠这些）

1. `IMAGE_REFS` 保活列表 —— 解决 `PhotoImage` 被 GC 变空白。
2. `enable_dpi_awareness()` —— Win 高 DPI 不糊字，必须在 `Tk()` 前调用。
3. `center_window()` —— 三行代码窗口居中。
4. `create_rounded_rectangle()` —— 纯 Canvas 圆角，零依赖做现代卡片。
5. `ImageButton(Label)` —— 用 Label 冒充按钮，实现完全自定义外观。
6. `pages` 模板的 `tkraise()` 多页切换 —— 标准的 tkinter 多页范式。
7. `-t class` 生成的 `GeneratedApp` 结构 —— 可被无头测试导入的最小封装。
8. Jinja2 驱动的代码生成思路 —— 自己做内部脚手架时可照搬。

---

## 9. 运行 / 一键启动

本目录已附带 **`启动.bat` + `run.py`**，双击 `启动.bat` 即启动 Tkinter-Designer 自带 GUI
（`gui/gui.py`）。`run.py` 会在依赖缺失时**自动用国内镜像安装** `requirements.txt`
（jinja2 / Pillow / requests / urllib3），再启动界面——无需手动装依赖。

```bash
# 一键启动（Windows 双击即用）
启动.bat
# 等价：python run.py

# 命令行模式（代码生成，不弹 GUI）
python -m tkdesigner.cli -o build --template class <figma_file_url> <token>
```

> 注意：Tkinter Designer 是**开发期工具**，依赖不进交付包。它生成的 `gui.py`
> 含 `try: from PIL import Image, ImageTk / except ImportError:` 回落，
> 素材为 PNG/GIF 时可纯标准库运行（详见 §6 取舍）。
