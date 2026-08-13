# 04 高频实战模式（控件级配方）

> 本文是"抄了就能用"的配方集。控件完整选项查 `11-official-docs/tkinter-ttk.md`。

## 1. Treeview 数据表格（最高频）

```python
cols = ("code", "name", "amount")
tree = ttk.Treeview(parent, columns=cols, show="headings", selectmode="browse", height=15)
for cid, text, w, anchor in [("code", "编码", 100, "w"), ("name", "名称", 220, "w"),
                             ("amount", "金额", 120, "e")]:
    tree.heading(cid, text=text)
    tree.column(cid, width=w, anchor=anchor, stretch=(cid == "name"))
vsb = ttk.Scrollbar(parent, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=vsb.set)
tree.grid(row=0, column=0, sticky="nsew"); vsb.grid(row=0, column=1, sticky="ns")

# ⚠️ 必须设置 rowheight！默认值 20 在中文/高DPI 下会截断文字
# 详见 `03-ui-design.md` §5.1（font.metrics 公式 + 对照表）
import tkinter.font as tkfont
_font = tkfont.Font(family="Microsoft YaHei UI", size=10)
tree.configure(rowheight=_font.metrics("linespace") + 8)   # → ~24px
```

要点：
- `show="headings"` 隐藏第 0 层树列；要树形结构时去掉并用 `tree.insert(parent_iid, ...)`
- **iid 存业务主键**：`tree.insert("", "end", iid=str(row_id), values=...)`，
  选中行取 `tree.selection()[0]` 即主键，禁止用"行号反查列表"的脆弱做法
- 值只能是字符串：金额格式化 `f"{v:,.2f}"` 再放入；排序时要转回数字
- 刷新 = `tree.delete(*tree.get_children())` 后重插；千行以上考虑分页
- 双击编辑：`tree.bind("<Double-1>", ...)`；选中变化：`tree.bind("<<TreeviewSelect>>", ...)`
- 列排序：heading 加 `command=lambda c=cid: sort_by(c)`，内部用
  `tree.move(iid, "", index)` 重排

## 2. 表单构建器（label + 控件成对生成）

```python
def build_form(parent, fields: list[dict], vars_: dict):
    """fields: [{key,label,kind(entry|combo|date|check|text),values?,width?}]"""
    for i, f in enumerate(fields):
        ttk.Label(parent, text=f["label"]).grid(row=i, column=0, sticky="w", padx=8, pady=4)
        if f["kind"] == "combo":
            var = tk.StringVar()
            w = ttk.Combobox(parent, textvariable=var, values=f["values"], state="readonly")
        elif f["kind"] == "check":
            var = tk.BooleanVar()
            w = ttk.Checkbutton(parent, variable=var)
        else:
            var = tk.StringVar()
            w = ttk.Entry(parent, textvariable=var, width=f.get("width", 28))
        w.grid(row=i, column=1, sticky="ew", padx=8, pady=4)
        vars_[f["key"]] = var
    parent.columnconfigure(1, weight=1)
```

要点：
- `vars_` 字典必须挂在 View 实例上（`self.form_vars`），防 GC
- Combobox 一律 `state="readonly"` 防手输脏数据；取值域来自 Model 查询
- 校验：提交时统一校验并 `messagebox.showwarning`，必填缺失时 `widget.focus_set()`

## 3. 模态对话框（新增/编辑弹窗）

```python
class FormDialog(tk.Toplevel):
    def __init__(self, master, title, fields, initial=None):
        super().__init__(master)
        self.title(title); self.resizable(False, False)
        self.result = None
        self.transient(master)              # 随主窗最小化、置于其上
        body = ttk.Frame(self, padding=12); body.pack(fill="both", expand=True)
        self.form_vars = {}; build_form(body, fields, self.form_vars)
        if initial:
            for k, v in initial.items():
                if k in self.form_vars: self.form_vars[k].set(v)
        bar = ttk.Frame(self, padding=(12, 0, 12, 12)); bar.pack(fill="x")
        ttk.Button(bar, text="确定", command=self._ok).pack(side="right")
        ttk.Button(bar, text="取消", command=self.destroy).pack(side="right", padx=8)
        self.bind("<Return>", lambda e: self._ok()); self.bind("<Escape>", lambda e: self.destroy())
        self.grab_set()                     # 模态：拦截主窗输入
        self.wait_visibility(); self.focus_set()

    def _ok(self):
        self.result = {k: v.get() for k, v in self.form_vars.items()}
        self.destroy()

# 调用方（阻塞直到关闭）：
dlg = FormDialog(root, "新增项目", FIELDS)
root.wait_window(dlg)
if dlg.result: ...
```

