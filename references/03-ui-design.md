# 03 界面设计（方法论 + 战术 + 现代增强）

> 本篇合并三份同源资料：**设计方法论**（Design System 视角）、**战术规范**（布局/样式/DPI/字体）、**现代增强**（ttk.Style 深度定制、Canvas 自绘、第三方库可选方案）。自上而下阅读：先建立设计系统认知，再落地战术，最后按需引入增强。
>
> **默认路线用标准库**（仅 tkinter + sqlite3，EXE ~11–12MB）。第三方美化库是可选增强，按需引入即可；引入后打包须按 `08-packaging.md` 的「第三方美化库打包」补 hidden-import / add-data。

---

## 0. 核心心法：做"设计系统"，不要"堆控件"

丑界面不是某个按钮没调色，而是**缺少统一决策**。

> 真正专业的 Tkinter UI = 变量集中管理 + 控件统一封装 + 页面结构标准化。

把颜色、间距、圆角、字体抽象成 **Design Token（设计变量）**，而不是写死在几十个控件里。项目一大，改主色调要找几十处就是埋雷。

**标准库版（推荐默认起点）**——用 `THEME` 字典做唯一真相来源，启动时灌进 `ttk.Style`：

```python
# common/ui.py
THEME = {
    # 主色 / 强调
    "primary":       "#2563eb",
    "primary_hover": "#1d4ed8",
    "primary_light": "#eff6ff",
    # 功能语义色
    "success": "#16a34a",
    "warning": "#d97706",
    "danger":  "#dc2626",
    "danger_hover": "#b91c1c",
    # 中性色
    "bg_app":   "#f5f6f8",
    "bg_card":  "white",
    "text_primary": "#0f172a",
    "text_muted":   "#64748b",
    # 边框 / 分隔
    "border":      "#cbd5e1",
    "border_light":"#e2e8f0",
    "trough":      "#f1f5f9",
    "thumb":       "#cbd5e1",
    "thumb_hover": "#94a3b8",
    # 间距 / 圆角
    "radius":   6,
    "pad_sm":   6,
    "pad_md":   12,
}

def setup_style(style: ttk.Style, t: dict = THEME):
    style.theme_use("clam")
    style.configure("TFrame", background=t["bg_app"])
    style.configure("TButton", padding=(10, 5), relief="flat")
    style.configure("Accent.TButton", foreground="white",
                    background=t["primary"], relief="flat")
    style.map("Accent.TButton",
              background=[("active", t["primary_hover"]),
                          ("disabled", "#93c5fd")])
    style.configure("Danger.TButton", foreground="white",
                    background=t["danger"], relief="flat")
    style.map("Danger.TButton", background=[("active", t["danger_hover"])])
    style.configure("Card.TFrame", background=t["bg_card"], relief="solid",
                    borderwidth=1)
    style.configure(".", font=("Microsoft YaHei UI", 10))   # 全局兜底字体
```

业务代码从此**只引用样式名**，不出现颜色字面值：

```python
ttk.Button(bar, text="保存", style="Accent.TButton", command=on_save)
ttk.Button(bar, text="删除", style="Danger.TButton", command=on_del)
```

**第三方库版**——把 Token 直接喂给控件封装类，见 §7。

---

## 1. 两条路线决策框架（标准库 vs 第三方，按需求取舍）

| 档位 | 手段 | 新增依赖 | EXE 体积 | 推荐度 |
| ---- | ---- | -------- | -------- | ------ |
| **A 标准库** | ttk.Style 深度定制 + Canvas 自绘 + 字体/emoji 图标 + 架构增强 | 无 | ~12MB | ⭐⭐⭐ 推荐起点 |

> 实战场：先用 A 档做出 90% 的现代感（本技能的 `common/ui.py` 已落地 A 档基础）。仅在 A 档不够时升级 C，并按 `08-packaging.md` 补 hidden-import / add-data。
> **选择原则**：简单工具走原生参数优化；正式项目/强视觉需求再上第三方；无论如何**不要为视觉效果牺牲功能稳定、不要过度美化**。

---

## 2. ttk.Style 的真相：它不是 CSS

绝大多数"样式不生效"的困惑，源于误以为 `ttk.Style` 像 CSS。关键认知：

- **本质是 theme + layout + element 三层绑定**，不解析 CSS、无选择器、无继承链。`configure("TButton", background=...)` 只是对控件类的一次性属性覆盖。
- **默认 / winnative / aqua 主题屏蔽颜色**：`configure` 的颜色类参数基本被忽略，**必须先 `theme_use("clam")`**（`clam` 是唯一跨平台行为一致的 theme）。
- **`configure` 管静态，`map` 管状态**：hover/active/disabled 必须靠 `style.map(...)`，只靠 configure 只能设默认态。
- **自定义样式名必须显式传 `style=`**：`"Accent.TButton"` 不会自动匹配，控件创建时要写 `style="Accent.TButton"`。
- **layout 必须显式重建**：想改 padding/border 等底层结构，要先 `print(style.layout("TButton"))` 看清元素，再 `style.layout("My.TButton", [...])` 重建，否则配置静默失败。
- **Tk 版本**：Tk 8.6.9+ 对 `clam` 圆角支持更好；旧版本仍显直角。
- **跨平台失效**：Windows `winnative` / macOS `aqua` 会屏蔽绝大多数 `configure` 颜色（OS 级限制，非 bug）；自定义样式在 Linux/macOS 失效更频繁，跨平台产品务必在目标平台实测。

**调试口诀**（比反复试颜色有用）：

