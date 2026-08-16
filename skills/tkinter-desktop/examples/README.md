# 示例 / Examples

本目录是 `tkinter-desktop` 技能的**可运行参考实现**。每个子目录都是一个独立、可直接运行的
tkinter 桌面应用示例，演示不同的技术路线与可复用的设计模式。每个示例都附有
**「可借鉴要点」**——做自己的 tkinter 应用时，能直接从该示例里抠走的零件。

| 示例 | 技术路线 | 运行期依赖 | 入口 |
|------|----------|-----------|------|
| `idle/` | 纯标准库 `idlelib` 大型 tkinter 应用架构范本 | 无（标准库） | 双击 `启动.bat` 或 `python run.py`（运行本目录 vendored 完整源码）；亦可 `python -m idlelib` |
| `pygubu-designer/` | pygubu-designer 完整生产级 RAD 设计器（完整源码 + `data/` 资源，**可直接运行**） | `pygubu` / `appdirs` / `blinker`（来自系统 pip，非 vendored） | 双击 `启动.bat` 或 `python run.py` 跑本目录 vendored 源码；详见 [`pygubu-designer/README.md`](pygubu-designer/README.md) |
| `tkinter-designer/` | Figma → Tkinter 代码生成器（vendored 研读，开发期工具） | jinja2 / Pillow / requests（仅生成时需要） | `python -m tkdesigner.cli <URL> <TOKEN>`；详见 [`tkinter-designer/README.md`](tkinter-designer/README.md) |
| `native-win32/` | 纯 Win32 API 计算器（ctypes 原生窗口，零 tkinter 依赖） | 无（标准库 ctypes） | `python calculator.py`；详见 [`native-win32/README.md`](native-win32/README.md) |
| `thonny/` | 纯 tkinter 写的真实 Python IDE（Thonny）**完整源码范本** | 无（标准库） | 双击 `启动.bat` 或 `python run.py`（运行本目录 vendored 完整源码，无需 `pip install thonny`）；亦可 `python -m thonny` |
| `bulk-image-processor/` | 图片批量处理工具（缩放 / 格式转换 / 重命名 / 水印等） | Pillow（仅图像处理时需要） | 双击 `启动.bat` 或 `python run.py`（运行本目录 vendored 源码）；入口 `image_processor_app.ImageProcessorApp` |
| `inventory-manager/` | 进销存管理后台（员工 / 供应商 / 品类 / 商品 / 销售 / 账单 + 离线问答机器人） | Pillow（图标/图片加载；sqlite3 为标准库） | 双击 `启动.bat` 或 `python run.py`（运行本目录 vendored 源码）；入口 `dashboard.IMS` |

---

## `idle/` — 标准库 idlelib 大型 tkinter 应用范本

IDLE 本身是用纯标准库 tkinter 写的真实 IDE，沉淀了大量可直接复用的模式与控件。
完整可借鉴内容见 [`idle/README.md`](idle/README.md)，要点速览：

- **文本编辑内核**：`Percolator`/`Delegator` 管道式文本变换、`undo.py` 撤销栈、`textview.py` 只读弹窗、`search.py`/`replace.py` 查找替换。
- **自动补全与提示**：`autocomplete.py`、`calltip.py`、`tooltip.py`。
- **多键绑定**：`multicall.py` 跨平台快捷键统一描述。
- **树形控件**：`tree.py` 可折叠树（懒加载）。
- **配置系统**：`config-*.def` 声明式 schema + `configdialog.py` 用 `ttk.Notebook` 做的设置面板范本。
- **GUI 与引擎分离**：`rpc.py` 子进程 + RPC 模式，GUI 永不假死。
- **多窗口管理**：`window.py` 的 `WindowList`。
- **预制对话框**：`query.py`、`help_about.py`、`statusbar.py`。
- **架构启示**：Delegator 管道、rpc 隔离、设置声明化、预制对话框库。

---

---

## `pygubu-designer/` — pygubu-designer 完整生产级 RAD 设计器（完整源码 + 可直接运行）

pygubu-designer 是用纯 tkinter 写的真实 RAD 设计器。本目录把它**完整源码 vendored 进来**，
是一份**可直接阅读、修改、运行的「生产级代码全集」**——不是只读片段（vendored v0.41.4，GPL-3.0）。
要点：

- **源码结构**：`pygubudesigner/`（完整 `.py` 源码 + `data/` 资源：`data/ui/*.ui` 设计器自身窗口、
  `data/images/`、`data/locale/` 多语言、`data/code_templates/*.mako` 代码模板）。
- **直接运行**：双击 `启动.bat` 或 `python run.py`。`run.py` 把本目录插到 `sys.path` 最前，
  并保证 `PYGUBU_DESIGNER_RUNNING` 在 import `pygubu` 前就置位，因此跑的是**本目录 vendored 源码**
  （而非系统 pip 的官方包），且设计器的属性注册表能正常初始化。
