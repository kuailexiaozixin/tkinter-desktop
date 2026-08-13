# CHANGELOG

## 1.7.25 (2026-08-03)
- **发布门禁瘦身 + pywinauto 回退段硬化验证循环纪律（形式审查减重约 40%）**。
  - `scripts/release_gate.py`：门禁从「4 步全 REQUIRED」精简为「2 步硬门禁（pytest + 无头 GUI 冒烟，REQUIRED 失败即非零退出）+ 2 项 CI 建议项（verify_imports / check_refs，ADVISORY，失败只告警不阻塞）」。`verify_imports` 由 `find_spec` 的 FAIL 降级为 WARNING（与 pytest+smoke 实际导入重复，不再阻塞）；`check_refs`（仅 `compile` 语法、不执行）维持 WARNING。`run()` 拆为硬门禁段与 CI 建议段两段输出，`--advisory-only` 可只跑建议项；更新模块 docstring 与退出码说明。实质防护未丢（逻辑 + 控件级仍每次必跑），形式审查负担降约 40%。
  - `references/09-testing-and-quality.md`：
    - 合并独立「§3 集成测试」节入 §2 无头 GUI 冒烟（复杂 Controller 的「建 Tk 实例 + `:memory:` DB」集成用例直接走 pytest，用 fixture 保证 `destroy()`），测试金字塔同步去掉独立集成层；原「集成测试」节不再单列。
    - §5.4 pywinauto 备选模板移植 windows-ui-controller 的「每步操作后扫描验证 + 截图纠错 + 智能缓存」验证循环纪律，并标注其与 tkinter-mcp-server 的 `get_ui_layout()`（读控件树）+ `view_application()`（截图核验）是同一套"先读后断、逐步验证"思路——这是唯一可移植的 SOP 模式，硬化了 EXE 态 pywinauto 回退段，不引入 WPF/WinForms/Qt 等无关主题。
  - SKILL.md：「发布门禁编排器」与提 PR 前门禁措辞由「4 步检查 / 完整 4 步门禁」改为「2 步硬门禁 + 2 项 CI 建议项」。

## 1.7.24 (2026-08-03)
- **新增 GUI 行为回归层：tkintertester（真实事件环内代码驱动、确定性、CI 友好）**。
  - 新建 `references/22-tkintertester.md`：澄清它是什么（event-loop-native、step 函数经 `root.after()` 调度、测试间 `entry()`/`reset()` 隔离）、与 `09` 既有无头冒烟 / `21` tkinter-mcp-server / pytest / pywinauto 的定位关系、安装（`pip install tkintertester`，并标注 tuna 镜像 build-isolation 缺 `setuptools>=61` 的坑、需 `--index-url https://pypi.org/simple`）、API 表（**已对照本机安装源码 `tkintertester/harness.py` 逐条核实 0.1.0 签名**：`run_host/attach_harness/add_test/set_timeout/set_resetfn/quit/get_results/print_results/write_results/show_results`）、step 契约、`harness.g`/`harness.tests` 全局态、①–⑧ 工作流融入、接入结构约束、counter 与业务流示例、局限。
  - **实测验证**：本机 `pip install` 成功（0.1.0）；跑官方 counter 范例 **2/2 成功**；专门验证其"捕获 Tk 静默吞掉的回调异常"卖点——按钮 `command=` 里 `raise RuntimeError` 被记为 `status:"fail"` + `fail_message:"Tk callback exception: ..."` + 完整 traceback。
  - **文档优于实测的更正**：上游 `docs/reference.md` 列了 `get_root()`，但 0.1.0 实测**该函数不存在**（取 root 用 `harness.g["root"]`），文档已据此标注。
  - `references/09-testing-and-quality.md` 同步：§2 无头冒烟尾注指向 22（"进真实事件环 + 捕获吞掉的异常"的回归）；新增 §8「tkintertester：真实事件环 GUI 行为回归（Track 2）」含五手段定位表 + two-track 落地建议（`tests/` pytest 逻辑层 + `guitests/` tkintertester GUI 层）。
  - SKILL.md 同步：质量检查清单加 22 引用；阶段 ⑦ 运行验证序列在"无头 GUI 冒烟"与"AI 真实弹窗自测"间插入"GUI 行为回归（tkintertester，见 22-）"；产出物表 ⑦ 行改为"无头 GUI 冒烟 + tkintertester GUI 行为回归 + AI 真实弹窗自测 三通过"。
  - 定位清晰：tkintertester = **开发者写代码、确定性、CI 可重复**的 GUI 回归，补"无头冒烟绕过真实事件环"的盲区（漏掉 Tk 吞掉的回调异常 + 时序/after 行为）；不替代 `21` 的 AI 多模态验收，二者在同一项目内分层共存。

## 1.7.23 (2026-08-03)
- **测试体系升级：从"浅层能跑通"到"业务对" + 引入 tkinter-mcp-server 真实 UI 自动化**。
  - `references/09-testing-and-quality.md` 新增 §5 深度测试框架（L1 数据驱动 / L2 功能 / L3 业务流程 / L4 E2E+UI 自动化 / L5 用户验收回溯，L1–L5 与既有浅层金字塔叠加）与 §6 深度测试金字塔；§5.4 明确"真实 UI 自动化优先 tkinter-mcp-server、pywinauto 备选"并给出 MCP 模板在前；§7 厘清深度测试是"发布/重大 bug 修复前必经"并列出产出物（测试用例 + pytest 报告/截图/验收矩阵）。
  - 新建 `references/21-tkinter-mcp-server.md`：工具能力表（已对照本机已安装源码逐条核对，共 16 个工具及签名）、安装注册、工作原理、在 ①⑤⑦⑧ 工作流的融入、局限、§7 验收会话示例（参数名已校正为 `script_path=` / `widget_id=` / `text=`）。
  - SKILL.md 同步：质量检查清单加 21 引用；阶段 ⑦ 改"真实弹窗自测"为"AI 真实弹窗自测（由 AI 驱动、不可转交用户；源码态优先 tkinter-mcp-server）"并补深层 L1–L5 必经说明；阶段 ⑧ 补"深层 E2E 优先源码态用 MCP、EXE 冒烟保启动底线"；产出物表对应更新。
  - 已将 `tkinter-mcp-server` 写入 `~/.workbuddy/mcp.json` 并启用（用 entry-point 全路径规避 PATH 歧义），实测 `mcp` 客户端拉起 server 成功、`list_tools()` 返回 16 个工具、签名与文档一致、`is_connected`/`get_ui_layout` 调用通路正常。
  - 说明：本批编辑落在 Roaming 权威路径 `C:\Users\17151\AppData\Roaming\WPS 灵犀\serverdir\user_skills\tkinter-desktop`；工作区镜像 `D:\WorkBuddy工作空间\...\tkinter-desktop` 为冗余副本，其上的同名编辑无效、以本路径为准。

## 1.7.22 (2026-08-03)
- **恢复案例研究里被二次误删的 matplotlib 事实引用**。
  - **根因**：1.7.20 把用户「除了 matplotlib 库以外，对其他库的引用也要恢复」解读为「matplotlib 维持剔除、其余库恢复」，导致案例里的 matplotlib 被二次清除——但事实上这些真实项目**确实用了 matplotlib**（Grocery Mart PyPI 含 matplotlib；SIMPLY 用 FigureCanvasTkAgg 画仪表盘；Sales Data Analyzer / HR Analytics / Interactive Sales 均用 matplotlib/seaborn）。
  - **修正**：按用户「案例引用是事实、务必保留」的一贯原则，把 matplotlib 恢复到 `examples/README.md` 案例段——矩阵 2/3/4/5/6/7 图表列、案例 2/3/5/6/7 技术栈与可借鉴点、案例 6 的 `FigureCanvasTkAgg` 嵌图代码、横向结论第 2/3 条；`20-tkinter-toolkit.md` 打包提示两处 `(pandas 等)` 还原为 `(pandas/matplotlib 等)`。案例 6 技术栈保留 `Pandas + Matplotlib + SciPy`（matplotlib 出图 + scipy.stats 统计，二者都真用）。
  - **立场边界（澄清）**：`03-ui-design.md` 的 matplotlib 教程小节仍保持删除（那是「技能不把 matplotlib 当推荐覆盖库」的立场）；但案例作为对真实项目的**事实描述**，其 matplotlib 引用与技能立场互不冲突，必须保留。即「技能正文覆盖立场」与「案例事实引用」是两件事，案例中用了什么就写什么。

## 1.7.21 (2026-08-03)
- `references/20-tkinter-toolkit.md` 补全为上游 Tkinter-Toolkit `database.json` 的**全量目录**（74 条，剔除本技能不覆盖的 tkinterweb）；每条新增「框架」标注（原生 ttk / CustomTkinter / 平台(Win32) / 工具），并据本技能「优先原生 ttk」立场补充使用原则与 CustomTkinter 引入代价提示；SKILL.md Layer3 行同步更新为「全量」描述。

## 1.7.20 (2026-08-03)

