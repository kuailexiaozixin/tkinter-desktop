---
name: tkinter-desktop
description: >
  Tkinter/ttk 原生桌面应用的全生命周期技能。覆盖从需求澄清、架构分层（MVC）、界面设计、
  编码、线程与异步、SQLite 数据层、运行验证到 PyInstaller 打包交付的完整链路。
  最终交付物是原生 Tkinter 桌面 EXE（无浏览器、无本地 HTTP 服务）。
  界面默认以 `.ui` 定义、运行期用 pygubu Builder 加载。
  当用户提到"Tkinter""ttk""Tk 界面""原生桌面""不依赖浏览器的桌面程序"
  "Python 自带 GUI""基于 .ui 的 tkinter 应用"时使用本技能。
version: "1.7.10"
author: agent
agent_created: true
platform: windows
---

# tkinter-desktop

> **技术栈（默认交付栈）**：tkinter/ttk（标准库 GUI）+ **pygubu（`.ui` 界面定义 + Builder 加载，固定运行期依赖）** + sqlite3（标准库数据层）+ PyInstaller（打包）。界面以 `.ui` 为唯一载体，运行期用 `pygubu.Builder` 加载；**非界面部分的业务/数据层保持零第三方依赖**。
> **pygubu 是界面设计的唯一默认方案**：AI 只写 `.ui` + 用 `pygubu.Builder` 校验/加载，不驱动 pygubu-designer 的 GUI（designer 仅人类可选工具；手搓 ttk 降级为备选）。完整 AI 自动化闭环见唯一 **`pygubu/`（子技能）**，脚本在 `scripts/ai-ui-design/`。
> **第三方增强（tksheet / tkchart 等）按需引入完全合法**：打包补 hidden-import 见 `08-packaging.md`，选型取舍见 `03-ui-design.md`（§1 / §10）。

一个技能，一次跑通，一种交付物——**原生桌面 EXE**。

---

## HARD-GATE：写控件代码前必读官方文档转档（不可跳过 · 首要地位）

> **`references/official-docs/` 是写代码前的「首要必读」（核心地位）。** 本技能任何控件/API 相关论断都以此转档为最高权威，技能正文与之冲突时以它为准。

**写任何 ttk 控件代码前，必须先读** `references/official-docs/tkinter-ttk.md`（ttk 全部控件的
选项、方法、样式系统）；涉及底层机制（变量类、事件绑定、pack/grid/place、after）时读
`references/official-docs/tkinter-core.md` 对应章节。

阅读后要求：
1. 确认本任务用到的控件清单及其关键选项（如 `Treeview` 的 `columns/show/selectmode`）
2. 确认样式定制走 `ttk.Style`，而不是给 ttk 控件传 `bg=/fg=` 这类经典选项（会报
   `unknown option "-bg"`）
3. 确认事件与虚拟事件名（如 `<<TreeviewSelect>>`、`<<ComboboxSelected>>`、`<<NotebookTabChanged>>`）

**跳过的后果**：ttk 选项用错、样式不生效、事件名拼错静默失效。

---

## 控件间距与行高铁律（必须遵守）

> **ttk 的默认间距参数是为 96DPI 英文环境设计的**（Treeview 默认 `rowheight=20`、控件默认 padding 极小）。
> 在中文 Windows / 高 DPI / 大字号下，**直接用默认值必然导致文字截断、行紧叠、字体被遮掩**（如你截图所示）。

### Treeview 行高：必须用 `font.metrics()` 计算，禁止依赖默认值

- **铁律**：任何使用 `ttk.Treeview` 的项目，`setup_style()` 里**必须调用 `setup_treeview_rowheight()` 设置 rowheight**。禁止使用默认值 20。
- **公式**：`rowheight = font.metrics('linespace') + vertical_reserve`（舒适模式 +8px）
- **完整公式、`setup_treeview_rowheight()` 函数、四档模式对照表（紧凑/舒适/宽松）、以及「默认 20 在各场景下的症状表」**：见 **`references/03-ui-design.md` §5.1**
- **反模式与自查清单**：见 **`references/03-ui-design.md` §11 反模式清单** / **§12 自查清单**
- **现象/本质/解法记录**：见 **`docs/troubleshooting.md`** 布局节「Treeview 内容对但列宽/行高怪异、中文挤成一团」

### 表单与通用控件间距

- **铁律**：表单控件之间必须有 `pady`/`padx` 间距，禁止零间距堆叠；间距应随 DPI 缩放（`dpi_scale * base_padding`）。
- **完整规范（padding / pady / DPI 缩放 / 高 DPI 验证全套）**：见 **`references/03-ui-design.md` §5.2~5.4**

---

## 快速理解这个技能在做什么

