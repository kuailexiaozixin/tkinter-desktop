# Tkinter-Toolkit 社区控件库目录（全量）

> **来源与定位**
> 本文件内容提取自开源目录类应用 **Tkinter-Toolkit**（Akascape 维护的 tkinter 第三方库发现/检索工具，其数据库 `assets/database.json` 收录了大量 tkinter 生态的控件库与工具）。
> **本目录已补全为上游数据库的全量条目（共 74 条；已剔除本技能明确不覆盖的 `tkinterweb`）**，方便检索时「工具应列尽列」。
> **框架标注**：每条均标注其「框架」归属，便于按本技能「优先原生 ttk」的立场筛选：
> - **原生 ttk**：纯 tkinter/ttk 实现，零额外 GUI 框架依赖 → 本技能首选。
> - **CustomTkinter**：基于 `customtkinter` 框架（独立 GUI 框架，非原生 ttk），引入前需先装 customtkinter，请结合本技能立场评估。
> - **平台/Win32**：调用系统 API 或平台专属能力。
> - **工具**：开发辅助（设计器 / 打包 / 转换），非界面控件。
> **用途**：当标准库 `ttk` 确实缺少某类控件、且自研成本偏高时，可在此快速检索成熟的第三方库，按需引入。引入原生 ttk 库后须按 `references/08-packaging.md` 补 `hidden-import` / `--add-data`；引入 CustomTkinter 类库则等于引入一整套独立框架，须评估其体积与维护代价（见 `08-packaging.md`）。

## 使用原则

- **核心交互优先手搓标准库 ttk**：表格用 `Treeview`、布局用 `grid`/`pack`、弹窗用 `Toplevel`+`tk_*dialog`。只有当某控件标准库缺失且自研成本高时，才引入下方库——**优先选「原生 ttk」标注的条目**。
- **CustomTkinter 系列需谨慎**：它是一套独立 GUI 框架（替换 ttk 默认控件渲染），并非标准库增强；本技能默认栈基于原生 ttk，仅在确有强需求且评估过代价后才考虑。
- **「本技能覆盖」标注**：表示本技能已有该库的专属参考文档，深入用法去看对应文件，本文件只做目录索引。
- **链接以仓库为准**：下方仓库链接均为原始 `database.json` 中的 `repo_url`，引入前请确认仓库活跃度与许可。

---

## 分类目录

### 一、表格 / 列表 / 数据展示

| 库 | 作者 | 框架 | 简介 | 仓库 |
| --- | --- | --- | --- | --- |
| **TkSheet** | ragardner | 原生 ttk | 高性能表格/树形表格，支持百万行、可编辑、下拉/复选/进度条、行列拖拽 | https://github.com/ragardner/tksheet |
| **CTkTable** | Akascape | CustomTkinter | CTk 表格控件 | https://github.com/Akascape/CTkTable |
| **CTkListbox** | Akascape | CustomTkinter | 自定义列表框控件 | https://github.com/Akascape/CTkListbox |
| **tkFileBrowser** | Juliette Monsel | 原生 ttk | 文件浏览对话框，GTK 风格，替代 `tkinter.filedialog` | https://github.com/j4321/tkFileBrowser |
| **CTkFIleDialog** | limafresh | CustomTkinter | 可定制文件对话框 | https://github.com/limafresh/CTkFileDialog |
| **TkColorPicker** | Juliette Monsel | 原生 ttk | 颜色选择器（`ColorPicker` 类 + `askcolor`） | https://github.com/j4321/tkColorPicker |
| **CTkColorPicker** | Akascape | CustomTkinter | CTk 颜色选择器 | https://github.com/Akascape/CTkColorPicker |
| **TkFontChooser** | Juliette Monsel | 原生 ttk | 字体选择对话框（`FontChooser` 类 + `askfont`） | https://github.com/j4321/tkFontChooser |
| **TkCalendar** | Juliette Monsel | 原生 ttk | 日历 / `DateEntry` 控件，支持本地化与事件显示 | https://github.com/j4321/tkcalendar |
| **CTkCalendar** | Mustafa Hilmi YAVUZHAN | CustomTkinter | CTk 日历控件 | https://github.com/MustafaHilmiYAVUZHAN/CTkCalender |
| **TkTimePicker** | PaulleDemon | 原生 ttk | 可定制时钟时间选择器 | https://github.com/PaulleDemon/tkTimePicker |
| **CTkDataVisualizingWidgets** | ZikPin | CustomTkinter | 自定义日历、图与图表控件集 | https://github.com/ZikPin/CTkDataVisualizingWidgets |

