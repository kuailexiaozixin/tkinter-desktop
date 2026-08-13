# -*- coding: utf-8 -*-
"""check_ui.py —— .ui 语义校验器（无头）。

为什么不能只「数控件个数」？
    早期版本只递归统计控件数量就报 OK，对下面这些**静默坏掉**的 UI 会给出假阳性
    （已在 pygubu 0.40.1 / Tk 8.6 上逐条实测）：

      1) ttk.Treeview 写 legacy ``<columns><column/></columns>``
         → pygubu 直接忽略，``tree["columns"] == []``，界面是一张全空白表格，**不报错**。
      2) ttk.Notebook 下直接挂 ttk.Frame（漏了 ttk.Notebook.Tab）
         → ``nb.tabs() == ()``，一个页签都没有，**不报错**。
      3) ttk.Treeview.Column 漏写 ``column_anchor``
         → 运行期 ``TclError: ambiguous anchor ""``（这个会崩，但要等到 build 才崩）。

    上述 1)、2) 是「静默失败」，人工看代码极难发现，正是本脚本存在的意义。

检查项一览
    XML 层（不依赖 Tk）：
      E  Treeview 使用 legacy <columns>
      E  Treeview 没有任何 ttk.Treeview.Column 子节点
      E  Column 缺 column_anchor（实测必崩）
      E  Notebook 的直接子节点不是 ttk.Notebook.Tab
      E  command 属性不是合法 JSON
      W  Column 缺 text（标题会回落成 id，界面上露出程序员标识符）
      W  Column 缺 heading_anchor（无害，默认 w；仅提示显式化）
    运行时层（真建控件）：
      E  Treeview 实际列数为 0
      E  Notebook 实际页数为 0
      I  列出 .ui 声明的全部回调名，供与 controller 比对

用法
    python check_ui.py                 # 校验脚本同目录下所有 *.ui
    python check_ui.py app.ui [b.ui]   # 校验指定文件
退出码：0 = 全部通过；1 = 存在 E 级问题。
"""
import glob
import json
import logging
import os
import sys
import tkinter as tk
import xml.etree.ElementTree as ET

import pygubu

HERE = os.path.dirname(os.path.abspath(__file__))

TREEVIEW = "ttk.Treeview"
TREE_COLUMN = "ttk.Treeview.Column"
NOTEBOOK = "ttk.Notebook"
NOTEBOOK_TAB = "ttk.Notebook.Tab"

# Tk 合法 anchor 值（实测报错信息里列出的全集）
VALID_ANCHORS = {"n", "ne", "e", "se", "s", "sw", "w", "nw", "center"}


# --------------------------------------------------------------------------
# XML 层
# --------------------------------------------------------------------------
def _direct_child_objects(obj):
    """取 <object> 的直接子 <object>（结构固定为 object/child/object）。"""
    return [c for c in obj.findall("child/object")]


def _prop(obj, name):
    """取 <property name="..."> 的文本；不存在返回 None。"""
    for p in obj.findall("property"):
        if p.get("name") == name:
            return (p.text or "").strip()
    return None


def _id_class_map(root):
    """构建 {id: class} 映射，供运行时层按 .ui 里的 id 定位控件。"""
    out = {}
    for obj in root.iter("object"):
        oid = obj.get("id")
        if oid:
            out[oid] = obj.get("class")
    return out


