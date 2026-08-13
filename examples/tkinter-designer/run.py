# -*- coding: utf-8 -*-
"""
run.py — Tkinter-Designer 一键启动脚本（本技能示例用）。

职责：
  1) 确保开发依赖已安装（见 requirements.txt：jinja2 / Pillow / requests / urllib3）；
     若缺失，自动用国内镜像安装，不转手给用户。
  2) 启动 Tkinter-Designer 自带 GUI（gui/gui.py）。

用法：
  直接双击同目录 启动.bat，或 `python run.py`
"""
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def _need(mod: str) -> bool:
    try:
        __import__(mod)
        return False
    except Exception:
        return True


def ensure_deps() -> None:
    """缺失依赖时自动安装（国内镜像）。"""
    required = [("jinja2", "jinja2"), ("PIL", "Pillow"),
                ("requests", "requests"), ("urllib3", "urllib3")]
    missing = [pip for mod, pip in required if _need(mod)]
    if not missing:
        return
    req = HERE / "requirements.txt"
    print(f"[run.py] 检测到缺失依赖：{missing}，尝试自动安装（国内镜像）...")
    if not req.exists():
        print("[run.py] 未找到 requirements.txt，请手动安装后再运行。")
        raise SystemExit(1)
    try:
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "-i",
            "https://pypi.tuna.tsinghua.edu.cn/simple", "-r", str(req),
        ])
    except subprocess.CalledProcessError as e:
        print(f"[run.py] 依赖安装失败：{e}")
        raise SystemExit(1)


def main() -> int:
    ensure_deps()
    gui = HERE / "gui" / "gui.py"
    if not gui.exists():
        print("[run.py] 未找到 gui/gui.py")
        return 1
    # 用全新子进程运行 GUI（cwd=本目录，tkdesigner 包路径由 gui.py 自行插入）
    return subprocess.call([sys.executable, str(gui)], cwd=str(HERE))


if __name__ == "__main__":
    raise SystemExit(main())
