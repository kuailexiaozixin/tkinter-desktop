# 15 · tksheet 参考手册（可选第三方：高性能表格 / 树形表格）

> **定位**：本文件是 `tkinter-desktop` 技能下「可选第三方增强」的专属参考。tksheet 是**纯 tkinter（基于 Canvas）的高性能表格 + 树形表格控件**，比标准库 `ttk.Treeview` 强大得多（可编辑、下拉、复选、进度条、拖拽行列、树形模式等），且不依赖 pandas（纯 tkinter 实现，更轻）。若只需“能编辑、功能丰富”的表格/树，首选 tksheet。
>
> 内容综合自官方仓库 README（https://github.com/ragardner/tksheet）整理。**许可证：MIT**。

---

## 0 · 重要状态说明

> 官方声明（README 原文）：*“With apologies, development of this library has ceased except for bug fixes or behavioral issues. Pull requests for other changes are unlikely to be merged.”* —— **除修 bug 外已停止开发**。新项目评估时应考虑此点（功能已很完整，但不会有新特性）。仅支持 **Python >= 3.8**。

---

## 1 · 功能清单（官方列表，逐条）

- 平滑显示与修改表格数据
- 直接编辑单元格
- 单元格值可为**任意类**（默认是任意带 `__str__` 方法的对象）
- **拖拽**调整列与行
- **可编辑的 Treeview 模式**（带可用拖拽、撤销等）
- 多行表头与索引单元格
- 可展开行高与列宽
- 可改字体与字号（不支持单个单元格单独字体）
- 可改表格中**任意颜色**
- **下拉框（Dropdown boxes）**
- **复选框（Check boxes）**
- **进度条（Progress bars）**
- 隐藏行和/或列
- 任意单元格/行/列的左对齐 `"w"` / 居中 `"center"` / 右对齐 `"e"`
- **内置自然排序（natural sorting）**
- 可选内置查找窗口

> 限制：因 Tkinter Canvas 限制，**不支持 RTL（从右到左）语言**。

---

## 2 · 安装

```bash
pip install tksheet
```

---

## 3 · 基本用法（v7+ 简洁语法）

```python
import tkinter as tk
from tksheet import Sheet

root = tk.Tk()
root.title("tksheet demo")

# 直接给数据即可，控件自动渲染
sheet = Sheet(root, data=[[1, 2, 3], [4, 5, 6], ["a", "b", "c"]])
sheet.pack(expand=True, fill="both")

root.mainloop()
```

### v7+ 单元格 / 列读写（类 Excel 语法）

```python
# 写单元格 A1
sheet["A1"].data = "edited cell A1"

# 读整列 B
column_b = sheet["B"].data

# 在第 4 列后插入 2 个空列，并记入撤销栈
sheet.insert_columns(columns=2, idx=4, undo=True)

# 删除第 0 和 3 列，并记入撤销栈
sheet.delete_columns(columns=[0, 3], undo=True)
```

---

## 4 · 常用 API 概览

- 构造：`Sheet(parent, data=None, width=None, height=None, **kwargs)`
- 数据读写：
  - `sheet["A1"].data` / `sheet["B"].data` / `sheet[0].data`（行）等
  - `set_sheet_data(data)` / `get_sheet_data()`
- 结构修改：`insert_columns` / `delete_columns` / `insert_rows` / `delete_rows`（均支持 `undo=`）
- 外观：`set_all_cell_sizes_to_text()` / `set_options(...)` / `set_theme()`
- 交互：`extra_bindings()`（绑定事件，如 `"edit_cell"`、`"end_edit_cell"`、`"begin_drag"` 等）
- 单元格控件：`dropdown_boxes` / `check_boxes` / `progress_bars` 相关方法与配置
- 树形模式：`enable_treeview()` / `treeview` 相关 API
- 排序：`sort()` / 内置自然排序

> 完整文档：
> - 版本 6 文档（Wiki）：https://github.com/ragardner/tksheet/wiki/Version-6
> - 版本 7 文档：https://ragardner.github.io/tksheet/DOCUMENTATION.html
> - 更新日志：https://github.com/ragardner/tksheet/blob/master/docs/CHANGELOG.md

---

## 5 · v7 重要变更（迁移注意）

- **所有** `extra_bindings()` 事件对象已改变（详见 v7 文档“bind specific table functionality”）。
- `edit_cell` / `end_edit_cell` 绑定的函数**不再要求返回值**，也不再会把单元格设为返回值；改用 `edit_validation()` 做校验（见 v7 文档“validate user cell edits”）。
- `edit_cell_validation` 已移除，由 `edit_validation()` 取代。
- 仅支持 Python >= 3.8；文件名已变更。

---

## 6 · 何时选 / 何时不选

**选 tksheet 当**：
- 需要**高性能、可编辑、功能丰富**的表格（下拉/复选/进度条/拖拽行列/树形）
- 不想引入 pandas 重依赖（纯 tkinter 实现，更轻）
- 需要树形表格且比 `ttk.Treeview` 强

**不选 tksheet 当**：
- 需要 RTL 语言支持（tksheet 不支持）
- 要求库持续活跃开发（本项目已停止功能开发，仅修 bug）

---

## 7 · 与技能工作流的整合

- 在 `04-widgets-and-patterns.md` 的表格场景下，tksheet 是 `ttk.Treeview` 的强力替代；其下拉/复选/进度条能力可省去大量手写代码。
- **打包提醒**：tksheet 纯 tkinter + 无重依赖，打包体积小、hidden-import 少，是第三方表格里对 `08-packaging.md` 最友好的选项之一。

---

## 8 · 官方参考链接（已下载整理于本文件）

- 仓库：https://github.com/ragardner/tksheet
- v7 文档：https://ragardner.github.io/tksheet/DOCUMENTATION.html
- v6 Wiki：https://github.com/ragardner/tksheet/wiki/Version-6
- 更新日志：https://github.com/ragardner/tksheet/blob/master/docs/CHANGELOG.md
