# 05 线程与异步（主线程规则）

> Tkinter 非线程安全。**所有 widget 操作只能发生在创建 `Tk()` 的线程。**
> 违反的症状：偶发 `RuntimeError: main thread is not in main loop`、
> `Tcl_AsyncDelete: async handler deleted by the wrong thread`、无提示闪退、界面卡死。

## 决策树

```
操作耗时 < 100ms？ ──是──> 直接在事件回调里做
        │否
        ↓
需要周期执行？ ──是──> root.after(ms, fn)（fn 内再 after 自己，形成节拍器）
        │否
        ↓
一次性长任务（网络/大文件/大查询）
        → worker 线程 + queue.Queue + after 轮询（下方标准模式）
```

## 标准模式：线程 + 队列 + after 轮询

```python
import threading, queue

class LongTaskRunner:
    """通用后台任务执行器：worker 只算不碰 UI，主线程轮询收结果。"""
    def __init__(self, root):
        self.root, self.q = root, queue.Queue()

    def run(self, work_fn, on_done, on_error=None):
        def worker():
            try:
                self.q.put(("ok", work_fn()))
            except Exception as e:       # noqa: BLE001 —— 必须全捕获，异常带回主线程
                self.q.put(("err", e))
        threading.Thread(target=worker, daemon=True).start()
        self._poll(on_done, on_error)

    def _poll(self, on_done, on_error):
        try:
            status, payload = self.q.get_nowait()
        except queue.Empty:
            self.root.after(100, self._poll, on_done, on_error)
            return
        if status == "ok":
            on_done(payload)             # 此时已在主线程，可安全刷 UI
        elif on_error:
            on_error(payload)
```

Controller 用法：

```python
def on_import_excel(self):
    self.view.set_busy(True)             # 按钮禁用 + 进度条 start()
    self.runner.run(
        work_fn=lambda: self.svc.import_excel(path),      # 纯计算，无 UI
        on_done=lambda n: (self.view.set_busy(False), self.reload(),
                           self.view.set_status(f"导入 {n} 条")),
        on_error=lambda e: (self.view.set_busy(False),
                            messagebox.showerror("导入失败", str(e))),
    )
```

## 铁律

1. **worker 函数里禁止出现任何 widget / tk 变量**（连 `StringVar.set` 都不行，
   它底层走 Tcl 解释器同样非线程安全）
2. **worker 必须整体 try/except**：子线程未捕获异常不会进主线程 excepthook，
   会静默消失——必须打包成消息带回主线程处理
3. **daemon=True**：防止用户关窗口后残留线程拖住进程不退出
4. **sqlite3 连接的线程边界（重要 nuance）**：默认 `check_same_thread=True`，
   **在别的线程用同一连接会直接抛 `sqlite3.ProgrammingError`**（已运行核实：
   `SQLite objects created in a thread can only be used in that same thread`）。
   可用的三种模式：
   - **模式 A（最推荐，最简单）**：worker 只做纯计算，**DB 读写留在主线程**
     （在 `on_done` 里执行），彻底避开跨线程用连接。
   - **模式 B（官方推荐）**：worker 内 `get_conn()` **新开一条独立连接**用完即关，
     每线程各自连接、互不干扰（`sqlite3` 官方建议"每线程一连接"）。
   - **模式 C**：App 级**单连接 + `check_same_thread=False`**，
     靠 `_busy` 忙标志保证**同一时刻只有一个 worker**，且 worker 运行期间主线程不碰库
     → 事实串行。⚠️ **`check_same_thread=False` 只是关掉线程校验，并不让连接变线程安全**：
     多 worker 并发访问同一连接仍可能损坏连接/数据，必须靠串行化（单 worker + 主线程闲置）
     或 `threading.Lock` 保护（已核实：设 `False` 后跨线程用连接不再报该错，但安全性需自保）。
   详见 `06` 数据层。
5. **禁止 `time.sleep` 出现在主线程**；等待用 `after`
6. **进度上报**：worker 周期性 `q.put(("progress", pct))`，轮询函数分支处理并
   `progressbar["value"] = pct`

## 示例：归集中心（示意）

下方是一个归集 Controller 的示意落地，worker 内顺带做 DB 写库
（走模式 C：共享单连接 + `check_same_thread=False` + `_busy` 串行）：

```python
import queue, threading
from ..services import engine

class CollectController:
    def __init__(self, app):
        self.app = app
        self.view = None                       # 由 MainController 注入
        self._q: queue.Queue = queue.Queue()
        self._busy = False

    def run(self, kind, month=None):
        if self._busy:                         # 单 worker 串行护栏
            self.view.append_log("上一个归集任务尚未完成，请稍候…", "warn")
            return
        self._busy = True
        title, fn = RUNNERS[kind]

        def worker():
            try:
                self._q.put(("done", fn(month)))   # 只放结果，绝不碰 widget
            except Exception as exc:                # noqa: BLE001
                log.exception("归集失败：%s", kind)
                self._q.put(("error", str(exc)))    # 异常带回主线程
        threading.Thread(target=worker, daemon=True).start()
        self._poll()

    def _poll(self):
        try:
            status, payload = self._q.get_nowait()
        except queue.Empty:
            self.view.after(80, self._poll)        # after 挂在任何 widget 上都行
            return
        self._busy = False
        if status == "error":
            self.view.append_log(f"✗ 执行异常：{payload}", "err")
            return
        ...                                          # 主线程安全刷新 UI
        self.app.refresh_pages("dashboard", "expenses")
```

要点（均与本技能一致）：
- worker **只 `q.put`**，UI 操作（`append_log` / `refresh_pages`）全在 `_poll` 主线程做；
- `_busy` 保证同时只有一个 worker，配合模式 C 的串行访问才安全；
- `_poll` 用 `self.view.after(80, ...)` 而非 `root.after` —— `after` 是 Widget 方法，
  挂在任何存活 widget 上都可（已核实 `ttk.Frame.after` 存在）；
- `daemon=True` 防关窗后线程拖住进程（铁律 3）。

## after 使用规范

- `after(0, fn)`：把 fn 排到事件队列尾部（常用于"等当前事件处理完再做"）
- `after_idle(fn)`：空闲时执行
- 周期任务记得保存 id 并在页面销毁时取消：
  `self._timer = root.after(1000, tick)` / `root.after_cancel(self._timer)`，
  否则窗口销毁后回调触发报 `invalid command name`
- **update() 慎用**：`root.update()` 会重入事件循环，在按钮回调里滥用会导致
  递归重入与诡异状态；刷新界面用 `update_idletasks()` 就够