```python
print(style.theme_names())        # 看可用主题
print(style.layout("TButton"))     # 看元素结构，定位 configure 失效原因
print(style.element_options("Button.border"))  # 看某元素可配属性
```

---

## 3. 布局哲学：复合布局，Frame 即布局单元

单一用 `pack` 或 `grid` 都容易塌。共识做法：

- **外层用 grid 做区域划分，内层 Frame 用 pack 自适应排列**；同一容器**绝不混用** pack 与 grid（混用会直接抛错）。
- Frame 作为"布局单元"：每个功能块包一层 Frame，Frame 内部管理自己的小布局，整体更稳。

```python
main.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
main.columnconfigure(0, weight=1)
left = ttk.Frame(main);  left.pack(side="left",  fill="y")      # 侧边栏
right = ttk.Frame(main); right.pack(side="left", fill="both", expand=True)  # 内容区
```

### 布局三板斧（grid 为主）

1. **权重决定伸缩**：容器必须显式配置，否则窗口拉大内容不动：

```python
frame.columnconfigure(0, weight=1)   # 第0列吃掉多余宽度
frame.rowconfigure(1, weight=1)      # 表格所在行吃掉多余高度
tree.grid(row=1, column=0, sticky="nsew")
```

2. **sticky + padding 统一**：输入控件 `sticky="ew"`，表格 `sticky="nsew"`，标签 `sticky="w"`；统一 `padx=8, pady=4`，别每处随手写不同值。
3. **经典页面骨架**（工具条 + 表格 + 状态栏）：

```python
self.columnconfigure(0, weight=1)
self.rowconfigure(1, weight=1)
toolbar = ttk.Frame(self);  toolbar.grid(row=0, column=0, sticky="ew", padx=8, pady=(8, 4))
body    = ttk.Frame(self);  body.grid(row=1, column=0, sticky="nsew", padx=8)
status  = ttk.Label(self, anchor="w"); status.grid(row=2, column=0, sticky="ew", padx=8, pady=4)
```

> 侧边栏 + 内容区骨架见验证项目 `views/main_window.py`。

---

## 4. ttk.Style 主题化（战术）

起手式：

```python
style = ttk.Style()
style.theme_use("clam")          # Windows 上比默认 vista 更可定制
style.configure("TButton", padding=6)
# ⚠️ rowheight 不可用默认值 20！必须用 font.metrics() 计算（详见 §5.1）
# 此处为快速起手值，正式项目应调用 setup_treeview_rowheight()
style.configure("Treeview", rowheight=26)
style.configure("Treeview.Heading", font=("Microsoft YaHei UI", 10, "bold"))
style.configure("Accent.TButton", foreground="#fff", background="#2563eb")
style.map("Accent.TButton", background=[("active", "#1d4ed8"), ("disabled", "#93c5fd")])
```

- **规则**：自定义样式名 = `前缀.T控件名`（如 `Accent.TButton`、`Danger.TLabel`）。`configure` 管静态外观，`map` 管状态（active/disabled/selected）外观。
- **vista/xpnative 主题下很多颜色改不动**（如 Treeview heading 背景、按钮背景），这不是代码错误而是原生主题限制——需要深度定制时先 `theme_use("clam")`。
- **语义色号约定**（与业务含义绑定）：主行动 `#2563eb`、成功 `#16a34a`、警示 `#dc2626`、次要文字 `#6b7280`。

### 表格 Treeview（行高 / 斑马纹 / 配色）

> **⚠️ 行高必须用 `font.metrics('linespace')` 计算**（§5.1 完整公式与对照表）。
> 下方 `rowheight=30` 是 10pt YaHei UI 舒适模式的近似值；正式项目应调用 `setup_treeview_rowheight()` 函数。

```python
style.configure("Treeview", rowheight=30, font=("Microsoft YaHei UI", 10),
                background="white", fieldbackground="white",
                foreground="#1e293b", bordercolor="#e2e8f0",
                lightcolor="#e2e8f0", darkcolor="#e2e8f0")
style.configure("Treeview.Heading", font=("Microsoft YaHei UI", 10, "bold"),
                background="#f1f5f9", foreground="#0f172a", relief="flat", borderwidth=1)
style.map("Treeview", background=[("selected", "#dbeafe")],
          foreground=[("selected", "#0f172a")])
# 斑马纹：插入行时打 tag
tree.tag_configure("odd", background="#f8fafc")
tree.tag_configure("even", background="white")
```

### 滚动条 / 进度条 / 下拉 / 输入框 雅化

```python
style.configure("Vertical.TScrollbar", troughcolor="#f1f5f9",
                thumbcolor="#cbd5e1", bordercolor="#e2e8f0",
                arrowcolor="#64748b", width=10)
style.map("Vertical.TScrollbar", thumbcolor=[("active", "#94a3b8")])
style.configure("TProgressbar", thickness=8, troughcolor="#e2e8f0",
                bordercolor="#e2e8f0", lightcolor="#2563eb", darkcolor="#2563eb")
style.configure("TCombobox", arrowcolor="#64748b", arrowsize=14,
                fieldbackground="white", foreground="#1e293b")
style.map("TCombobox", fieldbackground=[("focus", "white")],
          bordercolor=[("focus", "#2563eb")])
style.configure("TEntry", fieldbackground="white", bordercolor="#cbd5e1",
                lightcolor="#cbd5e1", darkcolor="#cbd5e1", padding=5)
style.map("TEntry", bordercolor=[("focus", "#2563eb")])
```

### 自定义元素布局（给卡片加左侧色条等）

`style.layout()` 可重组控件内部元素；更稳定做法是**用 Frame 包出"左侧色条 + 内容"的现代卡片**，避免 element 复杂度：

