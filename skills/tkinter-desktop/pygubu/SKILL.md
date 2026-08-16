---
name: pygubu
description: >
  pygubu + pygubu-designer 的完整指导技能（tkinter-desktop 的子技能）。
  pygubu 是 tkinter 的 RAD（快速应用开发）工具：把界面写成纯文本 XML（`.ui`），
  运行期用 `pygubu.Builder` 动态加载。本技能覆盖两种路径：
  A) AI 自动化 UI 设计闭环（核心，面向 LLM：生成/校验/修正 .ui，不依赖设计器 GUI）；
  B) pygubu-designer 可视化设计器的人类使用（可选路径）。
  当用户提到 "pygubu" "pygubu-designer" ".ui 界面" "界面用 Builder 加载" "RAD 界面设计"
  "AI 自动化 UI" 时使用本技能。
---

# pygubu · pygubu-designer 完整指导

> **定位**：本技能是 `tkinter-desktop` 技能下「pygubu / pygubu-designer」的**完整指导**（子技能）。
> pygubu 是 tkinter 的 **RAD（快速应用开发）工具**：把界面写成纯文本 XML（`.ui`），运行期用 `pygubu.Builder` 动态加载。它把「手写布局代码繁琐、难预览」的痛点，转化为「**界面即数据，可脚本化、可机器穷尽校验**」——AI 在后台生成、校验、修正 UI，无需人打开设计器。
>
> 内容综合自官方仓库 README（pygubu：https://github.com/alejandroautalan/pygubu ；pygubu-designer：https://github.com/alejandroautalan/pygubu-designer ）与 Wiki 整理。**许可证**：pygubu-designer 为 **GPL-3.0**；pygubu 核心与生成的纯 Python 代码按 **MIT** 许可（标准插件同 MIT；第三方插件见其各自许可）。

## 导航路由（MOC）

本技能内容分三块，按需进入：

### A. AI 自动化 UI 设计闭环（核心，面向 LLM）
面向 LLM 无人工介入的单一闭环：`.ui` 语法坑、无头语义校验、视觉截图校验、运行期 Builder 加载与回调绑定、打包要点。
→ 见下方 **§0–§14**（融合自原 `tkinter-desktop/references/14-pygubu.md`，内容完整无缺失）。
配套可运行脚本在父级 `tkinter-desktop/scripts/ai-ui-design/`（相对路径 `../scripts/ai-ui-design/`）：
`check_ui.py`（语义校验）、`check_ui_visual.py`（视觉校验）、`app.py`（运行期加载范本）。

### B. pygubu-designer 可视化设计器（人类路径，可选）
人类拖拽设计器的 GUI 使用与工程设置。AI 后台闭环**不依赖**此路径；仅在「为人类产出可用设计器工程 / 讲解设计器用法」时进入。
→ 见下方 **§15 设计器 GUI 使用**（综合自 wiki：Design-Screen / Code-Generator-Screen / Project-Settings / Design-Reuse 等）。

### C. 官方 Wiki 原文存档（权威参考）
官方 wiki 精选页面已归档在本技能 `references/wiki/`（剔除贡献者/纯示例杂项，保留开发相关 21 页 + images）。
→ 需要权威原文细节时，按下方 **§16 wiki 索引** 查对应 `references/wiki/<页面>.md`。

> **脚本路径**：本技能所有 `scripts/ai-ui-design/` 引用均指向父级 `tkinter-desktop/scripts/ai-ui-design/`（本子技能位于 `tkinter-desktop/pygubu/`，相对路径为 `../scripts/ai-ui-design/`）。

---

## 0 · 为什么走这条路线

手写 tkinter 布局代码繁琐、难预览、改动成本高。pygubu 把界面描述为纯文本 XML（`.ui`），
于是界面变成了**可脚本化、可机器穷尽校验**的东西——AI 可以像写代码一样生成/修改 UI，并用
`pygubu.Builder` 在后台**无头校验**（不弹窗、不用人操作），再把渲染结果截图做**视觉校验**。
这把「UI 设计」从「人肉拖拽」升级成「AI 闭环迭代」，与本技能「机器验证优先、不靠人代测」的纪律一致。

---

## 1 · 单一闭环（AI 后台执行，无分支）