- **补全此前误删/误改的库引用（保留 matplotlib 不覆盖立场）**：基于真实仓库/PyPI 实测复查三个 BI 案例与 Grocery Mart 的真实技术栈，修正 `examples/README.md`（合并的「真实案例研究」段）与 `references/20-tkinter-toolkit.md`：
  - **移除所有 matplotlib 引用**（技能不把 matplotlib 当作推荐覆盖库，案例里仅作「图表控件由你选用的图表库提供，本技能不展开」处理）：技术栈矩阵 5/6/7 行的 `Matplotlib/Seaborn` 改为 `—`（5、7）/`SciPy`（6）；案例 3/6/7 正文与「可借鉴点」中的 `matplotlib`/`FigureCanvasTkAgg` 全部删除；案例 6 代码回退为库无关的 `clear_frame()` + `embed_chart(chart_widget)` 模式；横向结论第 2/3 条与「与默认栈的关系」段去掉 matplotlib。
  - **恢复被误删的非 matplotlib 库**：案例 6 技术栈在 1.7.17 中被错把 **SciPy** 换成 `Matplotlib/Seaborn`——已还原为 `Pandas + SciPy`（其代码本身调用 `scipy.stats.skew`）；矩阵 5/6/7 行的非图表库 `SciPy` 保留。Grocery Mart 的 `pandas / openpyxl / fpdf2`（另有 numpy/ttkbootstrap）保持完整；案例 3 的 `PIL`/`numpy`、案例 7 的 `ttkbootstrap` 等均保留。
  - `20-tkinter-toolkit.md` 两处「带重依赖（pandas/matplotlib 等）」改为「（pandas 等）」，保留 pandas 指代。
  - 验证：grep 确认两文件已无 `matplotlib`/`FigureCanvasTkAgg`/`Seaborn` 残留；SQLAlchemy/Pandas/SciPy/openpyxl/fpdf2/numpy/ttkbootstrap/PIL/ttkthemes/tkcalendar 等非 matplotlib 库引用完整。

## 1.7.19 (2026-08-03)

- **为三份资料补齐编号并强调地位**：
  - `references/official-docs/` → **`11-official-docs/`**，在 SKILL.md 的 HARD-GATE 与 Layer 1 表强调其「核心地位 / 首要地位」（权威性最高、优先级最高的首要参考，任何控件/API 疑问一律先查它）。
  - `references/moore-tkinter-2e-index.md` → **`14-moore-tkinter-2e-index.md`**，在 Layer 1 表强调其「重要参考价值」（技能正文未覆盖的工程化主题优先查此索引）。
  - `references/tkdocs-tutorial/` → **`18-tkdocs-tutorial/`**，补齐编号 18。
  - 同步更新 SKILL.md、04-widgets-and-patterns.md、14-moore 内部链接、18-tkdocs README 内部链接的全部相对/绝对路径引用。

## 1.7.18 (2026-08-03)

- **合并 SKILL.md 中重复的「Win32 原生能力」段落**：原 SKILL.md 在「参考实现/质量检查」段末（旧第 175 行「### Win32 原生能力（强制规则）」）与「工作流硬要求」段内（旧第 369 行「### Win32 原生能力（强制）」）两处都在讲同一套 ctypes ⭐ + pywin32 ⭐ 的 Win32 原生能力，内容重复。删除前者，保留后者为唯一说明，并把前者独有的 `examples/native-win32/calculator.py` 原生示例指针并入保留段。现全文件仅存一处 Win32 原生能力说明。

## 1.7.17 (2026-08-03)

- **恢复案例研究与控件目录中的「真实库引用」（修正 1.7.15 误删）**：用户明确——案例（真实应用）里描述项目实际用了哪些库（matplotlib / pandas 等）是**事实性、必要的**，不应误删；删的是「技能把 matplotlib 当推荐库来覆盖」，而非「案例里提到真实项目用 matplotlib」。
  - `examples/README.md`（即 1.7.16 并入的「真实案例研究」段）：还原 matplotlib 事实引用——① 顶部「与默认栈关系」加回 `/ matplotlib`；② 技术栈矩阵第 5/6/7 行「分析/图表」列还原 `Matplotlib / Seaborn`、`Matplotlib / SciPy`；③ 案例 3 技术栈与可借鉴点还原 `matplotlib(FigureCanvasTkAgg)` 画仪表盘；④ 案例 6 技术栈还原 `Pandas + Matplotlib/Seaborn`、代码摘录还原 `FigureCanvasTkAgg(fig, master)` 嵌图写法、可借鉴点还原 `clear_frame() + FigureCanvasTkAgg...draw()` 标准模板；⑤ 案例 7 技术栈与可借鉴点还原 `Matplotlib/Seaborn` 与 `FigureCanvasTkAgg 嵌图`；⑥ 横向结论第 2/3 条还原 `pandas/matplotlib 后端`、`/ matplotlib`。
  - `references/20-tkinter-toolkit.md`：两处「带重依赖（pandas 等）」还原为「（pandas/matplotlib 等）」（描述重依赖库体积增量，属正常表述）。
  - **未动** `references/03-ui-design.md` 的 matplotlib 小节删除（那是「技能不把 matplotlib 作为推荐覆盖库」的立场，与「案例描述真实项目用 matplotlib」是两回事，互不影响）。

## 1.7.16 (2026-08-03)

- **合并 `references/11-case-studies.md` 进 `examples/README.md` 末尾，并强化 examples 的优先性**：
  - 将「真实案例研究」整段（标题降一级：H1→H2、H2→H3、H3→H4）并入 `examples/README.md` 末尾，作为外部社区真实应用（ERP / 进销存 / BI / 标杆型）的架构与反模式参考；并在段首加「与上面 vendored 可运行示例的区别」提示。
  - 原 `references/11-case-studies.md` 移入 `references/_archive/` 归档（非删除，避免两处内容不一致）。
  - SKILL.md：① Layer 3 表删除 `references/11-case-studies.md` 行（内容已并入 examples/README.md）；② 工作流⑤指针由 `11-case-studies` 改为指向 `examples/README.md` 末尾「真实案例研究」段；③ 「参考实现」段升级为**最高优先级**强调——`examples/` 是本技能最重要的参考、「非必要不自造轮子、自造前没翻 examples 视为流程缺失」，并明确 `examples/README.md` = 可运行示例 + 外部真实案例研究 的单一总入口。
  - `references/06-data-layer-sqlite.md` 顶部 SQLAlchemy 引用由 `11-case-studies.md` 改为 `examples/README.md` 末尾「真实案例研究」案例 1。
  - 未触碰：CHANGELOG 历史条目（不改历史）。

## 1.7.15 (2026-08-03)

- **移除 `tkinterweb` 与 `matplotlib` 两个库的话题覆盖（不再作为技能推荐/覆盖的第三方库）**：
  - `references/03-ui-design.md`：删除决策框架表「C 架构切换 / tkinterweb」整行；删除 §10 下 `### tkinterweb（内嵌 HTML / 富文本）` 小节（其 WebView 嵌入场景已由 `references/17-tkwebview.md` 的 tkwebview2/tkwebview 覆盖）；删除 `### matplotlib（tkinter backend 画专业图表）` 小节（含 TkAgg 嵌入示例与 +25~40MB 打包说明）。
  - `references/17-tkwebview.md`：引入场景/不引入两处「用 ttk/Canvas 即可」去掉 matplotlib 举例。
  - `references/20-tkinter-toolkit.md`：两处「带重依赖（pandas/matplotlib 等）」改为「（pandas 等）」。
  - `references/11-case-studies.md`：矩阵、技术栈句、二类标题、横向结论中移除 matplotlib 表述；案例 6 代码摘录由 matplotlib `FigureCanvasTkAgg` 改写为库无关的 `clear_frame()` + `embed_chart(chart_widget)` 模式；其余案例的 matplotlib 依赖描述一并去除，案例仍作为真实架构参考保留。
  - 未触碰：`examples/` 内 Thonny/pygubu 等 vendored 上游源码、`references/moore-tkinter-2e-index.md`（外部书目的目录索引，非技能覆盖）、CHANGELOG 历史条目（不改历史）。

## 1.7.11 (2026-08-03)

- **合并 `references/16-pygubu.md` 与 `references/17-ai-ui-design.md` 为单一文档**：技能面向 LLM、无人工介入，故把「pygubu 工具本体参考」与「AI 自动化 UI 设计工作流」融合成**一条单一闭环**（写 `.ui` → 无头校验 `check_ui.py` → 运行期加载 → 视觉截图校验 `check_ui_visual.py` → 交付），**取消所有分支**（删除「人用设计器 / AI 后台」两条路径、删除「经典 .ui / 生成代码」双工作流、删除「与手搓 ttk 二选一」）。原 17 移入 `references/_archive/` 保留（非删除）。同步更新 SKILL.md Layer 3 表、工作流⑤指针、第 33 行、以及 `examples/pygubu-designer/README.md` 的引用。
- **补充 tkwebview2 / tkwebview 实测体积数据**（`references/03-ui-design.md` tkinterweb 节后新增小节）：本机 PyInstaller `--onefile --windowed --noupx` / Python 3.13.14 实测——基线 9.90MB；tkwebview2 引入后 15.86MB（**+6MB**，拉入 pythonnet+pywebview）；tkwebview 引入后 10.06MB（**+0.2MB**，纯 C 封装无重依赖）。二者均依赖系统级 WebView2 Runtime（不进 EXE）。

