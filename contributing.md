# Contributing

感谢你愿意为 **tkinter-desktop** 贡献！

## 社区准则

- **友善与包容**：尊重每一位贡献者，遵循 [Contributor Covenant](https://www.contributor-covenant.org/)。
- **默认善意**：文字沟通容易产生歧义，请倾向于宽容理解。
- **教学相长**：若发现文档/示例有困惑之处，欢迎开 Issue 或 PR 改进。

## 如何贡献

### 报告问题

- 打开 [Issues](https://github.com/kuailexiaozixin/tkinter-desktop/issues)，清晰描述：目标、期望行为、实际行为、环境（Python 版本、系统）。
- 若涉及打包/控件异常，请附最小复现。

### 提交 PR

1. Fork 本仓库，基于 `main` 新建分支。
2. 改动技能核心逻辑时，**同步更新** `SKILL.md`、相关 `references/` 与 `CHANGELOG.md`。
3. 新增参考实现放入 `examples/`，并登记到 `examples/README.md`。
4. 保持三条铁律不被破坏：
   - 界面以 `.ui` 为唯一载体（pygubu Builder 加载）
   - 非界面业务/数据层保持零第三方依赖
   - 质量门禁（pytest + 无头 GUI 冒烟）必须通过
5. 提交信息简洁清晰，描述改动意图。

## 安全

发现安全漏洞请**不要**公开提交 Issue，而是通过仓库的 Security 途径私下报告（见 `SECURITY.md`）。

## 开发环境

- 技术栈：tkinter/ttk + pygubu + sqlite3 + PyInstaller（详见 `README.md`）
- 本地可运行 `scripts/run_dev.py` 做冒烟验证。