### 二、图表与可视化

| 库 | 作者 | 框架 | 简介 | 仓库 |
| --- | --- | --- | --- | --- |
| **TkChart** | Thisal-D | 原生 ttk | 在 tkinter 窗口内绘制图表（折线/柱等），轻量 | https://github.com/Thisal-D/tkchart |
| **CTkChart** | Thisal-D | CustomTkinter | CTk 图表控件 | https://github.com/Thisal-D/ctkchart |
| **CTkRadarChart** | Akascape | CustomTkinter | CTk 雷达图 | https://github.com/Akascape/CTkRadarChart |
| **CTkPieChart** | Akascape | CustomTkinter | CTk 饼图 | https://github.com/Akascape/CTkPieChart |
| **CTkExtendedGraph** | iLollek | CustomTkinter | 可定制动态堆叠条形图 | https://github.com/iLollek/CTkExtendedGraph |
| **TkCurve** | Akascape | 原生 ttk | 简单贝塞尔曲线编辑器控件 | https://github.com/Akascape/TkCurve |
| **PY-gui-gauge** | Dongli Liu | 原生 ttk | 可定制的仪表盘（Gauge）控件 | https://github.com/Dongli99/PY-gui-gauge |
| **TkDial** | Akascape | 原生 ttk | 旋钮/圆盘控件，可替代 `Scale`/滑块 | https://github.com/Akascape/TkDial |
| **TkSliderWidget** | MengxLi | 原生 ttk | 多头滑块控件（一个轨道多个滑块） | https://github.com/MenxLi/tkSliderWidget |
| **TkVisualizer** | Akascape | 原生 ttk | 简易音频可视化控件 | https://github.com/Akascape/TkVisualizer |
| **CTkVisualizer** | iLollek | CustomTkinter | CTk 音频可视化控件 | https://github.com/iLollek/CTkVisualizer |

### 三、主题 / 外观 / 窗口样式

| 库 | 作者 | 框架 | 简介 | 仓库 |
| --- | --- | --- | --- | --- |
| **ttkthemes** | The TkinterEP team | 原生 ttk | ttk 主题集合 | https://github.com/TkinterEP/ttkthemes |
| **ttkwidgets** | The TkinterEP team | 原生 ttk | 控件集合（日历/计时器/筛选框等） | https://github.com/TkinterEP/ttkwidgets |
| **Sun-Valley-ttk-theme (sv-ttk)** | rdbende | 原生 ttk | Windows 11 风格 ttk 主题 | https://github.com/rdbende/Sun-Valley-ttk-theme |
| **Sun Valley Theme Colorizer** | Valer100 | 原生 ttk | 修改 sv-ttk 主题的强调色 | https://github.com/Valer100/Sun-Valley-Theme-Colorizer |
| **TkFontAwesome** | israel-dryer | 原生 ttk | 通过 tksvg 在 tkinter 中使用 FontAwesome 图标 | https://github.com/israel-dryer/TkFontAwesome |
| **ttkbootstrap** | israel-dryer | 原生 ttk | 主题/控件库（内置多套 Bootstrap 风格主题） | https://github.com/israel-dryer/ttkbootstrap |
| **AwesomeTkinter** | Aboghazala | 原生 ttk | 图像型控件库：3D 按钮、圆形进度、日期选择等 | https://github.com/Aboghazala/AwesomeTkinter |
| **ShadowTk** | vednig | 原生 ttk | 为 tkinter 控件添加阴影 | https://github.com/vednig/shadowTk |
| **winaccent** | Valer100 | 原生(Win32) | 读取 Windows 强调色供 tkinter 应用使用 | https://github.com/Valer100/winaccent |
| **py-window-styles** | Akascape | 原生(Win32) | Windows 11 窗口主题（亚克力/云母/透明等） | https://github.com/Akascape/py-window-styles |
| **hPyT** | Zingzy | 原生(Win32) | 操控窗口标题栏与透明度（隐藏/样式化） | https://github.com/zingzy/hPyT |
| **Rounded-Tk** | AZachia | 原生 ttk | 为 tkinter 窗口添加圆角 | https://github.com/AZachia/Rounded-Tk |
| **CTkThemeMaker** | Akascape | CustomTkinter | 轻量 CTk 主题制作 | https://github.com/Akascape/CTkThemeMaker |
| **CTkThemeBuilder** | Clive Bostock | CustomTkinter | 高级 CTk 主题制作 | https://github.com/avalon60/ctk_theme_builder |

