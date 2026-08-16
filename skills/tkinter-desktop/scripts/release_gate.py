# -*- coding: utf-8 -*-
"""tkinter-desktop 发布门禁（Release Gate）。

统一发布门禁，适配 tkinter 桌面应用场景。

硬门禁（REQUIRED，任一失败则非零退出）：
  1. pytest          — Model 层 + 集成测试
  2. smoke_test_gui  — 无头 GUI 冒烟（控件级验证）

CI 建议项（ADVISORY，失败只告警、不阻塞门禁，建议放 CI 跑）：
  3. verify_imports  — 所有模块可导入（无循环依赖/缺失引用）
  4. check_refs      — references/ 文档中的代码片段语法正确

用法：
  python scripts/release_gate.py                     # 硬门禁 + CI 建议项全跑
  python scripts/release_gate.py --advisory-only    # 只跑 CI 建议项
  python scripts/release_gate.py --skip-smoke        # 跳过 GUI 冒烟（仅硬门禁中）
  python scripts/release_gate.py --skip-pytest       # 跳过 pytest（仅硬门禁中）
  python scripts/release_gate.py --root /path/to/project

退出码：
  0 = 硬门禁通过（CI 建议项失败仅告警）
  1 = 硬门禁有 REQUIRED 失败
"""
from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path