```
你写 View（`.ui` 界面定义，运行期 pygubu.Builder 加载）
      ↓
Controller 衔接事件 → Model（业务逻辑 + sqlite3）
      ↓
PyInstaller 打包成 EXE（双击即用，--windowed 无黑框）
```

本技能的本质特征：**没有 HTTP 服务、没有浏览器内核**。界面就是 Python
对象，状态就在进程内。因此：没有路由链路问题、没有静态资源路径问题、没有端口协商问题；
换来的新约束是：**主线程规则**（所有 UI 操作必须在 Tk 主线程）、**mainloop 阻塞模型**、
**ttk 样式系统**。

---

## 架构约束（选型前必读）

1. **单进程单主线程 GUI**：Tkinter 非线程安全。任何耗时操作（网络、文件、DB 大查询）
   放 worker 线程，结果经 `queue.Queue` + `widget.after()` 轮询回主线程刷新 UI。
   **禁止在子线程直接调用任何 widget 方法**（详见 `references/05-threading-and-async.md`）。
2. **mainloop 之后无代码**：`root.mainloop()` 是阻塞调用，其后的语句在窗口关闭前不会执行。
   初始化必须全部在 mainloop 之前完成；周期任务用 `after`，不要用 `while + sleep`。
3. **界面即状态**：没有"刷新页面"概念。数据变更后必须显式调用视图刷新方法
   （如重填 Treeview）。推荐 Model→View 的观察者/回调解耦（见 `references/02-architecture-mvc.md`）。
4. **验证路径**：Tkinter 可在无显示环境用 `root.update()` 驱动而不进 mainloop，
   因此**可以做真实控件级的自动化测试**（实例化 App → 调用回调 → 断言控件内容），
   这是本技能的机器验证主路径（见 `references/09-testing-and-quality.md`）。

---

## 目录结构与主题路由

> 原则：先按意图命中下表，再读对应文件；命中多个时优先读更具体的那个。

### 入口与决策

- **不清楚该从哪里开始** / 想了解完整流程：`./docs/glossary.md` → 读完回归此表
- **需求澄清**、首轮话术、必问问题：`./references/01-need-discovery.md`

### 环境与项目初始化

- Tkinter 是标准库，**无需安装 GUI 依赖**；但仍须为项目创建独立 venv（打包体积门禁）
- 项目初始化：`./scripts/bootstrap_project.ps1`（生成 src 结构 + MVC 骨架 + venv）
- 环境自检：`python -c "import tkinter; print(tkinter.TkVersion)"`（应 >= 8.6）

### 架构设计

- **MVC 分层与模块划分**（Model/View/Controller 职责、观察者模式、目录映射）：
  `./references/02-architecture-mvc.md`

### 编码与结构规范

文件体系分为三个层级，按顺序自上而下查阅。**Layer 1 为前置必读**。

#### Layer 1：官方 API 参考（⭐ 核心地位 / 首要地位，前置必读）

> **`references/official-docs/` 是本技能「权威性最高、优先级最高」的首要参考（核心地位）。**
> 它是 Python 3.13 + Tk 8.6 官方文档的本地转档，覆盖 ttk 全部控件、tkinter 核心机制、Tcl/Tk 8.6 命令参考——**任何控件选项、API 行为、底层命令的疑问，一律先查它；只有它确实没有覆盖的主题，才退回到技能正文或其他参考。** 下表所有条目均属于该核心参考。

| 文件 | 说明 | 优先级 |
| ---- | ---- | ------ |
| `references/official-docs/tkinter-ttk.md` | **ttk 全部控件**选项/方法/样式/Treeview/Notebook | **写控件代码前必读** |
| `references/official-docs/tkinter-core.md` | tkinter 核心机制：变量类、绑定、几何管理、after、协议 | 涉底层机制时查阅 |
| `references/official-docs/tkinter-messagebox.md` | 消息框 API | 用到弹窗时查阅 |
| `references/official-docs/tkinter-dialogs.md` | filedialog / colorchooser | 用到文件对话框时查阅 |
| `references/official-docs/tkinter-font.md` | 字体对象 | 定制字体时查阅 |
| `tcl-tk/tcl8.6-docs/` | **Tcl 8.6 / Tk 8.6 官方文档镜像（本地 Markdown）**：全 16 分区 488 页（Tcl/Tk 命令、解释器、第三方包、C API、关键词），与运行期 Tk 8.6 / Python 3.13 严格对齐；查 `event`/`bindtags`/`wm`/`winfo`/`grab`/`ttk_style`/`option`/`clipboard`/`selection` 等底层命令时查阅（**禁用 9.0 手册**）。**涉 Tcl/Tk 底层桥接调用（tk.eval/call、Tcl()、createcommand、ttk::style 底层、wm 高级等）→ 先读独立子技能 `tcl-tk/SKILL.md`** | 涉底层 Tcl/Tk 命令 / 桥接时查阅 |
| `references/11-moore-tkinter-2e-index.md` | **⭐ 重要参考价值** —《Python GUI Programming with Tkinter》第 2 版（Alan D. Moore, Packt 2021）索引：原书 PDF 在 `references/` 同名文件；本索引含 16 章+附录 A/B 的逐节页码（印刷页→PDF 页，偏移 +25）、主题速查表；覆盖 MVC/校验 Mixin/Treeview/Notebook/Ttk 主题/跨平台菜单/unittest 测 Tkinter/SQL 后端/联网/threading+Queue/Canvas 图表/cx_Freeze 打包等工程化主题。**凡遇技能正文未覆盖的工程化主题，优先查此索引定位原书章节。** | 讲「工程组织与最佳实践」或技能正文未覆盖的主题时查阅（重要参考） |