```
1. AI 写/改 x.ui        （纯文本编辑：容器、控件、grid/pack、属性、command 回调 JSON）
        │
2. 无头校验             python check_ui.py x.ui
        │ 失败 → 读 traceback（resizable/pad/command 等坑）→ 回到 1 改
        │ 成功 → .ui 可构建，进入 3
        ▼
3. 运行期加载           Builder().add_from_file("x.ui").get_object("mainwindow").connect_callbacks(self)
        │
4.（可选）视觉截图校验   python check_ui_visual.py x.ui
        │ 渲染 → PIL 截图 → 几何检查 → 多模态 AI 审查
        │ 发现不可见/截断/间距问题 → 回到 1 改
        ▼
5. 交付                 界面与逻辑解耦：改 UI 不动 Python，改 Python 不动 UI
```

**关键纪律**：第 2 步无头校验是「编译 UI」，`add_from_file` 查 XML schema、`get_object` 真正构建
控件树并捕获 `TclError`；它**只能保证控件树能搭起来，看不到渲染效果**——所以第 4 步视觉校验是必要的互补。

> 配套可运行脚本都在 `scripts/ai-ui-design/`：`check_ui.py`（语义校验）、`check_ui_visual.py`（视觉校验）、`app.py`（运行期加载范本）。
> pygubu-designer 的**完整源码范本**在 `examples/pygubu-designer/pygubudesigner/`（像 IDLE 一样只读学习）。

---

## 2 · 工具与默认环境

- **pygubu 核心（运行期必需）**——加载并构建 XML 定义的 UI。包含：一组 **Pygubu 专属控件**（见 §8）、
  **Themes**（基于 ttkbootstrap、仅用 tkinter 实现的一套主题）、许多辅助类。
- **pygubu-designer（开发期工具，本路线不依赖）**——图形化创建 XML 的编辑器（人用）。
  AI 直接写 `.ui`，不经过设计器 GUI；designer 只是产出 `.ui` 的备选手段，本闭环不依赖它。

安装（运行期只需 `pygubu`；`pillow` 仅用于第 4 步截图校验，生产运行不需要）：

```bash
pip install pygubu pygubu-designer pillow
```

- pygubu 核心 / pygubu-designer 均要求 **Python >= 3.9**。
- 运行期只有 `pygubu`（Builder 加载器）进入 EXE；designer 是开发期工具，**严禁 hidden-import 进 EXE**（见 §11）。

---

## 3 · 运行期三步加载（标准用法，app.py 范本）

`scripts/ai-ui-design/app.py` 是范本，核心逻辑：

```python
import tkinter as tk
import tkinter.messagebox as mb
import pygubu

class App:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.builder = pygubu.Builder()
        self.builder.add_from_file("demo.ui")                       # ① 解析 XML
        self.mainwindow = self.builder.get_object("mainwindow", root)  # ② 取顶层控件
        self.tree = self.builder.get_object("tree", root)
        self.entry = self.builder.get_object("entry_name", root)
        self.builder.connect_callbacks(self)                        # ③ 绑定回调

    def on_add(self):
        text = self.entry.get().strip()
        if not text:
            mb.showwarning("提示", "请输入事项")
            return
        n = len(self.tree.get_children()) + 1
        self.tree.insert("", "end", values=(n, text))
        self.entry.delete(0, "end")

    def on_clear(self):
        for iid in self.tree.get_children():
            self.tree.delete(iid)

def main():
    root = tk.Tk()
    root.withdraw()        # 关键：.ui 的 mainwindow 是 Toplevel，root 应隐藏，否则多一个空白 "tk" 窗口
    App(root)
    root.mainloop()

if __name__ == "__main__":
    main()
```

> **Toplevel 陷阱**：若 `.ui` 的 `mainwindow` 是 `tk.Toplevel`，根 `tk.Tk()` 必须 `root.withdraw()`
> 隐藏，否则会弹出一个多余的空白根窗口。若 `mainwindow` 是 `tk.Tk`，则不要 withdraw。

> **交付形态唯一**：`.ui` 是唯一界面载体，运行期一律由 `pygubu.Builder` 加载（固定运行期依赖，冻结进 EXE）；**不采用「生成纯 Python 代码消除运行期依赖」的交付形态**。本闭环的校验/加载逻辑不变。

---

## 4 · `.ui` XML 格式要点

`.ui` 是标准 XML，描述窗口结构与属性。核心结构：

