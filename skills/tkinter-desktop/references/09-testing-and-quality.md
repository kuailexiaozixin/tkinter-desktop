# 09 测试与质量门禁

> Tkinter 的独特优势：**不需要浏览器/CDP 就能做真实控件级验证**。
> `Tk()` 可以在不进 mainloop 的情况下用 `update()` 驱动，控件树、值、状态全部可断言。

## 测试金字塔

```
        EXE 冒烟（打包后，每次发布 1 次）
      无头 GUI 冒烟 + 复杂 Controller 集成（scripts/smoke_test_gui.py 控件级；pytest 内建 Tk + :memory: DB）
  单元测试（models/services 纯逻辑，量最大）
```

## 1. Model 层单元测试（主力）

- **禁止 import tkinter**；DB 用 `sqlite3.connect(":memory:")` + `init_db`
- 归集/报表这类核心算法必须数据驱动测试：构造输入 → 断言金额/口径/分类

```python
@pytest.fixture
def conn():
    c = sqlite3.connect(":memory:")
    c.row_factory = sqlite3.Row
    c.execute("PRAGMA foreign_keys=ON")
    init_db(c)
    return c

def test_research_stage_expense_is_expensed(conn):
    svc = CollectService(conn)
    ...
    assert row["cap_status"] == "费用化"
```

- Red-Green-Refactor：新业务模块先写失败测试；bug 修复先写复现测试（Prove-It）
- 若 config 模块**在 import 时**读取环境变量（如 `MYAPP_DB_DIR`），
  conftest 里必须"先设 env → 删掉已导入的包模块 → 重新 import"，
  否则拿到的是首次导入时冻结的路径：

```python
@pytest.fixture(scope="session")
def db(tmp_path_factory):
    os.environ["MYAPP_DB_DIR"] = str(tmp_path_factory.mktemp("app"))
    for mod in list(sys.modules):        # 清掉已缓存的包模块
        if mod.startswith("myapp"):
            del sys.modules[mod]
    from myapp.models import seed        # 此时才导入，路径正确
    seed.seed_all()
    yield
```

## 2. 无头 GUI 冒烟（本技能的机器验证主路径）

原理：创建真实 App 但不 mainloop，用 `update()` 泵事件：

```python
root = tk.Tk()
root.withdraw()                      # 不显示窗口（仍需图形会话，见下注）
app = build_app(root)                # 与生产完全相同的组装函数
root.update()                        # 泵一轮事件，完成布局

# 断言 1：页面全部注册（用 pages 字典 + win.show(key) 切页，非 ttk.Notebook）
assert set(app.pages) == {"dashboard", "projects", "expenses", "collect", "reports", "risks"}
# 断言 2：数据到位（种子数据渲染进 Treeview）
app.win.show("expenses"); root.update()
assert len(app.pages["expenses"].tree.get_children()) >= 3
# 断言 3：交互路径（直接调 Controller 方法模拟点击后果）
app.project_controller.add_project({"name": "冒烟项目", ...})
root.update()
assert "冒烟项目" in dump_tree(app.pages["projects"].tree)

root.destroy()
```

要点：
- **模拟交互优先调 Controller 方法**，而不是 `event_generate` 合成鼠标点击
  （合成事件依赖窗口可见与焦点，无头下不可靠；Controller 方法是稳定接口。
  例外：`<<TreeviewSelect>>` 这类虚拟事件在 withdraw 下可靠，
  且**必须**测一次"选中主表行→从表联动"——这是 View↔schema 字段错位
  （KeyError）唯一能被机器抓到的路径）
- **等待 worker 线程 + after 轮询完成**的固定写法（勿用无回调的
  `root.after(20)`，它会阻塞消息泵）：

