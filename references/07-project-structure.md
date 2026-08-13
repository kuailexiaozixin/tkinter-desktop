# 07 项目结构与入口规范

## 标准 src 结构

```
my-tool/
├── pyproject.toml
├── README.md
├── .gitignore
├── .venv/
├── data/                 # 运行时 SQLite（不入库，.gitignore）
├── logs/                 # 运行日志（不入库）
├── docs/
│   ├── architecture.md
│   └── modules.md
├── scripts/
│   └── smoke_test_gui.py
├── src/
│   ├── launcher.py       # ★ 打包入口：只做 from <pkg>.app import main; main()
│   └── <pkg>/
│       ├── __init__.py
│       ├── __main__.py   # python -m <pkg> 开发入口
│       ├── app.py        # 组装：DPI → Tk() → 字体/Style → 页面 → mainloop
│       ├── common/  models/  views/  controllers/   # 见 02-architecture-mvc.md
└── tests/
    └── test_*.py         # Model 层测试（无 tkinter）
```

## 双入口规范

- **开发**：`python -m <pkg>`（依赖 `__main__.py`），包内可用相对导入
- **打包**：PyInstaller 指向 `src/launcher.py`，launcher 只有两行：

```python
from <pkg>.app import main
main()
```

理由：直接把包内模块当脚本打包，冻结后相对导入会报
`attempted relative import with no known parent package`。顶层 launcher +
`--paths src` 是最稳组合。

## app.py 入口模板（顺序敏感，不可乱排）

```python
def main():
    setup_dpi()                    # 1. DPI —— 必须在 Tk() 之前
    setup_logging()                # 2. 文件日志 + excepthook
    root = tk.Tk()
    root.withdraw()                # 3. 先藏窗口，初始化完再 deiconify（防白屏闪烁）
    setup_fonts(); setup_style()   # 4. 字体/样式 —— 在建业务控件之前
    conn = get_conn(); init_db(conn)
    build_ui(root, conn)           # 5. 组装页面与控制器
    center(root, 1280, 800)
    root.deiconify()
    root.report_callback_exception = ui_excepthook   # 6. 回调异常兜底
    root.mainloop()
```

## 异常兜底（--windowed 交付必备）

```python
def ui_excepthook(exc_type, exc, tb):
    logging.error("UI 异常", exc_info=(exc_type, exc, tb))
    messagebox.showerror("程序出错", f"{exc}\n\n详情见 logs/ 目录")
```

- `root.report_callback_exception`：捕获**事件回调内**异常（默认只打印 stderr，
  --windowed 下用户完全无感知）
- `sys.excepthook`：捕获 mainloop 外异常
- 双钩都要挂；日志里必须有完整 traceback

## 路径与配置（common/config.py）

```python
import sys
from pathlib import Path

FROZEN = getattr(sys, "frozen", False)
BASE_DIR = Path(sys.executable).parent if FROZEN else Path(__file__).resolve().parents[3]
DATA_DIR = BASE_DIR / "data"
LOG_DIR  = BASE_DIR / "logs"

def resource_path(rel: str) -> Path:
    """打包进 EXE 的只读资源（图标、.tcl 主题）——写数据禁止用这里"""
    base = Path(getattr(sys, "_MEIPASS", BASE_DIR))
    return base / rel
```

两条路径规则背下来：
- **可写数据**（db/日志/导出）→ `BASE_DIR`（EXE 同级），基于 `sys.executable`
- **只读资源**（图标/主题）→ `sys._MEIPASS`，打包时 `--add-data` 塞进去

## 日志（common/logging_setup.py）

- `TimedRotatingFileHandler`，按日分文件，保留 30 天，UTF-8
- 格式：`%(asctime)s %(levelname)s %(name)s %(message)s`
- --windowed 下**不要加 StreamHandler 往 stdout 写**（stdout 为 None，
  logging 内部虽然吞异常但等于白写）；调试期可加判断
  `if sys.stderr is not None: 加流处理器`

## pyproject.toml 要点

```toml
[project]
name = "my-tool"
requires-python = ">=3.11"
dependencies = []                 # tkinter/sqlite3 是标准库，常见项目零运行依赖

[dependency-groups]
build = ["pyinstaller>=6"]        # 构建期依赖，不进运行时
dev = ["pytest>=8"]
```