```python
card = ttk.Frame(parent, style="Card.TFrame")
bar = tk.Frame(card, bg="#2563eb", width=4)
bar.pack(side="left", fill="y")
body = ttk.Frame(card); body.pack(side="left", fill="both", expand=True, padx=12, pady=10)
```

### 悬停交互（Sidebar 导航）

ttk 按钮的 `active` 状态在鼠标悬停时自动触发，配合 `style.map` 即可；对经典 `tk.Button` 侧边栏，则绑定 `<Enter>/<Leave>` 手动换色：

```python
def _enter(e): btn.configure(bg=ACTIVE_BG)
def _leave(e): btn.configure(bg=IDLE_BG)
btn.bind("<Enter>", _enter); btn.bind("<Leave>", _leave)
```

> 验证项目 `views/main_window.py` 已把侧边栏导航改为 ttk + `style.map` 悬停高亮方案（`Sidebar.TButton` / `SidebarActive.TButton`）。

---

## 5. 配色、字体与 DPI

### 三色 + 语义色原则

- **三色原则**：主色 + 辅助色 + 背景色，杜绝色彩杂乱。语义色：primary / success / warning / danger；中性色：文本主/次、卡片背景。
- **字体层级**：标题 / 正文 / 次要 三档，用 `size` + `weight` 区分，引导视线。中文统一"Microsoft YaHei UI"，英文数字可用 Consolas/Impact。
- **留白即呼吸**：大量用 `padx/pady`，拥挤是"丑"的首要原因。边距集中由 THEME 常量定义。

### DPI 感知（Windows 必做）

不设置时高分屏整个窗口发虚。**必须在创建 `Tk()` 之前调用**：

```python
import ctypes, sys
if sys.platform == "win32":
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(1)  # Per-Monitor 用 2
    except Exception:
        pass  # Win8 以下无 shcore
```

副作用：DPI 感知后系统不再放大字体，需自己放大——用 `root.tk.call('tk', 'scaling')` 读缩放，或统一设默认字体（见下）。

### 中文字体

Windows 下 Tk 默认字体在中文界面显示偏小且混杂。统一设置：

```python
from tkinter import font
for name in ("TkDefaultFont", "TkTextFont", "TkHeadingFont", "TkMenuFont"):
    font.nametofont(name).configure(family="Microsoft YaHei UI", size=10)
```

`nametofont` 修改必须在控件创建前完成才全局生效；ttk.Style 单独 configure 过 font 的样式不受影响，需要一并改。

### 控件间距与行高规范（必须遵守）

> **核心问题**：ttk/tkinter 的默认间距参数是为 96DPI 英文环境设计的（Treeview 默认 `rowheight=20`、控件默认 padding 极小）。
> 在中文界面或高 DPI 显示器上，这些默认值会导致**行与行之间太紧、文字被截断或显示不全**（尤其是含下行字母 g/j/p/q/y 的英文、或笔画密集的中文）。
> **必须在 `setup_style()` 里一次性统一修正，不可依赖默认值。**

#### 5.1 Treeview 行高：用 font.metrics() 算，不要猜硬编码

`rowheight` 必须根据实际字体行高计算，而非写死一个 magic number：

```python
import tkinter.font as tkfont

def setup_treeview_rowheight(style: ttk.Style, font_spec=None):
    """根据字体度量自动计算 Treeview 行高，确保文字不被截断。
    
    公式：rowheight = font.linespace + vertical_reserve
    - linespace：字体自身行高（含 ascent + descent + leading）
    - vertical_reserve：额外预留像素，补偿行间视觉呼吸感
      紧凑模式 +6，舒适模式 +8~10，宽松模式 +12+
    """
    base_font = tkfont.Font(family="Microsoft YaHei UI", size=10) if font_spec is None \
                else tkfont.Font(**(font_spec if isinstance(font_spec, dict)
                                     else {"family": font_spec}))
    linespace = base_font.metrics("linespace")   # 通常 10pt 字体 → ~15-17px
    rowheight = linespace + 8                     # 舒适模式：+8px 预留
    
    style.configure("Treeview", rowheight=rowheight)
    return rowheight

# 使用示例：在 setup_style() 中调用
# 实际返回值通常在 24~28 之间（取决于字体和 DPI）
```

**为什么不能依赖默认值 `rowheight=20`：**

| 场景 | 默认 20px | 正确计算后 | 截图症状 |
|------|----------|-----------|---------|
| 10pt 中文（Microsoft YaHei UI） | ⚠️ 行紧、笔画挤 | 24~26px | 行间无呼吸 |
| 10pt 英文混合数字 | ⚠️ 下行字母截断（g/j/p/q/y 底部被切） | 23~25px | 文字显示不全 |
| 150% DPI + 10pt 字体 | ❌ 严重截断 | 28~32px | 如截图 2 的 Sales Data Analyzer |
| 11pt 标题字体用于 Treeview | ❌ 几乎肯定截断 | 27~30px | 表格不可读 |

**快速对照表（常用字体 × 模式）：**

| 字体 | size | linespace（约） | 紧凑(+6) | **推荐(+8)** | 宽松(+12) |
|------|------|----------------|-----------|-------------|------------|
| Microsoft YaHei UI | 9 | 14 | 20 | **22** | 26 |
| Microsoft YaHei UI | 10 | 16 | 22 | **24** | 28 |
| Microsoft YaHei UI | 11 | 18 | 24 | **26** | 30 |
| Consolas（等宽/代码） | 10 | 16 | 22 | **24** | 28 |