```xml
<interface>
  <object class="tk.Toplevel" id="mainwindow">
    <property name="title">My App</property>
    <property name="geometry">400x300</property>
    <child>
      <object class="ttk.Frame" id="mainframe">
        <property name="padding">10</property>
        <child>
          <object class="ttk.Button" id="quit_btn">
            <property name="text">Quit</property>
            <layout manager="pack">
              <property name="side">top</property>
            </layout>
            <!-- 按钮 command：用 command 属性的 JSON 对象（value=方法名，cbtype=simple） -->
            <property name="command">{"value": "on_quit", "cbtype": "simple"}</property>
          </object>
        </child>
      </object>
    </child>
  </object>
</interface>
```

- `<object class="..." id="...">`：控件类型（标准 tkinter/ttk 或 Pygubu 控件）与 id
- `<property>`：控件属性（text、title、padding、command…）
- `<layout manager="pack|grid|place">`：布局管理器与参数
- 按钮 `command`：**用 `<property name="command">` 的 JSON 对象** `{"value": "on_quit", "cbtype": "simple"}`，
  `connect_callbacks` 读取 `value`（方法名）并绑定到 controller 的同名方法（见 §5）。
  注意：`<connection type="command" handler="..."/>` **不能**绑定按钮 command——那是给事件序列
  （如 `<connection type="1" handler="on_key"/>` 按键、`<connection type="FocusIn" handler="..."/>` 焦点）用的，
  写成 `<connection type="command">` 按钮点了不会触发任何回调。

---

## 5 · Builder 类 API（运行期加载 .ui）

常用方法：

- `Builder()` — 构造
- `.add_from_file(path)` — 从 `.ui` 文件加载 UI 定义
- `.add_from_string(xml_str)` — 从 XML 字符串加载
- `.get_object(id, master=None)` — 取回某个 id 对应的控件实例（通常是根窗口 `mainwindow`）
- `.get_objects()` — 取回所有对象
- `.connect_callbacks(controller)` — 把 `.ui` 里 `command` 属性 JSON 的 `value` 字段（方法名）绑定到 `controller` 的同名方法
- `.get_variable(id)` / `.import_variables(master)` — 变量（如 `tk.StringVar`）管理
- `.add_resource_path(path)` — **图片等资源的额外搜索目录**；必须在创建任何使用自定义图片的控件**之前**调用（见 §8A）
- `.get_image(name)` — 按 `.ui` 里 image 属性的 key 取回 `tkinter` 图片对象（见 §8A）
- `.replace_child(...)` / `.append(...)` / `.insert(...)` — 动态增删控件

> **控件变量（tkvariable）**：交互控件（`Entry`/`Radiobutton`/`Checkbutton`/`Scale`/`Combobox`…）的 `variable`/`textvariable` 属性可绑定控制变量。`.ui` 里用 combo 指定类型，运行期用 `.get_variable(name)` 取回。类型：`StringVar`（默认）/ `IntVar` / `DoubleVar` / `BooleanVar`。**未初始化，直到用户首次操作控件**。示例：`self.builder.get_variable('radiovar').get()`。

---

## 6 · `.ui` 关键语法坑（AI 手写 .ui 最易踩，按频率排列）

### 6.1 `resizable` 取固定枚举，不是布尔
```xml
<property name="resizable">both</property>     <!-- ✅ none / both / horizontally / vertically -->
<property name="resizable">False</property>    <!-- ❌ KeyError：False 不在枚举内 -->
```

### 6.2 `padx/pady` 用单值或空格分隔串，不是 python 元组
```xml
<property name="padding">10</property>          <!-- ✅ 单值 -->
<property name="pady">0 10 0 0</property>        <!-- ✅ 空格分隔（上 右 下 左） -->
<property name="pady">(0, 10)</property>         <!-- ❌ pygubu 原样传给 Tcl：bad pad value "(0, 10)" -->
```

### 6.3 按钮 `command` 必须用 JSON 对象（且用 `command` 属性，不是 `<connection>`）

**正确写法**——把命令写成 `command` 属性的 JSON 对象：

```xml
<property name="command">
  {"value": "on_add", "cbtype": "simple"}
</property>
```

`connect_callbacks(self)` 读取 JSON 里的 `value`（方法名），接到本类同名方法 `on_add()`；
普通按钮 `cbtype` 用 `simple`。**写错 JSON（如裸字符串 `on_add`）会直接 `json.loads` 报错。**

> ⚠️ **不要**用 `<connection type="command" handler="on_add"/>` 来绑按钮命令——`<connection>` 是给
> **事件序列**用的（如 `<connection type="1" handler="on_key"/>` 按键、`<connection type="FocusIn" handler="..."/>` 焦点），
> 对按钮 `command` 它**不生效**（实测 `btn.cget("command")` 为空，点了不触发任何回调）。