## 1.7.12 (2026-08-03)

- **新增 `references/17-tkwebview.md`**（tkwebview 内嵌 WebView2 内核轻量控件专属参考）：综合官方 PyPI（https://pypi.org/project/tkwebview/）与 GitHub（https://github.com/Smart-Space/tkwebview）整理，含定位/引入场景/重要限制（无事件回调·仅 Windows 二进制·Windows 焦点陷阱）/完整 API 清单/`bindjs` 的 JS↔Python 双向调用/官方 `test.py` 整理示例/打包注意（ctypes 加载的 DLL 需 `--collect-binaries`，否则运行期缺 DLL）/与 tkwebview2 取舍。同步：① `03-ui-design.md` 修正原错误归属（tkwebview 作者应为 **Smart-Space**，非 Rumia-Channel）并交叉引用 17；② SKILL.md Layer 3 表新增 17 行索引。

## 1.7.13 (2026-08-03)

- **合并 `references/14-tkinter-pywin32.md` 进 `references/13-pywin32/README.md`**：把「在 tkinter 中调用 pywin32 构建原生 UI」实战指南（内嵌原生控件 / 系统对话框 / 通知区 / COM 自动化 / ActiveX，各片段 Python 3.13 + pywin32 实测）并入 pywin32 全量离线文档 README，使其成为**「全量文档索引 + tkinter 实战指南」二合一**的单一入口；内部相对链接已修正为从 `13-pywin32/` 目录解析。原 14 移入 `references/_archive/` 保留（非删除）。同步更新 SKILL.md 全部 3 处引用（Win32 参考块、工作流硬要求段、场景段）指向 `13-pywin32/README.md`。
- **在 SKILL.md 强调 pywin32 的强大与重要性**：Win32 参考块、工作流硬要求段、场景段三处均新增措辞——pywin32 是 Windows 桌面开发**最强大、最完整的原生能力宝库**，封装 **54 个模块、数百对象与常量**，几乎覆盖全部 Windows API（窗口/控件/GDI/系统托盘/通用对话框/COM 自动化/ActiveX/注册表/服务/网络/安全等），是弥补 tkinter 原生短板、把程序提升到「专业 Windows 应用」级别的首选武器，**务必重视、优先掌握**。

## 1.7.14 (2026-08-03)

- **移动 `references/18-win32-native.md` 至 `references/12-ctypes/README.md`（更名）**：原 18「Win32 原生能力集成（强制规则）」整体并入 `12-ctypes/` 目录成为其总入口 README（内部相对链接已修正为从 `12-ctypes/` 解析：子文件链接去前缀、Petzold PDF 与 `05-threading` 改 `../`）；原 18 移入 `references/_archive/` 保留（非删除）。同步更新 SKILL.md（Win32 参考块 / 工作流硬要求段 / 场景段三处共 6 个引用）、`examples/README.md`、`examples/native-win32/README.md`、`references/04-widgets-and-patterns.md`、`references/17-tkwebview.md` 全部指向 `12-ctypes/README.md`。CHANGELOG 历史条目保留旧路径（不改历史）。
- **在 SKILL.md 强调 ctypes 的强大与重要性（与 pywin32 对等）**：Win32 参考块将 ctypes 提为 ⭐ 条目——「Python 标准库自带的『万能原生调用钥匙』，零额外依赖、零打包负担，可直接 P/Invoke 任意原生 DLL（kernel32/user32/gdi32/comdlg32/shcore… 及任意第三方 C 库），覆盖面与 pywin32 同样广」；工作流硬要求段、场景段（6 条强制规则、双路径段）均补「ctypes 是标准库自带、零打包负担的万能原生调用钥匙、务必重视优先掌握」的强调；明确 6 条 Win32 强制规则全部围绕 ctypes 展开、是其核心载体。

## 1.7.10 (2026-08-02)

在开发中反复实测核实、修正 4 处参考文档论断（均经本机 Python 3.13.14 实测与无头 `Tk()` 核实）：

- **修正 `references/14-tkinter-pywin32.md` §3.5 子类化片段**：① `WNDPROC` 原用 `w.LRESULT`，但
  `ctypes.wintypes` 无 `LRESULT`（已核实），改为 `ctypes.c_int64`；② 原片段未声明 `SetWindowLongPtrW`
  的 `argtypes`/`restype`，64 位指针被 ctypes 当 32 位 `c_int` 截断 → `OverflowError`，已补
  `argtypes=[HWND, c_int, c_void_p]` + `restype=c_void_p`，并一并声明 `CallWindowProcW` 签名。
- **修正 `references/18-win32-native.md` §3-D 单实例片段**：原 `kernel32.CreateMutexW(..., None, ...)`
  缺 `argtypes` 且引用 `wintypes.LPSECURITY_ATTRIBUTES`（wintypes 无此类型）→ `AttributeError`，已改为
  `LPVOID` 并补全 `argtypes`/`restype`（核实 `err=0` 正常）。
- **修正 `references/12-ctypes` 过度断言**：原称 `RECT`/`MSG`/`PAINTSTRUCT` 等「wintypes 不导出、必须手动
  定义」——实测 Python 3.13 `wintypes` **已导出** `RECT`/`MSG`/`POINT`/`SIZE`（仅 `WNDCLASSW`/
  `WNDCLASSEXW`/`PAINTSTRUCT`/`HCURSOR`/`LRESULT`/`LPSECURITY_ATTRIBUTES` 缺失）。已修正
  `structures.md` 顶部说明、§关键提醒，`common-apis.md` 使用前必读，与 `18 §2` 规则②一致。
- 配套核实脚本 `verify_refs.py`（29 项断言：wintypes 可用性、结构编译与 sizeof、shcore DPI、
  CreateMutexW、HWND 内外层、`win32gui.CreateWindowEx` 原生控件、子类化、对话框/托盘/COM、pywin32 模块、
  pygubu + ai-ui-design demo.ui 加载）：**TOTAL=29 PASS=29 FAIL=0**。
- version → 1.7.10。

## 1.7.9 (2026-08-02)

按用户指令移除 `examples/ecc-dashboard/`（ECC Dashboard，affaan-m/ECC vendored 适配），与既有「移除库/示例」同模式（移到 Temp 备份，非硬删）：

