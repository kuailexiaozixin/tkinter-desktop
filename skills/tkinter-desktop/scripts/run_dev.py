# -*- coding: utf-8 -*-
"""tkinter-desktop 一键开发启动脚本。

用途：在开发过程中快速验证项目状态，覆盖：
  ① 语法检查（py_compile 所有 .py）
  ② 导入验证（所有模块可 import）
  ③ pytest（Model 层测试）
  ④ 无头 GUI 冒烟（控件级验证）
  ⑤ 汇总报告

用法：
  python scripts/run_dev.py              # 全量检查
  python scripts/run_dev.py --run        # 检查通过后直接启动 GUI
  python scripts/run_dev.py --fast       # 快速模式（仅语法+导入）
  python scripts/run_dev.py --gate       # 完整发布门禁（含文档检查）

退出码：
  0 = 全部通过
  1 = 有失败

设计原则（workflow ⑦ 优化）：
  "先跑通再打包"——本脚本驱动 test/debug/check/verify/bugfix 循环，
  确认零错误、可交付后，才进入 workflow ⑧ PyInstaller 打包。
"""
from __future__ import annotations

import argparse
import os
import py_compile
import sys
import subprocess
import time
from pathlib import Path


# ── 配置 ────────────────────────────────────────────────────────
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent


def color(text: str, code: str) -> str:
    """终端彩色输出。"""
    return f"\033[{code}m{text}\033[0m"


# ═══════════════════════════════════════════════════════════════════
# 检查步骤
# ═══════════════════════════════════════════════════════════════════

def step_syntax() -> dict:
    """Step 1: py_compile 语法检查所有 .py 文件。"""
    print(f"\n{'='*60}")
    print(color("① 语法检查 (py_compile)", "33"))
    print(f"{'='*60}")

    errors = []
    checked = 0
    skip_dirs = {"__pycache__", ".git", "venv", ".venv", "node_modules",
                 ".workbuddy", "build", "dist", ".mypy_cache"}

    for py_file in PROJECT_ROOT.rglob("*.py"):
        rel = py_file.relative_to(PROJECT_ROOT)
        if any(s in rel.parts for s in skip_dirs):
            continue
        checked += 1
        try:
            py_compile.compile(str(py_file), doraise=True)
        except py_compile.PyCompileError as e:
            errors.append(str(rel))

    if errors:
        print(color(f"  ✗ {len(errors)} 个文件有语法错误:", "31"))
        for e in errors[:20]:
            print(f"     {e}")
        if len(errors) > 20:
            print(f"     ... 还有 {len(errors)-20} 个")
        return {"name": "syntax", "status": "FAIL",
                "detail": f"{len(errors)}/{checked} 失败"}
    else:
        print(color(f"  ✓ {checked} 个文件语法正确", "32"))
        return {"name": "syntax", "status": "PASS",
                "detail": f"{checked} files OK"}


def step_imports() -> dict:
    """Step 2: 验证关键模块可导入。"""
    print(f"\n{'='*60}")
    print(color("② 导入验证 (import check)", "33"))
    print(f"{'='*60}")

    # 尝试导入项目主包/入口
    modules_to_try = []
    # 自动发现顶层包
    for p in PROJECT_ROOT.iterdir():
        if p.is_dir() and (p / "__init__.py").exists():
            modules_to_try.append(p.name)
        elif p.suffix == ".py" and p.name != "run_dev.py":
            modules_to_try.append(p.stem)

    failures = []
    for mod_name in modules_to_try:
        try:
            r = subprocess.run(
                [sys.executable, "-c",
                 f"import sys; sys.path.insert(0, {str(PROJECT_ROOT)!r}); "
                 f"__import__({mod_name!r})"],
                capture_output=True, text=True, timeout=10,
                cwd=PROJECT_ROOT
            )
            if r.returncode != 0:
                err = (r.stderr or r.stdout).strip()[:100]
                failures.append(f"{mod_name}: {err}")
        except Exception as e:
            failures.append(f"{mod_name}: {e}")

    if failures:
        print(color(f"  ✗ {len(failures)} 个模块导入失败:", "31"))
        for f in failures[:10]:
            print(f"     {f}")
        return {"name": "imports", "status": "FAIL",
                "detail": f"{len(failures)} 失败"}
    else:
        checked = len(modules_to_try)
        print(color(f"  ✓ {checked} 个模块导入成功", "32"))
        return {"name": "imports", "status": "PASS",
                "detail": f"{checked} modules OK"}


def step_pytest() -> dict:
    """Step 3: pytest 单元测试。"""
    print(f"\n{'='*60}")
    print(color("③ 单元测试 (pytest)", "33"))
    print(f"{'='*60}")

    tests_dir = PROJECT_ROOT / "tests"
    if not tests_dir.exists():
        print(color("  ⊘ tests/ 目录不存在，跳过", "90"))
        return {"name": "pytest", "status": "SKIPPED"}

    result = subprocess.run(
        [sys.executable, "-m", "pytest", "-q", "--tb=line", str(tests_dir)],
        capture_output=True, text=True, timeout=120,
        cwd=PROJECT_ROOT
    )
    output = result.stdout.strip()
    # 只显示最后几行摘要
    lines = output.splitlines()
    summary = "\n".join(lines[-5:]) if len(lines) > 5 else output

    if result.returncode == 0:
        print(color(f"  ✓ pytest 全绿", "32"))
        print(f"     {summary}")
        return {"name": "pytest", "status": "PASS", "detail": summary}
    else:
        print(color(f"  ✗ pytest 有失败", "31"))
        print(f"     {summary}")
        return {"name": "pytest", "status": "FAIL", "detail": summary}