### 6.4 `font` 可用 dict 字面量
```xml
<property name="font">{'family': 'Microsoft YaHei UI', 'size': 14, 'weight': 'bold'}</property>
```

### 6.5 各属性命名即控件构造参数
`.ui` 的 `<property>` 大多直接映射 ttk 控件构造参数（`text`/`title`/`padding`/`borderwidth`/
`relief` 等）。ttk 控件不支持经典 `bg/fg`；要改颜色走 `ttk.Style`，或给包裹 Frame 设
`borderwidth`+`relief`（见 §10 实战坑）。

### 6.6 `ttk.Treeview` 列定义必须用子节点 + `column_anchor` 必显式

pygubu 0.40 的 `TTKTreeviewBO` **只认** `<object class="ttk.Treeview.Column">` 子节点。
**legacy `<columns><column/></columns>` 会被静默忽略** → 0 列空白表格，不报错。

此外，Column 的 `column_anchor` 属性 pygubu 默认值是空串 `""`，运行期必然抛
`TclError: ambiguous anchor ""`。每次写 Column 都必须显式写：

```xml
<child>
  <object class="ttk.Treeview.Column" id="idx">
    <property name="text">#</property>
    <property name="heading_anchor">center</property>   <!-- 缺失无害(默认w)，但建议写明 -->
    <property name="column_anchor">center</property>    <!-- 必须写！否则运行期崩 -->
    <property name="width">60</property>
    <property name="stretch">false</property>
  </object>
</child>
```

> 合法 anchor 值：`n / ne / e / se / s / sw / w / nw / center`。

### 6.7 `ttk.Notebook` 必须用 `ttk.Notebook.Tab` 做中间层

正确层级：`ttk.Notebook > ttk.Notebook.Tab > ttk.Frame > 具体控件`。
漏了 Tab 层 → Frame 被静默丢弃 → 0 个页签，不报错。

---

## 7 · 控件级坑（pygubu 特有，非 tkinter 本体问题）

> 以下坑**只在用 pygubu Builder 加载 `.ui` 时出现**，手写 tkinter/ttk 代码不会遇到。
> 已在 pygubu **0.40.1 / Tk 8.6 / Python 3.13** 上逐条实测确认。

### 7.1 `ttk.Treeview` 列定义必须用子节点，不能用 legacy `<columns>`

pygubu 的 `TTKTreeviewBO`（`allowed_children = ("ttk.Treeview.Column",)`）只认
`<object class="ttk.Treeview.Column">` 子节点。**legacy `<columns><column/></columns>` 会被静默忽略**
——不报错、不警告、构建成功、但 `tree["columns"] == []`，界面是一张全空白表格。

```xml
<!-- ❌ 静默失败：0 列空白表格 -->
<property name="show">headings</property>
<columns>
  <column name="idx" text="#"/>
  <column name="task" text="事项"/>
</columns>

<!-- ✅ 正确写法 -->
<property name="show">headings</property>
<child>
  <object class="ttk.Treeview.Column" id="idx">
    <property name="text">#</property>
    <property name="heading_anchor">center</property>
    <property name="column_anchor">center</property>
    <property name="width">60</property>
    <property name="stretch">false</property>
  </object>
</child>
```

### 7.2 `ttk.Treeview.Column` 的 `column_anchor` 必须显式写

pygubu 源码（`TTKTreeviewColumnBO._get_column_properties`）中：

| 属性 | 默认值 | 缺失后果 |
|------|--------|----------|
| `heading_anchor` | `tk.W`（即 `"w"`） | 无害 |
| `column_anchor` | **空串 `""`** | **运行期 `TclError: ambiguous anchor ""` 崩溃** |

合法值：`n / ne / e / se / s / sw / w / nw / center`。**每次写 Column 都必须同时写这两个属性**，
否则要么崩（`column_anchor`），要么行为不明确（`heading_anchor`）。

### 7.3 `ttk.Notebook` 的直接子节点必须是 `ttk.Notebook.Tab`

正确层级：`ttk.Notebook > ttk.Notebook.Tab > ttk.Frame > 具体控件`。
若把 `Frame` 直接挂在 `Notebook` 下（漏了 Tab 层），pygubu **静默丢弃**该 Frame →
`nb.tabs() == ()`，0 个页签，不报任何错误。

### 7.4 `connect_callbacks({})` vs `connect_callbacks(stub)`