#### Layer 2：框架集成与项目结构

| 文件 | 说明 |
| ---- | ---- |
| `references/07-project-structure.md` | src 结构、入口规范、路径适配、日志 |
| `references/04-widgets-and-patterns.md` | **高频实战模式**：Treeview 表格 CRUD、表单构建器、模态对话框、Notebook 多页、滚动容器、状态栏、**菜单与快捷键深度（§7）、简单控件配方（Listbox/Scale/Spinbox/Progressbar，§8）、窗口行为（Toplevel/模态协议/无边框/置顶/多窗口，§9）** |
| `references/06-data-layer-sqlite.md` | sqlite3 数据层：连接管理、schema 迁移、种子数据、Repository 模式 |
| `references/05-threading-and-async.md` | 线程规则、after 轮询、queue 桥接、进度条模式 |

| `ctypes/`（子技能） | **Win32 原生能力（ctypes P/Invoke，强制规则）**：6 条强制签名纪律（argtypes/restype、wintypes、GDI 归属、回调 GC、句柄配对、Unicode W 后缀）+ 互操作模式（高 DPI/任务栏图标/托盘/单实例/原生对话框）+ 分卷（common-apis/structures/ctypes-mapping/resource-management/message-loop）。**涉 Win32 原生调用（ctypes）→ 读 `ctypes/SKILL.md`** |
| `pywin32/`（子技能） | **pywin32 离线文档全集（6771 页）+ Tkinter 实战指南**：原生控件嵌入/系统对话框/托盘/COM 自动化/ActiveX/DPI 视觉样式。**涉 pywin32 原生 UI → 读 `pywin32/SKILL.md`** |

#### Layer 3：界面设计质量

| 文件 | 说明 |
| ---- | ---- |
| `references/03-ui-design.md` | 界面设计（方法论+战术+现代增强已合并）：Design Token 单一真相来源、标准库 vs 第三方 选型框架、ttk.Style 非 CSS 真相、复合布局、ttk.Style 主题化、配色/字体/DPI、**Canvas 自绘图表 + Canvas 交互深挖（图元/命中/拖拽/滚动，§6.4）、Text 富文本进阶（标签/marks/搜索/撤销，§6.5）**、组件封装、第三方库可选方案、反模式与自查清单、社区控件库检索目录（§14） |
| `references/12-tksheet.md` | **可选增强专属参考**：tksheet 高性能表格/树形表格（可编辑、下拉/复选/进度条、拖拽行列、树形模式、v7 简洁语法、MIT、已停止功能开发、何时选不选） |
| `references/10-tkchart.md` | **可选增强专属参考**：tkchart 实时折线图控件（LineChart/Line、流式更新、多线对比、刻度/网格/线型定制、纯 tkinter 增量≈0、PyInstaller 小节、MIT、何时选不选） |
| `references/15-tkinter-toolkit.md` | **社区控件库目录（全量）**：从 Tkinter-Toolkit 目录 `database.json` 提取的**全量**条目（74 条，已剔除本技能不覆盖的 tkinterweb），按类别整理并附作者、仓库链接与**框架标注**（原生 ttk / CustomTkinter / 平台(Win32) / 工具），便于按「优先原生 ttk」立场检索第三方控件库与工具 |
| `pygubu/`（子技能，SKILL.md） | **AI 自动化 UI 设计（pygubu 路线，单一闭环）**：pygubu / pygubu-designer 工具本体、`.ui` XML 格式、Builder API、`connect_callbacks`、专属控件/插件、`.ui` 语法坑（resizable 枚举 / pady 单值 / button command JSON / Treeview Column / Notebook Tab）、无头校验 `check_ui.py` → 视觉截图校验 `check_ui_visual.py` → 改错的完整闭环、打包要点、官方链接；配套脚本 `scripts/ai-ui-design/` |
| `references/13-tkwebview.md` | **可选增强专属参考**：tkwebview 内嵌 WebView2 内核的轻量控件（纯 C 封装、无 pythonnet/pywebview、EXE 几乎零增量）；完整 API、重要限制（无事件回调/仅 Windows 二进制/焦点陷阱）、JS↔Python `bindjs` 双向调用、官方示例、打包注意（ctypes 加载的 DLL 需 `--collect-binaries`）；与 tkwebview2 取舍见 `03-ui-design.md` |