- **移出技能目录**：`examples/ecc-dashboard/`（README + ecc_dashboard.py + ecc_dashboard_runtime.py + run.py + smoke_test_gui.py + 启动.bat）整体移至 `C:\Users\17151\AppData\Local\Temp\ecc-dashboard.removed\skill-example\`；工作区镜像同名目录同步移出（`mirror-example\`）。
- **清理失效交叉引用（7 个文件）**：`SKILL.md`（示例清单去 `ecc-dashboard/`、架构选型指针改 `inventory-manager/`、界面选型指针改 `idle/`+`inventory-manager/`）、`examples/README.md`（索引表去行 + 删整节）、`examples/tkinter-designer/README.md`（手搓 ttk 路线代表改指 `inventory-manager/`）、`references/09-testing-and-quality.md`（冒烟范本改指 `scripts/smoke_test_gui.py`）、`references/17-ai-ui-design.md`（手搓 ttk 示例去 ecc 指针）、`references/18-win32-native.md`（删 ECC Dashboard `maximize_window` 归属句，保留 Tkinter-Designer 模式说明）、`scripts/smoke_test_gui.py`（删 ECC 示例注释与文档串引用）。
- **保留（不改历史/不动上游）**：CHANGELOG 历史条目按「不改历史」纪律保留；工作区根目录遗留的 `_ecc_dashboard.py`/`_ecc_runtime.py`/`_ecc_preview.png`/`_ecc_shot.py`/`_vendor_ecc.py` 也一并移至 Temp 备份（`scratch\`）。
- version → 1.7.9。

## 1.7.8 (2026-08-02)

新增两个社区 tkinter 应用示例（经本机 `py_compile` + 无头 `Tk()` 冒烟核实可跑），并据用户决策剔除一个不合规候选项：

- **新增 `examples/bulk-image-processor/`**：Haidar-Dagham 的 Bulk Image Processor（图片批量缩放/格式转换/重命名/水印），单文件 GUI、运行期仅依赖 Pillow，是"小工具形态"的干净范本（已按技能惯例补 `run.py` 入 `sys.path` + `启动.bat` GBK/CRLF/无 BOM）。
- **新增 `examples/inventory-manager/`**：Rishikaa07 的 Inventory Management System（员工/供应商/品类/商品/销售/账单 + 离线规则问答机器人），多模块 + sqlite3 裸库。已做**可移植性修复**：原仓库硬编码作者机器绝对路径的图片与账单目录改为 `os.path.join(HERE, ...)`；`run.py` 启动 `os.chdir(HERE)` 保证 `r'ims.db'` 在任意 cwd 下可解析；清理原仓库 `_pychache` 与编译残留 `__pycache__`。
- **剔除 InfoSpider（kangvcar）**：经核实其为多平台账号**爬虫工具箱**（自动登录抓取邮箱/淘宝/支付宝/知乎/B站/运营商等个人数据），并非 tkinter UI 范例，依赖 selenium/nltk 等重型库，且存在平台 ToS 与隐私合规风险，与「技能只收纳本主题内容」原则冲突；用户决策改为仅保留上述两个纯 tkinter 示例。
- **文档接入**（共 2 个文件）：`SKILL.md` version → 1.7.8，参考实现节示例清单补 `bulk-image-processor/` `inventory-manager/`；`examples/README.md` 索引表补两行 + 各自「技术路线 + 可借鉴要点」详节。

## 1.7.7 (2026-08-02)

纠正 1.7.6 的 `.bat` 编码规则（1.7.6 的「UTF-8 带 BOM」是**错误**的，本机实测复现了它造成的故障）：

- **修正规则**（`SKILL.md` 打包段）：`启动.bat` 编码铁律改为 —— ① **禁止 UTF-8 带 BOM**（BOM 会让首行 `@echo off` 变 `锘緻echo off` 报错）；② **必须用 CRLF**（仅 LF 会让 `>`/`=` 被误判换行，拆碎 `chcp 65001`/`set PYTHONUTF8=1`）；③ 含中文（路径/注释）存 **GBK(CP936)**，纯 ASCII 可 UTF-8 无 BOM；④ 保留开头 `chcp 65001 >nul` + `set PYTHONUTF8=1` 让 Python 中文输出正常。
- **重做两个参考 .bat**（`examples/idle/启动.bat`、`examples/thonny/启动.bat`）：按「GBK + CRLF + 无 BOM」重写，已用 `cmd /c` 本机实测解析无报错（`~dp0` 中文路径 `WPS 灵犀` 正常、`python run.py` 可抵达）。
- version → 1.7.7。

> ⚠️ 1.7.6 曾写「`启动.bat` 必须 UTF-8 带 BOM」，该结论错误，已被本条目取代。请勿再照 1.7.6 的 .bat 编码说法执行。

## 1.7.6 (2026-08-02) — 已废弃（.bat 编码结论有误，见 1.7.7）

初版补充一键启动脚本的编码规则，误判为「UTF-8 带 BOM」。实测发现 BOM 会让 cmd 解析首行失败（`锘緻echo off`），故本条被 1.7.7 推翻。**保留记录以警示，勿采纳其 .bat 编码建议。**

## 1.7.5 (2026-08-01)

新增可选第三方增强参考 **tkchart**（实时折线图控件），编号 **10**（原 10 缺口，现回填空位）：

- **新增参考文档**：`references/10-tkchart.md`（综合官方中文文档 + 仓库 README 整理；MIT）。覆盖：核心类 `LineChart`/`Line` 参数表、方法（`show_data`/`configure` 等）、最小用法、后台线程实时流式更新、轴/网格/线型样式定制、PyInstaller 打包（纯 tkinter、增量≈0、通常无需 hidden-import）、与技能工作流整合、官方链接。
- **接入路由表与交叉引用**（共 4 个文件）：
  - `SKILL.md`：Layer 3 目录表新增 10-tkchart 行（位于 15-tksheet 之后，同为「可选增强专属参考」）；工作流 ⑤ 第三方增强按需分支补「要画实时折线图查 10-tkchart」；工作流 ⑧ 打包范围 `第三方美化库（15-16 任一）` → `第三方增强库（10-tkchart / 15-tksheet / 16-pygubu 任一）`；version → 1.7.5。
  - `references/08-packaging.md`：「第三方增强库打包」引文示例 `如 tksheet` → `如 tksheet / tkchart`。
  - `references/20-tkinter-toolkit.md`：底部「已深度覆盖」索引新增 tkchart 行（专属参考 10-tkchart.md），「以上 1 个库」→「以上 2 个库」（该库已在 §二 图表与可视化分类收录，仅补互链）。
- 实测体积参考：基线 stdlib tkinter ≈9.9MB，加 tkchart ≈9.95MB（增量≈0），属对 `08-packaging.md` 最友好的第三方图表库之一。

## 1.7.4 (2026-08-01)

移除第三方增强库 **ttkwidgets**（与 1.7.2/1.7.3 移除 ttkbootstrap/ttkthemes/maliang 同一思路）：

- **移出参考文档**：`references/14-ttkwidgets.md` 已移出技能、备份至系统 Temp（`C:\Users\17151\AppData\Local\Temp\tkinter-desktop-backup\14-ttkwidgets.md`，非硬删除）。
- **清理失效交叉引用**（共 6 个文件）：
  - `SKILL.md`：技术栈注记示例 `如 ttkwidgets` → `如 tksheet`；目录路由表删除 14-ttkwidgets 整行；工作流 ⑤ 美化列举去掉 `14-ttkwidgets /`；工作流 ⑧ 范围 `14-16 任一` → `15-16 任一`；version → 1.7.4。
  - `references/08-packaging.md`：「第三方美化库打包」引文 `如 ttkwidgets/tksheet` → `如 tksheet`。
  - `references/16-pygubu.md`：§6 插件支持列表去掉 `ttkwidgets`（保留 awesometkinter 等）。
  - `references/20-tkinter-toolkit.md`：社区控件库目录删除 ttkwidgets 行；底部「已深度覆盖」索引删除 ttkwidgets 行（dangling 链接），「以上 2 个库」→「以上 1 个库」。
- **按「不改历史 / 不动上游」原则保留**：CHANGELOG 历史条目中的 ttkwidgets 记录；pygubu-designer 等 vendored 上游源码中对 ttkwidgets 的引用。
- 现在「可选增强」路线为 15-tksheet / 16-pygubu（编号缺口 12–14 与原 10 缺口同例，可接受）。

## 1.7.3 (2026-08-01)

移除第三方美化库 **ttkthemes** 与 **maliang**（与 1.7.2 移除 ttkbootstrap 同一思路）：

- **删除参考文档**：`references/12-ttkthemes.md`、`references/13-maliang.md` 已移出技能、备份至 Temp（不做硬删除）。`references/` 现余 11 / 14 / 15 / 16 / 17 / 18 / 19 / 20（编号缺口 12–13 与原 10 缺口同例，可接受）。
- **清理活跃交叉引用**（共 5 个文件）：
  - `SKILL.md`：技术栈注记示例 `如 ttkthemes` → `如 ttkwidgets`；目录路由表删除 12/13 两行；工作流 ⑤ 美化列举改为 `14-ttkwidgets / 15-tksheet / 16-pygubu`；工作流 ⑧ 范围 `12-16 任一` → `14-16 任一`；version → 1.7.3。
  - `references/03-ui-design.md`：§1 决策框架删除「B 轻量换肤（ttkthemes）」档位、对应「升级 B/C」→「升级 C」；§10 可选增强删除 `### ttkthemes` 子节。
  - `references/08-packaging.md`：「第三方美化库打包」引文去掉 ttkthemes 特例、删除 ttkthemes 专属打包要点。
  - `references/14-ttkwidgets.md`：去除「若项目已用 ttkthemes（12-ttkthemes.md）」的失效指针，改为「与任意 ttk 主题方案共存」。
  - `references/20-tkinter-toolkit.md`：社区目录删除 Maliang / ttkthemes 两行；底部「已深度覆盖」索引删除这两行（dangling 链接），「以上 5 个库」→「以上 2 个库」。
- **按「不改历史 / 不动上游」原则保留**：CHANGELOG 历史条目中的 ttkthemes/maliang 记录；`examples/pygubu-designer/pygubudesigner/services/theming.py` 中 vendored 上游对 ttkthemes 的支持代码；`11-case-studies.md` 中 erp-python-simples 真实技术栈的 ttkthemes 事实性记载（非失效指针，保留）。
- 现在「可选增强」路线为 14-ttkwidgets / 15-tksheet / 16-pygubu。

## 1.7.2 (2026-08-01)

收口前几轮会话对技能的结构性调整（均与磁盘实际状态对齐、经核实后落地）：

- **移除 ttkbootstrap**：删除 `references/10-ttkbootstrap.md`（备份至 Temp），并清理 11 个文件中的失效交叉引用与教学性提及（SKILL.md / 03-ui-design / 08-packaging / 11-case-studies / 12-ttkthemes / 13-maliang / 14-ttkwidgets / 20-tkinter-toolkit / examples/README / examples/thonny/README）。CHANGELOG 历史条目与 vendored 上游源码中的旧引用按「不改历史 / 不动上游」原则保留。现在「可选增强」路线为 12-ttkthemes / 13-maliang / 14-ttkwidgets / 15-tksheet / 16-pygubu。
- **Thonny 升级为完整源码范本**：`examples/thonny/` 由「精选研习子集（~600KB，不可独立运行）」升级为 **Thonny 5.0.0 完整 vendored 源码**（约 850 文件，`thonny/` 包 + `run.py`/`启动.bat`/`requirements.txt`）；`run.py` 把本目录插到 `sys.path` 最前，导入的是本目录内随附源码，无需 `pip install thonny`。IDLE 同步为完整 `idlelib` 源码 + 本地启动器。
- **路径纠正**：Thonny/IDLE 完整源码原误放 `fasthtml-desktop/examples`，已移回本技能 `tkinter-desktop/examples/`（二者均为 tkinter 案例，归 tkinter-desktop）。