| 传入对象 | 返回值 | 含义 |
|----------|--------|------|
| `{}`（空 dict） | `['on_add', 'on_clear', ...]` | **声明的全部回调名**（controller 必须有同名方法） |
| 带 `__getattr__` 的 stub 对象 | `None` | pygubu 认为每个回调都已连上，**什么都查不出来** |

审计「controller 是否少写了某个回调」时，**必须传空 dict**；stub 只适合纯渲染场景
（如 `check_ui_visual.py` 截图时不关心回调是否真的存在）。

---

## 8 · Pygubu 专属控件与插件

**专属控件**（随核心提供，`pygubu` 自带、开箱即用）：

**容器/布局类**
- `AccordionFrame` — 手风琴式折叠面板，点击标题展开/收起一块内容区
- `AutoArrangeFrame` — 自动排列子控件（按行列均分排布）的容器，省去手写布局
- `HideableFrame` — 可折叠/隐藏的面板，带展开收起按钮
- `ScrolledFrame` — 自带滚动条的框架，内容超长时可滚动查看
- `DockFrame` / `DockPane` / `DockWidget` — 停靠布局系统：可拖拽/停靠的窗口与面板（类似 IDE 侧栏）

**输入/选择类**
- `ColorInput` — 颜色选择输入（弹出取色器）
- `FontInput` — 字体选择输入
- `PathChooserInput` / `PathChooserButton` — 文件/路径选择（输入框版 / 按钮版）
- `Combobox` — 增强下拉组合框

**展示/交互类**
- `CalendarFrame` — 日历选择器
- `Dialog` — 对话框容器（模态窗口骨架）
- `EditableTreeview` — 树形表格，**单元格可直接编辑**
- `FilterableTreeview` — 树形表格，**自带过滤/搜索框**
- `Tooltip` / `Tooltipttk` — 鼠标悬停提示（tk 版 / ttk 版）
- `Pygubu Forms` — pygubu 表单系统，用于组合/复用子表单与复合控件

**插件**（外部控件集，启用后即可在 `.ui` 里使用）：

- `awesometkinter`（AwesomeTkinter）— 增强控件集：扁平按钮、卡片、密码框、进度环等现代 UI 组件
- `tkcalendar` — 日历 + `DateEntry` 日期选择控件
- `tkintermapview` — 嵌入式**交互地图**（OpenStreetMap 瓦片）
- `tkintertable` — 可编辑表格控件
- `tksheet` — 高性能**电子表格/数据网格**（类 Excel 交互）
- `tkinterweb` — 嵌入式 HTML 浏览器控件
- `TkinterModernThemes` — 现代化主题外观
- `ttkwidgets` — ttk 增强控件集（autocomplete、checkbox tree、toggle 等）
- `customtkinter` — 现代扁平风格 UI 框架（圆角、暗色主题）

安装扩展控件集（随 designer 附带，`[all]` 装全部）：

```bash
pip install pygubu-designer[AwesomeTkinter]   # 单个
pip install pygubu-designer[all]              # 全部扩展控件集
```

> 例如装了 `tksheet` 插件，就能在 pygubu-designer 里直接拖出 tksheet 表格（见 `13-tksheet.md`）。
> 运行期 EXE 是否需要这些第三方控件，取决于 `.ui` 里是否真的用了它们；若未使用，按 §11 原则 exclude 掉，避免体积膨胀。

---

## 8A · 运行时高级功能（要点 + Wiki 原文见 `references/wiki/`）

以下功能是 `.ui` 加载后常见的运行时需求，补充 §5/§6 之外的能力。**要点与实测坑位**列于下；
完整操作与代码示例见 `references/wiki/` 对应页面（Command-Property / Variable-Property / Image-Property / Menus / Delete-Window-Event / Ttk-Styles-Support / Design-Reuse）。

### 8A.1 菜单（Menus）→ `references/wiki/Menus.md`
- 用 `Menu` + `Menuitem.Command` / `Checkbutton` / `Radiobutton` / `Submenu` / `Separator` 构建。
- **坑位**：菜单默认不可见，**必须手动挂到窗口**：`self.mainwindow.configure(menu=builder.get_object('mainmenu', ...))`。
- 菜单项回调用 `command` 属性 JSON（同按钮），`connect_callbacks(self)` 绑定。
- **坑位**：`command_id_arg=True` 时回调会收到被点菜单项的 **id** 作额外参数——可一个方法处理多个菜单项（`def on_mfile_item_clicked(self, itemid)`）。

