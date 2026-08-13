# 19. TDD 方法论与冒烟测试体系

> 本篇聚焦"怎么做 TDD"而非"有哪些测试类型"，是 `references/09-testing-and-quality.md`
> 的**方法论深化版**，并适配 tkinter 桌面应用场景。

---

## 1. Red-Green-Refactor 循环在 tkinter 项目中的实践

### 标准循环

```
RED   → 写一个失败的断言（描述期望行为）
GREEN → 写最少代码让断言通过
REFACTOR → 清理，保持全绿
```

### tkinter 特化：三种 Red-Green 模式

#### 模式 A：Model 层 TDD（主力，占 80%）

```python
# RED: 先写失败测试
def test_collect_expense_capitalizes_status():
    conn = sqlite3.connect(":memory:")
    init_db(conn)
    svc = CollectService(conn)
    row = svc.collect({"amount": 500000, "type": "研发"})
    assert row["cap_status"] == "费用化"  # ← 先跑，必然 FAIL（功能还没写）

# GREEN: 写最少实现
class CollectService:
    def collect(self, data):
        if data["amount"] >= 500000:
            data["cap_status"] = "资本化"
        else:
            data["cap_status"] = "费用化"
        return data

# REFACTOR: 提取规则引擎
class CapitalizationRule:
    THRESHOLD = 500_000
    def classify(self, amount):
        return "资本化" if amount >= self.THRESHOLD else "费用化"
```

**关键约束**：
- Model 层 **禁止 import tkinter**
- DB 用 `sqlite3.connect(":memory:")`
- 纯逻辑，可 pytest 并行

#### 模式 B：View 层冒烟 TDD（控件级，占 15%）

```python
# RED: 先写无头冒烟断言
def test_main_view_has_six_pages():
    root = tk.Tk(); root.withdraw()
    app = MainController(root)   # 创建但不 mainloop
    root.update()
    # 用 pages 字典 + win.show(key) 切页，不是 ttk.Notebook
    assert set(app.pages) == {"dashboard", "projects", "expenses",
                              "collect", "reports", "risks"}  # ← 必然 FAIL

# GREEN: 用 pages 字典登记各页，show(key) 做 tkraise 切页
class Window:
    def __init__(self, master):
        self.pages = {}
        self.container = ttk.Frame(master)
        self.container.pack(fill=tk.BOTH, expand=True)
    def register(self, key, page):
        page.place(in_=self.container, x=0, y=0, relwidth=1, relheight=1)
        self.pages[key] = page
    def show(self, key):
        self.pages[key].tkraise()
        if hasattr(self.pages[key], "refresh"):
            self.pages[key].refresh()   # 首次切到才拉数据

# REFACTOR: 每页是普通 ttk.Frame，实现 refresh() 延迟加载数据
class DashboardPage(ttk.Frame):
    def refresh(self): ...
```

**关键技巧**：
- 用 `withdraw()` 不弹窗，用 `update()` 驱动布局
- 断言控件树结构（tabs 数量、Treeview 列数、Label 文案）
- **不合成鼠标事件**——调 Controller 方法模拟交互
- 唯一例外：`<<TreeviewSelect>>` 虚拟事件必须测一次（主从联动是唯一能机器抓到的 schema 错位路径）

#### 模式 C：EXE 冒烟 TDD（发布门禁，占 5%）

```powershell
# RED: EXE 还没打包 → 脚本报找不到文件
# GREEN: 打包成功 → 脚本验证窗口出现
# 注：Tkinter 窗口常不被 Get-Process 识别为 MainWindowTitle，改用 tasklist /v + 启动日志兜底
$p = Start-Process dist\MyTool.exe -PassThru
$ok = $false
for ($i = 0; $i -lt 15; $i++) {
    Start-Sleep 1
    if ($p.HasExited) { throw "EXE 启动即退出 (ExitCode=$($p.ExitCode))" }
    $tl = tasklist /fi "pid eq $($p.Id)" /v 2>$null
    if ($tl -match [regex]::Escape("MyTool")) { $ok = $true; break }
}
if (-not $ok) {
    $log = "dist\logs\app.log"
    if ((Test-Path $log) -and (Select-String -Path $log -Pattern "主界面装配完成" -Quiet)) {
        $ok = $true
    }
}
if (-not $ok) { Stop-Process -Id $p.Id -Force; throw "EXE 启动后未出现主窗口" }
Stop-Process -Id $p.Id -Force
# REFACTOR: 加入版本号检查、命令行参数验证等
```

---

## 2. 测试金字塔（tkinter 版）

```
              ┌──────────────┐
              │  EXE 冒烟     │  5%  — 发布时 1 次
              │  (PowerShell) │
         ┌────┴──────────────┴────┐
         │   无头 GUI 冒烟          │ 15% — smoke_test_gui.py
         │   (withdraw+update)     │
    ┌────┴────────────────────────┴────┐
    │      集成测试 (Controller+DB)     │ 15% — pytest + Tk fixture
    │                                  │
 ┌───┴──────────────────────────────────┴───┐
 │       单元测试 (Model/Service)            │ 65% — pytest, 零 tkinter
 │                                          │
 └──────────────────────────────────────────┘
```