### 质量检查

- 无头控件级测试、pytest 组织、冒烟测试、交付门禁：`./references/09-testing-and-quality.md`
- **AI 真实 UI 自动化（tkinter-mcp-server，MCP 驱动真实事件环 + 多模态核验）**：
  `./references/16-tkinter-mcp-server.md`
- **GUI 行为回归（tkintertester，真实事件环内代码驱动、确定性、CI 友好）**：
  `./references/17-tkintertester.md`
- **TDD 方法论与冒烟体系**（Red-Green-Refactor / Prove-It / 测试金字塔 / 发布门禁）：
  `./references/14-tdd-methodology.md`
- GUI 冒烟脚本（无头驱动真实控件断言）：`./scripts/smoke_test_gui.py`（通用模板，覆写 `build_app()` 即用）
- **发布门禁编排器**（2 步硬门禁：pytest → 冒烟；外加 2 项 CI 建议项：导入检查 / 文档代码块语法检查，失败只告警不阻塞）：
  `./scripts/release_gate.py`
- **一键开发验证**（语法→导入→pytest→冒烟，驱动开发循环）：
  `./scripts/run_dev.py`

### 打包与交付

- Tkinter 专项打包指南（--windowed、Tcl/Tk 资源、图标、**版本信息注入**、单文件）：`./references/08-packaging.md`
- Windows EXE 构建脚本：`./scripts/build_windows_exe.ps1`
- 交付清单：`./docs/delivery-checklist.md`

### 参考实现（⭐ 第一优先：先看 examples，非必要不自造轮子）

> **[最高优先级] `examples/` 是本技能最重要的参考，没有之一。**
> 它不是「附属资料」，而是**可直接运行、可抠走复用的最低成本学习入口**——比任何 references 文档都更贴近「能跑的代码」。
> **铁律级要求**：在需求澄清、架构设计、界面设计、代码编写等**每一步**，**先到 `./examples/` 与 `examples/README.md` 翻一遍有没有能直接复用的技术，非必要不自造轮子。** 自造轮子前没翻过 examples，视为流程缺失。
>
> 本技能附带一组**可运行参考示例**——`idle/` `pygubu-designer/` `tkinter-designer/` `native-win32/` `thonny/` `bulk-image-processor/` `inventory-manager/`（每个都自带 `启动.bat` / `run.py`，双击即运行）。
> 每个示例都配有「可借鉴要点」（能直接抠走复用的零件 / 模式）。
> **完整清单、每个示例的「技术路线 + 可借鉴要点」统一见 `examples/README.md`**；该文件**末尾还集成了「真实案例研究」段**——10 个社区真实 Tkinter 应用（ERP / 进销存 / BI / 标杆型）的架构与反模式借鉴。即：**`examples/README.md` = 可运行示例 + 外部真实案例研究 的单一总入口**（本段不重复罗列细节，避免两处内容不一致）。

- **项目骨架（空白模板）**：`./templates/project-blueprints/tk-desktop-app/`（新建项目的起手脚手架）
- **⭐ 可运行参考示例 + 真实案例研究 · 总入口（必读）**：`examples/README.md`（每个示例自带 `启动.bat` / `run.py`，双击即运行；与本技能「标准库 vs 第三方，按需求取舍」框架互为印证）
- **示例目录**：`./examples/`

### 文档组织约定（写作/维护铁律）

**核心原则：SKILL.md 只放「主干」，具体内容一律下沉到 `references/`。**
- 本文件（SKILL.md）只承载**核心主干内容**：强制铁律、关键决策、工作流骨架、目录路由。
  任何「具体怎么做 / 为什么 / 踩了什么坑」的细节**都不写进本文件**，只保留一句**简练规则**
  + 指向具体参考文档的指针（如「详见 `references/08-packaging.md`」）。
- **非核心主干的具体内容，放到 `references/` 下对应的具体参考资料**：
  - 机制说明 / 配置命令 / opt-in 步骤 / how-to → 对应 `references/NN-*.md`
  - 执行中问题（现象 → 本质 → 解法）→ `docs/troubleshooting.md`
  - 术语解释 → `docs/glossary.md`
- **例外**：仅当内容涉及「特别重要的主干内容」（影响交付正确性的强制铁律、必须每次遵守的纪律），
  才允许以简练规则形式留在 SKILL.md，并附指针。