### 8A.2 窗口关闭事件（WM_DELETE_WINDOW）→ `references/wiki/Delete-Window-Event.md`
- 用顶层窗口 `protocol("WM_DELETE_WINDOW", callback)` 捕获点 × 关闭。
- **坑位**：根是 **Frame**（master 为 `tk.Tk`）时 `master.protocol(...)` + `self.mainwindow.master.destroy()`；根是 **Toplevel** 时 `self.mainwindow.protocol(...)` + `self.mainwindow.destroy()`。

### 8A.3 图片属性（image）→ `references/wiki/Image-Property.md`
- `image` 属性接受图片文件名作 `.ui` 里的 key；`add_resource_path()` 追加搜索目录（**必须在创建任何使用图片的控件之前调用**）；`get_image(name)` 取回 `tkinter` 图片对象。

### 8A.4 ttk 自定义样式定义文件 → `references/wiki/Ttk-Styles-Support.md` / `Project-Settings.md`
- 一个 python 模块，内含 `setup_ttk_styles(master=None)` 函数。
- **坑位/约定**：样式名以目标 ttk 类名结尾（`MyBlueLabels.TLabel`），才能在 `.ui` 的 `style` 属性下拉选择；`.ui` 里 `<property name="style">MyBlueLabels.TLabel</property>`，运行期先调 `setup_ttk_styles()`。与 §6.5 一致：ttk 改颜色走 Style，不走 `bg/fg`。

### 8A.5 自定义控件注册（BuilderObject / register_widget）→ `references/wiki/Design-Reuse.md`
- 用 `BuilderObject` + `register_widget` 把第三方/自建控件纳入 pygubu 体系（从而能在 `.ui` 里用）。
- 核心：`register_widget('buildermodule.widgetname', BuilderCls, 'Label', ('ttk', 'Group'))`；`classname` 用 `模块.控件` 约定存进 `.ui` 的 `class` 属性。
- `OPTIONS_STANDARD` / `OPTIONS_SPECIFIC` / `OPTIONS_CUSTOM` 声明可编辑属性；`ro_properties` 标只读；`_process_property_value` 做类型转换；`register_custom_property` 注册属性编辑器。
- 属性编辑器类型：`entry` / `choice` / `colorentry` / `naturalnumber` / `spinbox` / `checkbutton` / `geometryentry` / `fontentry` / `imageentry` / `stickyentry` / `tkvarentry` 等约 20 种。
- **AI 闭环**：直接用 §8 现成插件控件即可，无需注册自定义控件。

## 9 · 语义校验 `check_ui.py`（「编译 UI」）

`scripts/ai-ui-design/check_ui.py`——不弹窗，对 `.ui` 做**语义级校验**（不只是数控件个数）：

```bash
# 默认校验同目录所有 *.ui；也可指定任意 .ui
python check_ui.py
python check_ui.py path/to/xxx.ui [b.ui]
```

**检查项**（已在 pygubu 0.40.1 / Tk 8.6 上逐条实测）：

| 层级 | 检查项 | 级别 | 说明 |
|------|--------|------|------|
| XML | legacy `<columns>` 用法 | **E** | pygubu 静默忽略 → 0 列空白表格 |
| XML | Treeview 无 Column 子节点 | **E** | 同上（0 列） |
| XML | Column 缺 `column_anchor` | **E** | 运行期 `TclError: ambiguous anchor ""` 崩溃 |
| XML | Column 缺 `heading_anchor` | W | 无害（默认 w），建议显式写明 |
| XML | Column 缺 `text` | W | 标题回落为 id，界面露出程序员标识符 |
| XML | Notebook 直接子节点非 Tab | **E** | 内容静默丢失 → 0 页签 |
| XML | `command` 非 JSON | **E** | 构建期 `JSONDecodeError` |
| 运行时 | Treeview 实际列数为 0 | **E** | XML 层漏掉的兜底 |
| 运行时 | Notebook 实际页签数为 0 | **E** | 同上 |
| 运行时 | 列 anchor / heading_anchor 非法值 | **E** | 兜底 |
| 信息 | 声明的回调名列表 | I | controller 必须有同名方法 |

逻辑要点：
- **XML 层预检**：用 ElementTree 解析 `.ui`，不依赖运行时就能抓出「还没 build 就已知的坑」
- **运行时构建**：`root.withdraw()` + `Builder().add_from_file()` + `get_object()` 真正建控件树
- **id 映射**：通过 `builder.objects` 把控件映射回 `.ui` 的 id（错误信息可读）
- **回调审计**：传空 dict 给 `connect_callbacks({})` 获取声明的全部回调名
  （⚠️ 不要传带 `__getattr__` 的 stub——那会让 pygubu 认为全连上、返回 None）