```python
import time
deadline = 200                        # 200 × 20ms = 4s 超时
while ctrl._busy and deadline > 0:    # 真实项目用 _busy 标志（单 worker 串行访问时）
    root.update()                     # update() 才会执行到期的 after 回调
    time.sleep(0.02)
    deadline -= 1
assert not ctrl._busy, "后台任务未在期限内完成"
```
- 模态对话框绕过：测试专用入口注入 `dict` 而非弹窗（Controller 的方法参数化）
- 断言后必须 `root.destroy()`，否则残留 Tcl 解释器影响后续用例
- 每断言一步 print 一行 `[OK] ...`，失败即非零退出——脚本兼做 CI 门禁
- 通用冒烟框架见 `scripts/smoke_test_gui.py`（逐页切换 + 主从联动断言，覆写 `build_app()` 即可套用任意示例）
- 注：`withdraw` 只是不显示，**仍需要图形会话**（Windows 桌面/交互式 CI 均可；
  纯无显示服务器会 `TclError: no display`——那种环境下只跑 Model 层测试）
- **复杂 Controller 集成用例也走本节（不再是独立节）**：`pytest.importorskip("tkinter")` 下建 Tk 实例 + `:memory:` DB，模式同无头冒烟；用 fixture 保证 `destroy()`。原「集成测试」节已并入此处——集成/单元/无头冒烟同走 `pytest`，无需单列章节。
- **要"进真实事件环 + 捕获 Tk 吞掉的回调异常 + 时序/after 验证"的确定性 GUI 回归**：见 `19-tkintertester.md`（作为 GUI Track 2，与本节浅层冒烟、① 的 pytest 逻辑层叠加，不替代它们）。

## 4. EXE 冒烟（发布门禁，不可跳过）

```powershell
# 注：Tkinter 窗口常不被 Get-Process 识别为 MainWindowTitle（返回空），
# 故用 tasklist /v 探测真实窗口标题，并以启动日志兜底校验（见 build_windows_exe.ps1）。
$p = Start-Process dist\MyTool.exe -PassThru
$ok = $false
for ($i = 0; $i -lt 15; $i++) {
    Start-Sleep 1
    if ($p.HasExited) { throw "EXE 启动即退出 (ExitCode=$($p.ExitCode))" }
    $tl = tasklist /fi "pid eq $($p.Id)" /v 2>$null
    if ($tl -match [regex]::Escape("MyTool")) { $ok = $true; break }
}
if (-not $ok) {      # 兜底：启动日志出现主界面装配完成则视为通过
    $log = "dist\logs\app.log"
    if ((Test-Path $log) -and (Select-String -Path $log -Pattern "主界面装配完成" -Quiet)) {
        $ok = $true
    }
}
if (-not $ok) { Stop-Process -Id $p.Id -Force; throw "EXE 启动后未出现主窗口" }
Stop-Process -Id $p.Id -Force
```

## 每次改码后的最小验证串（顺序执行）

1. `py_compile` 所有改动文件
2. `python -c "import <pkg>.app"` 导入测试（防精确替换断裂引用）
3. `pytest -q`（Model + 集成）
4. `python scripts/smoke_test_gui.py`（控件级冒烟）

## 交付门禁清单

- [ ] pytest 全绿
- [ ] 无头 GUI 冒烟全 [OK]
- [ ] 03-ui-design.md 设计质量自查清单过一遍
- [ ] EXE 冒烟通过（干净目录双击）
- [ ] logs/ 生成正常、无 ERROR
- [ ] 交付清单（docs/delivery-checklist.md）已填写

## 5. 深度测试框架（从"能跑通"到"业务对"）

当前金字塔（单元→集成→无头冒烟→EXE 冒烟）保证"代码能跑、控件存在、接线通"，
但**缺少"真实业务结果正确"的断言**——这正是"搜 000001 却返回 0 条"类 bug 漏网的根因：
打包前没有任何测试断言"业务结果对了"。补齐以下 L1–L5 深层层级，与浅层金字塔**叠加**：

```
L5 用户/验收测试   对照 ① 的 MoSCoW 验收标准，AI 真实弹窗自测逐条打勾（见 18-tkinter-mcp-server.md）
L4 端到端(E2E)     tkinter-mcp-server / pywinauto 拉起 EXE：输入→操作→断言落盘+DB+日志
L3 业务流程测试     search→多选→download_all→断言文件数+DB 行+无半途失败
L2 功能测试         query(000001) 只返 000001；query(空) 报错不崩
L1 数据驱动测试     parametrize:[代码×市场×日期×有效/无效] 矩阵
   （L1–L2 用 pytest + 临时目录 + 内存/临时 DB；L3–L5 用真实运行）
```

