# -*- coding: utf-8 -*-
"""check_ui_visual.py —— .ui 可视化校验：真渲染 + 截图 + 几何检查。

与 check_ui.py 的分工
    check_ui.py        无头，查「语义」：列数为 0、页签为 0、anchor 非法、回调声明……
    check_ui_visual.py 真渲染，查「视觉」：控件零尺寸、子控件超出父容器（被裁切），
                       并产出 PNG 供人工或多模态 AI 按图复核（文字截断、错位、
                       中文乱码这类问题只能看图发现）。
    两者互补，建议都跑。

用法
    python check_ui_visual.py                  # 渲染同目录下所有 *.ui
    python check_ui_visual.py app.ui [b.ui]    # 渲染指定文件
输出
    与 .ui 同目录、同名的 <名字>_preview.png
退出码：0 = 无几何告警；1 = 有几何告警或渲染失败。

前置：pip install pygubu pillow
注意：本脚本会真的把窗口显示出来（截图需要），不能在无桌面会话里跑。
"""
import glob
import os
import sys
import tkinter as tk

import pygubu
from PIL import ImageGrab

HERE = os.path.dirname(os.path.abspath(__file__))

# 容差：Tk 的边框/内边距会让子控件比父容器"超出"1~2 像素，属正常
TOLERANCE = 2


class _CallbackStub:
    """渲染用的占位回调对象。

    警告：**不要**用这种带 __getattr__ 的 stub 去审计回调完整性 ——
    pygubu 会认为每个回调都已连上、connect_callbacks 返回 None，
    从而永远查不出 controller 少写了哪个方法。
    审计回调请用 check_ui.py（它传空 dict，让 pygubu 吐出全部声明的回调名）。
    """

    def __getattr__(self, _name):
        def _cb(*_a, **_k):
            return None

        return _cb


def _collect_geometry(widget, issues, depth=0):
    """递归检查：零尺寸 + 子控件超出父容器可视范围。"""
    try:
        w, h = widget.winfo_width(), widget.winfo_height()
        cls = widget.winfo_class()
        name = getattr(widget, "_name", "?")
    except Exception:
        return

    if w <= 1 or h <= 1:
        issues.append(f"[零尺寸] {'  ' * depth}{cls}({name}) {w}x{h}")

    try:
        px, py = widget.winfo_rootx(), widget.winfo_rooty()
    except Exception:
        px = py = None

    for child in widget.winfo_children():
        if px is not None:
            try:
                cx, cy = child.winfo_rootx(), child.winfo_rooty()
                cw, ch = child.winfo_width(), child.winfo_height()
                if (cx + cw > px + w + TOLERANCE) or (cy + ch > py + h + TOLERANCE) \
                        or (cx < px - TOLERANCE) or (cy < py - TOLERANCE):
                    issues.append(
                        f"[超出父容器] {'  ' * depth}"
                        f"{child.winfo_class()}({getattr(child, '_name', '?')}) "
                        f"位于 ({cx},{cy},{cw}x{ch})，父 {cls}({name}) "
                        f"仅 ({px},{py},{w}x{h}) → 可能被裁切"
                    )
            except Exception:
                pass
        _collect_geometry(child, issues, depth + 1)


def render_one(path) -> bool:
    print(f"\n=== {path} ===")
    root = tk.Tk()
    root.withdraw()
    ok = True
    try:
        builder = pygubu.Builder()
        builder.add_from_file(path)

        tops = [w.identifier for w in builder.uidefinition.widgets()]
        if not tops:
            print("FAIL: .ui 中没有顶层对象")
            return False
        top_id = tops[0]
        if len(tops) > 1:
            print(f"提示：存在多个顶层对象 {tops}，本次渲染第一个 {top_id!r}")

        target = builder.get_object(top_id, root)
        builder.connect_callbacks(_CallbackStub())

        # 顶层可能是 Toplevel，也可能是挂在 root 下的 Frame
        window = target if isinstance(target, (tk.Toplevel, tk.Tk)) else root
        if window is root:
            root.deiconify()
        else:
            window.deiconify()
        window.lift()
        window.attributes("-topmost", True)
        root.update_idletasks()
        root.update()
        root.after(300)
        root.update()
        window.attributes("-topmost", False)

        issues = []
        _collect_geometry(target, issues)

        bx, by = window.winfo_rootx(), window.winfo_rooty()
        bw, bh = window.winfo_width(), window.winfo_height()
        img = ImageGrab.grab(bbox=(bx, by, bx + bw, by + bh))
        out = os.path.splitext(path)[0] + "_preview.png"
        img.save(out)
        print(f"SCREENSHOT: {out}  ({bw}x{bh})")

        if issues:
            ok = False
            print(f"GEOMETRY: 发现 {len(issues)} 处告警")
            for i in issues:
                print("   ", i)
        else:
            print("GEOMETRY: 无零尺寸 / 超出父容器 告警")
    except Exception as e:
        ok = False
        print(f"FAIL: 渲染失败 -> {type(e).__name__}: {e}")
    finally:
        try:
            root.destroy()
        except Exception:
            pass
    return ok


def main() -> int:
    args = sys.argv[1:]
    files = args or sorted(glob.glob(os.path.join(HERE, "*.ui")))
    if not files:
        print("没有找到任何 .ui 文件")
        return 1
    results = []
    for p in files:
        if not os.path.isfile(p):
            print(f"\n=== {p} ===\nFAIL: 文件不存在")
            results.append(False)
        else:
            results.append(render_one(p))
    print(f"\n汇总：{sum(results)}/{len(results)} 个 .ui 无视觉告警")
    return 0 if all(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