### 四、文本与代码编辑

| 库 | 作者 | 框架 | 简介 | 仓库 |
| --- | --- | --- | --- | --- |
| **Chlorophyll** | rdbende | 原生 ttk | 带语法高亮与行号的代码编辑 `CodeView` 控件 | https://github.com/rdbende/chlorophyll |
| **TkLineNums** | Moosems | 原生 ttk | 为 tkinter `Text` 控件添加行号 | https://github.com/Moosems/TkLineNums |
| **CTkCodeBox** | Akascape | CustomTkinter | CTk 代码查看控件 | https://github.com/Akascape/CTkCodeBox |
| **tk_html_widgets (Tkhtmlview)** | paolo-gurisatti | 原生 ttk | 在 UI 中显示基础 HTML | https://github.com/paolo-gurisatti/tk_html_widgets |
| **libtextworker** | Le Bao Nguyen | 原生 ttk | 文本编辑/关于框/目录树等 tkinter 工具集 | https://github.com/lebao3105/libtextworker |

### 五、终端

| 库 | 作者 | 框架 | 简介 | 仓库 |
| --- | --- | --- | --- | --- |
| **TkTerm** | dhanoosu | 原生 ttk | 终端模拟器 `Frame` 控件（完整控制台仿真） | https://github.com/dhanoosu/TkTerm |
| **tkterminal** | Saad Mairaj | 原生 ttk | 终端控件，为 tkinter 提供终端支持 | https://github.com/Saadmairaj/tkterminal |

### 六、多媒体（视频 / GIF）

| 库 | 作者 | 框架 | 简介 | 仓库 |
| --- | --- | --- | --- | --- |
| **tkVideoPlayer** | PaulleDemon | 原生 ttk | 视频播放控件：播放/暂停/跳转/拖拽进度 | https://github.com/PaulleDemon/tkVideoPlayer |
| **AnimatedGIF** | olesk75 | 原生 ttk | 在 tkinter `Label` 中播放动画 GIF | https://github.com/olesk75/AnimatedGIF |
| **CTkGif** | IfTrueEqualsEqualsTrue | CustomTkinter | CTk GIF 控件 | https://github.com/IfTrueEqualsEqualsTrue/CTkGif |

### 七、画布 / 节点 / UI 框架

| 库 | 作者 | 框架 | 简介 | 仓库 |
| --- | --- | --- | --- | --- |
| **TkNodeSystem** | Akascape | 原生(Canvas) | 基于 tkinter Canvas 的节点编辑器（DAG，流程式操作） | https://github.com/Akascape/TkNodeSystem |
| **Maliang** | Xiaokang2022 | 原生(Canvas) | 轻量 UI 框架，全部用 Tk Canvas 绘制 | https://github.com/Xiaokang2022/maliang |

### 八、Web / PDF / 地图

| 库 | 作者 | 框架 | 简介 | 仓库 |
| --- | --- | --- | --- | --- |
| **TkinterMapView** | TomSchimansky | 原生 ttk | 地图显示控件（基于 tile 地图） | https://github.com/TomSchimansky/TkinterMapView |
| **CTkPDFViewer** | Akascape | CustomTkinter | CTk PDF 控件 | https://github.com/Akascape/CTkPDFViewer |

### 九、拖拽

| 库 | 作者 | 框架 | 简介 | 仓库 |
| --- | --- | --- | --- | --- |
| **tkinterdnd2** | Philippe Gagne | 原生(扩展) | 为 tkinter 提供原生拖放（Drag & Drop）支持 | https://github.com/pmgagne/tkinterdnd2 |

### 十、平台相关

| 库 | 作者 | 框架 | 简介 | 仓库 |
| --- | --- | --- | --- | --- |
| **tkmacosx** | Saad Mairaj | 原生(平台) | 修复 tkinter 在 macOS 上的问题，新增 `CircleButton`/`Colorscale` 等 | https://github.com/Saadmairaj/tkmacosx |
| **CustomTkinterTitlebar** | XiaoBaiYun | CustomTkinter | 可定制窗口标题栏 | https://github.com/littlewhitecloud/CustomTkinterTitlebar/ |
| **CTkXYFrame** | Akascape | CustomTkinter | 增强滚动框架 | https://github.com/Akascape/CTkXYFrame |
| **CTkSlideView** | rigvedmaanas | CustomTkinter | 幻灯片/轮播控件 | https://github.com/rigvedmaanas/CTkSlideView |

