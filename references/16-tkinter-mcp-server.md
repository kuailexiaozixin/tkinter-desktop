# 21 tkinter-mcp-server：AI 驱动的真实 UI 自动化（MCP）

> 上游项目：[github.com/tctibbs/tkinter-mcp-server](https://github.com/tctibbs/tkinter-mcp-server)（MIT，Python 3.10+）。
> 本文件说明它是什么、怎么装、以及如何在 tkinter-desktop 工作流（尤其测试与质检）中融入。
> 它直接补齐 `09-testing-and-quality.md` 里 L4（E2E/UI 自动化）与 L5（验收）缺的"真实事件环驱动 + 多模态核验"能力。
> 文中工具名 / 签名已对照本机已安装源码 `tkinter_mcp/server/mcp_server.py` 逐条核对（共 16 个工具）。

## 1. 它是什么

一个 **MCP Server**：让 AI 智能体（Claude、WorkBuddy 等）**启动、内省、控制** Tkinter GUI 应用。
核心特点：

- **零侵入**：通过 monkey-patch `tkinter.Tk.__init__`，在自定义 launcher 里注入一个探针 agent；
  **目标应用无需任何改造**即可被检视/操控。
- **线程安全**：探针通过本地 socket 与 MCP Server 通信，GUI 操作走 Tk 主线程，避免跨线程崩溃。
- **结构化 + 视觉双通道**：既能拿到控件树 JSON（精确断言），也能截图（多模态视觉核验）。

这恰好解决了本技能旧的"AI 真实弹窗自测"短板——过去要么用无头 `smoke_test_gui.py`（绕过真实事件环、
直接调 Controller），要么用 `pywinauto`（对 Tk 的窗口管理较脆弱）。tkinter-mcp-server 走**真实事件环**且对 Tk 原生友好。

## 2. 工具能力表（已核对安装源码，共 16 个）

| 工具 | 签名 | 作用 | 测试用途 |
|---|---|---|---|
| `launch_app` | `launch_app(script_path: str)` | 以检视模式启动一个 Tkinter 应用 | 取代手动 `启动.bat`，启动即带探针 |
| `is_connected` | `is_connected()` | 检查当前是否有 app 连接 | 冒烟前置健康检查 |
| `get_ui_layout` | `get_ui_layout()` | 取控件树为结构化 JSON | **精确断言**：某控件存在、层级、文本、启用态；并从中取 `widget_id` |
| `view_application` | `view_application(max_size: int = 800, quality: int = 70)` | 截高质量 JPEG 截图 | **多模态核验**：中文无截断、布局无重叠/塌陷 |
| `view_application_thumbnail` | `view_application_thumbnail()` | 小缩略图截图 | 概览 |
| `get_window_info` | `get_window_info()` | 窗口位置与尺寸 | 验证窗口正常渲染、非最小化/零尺寸 |
| `click_widget` | `click_widget(widget_id: int, button: str = "left", double: bool = False)` | 点击控件（左/右/中、单/双击） | 真实按钮事件（走真实绑定） |
| `type_text` | `type_text(widget_id: int, text: str)` | 向 Entry/Text 键入文本 | 真实输入框填充 |
| `get_widget_by_text` | `get_widget_by_text(text: str)` | 按文本定位控件 | 不依赖内部变量名，靠可见文本定位 |
| `focus_widget` / `get_focused_widget` | `focus_widget(widget_id: int)` / `get_focused_widget()` | 设/取焦点 | 键盘流验证 |
| `get_widget_value` / `set_widget_value` | `get_widget_value(widget_id: int)` / `set_widget_value(widget_id: int, value: str)` | 读/写控件值（Entry/Text/Scale/Checkbutton…） | 断言输入回显、驱动状态 |
| `get_widget_options` | `get_widget_options(widget_id: int)` | Combobox/Listbox 选项 | 断言下拉内容 |
| `drag_widget` | `drag_widget(start_widget_id: int, end_widget_id: int)` | 两控件间拖放 | 拖拽交互验证 |
| `close_app` | `close_app()` | 终止应用 | 冒烟收尾，等同 `app.kill()` |

> 全部工具返回字符串（JSON 文本或截图路径）。控件以 `widget_id`（整数）标识，取自 `get_ui_layout()` 返回的控件树。

## 3. 安装与注册

### 3.1 安装包

```bash
# 推荐 pip（用 PIL/ImageTk 的应用务必 pip，不要 uvx，见 §6 局限）
pip install tkinter-mcp-server
```

> ⚠️ **uvx 与 PIL/ImageTk 不兼容**：若目标应用用到 PIL，必须用 `pip install` 而非 `uvx`，
> 否则截图功能可能异常。
> ⚠️ **镜像站可能缺此包**：实测 `pypi.tuna.tsinghua.edu.cn` 等镜像未同步该包，
> 安装失败请用官方源：`pip install tkinter-mcp-server --index-url https://pypi.org/simple`。

### 3.2 注册为 MCP Server（WorkBuddy 环境）

本技能运行在 WorkBuddy，MCP 配置位于 `~/.workbuddy/mcp.json`（等价 Claude 的 `claude mcp add`）。
加入（**用 entry-point 的完整路径最稳，避免 PATH 解析歧义**）：

```json
{
  "mcpServers": {
    "tkinter-mcp-server": {
      "command": "D:\\Python\\cpython-3.13.14-windows-x86_64-none\\Scripts\\tkinter-mcp-server.exe"
    }
  }
}
```

> 若 WorkBuddy 进程的环境 PATH 已包含该 Scripts 目录，也可简写为 `"command": "tkinter-mcp-server"`。
> 注册后需在连接管理里**信任/启用**该 server 才会激活。

## 4. 工作原理（简图）

```
[AI/MCP Client]  ⇄  [MCP Server]  ⇄  [本地 socket]  ⇄  [探针 Agent]  ⇄  [Tkinter App]
```

- MCP Server 用自定义 launcher 启动目标 app，launcher 在 `Tk.__init__` 时注入探针。
- 探针在 app 进程内，经 socket 把控件树/截图回传、并接收点击/键入指令（主线程执行）。
- AI 因此能"看见并操作"真实运行的 GUI，所有断言基于真实渲染结果。

## 5. 在工作流中的融入

按阶段映射（①–⑧），**重点在 ⑤ 视觉质检、⑦ 运行验证、⑧ 打包交付、① 需求**。

### ⑤ 界面设计 / 视觉质检
- 用 `view_application` 截图 → 接入本技能既有的"AI 多模态视觉审查"（发现控件不可见/重叠/中文截断）。
- 比 §3 的"几何检查→PNG"更直接：MCP 截图即真实窗口，省去 `root.update()` + `savefig` 的脚手架。

### ⑦ 运行验证（AI 真实弹窗自测）
- **取代/增强** `pywinauto`：用 `launch_app(script_path=...)` 启动源码入口（或 `启动.bat` 等价入口），
  `type_text` 填表 → `click_widget` 触发真实按钮 → `get_ui_layout`/`get_widget_value` 断言结果。
- 覆盖正常 + 异常路径：异常路径（空输入）可断言弹窗文本（`get_widget_by_text` 命中"输入错误"）。
- 这是 L4/E2E + L5 验收在"源码态"的落点；比无头冒烟多了**真实事件环**与**多模态核验**。

### ⑧ 打包交付（EXE 冒烟 / E2E）
- 对**已构建的 EXE**：见 §6 局限——MCP 探针需在 app 启动早期注入，
  因此**无法直接 attach 到已运行的 EXE**。可行做法：
  1. E2E 在**源码态**用 `launch_app` 跑完整业务路径（推荐，覆盖最全）；
  2. EXE 产物的"启动冒烟"仍由 `启动.bat` + 进程/窗口探测完成（保持既有 `build_windows_exe.ps1` 逻辑），
     必要时用 `view_application` 对 EXE 启动后的窗口截图核验（若能从外部启动并让 MCP 接管启动时机）。
- 结论：**L4 业务正确性优先在源码态用 MCP 验证；EXE 冒烟保"能启动+能渲染"底线。**

### ① 需求（验收回溯）
- ① 产出的 MoSCoW 验收标准，逐条写成 MCP 驱动的会话脚本（见 §7），
  形成 `09` §5.5 的可追溯矩阵。验收项 = 一段"启动→操作→断言"的 MCP 工具调用序列。

### 与既有测试手段的关系
| 手段 | 角色 | 与 MCP 的关系 |
|---|---|---|
| `smoke_test_gui.py`（无头） | 浅层门禁前哨 | 保留；MCP 不替代它，MCP 负责更深的真实运行验证 |
| `pytest` 单元/集成 | 逻辑正确性 | 保留；MCP 负责 UI/业务路径层 |
| `pywinauto` | 真实 UI 自动化（备选） | MCP 对 Tk 更稳，优先 MCP；pywinauto 作降级 |
| tkinter-mcp-server | **AI 驱动真实事件环 + 多模态核验** | 新增的深层主力 |

## 6. 局限与注意

- **需经其 launcher 启动**：探针在 `Tk.__init__` 注入，故 app 必须由 `launch_app(script_path=...)` 拉起；
  对"已打包独立 EXE"无法直接 attach（见 ⑧）。
- **PIL/ImageTk + uvx 不兼容**：含 PIL 的应用用 `pip install`，勿用 uvx。
- **Python 3.10+**：低于此版本无法运行 server。
- **截图依赖显示会话**：`view_application` 需要图形会话（同无头冒烟的 `withdraw` 限制），
  纯无显示 CI 只能跑 `get_ui_layout`（JSON 树）这类非截图断言。
- **多窗口/Toplevel**：复杂多窗口应用需按窗口标题/层级在 `get_ui_layout` 结果里定位，
  断言脚本要处理控件树嵌套。

## 7. 示例：AI 驱动的验收测试会话（公告下载器 L5）

把验收标准 `AC-01 "用户输入代码能精确查到该股票公告"` 写成 MCP 工具调用序列：

```
1. launch_app(script_path="src/announcement_downloader/tkapp.py")   # 启动即带探针
2. is_connected() -> "true"
3. layout = get_ui_layout()        # 取控件树 JSON，定位搜索框 / 搜索按钮的 widget_id
4. type_text(widget_id=<搜索框 id>, text="000001")                   # 真实键入
5. click_widget(widget_id=<搜索按钮 id>)                             # 真实按钮事件
6. layout = get_ui_layout(); 断言: Treeview 行中 secCode 全为 "000001"，且无其他股票
7. view_application() -> 截图，多模态核验中文标题无截断
8. close_app()
```

> 注意参数名：`launch_app` 用 `script_path=`，`type_text`/`click_widget` 用 `widget_id=`（整数，
> 取自 `get_ui_layout()` 的控件树），不要写成 `entry=` / `target=`。

这段序列可固化为一个 pytest 包装（用 MCP 客户端 SDK 调工具），纳入 `09` §5.5 的验收矩阵，
作为 PR 前必跑项——真正实现"业务对"而非"能跑通"。

## 8. 快速决策

- 只要"控件存在/接线通" → 无头 `smoke_test_gui.py`（快、每次改码）。
- 要"业务结果正确 / 真实点击有效 / 中文渲染对" → **tkinter-mcp-server**（PR 前/发布前）。
- 纯逻辑（金额/口径/分类）→ `pytest` 单元/集成（最快、最稳）。