> 浅层金字塔是"门禁前哨"（快、廉价、每次改码必跑）；深层 L1–L5 是"业务正确性网"
> （慢、贵、PR 前/发布前必跑，且作为 bug 修复的**回归护网**）。

### 5.1 L1 数据驱动测试（Data-Driven）

同一逻辑 × 多数据集，用 `@pytest.mark.parametrize` 固化输入矩阵，避免"手测几个样例就发货"：

```python
import pytest

@pytest.mark.parametrize("code,market,start,end,expect_ok,n_expect", [
    ("000001", "SZSE", "2026-01-01", "2026-08-03", True,  1),  # 精确命中
    ("600036", "SHSE", "",          "",            True,  1),  # 上交所
    ("830799", "BSE",  "",          "",            True,  1),  # 北交所
    ("000001", "SHSE", "",          "",            False, 0),  # 代码与市场不匹配 → 应拦截
    ("",       "SZSE", "",          "",            False, 0),  # 空代码 → 应报错
    ("999999", "SZSE", "",          "",            True,  0),  # 格式有效但无公告
])
def test_search_matrix(code, market, start, end, expect_ok, n_expect):
    if not expect_ok:
        with pytest.raises(ValueError):
            api.query(stock_code=code, market=market,
                      start_date=start or None, end_date=end or None)
        return
    r = api.query(stock_code=code, market=market,
                  start_date=start or None, end_date=end or None)
    assert len(r.announcements) >= n_expect
    assert {a.sec_code for a in r.announcements} <= {code}  # 不混入其他股票
```

数据可外置到 `tests/data/*.json`，用 `pytest` 的 `pytest_generate_tests` 动态展开，
实现"算法与数据集分离"，新增用例只改数据不改代码。

### 5.2 L2 功能测试（Functional）

断言**组装后**的业务结果，而非孤立函数返回值。例（公告下载器）：

```python
def test_search_precise_only_target():
    r = api.query(stock_code="000001", market="SZSE",
                  start_date="2026-01-01", end_date="2026-08-03")
    assert r.announcements, "应有结果"
    assert {a.sec_code for a in r.announcements} == {"000001"}  # 关键回归断言

def test_search_empty_input_raises():
    with pytest.raises(ValueError):
        api.query(stock_code="", market="SZSE")
```

### 5.3 L3 业务流程测试（Business Process）

跨模块串联多步，验证"状态一致"而非单点：

```python
def test_download_workflow(tmp_path):
    res = api.query(stock_code="000001", market="SZSE",
                    start_date="2026-01-01", end_date="2026-08-03")
    selected = res.announcements[:3]
    out_dir = tmp_path / "out"
    svc.download_all(selected, out_dir)            # Controller 级调用，或走真实 UI
    assert len(list(out_dir.glob("*.pdf"))) == 3   # 磁盘落盘正确
    assert db.count_downloaded("000001") == 3      # DB 状态正确
```

### 5.4 L4 端到端 / UI 自动化测试（E2E + UI Automation）

驱动**真实运行**的应用走完核心业务路径，断言外部可观测结果（文件、DB、日志、控件树）。
**首选 `tkinter-mcp-server`**（见 `18-tkinter-mcp-server.md`）做 AI 驱动的真实事件环验证；
`pywinauto` 为备选。

tkinter-mcp-server 模板（源码态，经其 launcher 启动即带探针）：

```python
# 用 MCP 客户端 SDK 驱动（调用序列示意，可包装为 pytest）；widget_id 取自 get_ui_layout() 返回的控件树
# 1) launch_app(script_path="src/announcement_downloader/tkapp.py")   # 启动即带探针
# 2) is_connected() -> "true"
# 3) layout = get_ui_layout();  # 取控件树 JSON，定位搜索框 / 搜索按钮的 widget_id
# 4) type_text(widget_id=<搜索框 id>, text="000001")                  # 真实键入
# 5) click_widget(widget_id=<搜索按钮 id>)                            # 真实按钮事件
# 6) layout = get_ui_layout(); 断言 Treeview 行 secCode 全为 "000001" 且无其他股票
# 7) view_application() -> 截图，多模态核验中文标题无截断
# 8) close_app()
```