`SKILL.md`：version → 1.7.2；工作流 ⑧ 打包步骤「第三方美化库（10-16 任一）」修正为「（12-16 任一）」；工作流 ⑤ 第三方美化列举补全 14-ttkwidgets / 16-pygubu。

## 1.7.1 (2026-08-01)

按用户决策将 1.7.0 的 5 份独立参考文档**合并进现有 `03-ui-design.md` / `04-widgets-and-patterns.md`**（更 DRY，避免"一个主题一个编号文件"的碎片化）。已删除 `references/20-menus.md` / `21-simple-widgets.md` / `22-canvas-interaction.md` / `23-text-advanced.md` / `24-window-behavior.md`，全部实测结论保留：

- **菜单深度** → 扩写进 `04` §7「菜单与快捷键」（`menubar` 层级 / `add_cascade`+`add_command`+`add_separator`+`add_checkbutton`+`add_radiobutton` / `tearoff=False` / `accelerator` 仅显示需另 bind / 右键 `tk_popup`+`<Button-3>` / macOS `createcommand` 应用菜单 / MVC 接法）。
- **简单控件配方** → 新增 `04` §8「简单控件配方」（`tk.Listbox` `<<ListboxSelect>>`+滚动联动、`ttk.Scale` `set()` 改值 + 浮点 + 无 `<<RangeChanged>>`、`ttk.Spinbox` `get()` 字符串 + 不吸附 + 无 `<<Increment>>`/`<<Decrement>>`、`ttk.Progressbar` determinate/indeterminate + `step`）；Scrollbar 联动已在 `04` §1/§5 覆盖，本节不再重复。
- **窗口行为** → 新增 `04` §9「窗口行为」（`Toplevel` 基础、`WM_DELETE_WINDOW` 关闭拦截、`overrideredirect` 无边框、`attributes("-topmost"/"-alpha"/state)` 置顶/透明/最大化、多窗口管理、transient+`iconify()` TclError 实测坑）；模态范式已在 `04` §3 覆盖，本节只补充 §3 之外的窗口行为。
- **Canvas 交互** → 扩写进 `03` §6.4「Canvas 交互深挖」（`create_*`/`tags`/`itemconfig`/`coords`/`move`/`delete`、命中测试 `find_closest`/`find_overlapping`/`find_enclosed` 无 `find_within`、`tag_bind` 拖拽、`scrollregion`+滚轮滚动）。
- **Text 富文本** → 扩写进 `03` §6.5「Text 富文本进阶」（`get("1.0","end-1c")` 去尾换行、`tag_configure`/`tag_add` 着色、`mark_*`、`search`/`replace`、`image_create`/`window_create`、`<<Modified>>`+`edit_modified`、撤销栈）。

`SKILL.md`：**version → 1.7.1**；目录路由表移除 20–24 行，并在 `03`/`04` 行描述中补回合并后的覆盖范围。

## 1.7.0 (2026-08-01)

补齐 tkdocs 教程相对本技能的内容缺口（菜单深度、"简单控件"配方、Canvas 交互、Text 富文本、窗口行为）。**全部 API 均在本机 Tk 8.6 / Python 3.13 实测通过**，未引入任何未经运行验证的虚拟事件或选项名。

新增 5 份参考文档：
- **`references/20-menus.md`**：菜单深度——menubar 层级、`add_cascade/command/separator/checkbutton/radiobutton`、`tearoff=False` 去虚线、`accelerator` 仅显示需另 bind、右键上下文菜单（`tk_popup` + `<Button-3>`）、macOS 应用菜单 `createcommand`、跨平台注意点。
- **`references/21-simple-widgets.md`**：Listbox（`<<ListboxSelect>>` + 滚动联动）、Scrollbar 双向绑定、Scale（`set()` 改值 / `get()` 浮点 / **无 `<<RangeChanged>>`**）、Spinbox（`get()` 字符串 / `set()` 不按步长吸附 / **无 `<<Increment>>`/`<<Decrement>>`**）、Progressbar（determinate/indeterminate + `step`）；注明哪些控件无 ttk 版。
- **`references/22-canvas-interaction.md`**：`create_*`/`tags`/`itemconfig`/`coords`/`move`/`delete`、`find_closest`/`find_overlapping`/`find_enclosed` 命中测试（**实测无 `find_within`**）、`tag_bind` 拖拽、`scrollregion` + 滚轮滚动。
- **`references/23-text-advanced.md`**：`get("1.0","end-1c")` 去尾换行、`tag_configure`/`tag_add` 着色、`mark_*`、`search`、`image_create`/`window_create`、`<<Modified>>` + `edit_modified`、撤销栈。
- **`references/24-window-behavior.md`**：`Toplevel` 基础、`transient`+`grab_set`+`wait_window` 模态范式（rd-expense 已验证）、`WM_DELETE_WINDOW` 关闭拦截、`overrideredirect` 无边框、`attributes("-topmost")` 置顶、**实测坑：对 transient 窗口 `iconify()` 抛 TclError**。

交叉修正（已写入文档的"坑"）：
- `ttk.Scale` 直接改 `["value"]` 选项不会移动滑块 / 同步变量——必须用 `.set()`。
- `ttk.Spinbox` `set()` 自由设值不按 `increment` 吸附。
- Scale/Spinbox/Scrollbar **不存在** `<<Increment>>`/`<<Decrement>>`/`<<RangeChanged>>` 虚拟事件——监听变化用 `command=` 或变量 `trace`。
- `tk.Text.get("1.0","end")` 含末尾换行，规范写法 `"end-1c"`。

`SKILL.md`：version → 1.7.0；目录路由表新增 20–24 行；`04-widgets-and-patterns.md` §7 加指向 20/21 的指针。

## 1.5.5 (2026-07-30)

把 references 全部接入「完整工作流」，消除"目录表有、工作流无"的未引用现象：