- **外部依赖（来自系统 pip，不随本目录 vendored）**：`pygubu`（UI 构建核心，需 `>=0.38.2`）、
  `appdirs`（`preferences` 用到，缺失会直接退出）、`blinker`（属性注册表的信号机制需要）。
  `run.py` 还会把 `pygubu.__version__`（0.40.x 未暴露该属性）从包元数据补上，故无需改动上游源码即可启动。
- **可借鉴方向**（读 `pygubudesigner/` 源码）：插件化架构（services/plugins）、属性编辑面板（properties/）、代码生成器（codegen/）、预览宿主（preview/）、`ttk.Style` 专业外观（designerstyles.py）。

> pygubu 的 `.ui` 格式、Builder API、专属控件见 `../pygubu/`（子技能）；本目录的用法与源码研读见
> [`pygubu-designer/README.md`](pygubu-designer/README.md)。

---

## `tkinter-designer/` — Figma → Tkinter 代码生成器（工具类示例）

Tkinter Designer 通过 Figma REST API 把设计稿翻译成**绝对定位（Canvas + place）的 tkinter 代码**。
它是**开发期工具**，不是业务应用。详见 [`tkinter-designer/README.md`](tkinter-designer/README.md)。

要点速览：
- **三种模板**：`script` / `class` / `pages`（多页向导），共享 `COMMON_TEMPLATE_HEADER`。
- **可直接抠走的零件**：`IMAGE_REFS` 保活列表、`enable_dpi_awareness()`、`center_window()`、圆角矩形 `ImageButton`。
- **适用场景**：登录页/启动页/仪表盘大屏等固定尺寸窗口；不适合需要拉伸的业务主窗口。

---


## `native-win32/` — 纯 Win32 API 计算器（ctypes 原生窗口示例）

**不使用 tkinter** 的纯 Win32 原生窗口开发——作为对比参照和 ctypes 编程的学习起点。
440 行纯 Win32 API 计算器：窗口注册 → WNDPROC 回调 → 控件创建 → GDI 状态栏绘制 → 消息循环。详见 [`native-win32/README.md`](native-win32/README.md)。

要点速览：
- **完整消息驱动骨架**：RegisterClassW → CreateWindowExW → ShowWindow → GetMessageW 循环
- **WNDPROC 全局引用防 GC**：回调必须赋值给模块级变量
- **WM_COMMAND 处理**：wparam 低 16 位 = 控件 ID，高 16 位 = 通知码
- **WM_PAINT GDI 绘制**：BeginPaint/EndPaint + CreateSolidBrush/FillRect + TextOutW
- **gdi32.dll 归属**：CreateSolidBrush/DeleteObject/TextOutW 在 gdi32 不在 user32
- **GetMessageW 返回值判定**：返回 0 = WM_QUIT（正常退出），返回 -1 = 调用出错（须 raise）

> 本示例是 tkinter ↔ Win32 互操作的**底层能力参考**——通过 `root.winfo_id()` 获取 HWND 后，
> 即可调用 Win32 API 实现高 DPI、任务栏图标、单实例锁定等能力。详见 `ctypes/SKILL.md` §3。

---

## `thonny/` — Thonny：纯 tkinter 真实 IDE 完整源码范本

Thonny 是塔尔图大学出品的 Python IDE，**纯标准库 tkinter 实现**、MIT 许可、千万级下载。
本目录是它的**完整 vendored 源码**（`thonny/` 包 + `run.py`/`启动.bat`/`requirements.txt`，约 850 个文件），
专门用来研究"大型 tkinter 应用如何组织"，且**可直接运行**——`run.py` 把本目录插到 `sys.path` 最前，
导入的是本目录内随附的 `thonny` 源码包，无需另装 `pip install thonny`。
完整可借鉴内容见 [`thonny/README.md`](thonny/README.md)，要点速览：

- **注册中心架构**：`workbench.py` 的 `Workbench` 单例用 `add_view`/`add_command`/`add_menu` 统一注册，功能靠插件注入（开闭原则）。
- **全局单例 + 事件总线**：`get_workbench()` 随处可取；`bind`/`emit` 解耦 Model↔多 View（MVC 正解）。
- **插件系统**：模块里写 `load_plugin()` 即被自动发现——加功能=加文件，不动主窗体。
- **可直接抠的零件**：`ui_utils.py` 的 `create_tooltip` / `ask_*` / `ems_to_pixels` 几乎零依赖。
- **可关闭页签 Notebook**：`custom_notebook.py`（做多标签页编辑器首选）。
- **代码编辑器四件套**：`codeview.py`（行号）+ `tktextext.py`（增强 Text）+ `editors.py`（标签管理）+ `roughparse.py`（语法着色分词，类 IDLE）。
- **设置面板 / 首次向导**：`config_ui.py`（Notebook 分页设置）、`first_run.py`（极简引导）。
- **主题与 DPI**：`plugins/base_ui_themes.py` 用 `add_ui_theme` + `scale()` 做明暗主题与高分屏适配——比第三方美化库更轻、零依赖的纯 ttk 路线。
- **后端隔离**：`running.BackendProxy`（本目录已收录）让 GUI 永不假死，呼应 IDLE 的 `rpc.py`。

