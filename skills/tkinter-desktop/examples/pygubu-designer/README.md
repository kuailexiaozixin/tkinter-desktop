# pygubu-designer — 用 tkinter 写成的生产级 RAD 设计器（完整源码示例）

`pygubu-designer` 本身就是一个**用纯 tkinter 开发的大型真实应用**（RAD 可视化 UI 设计器），
本目录把它**完整源码 vendored 进来**——不是「只读研习」的片段，而是一份
**可直接阅读、修改、运行的生产级代码全集**：含全部 `.py` 源码与 `data/` 资源
（`data/ui/*.ui` 设计器自身的窗口定义、`data/images/`、`data/locale/` 多语言、`data/code_templates/` 代码模板）。

本例与 `examples/` 下其它案例（inventory-manager、native-win32、thonny …）同一取向：
**给 LLM 一份「真实软件在生产环境里长什么样」的参照**，而不是玩具 demo。

> 许可：pygubu-designer 本体 **GPL-3.0**（见同目录 `LICENSE`）。可作学习参考与本地运行，
> 不要把它当业务依赖直接引入你的闭源产品。当前 vendored 版本：`__version__ = "0.41.4"`，
> 与上游 GitHub tag `v0.41.4` 逐字节一致（仅去除 `__pycache__`/构建产物等无用文件）。

---

## 本目录内容

| 路径 | 说明 |
|------|------|
| `pygubudesigner/` | **designer 的完整可运行源码**（含全部子包与 `data/` 资源）。`run.py` 直接启动它 |
| `run.py` | 启动引导脚本：把本目录插入 `sys.path` 最前并设 DPI 感知，**确保跑的是本目录 vendored 源码** |
| `启动.bat` | 一键启动（调用 `run.py`，优先 `pythonw` 无控制台窗口） |
| `LICENSE` | 上游 GPL-3.0 全文 |
| `README.md` | 本文件 |

### 启动脚本跑的是哪份代码？

`启动.bat` → `run.py` 用 `cd /d "%~dp0"` 切到本目录再启动，并把本目录插入 `sys.path` 最前，
因此 `import pygubudesigner` **命中的是本目录的 `pygubudesigner/` 源码，而不是你 pip 装的官方包**。
这样「读到的源码 = 跑起来的源码」，自包含、与系统里的同名包解耦。

> **DPI 说明**：控制台子系统启动时进程默认 DPI 不感知，Tk 会按 96 DPI 虚拟值渲染，字体比官方
> 包（DPI 感知）偏小。`run.py` 在导入 tkinter 之前调用 `SetProcessDpiAwareness`，让 Tk 按真实
> 屏幕 DPI 计算字体，显示与官方打包的 `.exe` 一致。

### 外部运行时依赖（仅 `pygubu` 核心库与少量支撑库，不随本目录 vendored）

`pygubudesigner` 在 `pyproject.toml` 中声明依赖 `pygubu >=0.38.2`（UI 构建核心库，纯 Python）。
从你的 Python 环境（pip）提供即可。**缺 `appdirs` 会直接 `sys.exit(-1)`；缺 `blinker` 属性注册表无法初始化**：

```bash
pip install "pygubu>=0.38.2" appdirs blinker
```

> **已验证可运行组合**：本机 `pygubu 0.40.1` + `appdirs 1.4.4` + `blinker`，与 vendored 的 designer 0.41.4 搭配正常启动。
> `pygubu 0.40.x` 不在包上暴露 `__version__`，但 designer 0.41.4 启动时会读 `pygubu.__version__`——
> 这部分由 `run.py` 从包元数据（`importlib.metadata`）补上，因此**无需改动上游源码**即可启动。
> 同理 `run.py` 在 import `pygubu` **之前**就置好 `PYGUBU_DESIGNER_RUNNING`，让 `pygubu` 的属性注册表
> 启用「真实（带信号）」实现，否则会退化为静默丢弃注册的 Dummy，导致 `'class'`/`'id'` 属性 KeyError。

---

## 怎么用这个示例

1. **读 / 改 / 跑真实代码**：直接浏览 `pygubudesigner/` 各模块，或双击 `启动.bat` 把设计器跑起来，
   用可视化拖拽做 UI，保存为 `.ui` 后用 `pygubu.Builder` 加载（见下）。
2. **学「生产级 tkinter 应用」怎么搭**：下面这些是本例最值得借鉴的架构模式——

| 生产模式 | 在本例的位置 |
|----------|--------------|
| **UI 与逻辑分离（.ui 驱动）** | `services/main_window.py` + `main_windowui.py`；窗口布局写在 `data/ui/*.ui`，逻辑类加载它 |
| **可扩展的控件/工具体系** | `services/widgets/`（container layout editor、tree component palette、properties editor、project tree frame）及其 `*ui.py` |
| **动态属性编辑面板** | `properties/` + `properties/editors/`（color / font / image / sticky / ttkstyle / json 等专用编辑器） |
| **代码生成器（反向工程）** | `codegen/`（codebuilder、scriptgenerator）+ `data/code_templates/*.mako` 模板 |
| **预览宿主** | `preview/`（builder / preview / helper）把任意 `.ui` 真正渲染并嵌入设计器 |
| **样式与主题** | `designerstyles.py` + `services/stylehandler.py` + `services/theming.py` 用 `ttk.Style` 做专业外观 |
| **i18n 多语言** | `i18n.py` + `data/locale/`（de/es/tr/zh_CN/zh_Hans 的 `.po`/`.mo`） |
| **文件 / 项目管理** | `services/fileactions.py`、`project.py`、`rfilemanager.py` |
| **异步任务与可观测** | `util/taskexecutor.py`、`util/observable.py`、`util/loghandler.py` |

---

## 运行时加载 `.ui`（与 AI 自动化 UI 设计的关系）

designer 产出的是 `.ui`（XML）。运行你的应用时，用 `pygubu.Builder` 三行加载（来自 pip 的
`pygubu` 库，非本目录 vendored 副本）：

```python
builder = pygubu.Builder()
builder.add_from_file("x.ui")                  # ① 解析 XML
mainwindow = builder.get_object("mainwindow")  # ② 取控件
builder.connect_callbacks(self)                # ③ 把 .ui 的 command 接到同名方法
```

> **AI 自动化 UI 设计工作流**（写 `.ui` → 无头校验 → 截图校验 → 改错，单一闭环）见技能
> `pygubu/`（子技能 SKILL.md）；`.ui` 格式 / `Builder` API / 专属控件 / 语法坑 / 打包要点均已合并入该文件。
