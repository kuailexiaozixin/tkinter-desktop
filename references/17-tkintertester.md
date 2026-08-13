# 22 tkintertester：真实事件环内的 GUI 行为回归（代码驱动）

> 上游项目：[github.com/LionKimbro/tkintertester](https://github.com/LionKimbro/tkintertester)（**CC0 公共领域**，PyPI 包名 `tkintertester`，本机实测版本 **0.1.0**）。
> 本文件说明它是什么、怎么装、API（已对照本机安装源码 `tkintertester/harness.py` 逐条核实），以及如何在 tkinter-desktop 工作流（尤其测试与质检）中融入。
> 它补齐 `09-testing-and-quality.md` 里"无头冒烟（绕开真实事件环，直接调 Controller）"与"tkinter-mcp-server（21，AI 驱动、需外部 launcher+socket）"之间缺失的一层：**开发者写代码、在真实 `mainloop()` 内确定性地跑 GUI 行为序列的回归测试**。

## 1. 它是什么

**极简、事件循环原生（event-loop-native）的 Tkinter GUI 测试框架**。测试在**真实的 Tk 事件循环**里运行——无 async、无线程、无独立进程。每个测试由若干 **step 函数**组成，经 `root.after()` 调度逐步执行；被测应用在每测试前全新创建、测试后销毁，测试间相互隔离。

它要解决的三个 Tk 测试老问题（也是本技能既有无头冒烟的盲区）：

1. **Tk 不能干净重启**：同一进程 `destroy` 一个 Tk root 再建新的是不可靠的，导致 pytest/unittest 里"建窗→拆窗"的 fixture 不稳。tkintertester 用单一隐藏 root + `entry()`/`reset()` 重建应用规避。
2. **Tk 跑阻塞事件循环**：不能从测试代码直接"调用" GUI 并检视（会阻塞 mainloop 或需线程/async 复杂度）。tkintertester 让测试作为 `after()` 调度的回调在循环内执行。
3. **Tk 静默吞掉异常**：回调里抛异常只打到 stderr 不传播，测试照跑。tkintertester 覆写 `root.report_callback_exception`，**捕获回调异常并把当前测试判失败**（本机实测：button `command=` 里 `raise RuntimeError` 被记为 `status:"fail"` + `fail_message:"Tk callback exception: ..."` + 完整 traceback）。

> **本机实测验证点**：`pip install tkintertester==0.1.0` 成功；跑官方 counter 范例 **2/2 成功**；跑"回调抛异常"范例被正确捕获为 fail。
> **关键更正（实测优于文档）**：上游 `docs/reference.md` 列了 `get_root()`，但 0.1.0 实测该函数**不存在**（取 root 用 `harness.g["root"]`）。文档其余 API 与 0.1.0 一致。

## 2. 与既有测试手段的关系（定位）

| 手段 | 角色 | 与 tkintertester 的关系 |
|---|---|---|
| `pytest` 单元/集成 | 纯逻辑正确性 | 保留；tkintertester 不碰逻辑层 |
| `smoke_test_gui.py`（无头） | 浅层门禁前哨（快、每次改码） | tkintertester **更强**：同样跑真实控件，但进 `mainloop()`、`after()`/回调路径可被验证、且**捕获 Tk 吞掉的异常** |
| `tkinter-mcp-server`（21） | AI 驱动真实事件环 + 多模态截图（L4/L5） | 互补：MCP 需外部 launcher+socket、适合 AI 交互/验收/截图；tkintertester 纯代码、无 AI、确定性、**适合 CI 回归** |
| `pywinauto` | 真实 UI 自动化（EXE 态，Windows 专属） | 降级备选；tkintertester 在源码态跑，不依赖 Windows 句柄 |
| **tkintertester** | **源码态 GUI 行为回归（真实事件环、代码驱动、CI 友好）** | **新增的 GUI Track 2** |

放进 09 的金字塔：`pytest`(逻辑) → `smoke_test_gui.py`(浅层 GUI 门禁) → **tkintertester(真实事件环 GUI 行为回归)** → tkinter-mcp-server/pywinauto(L4/L5 真实运行+多模态)。

## 3. 安装

```bash
pip install tkintertester
```

> ⚠️ **镜像站 build-isolation 坑**（已实测）：默认 tuna 镜像在构建隔离环境里找不到 `setuptools>=61`（报 `Could not find a version that satisfies the requirement setuptools>=61.0`）。这是镜像问题不是包问题；用官方源绕过：
> `pip install tkintertester --index-url https://pypi.org/simple`
> （本机用官方源成功装到 0.1.0。）

## 4. API（已对照本机 0.1.0 源码核实）

全部是 `tkintertester.harness` 模块级函数（无类、无 TestCase 夹具）：

| 函数 | 签名（实测） | 作用 |
|---|---|---|
| `run_host` | `run_host(app_entry, flags='')` | Host 模式：建隐藏 Tk root 并拥有生命周期，跑完所有测试后退出或转正常运行时 |
| `attach_harness` | `attach_harness(root, flags='')` | 挂载到已运行的 Tk 应用；`"x"` flag 不允许（抛 RuntimeError） |
| `add_test` | `add_test(title, steps, flags='')` | 注册测试，`steps` 为 step 函数列表（会防御性拷贝）；`flags="q"` 表示预期调 `harness.quit()` |
| `set_timeout` | `set_timeout(timeout_ms)` | 每测试超时毫秒，默认 5000；须在 `run_host`/`attach_harness` 前调用 |
| `set_resetfn` | `set_resetfn(app_reset)` | 注册重置函数（host 模式每测试后调），负责拆掉 `entry()` 建的应用 |
| `quit` | `quit()` | 应用退出信号，替代 `root.quit()` |
| `get_results` | `get_results(flags='')` | 返回结果摘要；无 flag 文本，`"J"` 为 JSON 数组 |
| `print_results` | `print_results(flags='')` | 打印 `get_results()` |
| `write_results` | `write_results(filepath, flags='')` | 写结果到文件（utf-8） |
| `show_results` | `show_results(flags='')` | 弹 Tk Toplevel 显结果（需 harness 已运行，`g["root"]` 设好） |

全局状态（无 TestCase 助手，用 globals）：
- `harness.g`：字典，含 `root`、`current_test`、`current_step_index`、`test_done`、`exit_requested` 等键。
- `harness.tests`：测试字典列表，执行后原地填入结果。

`flags`：`"x"` 测试后退出 mainloop；`"s"` 测试后弹结果窗。

## 5. step 函数契约

每个 step 是空参可调用对象，返回 `(action, value)`，**必须非阻塞**（禁止 `time.sleep`）：

| 返回值 | 含义 |
|---|---|
| `("next", None)` | 立即进入下一步 |
| `("next", ms)` | `ms` 毫秒后进入下一步 |
| `("wait", ms)` | `ms` 毫秒后**重复本步** |
| `("goto", index)` | 跳至 index 步 |
| `("success", None)` | 立即标记成功 |
| `("success", ms)` | `ms` 毫秒后标记成功 |
| `("fail", reason)` | 立即以 reason 失败 |

所有步耗尽且无显式 success/fail → 视为成功。步内抛异常 → 测试失败，traceback 存入 `exception`。

## 6. 工作原理（简图）

```
[测试 step 函数]  ⇄  root.after() 调度  ⇄  [真实 Tk mainloop]  ⇄  [应用 entry()/reset()]
```

- host 模式：`run_host` 建隐藏 root → 每测试 `entry()` 建应用 → 按序跑 steps（每个 step 经 `after()` 回到循环）→ 结束 → `reset()` 拆 → 下一测试。
- 回调异常被 `report_callback_exception` 覆写捕获 → 测试判 fail（这是它相对 `smoke_test_gui.py` 的核心优势）。
- 应用退出必须走 `harness.quit()`，不可直接 `root.quit()`。

## 7. 在工作流中的融入

按阶段映射（①–⑧），**重点在 ⑨ 测试与质量门禁、⑦ 运行验证、⑤ 界面设计**：

### ⑨ 测试与质量门禁（主战场）
- **作为 GUI Track 2 回归**：把"真实事件环内的 GUI 行为"写成 `guitests/test_*.py`（每文件 `run_host(entry, "x")` + `print_results`/`write_results`），纳入 09 §7 的"测试产出"。
- **专治 `smoke_test_gui.py` 测不到的两类 bug**：
  1. **回调异常被 Tk 吞掉**：按钮 `command=` / 事件绑定 / `after()` 回调里抛异常，无头冒烟（直接调 Controller）发现不了，tkintertester 能捕获。
  2. **时序 / `after()` / 生命周期**：计数器防抖、`after(ms)` 轮询、窗口 `protocol("WM_DELETE_WINDOW")` 等真实事件环行为，只有进 mainloop 才能验证。
- 与 09 既有金字塔叠加：浅层（pytest + 无头冒烟）保"能跑"；tkintertester 保"真实事件环内 GUI 行为对"；MCP/pywinauto 保"真实运行+多模态"。

### ⑦ 运行验证
- 在"无头 GUI 冒烟"之后、"AI 真实弹窗自测（MCP）"之前，可加一道 tkintertester GUI 回归（确定性强、无需 AI、适合每次提交）。
- 异常路径（空输入触发回调异常）会被它抓成 fail，比无头冒烟更可靠地暴露"事件分发路径"的缺陷。

### ⑤ 界面设计
- tkintertester 不替代 MCP 的 `view_application` 视觉核验（它不做截图）；视觉/中文截断仍走 21。但 tkintertester 可断言"点击后控件文本/启用态/可见性正确"，是视觉之外的**行为**正确性网。

### 与 21（tkinter-mcp-server）的协同
- 两者都跑真实事件环；但 tkintertester 是**开发者写代码、确定性、CI 可重复**，适合放进回归套件；MCP 是 **AI 现场驱动、带截图、适合验收/L4–L5**。一个项目可同时用：逻辑→pytest，GUI 行为→tkintertester（CI 每次跑），验收→MCP（PR 前 AI 跑）。

## 8. 应用需满足的结构约束（接入要求）

tkintertester 不拥有你的控件——它靠共享状态工作：

1. 应用要拆出 `entry()`（每测试前建 UI，挂到 `harness.g["root"]` 下的 Toplevel）与 `reset()`（拆 UI、清 `widgets`）。
2. 控件引用集中放一个模块级 `widgets` 字典（step 函数里直接 `widgets["button"].invoke()` / `widgets["label"].cget("text")` 断言）。
3. 退出走 `harness.quit()` 而非 `root.quit()`。

> 本技能既有应用多用 `build_app(root)` 组装。接入模式：包一层 `entry()` 调 `build_app(harness.g["root"])`、把内部 `widgets` 暴露到模块级，再 `set_resetfn` 调拆窗函数。

## 9. 示例

### 9.1 官方 counter（本机 2/2 通过）

```python
import tkinter
from tkinter import ttk
from tkintertester import harness

app = {"count": 0, "toplevel": None}
widgets = {}

def entry():
    app["count"] = 0
    win = tkinter.Toplevel(harness.g["root"])
    app["toplevel"] = win
    widgets["label"] = ttk.Label(win, text="0")
    widgets["label"].grid(row=0, column=0, padx=20, pady=10)
    widgets["button"] = ttk.Button(win, text="Increment",
                                   command=handle_click)
    widgets["button"].grid(row=1, column=0, padx=20, pady=10)

def reset():
    if app["toplevel"]:
        app["toplevel"].destroy(); app["toplevel"] = None
    widgets.clear()

def handle_click():
    app["count"] += 1
    widgets["label"].config(text=str(app["count"]))

def test_initial():
    def step():
        return ("success", None) if widgets["label"].cget("text") == "0" else ("fail", "init!=0")
    return [step]

def test_increment():
    def step_click():
        widgets["button"].invoke(); return ("next", None)
    def step_verify():
        return ("success", None) if widgets["label"].cget("text") == "1" else ("fail", f"got {widgets['label'].cget('text')}")
    return [step_click, step_verify]

if __name__ == "__main__":
    harness.set_timeout(3000); harness.set_resetfn(reset)
    harness.add_test("Initial is zero", test_initial())
    harness.add_test("Increment once", test_increment())
    harness.run_host(entry, "x")
    harness.print_results()
```

### 9.2 业务流（搜索→断言不混入其他项，对应 09 L2/L3）

```python
# guitests/test_search.py —— 真实事件环内验证"搜 000001 只返 000001"
def entry():
    g_app["root"] = harness.g["root"]
    app.entry()                       # 复用既有 build_app 逻辑

def test_search_precise():
    def step_type():
        widgets["code_entry"].delete(0, "end")
        widgets["code_entry"].insert(0, "000001")
        return ("next", None)
    def step_click():
        widgets["search_btn"].invoke()       # 触发真实按钮 command
        return ("wait", 50)                  # 等 after() 轮询完成（真实事件环）
    def step_verify():
        rows = widgets["tree"].get_children()
        secs = {widgets["tree"].set(r, "secCode") for r in rows}
        if secs <= {"000001"} and rows:
            return ("success", None)
        return ("fail", f"混入其他股票: {secs}")
    return [step_type, step_click, step_verify]

harness.set_resetfn(app.reset)
harness.add_test("搜000001只返000001", test_search_precise())
harness.run_host(entry, "x")
harness.write_results("out/guitest_search.json", "J")
```

## 10. 局限与注意

- **需图形会话**：`run_host` 建 Tk root，Windows 桌面/交互 CI 可跑；纯无显示服务器会 `TclError: no display`（同无头冒烟的 `withdraw` 限制），那种环境只跑 pytest 逻辑层。
- **无类/TestCase 夹具**：纯模块函数 + 全局 `g`/`widgets`，与 pytest 的 fixture 体系正交；GUI 测试文件自己 `run_host` 跑（不是 `pytest` 收集）。
- **不拥有控件**：靠共享 `widgets` 字典与 `harness.g`，应用要按 §8 改造（拆 `entry()`/`reset()`）。
- **`get_root()` 在 0.1.0 不存在**：上游 reference.md 列了它，但本机实测无此函数；取 root 用 `harness.g["root"]`。
- **与 MCP 互补不替代**：要"AI 现场驱动 + 截图多模态"仍用 21；要"确定性 CI GUI 行为回归"用本文件。

## 11. 快速决策

- 纯逻辑（金额/口径/分类） → `pytest`（最快最稳）。
- 只要"控件存在/接线通" → 无头 `smoke_test_gui.py`（每次改码必跑，快）。
- 要"真实事件环内 GUI 行为对 + 捕获 Tk 吞掉的回调异常 + 时序/after 验证 + CI 确定性回归" → **tkintertester（本文件）**。
- 要"AI 驱动真实点击 + 中文渲染多模态核验 + 验收 L4/L5" → **tkinter-mcp-server（21）**。