> 运行完整 IDE：进入本目录双击 `启动.bat`（即 `python run.py` → `from thonny import launch`，运行本目录内 vendored 源码）；也可 `python -m thonny`（需另装）。

---

## `bulk-image-processor/` — 图片批量处理工具（单文件 GUI）

Haidar-Dagham 的 Bulk Image Processor 是一个**聚焦单一功能**的 tkinter 小工具，演示"一个窗口 + 一组参数 + 批量处理文件"的典型形态（vendored，MIT）。要点：

- **运行期零额外负担（仅 Pillow）**：除了图像处理的 Pillow，没有任何 GUI 框架依赖——纯标准库 ttk 画界面，是"小工具该长什么样"的干净范本。
- **批量文件选择模式**：用 `filedialog.askopenfilenames()` 多选 + 列表展示，比单个文件对话框更贴近真实批处理场景。
- **参数驱动处理**：缩放比例 / 输出格式 / 重命名规则 / 水印等参数集中在窗口，点"处理"后遍历文件——可直接抠走"参数表单 → 循环处理 → 进度反馈"这套骨架。
- **图标保活**：窗口/按钮图标用 `PhotoImage` 后存实例属性防 GC（`label.image = img` 套路），呼应技能编码铁律。
- **入口即类**：`ImageProcessorApp(root)` 接收 `Tk()` 根，符合技能"App 类只管一个窗口"的拆分约定。

> 运行：进入本目录双击 `启动.bat`（即 `python run.py` → `ImageProcessorApp(root)`）；依赖 `pip install Pillow`。

---

## `inventory-manager/` — 进销存管理后台（多模块 + sqlite3）

Rishikaa07 的 Inventory Management System 是一个**中等规模、多模块**的进销存应用，演示"真实业务后台如何用 tkinter + sqlite3 组织"（vendored；含 Pillow 仅用于图标/图片加载）。要点：

- **左侧图标菜单导航**：`Frame` + `PhotoImage` 图标按钮组成的侧边菜单（`employee/supplier/category/product/sales/chatbot/exit`），是后台/管理面板类应用最常见的布局模板，可直接复用。
- **子窗口用 Toplevel**：每个功能模块（员工/供应商/品类/商品/销售）都是独立 `Toplevel` 子窗体 + 自己的 CRUD 类——呼应技能"一个 View 类只管一个页面/Tab"的拆分约定。
- **sqlite3 数据层**：`ims.db` 裸库 + 各模块 `sqlite3.connect(r'ims.db')` 直连，覆盖"标准库裸库"这条数据层路线（与 `06-data-layer-sqlite.md` 的 Repository 模式对照，可借鉴其轻量写法）。
- **after 时钟刷新**：`lbl_clock.after(200, self.update_content)` 驱动状态栏时间与各项计数实时刷新——典型的"周期任务用 after、不进 mainloop"范式。
- **离线规则问答机器人**：`chatbot.py` 是纯规则匹配（无需 API key），演示"把简单 NLP 嵌进桌面应用"的轻量做法。
- **可移植性修复（已做）**：原仓库硬编码作者机器绝对路径（`C:\Users\ajayv\...` 下的 `checklist .png` / `images\menu_im.png` / `images\side.png` 与账单目录），已统一改为 `os.path.join(HERE, ...)`；`run.py` 启动时 `os.chdir(HERE)`，保证 `r'ims.db'` 相对路径在任意 cwd 下都能解析。

> 运行：进入本目录双击 `启动.bat`（即 `python run.py` → `dashboard.IMS(root)`）；依赖 `pip install Pillow`，数据库 `ims.db` 已随附样例数据。

---

## 真实案例研究（Real-World Tkinter Apps，外部参考）

