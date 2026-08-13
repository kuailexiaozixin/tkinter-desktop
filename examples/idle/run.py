# -*- coding: utf-8 -*-
"""
启动本示例目录中「本地源码」里的 IDLE。

本脚本运行的是本示例 `idlelib/` 子目录下随附的 idlelib 源码包，
而不是系统 Python 自带的 idlelib。
我们把本目录插到 sys.path 最前面，确保本地源码始终优先被导入。

等价于官方 `python -m idlelib`，但源码取自示例文件夹内部。
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

from idlelib.pyshell import main

if __name__ == "__main__":
    main()