> **规则**：任何使用 Treeview 的项目，`setup_style()` 里**必须调用上述函数设置 rowheight**。禁止使用默认值 20。

#### 5.2 表单字段垂直间距

表单中「标签 + 输入框」的行间节奏是拥挤感的另一大来源：

```python
# === 错误：无 pady 或 值太小 ===
label.grid(row=0, column=0, sticky="w")
entry.grid(row=0, column=1, sticky="ew")
# 结果：标签和输入框紧贴上下行，整体"糊"在一起

# === 正确：统一 pady + 分组间距 ===
FORM_PAD_Y = 4          # 同一行内标签与输入框的垂直对齐余量
GROUP_PAD_Y = 10        # 两组字段之间的间距（如"用户名"组与"地址"组之间）

# 标签行
ttk.Label(form, text="用户名：").grid(row=0, column=0, sticky="w",
                                       padx=8, pady=FORM_PAD_Y)
ttk.Entry(form).grid(row=0, column=1, sticky="ew",
                          padx=8, pady=FORM_PAD_Y)

# 下一组字段——加大间距
ttk.Label(form, text="备注：").grid(row=1, column=0, sticky="n", padx=8,
                                       pady=(GROUP_PAD_Y, FORM_PAD_Y))
ttk.Text(form, height=4).grid(row=1, column=1, sticky="nsew", padx=8,
                                pady=(GROUP_PAD_Y, FORM_PAD_Y))
```

**间距常量纳入 THEME 字典：**

```python
THEME = {
    # ... 已有颜色配置 ...
    # 间距体系（四档）
    "pad_xs":   4,    # 行内紧凑（标签-输入框对齐）
    "pad_sm":   6,    # 相邻紧密元素（按钮组内）
    "pad_md":   10,   # 分组间隔（表单两组之间）
    "pad_lg":   16,   # 区块间隔（卡片与卡片 / 区块标题与内容）
    "pad_xl":   24,   # 页面级边距（主内容区距窗口边缘）
}
```

#### 5.3 常见控件的间距检查清单

| 控件 | 必设参数 | 推荐值 | 不设的后果 |
|------|---------|--------|-----------|
| `ttk.Treeview` | `rowheight=` | `linespace + 8`（≈24~26） | **文字截断、行紧叠**（截图 2 的典型问题） |
| `ttk.Button` | `padding=` | `(10, 5)` 或 `(12, 6)` | 按钮太小、点击困难 |
| `ttk.Entry` | `padding=` | `5`（内部留白） | 光标贴边、输入文字挤 |
| `TLabel`（表单） | grid `pady=` | `THEME["pad_xs"]`（4） | 与上下行粘连 |
| `Frame`（卡片） | pack/grid `padx/pady` | `THEME["pad_md"]`（10） | 卡片内容贴边 |
| `Toplevel`（对话框）| 内部 Frame `padx/pady` | `THEME["pad_lg"]`（16） | 对话框内容顶边 |
| `ttk.Notebook` | 内部 Frame `padx/pady` | `THEME["pad_md"]`（10） | Tab 内容贴边 |
| `ttk.Panedwindow` | `paneborderwidth` + `sashwidth` | `2` + `4` | 分隔线太细或拖动区太窄 |

#### 5.4 高 DPI 下的间距放大

开启 DPI 感知（§5 上文 `SetProcessDpiAwareness`）后，不仅字体需要调整，间距也应按比例放大：

```python
def dpi_scale(base_value: int, root: tk.Tk) -> int:
    """将基础间距值按 DPI 缩放因子放大。
    
    用法：pad_scaled = dpi_scale(THEME["pad_md"], root)
    """
    scaling = float(root.tk.call('tk', 'scaling'))  # 通常 1.0 / 1.25 / 1.33 / 1.5 / 1.75 / 2.0
    return max(base_value, int(base_value * scaling))

# 高 DPI 下自动放大的间距
style.configure("Treeview", rowheight=dpi_scale(
    tkfont.Font(family="Microsoft YaHei UI", size=10).metrics("linespace") + 8,
    root))
```

> **反模式警示**：截图 2（Sales Data Analyzer）的 Treeview 问题就是典型的「未设 rowheight + 未做 DPI 适配」叠加后果。
> 社区示例代码常犯此错——它们通常在作者的 96DPI 屏幕上看起来还行，换到 125%/150% DPI 或中文字体下立刻暴露。
> **本技能的模板和示例已内置正确的间距设置，新项目必须继承此规范。**

### emoji / 符号图标（标准库方案）

直接用系统 emoji 字体即可，无需图片资源：

```python
ttk.Label(frm, text="📊  仪表盘")    # 依赖系统 Segoe UI Emoji / 微软雅黑 emoji
```

> 注意：`--windowed` 下诊断走 logging 文件，**不要**在日志里打 emoji（GBK 控制台会炸，见 `08-packaging.md` 控制台编码）。UI 文本里的 emoji 没问题。

### 图片图标（PIL，可选）

需要 PNG/SVG 等精致图标时引入 Pillow（会 +几 MB）：

```python
from PIL import Image, ImageTk
img = ImageTk.PhotoImage(Image.open("assets/icon.png").resize((20, 20)))
label = ttk.Label(frm, image=img); label.image = img   # 关键：保持引用
```

引入 Pillow 即增加第三方依赖；打包需 `--add-data` 打入 assets。

---

## 6. Canvas 与 Text：标准库高级控件（强烈推荐）

`tk.Canvas` 是做出「图表 / 仪表 / 进度环」等现代视觉的标准库利器，完全可控、体积小。

### 横向条形图（仪表盘「各项目研发费用」）