> ⚠️ **与上面各目录的区别**：上面 `idle/` `thonny/` `pygubu-designer/` 等是**本技能已 vendored、可直接运行**的示例；下面这些是**社区里真实存在、但源码不在本技能目录内**的外部应用，仅作「架构与写法」参考，**不要逐行照抄**。
>
> **用途**：本段把社区里真实存在的 Tkinter 桌面应用作为「案例」引入，供你设计/编码时**借鉴其架构与写法**，而不是照抄。每个案例都尽量附**实拉取过的源码片段**（研究日期 2026-07-30），并标注「已核实 / 链接失效」。
>
> **怎么读**：① 先看「技术栈矩阵」定调；② 找和你项目同类的案例（ERP 看一类、BI 看二类）；③ 重点读「可借鉴点」与「反模式警示」——前者是可直接搬的模式，后者是这些真实项目里踩过的坑，本技能的铁律正是用来规避它们的。
>
> **与默认栈的关系**：本技能默认栈是 `03-ui-design.md` 的标准库 ttk.Style + sqlite3 + PyInstaller。下面案例里凡是引入 SQLAlchemy / Pandas / openpyxl / matplotlib 的，都属于「可选增强 / 第三方依赖」路线，打包体积与依赖代价见 `08-packaging.md`。

### 0 · 技术栈矩阵（一眼看全）

| # | 应用 | 类别 | GUI | 数据层 | 分析/图表 | 已核实 |
|---|------|------|-----|--------|-----------|--------|
| 1 | erp-python-simples | ERP | Tkinter + ttkthemes + tkcalendar | **SQLAlchemy + SQLite** | — | ✅ 源码 |
| 2 | Grocery Mart Inventory Manager | 进销存/POS | Tkinter + **ttkbootstrap** | SQLite | matplotlib / pandas / openpyxl / fpdf2 | ⚠️ 仅 PyPI 元数据（GitHub 404） |
| 3 | SIMPLY – Order Management | 订单管理 | Tkinter | **Excel (openpyxl)** | matplotlib | ✅ 源码 |
| 4 | Grocery Store Management V1.1 | 零售教学 | Tkinter | **JSON** | matplotlib | ✅ 源码 |
| 5 | Sales Data Analyzer | 销售 BI | Tkinter (ttk.Style clam) | pandas (读 Excel) | Matplotlib / Seaborn | ✅ 源码 |
| 6 | HR Analytics Dashboard | HR BI | Tkinter | pandas (读 CSV) | Matplotlib / SciPy | ✅ 源码 |
| 7 | Interactive Sales Dashboard | 销售 BI | **ttkbootstrap (darkly)** | pandas (读 Excel) | Matplotlib / Seaborn | ✅ 源码 |
| 8 | IDLE | 标杆 IDE | Tkinter | — | — | 参考（官方） |
| 9 | Leo Editor | 标杆大纲/IDE | 早期 Tkinter | — | — | 参考 |
| 10 | Pyspread | 标杆表格 | 早期 Tkinter→PyQt | — | — | 参考（已迁离 Tk） |

### 一、ERP / 进销存 / 订单管理

#### 1. erp-python-simples（家庭小企业 ERP）
- **定位**：为本地家族小企业做的桌面 ERP：客户 / 供应商 / 销售 / 收款 / 报表。
- **技术栈**：Tkinter + **SQLAlchemy + SQLite**；辅助 `ttkthemes.ThemedTk`、`tkcalendar.DateEntry`、`logging`。
- **架构 / 文件结构**（清晰的「数据层 ↔ UI 层」分离）：
  - `models.py`：SQLAlchemy 声明式 ORM 模型（`Vendedor`/`Cliente`/`Usuario`/`Venda`/`PagamentoVenda`…）
  - `database.py` + `create_db.py`：engine / session 工厂与建库
  - `*_operations.py`：`cliente_operations` / `fornecedor_operations` / `vendas_operation` / `pagamento_operations` / `pagamento_venda_operations` / `user_operations`——**每个实体一个操作模块**，返回 ORM 对象
  - `main.py`：UI 编排（表单构建、校验、调 operations）
  - `ui/ui_components.py`：可复用组件（如 `WidgetBuscaCliente`）
- **代表性代码摘录**：

  ```python
  # models.py —— ORM 关系定义（数据层）
  class Venda(Base):
      __tablename__ = 'vendas'
      id = Column(Integer, primary_key=True)
      numero_notinha = Column(Integer, nullable=False)
      valor_total = Column(Numeric(10,2), nullable=False)
      cliente_id = Column(Integer, ForeignKey('clientes.id'), nullable=False)
      vendedor_id = Column(Integer, ForeignKey('vendedores.id'), nullable=False)
      cliente = relationship("Cliente", back_populates="vendas")
      vendedor = relationship("Vendedor", back_populates="vendas")
      pagamentos = relationship("PagamentoVenda", back_populates="venda")
  ```

  ```python
  # main.py —— 表单保存流程（UI 层）
  def handle_salvar_venda():
      numero_notinha = entry_notinha.get()
      valor_notinha = entry_valor.get()
      if not numero_notinha or not valor_notinha:
          messagebox.showerror("Erro de Validação", "Número e Valor são obrigatórios.")
          return
      try:
          notinha_inteiro = int(numero_notinha)
          valor_decimal = float(valor_notinha.replace(",", "."))
      except ValueError:
          messagebox.showerror("Erro de Formato", "Devem ser números válidos.")
          return
      if 'id' not in dados_cliente_selecionado:
          messagebox.showwarning("Seleção Necessária", "Busque e selecione um cliente.")
          return
      dados_venda = {'numero_notinha': notinha_inteiro, 'valor_total': valor_decimal,
                     'cliente_id': dados_cliente_selecionado['id'], ...}
      resultado = add_venda(dados_venda)          # 调用数据层
      if resultado:
          messagebox.showinfo("Sucesso", f"Venda ID {resultado.id} salva!")
          limpar_formulario()
  ```

