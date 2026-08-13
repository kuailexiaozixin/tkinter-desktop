# Tcl 8.6 / Tk 8.6 官方命令参考（本地 Markdown）

本目录是 `www.tcl-lang.org/man/tcl8.6/` 的**命令参考部分**的本地转档，
与 `tkinter-desktop` 技能的运行期严格对齐：**运行期 = Tk 8.6 / Python 3.13.14**。
原始 HTML 已转为 **Markdown**（`*.md`）以节省体积。

## 内容清单

已镜像 **Tcl/Tk 8.6.18 全部 16 个官方分区**：

| 目录 / 文件 | 说明 | 数量 |
| --- | --- | --- |
| `contents.md` | 总索引（Tcl/Tk 8.6.18 文档入口） | 1 |
| `UserCmd/` | Tcl/Tk 应用（`tclsh` / `wish` 解释器） | 3 页 + `contents.md` |
| `TclCmd/` | Tcl 命令参考（`tclsh` 实现的命令） | 124 页 + `contents.md` |
| `TkCmd/` | Tk 命令参考（`wish` 实现的命令） | 86 页 + `contents.md` |
| `ItclCmd/` | [incr Tcl] 包命令 | 18 页 + `contents.md` |
| `SqliteCmd/` | SQLite3 包命令 | 2 页 + `contents.md` |
| `TdbcCmd/` | TDBC 包命令 | 7 页 + `contents.md` |
| `TdbcmysqlCmd/` | tdbc::mysql 包命令 | 2 页 + `contents.md` |
| `TdbcodbcCmd/` | tdbc::odbc 包命令 | 2 页 + `contents.md` |
| `TdbcpostgresCmd/` | tdbc::postgres 包命令 | 2 页 + `contents.md` |
| `TdbcsqliteCmd/` | tdbc::sqlite3 包命令 | 2 页 + `contents.md` |
| `ThreadCmd/` | Thread 包命令 | 5 页 + `contents.md` |
| `TclLib/` | Tcl C API | 109 页 + `contents.md` |
| `TkLib/` | Tk C API | 88 页 + `contents.md` |
| `ItclLib/` | [incr Tcl] 包 C API | 7 页 + `contents.md` |
| `TdbcLib/` | TDBC 包 C API | 2 页 + `contents.md` |
| `Keywords/` | 关键词索引 | 27 页 + `contents.md` |

总计 **488 个命令/API 页面**，0 下载失败。

镜像脚本：
- `mirror_tcl86_full.py`：**产出 Markdown**（`html2text` 转档，从正文 NAME 起点转换、交叉链接改 `*.md`），支持增量（跳过已有 `.md`）。

## 如何打开

直接查看 `contents.md`（Markdown 文本，用编辑器 / Markdown 阅读器打开）。
每个分区目录下均有 `contents.md`（命令页索引），可逐级进入每个命令/API 页；
页内交叉链接已改写为相对 `*.md` 链接（跨分区链接仍有效）。

## ⚠️ 版本铁律：只用 8.6，不要用 9.0

- 本技能运行期是 **Tk 8.6 / Tcl 8.6**。所有写入技能文档的论断都必须经过运行期验证。
- **禁止引入 `www.tcl-lang.org/man/tcl9.0/`（或 `tk9.0/`）文档**：
  Tcl 9.0 手册包含 8.6 **不存在**的命令，例如 `busy`、`systray`、
  `sysnotify`、`print`、`ttk_vsapi` 等。如果在 8.6 运行期引用这些命令，
  会直接 `TclError` / 行为不符，违反技能「所有论断运行期验证」的硬性规则。
- 若需查证某个命令，请以本目录的 8.6 镜像为准。

## 与技能文档的关系（DRY）

本镜像填补了技能参考文档中 6 个偏低层、但 tkinter 直接依赖的空白
（命令名 → 本地页）：

1. 自定义虚拟事件 + `event` / `bindtags` → `TkCmd/event.md`、`TkCmd/bindtags.md`
2. `ttk::style` 元素 / 布局引擎 → `TkCmd/ttk_style.md`
3. `wm` 子命令全集 → `TkCmd/wm.md`
4. `winfo` / `grab` / `tkwait` 全集 → `TkCmd/winfo.md`、`TkCmd/grab.md`、`TkCmd/tkwait.md`
5. `option` 选项数据库 → `TkCmd/option.md`
6. `clipboard` / `selection` 命令 → `TkCmd/clipboard.md`、`TkCmd/selection.md`

按 DRY 原则，这些低层细节应作为「上游权威参考」指向本目录，
**不应整段搬运进 `03-ui-design.md` / `04-widgets-and-patterns.md`**；
如需在技能正文中引用，写一句结论 + 指向本目录对应页的链接即可。

## 补全说明（2026-08-10）

已将全部 **16 个官方分区**补全为本地 Markdown（此前仅 `TclCmd` + `TkCmd` 两个命令分区）。
补全覆盖：解释器（`UserCmd`）、第三方包命令（`Itcl`/`Sqlite`/`Tdbc`/`Thread`）、
C API（`TclLib`/`TkLib`/`ItclLib`/`TdbcLib`）与关键词索引（`Keywords`）。

- 补全脚本：`mirror_tcl86_full.py`（产出 Markdown，增量跳过已有 `.md`）。
- 新增分区页面为 `html2text` 转档，从正文 `NAME` 起点转换（跳过面包屑与顶部导航），
  交叉链接已改 `*.md`；与原有 `TclCmd`/`TkCmd` 页面的精确排版略有差异（内容完整）。