def _xml_checks(root, errors, warns):
    for obj in root.iter("object"):
        cls = obj.get("class")
        oid = obj.get("id") or "?"

        # ---- ttk.Treeview ----
        if cls == TREEVIEW:
            cols = [c for c in _direct_child_objects(obj)
                    if c.get("class") == TREE_COLUMN]
            if obj.find("columns") is not None:
                errors.append(
                    f"[{TREEVIEW}:{oid}] 使用了 legacy <columns> 语法，"
                    f"pygubu 0.40 会**静默忽略**它 → 实际 0 列（空白表格）。"
                    f"请改写成 <object class=\"{TREE_COLUMN}\"> 子节点。"
                )
            elif not cols:
                errors.append(
                    f"[{TREEVIEW}:{oid}] 没有任何 {TREE_COLUMN} 子节点 → 0 列空白表格。"
                )
            for col in cols:
                cid = col.get("id") or "?"
                anchor = _prop(col, "column_anchor")
                if not anchor:
                    errors.append(
                        f"[{TREEVIEW}:{oid} / Column:{cid}] 缺少 column_anchor。"
                        f"pygubu 默认值是空串，运行期必然抛 "
                        f"TclError: ambiguous anchor \"\"。请显式写 w / center / e。"
                    )
                elif anchor not in VALID_ANCHORS:
                    errors.append(
                        f"[{TREEVIEW}:{oid} / Column:{cid}] column_anchor=\"{anchor}\" 非法，"
                        f"合法值：{sorted(VALID_ANCHORS)}。"
                    )
                head_anchor = _prop(col, "heading_anchor")
                if head_anchor and head_anchor not in VALID_ANCHORS:
                    errors.append(
                        f"[{TREEVIEW}:{oid} / Column:{cid}] heading_anchor=\"{head_anchor}\" 非法。"
                    )
                elif not head_anchor:
                    warns.append(
                        f"[{TREEVIEW}:{oid} / Column:{cid}] 未写 heading_anchor"
                        f"（无害，默认 w；建议显式写明与 column_anchor 对齐）。"
                    )
                if not _prop(col, "text"):
                    warns.append(
                        f"[{TREEVIEW}:{oid} / Column:{cid}] 未写 text，"
                        f"列标题会回落成 id \"{cid}\"（界面上露出程序员标识符）。"
                    )

        # ---- ttk.Notebook ----
        elif cls == NOTEBOOK:
            kids = _direct_child_objects(obj)
            bad = [c for c in kids if c.get("class") != NOTEBOOK_TAB]
            if not kids:
                errors.append(f"[{NOTEBOOK}:{oid}] 没有任何子节点 → 0 个页签。")
            elif bad:
                names = ", ".join(f"{c.get('class')}#{c.get('id')}" for c in bad)
                errors.append(
                    f"[{NOTEBOOK}:{oid}] 直接子节点必须是 {NOTEBOOK_TAB}，"
                    f"但发现 {names} → 这些内容会**静默丢失**，页签数为 0。"
                    f"正确层级：{NOTEBOOK} > {NOTEBOOK_TAB} > ttk.Frame > 具体控件。"
                )

        # ---- command 必须是 JSON ----
        for p in obj.findall("property"):
            if p.get("name") not in ("command", "xscrollcommand", "yscrollcommand",
                                     "validatecommand", "invalidcommand",
                                     "postcommand", "tabchangedcommand"):
                continue
            raw = (p.text or "").strip()
            if not raw:
                continue
            try:
                json.loads(raw)
            except Exception:
                errors.append(
                    f"[{cls}:{oid}] 属性 {p.get('name')} 不是合法 JSON："
                    f"{raw!r} → 构建期抛 JSONDecodeError。"
                    f"正确写法：{{\"value\": \"on_xxx\", \"cbtype\": \"simple\"}}"
                )


# --------------------------------------------------------------------------
# 运行时层
# --------------------------------------------------------------------------
def _declared_callbacks(builder):
    """用「传空 dict」让 pygubu 吐出 .ui 声明的全部回调名。

    坑：若传一个带 __getattr__ 的 stub 对象，pygubu 会认为每个回调都已连上，
    返回 None，什么都查不出来。必须传空 dict。
    """
    logger = logging.getLogger("pygubu")
    old = logger.level
    logger.setLevel(logging.CRITICAL)  # 屏蔽 "Missing callbacks" 噪音
    try:
        return sorted(builder.connect_callbacks({}) or [])
    finally:
        logger.setLevel(old)