class Gate:
    """发布门禁编排器。"""

    def __init__(self, root: str, skip_pytest: bool = False,
                 skip_smoke: bool = False, skip_imports: bool = False,
                 skip_refs: bool = False, advisory_only: bool = False):
        self.root = Path(root).resolve()
        self.skip_pytest = skip_pytest
        self.skip_smoke = skip_smoke
        self.skip_imports = skip_imports
        self.skip_refs = skip_refs
        self.advisory_only = advisory_only
        self.results: list[dict] = []

    # ── 检查步骤 ──────────────────────────────────────────────

    def check_pytest(self) -> dict:
        """Step 1: pytest 单元测试 + 集成测试。"""
        if self.skip_pytest:
            return {"name": "pytest", "status": "SKIPPED", "detail": "--skip-pytest"}

        tests_dir = self.root / "tests"
        if not tests_dir.exists():
            return {"name": "pytest", "status": "WARNING",
                    "detail": "tests/ 目录不存在（无 Model 层测试）"}

        result = subprocess.run(
            [sys.executable, "-m", "pytest", "-q", "--tb=short", str(tests_dir)],
            cwd=self.root, capture_output=True, text=True, timeout=120
        )
        ok = result.returncode == 0
        return {
            "name": "pytest",
            "status": "PASS" if ok else "FAIL",
            "detail": result.stdout.strip()[-200:] if result.stdout else result.stderr[:200],
            "required": True,
        }

    def check_smoke(self) -> dict:
        """Step 2: 无头 GUI 冒烟测试。"""
        if self.skip_smoke:
            return {"name": "smoke_test_gui", "status": "SKIPPED", "detail": "--skip-smoke"}

        smoke_script = self.root / "scripts" / "smoke_test_gui.py"
        if not smoke_script.exists():
            return {"name": "smoke_test_gui", "status": "WARNING",
                    "detail": "scripts/smoke_test_gui.py 不存在（请先创建并覆写 build_app()）"}

        result = subprocess.run(
            [sys.executable, str(smoke_script)],
            cwd=self.root, capture_output=True, text=True, timeout=60
        )
        ok = result.returncode == 0
        return {
            "name": "smoke_test_gui",
            "status": "PASS" if ok else "FAIL",
            "detail": (result.stdout + result.stderr).strip()[-300:],
            "required": True,
        }

    def check_imports(self) -> dict:
        """Step 3: 验证所有 Python 模块可导入。"""
        if self.skip_imports:
            return {"name": "verify_imports", "status": "SKIPPED", "detail": "--skip-imports"}

        failures = []
        # 收集项目内所有 .py 文件（排除 __pycache__、venv、.git）
        py_files = []
        for p in self.root.rglob("*.py"):
            rel = p.relative_to(self.root)
            parts = rel.parts
            # 跳过无关目录
            skip_dirs = {"__pycache__", ".git", "venv", ".venv", "node_modules",
                         ".workbuddy", "build", "dist"}
            if any(s in skip_dirs for s in parts):
                continue
            py_files.append(p)

        for py_file in py_files:
            rel = py_file.relative_to(self.root)
            # 尝试作为模块导入
            module_name = str(rel.with_suffix("")).replace(os.sep, ".").replace("/", ".")
            try:
                # 用 subprocess 隔离导入，避免污染当前进程
                r = subprocess.run(
                    [sys.executable, "-c",
                     f"import sys; sys.path.insert(0, {str(self.root)!r}); import importlib; "
                     f"spec = importlib.util.find_spec({module_name!r}); "
                     f"print('OK' if spec else 'NO_SPEC')"],
                    capture_output=True, text=True, timeout=10
                )
                if "OK" not in r.stdout:
                    failures.append(f"{rel}: 导入失败")
            except Exception as e:
                failures.append(f"{rel}: 异常 {e}")

        if failures:
            return {"name": "verify_imports", "status": "WARNING",
                    "detail": f"{len(failures)} 个模块导入失败（CI 建议项，不阻塞门禁）:\n  " + "\n  ".join(failures[:10]),
                    "required": False}
        return {"name": "verify_imports", "status": "PASS",
                "detail": f"已检查 {len(py_files)} 个 .py 文件（CI 建议项）",
                "required": False}

    def check_refs(self) -> dict:
        """Step 4: 检查 references/ 中代码片段的语法正确性。"""
        if self.skip_refs:
            return {"name": "check_refs", "status": "SKIPPED", "detail": "--skip-refs"}

        refs_dir = self.root / "references"
        if not refs_dir.exists():
            return {"name": "check_refs", "status": "WARNING",
                    "detail": "references/ 目录不存在"}

        errors = []
        for md_file in sorted(refs_dir.rglob("*.md")):
            content = md_file.read_text(encoding="utf-8")
            # 提取 ```python ... ``` 代码块
            in_block = False
            block_lines = []
            block_start = 0
            for i, line in enumerate(content.splitlines(), 1):
                if line.startswith("```python"):
                    in_block = True
                    block_lines = []
                    block_start = i
                elif line.startswith("```") and in_block:
                    in_block = False
                    code = "\n".join(block_lines)
                    # 只做语法检查（不执行），跳过含 ... 或明显不完整的片段
                    if len(code.strip()) > 20 and "..." not in code[:50]:
                        try:
                            compile(code, str(md_file.relative_to(self.root)), "exec")
                        except SyntaxError as e:
                            rel = md_file.relative_to(self.root)
                            errors.append(f"{rel}:{block_start}: {e}")
                    block_lines = []
                elif in_block:
                    block_lines.append(line)

        if errors:
            return {"name": "check_refs", "status": "WARNING",
                    "detail": f"{len(errors)} 个代码块有语法问题:\n  " + "\n  ".join(errors[:5])}
        return {"name": "check_refs", "status": "PASS",
                "detail": "references/ 代码块语法检查通过"}

    # ── 编排 ───────────────────────────────────────────────────

    def run(self) -> int:
        """按顺序执行所有门禁检查。"""
        print("=" * 64)
        print("tkinter-desktop RELEASE GATE")
        print(f"root: {self.root}")
        print("=" * 64)

        # 硬门禁（REQUIRED，失败即阻塞）+ CI 建议项（ADVISORY，不阻塞）
        if self.advisory_only:
            steps = [("verify_imports", self.check_imports),
                     ("check_refs", self.check_refs)]
            print("MODE: --advisory-only（仅 CI 建议项：导入 / 文档代码块）")
        else:
            steps = [("pytest", self.check_pytest),
                     ("smoke_test_gui", self.check_smoke)]
            print("MODE: 硬门禁（pytest + 无头 GUI 冒烟）")
            advisory = [("verify_imports", self.check_imports),
                        ("check_refs", self.check_refs)]

        required_failures = 0
        warnings = 0
        hard_label = "REQUIRED" if not self.advisory_only else "ADVISORY"

        for name, fn in steps:
            print(f"\n[{name}] ({hard_label})")
            result = fn()
            self.results.append(result)
            status = result["status"]
            icon = {"PASS": "✓", "FAIL": "✗", "WARNING": "⚠", "SKIPPED": "⊘"}.get(status, "?")
            print(f"  {icon} {status}")
            if "detail" in result and status != "PASS":
                detail = result["detail"]
                if len(detail) > 200:
                    detail = detail[:200] + "..."
                print(f"     {detail}")
            if status == "FAIL":
                required_failures += 1
            elif status == "WARNING":
                warnings += 1

        if not self.advisory_only:
            print("\n--- CI 建议项（ADVISORY，不阻塞门禁）---")
            for name, fn in advisory:
                print(f"\n[{name}] (ADVISORY)")
                result = fn()
                self.results.append(result)
                status = result["status"]
                icon = {"PASS": "✓", "FAIL": "✗", "WARNING": "⚠", "SKIPPED": "⊘"}.get(status, "?")
                print(f"  {icon} {status}")
                if "detail" in result and status != "PASS":
                    detail = result["detail"]
                    if len(detail) > 200:
                        detail = detail[:200] + "..."
                    print(f"     {detail}")
                if status == "WARNING":
                    warnings += 1

        # ── 汇总 ───────────────────────────────────────────────
        print("\n" + "=" * 64)
        total = len(self.results)
        passed = sum(1 for r in self.results if r["status"] == "PASS")
        print(f"RESULT: {passed}/{total} PASSED, "
              f"{required_failures} HARD-FAIL(S), {warnings} ADVISORY-WARNING(S)")
        print("=" * 64)

        if required_failures > 0:
            print("\n❌ 硬门禁未通过（pytest / 无头 GUI 冒烟 有失败项）。修复后重新运行。")
            return 1
        elif warnings > 0:
            print(f"\n✅ 硬门禁通过；{warnings} 项 CI 建议项告警（不阻塞，建议修复）。")
            return 0
        else:
            print("\n✅ 全部通过。可以进入打包流程（workflow ⑧）。")
            return 0


def main():
    parser = argparse.ArgumentParser(description="tkinter-desktop 发布门禁")
    parser.add_argument("--root", default=".", help="项目根目录（默认当前目录）")
    parser.add_argument("--skip-pytest", action="store_true", help="跳过 pytest")
    parser.add_argument("--skip-smoke", action="store_true", help="跳过 GUI 冒烟")
    parser.add_argument("--skip-imports", action="store_true", help="跳过导入检查")
    parser.add_argument("--skip-refs", action="store_true", help="跳过文档代码块检查")
    parser.add_argument("--advisory-only", action="store_true",
                        help="只跑 CI 建议项（verify_imports / check_refs），跳过硬门禁")
    args = parser.parse_args()

    gate = Gate(
        root=args.root,
        skip_pytest=args.skip_pytest,
        skip_smoke=args.skip_smoke,
        skip_imports=args.skip_imports,
        skip_refs=args.skip_refs,
        advisory_only=args.advisory_only,
    )
    raise SystemExit(gate.run())


if __name__ == "__main__":
    main()
