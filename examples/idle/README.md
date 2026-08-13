# IDLE（完整源码示例）

本目录包含 **IDLE（Python 官方 IDE）的完整源码**（取自 CPython 3.13.14
标准库中的 `idlelib` 包，**未做任何改动**），用于展示一个真实、复杂的
Tkinter 桌面软件是如何组织与生产化的。

- `idlelib/` —— CPython 官方完整 idlelib 源码包（146 个文件，含
  `pyshell.py`、`editor.py`、`config-*.def`、`Icons/` 等）。
- `run.py` / `启动.bat` —— 启动入口，**指向本目录内的本地源码**，而非系统
  Python 自带的 idlelib。

## 运行方式

IDLE 仅依赖 Python 标准库与 Tkinter，无需额外安装依赖。直接启动：

    python run.py
    # 或双击 启动.bat

`run.py` 会把本目录加入 `sys.path` 最前端，再执行
`from idlelib.pyshell import main; main()`，等价于官方 `python -m idlelib`，
但源码来自示例文件夹内部。