def _runtime_checks(path, id2class, errors, warns, stats):
    root = tk.Tk()
    root.withdraw()
    try:
        builder = pygubu.Builder()
        builder.add_from_file(path)

        tops = [w.identifier for w in builder.uidefinition.widgets()]
        if not tops:
            errors.append("`.ui` 中没有任何顶层对象。")
            return
        stats["tops"] = tops

        for top in tops:
            w = builder.get_object(top, root)
            if isinstance(w, tk.Toplevel):
                w.withdraw()  # 保持无头，不弹窗

        # 按 .ui 的 id 定位控件（比 widget._name 之类的内部名可读得多）
        for oid, bo in builder.objects.items():
            cls = id2class.get(oid)
            widget = getattr(bo, "widget", None)
            if widget is None:
                continue

            if cls == TREEVIEW:
                stats["treeview"] += 1
                cols = list(widget["columns"] or [])
                if not cols:
                    errors.append(
                        f"[运行时][{TREEVIEW}:{oid}] 实际列数为 0 —— 界面上是一张空白表格。"
                    )
                    continue
                stats["column"] += len(cols)
                for c in cols:
                    # 「是否漏写 text」由 XML 层精确判断，这里不做等值启发式，
                    # 否则 text 恰好等于 id 时会误报。
                    anchor = str(widget.column(c, "anchor") or "").strip()
                    if anchor not in VALID_ANCHORS:
                        errors.append(
                            f"[运行时][{TREEVIEW}:{oid}] 列 {c} 的 anchor=\"{anchor}\" 非法。"
                        )

            elif cls == NOTEBOOK:
                stats["notebook"] += 1
                tabs = widget.tabs()
                if not tabs:
                    errors.append(
                        f"[运行时][{NOTEBOOK}:{oid}] 实际页签数为 0 —— "
                        f"检查 {NOTEBOOK_TAB} 是否为直接子节点。"
                    )
                    continue
                stats["tab"] += len(tabs)
                for t in tabs:
                    if not str(widget.tab(t, "text") or "").strip():
                        errors.append(f"[运行时][{NOTEBOOK}:{oid}] 存在标题为空的页签。")

        stats["callbacks"] = _declared_callbacks(builder)
    finally:
        try:
            root.destroy()
        except Exception:
            pass


# --------------------------------------------------------------------------
def check_file(path) -> bool:
    print(f"\n=== {path} ===")
    errors, warns = [], []
    stats = {"treeview": 0, "column": 0, "notebook": 0, "tab": 0,
             "callbacks": [], "tops": []}

    try:
        xml_root = ET.parse(path).getroot()
    except ET.ParseError as e:
        print(f"FAIL: 不是合法 XML -> {e}")
        return False

    _xml_checks(xml_root, errors, warns)
    id2class = _id_class_map(xml_root)

    try:
        _runtime_checks(path, id2class, errors, warns, stats)
    except Exception as e:
        errors.append(f"[运行时] 构建失败 -> {type(e).__name__}: {e}")

    print(f"顶层对象：{stats['tops']}")
    print(f"控件统计：Treeview×{stats['treeview']}（列×{stats['column']}）  "
          f"Notebook×{stats['notebook']}（页×{stats['tab']}）")
    if stats["callbacks"]:
        print(f"声明的回调（controller 必须有同名方法）：{stats['callbacks']}")

    for w in warns:
        print(f"  [WARN] {w}")
    if errors:
        print(f"FAIL: 发现 {len(errors)} 处语义问题：")
        for e in errors:
            print(f"  [ERR ] {e}")
        return False

    print("OK: 语义校验通过。")
    return True


def main() -> int:
    args = sys.argv[1:]
    files = args or sorted(glob.glob(os.path.join(HERE, "*.ui")))
    if not files:
        print("没有找到任何 .ui 文件")
        return 1

    results = [check_file(p) if os.path.isfile(p)
               else (print(f"\n=== {p} ===\nFAIL: 文件不存在") or False)
               for p in files]

    ok = sum(1 for r in results if r)
    print(f"\n汇总：{ok}/{len(results)} 个 .ui 通过")
    return 0 if all(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