- **可借鉴点**：
  - **SQLAlchemy ORM 作为数据层**——比本技能默认的裸 `sqlite3` 更适合多实体、有外键/关系的业务（本技能的 `06-data-layer-sqlite.md` 用裸 sqlite3；这里展示了 ORM 替代路线）。
  - **「按实体拆 operations 模块」**——`*_operations.py` 把 CRUD 与业务逻辑从 UI 剥离，UI 只负责「取控件值 → 校验 → 调 operations → 弹 messagebox」。这正是 `02-architecture-mvc.md` 倡导的分层，但用函数式而非严格类。
  - `DateEntry` 处理日期、`logging` 全程打点、`replace(",", ".")` 做本地化数字解析——都是真实项目的小但实用的细节。
- **反模式警示**：UI 仍直接写在 `main.py` 里（非严格 MVC），表单重建用「销毁容器子控件」`for widget in container.winfo_children(): widget.destroy()`——能用，但本技能推荐用 `BasePage`/组件封装（`03-ui-design.md`）更稳。
- **源码**：https://github.com/augustodbatista/erp-python-simples （✅ 已核实）

#### 2. Grocery Mart Inventory Manager（杂货进销存 + POS）
- **定位**：本地优先（local-first）的杂货进销存 + POS + 销售趋势 KPI。
- **技术栈**（来自 PyPI `grocery-mart-application` 元数据，2026-07-30 抓取）：**Tkinter + ttkbootstrap + SQLite**；运行依赖 `ttkbootstrap>=1.10.1`、`pandas>=2.2`、`openpyxl>=3.1.2`、`fpdf2>=2.7.9`、`numpy<2,>=1.26`、`matplotlib`（销售趋势图表）；`Python >=3.11`；额外 extras：`opencv-contrib-python` + `pyzbar`（camera 条码）。
- **架构提示**：本地优先 + SQLite 数据层，但**在 GUI 之外叠了一整层分析/报表能力**（pandas 清洗、openpyxl 进出 Excel、fpdf2 导出 PDF、可选摄像头条码）。这是「标准库默认栈」之外的「重增强栈」范例。
- **可借鉴点**：想做带报表/导出的本地业务系统时，ttkbootstrap(界面) + SQLite(存) + pandas(算) + fpdf2(出 PDF) 是一条成熟组合；`Python>=3.11` 门槛注意（本技能默认栈无此限制）。
- **反模式警示 / 说明**：⚠️ **GitHub 仓库 `atifafzal786/Grocery_mart_Application` 在 2026-07-30 抓取时返回 404**（PyPI 的 `project_urls` 仍指向它，疑似仓库被删/改名）。本条目仅依据 PyPI 元数据 + 用户描述整理，**未核实源码**，不宜逐行引用。
- **源码**：PyPI https://pypi.org/project/grocery-mart-application/ ｜ GitHub（失效）https://github.com/atifafzal786/Grocery_mart_Application

#### 3. SIMPLY – Order Management System（配送订单管理）
- **定位**：面向印度配送公司的订单管理：库存、订单 CRUD、搜索/排序、从接单到发货全跟踪。
- **技术栈**：Tkinter + **Excel 作数据库（openpyxl）**；另用 `matplotlib`(FigureCanvasTkAgg) 画仪表盘、`PIL` 做图标、`numpy`。单文件 `main.py`。
- **架构 / 文件结构**：单文件 `main.py` + `Database.xlsx`（数据落地）+ `Images/`（图标素材）。用全局 `table_data` 缓存行，函数式页面切换 `dashboard()`/`delframe()`。
- **代表性代码摘录**：

  ```python
  # 用 Excel 充当数据库：首次运行自动建表
  import openpyxl
  if not os.path.exists('Database.xlsx'):
      wb = openpyxl.Workbook(); wb.save("Database.xlsx")
      ws = wb.active
      ws['A1'].value = "Order ID"; ws['B1'].value = "Item"
      ws['C1'].value = "Customer Name"; ws['D1'].value = "Address"; ws['E1'].value = "Status"
      wb.save("Database.xlsx")
  # 启动时全量读入内存
  wb = load_workbook("Database.xlsx"); ws = wb.active
  table_data = [[c.value for c in row] for row in ws.iter_rows(min_row=2, max_col=5)]
  ```

  ```python
  # 仪表盘页：先清后建（简单但有效）
  def delframe():
      for frame in main_frame.winfo_children():
          frame.destroy()
  def dashboard():
      delframe(); chv()                 # chv() 统计各状态订单数
      df = tk.Frame(main_frame, background="#15114a")
      ...
  ```