顺序铁律：`transient → grab_set → wait_window`。`grab_set` 前必须窗口已可见
（`wait_visibility`），否则 Windows 下偶发 `grab failed: window not viewable`。

## 4. Notebook 多页应用

```python
nb = ttk.Notebook(root)
nb.add(ProjectView(nb), text="  项目管理  ")
nb.add(ExpenseView(nb), text="  费用归集  ")
nb.grid(sticky="nsew")
nb.bind("<<NotebookTabChanged>>", lambda e: controllers[nb.index("current")].on_show())
```

- 页面多/数据大时用**懒加载**：add 占位 Frame，首次切到该页再真正构建
- `on_show()` 钩子：切页时刷新数据，保证跨页操作后数据不过期

## 5. 滚动容器（长表单）

Canvas + 内嵌 Frame 是唯一正解（ttk.Frame 自身不可滚动）：

```python
canvas = tk.Canvas(parent, highlightthickness=0)
vsb = ttk.Scrollbar(parent, orient="vertical", command=canvas.yview)
inner = ttk.Frame(canvas)
inner_id = canvas.create_window((0, 0), window=inner, anchor="nw")
inner.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.bind("<Configure>", lambda e: canvas.itemconfigure(inner_id, width=e.width))
canvas.configure(yscrollcommand=vsb.set)
```

鼠标滚轮（Windows）：`canvas.bind_all("<MouseWheel>", lambda e: canvas.yview_scroll(-e.delta//120, "units"))`
——注意 bind_all 在多滚动区页面要在离开时解绑，否则互相抢滚轮。

## 6. 状态栏与忙碌反馈

- 状态栏：底部 `ttk.Label(anchor="w")`，Controller 统一 `set_status("已保存 3 条")`
- 长操作（>0.5s）：按钮置灰 `state="disabled"` + `ttk.Progressbar(mode="indeterminate").start()`，
  完成后恢复——线程配合见 05-threading-and-async.md

## 7. 菜单与快捷键

> 事实：tkinter **只有 `tk.Menu`，没有 `ttk.Menu`**。菜单是无外观控制器，靠 `root.config(menu=...)` 挂窗口，或 `.post(x,y)` 在坐标弹出。`accelerator=` 只显示文字、不绑定快捷键，必须自己 `bind`。菜单回调走 Controller（见 `02-architecture-mvc.md`），不要在回调里写业务 SQL。

快速上手（menubar 最小骨架）：

```python
menubar = tk.Menu(root)          # 顶层菜单容器（本身也是 Menu）
root.config(menu=menubar)        # 关键：挂到窗口；等价于 root["menu"] = menubar

file_menu = tk.Menu(menubar, tearoff=False)   # tearoff=False 去掉顶部虚线"撕下"手柄
file_menu.add_command(label="打开", command=on_open, accelerator="Ctrl+O")
file_menu.add_separator()
file_menu.add_command(label="退出", command=root.quit)
menubar.add_cascade(label="文件", menu=file_menu)   # 把子菜单挂成级联项

edit_menu = tk.Menu(menubar, tearoff=False)
edit_menu.add_command(label="设置", command=on_settings)
menubar.add_cascade(label="编辑", menu=edit_menu)
```

- `add_cascade(label=..., menu=子Menu)` 建立"顶级菜单 → 子菜单"层级；可多层嵌套。顶级菜单项（"文件""编辑"）本身也通过 `add_cascade` 加入 `menubar`。
- `tearoff` 默认 `1`（有虚线手柄），生产应用几乎总是 `tearoff=False`。

### 菜单项类型

| 方法 | 用途 | 关键选项 |
| --- | --- | --- |
| `add_command(label=, command=, accelerator=, compound=, image=)` | 普通可点击项 | `state="disabled"` 可禁用 |
| `add_separator()` | 分隔线 | — |
| `add_cascade(label=, menu=)` | 子菜单入口 | — |
| `add_checkbutton(label=, variable=, command=, onvalue=, offvalue=)` | 勾选项 | 必须传 `tk.BooleanVar`/`IntVar` |
| `add_radiobutton(label=, variable=, value=, command=)` | 单选组 | 同一 `variable` 下不同 `value` 互斥 |

复选 / 单选示例：

