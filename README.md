# tkinter-desktop

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![skills.sh](https://skills.sh/b/kuailexiaozixin/tkinter-desktop)](https://skills.sh/kuailexiaozixin/tkinter-desktop)

原生 **Tkinter / ttk** 桌面应用的全生命周期 **Agent Skill**——从需求澄清、MVC 架构分层、界面设计、编码、线程与异步、SQLite 数据层、运行验证到 PyInstaller 打包交付，一次跑通，最终交付物是**原生桌面 EXE**（无浏览器、无本地 HTTP 服务）。

> **Agent Skill 是什么？** Skill 是「指令 + 脚本 + 资源」的文件夹，AI Agent 会动态发现并加载它，以在特定任务上表现得更好。本仓库遵循 [Agent Skills 开放标准](https://agentskills.io)——**一次编写，处处使用**，可被 Claude、灵犀、Codex 等支持该标准的助手直接读取。

---

## 这是什么

本技能为 AI Agent 提供一套**标准化、可复现**的 Tkinter 桌面应用开发流程，解决「原生 GUI 项目结构混乱、可测试性差、打包反复踩坑」的痛点：

- **界面以 `.ui` 为唯一载体**（pygubu Builder 加载），业务/数据层保持零第三方依赖
- **MVC 分层 + Repository 数据模式**，Controller 可无头测试
- **内置完整质量门禁**：pytest + 无头 GUI 冒烟 + release gate，交付前自动校验
- **Win32 原生能力**（ctypes / pywin32）可选增强

适合：库存管理、图像批处理、工具软件、内部系统等**不依赖浏览器**的桌面程序。

---

## 技术栈（默认交付栈）

| 层 | 选型 | 说明 |
|----|------|------|
| GUI 框架 | **tkinter / ttk** | Python 标准库，无需额外安装 |
| 界面定义 | **pygubu** | 界面以 `.ui` 为唯一载体，运行期用 `pygubu.Builder` 加载 |
| 数据层 | **sqlite3** | Python 标准库，零第三方依赖 |
| 打包 | **PyInstaller** | 产出原生 Windows EXE |
| 原生能力 | ctypes / pywin32 | 可选增强（Win32 消息循环、资源管理等） |

---

## 安装 / 使用

Agent Skills 通常已内置在支持该标准的助手中；也可将本仓库添加为 **Skill / Plugin**：

```bash
# 以支持 AgentSkills 的助手为例（如 Claude Code）
/plugin marketplace add kuailexiaozixin/tkinter-desktop
```

安装后，只需对助手说一句，例如：

> 「用 tkinter-desktop 技能，帮我做一个带 SQLite 的库存管理桌面程序，打包成 EXE。」

助手会读取 `SKILL.md`，按其中的工作流与铁律自动完成从脚手架到打包的完整链路。

---

## 作为 dsh 插件使用

本技能也可打包为 [DeepSeek Harness (dsh)](https://deepseek-ai.github.io/deepseek-harness/) 插件的 **Cordis Bundle**，把技能注册进 dsh 的 `ctx.skills`，让 dsh Agent 在会话中通过 `skill` 工具加载使用。插件源码位于 [`dsh-plugin/`](dsh-plugin/)，**形态**为 Cordis Bundle（Host 侧），**类型**为 skill 插件（嵌入式提供方，参照官方 `dsh-skill-badge`）。

### 安装

在已安装 `dsh` CLI 的机器上，进入本仓库根目录：

```bash
dsh plugin --profile web add ./dsh-plugin
```

验证配置层并启动：

```bash
dsh --profile web --dump-config   # 应看到 "# == dsh-tkinter-desktop" 层
dsh web
```

### 使用

启动 dsh Web UI 后，对 Agent 说一句即可触发，例如：

> 「用 tkinter-desktop 技能，帮我做一个带 SQLite 的库存管理桌面程序，打包成 EXE。」

Agent 会调用 `skill` 工具加载本技能，按 `SKILL.md` 的工作流完成从脚手架到打包的完整链路。

### 移除

```bash
dsh plugin --profile web remove dsh-tkinter-desktop
```

详见 [dsh-plugin/README.md](dsh-plugin/README.md)。

---

## 目录结构

```
tkinter-desktop/
├── SKILL.md              # 技能主入口（工作流 + 铁律）
├── CHANGELOG.md          # 版本变更记录
├── LICENSE               # MIT 许可证
├── README.md             # 本文件
├── references/           # 深度参考（架构、UI、打包、质量门禁、Win32 等）
├── examples/             # 参考实现（优先参考，非必要不自造轮子）
├── templates/            # 项目脚手架模板（含启动.bat 等）
├── scripts/              # 自动化脚本（构建、测试、门禁、UI 设计）
├── docs/                 # 交付清单、术语表、排障
├── pygubu/               # pygubu 子技能（界面设计唯一默认方案）
├── ctypes/               # Win32 原生 API 参考
├── pywin32/              # pywin32 模块/对象参考
└── tcl-tk/               # Tcl/Tk 底层参考
```

---

## 快速开始（给 Agent）

1. **读取入口**：`SKILL.md` 定义完整工作流与铁律，是执行的最高依据。
2. **写控件代码前**：必读 `references/official-docs/` 的 ttk 官方转档（HARD-GATE）。
3. **界面设计**：只用 pygubu 写 `.ui` + `pygubu.Builder` 加载，参考 `pygubu/` 子技能。
4. **生成项目**：用 `templates/` 脚手架（含 `bootstrap_project.ps1` / `run_dev.py`）初始化。
5. **开发迭代**：Controller + Repository 分层编码，线程用 `after()` 调度回 UI。
6. **质量门禁**：`pytest` + `scripts/smoke_test_gui.py`（无头 GUI 冒烟）+ `release_gate.py`。
7. **打包**：`scripts/build_windows_exe.ps1` 产出 EXE，按 `references/08-packaging.md` 补 hidden-import。

> 参考 `examples/` 中与目标最接近的项目，非必要不自造轮子。

---

## 贡献

欢迎提交 Issue 与 PR 完善工作流。请遵循：

- 改动技能核心逻辑时，同步更新 `SKILL.md`、`references/` 与 `CHANGELOG.md`
- 新增参考实现请放入 `examples/`，并登记到 `examples/README.md`
- 保持「界面 `.ui` + 业务零依赖 + 质量门禁」三条铁律不被破坏

详见 [contributing.md](contributing.md)。

---

## 第三方内容与合规

`examples/` 目录下以完整源码形式收载了若干**第三方开源项目**（Thonny、IDLE、pygubu-designer、Tkinter-Designer、Inventory-Management-System、Bulk Image Processor 等），它们各自保留原始许可证与版权声明，与本仓库 MIT 许可相互独立。其中 inventory-manager、bulk-image-processor 的上游**未声明许可证**（默认保留所有权利），存在合规风险，不建议再分发。完整来源、许可证与使用注意详见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。

---

## 许可证

[MIT](LICENSE) © kuailexiaozixin

---

**相关**：同系列的 [fasthtml-desktop](https://github.com/kuailexiaozixin/fasthtml-desktop)（Web 桌面壳方案，技术栈互斥，可作对比）。