**退出码**：0=通过，1=存在 E 级问题。可接进 CI / 自动化脚本做门禁。

---

## 10 · 视觉截图校验 `check_ui_visual.py`（语义校验的互补）

`check_ui.py` 只确认「控件树能构建 + 语义正确」，但**看不到渲染效果**。常见视觉问题它完全抓不到：
控件与背景融为一体（如空 Treeview 无边框）、文字截断、间距不均、子控件超出父容器被裁切。

`scripts/ai-ui-design/check_ui_visual.py` 补上这一环：

```bash
cd scripts/ai-ui-design
python check_ui_visual.py        # 渲染同目录所有 *.ui
python check_ui_visual.py x.ui   # 渲染指定文件
```

脚本做的事：
1. **真正渲染窗口**：Builder 构建 → `deiconify()` + `lift()` + `update()` 让窗口画出来
2. **PIL `ImageGrab` 截图**：按窗口 bbox 抓取像素，保存为 `<名字>_preview.png`
3. **几何检查**：递归遍历所有子控件，报告**零尺寸 / 超出父容器可视范围**
4. **多模态 AI 审查**：AI 用视觉能力查看 `_preview.png`，发现布局/配色/截断等人类才能看到的问题

> 前置：`pygubu` + `pillow`（`scripts/ai-ui-design/requirements.txt`）。截图依赖真实显示环境；
> 在 CI/无头服务器上此步自动跳过。截图可能被其他窗口遮挡（`ImageGrab.grab` 抓屏幕像素），
> 可把目标窗口移到安全位置再截。

**真实案例**（本 demo 首次截图即触发）：空 `ttk.Treeview` 与父 Frame 背景完全同色，用户看不到
列表区域在哪。无头 `check_ui.py` 全程报 OK，只有截图暴露了问题。修复：给包裹 Treeview 的 Frame
加 `borderwidth="1"` + `relief="solid"`（ttk.Treeview 本身不支持 `borderwidth`/`relief`，须在父 Frame 上做）。

---

## 11 · 打包要点（运行期 vs 开发期）

> 完整打包规则与机制分析见父级 **`../references/08-packaging.md`**（§「误把设计器 hidden-import 进 EXE」「pygubu 默认排除 PIL 与第三方插件」）。此处只列 pygubu 打包的**核心命令**：

```bash
--hidden-import=pygubu                     # 核心必需：运行期 Builder 加载 .ui
--exclude-module=PIL                       # 默认排除（stockimage 惰性分支，占约 21% 体积）
--exclude-module=pygubu.plugins.ttkwidgets
--exclude-module=pygubu.plugins.customtkinter
# 严禁 --hidden-import=pygubudesigner（设计器依赖链 numpy 等，EXE 凭空 +26MB 死重）
```

**pygubu 特有的 Wiki 排障补充**（父级 08-packaging 未含）：
- `ImportError: cannot import name 'ImageFont' from 'PIL'`：加 `--hidden-import=PIL.ImageFont`（连同 `PIL.ImageDraw`）。
- `Exception: Class "tkinterweb.HtmlFrame" not mapped`（用 tkinterweb 等第三方控件）：用 spec 文件的 `collect_all` 收集：
  ```python
  from PyInstaller.utils.hooks import collect_all
  datas, binaries, hiddenimports = [], [], []
  for ret in (collect_all('tkinterweb'), collect_all('pygubu')):
      datas += ret[0]; binaries += ret[1]; hiddenimports += ret[2]
  ```

## 12 · 本技能环境快速命令清单

```bash
# —— 启动可视化设计器（人用；AI 闭环不依赖）——
# 双击 examples/pygubu-designer/启动.bat
# 或（依赖已 pip install）：python -m pygubudesigner

# —— AI 语义校验（不弹窗，检查 Treeview/Notebook/anchor/command JSON/回调声明）——
cd scripts/ai-ui-design
python check_ui.py            # 校验同目录所有 *.ui（默认 demo.ui）
python check_ui.py xxx.ui     # 校验指定 .ui（可多文件）

# —— AI 视觉截图校验（需 Pillow + 显示环境，输出 <名字>_preview.png）——
python check_ui_visual.py     # 渲染同目录所有 *.ui
python check_ui_visual.py x   # 渲染指定 .ui

# —— 运行 demo 应用（加载 demo.ui）——
python app.py
```

