# 调试纪律（Debug）

> 定位：**失败之后的处理闭环**。`09-testing-and-quality.md` 与 `14-tdd-methodology.md` 回答「行为对不对」，Debug 回答「失败为什么发生、怎么修好」。
> 与静态关卡（语法/导入/Ruff，见 `09` §「每次改码后的最小验证串」）、动态验证（pytest / 无头 GUI 冒烟 / EXE 冒烟 / tkintertester）互补：任何 Check/Test 失败后进入本节闭环。
> 排障知识沉淀库：`../docs/troubleshooting.md`（执行中问题 → 现象/本质/解决，优先沉淀于此）。

---

## 调试总纲：复现 → 定位 → 修复 → 回归 → 沉淀

任何失败按固定闭环处理，**绝不无测试修 bug、绝不「改了没验证」**：

1. **复现**：先写能稳定失败的复现（复现测试 / 最小用例），确认失败原因正确（不是拼写/环境错）。
2. **定位**：用日志、断点、无头 `root.update()` 泵事件、二分法缩小范围，找出根因。
3. **修复**：最小改动修复，不过度设计。
4. **回归**：重跑 `python scripts/release_gate.py`（pytest → 无头 GUI 冒烟 → 导入检查）全绿，确认无回归。
5. **沉淀**：将现象/本质/解法写入 `../docs/troubleshooting.md`，避免重复踩坑。

---

## Prove-It 模式（Bug 修复必做）

收到 bug → **先写复现测试（必失败）→ 实现修复 → 测试通过 → 跑全量防回归**。**绝不无测试修 bug。**

```
bug 报告
  ↓
写复现测试（应当 FAIL，如 test_bug_147_...）
  ↓
测试 FAIL（确认 bug 存在）
  ↓
实现修复（最小改动）
  ↓
测试 PASS（证明修好）
  ↓
跑全量 release_gate.py（pytest + 冒烟 + 导入，无回归）
```

> 复现测试一旦写入**永远不删除**——它是该 bug 的永久疫苗（见 `14-tdd-methodology.md` §3）。Prove-It 细节、tkinter 特化的三种 Red-Green 模式见 `14-tdd-methodology.md` §1/§3。

---

## Flaky 重复跑纪律

为让「全绿」结论可信，关键测试可加重复跑兜底：

- 安装 `pytest-rerunfailures`（或 `pytest-repeat`）：在项目 dev 依赖组追加；
- 关键测试加 `@pytest.mark.flaky(reruns=3)`（worker 线程 / 文件类易抖动的集成测试）；
- CI 层对整轮加 `--reruns` 或作业重试；
- 重复跑**只能兜底偶发环境抖动**，不能掩盖真实失败；若某测试频繁 flaky，必须修根因（竞态 / 未隔离状态 / 时间依赖 / Tcl 解释器残留）。

> tkinter 特化 flaky 主因（见 `14-tdd-methodology.md` §6）：worker 线程结果未就绪就断言 → 用 `after` 轮询 + deadline 超时循环；Tcl 解释器残留 → 每个 fixture 都 `root.destroy()`；import 时读环境变量 → conftest 先设 env → `del sys.modules` → 再 import。

---

## 改后干净复测回路（防「改了但没生效」假象）

> 典型踩坑：改了业务模块，但重跑时命中了**仍驻留内存的旧 Tcl 解释器 / 旧进程**，导致反复误判「修改无效」。

任何「改代码后复测」的流程，必须先确保**真的加载了新代码**：

1. 若改了 `models/` / `controllers/`：先跑 `py_compile` + 包导入测试，确认无语法/引用断裂；
2. 若跑了无头 GUI 冒烟后残留 Tcl 解释器：确认每个 fixture 都 `root.destroy()`，或重启 Python 进程；
3. 复测前先跑 `python scripts/run_dev.py --fast`（语法+导入），确认改动文件被正确加载（无旧 `.pyc` / 缓存）；
4. 再跑完整 `release_gate.py`。第 3 步能根除「改了但没生效」的假象。

---

## 排障沉淀

- 任何「现象 → 根因 → 解法」一旦确认，立即追加到 `../docs/troubleshooting.md`，避免重复踩坑；
- 沉淀格式：现象（可复现症状）/ 本质（根因）/ 解决（最小修复 + 验证）。
