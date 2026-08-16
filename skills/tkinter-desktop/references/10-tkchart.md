# 10 · tkchart 参考手册（可选第三方：实时折线图 / LineChart）

> **定位**：本文件是 `tkinter-desktop` 技能下「可选第三方增强」的专属参考。tkchart 是基于 tkinter 的**实时更新折线图控件**（核心类 `tkchart.LineChart` + `tkchart.Line`），纯 tkinter 实现、无重依赖，适合在桌面工具里画「流式/实时」折线（如监控曲线、传感器数据、实时统计）。标准的 `03-ui-design.md §6.4 Canvas 自绘图表`也能画静态图，但若要**持续追加数据点、动画更新、多线对比、刻度网格自动管理**，tkchart 比手写 Canvas 省事得多。
>
> 内容综合自官方中文文档（https://github.com/thisal-d/tkchart/blob/main/documentation/DOCUMENTATION_zh.md）与仓库 README。**许可证：MIT**。

---

## 0 · 一句话结论

- **纯 tkinter 实现**，运行期仅一个第三方依赖 `tkchart`，**本机实测打包增量 ≈0**（与 tksheet 同量级；远低于 ttkbootstrap 的 +8MB）。
- **核心三步走**：① 建 `LineChart`（指定 `master` / `x_axis_values` / `y_axis_values`）→ ② 建 `Line`（挂到 chart）→ ③ `chart.show_data(line=..., data=[...])` 推数据。
- **实时更新**：把 `show_data` 放进后台线程循环（或 `after` 轮询），配合 `root.update()` / `mainloop` 即可流式刷新。
- **打包**：通常**无需** hidden-import；若运行期报 `ModuleNotFoundError: tkchart`，补 `hiddenimports=['tkchart']`（见 §9）。

---

## 1 · 功能清单

- **实时 / 流式更新**：持续追加数据点，曲线平滑动画刷新（live updating）
- **多线对比**：同一 `LineChart` 上可叠加多条 `Line`
- **坐标轴定制**：x/y 轴范围、标签数、精度、命名、字体/颜色
- **网格线（section）**：x/y 方向网格数量、颜色、实线/虚线样式
- **线条样式**：颜色、粗细、实/虚/点线、端点高亮、区域填充
- **鼠标指针交互**：`pointer_state` 显示悬浮数值
- **尺寸可控**：`width` / `height` 适配任意布局
- **细粒度配置**：v2.2.0+ 提供 `configure_*()` 系列方法

---

## 2 · 安装

```bash
pip install tkchart
```

```python
import tkchart
```

> 仓库：https://github.com/Thisal-D/tkchart ｜ PyPI：https://pypi.org/project/tkchart ｜ 中文文档：https://github.com/thisal-d/tkchart/blob/main/documentation/DOCUMENTATION_zh.md

---

## 3 · 核心类与参数

### 3.1 `tkchart.LineChart`（折线图主体）

**必备参数**

| 参数 | 说明 |
| ---- | ---- |
| `master` | 父控件（任意 widget） |
| `x_axis_values` | x 轴取值，`tuple`，如 `(1,2,3)` 或 `("a","b","c")` |
| `y_axis_values` | y 轴最小/最大，`tuple[int\|float, ...]`，如 `(-100, 100)` |

**常用可选参数**

| 参数 | 说明 |
| ---- | ---- |
| `width` / `height` | 图表宽/高（int） |
| `bg_color` / `fg_color` | 背景色 / 前景色 |
| `axis_color` / `axis_size` | 坐标轴颜色 / 线宽 |
| `x_axis_data` / `y_axis_data` | 轴名称（str） |
| `x_axis_label_count` / `y_axis_label_count` | 轴标签数量（int） |
| `x_axis_section_count` / `y_axis_section_count` | 网格线数量（int） |
| `x_axis_section_color` / `y_axis_section_color` | 网格线颜色 |
| `x_axis_section_style` / `y_axis_section_style` | 网格线样式：`"normal"` / `"dashed"` |
| `x_axis_section_style_type` / `y_axis_section_style_type` | 虚线尺寸，如 `(20, 10)` |
| `x_axis_font_color` / `y_axis_font_color` | 轴文字颜色 |
| `axis_font_style` | 轴字体，如 `("arial", 13, "bold")` |
| `data_font_style` | 数据标签字体 |
| `y_axis_precision` | y 轴小数精度（int） |
| `x_axis_data_position` / `y_axis_data_position` | 轴名称位置：`"top"` / `"side"` |
| `x_axis_display_values_indices` | 指定显示哪些 x 标签下标，如 `(1, 4, 7)` |
| `x_axis_point_spacing` | 数据点间距：`"auto"` 或 int |
| `pointer_state` / `pointer_color` | 鼠标指针交互开关/颜色 |

