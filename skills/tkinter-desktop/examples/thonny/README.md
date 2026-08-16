# Thonny（完整源码示例）

本目录包含 **Thonny IDE 的完整源码**（取自官方 PyPI 发布的 `thonny-5.0.0`
wheel 中的 `thonny/` 包，**未做任何改动**），用于展示一个真实、复杂的
Python/Tkinter 桌面软件是如何组织与生产化的。

- `thonny/` —— Thonny 官方完整源码包（843 个文件，含 `workbench.py`、
  `running.py`、`plugins/`、`res/`、`locale/` 等）。
- `run.py` / `启动.bat` —— 启动入口，**指向本目录内的本地源码**，而非系统
  Python 中安装的 thonny 库。
- `requirements.txt` —— Thonny 的运行期依赖（官方元数据）。

## 运行方式

先安装运行期依赖（只需一次）：

    pip install -r requirements.txt

然后启动（任选其一）：

    python run.py
    # 或双击 启动.bat

`run.py` 会把本目录加入 `sys.path` 最前端，再执行
`from thonny import launch; launch()`，等价于官方 `python -m thonny`，
但源码来自示例文件夹内部。