- **工作流 ①–⑧ 补全参考引用**：③ 项目初始化补 `07-project-structure.md`（src 结构 / 入口规范 / 路径适配）；⑤ 界面设计补 `16-pygubu.md`（工具本体）并加「第三方美化按需查 10/12/13/14/15、11-case-studies 借鉴」分支指针；⑤ 内 pygubu 分支显式加 `16-pygubu.md`；⑧ 打包交付补「引入第三方美化库（10-16 任一）须按各参考 PyInstaller 小节补 hidden-import / --add-data」。
- **结果**：references 01–17 现在都出现在工作流执行清单里（01/02/03/04/05/06/08/09 在必做步骤；10–16、11 作为可选增强指针在 ⑤/⑧；16 在 ⑤；17 在 ⑤ pygubu 分支）；official-docs 5 篇在 HARD-GATE / Layer 1。
- **其他文件夹审计**：docs/（glossary/troubleshooting/delivery-checklist）、scripts/（bootstrap_project.ps1 / build_windows_exe.ps1 / ai-ui-design/*）、examples/（含 vendored 源码树）、templates/project-blueprints/tk-desktop-app/ 均已被 SKILL.md 引用，无游离文件。仅 3 个脚手架 `.tmpl`（item_controller / item_view / test_repository）属已被引用的 blueprint 内部组件，非孤立文件。
- **`SKILL.md`**：version → 1.5.5。

## 1.5.4 (2026-07-30)

重构 `examples/pygubu-designer/` 定位（源码范本，像 IDLE）+ 把 AI 自动化 UI 设计工作流移出 examples：

- **`examples/pygubu-designer/` 改为 pygubu-designer 完整源码范本**：从官方安装包复制 106 个 `.py` + `.mako`（保留子包结构：`codegen/` `data/` `preview/` `properties/` `services/` `util/` `widgets/`），vendored 进 `examples/pygubu-designer/pygubudesigner/`，**只读学习用**（像 `idle/` 的 idlelib）。当前 vendored 版本 0.41.4，GPL-3.0。
- **`启动.bat` 改为启动 pygubu-designer 本身**：`pythonw -m pygubudesigner`（封装已安装版，含 data 资源；刻意 cd 到安装目录，避免本目录 vendored 副本被优先 import 而缺资源崩溃）。
- **AI 自动化 UI 设计工作流移出 examples**：原 `demo.ui` + `app.py` + `check_ui.py` + `check_ui_visual.py` + `demo_preview.png` + `requirements.txt` 移至 `scripts/ai-ui-design/`（仍可运行，但不再是 example）。
- **新增 `references/17-ai-ui-design.md`**：独立的 AI 自动化 UI 设计工作流参考——写 `.ui` → 无头校验 `check_ui.py` → 视觉截图校验 `check_ui_visual.py` → 改错完整闭环、`.ui` 语法坑（resizable 枚举 / pady 单值 / button command JSON）、闭环命令清单。
- **`SKILL.md`**：version → 1.5.4；技术栈说明 pygubu 段改指向 references/17；Layer 3 表加 17 行、16 行注明「闭环见 17」；参考实现节 `pygubu-designer/` 描述更新为「源码范本」；工作流 ⑤ AI 分支改引用 references/17 + `scripts/ai-ui-design/`，并修正缩进。
- **`check_ui.py` 健壮性**：默认校验的 `demo.ui` 改为相对脚本自身目录解析，可在任意 cwd 下运行。
- **`examples/README.md`** / `examples/pygubu-designer/README.md`：同步更新定位。

## 1.5.3 (2026-07-30)

新增 5 份「可选第三方增强 / AI 自动化 UI 设计」参考文档（下载完整文档内容，非仅链接）：

- **`references/12-ttkthemes.md`**：ttkthemes 主题换肤——完整主题名清单（arc/clearlooks/radiance/scid 系列等 ~20 套）、`ThemedTk`/`ThemedStyle` 零侵入用法、`get_themes()`、`set_theme_advanced()` 动态主题与 pixmap 主题清单、与 ttkbootstrap 取舍、GPLv3/BSD 许可。
- **`references/13-maliang.md`**：maliang Canvas 自绘 UI 框架——全 UI 由 Canvas 绘制、MIT、Python≥3.10、必需/可选/扩展依赖（`[opt]`/`[ext]`）、设计哲学、何时选不选。
- **`references/14-pandastable.md`**：pandastable——pandas DataFrame 表格控件 + matplotlib 交互绘图、完整功能清单、`Table` 用法、`dataexplore` 应用、何时选不选。
- **`references/15-tksheet.md`**：tksheet 高性能表格/树形表格——可编辑、下拉/复选/进度条、拖拽行列、树形模式、v7 简洁语法、MIT、已停止功能开发的状态说明、何时选不选。
- **`references/16-pygubu.md`**：pygubu / pygubu-designer——`.ui` XML 格式、Builder API（`add_from_file`/`get_object`/`connect_callbacks`）、专属控件与插件、designer 两种工作流（经典 .ui / 生成代码）、与技能工作流⑤「AI 自动化 UI 设计」整合、官方链接。
- **SKILL.md**：Layer 3 目录表新增 12–16 行；`version` → 1.5.3。
- **修复**：`10-ttkbootstrap.md` 标题 stale `# 11 ·` → `# 10 ·`（上次编号重排遗漏）。

## 1.5.2 (2026-07-30)

修复 UI 异常 + references 编号连续化：

- **references/ 编号连续化**：`11-ttkbootstrap.md` → `10-ttkbootstrap.md`，`12-case-studies.md` → `11-case-studies.md`（填补删除 `10-customtkinter.md` 后的空缺）。更新所有活跃交叉引用：SKILL.md 目录表、`06-data-layer-sqlite.md`、`11-case-studies.md` 内部引用。CHANGELOG 历史条目保留旧编号不变。
- **修复 pygubu-demo "tk" 空白窗口**：`app.py` 的 `main()` 创建了 `root=tk.Tk()` 但未隐藏它。`.ui` 的 mainwindow 是 Toplevel，挂在 root 上，导致 root 以空白 "tk" 窗口形式显示。修复：在 `App(root)` 后加 `root.withdraw()`。
- **修复 rd-expense-tk 仪表盘布局**：
  - 环图列（column 2）去掉固定 minsize=190，改为按内容自适应宽度（`sticky="ns"` 而非 `"nsew"`），消除右侧大面积空白
  - 环图区域改用 pack 居中布局（Canvas + Label 垂直排列），不再用 grid stretch
  - 条形图画布宽度从 360 缩至 280，给 Treeview 留更多空间
  - `refresh()` 中画环前加 `ring.update_idletasks()` 确保 canvas 已完成布局
  - 环图绘制 size 从 120 调至 110（适配更小的 140×140 canvas）
- **验证**：rd-expense-tk pytest 16 passed + GUI smoke 8/8；pygubu check_ui.py headless OK。

## 1.5.1 (2026-07-30)

增强 pygubu 自动化 UI 设计闭环 + 一键启动脚本：

- **新增视觉截图校验**（`examples/pygubu-designer/check_ui_visual.py`）：
  - 真正渲染 `.ui` 窗口 → PIL ImageGrab 截图 → 几何检查（零尺寸/越界）→ 输出 `demo_preview.png`
  - **首次截图即捕获无头校验漏掉的 Bug**：空 ttk.Treeview 与父 Frame 背景完全同色，用户看不到列表区域
  - 修复：给包裹 Treeview 的 `listframe` 加 `borderwidth="1"` + `relief="solid"`（ttk.Treeview 本身不支持 borderwidth/relief）
  - 需 Pillow（已加入 `requirements.txt`，标记可选）
  - 工作流 ⑤ 新增步骤 5「视觉截图校验」：渲染→截图→几何检查→AI 多模态审查
- **三个示例各增一键启动脚本**：
  - `examples/idle/启动IDLE.bat` — 双击启动 IDLE（`pythonw -m idlelib`）
  - `examples/rd-expense-tk/启动.bat` — 双击启动研发费用管理系统（`pythonw launcher.py`）
  - `examples/pygubu-designer/启动.bat` — 双击启动 demo.ui 示例窗口（`pythonw app.py`）
  - 均优先 `pythonw`（无控制台）、回退 `python`
- **`SKILL.md`** → 1.5.1；工作流 ⑤ 补充视觉截图校验步骤。

## 1.5.0 (2026-07-30)

重构 `examples/` 示例集，并引入「AI 自动化 UI 设计」工作流（pygubu）：

- **移除三个社区示例**：`sales-data-analyzer/`、`interactive-sales-dashboard/`、`erp-python-simples/`（依赖重、与「标准库 vs 第三方取舍」教学主线关系弱）。
- **`examples/idle/` 深度展开**：重写其 `README.md`，系统梳理 `idlelib` 在自制 tkinter 应用时的可借鉴模块——文本编辑内核（Percolator/Delegator/undo/textview/search）、补全与提示（autocomplete/calltip/tooltip）、多键绑定（multicall）、树形（tree.py）、配置系统（config-*.def/configdialog.py）、GUI 与引擎分离（rpc.py）、多窗口（window.py）、预制对话框（query.py/help_about.py/statusbar.py）、平台适配（macosx/redirector/util），并给出架构启示。
- **新增 `examples/rd-expense-tk/`**：将研发费用管理系统重做为「功能更丰富、界面更美观」的示范版并 vendored 进 `examples/`——Treeview 行高按字体 metrics 自适应、Canvas 环形预算执行图、列表内搜索过滤、零依赖「关于」对话框（借鉴 idlelib help_about）；运行期零第三方依赖，附「可借鉴内容」README。
- **新增 `examples/pygubu-designer/`**：vendored 安装 pygubu-designer（RAD，UI 以 XML `.ui` 描述）。含 `demo.ui` + `app.py` + 无头校验脚本 `check_ui.py` + 「可借鉴内容」README；README 记录 AI 后台自动设计 UI 的闭环（写/改 `.ui` → `pygubu.Builder` 无头校验 → 按报错改 → 运行期 `Builder().add_from_file().get_object().connect_callbacks()` 绑定回调）与 `.ui` 常见填坑（resizable 取值、pady/padx 格式、button command JSON 格式）。
- **`SKILL.md`**：
  - version → 1.5.0
  - 技术栈说明新增 pygubu 为可选「AI 自动化 UI 设计」工具（仅 `pygubu.Builder` 一个运行期依赖，非交付必选项）
  - 「参考实现」节 `examples/` 列表更新为 `idle/` + `rd-expense-tk/` + `pygubu-designer/`
  - 完整工作流 ⑤ 界面设计新增「AI 自动化 UI 设计（pygubu 路线）」分支：全程 AI 后台执行命令，人无需打开设计器
- **`examples/README.md`**：索引表更新为 `idle/` / `rd-expense-tk/` / `pygubu-designer/`，各自附可借鉴要点。

## 1.4.9 (2026-07-30)

新增**控件间距与行高规范**（§5.1~5.4），系统性解决 Tkinter 应用「行与行之间太紧、字体被截断或显示不全」的顽疾：

- **`references/03-ui-design.md`** 新增 §5 子节「控件间距与行高规范（必须遵守）」：
  - **§5.1 Treeview 行高公式**：`rowheight = font.metrics('linespace') + vertical_reserve`，提供 `setup_treeview_rowheight()` 函数、四档模式对照表（紧凑/舒适/宽松）、以及「默认 20 在各场景下的症状表」（中文/英文混合/高 DPI/大字号）
  - **§5.2 表单字段垂直间距**：`FORM_PAD_Y=4`（行内）+ `GROUP_PAD_Y=10`（组间）+ 四档间距常量体系 `pad_xs/sm/md/lg/xl` 纳入 THEME 字典
  - **§5.3 常见控件间距检查清单**：Treeview/Button/Entry/Label/Frame/Toplevel/Notebook/Panedwindow 各自必设参数与推荐值
  - **§5.4 高 DPI 间距放大**：`dpi_scale()` 函数按缩放因子自动放大间距
- **`references/04-widgets-and-patterns.md`**：Treeview 示例代码追加 `font.metrics('linespace') + 8` 行高设置，禁止依赖默认值
- **`references/03-ui-design.md` §11 反模式清单**：新增 3 条反模式（Treeview 默认 rowheight / 表单无 pady / 间距不随 DPI 放大）
- **`references/03-ui-design.md` §12 自查清单**：新增 5 条间距相关检查项（rowheight 公式 / 表单 pady / 控件 padding / dpi_scale / 高 DPI 全套验证）
- **`references/03-ui-design.md` §4 起手式示例**：旧 `rowheight=26` 硬编码改为带注释的过渡值，指向 §5.1 公式；Treeview 子节加引用提示
- 触发来源：四个示例 GUI 本地运行实测截图反馈——Sales Data Analyzer 的 Treeview 文字截断是典型症状

## 1.4.8 (2026-07-30)

新增 `examples/` 可运行参考示例，使技能从「文档 + 骨架」走向「文档 + 骨架 + 真实可跑示例」：

- **新增 `examples/` 目录**（四个示例，均经本地正向运行验证可打开 GUI）：
  - `erp-python-simples/`：SQLAlchemy + ttkthemes + tkcalendar + Pillow + bcrypt + passlib，演示「标准库 + 第三方共存」路线；含 `create_db.py` 建库步骤
  - `sales-data-analyzer/`：单文件 pandas + matplotlib + seaborn 数据分析工具，启动即开空窗口、由用户选文件
  - `interactive-sales-dashboard/`：ttkbootstrap 销售看板，已将原作者硬编码桌面路径改为相对 `sales_data.xlsx`，并清理上游污染的 `pip freeze`（另存 `requirements.upstream.txt` 参考）
  - `idle/`：CPython 标准库 `idlelib` 完整 vendored 源码，作为纯标准库大型 tkinter 应用架构范本
- **每个示例自带 `requirements.txt` + `README.md`**，并在 `examples/README.md` 给出索引与统一运行方式
- **`SKILL.md`**：version → 1.4.8；「参考实现」节新增 `examples/` 四个示例的指向与运行说明
- 示例源码为社区项目忠实搬运（含必要可移植性修复），版权归原作者，仅作教学/起步参考



取消并移除「零依赖铁律」：第三方库不再是「打破铁律」的例外，而是与标准库并列的一等公民。

- **核心理念变更**：标准库（tkinter+sqlite3）仍是默认交付栈，但 ttkbootstrap / pandas / matplotlib / SQLAlchemy / openpyxl 等第三方库按需引入完全合法，不再有「零依赖优先」的硬性约束；选型只看需求与代价（EXE 体积、Python 门槛等）。
- **`SKILL.md`**：version → 1.4.7；「技术栈锁死（默认交付）」改为「技术栈（默认交付栈）」；删除「会打破零依赖铁律」等表述；Layer 3 目录表「零依赖 vs 第三方决策框架」改为「标准库 vs 第三方 选型框架」。
- **`references/03-ui-design.md`**：两条路线决策框架去掉「默认零依赖/破零依赖铁律」措辞，A 路线由「零依赖（默认）」改为「标准库（推荐默认起点）」；Canvas / emoji 等标准库技法保留，仅去掉「铁律」字眼。
- **`references/06-data-layer-sqlite.md`**：数据层「锁定标准库 sqlite3」改为「默认用标准库 sqlite3」，并指明复杂场景可用 SQLAlchemy。
- **`references/11-ttkbootstrap.md`**：删除「铁律提醒 / 放弃零依赖铁律」等措辞，改为中性的「引入第三方依赖须补打包配置」。
- **`references/12-case-studies.md`**：「零依赖默认栈」相关表述改为「标准库默认栈」。
- 历史 CHANGELOG 条目保留作演进记录，不指向已失效的「铁律」。


## 1.4.6 (2026-07-30)

移除失效案例，保持案例研究文档整洁（无未核实/死链条目）：

- **`references/12-case-studies.md`**：删除案例 7「HR Analyzer（SimBoex）」——原 GitHub 链接 404、仅依用户描述整理、未核实源码；后续案例顺移重编号（Interactive Sales Dashboard 8→7、IDLE 9→8、Leo Editor 10→9、Pyspread 11→10），技术栈矩阵与全文交叉引用同步重排；「链接失效」横向结论与二类源码索引去掉 HR Analyzer；案例总数 11 → 10
- **`SKILL.md`**：version → 1.4.6；Layer 3 目录表案例研究描述「11 个社区 Tkinter 应用」改为「10 个」


## 1.4.5 (2026-07-30)

移除 CustomTkinter 专属参考，收敛「可选增强」路线到 ttkbootstrap 单条主线：

- **删除 `references/10-customtkinter.md`**：不再维护 CustomTkinter 专册（其 Pillow 强依赖、+7MB 体量、架构级切换代价与「零依赖优先」原则冲突，且社区活跃度下降）；相关副本均已删除
- **`SKILL.md`**：version → 1.4.5；技术栈锁死注释的第三方库清单移除 CustomTkinter（保留 ttkthemes / tkinterweb / matplotlib / ttkbootstrap）；Layer 3 目录表删除 10-customtkinter.md 行
- **`references/03-ui-design.md`**：决策框架 C 档（架构切换）去掉 CustomTkinter；§7 组件封装的第三方范式由 CTk 改为 ttkbootstrap；§8 状态反馈去掉 CTk 对比；§10 删除整段「CustomTkinter 架构级切换」子节；来源索引去掉 2 条 CTk 专属来源
- **`references/08-packaging.md`**：第三方美化库打包节移除 CustomTkinter 两处（含重复项），第三方清单与 §10 可选增强指向改为 `03-ui-design.md`（顺带修复此前遗留的 `10-modern-ui.md` 死链）
- **`references/11-ttkbootstrap.md`**：定位块去掉「与 10-customtkinter 并列」、体积对比去掉「与 CustomTkinter 同量级」、关联索引去掉 10 交叉引用，使其成为唯一可选增强专册
- **`references/12-case-studies.md`**：关系说明与关联索引去掉 `10-customtkinter.md` 引用

## 1.4.4 (2026-07-30)

新增真实案例研究参考（综合用户提供的 11 个社区 Tkinter 应用，实测拉取源码整理）：

- **新增 `references/12-case-studies.md`**：按三类组织——① ERP/进销存/订单管理（erp-python-simples、Grocery Mart、SIMPLY、Grocery Store V1.1）；② 数据分析/BI（Sales Data Analyzer、HR Analytics Dashboard、HR Analyzer、Interactive Sales Dashboard）；③ 标杆型（IDLE、Leo Editor、Pyspread）。每个案例含定位/技术栈/文件结构/**实拉源码摘录**/可借鉴点/反模式警示/链接（标注「已核实」或「GitHub 404 失效」）。附技术栈矩阵与「对本技能的启示」横向结论。
- **实测核实**：8 个仓库源码已核实（erp-python-simples 的 SQLAlchemy ORM 分层、SIMPLY 的 Excel-as-db、Sales Data Analyzer 的 class+ttk.Style 结构、HR Analytics 的 `clear_frame()+FigureCanvasTkAgg` 嵌图模板、Interactive Sales Dashboard 的 ttkbootstrap darkly+Treeview 看板等）；Grocery Mart 仅 PyPI 元数据可证（ttkbootstrap+SQLite+Python≥3.11），HR Analyzer 原链接 404 仅依用户描述整理。
- **洞察落点**：数据层 4 条真实路线（JSON < Excel < SQLite 裸库 < SQLAlchemy ORM）；BI 类「Tkinter 前端 + pandas/matplotlib 后端」标准形态；反复出现的反模式（硬编码路径、单文件无分层、全局状态、锁死窗口）正是 `03/08` 铁律的规避对象。
- **SKILL.md**：version → 1.4.4；Layer 3 目录表新增 12-case-studies.md 行。