- **可借鉴点**：**Excel-as-database** 是「零安装、用户可双击打开看数据」的务实路线（适合内部小工具）；`matplotlib` 嵌进 Tkinter 仪表盘（`FigureCanvasTkAgg`）的写法可直接复用（见二类案例 6 的 `embed_chart`）；单文件 + 全局缓存 + 函数式页面切换（`dashboard()`/`delframe()`）的写法可作为小型工具骨架参考。
- **反模式警示**（正是本技能铁律要规避的）：① **全局可变状态** `table_data` 与 `np/nc/nd/...` 计数器；② 全部逻辑塞进单文件、无分层；③ 硬编码 `root.geometry("1600x900")`、`resizable(0,0)` 锁死尺寸；④ 图标路径 `./Images/logo.png` 硬编码。打包后这些都会出问题——参见 `03/08` 的「路径用 `sys.frozen` 检测」「grid 必设权重」「组件封装」等铁律。
- **源码**：https://github.com/subhojitghosh712/SIMPLY （✅ 已核实）

#### 4. Grocery Store Management V1.1（单店零售，教学级）
- **定位**：单店零售：商品管理、购物车、结账、订单历史、销售统计图。教学级、单文件。
- **技术栈**：Tkinter + **JSON 存储**；`webbrowser` 外链。
- **架构 / 文件结构**：单文件 `GroceryStoreApp.v1.1.py`，内含一个 `LANG` 双语字典（en/tr）做 i18n。
- **代表性代码摘录**：

  ```python
  # 用字典做 i18n：所有 UI 文案走 LANG[当前语言][key]
  LANG = {
      "en": {"add_cart":"Add Cart", "products":"Products", "complete_purchase":"Complete Purchase",
             "error_stock":"Only {} available in stock!", ...},
      "tr": {"add_cart":"Sepete Ekle", "products":"Ürünler", "complete_purchase":"Alışverişi Tamamla",
             "error_stock":"Stokta sadece {} ürün var!", ...},
  }
  # 使用：messagebox.showerror("!", LANG[cur]["error_stock"].format(qty))
  ```

- **可借鉴点**：**JSON 作为最简单的数据层**（比 Excel 更轻、比 SQLite 更易调试），适合教学/原型；**字典驱动的 i18n** 是多语言桌面 app 的轻量实现（替代 gettext）。
- **反模式警示**：同样单文件、硬编码路径；i18n 用字典而非标准 gettext，规模一大难维护。仅适合小项目。
- **源码**：https://github.com/EymenOzt/Grocery_Store_Management_V1.1 （✅ 已核实）

### 二、数据分析 / 桌面 BI 看板（Tkinter 前端 + Pandas）

#### 5. Sales Data Analyzer Application（销售分析器）
- **定位**：读 Excel 销售数据 → 描述统计 + 8 类图表 + 300DPI 导出。
- **技术栈**：Tkinter + **Pandas + Matplotlib/Seaborn**；单文件 `app.py`，class 化、自定义暗色主题。
- **代表性代码摘录**：

  ```python
  class DataAnalysisApp:
      def __init__(self, root):
          self.root = root
          self.root.title("Advanced Sales Analyzer"); self.root.geometry("1000x800")
          self.style = ttk.Style(); self.style.theme_use('clam')
          self.configure_styles()
          self.main_frame = ttk.Frame(self.root); self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
          # 文件选择区
          file_frame = ttk.Frame(self.main_frame); file_frame.pack(fill=tk.X, pady=10)
          ttk.Label(file_frame, text="Select Excel File:").pack(side=tk.LEFT, padx=5)
          self.file_entry = ttk.Entry(file_frame, width=50); self.file_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
          ttk.Button(file_frame, text="Browse", command=self.load_file).pack(side=tk.LEFT)
          # 输出控制台
          console_frame = ttk.LabelFrame(self.main_frame, text="Analysis Output")
          self.output_console = scrolledtext.ScrolledText(console_frame, height=15, ...)
  ```