### 3.2 `tkchart.Line`（一条折线）

**必备参数**

| 参数 | 说明 |
| ---- | ---- |
| `master` | 所属 `LineChart` 实例 |

**常用可选参数**

| 参数 | 说明 |
| ---- | ---- |
| `color` | 折线颜色（str） |
| `size` | 折线粗细（int） |
| `style` | 线型：`"normal"` / `"dashed"` / `"dotted"` |
| `style_type` | 虚线尺寸，如 `(10, 2)` |
| `point_highlight` | 端点高亮开关：`"enabled"` / `"disabled"` |
| `point_highlight_color` / `point_highlight_size` | 高亮颜色 / 尺寸 |
| `fill` | 区域填充开关：`"enabled"` / `"disabled"` |
| `fill_color` | 填充颜色 |

---

## 4 · 常用方法

**LineChart**

- `configure(...)`：改属性（除 `master`）
- `show_data(data, line)`：**推送一组数据点到指定 line**（`data` 为单点列表如 `[v]` 或多点列表）
- `place` / `pack` / `grid`：布局（继承自 widget）
- `reset()` / `clear_data()`：清空数据
- `get_line_area()`：获取绘图区尺寸
- `get_lines_visible_data()`：获取当前可见数据
- `destroy()`：销毁

**Line**

- `configure(...)`：改线属性
- `cget(...)`：读参数
- `set_visible(bool)` / `get_visibility()`：显隐切换
- `get_data()` / `clear_data()` / `destroy()`

---

## 5 · 最小用法（静态单线）

```python
import tkinter as tk
import tkchart
import random

root = tk.Tk()
root.configure(bg="#151515")

# 1. 创建折线图（必须给 x/y 轴取值）
chart = tkchart.LineChart(
    master=root,
    x_axis_values=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
    y_axis_values=(-100, 100),
)
chart.pack()

# 2. 创建一条线
line = tkchart.Line(master=chart)

# 3. 推送数据（随机演示）
data = [x for x in range(-100, 101)]
def loop():
    chart.show_data(line=line, data=random.choices(data, k=1))
    root.after(500, loop)
loop()

root.mainloop()
```

---

## 6 · 实时流式更新（后台线程）

> 与技能「主线程规则」一致：UI 刷新仍在主线程，数据生产放后台线程，经 `chart.show_data` 推给主线程的 chart 对象。

```python
import tkinter as tk
import tkchart
import random
import threading
import time

root = tk.Tk()

# 1. 创建图表
chart = tkchart.LineChart(
    master=root,
    x_axis_values=("a", "b", "c", "d", "e", "f"),
    y_axis_values=(100, 900),
)
chart.place(x=10, y=10)

# 2. 创建线
line = tkchart.Line(master=chart)

# 3. 后台线程持续推数据
def loop():
    while True:
        chart.show_data(line=line, data=[random.choice(range(100, 900))])
        time.sleep(1)

threading.Thread(target=loop, daemon=True).start()
root.mainloop()
```

---

## 7 · 样式定制示例

**轴命名 + 字体颜色**

```python
chart = tkchart.LineChart(
    master=any_widget,
    x_axis_values=(2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025),
    y_axis_values=(-100, 100),
    y_axis_data="Y data",
    x_axis_data="X data",
    x_axis_data_font_color="#ff0000",
    y_axis_data_font_color="#00ff00",
    data_font_style=("arial", 15, "underline"),
)
```

**标签数量**