> 上述序列可固化为 pytest（用 MCP 客户端 SDK 调工具），纳入 L5 验收矩阵（见 §5.5）。
> 对 Tk 更稳、无需 Windows 专属依赖（pywinauto 对 Tk 窗口管理较脆弱）。

pywinauto 备选模板（EXE 态或无法走 MCP launcher 时）：

```python
from pywinauto.application import Application
from pathlib import Path

def test_e2e_search_download_exe():
    app = Application().start(r"dist\AnnouncementDownloader.exe")
    dlg = app.window(title="公告下载器")
    # —— 验证循环纪律：每步操作后扫描验证 + 截图纠错 + 智能缓存 ——
    # 与 tkinter-mcp-server 的 get_ui_layout()(读控件树) + view_application()(截图核验)
    # 是同一套"先读后断、逐步验证"纪律，仅执行器不同。
    dlg.Edit.type_keys("000001")                # 真实键入
    assert dlg.Edit.exists(), "搜索框未就绪"      # ① 扫描验证：操作后确认控件/状态
    dlg["搜索(&S)"].click()                     # 真实按钮事件
    rows = dlg.ListView.get_items()
    assert rows and all("000001" in r.texts() for r in rows), "结果未出现/混入其他股票"  # ① 验证
    dlg.capture_as_image().save("out/e2e_search.png")  # ② 截图纠错（等价 MCP view_application()）
    dlg["下载(&D)"].click()
    assert any(out.glob("*.pdf") for out in Path("downloads").glob("*"))
    app.kill()
```

> **验证循环纪律（硬化 pywinauto 回退段，唯一可移植的 SOP 模式）**：pywinauto 对 Tk 窗口管理较脆弱，单点 `click`/`type_keys` 后**绝不能只调一次就断言**，必须做"操作 → 验证 → 纠错"循环：
> 1. **每步操作后扫描验证**：每步之后立即重新读取控件树/状态（pywinauto 侧用 `exists()`、`wrapper_object()`、`子控件.texts()`，等价 MCP `get_ui_layout()`）确认上一步真的生效，再进下一步；
> 2. **截图纠错**：关键步骤后 `capture_as_image()` 存盘对照（等价 MCP `view_application()` 多模态核验），发现错位/截断立即中断，不靠最后一条断言兜底；
> 3. **智能缓存**：首轮跑通后缓存"控件路径 ↔ (title/class/automation_id)"映射与窗口句柄，后续重放跳过重复探测，降低 Tk 控件树不稳定的重试成本。
>
> 这套纪律同样适用于 tkinter-mcp-server 的 L4/L5 会话（其 `get_ui_layout` + `view_application` 已内建"读-断"循环），与 `21-` 思路完全一致——只是执行器从 MCP/AI 换成了 pywinauto 脚本。

### 5.5 L5 用户/验收测试（Acceptance）与回溯

① 需求阶段的 MoSCoW 验收标准必须**逐条映射**到自动化检查，形成可追溯矩阵：

| 验收标准（① 产出） | 类型 | 自动化检查（落点） |
|---|---|---|
| 用户输入代码能精确查到该股票公告 | 功能 | `test_search_precise_only_target`（L2） |
| 非法/空输入给出明确报错 | 功能 | `test_search_empty_input_raises`（L1/L2） |
| 一键下载全部选中公告到本地 | 业务流程 | `test_download_workflow`（L3） |
| 界面中文/控件可见无截断 | UI | tkinter-mcp-server `view_application` 多模态核验（L4/L5） |

回溯方法：验收标准 ID（如 `AC-01`）写入测试名/标记 `@pytest.mark.acceptance(ids=["AC-01"])`，
PR 模板与交付清单引用该矩阵，缺映射的验收项视为"未验证"。