- **可借鉴点**：**class 化 + ttk.Style 自定义主题 + ScrolledText 输出控制台**——结构清晰，是本技能「组件封装」铁律的好范例；`filedialog` 让用户选文件（对比案例 7 的硬编码路径，这是正确做法）。
- **反模式警示**：图表 DPI/配色写死在代码里（`COLORS` 字典硬编码），主题切换不灵活；不过比硬编码路径好。
- **源码**：https://github.com/Its-Vikas-xd/Sales-Data-Analyzer-Application （✅ 已核实）

#### 6. HR Analytics Dashboard（HR 分析看板）
- **定位**：HR CSV → 均值/协方差/偏度 + 二项分布计算器 + 图表。
- **技术栈**：Tkinter + **Pandas + Matplotlib + SciPy**；单文件 `prob.py`。
- **代表性代码摘录**（图表区切换的通用模式）：

  ```python
  # 清掉旧控件，再嵌入新视图 —— 所有「同一区域切换视图/图表」案例都可复用此模式
  def clear_frame():
      for widget in chart_area.winfo_children():
          widget.destroy()

  # 用 matplotlib 的 FigureCanvasTkAgg 把图嵌进 Tkinter —— 所有图表类案例都可复用
  def embed_chart(fig):
      clear_frame()
      canvas = FigureCanvasTkAgg(fig, master=chart_area)
      canvas.draw()
      canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

  def show_skewness():
      skew_years = stats.skew(df['YearsAtCompany'])
      skew_salary = stats.skew(df['PercentSalaryHike'])
      label_result.config(text=f"Skewness:\nYears: {skew_years:.2f}\nHike: {skew_salary:.2f}")
  ```

- **可借鉴点**：**`clear_frame()` + `FigureCanvasTkAgg(fig, master).draw()` 是 Tkinter 里「在同一区域切换多张图」的标准写法**，强烈建议直接搬（本技能若要做图表类 app，这就是模板）。`scipy.stats` / `math.comb` 做统计/概率，pandas 做聚合；matplotlib 负责出图。
- **反模式警示**：全局 `df` + 全局 `load_data()` 顶层调用（文件缺失时静默置空 DataFrame，后续才报错）——生产应改为「显式加载 + 异常提示 + 禁用分析按钮」。单文件但功能完整，适合参考写法而非结构。
- **源码**：https://github.com/Ahmed-Mohsen-2005/HR-Attrition-probability-project （✅ 已核实）

#### 7. Interactive Sales Dashboard（交互式销售看板）
- **定位**：电子商品销售：饼图（销售分布）、柱状图（数量/营收，可排序）、时序图（销量趋势），从 Excel 读取。
- **技术栈**：**ttkbootstrap (darkly 主题) + Pandas + Matplotlib/Seaborn**；单文件 `Sales_Data_Representation.py`（仓库 `rakesh-madadi/Datafactz-Project`）。
- **代表性代码摘录**：

  ```python
  import ttkbootstrap as ttk
  from ttkbootstrap.constants import *
  class InteractiveSalesDashboard:
      def __init__(self, master):
          self.master = master
          self.master.title("Sales Data Analysis Of Electronics")
          self.style = ttk.Style("darkly")          # ttkbootstrap 主题
          self.create_widgets(); self.load_and_process_data()

      def create_widgets(self):
          self.main_frame = ttk.Frame(self.master, padding="15")
          self.main_frame.pack(fill=BOTH, expand=YES)
          self.left_frame = ttk.Frame(self.main_frame, width=400); self.left_frame.pack(side=LEFT, fill=Y)
          # Treeview 摘要表 + 滚动条
          self.tree = ttk.Treeview(self.tree_frame, columns=("Product Name","Total Quantity","Total Revenue"), show='headings')
          self.tree_scroll = ttk.Scrollbar(self.tree_frame, orient="vertical", command=self.tree.yview)
          self.tree.configure(yscrollcommand=self.tree_scroll.set)
          # 右侧图表区
          self.right_frame = ttk.Frame(self.main_frame); self.right_frame.pack(side=LEFT, fill=BOTH, expand=YES)
          self.chart_frame = ttk.Frame(self.right_frame); self.chart_frame.pack(fill=BOTH, expand=YES)

      def load_and_process_data(self):
          self.df = pd.read_excel(r"<开发者本地桌面路径>\sales_data.xlsx")  # ⚠️ 硬编码绝对路径
          self.df = self.clean_data(self.df)
          self.summary_df = self.format_data(self.df)   # groupby 聚合
          self.display_data()

      def format_data(self, df):
          df['Total Revenue'] = df['Quantity'] * df['Sales Price'] / 1e6
          return df.groupby('Product Name').agg(
              Total_Quantity_Sold=('Quantity','sum'),
              Total_Revenue_M=('Total Revenue','sum')).reset_index()
  ```