```python
def draw_bar_chart(canvas, items, color="#2563eb", label_w=120, max_val=None):
    """items: [(label, value), ...]；在 canvas 上画横向条形图。"""
    canvas.delete("all")
    w = canvas.winfo_width() or 360
    h = canvas.winfo_height() or 240
    top, row_h = 6, max(20, (h - 12) / max(len(items), 1))
    bar_max = max(10, w - label_w - 70)
    if max_val is None:
        max_val = max((v for _, v in items), default=1) or 1
    for i, (label, val) in enumerate(items):
        y = top + i * row_h
        canvas.create_text(6, y + row_h / 2, anchor="w", text=str(label)[:14],
                           font=("Microsoft YaHei UI", 9), fill="#475569")
        bw = int((val / max_val) * bar_max) if max_val else 0
        canvas.create_rectangle(label_w, y + 3, label_w + bw, y + row_h - 3,
                                fill=color, outline="")
        canvas.create_text(label_w + bw + 6, y + row_h / 2, anchor="w",
                           text=f"{val:,.0f}", font=("Microsoft YaHei UI", 9),
                           fill="#0f172a")
```

### 环形进度 / 仪表（资本化率、预算执行率）

```python
def draw_ring(canvas, ratio, color="#16a34a", size=120, text=None):
    canvas.delete("all")
    r = size / 2 - 8
    cx = canvas.winfo_width() / 2 or size / 2
    cy = canvas.winfo_height() / 2 or size / 2
    canvas.create_oval(cx - r, cy - r, cx + r, cy + r, outline="#e2e8f0", width=10)
    ratio = max(0.0, min(1.0, ratio))
    if ratio > 0:
        canvas.create_arc(cx - r, cy - r, cx + r, cy + r, start=90,
                          extent=-ratio * 360, outline=color, width=10, style="arc")
    label = text if text is not None else f"{ratio * 100:.0f}%"
    canvas.create_text(cx, cy, text=label, font=("Microsoft YaHei UI", 14, "bold"),
                       fill="#0f172a")
```

### 折线 / 迷你走势（Sparkline）

`canvas.create_line([(x0,y0),(x1,y1),...])` + `canvas.create_polygon(..., fill=...)` 填充。

> 注意：**Canvas 绘制必须在主线程**；数据计算放 worker 线程，结果经 queue + `after` 回主线程后再调 `draw_*`（见 §8 / `05-threading-and-async.md`）。

### 6.4 Canvas 交互深挖（图元增删改 / 命中测试 / 拖拽 / 滚动）

> 事实：只有 `tk.Canvas`，无 `ttk.Canvas`。Canvas 里一切可见元素都是"图元（item）"，每个图元有整数 id（创建时返回）；坐标默认是画布坐标系。

**创建与删除图元**：

```python
cv = tk.Canvas(frame, width=400, height=300, bg="white", highlightthickness=0)  # highlightthickness=0 去聚焦边框
r  = cv.create_rectangle(10, 10, 80, 60, fill="#2563eb", tags=("box", "sel"))
o  = cv.create_oval(100, 10, 140, 50, tags=("circ",))
t  = cv.create_text(200, 30, text="标签", anchor="w", font=("Microsoft YaHei UI", 10))
ln = cv.create_line(0, 0, 100, 100)
pg = cv.create_polygon(0, 0, 50, 0, 25, 40, fill="orange")
ar = cv.create_arc(0, 0, 60, 60, start=0, extent=90, style="arc")
```

所有 `create_*` 均实测存在：`create_rectangle` / `create_oval` / `create_text` / `create_line` / `create_polygon` / `create_arc` / `create_bitmap` / `create_image` / `create_window`。重绘范式（rd-expense 做法）：先 `cv.delete("all")` 再重画，避免图元堆积。

**tags 分组与查询**：

```python
cv.addtag_all("all2")
print(cv.gettags(r))                        # ('box', 'sel')
print(cv.type(r))                           # 'rectangle'
print(cv.find_withtag("box"))               # 含 r 的图元 id 元组
print(cv.find_all())                        # 全部图元 id
```

可用：`addtag_*`、`gettags(id)`、`find_withtag(tag)`、`find_all()`、`dtag(id, tag)`。

⚠️ 实测：**没有 `find_within` 方法**。命中测试用下面的 `find_closest` / `find_overlapping` / `find_enclosed`（均已验证存在）。

**修改图元**：

```python
cv.itemconfig(r, fill="blue")               # 改属性
print(cv.itemcget(r, "fill"))               # 'blue'
cv.coords(r, 0, 0, 20, 20)                 # 重设坐标
cv.move(r, 5, 5)                           # 相对平移
cv.scale(r, 0, 0, 2, 2)                    # 以 (0,0) 为锚点缩放 2x
cv.delete(r)                                # 删单个；cv.delete("all") 全删
cv.tag_raise(r)                             # 提到顶层；tag_lower 反之
```

**命中测试与拖拽**：

```python
def on_box_click(event):
    item = cv.find_withtag("current")       # 被点的图元（"current" 是 Tk 维护的特殊 tag）
    print("clicked item", item)
cv.tag_bind("box", "<Button-1>", on_box_click)
cv.tag_bind(r, "<Enter>", lambda e: cv.itemconfig(r, fill="red"))
cv.tag_bind(r, "<Leave>", lambda e: cv.itemconfig(r, fill="blue"))

# 几何命中（适合"点空白处"逻辑）
nearest  = cv.find_closest(event.x, event.y)            # 离点击点最近的图元
hits     = cv.find_overlapping(x1, y1, x2, y2)          # 矩形/椭圆区域内图元
enclosed = cv.find_enclosed(x1, y1, x2, y2)             # 完全落在区域内的图元
```

