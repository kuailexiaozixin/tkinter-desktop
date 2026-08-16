"""Pygubu Designer 启动引导脚本 —— 指向本目录 vendored 源码，而非 pip 安装的官方包。

设计原则
--------
- 本文件只做「启动引导」，不修改 pygubudesigner 应用源码（源码保持与上游逐字节一致）。
- 把本文件所在目录插入 sys.path 最前，保证 `import pygubudesigner` 命中的是
  本目录里的 pygubudesigner/ 源码，而不是你 pip 装的那个同名包。
- Windows 下在导入 tkinter 之前把进程设为 DPI 感知，使字体按真实屏幕 DPI 渲染
  （与官方打包的 .exe 表现一致，不再因控制台子系统默认 96 DPI 而偏小）。
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

# --- 关键：pygubu 的 PropertyRegistry 单例在「首次 import pygubu 时」就创建，
# 且只有当 PYGUBU_DESIGNER_RUNNING 环境变量已存在时才会启用「真实（带信号）」实现；
# 否则退回 PropertyRegistryDummy，它会静默丢弃所有 register() 调用（包括 'class'/'id'），
# 导致设计器启动即 KeyError。必须在 import pygubu 之前就置好这个变量。
os.environ.setdefault("PYGUBU_DESIGNER_RUNNING", "Y")

# --- pygubu 0.40 / 0.41 不在包上暴露 __version__ 属性，但 pygubu-designer 0.41.4
# 会在启动横幅（main.py）和「关于」对话框（aboutdialog.py）里读取 pygubu.__version__，
# 缺失会直接 AttributeError 崩溃。这里从包元数据把版本号补到模块对象上，
# 既不修改上游 vendored 源码，又能让设计器正常启动。
import pygubu
if not hasattr(pygubu, "__version__"):
    try:
        import importlib.metadata as _md
        pygubu.__version__ = _md.version("pygubu")
    except Exception:
        pygubu.__version__ = "0.41"

if sys.platform == "win32":
    import ctypes
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(1)  # SYSTEM_DPI_AWARE
    except Exception:
        try:
            ctypes.windll.user32.SetProcessDPIAware()
        except Exception:
            pass

from pygubudesigner.main import start_pygubu

if __name__ == "__main__":
    start_pygubu()