def step_smoke() -> dict:
    """Step 4: 无头 GUI 冒烟测试。"""
    print(f"\n{'='*60}")
    print(color("④ GUI 冒烟 (smoke_test_gui)", "33"))
    print(f"{'='*60}")

    smoke_script = PROJECT_ROOT / "scripts" / "smoke_test_gui.py"
    if not smoke_script.exists():
        print(color("  ⊘ smoke_test_gui.py 不存在（请先创建并覆写 build_app()）", "90"))
        return {"name": "smoke", "status": "SKIPPED"}

    result = subprocess.run(
        [sys.executable, str(smoke_script)],
        capture_output=True, text=True, timeout=60,
        cwd=PROJECT_ROOT
    )
    output = (result.stdout + result.stderr).strip()

    if result.returncode == 0:
        print(color(f"  ✓ GUI 冒烟通过", "32"))
        # 提取 SMOKE OK 行
        for line in output.splitlines():
            if "SMOKE OK" in line or "PASSED" in line:
                print(f"     {line}")
        return {"name": "smoke", "status": "PASS", "detail": output[-200:]}
    else:
        print(color(f"  ✗ GUI 冒烟失败", "31"))
        for line in output.splitlines():
            if "FAIL" in line or "EXCEPTION" in line or "Error" in line:
                print(f"     {line}")
        return {"name": "smoke", "status": "FAIL", "detail": output[-300:]}


# ═══════════════════════════════════════════════════════════════════
# 主流程
# ═══════════════════════════════════════════════════════════════════

def run_checks(fast: bool = False, run_app: bool = False,
                gate: bool = False) -> int:
    """执行检查步骤并返回退出码。"""
    t0 = time.time()

    print(color("\n╔══════════════════════════════════════════╗", "36"))
    print(color("║   tkinter-desktop 开发验证工具           ║", "36"))
    print(color(f"║   项目: {PROJECT_ROOT.name:<28} ║", "36"))
    print(color("╚══════════════════════════════════════════╝", "36"))

    steps = []
    if gate:
        # 完整门禁模式：调用 release_gate.py
        result = subprocess.run(
            [sys.executable, str(SCRIPT_DIR / "release_gate.py"),
             "--root", str(PROJECT_ROOT)],
            capture_output=True, text=True, timeout=180,
            cwd=PROJECT_ROOT
        )
        print(result.stdout)
        if result.stderr:
            print(result.stderr)
        return result.returncode

    # 标准模式 / 快速模式
    steps.append(step_syntax())
    steps.append(step_imports())

    if not fast:
        steps.append(step_pytest())
        steps.append(step_smoke())

    # ── 汇总 ───────────────────────────────────────────────
    elapsed = time.time() - t0
    passed = sum(1 for s in steps if s["status"] == "PASS")
    failed = sum(1 for s in steps if s["status"] == "FAIL")
    skipped = sum(1 for s in steps if s["status"] == "SKIPPED")

    print(f"\n{'='*60}")
    print(color(f"汇总: {passed} 通过 | {failed} 失败 | {skipped} 跳过 | 耗时 {elapsed:.1f}s",
               "36" if failed == 0 else "31"))
    print(f"{'='*60}")

    if failed > 0:
        print(color("\n⚠ 有失败项，修复后重新运行 python scripts/run_dev.py", "33"))
        for s in steps:
            if s["status"] == "FAIL":
                print(f"  ✗ [{s['name']}] {s.get('detail', '')[:100]}")
        return 1

    # 全部通过 → 可选启动 GUI
    if run_app:
        print(color("\n✓ 全部通过，正在启动应用...", "32"))
        launch_app()
    else:
        print(color("\n✓ 全部通过！可以进入下一步（打包 EXE 或继续开发）。", "32"))
        print(f"   完整门禁: python scripts/release_gate.py")
        print(f"   启动应用: python scripts/run_dev.py --run")

    return 0


def launch_app():
    """尝试发现并启动应用的主入口。"""
    # 常见入口文件名
    candidates = [
        PROJECT_ROOT / "launcher.py",
        PROJECT_ROOT / "main.py",
        PROJECT_ROOT / "app.py",
    ]
    for candidate in candidates:
        if candidate.exists():
            print(f"   启动: {candidate.relative_to(PROJECT_ROOT)}")
            os.chdir(candidate.parent)
            os.execv(sys.executable, [sys.executable, str(candidate)])

    print("  未找到入口文件，请手动运行你的应用启动脚本")
    print(f"  当前目录: {PROJECT_ROOT}")


def main():
    parser = argparse.ArgumentParser(description="tkinter-desktop 一键开发验证")
    parser.add_argument("--fast", action="store_true",
                        help="快速模式：仅语法+导入检查")
    parser.add_argument("--run", action="store_true",
                        help="检查通过后自动启动 GUI 应用")
    parser.add_argument("--gate", action="store_true",
                        help="完整发布门禁模式（等同 release_gate.py）")
    args = parser.parse_args()

    raise SystemExit(run_checks(fast=args.fast, run_app=args.run, gate=args.gate))


if __name__ == "__main__":
    main()
