# -*- coding: utf-8 -*-
"""通用无头 GUI 冒烟测试模板。

用法：
  1. 复制本文件到你的项目 scripts/ 目录
  2. 修改 `build_app()` 函数，返回你的 App 实例
  3. 在 `test_*` 方法中添加项目特定的断言
  4. 运行：python scripts/smoke_test_gui.py

退出码 0 = 全部通过；非零 = 有失败项。

设计原则（本技能 TDD 门禁）：
  - Red-Green-Refactor：先写失败断言 → 实现功能 → 重构
  - Prove-It：bug 修复前先写复现测试
  - 无头验证：withdraw + update + assert，不弹窗
"""
from __future__ import annotations

import sys
import os

# ── 项目根目录加入 sys.path ──────────────────────────────────────
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_PROJECT_ROOT = os.path.dirname(_SCRIPT_DIR)
if _PROJECT_ROOT not in sys.path:
    sys.path.insert(0, _PROJECT_ROOT)


def build_app():
    """【必须覆写】构建并返回 App 实例，不进入 mainloop。

    返回值要求：
      - 必须有 .destroy() 方法（tkinter.Tk 或其子类）
      - 建议提供 .notebook / .tree / .status_label 等常用属性供断言
    """
    # ---- 示例：你的项目（按需替换）----
    # from views.main_view import MainView
    # root = tk.Tk()
    # root.withdraw()
    # app = MainView(root)
    # return app  # 或 return root

    raise NotImplementedError(
        "请覆写 build_app() 返回你的 App 实例。"
        "\n可参考 examples/inventory-manager/ 或 idle/ 的启动方式套用。"
    )


# ═══════════════════════════════════════════════════════════════════
# 通用断言工具
# ═══════════════════════════════════════════════════════════════════

class SmokeTest:
    """无头 GUI 冒烟测试框架。"""

    def __init__(self, app):
        self.app = app
        self.failures: list[str] = []

    def check(self, condition: bool, message: str) -> None:
        """记录一个检查点。condition=False 时记录失败但不中断。"""
        if not condition:
            self.failures.append(message)
            print(f"  FAIL: {message}")
        else:
            print(f"  OK:   {message}")

    def check_widget_exists(self, widget, name: str = "") -> None:
        """断言控件存在且尺寸合理（非零且非负）。"""
        exists = widget is not None
        if exists:
            try:
                w = widget.winfo_width()
                h = widget.winfo_height()
                reasonable = w > 0 and h > 0
                self.check(reasonable,
                           f"{name or widget.winfo_class()} 存在且尺寸合理 ({w}x{h})")
                return
            except Exception:
                pass
        self.check(False, f"{name or '?'} 控件不存在或无法查询")

    def check_treeview_rows(self, tree, min_count: int = 0, name: str = "Treeview") -> None:
        """断言 Treeview 行数 >= min_count。"""
        rows = len(tree.get_children()) if tree else 0
        self.check(rows >= min_count,
                   f"{name} 行数={rows} (期望 >= {min_count})")

    def run(self) -> int:
        """执行全部测试，返回退出码。"""
        print("=" * 60)
        print("SMOKE TEST: 无头 GUI 冒烟")
        print("=" * 60)

        try:
            self.app.withdraw()           # 关键：不显示窗口
            self.app.update_idletasks()   # 强制完成布局
            self.app.update()             # 泵一轮事件

            # ── 通用检查点（可覆写/扩展）──
            self.test_window_created()
            self.test_layout_complete()
            # 项目特定检查点（覆写此方法添加）
            self.test_project_specific()

        except Exception as e:
            self.failures.append(f"异常: {e}")
            print(f"  EXCEPTION: {e}")
        finally:
            try:
                self.app.destroy()
            except Exception:
                pass

        print("-" * 60)
        if self.failures:
            print(f"RESULT: {len(self.failures)} FAILURE(S)")
            for f in self.failures:
                print(f"  ✗ {f}")
            return 1
        print("RESULT: ALL PASSED")
        return 0

    # ── 可覆写的测试方法 ────────────────────────────────────────

    def test_window_created(self) -> None:
        """检查窗口已创建。"""
        self.check(self.app is not None, "App 实例已创建")

    def test_layout_complete(self) -> None:
        """检查布局已完成（窗口有合理尺寸）。"""
        try:
            w = self.app.winfo_width()
            h = self.app.winfo_height()
            self.check(w > 0 and h > 0,
                       f"布局完成: 窗口尺寸 {w}x{h}")
        except Exception as e:
            self.check(False, f"布局检查异常: {e}")

    def test_project_specific(self) -> None:
        """【覆写】添加项目特定的冒烟断言。

        示例：
            self.check_widget_exists(getattr(self.app, 'notebook', None), 'Notebook')
            self.check_treeview_rows(getattr(self.app, 'tree', None), min_count=3)
            self.check('Ready' in getattr(self.app, 'status_label', type('', (), {'cget': lambda s, k: ''}))().cget('text'),
                       '状态栏包含 Ready')
        """
        pass


# ═══════════════════════════════════════════════════════════════════
# 主入口
# ═══════════════════════════════════════════════════════════════════

def main() -> int:
    app = build_app()
    tester = SmokeTest(app)
    return tester.run()


if __name__ == "__main__":
    raise SystemExit(main())