**数据驱动测试**（@parametrize）：

```python
@pytest.mark.parametrize("amount,expected", [
    (100_000, "费用化"),
    (499_999, "费用化"),
    (500_000, "资本化"),
    (1_000_000, "资本化"),
    (0, "费用化"),
])
def test_capitalization_threshold(amount, expected):
    rule = CapitalizationRule()
    assert rule.classify(amount) == expected
```

---

## 3. Prove-It 模式（Bug 修复必做）

发现 bug 时，**先写复现测试，再修复**：

```python
# Step 1: 写复现测试（必然 RED）
def test_bug_147_treeview_sort_by_date_crashes():
    """#147: 按日期列排序时 KeyError 'invalid_date'"""
    app = build_app()
    app.withdraw()
    app.update()
    # 触发排序操作
    app.project_view.tree.heading("date", command=lambda: sort_tree(app.project_view.tree, "date"))
    app.project_view.tree.heading("date").invoke()
    app.update()
    # 不应崩溃
    assert len(app.project_view.tree.get_children()) >= 0
    app.destroy()

# Step 2: 修复 bug（让测试 GREEN）
def sort_tree(tree, col):
    # ... 修复日期解析逻辑 ...

# Step 3: REFACTOR（如有必要）
```

**回归保护**：Prove-It 测试一旦写入，**永远不删除**——它是该 bug 的永久疫苗。

---

## 4. 发布门禁（release_gate.py）

本技能提供统一的发布门禁脚本 `scripts/release_gate.py`，按顺序执行：

| 步骤 | 命令 | 失败后果 |
|------|------|---------|
| ① pytest | `pytest -q tests/` | **REQUIRED** → 门禁不通过 |
| ② GUI 冒烟 | `python scripts/smoke_test_gui.py` | **REQUIRED** → 门禁不通过 |
| ③ 导入检查 | 扫描所有 .py 验证 import | **REQUIRED** → 门禁不通过 |
| ④ 文档代码块 | references/*.md 中 python 代码块 compile | WARNING → 提示但不阻断 |

```bash
# 全量运行
python scripts/release_gate.py --root /path/to/project

# 开发期跳过耗时项
python scripts/release_gate.py --skip-pytest --skip-smoke

# CI 中使用（非零退出 = 构建失败）
python scripts/release_gate.py || exit 1
```

---

## 5. 开发流程中的测试位置（对应 workflow ⑥⑦）

```
workflow ⑤ 编写业务代码
  │
  ├─→ [TDD] 写 Model 测试 (RED) → 实现 (GREEN) → 重构 (REFACTOR)
  │
  ├─→ [TDD] 写 View 冒烟 (RED) → 创建控件 (GREEN) → 样式调整
  │
  ├─→ 运行 release_gate.py（开发期可用 --skip-smoke 加速）
  │
  ├─→ 修复所有 FAIL → 全绿
  │
  ▼
workflow ⑥ 测试与质量 ← release_gate.py 全量通过后进入
  │
  ├─→ 无头 GUI 冒烟确认
  │
  ├─→ UI 设计质量自查（03-ui-design.md 清单）
  │
  ▼
workflow ⑧ 打包为 EXE ← 只有门禁全绿才允许打包
  │
  ├─→ PyInstaller onefile+windowed
  │
  ├─→ EXE 冒烟（PowerShell 启动验证）
  │
  ▼
交付
```

---

## 6. tkinter 测试的常见陷阱与解法

| 陷阱 | 症状 | 解法 |
|------|------|------|
| PhotoImage 被 GC 变空白 | 图片区域变灰/透明 | 保持全局引用列表（IMAGE_REFS） |
| withdraw 后 event_generate 无效 | 点击事件不触发 | 改调 Controller 方法 |
| worker 线程结果未就绪就断言 | AssertionError | after 轮询 + deadline 超时循环 |
| Tcl 解释器残留 | 第二个用例报奇怪错误 | 每个 fixture 都 `root.destroy()` |
| import 时读环境变量 | 拿到缓存旧值 | conftest 先设 env → del sys.modules → 再 import |
| 字体/主题跨平台差异 | Linux 上字体名不同 | 用 tk.font.families() 动态检测或 fallback |

---

## 7. 快速启动测试的 checklist

新项目第一次设置测试时，逐项确认：

- [ ] `tests/` 目录存在，含 `conftest.py`（DB 内存 fixture）
- [ ] `scripts/smoke_test_gui.py` 存在且已覆写 `build_app()`
- [ ] `scripts/release_gate.py` 可执行（零配置即可跑）
- [ ] CI 配置中包含 `python scripts/release_gate.py || exit 1`
- [ ] Model 层测试覆盖核心算法（归集口径、分类规则、计算公式）
- [ ] 至少有一个 View 层冒烟测试（验证 Notebook tabs / Treeview columns）
- [ ] Prove-It 测试目录已建立（`tests/regression/` 或类似命名）