## 1.4.3 (2026-07-30)

新增 ttkbootstrap 专属参考（综合官方文档 ttkbootstrap.readthedocs.io 2.x 版转化）：

- **新增 `references/11-ttkbootstrap.md`**：定位为「可选第三方增强路径」的专属参考（引入即破零依赖铁律，需补打包）。涵盖：决策代价对比表（Python 3.10+ 门槛、唯一运行期依赖 Pillow）、安装与环境、快速上手、30 套内置主题（15 家族 × 明暗）与运行时换肤、Colors 色阶对象（`c.primary[300]` 等）与自定义主题、`bootstyle` 语义化语法（`[@surface] [color] [variant] <base-type> [orient]`、严格模式、等价 ttk 样式名）、全组件速查表（含独占 Meter/DateEntry/Floodgauge/Tableview/ScrolledFrame/CollapsibleFrame/Toast/Messagebox/Querybox）、从 ttk 迁移映射表、PyInstaller 打包要点、体积实测、来源索引
- **体积实测**：独立 venv（Python 3.13.12 / PyInstaller 6.21.0 / `--onefile --windowed --noupx`）A/B 打包——纯 stdlib tkinter 基线 **9 MB**，ttkbootstrap 最小程序 **18 MB**，实测增量 **+8 MB**（远小于 matplotlib 的 +25~40MB；与 CustomTkinter +7 MB 同量级）；§0 对比表与 §10 体积实测节均回填真实数字
- **SKILL.md**：version → 1.4.3；技术栈锁死注释补「ttkbootstrap 专册见 11」；Layer 3 目录表新增 11-ttkbootstrap.md 行