```python
opts = tk.Menu(menubar, tearoff=False)
autosave = tk.BooleanVar(value=True)
opts.add_checkbutton(label="自动保存", variable=autosave,
                     command=lambda: print("autosave=", autosave.get()))
mode = tk.StringVar(value="A")
opts.add_radiobutton(label="模式 A", variable=mode, value="A")
opts.add_radiobutton(label="模式 B", variable=mode, value="B")
menubar.add_cascade(label="选项", menu=opts)
```

> `variable` 必须保持引用（实例属性或模块级），否则被 GC 后勾选状态丢失——与技能铁律"变量对象必须保持引用"一致。
> 运行时增删 / 改状态：`add()`、`.delete(index)`、`.entryconfig(index, label=.../state=...)`、`.invoke(index)`、`insert_cascade()` 等；索引可用整数、`"last"`、`"active"`，或用 label 字符串配合 `index(label)`。

### 让 accelerator 真正生效

`accelerator="Ctrl+O"` 只把 "Ctrl+O" 画在右侧，点击菜单项才触发 `command`；按键盘 Ctrl+O **不会**自动触发。必须显式绑定：

```python
root.bind("<Control-o>", lambda e: on_open())
root.bind("<Control-O>", lambda e: on_open())   # macOS/部分键盘用大写形式更稳
```

### 上下文菜单（右键）

绑 `<Button-3>`（鼠标右键），在指针处 `post`。用 `event.x_root/event.y_root` 拿屏幕坐标：

```python
def make_context_menu(widget, commands):
    """commands: list[(label, callback)]，挂到 widget 的右键菜单。"""
    m = tk.Menu(widget, tearoff=False)
    for label, cb in commands:
        m.add_command(label=label, command=cb)

    def _popup(event):
        try:
            m.tk_popup(event.x_root, event.y_root)
        finally:
            m.grab_release()

    widget.bind("<Button-3>", _popup)
    widget.bind("<Button-2>", _popup)   # macOS 触控板右键是 <Button-2>

make_context_menu(tree, [("刷新", on_refresh), ("导出", on_export)])
```

> 实测 `Menu.post(x, y)` 可用；`tk_popup()` 更省心（自动处理 grab 与跨平台右键按钮）。`unpost()` 手动关闭。

### 跨平台特殊菜单（重要，按目标 OS 验证）

- **macOS**：菜单栏**第一个顶级菜单会被当作"应用菜单"（Apple 菜单）**。加"关于 / 偏好 / 退出"到系统菜单用 macOS 专属钩子（仅 macOS 有效，本机 Windows 无法实测，请在 macOS 真机验证）：
  ```python
  root.createcommand("::tk::mac::ShowPreferences", on_settings)
  root.createcommand("::tk::mac::Quit", on_quit)
  root.createcommand("::tk::mac::ShowHelp", on_help)
  ```
  `Help` 菜单通常放最后，macOS 会挪到系统 Help 位置。
- **Windows / Linux**：无特殊系统菜单，按普通 `add_cascade` 组织即可。
- 菜单项图标用 `add_command(image=photo, compound="left")`，且 **`photo` 必须保持引用**（技能铁律：PhotoImage 保持引用）。

### 与 MVC 接法

菜单回调应是薄的"转发层"：

```python
def on_open():
    controller.open_file()    # 交给 Controller，不在这里直接读文件 / 写 DB
file_menu.add_command(label="打开", command=on_open)
```

实战指路：菜单项弹窗可复用 §9 的 `FormDialog` 范式（`transient`+`grab_set`+居中）；想看大型应用如何组织菜单读 `examples/idle/`（idlelib 菜单系统，标准库范本）。下拉选择若只是"静态若干选项"，也可考虑 `ttk.Combobox(state="readonly")` 或 `ttk.OptionMenu`（后者是 `tk.Menubutton`+`tk.Menu` 封装），不一定自建 `tk.Menu`。

---

## 8. 简单控件配方（Listbox / Scale / Spinbox / Progressbar）

> 哪些有 ttk 版：`Listbox` **无**（只用 `tk.Listbox`）；`Scrollbar`/`Scale`/`Spinbox`/`Progressbar` 均有 ttk 版，优先 ttk。Scrollbar 与任意可滚动目标（Treeview/Listbox/Text/Canvas）的双向联动范式见 §1 / §5，本节聚焦其余控件。

### Listbox（列表框）

`tk.Listbox` 无 ttk 版，直接用经典控件；样式走 `bg/fg/selectbackground/height` 等选项。