### 十一、工具与辅助（设计器 / 打包 / 转换 / 基础控件）

| 库 | 作者 | 框架 | 简介 | 仓库 |
| --- | --- | --- | --- | --- |
| **CustomTkinter** | TomSchimansky | CustomTkinter | 现代 UI 库（整套 CTk 控件的基础框架） | https://github.com/TomSchimansky/CustomTkinter |
| **auto-py-to-exe** | Brent Vollebregt | 工具 | 基于 PyInstaller 的 `.py → .exe` 图形化转换器 | https://github.com/brentvollebregt/auto-py-to-exe |
| **Tkinter_Quick_Layout** | EasyDevv | 工具 | 生成复杂 `grid` 布局参考代码的工具 | https://github.com/EasyDevv/Tkinter_Quick_Layout |
| **Tk-to-CTk** | Donny | 工具 | tkinter → customtkinter 转换工具 | https://github.com/Donny-GUI/tkinter-to-customtkinter-converter |
| **CTkComponents** | rudymohammadbali | CustomTkinter | 常用 UI 元素集 | https://github.com/rudymohammadbali/ctk_components |
| **CTkDesigner** | Akascape | CustomTkinter | CTk 图形化 GUI 设计器 | https://github.com/Akascape/CTkDesigner-Support |
| **CTkSeparator** | AJ-cubes | CustomTkinter | 可定制分隔线 | https://github.com/AJ-cubes/CTkSeparator |
| **CTkToggle** | Tchicdje Kouojip Joram Smith | CustomTkinter | 开关按钮控件 | https://github.com/DeltaGa/ctk_toggle |
| **CTkMeter** | Anand Krishnan | CustomTkinter | 圆形进度条 | https://github.com/anamite/ctk_widget |
| **CTkClock** | Arthur-101 | CustomTkinter | 时钟控件 | https://github.com/Arthur-101/CTkClock |
| **CTkMenuBar** | Akascape | CustomTkinter | 自定义工具栏 | https://github.com/Akascape/CTkMenuBar |
| **CTkPopupKeyboard** | Akascape | CustomTkinter | 屏幕键盘/小键盘控件 | https://github.com/Akascape/CTkPopupKeyboard |
| **CTkMessagebox** | Akascape | CustomTkinter | CTk 消息框 | https://github.com/Akascape/CTkMessagebox |
| **CTkTooltip** | Akascape | CustomTkinter | CTk 工具提示 | https://github.com/Akascape/CTkToolTip |
| **CTkScrollableDropdown** | Akascape | CustomTkinter | Combobox/OptionMenu 下拉控件 | https://github.com/Akascape/CTkScrollableDropdown |
| **CTkRangeSlider** | Akascape | CustomTkinter | 范围滑块控件 | https://github.com/Akascape/CTkRangeSlider |
| **Popup Menu（教程）** | Akascape | CustomTkinter | CTk 右键菜单实现教程 | https://www.akascape.com/coding/how-to-make-a-popup-menu-in-customtkinter |
| **Full Custom Window（模板）** | Akascape | CustomTkinter | 自定义窗口样式模板 | https://www.akascape.com/coding/full-python-window-template-with-new-header |

---

## 本技能已深度覆盖的库（跳转专属参考）

| 库 | 专属参考 | 说明 |
| --- | --- | --- |
| tksheet | `references/12-tksheet.md` | 高性能表格/树形表格 |
| tkchart (TkChart) | `references/10-tkchart.md` | 实时折线图控件（LineChart/Line） |

> 以上库在本目录中也有收录；本技能已为其写了完整参考，此处仅作索引互链，深入用法以专属参考为准。

## 打包提示（通用）

- **原生 ttk 库**：引入后 PyInstaller 常需补 `hidden-import`（如 `tkinterdnd2` 等）或 `--add-data`（含 `.tcl` 主题/图标资源）。具体见 `references/08-packaging.md` 与各库官方文档。
- **CustomTkinter 类库**：等于引入整套 customtkinter 框架，打包需按 customtkinter 官方指南补资源（主题/字体/`.tcl`），体积与维护代价显著高于原生 ttk，引入前务必评估。
- 体积增量差异大：纯 tkinter 实现（tksheet、TkDial、TkChart 等）增量小；带重依赖（pandas/matplotlib 等）或整套框架（customtkinter）的库增量大，引入前务必评估。
