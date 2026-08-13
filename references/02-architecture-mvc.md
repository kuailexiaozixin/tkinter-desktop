# 02 架构分层（MVC）

> Tkinter 项目失控的头号原因：把业务逻辑、SQL、控件操作全塞进一个巨型类。
> 本技能强制 MVC 分层，Model 层零 tkinter 依赖。

## 分层职责

```
┌────────────────────────────────────────────┐
│ View（views/）                              │
│  只做三件事：建控件、摆布局、暴露刷新方法      │
│  不写 SQL、不写业务规则、不 import models 内部 │
├────────────────────────────────────────────┤
│ Controller（controllers/）                  │
│  事件处理器：收集 View 输入 → 调 Model →      │
│  把结果喂回 View.refresh()；线程调度也在这层   │
├────────────────────────────────────────────┤
│ Model（models/）                            │
│  业务规则 + Repository（SQL）+ 领域计算       │
│  ★ 禁止 import tkinter ——可测试性的根基       │
└────────────────────────────────────────────┘
```

## 目录映射

```
src/<pkg>/
├── __init__.py
├── __main__.py          # python -m <pkg> 入口
├── app.py               # 组装根窗口、页面（Notebook 或 tkraise 堆叠帧）、各控制器
├── common/
│   ├── config.py        # BASE_DIR（sys.frozen 适配）、常量
│   ├── logging_setup.py # 文件日志
│   └── ui.py            # DPI、Style、通用小部件工厂
├── models/
│   ├── db.py            # 连接管理 + schema + 种子数据
│   ├── repository.py    # CRUD（按表拆分亦可）
│   └── services.py      # 领域计算（归集、报表等纯逻辑）
├── views/
│   ├── main_window.py   # 根窗口 + 导航
│   └── <feature>_view.py# 每个页面/Tab 一个 View 类
└── controllers/
    └── <feature>_controller.py
```

## 接线模式（推荐写法）

View 暴露回调挂钩，Controller 注入：

```python
class ProjectView(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.on_add = None            # Controller 注入
        self.tree = ttk.Treeview(self, columns=("name", "status"), show="headings")
        ttk.Button(self, text="新增", command=lambda: self.on_add and self.on_add()).grid(...)

    def refresh(self, rows: list[dict]):
        self.tree.delete(*self.tree.get_children())
        for r in rows:
            self.tree.insert("", "end", iid=str(r["id"]), values=(r["name"], r["status"]))

class ProjectController:
    def __init__(self, view, repo):
        self.view, self.repo = view, repo
        view.on_add = self.add_project
        self.reload()

    def reload(self):
        self.view.refresh(self.repo.list_projects())
```

要点：
- View 持有控件，Controller 持有 View + Model，Model 谁也不持有
- **刷新是显式的**：任何写操作成功后 Controller 必须调 `view.refresh(...)`，
  Tkinter 没有自动响应式绑定
- 跨页面联动（如新增项目后费用页下拉框要更新）走 App 级事件总线：
  最简单实现是根窗口 `event_generate("<<ProjectsChanged>>")` + 各页
  `bind("<<ProjectsChanged>>", ...)`。注意 `bind` 到根窗口时用 `add="+"` 防覆盖
- 中小应用更推荐**显式 App 级中介**而非事件总线（见下方真实示例）：
  Controller 持有 App 控制器，写操作后调 `app.refresh_pages("projects", "expenses")`，
  由 App 统一调各页 `refresh()`，依赖关系清晰、易调试

## 示例：MVC 接线（示意）

下方以一个典型 MVC 接线示意说明本技能理念（代码为讲解用，非某特定项目）：

```python
# views/projects_view.py —— View 持有控制器，按钮直接调控制器方法
class ProjectsView(ttk.Frame):
    def __init__(self, parent, ctrl):
        self.ctrl = ctrl                       # 注入控制器
        ttk.Button(self, text="项目指标",
                   command=lambda: self.ctrl.show_metrics(self._sel()))

    def refresh(self):                         # 显式刷新：从控制器取数重填 Treeview
        rows = [self._row(p) for p in self.ctrl.projects()]
        fill_tree_plain(self.tree, rows)

# controllers/project_controller.py —— Controller 持有 app（App 级控制器）
class ProjectController:
    def __init__(self, app): self.app = app
    def edit_boundary(self, pid, parent_view):
        ...
        repo.update("project", pid, **vals)    # 纯 Model 调用，无 widget
        self.app.set_status("已更新研发边界")
        self.app.refresh_pages("projects")     # 跨页刷新由 App 统一调度

# controllers/main_controller.py —— App 级装配与跨页刷新
class MainController:
    def __init__(self, root):
        self.pages = {
            "projects": ProjectsView(self.win.content, self.project_ctrl),
            "expenses": ExpensesView(self.win.content, self.expense_ctrl),
            ...
        }
    def refresh_pages(self, *keys):
        for k in keys:
            f = self.pages.get(k)
            if f is not None and hasattr(f, "refresh"):
                f.refresh()
```

关键要点（均与本技能一致）：

- **Model 层零 tkinter**：`models/db.py`、`models/repository.py` 等 Model 模块应**无**
  `import tkinter` —— 可脱离 GUI 单测（unittest 直接测 repository/engine）。
- **导航两种都行**：可用 `tkraise()` 把各页 Frame 叠在同一容器、`show(key)`
  时 `frame.tkraise()` 切换（替代 Notebook）；Notebook 仍是简单多 Tab 的首选。
- **模态对话框**复用 §3 的 `FormDialog` 范式（`transient(parent)` + `grab_set()` +
  居中 + `wait_window(dlg)` 阻塞取 `dlg.result`）。控制器里 `parent_view.wait_window(dlg)`
  后判空即取消。
- **状态栏**用 `tk.StringVar` 绑定 Label，`app.set_status()` → `win.set_status()` →
  `status_var.set(...)`，始终在主线程调用（Controller 在事件回调里跑，天然主线程）。
- **首启**可在 `MainController.__init__` 幂等建库播种（见 `06`）。

## MVP 边界与模块分解产出

在 `docs/architecture.md` 写清：
1. **模块分解表**：模块名 → 对应 View/Controller/Model 文件 → 依赖哪些表
2. **数据模型**：每张表字段、类型、外键、种子数据
3. **界面地图**：Notebook 有哪些 Tab、每个 Tab 的主控件（表格/表单/按钮组）、
   模态对话框清单

## 常见反模式

| 反模式 | 症状 | 纠正 |
| ------ | ---- | ---- |
| God-class App | 一个类 2000 行，控件+SQL+规则混杂 | 按上表拆 MVC |
| View 里写 SQL | 换库/改表要动界面代码 | SQL 全收进 repository |
| Model import tkinter | 测试必须开 GUI | Model 层纯 Python |
| 直接操作全局 widget | 模块间强耦合 | 只经 Controller 传递 |
| 每次刷新重建整个页面 | 闪烁、状态丢失 | 只更新数据控件（Treeview 重填） |