**三类文档的分工（避免重复、各司其职）**：
- `SKILL.md`（本文件）：主干铁律 / 决策 / 路由——**不展开细节**
- `references/*.md`：具体机制与 how-to（配置、opt-in、原理）——**细节的唯一归宿**
- `docs/troubleshooting.md`：排障记录（现象/本质/解决）；`docs/glossary.md`：术语

- 常见错误与解决方案：`./docs/troubleshooting.md`
- 术语解释：`./docs/glossary.md`

---

## 完整工作流（= 后续 AI 的最低执行清单）

> 按 ①→⑧ 顺序执行，不可跳过、不可乱序。
>
> **Win32 原生能力（ctypes / pywin32）是工作流的常用手段，不是点缀**：只要在某一步遇到 `ctypes/SKILL.md` §1 场景表里的任一诉求（高 DPI、任务栏图标、系统托盘、单实例、原生对话框、窗口置顶、GDI 绘制、注册表等），**tkinter 原生能解决的就用 tkinter；tkinter 确实做不到时，优先用轻量原生的 Win32 方案（ctypes / pywin32），避免引入高度复杂的框架**。**ctypes 是 Python 标准库自带的万能原生调用钥匙（零额外依赖、零打包负担，可直接 P/Invoke 任意原生 DLL、覆盖面极广）；pywin32 功能同样极其强大（54 模块、数百对象与常量，几乎覆盖全部 Windows API）**——二者都是弥补 tkinter 原生短板的首选武器，务必重视、优先掌握；详见 `ctypes/SKILL.md` 与 `pywin32/SKILL.md`（pywin32 全量文档 + tkinter 实战指南）。

```
用户说"帮我做个桌面工具"
  │
  ├─ 分支：新建项目 / 已有项目？
  │     ├─ 新建项目 → 走以下完整流程
  │     └─ 已有项目 → 跳过 ①-③，做结构合规检查（src 结构 / venv / MVC 分层 /
  │        主线程规则抽查）后进入 ⑤ 或 ⑥
  │
  ├─ ① 需求澄清（01-need-discovery.md）
  │    问清楚：做什么？输入输出？给谁用？单机还是联网？数据量多大？
  │    ▶ 产出：需求优先级表（MoSCoW 分级）+ 可测试验收标准
  │    ▶ 先扫一眼 `examples/README.md` 的示例清单，看需求是否贴近某个现成范本（仪表盘 / CRUD / 计费归集等）；有则直接借鉴、别从零定边界
  │
  ├─ ② 架构设计（02-architecture-mvc.md）
  │    定 MVP 边界 → 画模块分解 → 定 Model/View/Controller 边界与接口契约
  │    ▶ 产出：docs/architecture.md（模块分解 + 数据模型 + 界面地图）
  │    ▶ 架构选型前翻 `examples/`：`idle/`（大型应用架构）、`inventory-manager/`（中等复杂度业务系统）、`thonny/`（插件化 IDE 架构）——复用其分层与模式，不自造
  │
  ├─ ③ 项目初始化（bootstrap_project.ps1 + 07-project-structure.md）
  │    生成 src 结构（遵守 07 的 src 结构 / 入口规范 / 路径适配）+ venv + pyproject.toml + MVC 骨架
  │    ▶ 产出：可运行的空壳窗口（python -m app 弹出主窗口）；骨架已含 `启动.bat` + `src/launcher.py`，双击即用
  │    ⚠ 逐文件 Write，禁单条巨命令堆文件
  │
  ├─ ④ 数据层（06-data-layer-sqlite.md）
  │    schema DDL → Repository → 种子数据 → 单元测试（纯逻辑，不碰 GUI）
  │    ▶ 产出：models/ + tests/test_models_*.py 全绿
  │
  ├─ ⑤ 界面设计（03-ui-design.md + 04-widgets-and-patterns.md + `pygubu/`）
  │    先搭静态布局（假数据）→ 无头冒烟确认控件树 → 再接真数据
  │    ▶ 产出：views/ 各页面 + 布局审查通过
  │    ▶ 先到 `examples/` 找同类界面的成熟实现（如 `idle/` 的大型应用控件库、`inventory-manager/` 的业务系统 CRUD + 搜索过滤），抠走可复用零件
  │    ▶ 界面默认走 pygubu（见下方 ★，唯一默认）；第三方增强（按需）：要更现代外观查 13-tksheet，要画实时折线图查 10-tkchart（选型与取舍见 03 §1 / §6.4）
  │    ▶ 社区实战借鉴与反模式警示统一见 `examples/README.md` 末尾「真实案例研究」段（ERP / BI / 标杆型外部应用）
  │
  │    ★ 界面设计（**唯一默认**，pygubu 路线）：界面一律以 `.ui` 定义；由 AI 后台接管时
  │      走 pygubu 闭环——全程 AI 执行命令，人不必打开设计器。
  │      完整闭环、`.ui` 语法坑、命令清单、Builder API、打包要点见唯一的 **`pygubu/`（子技能）§1**；
  │      配套脚本在 `scripts/ai-ui-design/`（check_ui.py / check_ui_visual.py / app.py）。
  │
  ├─ ⑥ 编码集成（02-architecture-mvc.md + 05-threading-and-async.md）
  │    Controller 接线：事件 → Model → 刷新 View；耗时操作走线程 + queue
  │    ▶ 测试驱动：业务逻辑先写失败测试再实现；bug 修复先写复现测试
  │    ▶ 写具体控件/模式前，先查 `examples/` 有无同款可抄的零件（Treeview 封装、模态对话框、Canvas 图表、DPI 感知、任务栏图标等），直接复用高于自造
  │    ▶ **每次改完跑一键验证**：`python scripts/run_dev.py --fast`（语法+导入，~4s）
  │       或完整版 `python scripts/run_dev.py`（含 pytest + 冒烟，~30s）
  │       全绿后才进入下一步
  │
  ├─ ⑦ 运行验证（09-testing-and-quality.md + 16-tdd-methodology.md）
  │    ▶ **先跑发布门禁**：`python scripts/release_gate.py`（或 `python scripts/run_dev.py --gate`）
  │    ▶ pytest 全绿 → 无头 GUI 冒烟（scripts/smoke_test_gui.py）→ GUI 行为回归（tkintertester，真实事件环内确定性跑 GUI 序列、捕获 Tk 吞掉的回调异常，见 22-）→ AI 真实弹窗自测
  │    （由 AI 自行驱动，不可转交用户；源码态优先 tkinter-mcp-server，见 21-；
  │    EXE 态用 pywinauto / 窗口探测）（正常 + 异常路径）→ 中文/DPI/缩放检查
  │    ▶ 深层 L1–L5 业务正确性（数据驱动/功能/业务流程/E2E/验收，见 09 §5）PR 前必跑
  │    ▶ 确认零错误、可交付后，才进入 ⑧ 打包
  │    ▶ 产出：pytest 报告 + 冒烟记录
  │
  └─ ⑧ 打包交付（08-packaging.md + build_windows_exe.ps1 + delivery-checklist.md）
      最小 venv → pytest 门禁 → PyInstaller --onefile --windowed → EXE 冒烟
      （启动进程 → 等窗口出现 → 正常退出）→ 填交付清单
      ▶ 深层 E2E / L5 优先在源码态用 tkinter-mcp-server 验证（见 21-）；
        EXE 冒烟保"能启动 + 能渲染"底线
      ▶ 若界面引入了第三方增强库（10-tkchart / 13-tksheet / pygubu 任一），须额外按该参考的 PyInstaller 小节
        补 hidden-import / --add-data（依赖与体积见各参考；tkchart 纯 tkinter 增量≈0，通常无需 hidden-import）
      ▶ 产出：dist/*.exe + 一键启动脚本（启动.bat / run.py）+ README + 交付清单
```

