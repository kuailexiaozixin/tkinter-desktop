# -*- coding: utf-8 -*-
"""
启动本示例目录中「本地源码」里的 Thonny。

本脚本运行的是本示例 `thonny/` 子目录下随附的 thonny 源码包，
而不是系统 Python / site-packages 中通过 pip 安装的 thonny。
我们把本目录插到 sys.path 最前面，确保本地源码始终优先被导入。

等价于官方 `python -m thonny`，但源码取自示例文件夹内部。
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

from thonny import launch

if __name__ == "__main__":
    launch()