可拖拽图元（标准范式）：

```python
drag = {"id": None, "x": 0, "y": 0}
def on_press(e):
    drag["id"] = cv.find_withtag("current")
    drag["x"], drag["y"] = e.x, e.y
def on_move(e):
    if drag["id"] is None:
        return
    cv.move(drag["id"], e.x - drag["x"], e.y - drag["y"])
    drag["x"], drag["y"] = e.x, e.y
def on_release(e):
    drag["id"] = None
cv.tag_bind("box", "<ButtonPress-1>", on_press)
cv.tag_bind("box", "<B1-Motion>", on_move)
cv.tag_bind("box", "<ButtonRelease-1>", on_release)
```

> `<B1-Motion>` 是"按住左键移动"的复合事件，比逐帧 `Motion` 更准。

**大画布滚动**（设 `scrollregion` + 联动 Scrollbar）：

```python
cv.configure(scrollregion=(0, 0, 800, 600))    # 虚拟画布大小
vsb = ttk.Scrollbar(frame, orient="vertical", command=cv.yview)
hsb = ttk.Scrollbar(frame, orient="horizontal", command=cv.xview)
cv.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

def on_wheel(e):
    cv.yview_scroll(int(-1 * (e.delta / 120)), "units")
cv.bind("<MouseWheel>", on_wheel)
```

布局上垂直滚动条 `sticky="ns"`、水平 `sticky="ew"`，Canvas 本体占主格并 `rowconfigure/columnconfigure(weight=1)`。

> 实战要点（来自 rd-expense）：`draw_bar_chart()` / `draw_ring()` 用 `cv.delete("all")` + `cv.winfo_width()/winfo_height()` 拿真实分配尺寸再画；固定像素高度（如条形 26px）避免被行高撑大；用 `min(cw, ch, size)` 取安全绘图区防溢出；所有 Canvas 操作必须在主线程。

### 6.5 Text 富文本进阶（标签格式化 / marks / 嵌入 / 搜索 / 撤销）

> 事实：只有 `tk.Text`，无 `ttk.Text`。内容用"索引"定位：`"1.0"`（第1行第0列，行号从 1、列号从 0）、`"end"`、`"insert"`（光标）、`"@x,y"`、`"sel.first"/"sel.last"`。大量结构化数据表格**优先用 Treeview**（见 `04`）；Text 适合日志、报告、富文本、代码/配置查看器。

**内容读写**：

```python
tx = tk.Text(frame, width=60, height=12, wrap="word", font=("Microsoft YaHei UI", 10))
tx.insert("1.0", "第一段\n")
tx.insert("end", "追加内容")
tx.delete("1.0", "1.5")
full = tx.get("1.0", "end-1c")               # ⚠️ 用 end-1c 去掉末尾多余换行
```

> **实测坑**（rd-expense `FormDialog` 同款处理）：`get("1.0", "end")` 会包含结尾 `\n`，导致往返编辑文本越攒越长。规范写法是 `"end-1c"`。

**标签格式化（富文本着色）**：

```python
tx.tag_configure("warn", foreground="#d97706", background="#fff7ed",
                 font=("Microsoft YaHei UI", 10, "bold"))
tx.tag_configure("code", font=("Consolas", 10), background="#f1f5f9")
tx.insert("end", "警告：", ("warn",))         # 插入时直接打 tag
tx.tag_add("code", "2.0", "2.20")            # 事后给区间打 tag
print(tx.tag_names())                         # 所有已定义 tag
print(tx.tag_ranges("warn"))                  # 该 tag 覆盖区间
tx.tag_remove("warn", "3.0", "3.4")          # 去掉区间的 tag
```

- `tag_configure` 可设：`foreground`/`background`/`font`/`justify`/`lmargin1`/`spacing1` 等。`tag_raise`/`tag_lower` 控制重叠显示优先级。`tag_bind(tag, "<Button-1>", cb)` 给带该 tag 文本绑定点击（如链接）。

**标记 marks（浮动锚点）**：

```python
tx.mark_set("bookmark", "1.0")
tx.mark_unset("bookmark")
print(tx.mark_names())                        # 含 "insert"/"current" 及自定义
tx.mark_gravity("bookmark", "right")          # 插入点落在 mark 左/右侧
```

**搜索与替换**：

```python
idx = tx.search("关键字", "1.0", stopindex="end", forwards=True, nocase=True, regexp=False)
if idx:
    end = f"{idx}+{len('关键字')}c"
    tx.tag_add("hl", idx, end)
cnt = tk.IntVar()
tx.search("err", "1.0", stopindex="end", count=cnt)
print("命中", cnt.get())
tx.replace("1.0", "1.5", "新文本")           # 区间替换
```

`search` 返回首个匹配索引（如 `"2.3"`），无匹配返回 `""`；`regexp=True` 用 Tcl 正则。

**嵌入图像与控件**：

```python
tx.image_create("insert", image=photo)        # photo 必须保持引用！
tx.insert("end", "\n")
btn = ttk.Button(tx, text="点我")
tx.window_create("end", window=btn)
```

`image_create`/`window_create` 均实测存在。`photo` 一定要存实例属性或模块级变量，否则被 GC 后图片变空白（技能铁律）。

**修改通知与撤销**：

```python
tx.configure(undo=True, maxundo=50)
tx.edit_modified(False)                        # 清"已修改"标记
tx.bind("<<Modified>>", lambda e: on_text_changed())   # 已验证会触发
print(tx.edit_modified())                      # 1（已修改）/ 0
tx.edit_undo(); tx.edit_redo()
```