```python
lb = tk.Listbox(frame, height=8, selectmode="browse", exportselection=False)
lb.insert("end", "苹果", "香蕉", "橙子")
lb.insert(0, "置顶项")
lb.delete(0)                               # 删除首项；delete(0, "end") 清空
lb.selection_set(1)
print(lb.curselection())                   # (1,) 当前选中（tuple）
print(lb.get(0, "end"))                    # 取全部内容（tuple）
lb.see(2)                                 # 滚动到可见

# 联动滚动条（与 Treeview 同理，双向绑定缺一不可）
sb = ttk.Scrollbar(frame, orient="vertical", command=lb.yview)
lb.configure(yscrollcommand=sb.set)
lb.grid(row=0, column=0, sticky="nsew"); sb.grid(row=0, column=1, sticky="ns")

# 响应选择变化：绑定 <<ListboxSelect>> 虚拟事件（已验证会触发）
def on_select(event):
    sel = lb.curselection()
    if not sel:
        return
    controller.on_pick(lb.get(sel[0]))
lb.bind("<<ListboxSelect>>", on_select)
```

> `selectmode`：`"browse"`（单选，默认）/ `"single"` / `"multiple"` / `"extended"`（Shift/Ctrl 多选）。多选用 `lb.curselection()` 拿所有选中索引。
> `exportselection=False` 很关键：默认 True 时，选中 Listbox 内容会清空系统剪贴板选择，导致与其他控件冲突。

### Scale（滑块）

`ttk.Scale` 取值是**浮点**。

```python
val = tk.DoubleVar(value=33.0)
sc = ttk.Scale(frame, from_=0, to=100, orient="horizontal",
               variable=val, command=lambda v: print("当前", v))  # v 是字符串 "33.0"
sc.set(50)                  # ✅ 正确改值方式（移动滑块并同步 variable）
print(sc.get())             # 33.0（float）
```

⚠️ **实测坑**：直接改选项 `sc["value"] = 50` **不会**移动滑块、也不会同步 `variable`（已验证 get() 仍为旧值）。改 Scale 值一律用 `.set()`。

- `command` 回调收到的值是**字符串**（如 `"5.0"`），需要时 `float(v)`。
- 其它常用选项：`resolution`（步长）、`bigincrement`（PageUp/Down 步长）、`digits`（显示位数）、`length`。
- **没有** `<<RangeChanged>>` 之类虚拟事件——监听变化用 `command=` 或跟踪 `variable`（`val.trace_add`）。

### Spinbox（数字微调框）

`ttk.Spinbox` 的 `get()` 返回**字符串**；`set()` 自由设值，**不按步长吸附**（已验证：`set(3)` 配 `increment=2` 仍得 `'3'`）。

```python
v = tk.StringVar(value="5")
sb = ttk.Spinbox(frame, from_=0, to=10, increment=1, textvariable=v, wrap=True, width=8)
sb.set(3)
print(sb.get())             # '3'（str）

sb.configure(values=("小", "中", "大"))   # 离散选项模式
sb.set("中"); print(sb.get())             # '中'

def on_spin():
    controller.on_count_changed(sb.get())   # 回调内用 .get() 读新值
sb.configure(command=on_spin)
```

- `from_`/`to`/`increment`/`wrap`（到边界回环）/ `state`（`"readonly"` 禁止手输）。
- **没有** `<<Increment>>` / `<<Decrement>>` 虚拟事件——箭头改变时走 `command=` 回调，在回调里 `.get()` 读新值。
- 可用 §9 的 `FormDialog` 范式把 `ttk.Spinbox`（`wtype="spin"`）作表单字段。

### Progressbar（进度条）

`ttk.Progressbar`，`value` 为**浮点**。

```python
pb = ttk.Progressbar(frame, orient="horizontal", length=200, maximum=100, mode="determinate", value=0)
pb["value"] = 40           # 直接设数值（实测为 float 40.0）
pb.step(10)                # 相对步进 → 50.0
pb.update_idletasks()

pb2 = ttk.Progressbar(frame, mode="indeterminate")
pb2.start(50)              # 每 50ms 滑动一格；完成时 pb2.stop()
```

- `mode="determinate"`（已知进度，设 `value`）+ `step(delta)`；`mode="indeterminate"` + `start(interval)`/`stop()`。
- `maximum` 设总量；`value` 设当前量。
- 外观（厚度/颜色）在 `ui.py` 的 `setup_style()` 已雅化（`TProgressbar` 的 `thickness`/`troughcolor`/`lightcolor`/`darkcolor`），见 `03-ui-design.md` §4。
- 长任务放 worker 线程，主线程 `after()` 轮询里 `pb["value"] = pct`，配合 `05-threading-and-async.md`。