## 6. 深度测试金字塔（叠加示意）

```
         L5 验收/用户测试   ← tkinter-mcp-server 真实弹窗自测逐条打勾
        L4 端到端(E2E)      ← tkinter-mcp-server / pywinauto 真实运行断言落盘
       L3 业务流程测试       ← 跨模块串联 + 状态一致
      L2 功能测试            ← 组装后业务结果正确
     L1 数据驱动测试         ← parametrize 输入矩阵
   ─────────────────────────  （以下为既有浅层金字塔，保持）
   无头 GUI 冒烟 / 集成 / 单元 / EXE 启动冒烟
```

两层金字塔互补：浅层保"能跑"，深层保"业务对"。

## 7. 深度测试：可选还是必经？产出物有哪些？

- **定位：门禁前的"业务正确性网"——发布 / 重大 bug 修复前必经；不是每次改码都跑。**
  每次改码的轻量门禁仍是无头冒烟 + pytest（快、廉价）；深层 L1–L5 在合并 / 发布前补齐，
  并作为 bug 修复的回归护网（修一个业务 bug 先写一条 L1–L3 复现测试）。
- **产出物（即"测试结果反馈"）**：
  1. **测试用例**：`tests/test_*.py` 里的 parametrize 矩阵 + L2/L3 函数 + L4/L5 的 MCP / pywinauto 会话脚本；
  2. **测试结果**：pytest 报告（JUnit XML / `pytest -q` 文本）+ L4 截图（`view_application` 导出的 PNG）+ L5 验收矩阵（AC-ID ↔ 测试 映射表，缺映射即"未验证"）；
  3. 上述产出随 `release_gate.py` 一起作为发布证据，登记进交付清单（`docs/delivery-checklist.md`）。

## 8. tkintertester：真实事件环 GUI 行为回归（Track 2）

`09` 既有金字塔（单元→集成→无头冒烟→EXE 冒烟）与深层 L1–L5 保证"逻辑对、控件在、接线通、业务结果对"，但**浅层无头冒烟绕过真实事件环**（直接调 Controller、不进 mainloop），因此漏掉两类 GUI 缺陷：① Tk **静默吞掉的回调异常**（按钮 `command=` / 事件绑定 / `after()` 回调里抛异常不传播）；② **时序 / `after()` / 生命周期**行为（只有进 mainloop 才能验证）。

`tkintertester`（`19-tkintertester.md`）补这一层：开发者写 step 函数、在**真实 `mainloop()` 内**确定性地跑 GUI 行为序列，覆写 `report_callback_exception` **捕获回调异常并判失败**，且测试间 `entry()`/`reset()` 隔离。它**不替代**以下任一手段，而是作为 GUI Track 2 与它们叠加：

| 手段 | 管哪一层 | 与 tkintertester 的关系 |
|---|---|---|
| `pytest` 单元/集成 | 纯逻辑 | 保留；tkintertester 不碰逻辑 |
| `smoke_test_gui.py`（无头） | 浅层 GUI 门禁（快、每次改码） | tkintertester 更强：进真实事件环 + 捕获吞掉的异常 |
| **tkintertester** | **真实事件环 GUI 行为回归（CI 确定性）** | 本层 |
| `tkinter-mcp-server`（21） | AI 驱动真实运行 + 多模态（L4/L5） | 互补：MCP 适合 AI 验收/截图；tkintertester 适合 CI 回归 |
| `pywinauto` | EXE 态真实 UI（降级备选） | 同上 |

**项目落地建议（two-track）**：
- `tests/`：`pytest` 逻辑测试（Track 1，每次改码必跑，快）。
- `guitests/`：`tkintertester` GUI 行为测试（Track 2，PR 前/发布前跑，确定性、可进 CI）。
- 验收/L4/L5 多模态仍走 `tkinter-mcp-server`（21）；EXE 冒烟走既有 `build_windows_exe.ps1`。

> 接入要求：应用需拆出 `entry()`/`reset()` 并暴露模块级 `widgets` 字典（详见 `22` §8）。