### 各步骤产出物清单

| 步骤 | 产出物 | 验收标准 |
| ---- | ------ | -------- |
| ① 需求澄清 | 需求优先级表 | MoSCoW 已分级，MVP 已确认 |
| ② 架构设计 | `docs/architecture.md` | 模块分解 + 数据模型 + 界面地图齐备 |
| ③ 项目初始化 | 骨架 + `.venv` | 空壳窗口可弹出 |
| ④ 数据层 | `models/` + 测试 | pytest 全绿，无 GUI 依赖 |
| ⑤ 界面设计 | `views/` | 无头冒烟通过，布局无重叠/塌陷 |
| ⑥ 编码集成 | `controllers/` + 测试 | 语法/导入/pytest 全绿 |
| ⑦ 运行验证 | 冒烟记录 | 无头 GUI 冒烟 + tkintertester GUI 行为回归 + AI 真实弹窗自测 三通过 |
| ⑧ 打包交付 | `dist/*.exe` + `启动.bat` + README + 清单 | EXE 冒烟 + 一键启动通过，双击可用 |

---

## 必须遵守的铁律（最高优先级）

### 环境与初始化

- **必须创建最小 venv**：项目目录创建后立即 `python -m venv .venv`。Tkinter 随
  CPython 自带不需要装，但业务依赖与 PyInstaller 必须隔离，否则打包体积失控
- **必须先有骨架再写代码**：跑 `bootstrap_project.ps1` 生成骨架，骨架落地前禁止写业务 .py
- **构建期工具（PyInstaller）严禁进运行时依赖**：装进独立打包 venv 或用
  `--group build`，不进 `[project.dependencies]`

### 编码