---

## 9. 窗口行为（Toplevel / 协议 / 无边框 / 置顶 / 多窗口）

> 事实：子窗口用 `tk.Toplevel(parent)`（无 ttk 版）；主窗口是 `Tk()`。窗口行为方法大量存在于 `Tk` 与 `Toplevel` 共通。⚠️ **实测坑**：对 `transient` 窗口调用 `iconify()` 会抛 `TclError: can't iconify ... it is a transient`；要做图标化先 `transient("")` 清除瞬态。

### 基础属性

```python
top = tk.Toplevel(root)
top.title("设置")
top.geometry("480x360")                       # 也可 "+x+y" 设位置
top.minsize(320, 240); top.maxsize(1280, 960)
top.resizable(False, False)                    # 禁止拉伸（对话框常用）
top.attributes("-alpha", 0.95)                 # 透明度（0~1）
```

- `geometry("WxH+X+Y")` 同时设尺寸与位置；只设 `"+X+Y"` 仅移动。`resizable(w,h)`：`False` 锁死某方向。

### 模态对话框（标准范式）

见 §3 的 `FormDialog` 类（`transient → grab_set → wait_window`）。该范式支持 entry/combo/spin/text/check 字段、回车确定/Esc 取消、居中，**新增/编辑弹窗直接复用**。要点回顾：`transient(parent)` 让子窗浮在父窗之上且随父最小化；`grab_set()` 拦截其它窗口输入（真正模态，销毁时自动释放，记得配对 `grab_release()`）；`wait_window()` 阻塞直到 `destroy()`；居中必须在 `update_idletasks()` 之后，否则 `winfo_width()` 还是 1。

### 拦截关闭（WM_DELETE_WINDOW 协议）

点关闭按钮时做"确认 / 保存提示 / 禁止关闭"，拦截协议：

```python
def on_close():
    if dirty and not confirm("有未保存修改，确定退出？"):
        return                       # 返回即可取消关闭
    top.grab_release()
    top.destroy()

top.protocol("WM_DELETE_WINDOW", on_close)     # 等价 top.wm_protocol(...)
```

- `protocol`/`wm_protocol` 均实测存在。不调用 `destroy()` 则窗口保持打开。模态对话框配合 `grab_set`：关闭前务必 `grab_release()`，否则后续窗口拿不到输入。
- 主窗口关闭确认同理：`root.protocol("WM_DELETE_WINDOW", on_close)`（也见 `03-ui-design.md` §9）。

### 无边框窗口（overrideredirect）

做启动闪屏、自定义标题栏时用：

```python
top.overrideredirect(True)     # 去掉标题栏 + 边框 + 原生关闭/最小化
```

代价：失去原生拖动、最小化、关闭、任务栏右键。**必须自己实现**：拖动绑 `<ButtonPress-1>` + `<B1-Motion>`，用 `winfo_x()/winfo_y()` + 鼠标位移 `geometry(f"+{x}+{y}")` 跟手移动；关闭/最小化自己放按钮调 `top.destroy()` / `top.iconify()`。无边框下 `transient` 无意义，二者一般不混用。

### 置顶 / 状态 / 层级

```python
top.attributes("-topmost", True)              # 置顶（实测返回值为 1，非 True）
top.attributes("-topmost", False)
top.iconify(); top.deiconify()                # 最小化 / 还原
top.lift(); top.lower()                        # 提到最前 / 反之
top.state("zoomed")                            # Windows 最大化；"iconic"/"normal"
```

- `attributes()` 可读可写：写 `attributes("-key", val)`，读 `attributes("-key")` 返回实际值，布尔项返回 `1`/`0`。多属性用 dict 形式 `attributes(**{"-topmost": True})`。
- `state("zoomed")` 在 Windows 上最大化；macOS/Linux 用 `attributes("-zoomed", True)` 等，请按目标 OS 验证。

### 多窗口管理

- 用 `list` 跟踪所有 `Toplevel`，关闭时 `w.destroy()`，退出时 `root.quit()` / `root.destroy()`。
- 单实例锁定、系统托盘等 Win32 能力见 `ctypes/SKILL.md` §3。
- 关闭全部前统一走 `on_close` 拦截逻辑，避免数据丢失。