```python
chart = tkchart.LineChart(
    master=any_widget,
    x_axis_values=(2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025),
    y_axis_values=(-100, 100),
    x_axis_label_count=4,
    y_axis_label_count=10,
)
```

**y 轴精度**

```python
chart = tkchart.LineChart(
    master=any_widget,
    x_axis_values=(2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025),
    y_axis_values=(-100, 100),
    y_axis_label_count=12,
    y_axis_precision=4,
)
```

**网格线（实线/虚线）**

```python
chart = tkchart.LineChart(
    master=any_widget,
    x_axis_section_count=8,
    y_axis_section_count=5,
    x_axis_section_color="#2C2C2C",
    y_axis_section_color="#2C2C2C",
)
```

```python
chart = tkchart.LineChart(
    master=any_widget,
    x_axis_section_count=8,
    y_axis_section_count=5,
    x_axis_section_style="dashed",
    x_axis_section_style_type=(20, 10),
    y_axis_section_style="dashed",
    y_axis_section_style_type=(20, 10),
)
```

**数据点间距**

```python
chart.configure(x_axis_point_spacing="auto")
# 或固定像素
chart = tkchart.LineChart(master=any_widget, x_axis_point_spacing=40)
```

---

## 8 · 线条样式（`tkchart.Line`）

```python
line = tkchart.Line(master=chart, color="#30ACC7", size=5)
```

```python
line = tkchart.Line(master=chart, line_style="dashed")
```

```python
line = tkchart.Line(master=chart, line_style="dashed", line_style_type=(10, 2))
```

```python
line = tkchart.Line(
    master=chart,
    point_highlight="enabled",
    point_highlight_color="#80CCFF",
    point_highlight_size=8,
)
```

```python
line = tkchart.Line(master=chart, fill="enabled", fill_color="#5D6DB6")
```

**多线对比（不同样式）**

```python
line1 = tkchart.Line(master=line_chart, color="#5dffb6", size=2, style="dashed", style_type=(10, 5))
line2 = tkchart.Line(master=line_chart, color="#FFBAD2", size=2,
                     point_highlight="enabled", point_highlight_color="#FFBAD2")
```

---

## 9 · PyInstaller 打包

- tkchart 是**纯 Python + tkinter** 实现，**无 C 扩展、无 Tcl 资源、无重依赖**，打包体积增量≈0（本机实测：基线 stdlib tkinter ≈9.9MB，加 tkchart 后 ≈9.95MB）。
- **通常无需** `hidden-import` / `--add-data`。
- 若运行期 EXE 报 `ModuleNotFoundError: No module named 'tkchart'`，在 `.spec` 或命令行补：
  ```python
  hiddenimports=['tkchart']
  ```
- 一般流程仍走 `08-packaging.md` 的 `--onefile --windowed` 标准路径，与标准库 tkinter 应用完全一致。

---

## 10 · 与技能工作流的整合

- **何时选 tkchart**：需要「实时/流式折线图、多线对比、刻度网格自动管理」时，优先于 `03-ui-design.md §6.4` 的纯 Canvas 自绘（手写 Canvas 更适合一次性静态图或极特殊交互）。
- **主线程规则**：`show_data` 由主线程调用；数据生产放 `threading` + `queue`（或 `after` 轮询），不要直接在子线程操作 chart（见 `05-threading-and-async.md`）。
- **打包**：纯 tkinter、增量≈0，是第三方图表库里对 `08-packaging.md` 最友好的选项之一，不需要额外 hidden-import（除非运行时报缺模块）。
- 在 `17-tkinter-toolkit.md` 的「图表与可视化」分类中 tkchart 已被收录；本文件为其深度参考。

---

## 11 · 官方参考链接

- 仓库：https://github.com/Thisal-D/tkchart
- 中文文档：https://github.com/thisal-d/tkchart/blob/main/documentation/DOCUMENTATION_zh.md
- 英文文档：https://github.com/thisal-d/tkchart/blob/main/documentation/DOCUMENTATION_en.md
- PyPI：https://pypi.org/project/tkchart
- 变更日志：https://github.com/thisal-d/tkchart/blob/main/CHANGES_en.md
