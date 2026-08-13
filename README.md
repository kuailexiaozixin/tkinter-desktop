# tkinter-desktop

原生 **Tkinter / ttk** 桌面应用的全生命周期 AI 技能（Agent Skill）。从需求澄清、MVC 架构分层、界面设计、编码、线程与异步、SQLite 数据层、运行验证到 PyInstaller 打包交付，一次跑通，最终交付物是**原生桌面 EXE**（无浏览器、无本地 HTTP 服务）。

> 本技能以 `SKILL.md` 为入口，面向 AI Agent（如 Claude / 灵犀等支持 AgentSkills 规范的助手）。AI 读取后即可按标准化流程辅助开发 Tkinter 桌面应用。

---

## 技术栈（默认交付栈）

| 层 | 选型 | 说明 |
|----|------|------|
| GUI 框架 | **tkinter / ttk** | Python 标准库，无需额外安装 |
| 界面定义 | **pygubu** | 界面以 `.ui` 为唯一载体，运行期用 `pygubu.Builder` 加载 |
| 数据层 | **sqlite3** | Python 标准库，零第三方依赖 |
| 打包 | **PyInstaller** | 产出原生 Windows EXE |
| 原生能力 | ctypes / pywin32 | 可选增强（Win32 消息循环、资源管理等） |

**架构铁律**：界面以 `.ui` 为唯一载体；非界面部分的业务/数据层保持**零第三方依赖**。第三方增强（tksheet / tkchart 等）按需合法引入，打包时补 `hidden-import`。

---

## 特性

- **MVC 分层**：视图（`.ui`）与控制器、数据仓库（Repository）解耦，可测试性高
- **pygubu 单一界面方案**：AI 只写 `.ui` + 用 `pygubu.Builder` 校验/加载，自动化闭环完整
- **内置 SQLite 数据层**：`Repository` 模式，`:memory:` 便于集成测试
- **完整质量门禁**：pytest + 无头 GUI 冒烟测试 + release gate，交付前自动校验
- **Win32 原生能力**：ctypes 消息循环、资源管理，可做原生 Windows 增强
- **参考实现优先**：`examples/` 提供可直接参考/改造的真实项目

---

## 目录结构

```
tkinter-desktop/
├── SKILL.md              # 技能主入口（工作流 + 铁律）
├── CHANGELOG.md          # 版本变更记录
├── references/           # 深度参考（架构、UI、打包、质量门禁、Win32 等）
├── examples/             # 参考实现（优先参考，非必要不自造轮子）
│   ├── inventory-manager # 库存管理示例
│   ├── bulk-image-processor
│   ├── native-win32      # 原生 Win32 示例
│   ├── pygubu-designer
│   ├── tkinter-designer
│   ├── thonny / idle     # 第三方开源项目参考
│   └── README.md
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

1. **读取入口**：`SKILL.md` 定义了完整工作流与铁律，是执行的最高依据。
2. **写控件代码前**：必读 `references/official-docs/` 的 ttk 官方转档（HARD-GATE）。
3. **界面设计**：只用 pygubu 写 `.ui` + `pygubu.Builder` 加载，参考 `pygubu/` 子技能。
4. **生成项目**：用 `templates/` 脚手架模板（含 `bootstrap_project.ps1` / `run_dev.py`）初始化。
5. **开发迭代**：Controller + Repository 分层编码，线程用 `after()` 调度回 UI。
6. **质量门禁**：`pytest` + `scripts/smoke_test_gui.py`（无头 GUI 冒烟）+ `release_gate.py`。
7. **打包**：`scripts/build_windows_exe.ps1` 产出 EXE，按 `references/08-packaging.md` 补 hidden-import。

> 参考 `examples/` 中与目标最接近的项目，非必要不自造轮子。

---

## 许可与来源

- 由 AI Agent 按 AgentSkills 规范创建并维护，`author: agent`，`platform: windows`
- 开源用于学习与二次开发，欢迎提交 Issue / PR 完善工作流

---

**相关**：同系列的 [fasthtml-desktop](https://github.com/kuailexiaozixin/fasthtml-desktop)（Web 桌面壳方案，技术栈互斥，可作对比）。