- **主线程规则（最高铁律）**：所有 widget 创建/读写只能发生在创建 `Tk()` 的线程。
  子线程只能把结果放进 `queue.Queue`，由主线程 `after()` 轮询消费。违反的典型症状：
  偶发 `RuntimeError: main thread is not in main loop`、静默崩溃、界面冻结
- **ttk 优先**：一律用 `ttk.Button/Label/Entry/...`，不用经典 `tk.*` 控件
  （除 `tk.Text`、`tk.Canvas`、`tk.Toplevel`、`tk.Menu` 这些无 ttk 版的）。
  样式定制走 `ttk.Style`，禁止给 ttk 控件传 `bg/fg/font` 之外它不支持的经典选项
- **grid 必设权重**：任何可缩放容器必须 `rowconfigure/columnconfigure(weight=...)`，
  否则窗口拉大后内容不跟随（最常见布局 bug）
- **变量绑定用 tk 变量类**：表单值用 `StringVar/IntVar/BooleanVar`，禁止直接
  `entry.get()` 满天飞；变量对象必须保持引用（局部变量被 GC 后 trace 失效）
- **PhotoImage 必须保持引用**：`label.image = img` 或存实例属性，否则图片显示空白
- **路径适配必须用 `sys.frozen` 检测**：
  `BASE_DIR = Path(sys.executable).parent if getattr(sys, 'frozen', False) else Path(__file__).resolve().parent.parent`
- **DPI 感知在创建 Tk() 之前设置**：
  `ctypes.windll.shcore.SetProcessDpiAwareness(1)`（详见 03-ui-design.md）

### 质量

- **一键开发验证门禁**：每次改码后必须运行 `python scripts/run_dev.py --fast`（语法+导入），
  提 PR 前跑 `python scripts/release_gate.py`（硬门禁 pytest + 冒烟，外加 CI 建议项：导入检查 / 文档代码块语法检查），禁止跳过硬门禁
- **语法检查门禁**：写入任何 .py 后立即 `py_compile` + 包导入测试，禁止跳过
- **编码门禁**：.py 一律 UTF-8 无 BOM；禁止 PowerShell `Set-Content` 写源码
- **逻辑测试与 GUI 测试分离**：Model 层测试禁止 import tkinter；GUI 冒烟用
  `scripts/smoke_test_gui.py` 无头驱动（`root.withdraw()` + `update()`），不进 mainloop
- **冒烟测试门禁（不可跳过）**：打包后必须启动 EXE、确认窗口类存在、正常退出。
  严禁让用户代为测试

### Win32 原生能力（强制）

- **6 条强制规则（argtypes/restype、wintypes 缺失、GDI 归属、回调 GC、句柄配对、Unicode W 后缀）**：完整规则与类型速查见 `ctypes/SKILL.md` §强制规则（含 64 位溢出防护、结构体手动定义、回调全局引用等细节）。**这 6 条规则全部围绕 ctypes 展开——它是本技能 Win32 集成强制纪律的核心载体：标准库自带、零打包负担，可直接 P/Invoke 任意原生 DLL、覆盖面极广，务必重视、优先掌握。**
- **tkinter 应用需要 Win32 的场景（允许直接用 tkinter 原生用法）**：高 DPI 感知（必须在 Tk() 前）、任务栏图标替换、
  单实例锁定、系统托盘、原生文件对话框、窗口置顶、屏幕取色、GDI 绘制、注册表操作等 → 见 `ctypes/SKILL.md` §1 场景表与 §3 互操作模式，以及 `pywin32/SKILL.md`（**pywin32 全量离线文档 + 在 tkinter 中调用 pywin32 拼装原生 UI 的实战指南**；① **⭐ ctypes 是 Python 标准库自带的万能原生调用钥匙**，零额外依赖、零打包负担，可直接 P/Invoke 任意原生 DLL、覆盖面极广，是本技能 Win32 强制规则的核心载体，务必重视、优先掌握；② **⭐ pywin32 是 Windows 桌面开发最强大、最完整的原生能力宝库**，封装 54 个模块、数百对象与常量，几乎覆盖全部 Windows API，务必重视、优先掌握）。**这些场景允许直接使用 tkinter 原生用法实现；优先选轻量、原生的方案（ctypes / pywin32），尽量避免引入高度复杂的框架。**
- **Win32 调用两条合法路径，ctypes 与 pywin32 都鼓励**：① 标准库 `ctypes` 直接 P/Invoke（低层 DLL 调用、DPI 感知、自定义窗口过程、GDI 等，**⭐ ctypes 是标准库自带、零打包负担的万能原生调用钥匙，覆盖面极广，务必重视、优先掌握**，遵循 `ctypes/SKILL.md` 强制规则）；② `pywin32`（`win32gui`/`win32api`/`win32con`/`win32ui`）用于更对象化的封装（任务栏图标、系统托盘、窗口枚举、消息框等，**⭐ 同样极其强大**）。两条路都合法、都鼓励；按任务选顺手的那条。**tkinter 原生、ctypes、pywin32、Python 标准库都属于推荐用法**；需要原生能力时优先用它们即可，无需为"原生"而引入高度复杂的第三方框架。无论哪条都要遵守 `ctypes/SKILL.md` 的句柄/签名纪律。
- **原生窗口示例**：`examples/native-win32/calculator.py`（纯 Win32 API 计算器，可直接运行参考）