## 1.4.2 (2026-07-30)

实测修正 CustomTkinter 体积数据（纠正此前误用的 matplotlib 量级）：

- **实测方法**：新建独立 venv 装 customtkinter 6.0.0 + Pillow 12.3.0 + PyInstaller 6.21.0；对最小程序做 A/B onefile --windowed --noupx 打包——纯 stdlib tkinter 基线 **9 MB**，CustomTkinter **17 MB**，**实测增量 +7 MB**（未压缩源码包 customtkinter≈0.95MB + Pillow≈12MB 共≈16MB，但 PyInstaller 仅收集被 import 部分并压缩）。
- **`10-customtkinter.md`**：§0 定位块、§0 对比表、§9 打包要点三处「+25~40MB」全部修正为实测「+~7 MB」，并注明与 matplotlib 量级区别。
- **`08-packaging.md`**：第三方美化库打包节补充 CustomTkinter 实测代价「约 +7 MB」，与 matplotlib 的 +25~40MB 区分。
- **SKILL.md**：version → 1.4.2。

## 1.4.1 (2026-07-30)

新增 CustomTkinter 专属参考（综合官方文档 + 官方 examples 转化）：

- **新增 `references/10-customtkinter.md`**：定位为「可选第三方增强路径」的专属参考（引入即破零依赖铁律，需补打包）。涵盖：安装与环境、快速上手、主题与外观模式（含自定义 JSON 主题）、缩放与 HighDPI、全组件速查表（CTk/Frame/Label/Button/Entry/Textbox/CheckBox/Switch/Radio/Slider/ProgressBar/OptionMenu/ComboBox/SegmentedButton/Tabview/ScrollableFrame/Canvas/Image/Font/MenuBar/InputDialog）、外观感知颜色元组语法、`pack/grid/place` 布局、从 ttk 迁移映射表、PyInstaller 打包要点、5 个官方示例（simple/complex/image/scrollable/background）提炼
- **SKILL.md**：version → 1.4.1；技术栈锁死注释补「CustomTkinter 专参见 10」；Layer 3 目录表新增 10-customtkinter.md 行
- references 编号由 01–09 扩展为新增 10（CustomTkinter 专册）

## 1.4.0 (2026-07-30)

文件合并与编排（消除同源重复、收敛编号、梳理工作流）：

- **合并 UI 三件套为单一 `references/03-ui-design.md`**：原 `03-ui-design.md`（战术）、
  `10-modern-ui.md`（现代增强）、`11-ui-design-methodology.md`（方法论）三份同源资料合并
  重写，按「方法论 → 战术 → 现代增强」自上而下组织；删除 `10`、`11` 两个冗余文件
- **references 收敛为 01–09 连续编号**（加 official-docs），结构更干净
- **SKILL.md**：version → 1.4.0；Layer 3 目录表三行合一为单一 03 行（覆盖方法论+战术+现代
  增强）；工作流 ⑤ 去掉 10/11 引用；技术栈锁死注释的「方案与取舍」指向改为 03（§1 决策
  框架 / §10 可选增强）
- 合并后核心要点：Design Token 单一真相来源、零依赖 vs 第三方决策框架、ttk.Style 非 CSS
  真相、复合布局（Frame 即单元、外层 grid/内层 pack、禁混用）、组件封装（`**kwargs` 透传
  铁律）、反模式清单、交付前自查清单、来源索引

## 1.3.0 (2026-07-30)

新增界面设计方法论（综合 7 篇公开资料提炼，按"零依赖优先"裁剪）：

- **新增 `references/11-ui-design-methodology.md`**：Design System 视角的上层方法论，与战术性
  `03-ui-design.md` 互补。涵盖：Design Token 单一真相来源（零依赖 ttk.Style 注入版 + 第三方
  CustomTkinter 封装版）、零依赖 vs 第三方两条路线决策框架、ttk.Style 非 CSS 真相（theme+layout+
  element 三层绑定、必须 clam、map 管状态、layout 重建、跨平台失效、调试口诀）、复合布局哲学
  （Frame 即布局单元、外层 grid / 内层 pack、禁止混用）、三色+语义色配色、组件封装（命名样式 /
  AppButton / BasePage、`**kwargs` 透传铁律）、交互与状态联动（变量 trace / 异步缓冲）、跨平台
  一致性陷阱、反模式清单、方法论层自查清单、来源索引
- **SKILL.md**：version → 1.3.0；Layer 3 目录表新增 11-ui-design-methodology.md 行；
  工作流 ⑤ 界面设计补充引用 11

## 1.2.0 (2026-07-30)

现代化 UI 增强 + 打包进阶要点（统一结构化组织）：

- **新增 `references/10-modern-ui.md`**：现代化增强总纲。含 ttk.Style 深度定制
  （滚动条/进度条/下拉/输入框雅化、悬停/选中态 map）、Canvas 自绘条形图与环形进度、
  字体/emoji/PIL 图标、第三方美化库可选方案（ttkthemes / CustomTkinter / tkinterweb /
  matplotlib tkinter backend，含依赖与体积代价）、延迟加载与异步桥接、现代化检查清单
- **`08-packaging.md` 新增 PyInstaller 打包进阶内容**：版本信息注入
  （`version_info.txt` VSVersionInfo + `build_info.json` + 一致性原则）、非标准
  Python/Conda 的 DLL 依赖链（`_tkinter.pyd`/`tcl86t.dll`/`_sqlite3.pyd` 等）、
  受限/沙箱环境构建（workpath/distpath 重定向）、`.spec` 文件的 CLI 陷阱、第三方库
  打包（hidden-import / collect-submodules / copy_metadata / 裁剪优于全量）、代码签名
- **`scripts/build_windows_exe.ps1`**：新增 `-VersionFile` 参数，存在则 `--version-file`
  注入 EXE 版本信息
- **SKILL.md**：技术栈锁死说明改为「默认零第三方依赖，第三方美化库为可选增强」；目录表与
  打包铁律补充 10-modern-ui / 版本信息注入

### 验证项目同步现代化（rd-expense-tk）

- `common/ui.py`：setup_style 新增滚动条/进度条/下拉/输入框雅化样式与 `Sidebar.TButton`/
  `SidebarActive.TButton` 导航样式；新增 `draw_bar_chart()` / `draw_ring()` Canvas 自绘助手
- `views/main_window.py`：侧边栏导航由经典 tk.Button 改为 ttk 按钮（悬停/激活态由
  `style.map` 驱动，现代化一致观感）
- `views/dashboard_view.py`：新增 Canvas 自绘「各项目研发费用」横向条形图（零依赖）
- `services/engine.py` + `controllers/main_controller.py`：新增 `expense_by_project()`
  聚合，供仪表盘图表使用
- 四道门禁回归全绿：16 pytest + 8 项 GUI 冒烟 + PyInstaller onefile（注入版本信息）+ EXE 冒烟

## 1.1.0 (2026-07-30)

实战验证回写（rd-expense-tk 复刻项目四道门禁全通过：16 单测 + 8 项 GUI 冒烟断言 + PyInstaller onefile + EXE 冒烟）：

- troubleshooting：新增「View↔schema 字段错位 KeyError（仅 GUI 冒烟联动路径可抓）」
- troubleshooting：新增「冒烟脚本等待 after 回调的正确轮询姿势（update()+sleep，勿用无回调 after(20)）」
- troubleshooting：新增「Git Bash POSIX 路径经环境变量传给 Windows Python 被解析为盘符根目录」
- 09-testing：补充 TreeviewSelect 联动必测说明、worker+after 等待循环模板、
  conftest 中 import 期环境变量的模块清缓存模式

## 1.0.0 (2026-07-30)

- 初版：SKILL.md 总路由 + 9 篇 references + 官方文档转档（tkinter/ttk/messagebox/font/dialogs）
- scripts：bootstrap_project.ps1（骨架生成）、build_windows_exe.ps1（四道门禁打包）、蓝图内置 smoke_test_gui.py
- templates：tk-desktop-app 蓝图（MVC 分层、可运行空壳、测试齐备）
- 验证项目：研发费用管理系统 Tkinter 版（rd-expense-tk）全链路跑通