- **可借鉴点**：**ttkbootstrap `Style("darkly")` + 左侧 Treeview 摘要 + 右侧图表区**的 BI 布局范式；`groupby().agg()` 做指标聚合、`Treeview` 展示摘要、`FigureCanvasTkAgg`(matplotlib) 嵌图，三者结合是销售看板的标准骨架。
- **反模式警示**：① **数据源写死为开发者本地桌面的绝对路径**——打包/换机必崩；应改 `filedialog.askopenfilename` 让用户选文件（对照案例 5 的正确做法）。② 单文件、路径写死。
- **源码**：https://github.com/rakesh-madadi/Datafactz-Project （✅ 已核实；原搜索名 interactive-sales-dashboard 指向此仓库）

### 三、标杆型 Tkinter 应用（参考架构，不 vendoring 源码）

> 这三类是「Tkinter 能做到多大」的参照系，重点看**架构思路**，不需要（也不建议）把它们的代码搬进技能。

#### 8. IDLE（Python 官方 IDE）
- **定位**：随 CPython 分发的官方 IDE，Guido 用 Tkinter 写。
- **参考点**：一个**长期维护、规模可观**的真实 Tkinter 应用长什么样——大量使用 `tk.Text` 作编辑器内核、多窗口、配置系统、较新版本已用 ttk 做主题。证明 Tkinter 完全撑得起「编辑器级」复杂度。
- **链接**：中文介绍 https://idle.org.cn/ ｜ 源码随 CPython（`Lib/idlelib`）

#### 9. Leo Editor（大纲编辑器 / IDE）
- **定位**：早期以 Tkinter 为 GUI 的知名大纲编辑器/IDE，后 GUI 层演化，但社区仍视其为 Tkinter 系代表。
- **参考点**：**树状大纲 + 多窗格 + 插件架构**在 Tkinter 上的实现范式；对做「带侧边树 + 多标签页」类工具的布局有启发。
- **链接**：https://leo-editor.github.io/leo-editor/ ｜ https://github.com/leo-editor/leo-editor

#### 10. Pyspread（Python 公式电子表格）
- **定位**：单元格直接写 Python 表达式的电子表格；早期 Tkinter 版本影响过很多「表格 + Python 表达式」思路。
- **参考点（溯源）**：做「网格 + 单元格求值」类工具（如本技能若要做类 Excel 界面）时的思路来源；**注意它已迁离 Tkinter 到 PyQt**——说明超大规模网格场景下 Tkinter 性能受限，需权衡。
- **链接**：https://pyspread.gitlab.io/ ｜ https://gitlab.com/pyspread/pyspread

### 横向结论：对本技能的启示

1. **数据层有四种真实路线**，按复杂度递增：JSON（案例 4）< Excel/openpyxl（案例 3）< SQLite 裸库（本技能默认）< **SQLAlchemy ORM（案例 1）**。本技能默认 sqlite3，但案例 1 证明 ORM 在多实体业务里更省心——需要时按 `06-data-layer-sqlite.md` 的思路升级即可。
2. **「Tkinter 前端 + pandas/matplotlib 后端」是 BI 类 app 的标准形态**（案例 5/6/7）。核心是两条复用模板：① `FigureCanvasTkAgg(fig, master).draw()` 嵌图 + `clear_frame()` 切图（案例 6）；② `filedialog` 选文件 + `ttk.Style` 自定义主题（案例 5）。
3. **第三方库（SQLAlchemy / Pandas / openpyxl / matplotlib）在真实项目里很常见**，按需引入即可，代价见 `08-packaging.md`。
4. **反复出现的反模式**（本技能铁律正是为规避它们）：硬编码绝对路径、单文件无分层、全局可变状态、锁死窗口尺寸、`import` 顶层做重 IO。凡案例里中招的，都已在 `03-ui-design.md` / `08-packaging.md` 有对应铁律。
5. **「链接失效」提醒**：案例 2（Grocery Mart）的原 GitHub 链接在 2026-07-30 已 404；开源项目会消失，案例价值在「思路」而非「逐行复制」。技能引用外部仓库时，优先以 PyPI/文档元数据佐证栈，再以源码佐证写法。

### 来源索引
- 一类：erp-python-simples（augustodbatista）、Grocery Mart（PyPI grocery-mart-application）、SIMPLY（subhojitghosh712）、Grocery Store V1.1（EymenOzt）
- 二类：Sales Data Analyzer（Its-Vikas-xd）、HR Analytics（Ahmed-Mohsen-2005）、Interactive Sales Dashboard（rakesh-madadi/Datafactz-Project）
- 三类：IDLE（idle.org.cn / CPython idlelib）、Leo（leo-editor.github.io）、Pyspread（pyspread.gitlab.io）
- 关联本技能：`03-ui-design.md`（标准库方案 + 组件封装铁律）、`06-data-layer-sqlite.md`（数据层）、`08-packaging.md`（第三方库打包）