### 打包

- **必须 `--onefile --windowed`**：GUI 应用禁止带控制台黑框（`--console` 仅限调试版）。
  验收标准：`dist/` 下无 `_internal/` 目录
- **必须交付一键启动脚本**：项目根目录 `启动.bat`（调用 `src/launcher.py`，优先 pythonw 无黑框）+ `run.py`，让用户双击即用；构建骨架（`bootstrap_project.ps1`）已自动生成，禁止删除
- **`启动.bat` 编码铁律**：含中文的 .bat 必须 **GBK(CP936/ANSI 中文) + CRLF + 无 BOM**，开头加
  `chcp 65001 >nul` + `set PYTHONUTF8=1`；纯 ASCII 的 .bat 可 UTF-8 无 BOM。两条红线：
  **禁 UTF-8 带 BOM**（首行 `@echo off` 变 `锘緻echo off` 报错）、**禁仅 LF 换行**
  （`>`/`=` 被当换行、命令拆成碎片）。完整现象/本质/解法见 `docs/troubleshooting.md`
  打包节「启动.bat 中文乱码 / 命令被拆成碎片」；参考实现：`examples/idle/启动.bat`、
  `examples/thonny/启动.bat`。
- **--windowed 下 print 会炸**：无控制台时 `sys.stdout` 为 None，所有诊断输出走
  logging 文件日志；顶层必须有 excepthook 把未捕获异常写日志 + messagebox 提示
- **Tcl/Tk 资源由 PyInstaller 自动收集**：不需要手动 --add-data tcl；但若用了
  第三方主题（.tcl 文件）或图标资源，必须显式 --add-data 并用 sys._MEIPASS 取
- **任务栏图标要 AppUserModelID**：`ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("company.app")`
  否则任务栏显示 Python 默认图标（详见 08-packaging.md）
- **pygubu 打包（默认剔除 PIL 与第三方插件）**：核心 `pygubu` 必须 `--hidden-import=pygubu`（运行期加载 `.ui` 必需）；默认排除 PIL / ttkwidgets / customtkinter，严禁引入 pygubudesigner（设计器依赖链死重）。完整命令与机制见 `pygubu/`（子技能）§11 与 `references/08-packaging.md`。
- **HTTPS 走标准库 `ssl`，默认排除 `cryptography`（~27% 死重）**：默认
  `--exclude-module=cryptography` + `--exclude-module=bcrypt`（bcrypt 仅为 cryptography 依赖）；
  `libcrypto`/`libssl` 仍随标准库 `_ssl` 保留、TLS 正常。未来真做自签证书/加解密时删排除并补
  `--hidden-import=cryptography`（默认关、不禁止）。现象/本质/机制见 `docs/troubleshooting.md`
  打包节「cryptography 被静默拖入 EXE」与 `references/08-packaging.md`「默认排除 cryptography」。
- **版本信息注入**：交付 EXE 应带 `version_info.txt`（右键属性→详细信息），由 build 脚本
  `-VersionFile`（`--version-file`）注入；版本号与 `pyproject`/`CHANGELOG` 同步
  （`version_info.txt` / `build_info.json` / `__version__` 三者一致，详见 08-packaging.md）

### 命令执行与超时（防 120s 卡死）

- **禁止用单条 shell 命令批量造文件**：源码/配置逐文件用 Write/Edit 工具
- **PyInstaller 构建必带大 timeout（>=600s）或后台运行**：--onefile 构建常 >120s
- **失败即拆步**：命令超时就拆成更小步骤，不要重试同一条巨命令

---

## 命令代执行规则

- 涉及 venv 创建、pip/uv、pytest、pyinstaller 时，默认由 AI 发起，不转手给用户
- 中国网络环境下，包安装默认先配置镜像（清华/阿里）
- 用户问"怎么打包成 exe"时，默认理解为"请 AI 帮我打包并验证产物"

## 代码与结构原则

- 新项目使用 `src` 结构，MVC 目录：`models/`、`views/`、`controllers/`、`common/`
- 业务逻辑（Model）零 tkinter 依赖——这是可测试性的根基
- 默认补齐类型注解、logging 文件日志、错误提示、`.gitignore`、README
- 日志按日期分文件、保留最近 30 天
- 单文件超过 500 行主动拆分；一个 View 类只管一个页面/Tab