> 标准用法：先 `pip install pygubu pygubu-designer pillow`，再直接 `python -m pygubudesigner` /
> `python check_ui.py` 等。

---

## 13 · 许可与边界

- pygubu-designer 本体 **GPL-3.0**；pygubu 核心与生成的纯 Python 代码按 **MIT**（标准插件同 MIT）。
- `examples/pygubu-designer/pygubudesigner/` 是 vendored 源码，**只读学习**，不要当业务依赖引入。
- 本文件与 `scripts/ai-ui-design/` 不构成交付物的一部分；它们是「AI 设计 UI 的方法与工具」，
  产出的 `.ui` / 生成的代码才进入你的项目。

---

## 14 · 官方参考链接（已下载整理于本文件）

- pygubu 核心：https://github.com/alejandroautalan/pygubu
- pygubu-designer：https://github.com/alejandroautalan/pygubu-designer
- Wiki（设计器文档）：https://github.com/alejandroautalan/pygubu-designer/wiki
- 安装相关 Wiki：https://github.com/alejandroautalan/pygubu-designer/wiki/Installation-&-Related
- 启动 Wiki：https://github.com/alejaroautalan/pygubu-designer/wiki/Launch
- Wiki 关键页面（本文档 §5/§8/§8A 综合自）：Command-Property、Variable-Property、Image-Property、Menus、Delete-Window-Event、Design-Reuse、Ttk-Styles-Support、Project-Settings、Begin-with-Toplevel、Pad-a-Side、Code-Generator-Screen、Pyinstaller-troubleshooting
- 示例目录：https://github.com/alejandroautalan/pygubu-designer/tree/master/examples
- 入门视频：http://youtu.be/wuzV9P8geDg
- tkinter 参考：TkDocs、Python 官方 tk 文档、Tkinter 8.5 reference (effbot)、Tcl/Tk 9.0 / 8.6 Manual

---

## 15 · pygubu-designer 可视化设计器（人类路径，可选）

> 本技能核心是 **§0–§14 的 AI 自动化闭环**（面向 LLM，不依赖设计器 GUI）。本节仅作人类可视化设计器入口；AI 后台写 `.ui` 不需要进入。完整 GUI 操作见 `references/wiki/` 对应页面。

- 启动：`python -m pygubudesigner`，或双击 `examples/pygubu-designer/启动.bat`
- 设计界面四面板（Components Palette / Project Tree / Properties Panel / Preview Panel）→ `references/wiki/Design-Screen.md`
- 代码生成器（Application / Code Script / Custom Widget 模板）→ `references/wiki/Code-Generator-Screen.md`
  - ⚠️ 本技能默认 `.ui` + Builder 形态（§3），**不采用** Code Script「消除运行期依赖」形态。
- 项目设置（General / Code / Styles / Custom widgets）→ `references/wiki/Project-Settings.md`
- **坑位**：生成 `.py` 会被覆盖，**禁止手改**；自定义逻辑用**继承**扩展基类（`MyappBase` → `class Myapp(MyappBase)`）→ `references/wiki/Design-Code-Iteration.md`

## 16 · 官方 Wiki 存档索引（references/wiki/）

本技能已将官方 wiki 的**精选 21 页**归档到 `references/wiki/`（剔除贡献者流程、纯示例等杂项；`images/` 保留必要截图）。需要权威原文细节时按主题查对应页面：

| 主题 | 页面 |
|------|------|
| 总览/入门 | `Home` · `Installation-&-Related` · `Launch` · `Requirements` · `Learning-Tk-&-Tkinter` |
| 设计器界面 | `Design-Screen` · `Code-Generator-Screen` · `Project-Settings` |
| 属性与事件 | `Command-Property` · `Variable-Property` · `Image-Property` · `Pad-a-Side` · `Begin-with-Toplevel` · `Delete-Window-Event` |
| 菜单 | `Menus` |
| 自定义控件 | `Design-Reuse` |
| 样式 | `Ttk-Styles-Support` |
| 打包排障 | `Pyinstaller-troubleshooting` |
| 扩展控件 | `Additional-widget-sets` |
| 其他 | `Language-Translation` · `FAQ` |

> 原文全部保留（未改动），供权威查阅；本文档 §0–§14 已对这些内容做了面向 AI 闭环的提炼与实测验证。