- `<<Modified>>` 在**用户编辑**时触发（已验证），适合"未保存"提示；读状态用 `edit_modified()`（返回 1/0）。注意 `insert`/`delete` **程序调用**也会置 modified；提交保存后 `edit_modified(False)` 复位。
- 只读模式：`tx.configure(state="disabled")`，临时 `state="normal"` 插入后改回。
- MVC 接法：Text 放 View；变更经 `<<Modified>>` 或"保存"按钮 → Controller 校验 → 写 Model。大数据量只读展示（日志/报表）可不绑修改事件，仅刷新时 `delete("1.0","end-1c")` + 重新 `insert`。

---

## 7. 组件封装：别让细节四处流浪

业务代码里到处写 `fg_color="#4F46E5"` / `font=(...)` 是技术债。**封装一层自己的控件**：

- **标准库方案**：靠 §0 的 `setup_style` 预定义 `Accent.TButton` / `Danger.TButton` / `Card.TFrame` 等命名样式，业务代码只引用样式名（无需继承类）。

**封装铁律**：`**kwargs` **必须透传**给父类 `super().__init__`，否则调用方传的 `width/padx` 被静默忽略，排查极耗时间。

**BasePage 基类**统一页面骨架（header 标题 + content 内边距），每个页面只写自己的业务逻辑：

```python
class BasePage(ttk.Frame):
    def __init__(self, master, title="", **kwargs):
        super().__init__(master, style="Card.TFrame", **kwargs)
        if title:
            ttk.Label(self, text=title, font=("Microsoft YaHei UI", 14, "bold")).pack(
                anchor="w", padx=THEME["pad_md"], pady=(THEME["pad_md"], 0))
        self.content = ttk.Frame(self, style="Card.TFrame")
        self.content.pack(fill="both", expand=True, padx=THEME["pad_md"], pady=THEME["pad_sm"])
```

---

## 8. 交互与状态联动

- **状态反馈**：ttk 用 `style.map` 定义 hover/active/disabled 三态。按钮区分默认/悬停/点击三态色，提升层次感。
- **变量联动**：用 `tk` 变量类 `trace_add` 实现控件间智能响应，如勾选框禁用关联输入框：

```python
check_var = tk.BooleanVar()
def on_change(*_):
    entry["state"] = "normal" if check_var.get() else "disabled"
check_var.trace_add("write", on_change)
```

- **异步加载缓冲**：耗时操作期间弹 `Toplevel` 覆盖层 + `after` 驱动进度，避免"假死"。结合 `05-threading-and-async.md` 的 queue 模式；**子线程严禁直接碰任何 widget**。
- **延迟加载（Lazy Loading）**：重型页面/数据不要在主窗口构造时全量初始化，改为首次 `show()` 时再加载：

```python
def show(self, key):
    frame = self._pages[key]
    frame.tkraise()
    if hasattr(frame, "refresh"):
        frame.refresh()          # 数据/图表在此拉取，构造时只搭空壳
```

对特别重的图表，可在 `refresh` 内用 `root.after(50, self._lazy_draw)` 让首屏先出现、图表随后补齐。

---

## 9. 窗口规范

```python
root.title("研发费用管理系统")
root.geometry("1280x800")
root.minsize(1024, 700)
# 居中
root.update_idletasks()
x = (root.winfo_screenwidth() - 1280) // 2
y = (root.winfo_screenheight() - 800) // 2
root.geometry(f"1280x800+{x}+{y}")
```

- 关闭确认：`root.protocol("WM_DELETE_WINDOW", on_close)`——有未保存数据时弹确认。
- 图标：`root.iconbitmap(ico_path)` 只认 .ico；打包后路径见 `08-packaging.md`。

---

## 10. 第三方美化库（可选增强）

> 引入前务必阅读 `08-packaging.md` 的「第三方美化库打包」——它们都会改变依赖与体积。

### tkwebview2 / tkwebview（内嵌真实浏览器内核，按需）
仅在「必须用 WebView2/Chromium 内核渲染真实网页或现代 HTML/CSS/JS」时才引入（见下方场景）。二者在 Windows 上最终都依赖系统级 **WebView2 Runtime**（Edge 内核，~100–150MB，Win10/11 通常已预装，缺失时可由 `install_runtime()` 自动下载）——**该内核是系统组件，不进 EXE**。

- **tkwebview2**（Smart-Space，MIT，仅 Windows 最佳）：包装 `pywebview` + `pythonnet(clr)` + WebView2.Core。引入的 Python 依赖链偏重。
  - **实测体积（本机，PyInstaller `--onefile --windowed --noupx`，Python 3.13.14）**：纯标准库基线 **9.90 MB** → 引入 tkwebview2 后 **15.86 MB**，**增量约 +6 MB**（来自 tkwebview2 + pythonnet + pywebview 这条链）。
- **tkwebview**（Smart-Space，MIT，纯 C 封装 webview/webview，无 pythonnet/pywebview 依赖）：包体极小。完整 API、限制、焦点陷阱解法、官方示例见 **`references/13-tkwebview.md`**。
  - **实测体积**：基线 9.90 MB → 引入 tkwebview 后 **10.06 MB**，**增量约 +0.2 MB**（几乎可忽略）。
- **真实应用复测（announcement-downloader，基线 15.88 MB，已含 pygubu/requests/win32/sqlite）**：tkwebview2 → 21.21 MB（**+5.34 MB**）；tkwebview → 15.88 MB（**+0.01 MB**，可忽略）。与纯净基线结论一致——tkwebview2 的代价来自 pythonnet + pywebview 依赖链，tkwebview 几乎零代价。

> 选型小结：要最小体积增量且能接受纯 C 封装的有限能力 → **tkwebview**；需要完整 Edge/Chromium 内核能力（JS↔Python 双向调用、devtools、现代 web 标准）→ **tkwebview2**（代价是 +6MB 与 .NET 依赖链）。无论哪个，**WebView2 Runtime 都得在目标机上存在**，否则运行期报错。完整参考见 `15-tkwebview.md`；打包细则见 `08-packaging.md`「第三方美化库打包」。

---

## 11. 反模式清单（必避）

| 反模式 | 后果 | 正确做法 |
| ---- | ---- | ---- |
| 用原生 `tk.Button/Entry`（非 ttk） | 样式复古受限、无状态 | 一律 `ttk.*`（`04` §铁律） |
| **Treeview 用默认 `rowheight=20`** | **行紧、文字截断/显示不全（尤其中文/高DPI/下行字母）** | **用 `font.metrics('linespace') + 8` 计算（§5.1 公式+对照表）** |
| **表单字段不设 `pady` / 值太小** | **标签与输入框粘连、整体拥挤糊在一起** | **统一 `padx=8, pady=THEME["pad_xs"]`，组间 `GROUP_PAD_Y=10`（§5.2）** |
| 面条式代码（无 OOP 封装） | 不可维护 | 类封装 View/Page/Widget |
| 颜色/字体散落硬编码 | 改主题找几十处 | THEME 字典 + 命名样式 |
| 界面拥挤无留白 | "丑"的首要原因 | 统一间距常量体系（§5.2 四档 pad_xs/sm/md/lg/xl） |
| 忽略线程安全 | 卡死/崩溃 | 耗时操作走 worker 线程 + queue |
| 忽略 DPI/响应式 | 高分屏发虚、拉伸错乱、间距不够 | DPI 感知 + `dpi_scale()` 放大间距（§5.4） |
| 同容器 pack/grid 混用 | 直接抛错/布局崩 | 外层 grid、内层 pack |
| 封装控件不透传 `**kwargs` | 参数静默忽略 | 务必 `super().__init__(**kwargs)` |
| 过度美化牺牲功能 | 运行慢/冗余 | 功能优先，按需美化 |
| 误把 ttk.Style 当 CSS | 样式静默失效 | 先 `theme_use("clam")` + `map` + 显式 `style=` |

---

## 12. 设计质量自查清单（交付前过一遍）

- [ ] 配色/间距/字体是否来自 `THEME` 单一来源，业务代码无颜色字面值
- [ ] **Treeview `rowheight` 是否用 `font.metrics('linespace')` 计算（§5.1），禁止默认 20**
- [ ] **表单字段是否有统一 `padx/pady`，组间是否有 `GROUP_PAD_Y=10` 间隔（§5.2）**
- [ ] **按钮/输入框是否设了 `padding=`（Button ≥(10,5)、Entry ≥5）（§5.3 检查清单）**
- [ ] **高 DPI 下间距是否用 `dpi_scale()` 放大（§5.4）**
- [ ] 主题是否基于 `clam`，自定义样式名是否显式 `style=` 传入
- [ ] 控件是否统一封装（命名样式或封装类），无散落硬编码
- [ ] 布局是否 Frame 分层 + 外层 grid / 内层 pack，无混用
- [ ] 是否定义了状态反馈（hover/active/disabled）
- [ ] 窗口拉大：表格/输入区跟随伸缩，无大片空白死区
- [ ] 窗口缩到 minsize：无控件被裁切、无横向滚动条常驻
- [ ] 高 DPI（150%）：文字不发虚、行高不挤、间距不粘（§5 全套）
- [ ] 所有按钮有明确文字（无裸英文标识符）、危险操作红色/二次确认
- [ ] 表格空态有提示（"暂无数据，点击新增…"），不是纯空白
- [ ] 是否有空态提示、危险操作二次确认、关闭确认
- [ ] Tab 顺序合理，回车触发默认按钮（`bind('<Return>', ...)`）
- [ ] 跨平台产品是否在目标 OS 实测样式

---

## 13. 来源索引（可追溯）

本篇由技能内三份同源资料合并重写，并综合下列公开资料提炼，落地时已按"标准库优先"原则裁剪：

- cda.cn/bigdata/207526 — 原生 vs 第三方美化四维思路、三色原则、避免过度美化
- 2048ai.net/698414 — Tkinter"土味"根源剖析、ttk 主题（clam/alt）、基础美化
- php.cn/faq/2765178 — ttk.Style 非 CSS 真相、clam 强制、layout 重建、跨平台失效
- foxfire.com.cn/683 — 复合布局黄金法则、动态色彩管理、变量联动、Canvas 层级、异步缓冲

> 注：部分来源含个别推广性内容，已剔除，仅保留可验证的技术要点。

---

## 14. 社区控件库检索目录（参考资源）

[Akascape/tkinter-toolkit](https://github.com/Akascape/tkinter-toolkit) —— 社区 **标准 tkinter 第三方控件库与实用工具**的检索/目录应用：内置 `database.json` 收录大量社区维护的 tkinter 扩展控件与工具，可逐个浏览、按图索骥找「轮子」。

> 用法：仅作为「找轮子」的索引资源使用——**只挑选明确基于标准 tkinter（tk / ttk）实现的扩展件**，按需取用；本技能不依赖它，也不推荐把它本身作为项目依赖。更系统的原生 Tkinter 子集整理见 `references/15-tkinter-toolkit.md`。
