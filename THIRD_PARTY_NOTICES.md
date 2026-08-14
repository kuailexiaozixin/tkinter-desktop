# Third-Party Notices

本仓库（`tkinter-desktop`）主仓库代码以 **MIT License** 发布（见根目录 `LICENSE`）。

`examples/` 目录下**以完整源码形式收载（vendored）了若干第三方开源项目**，用于教学研读与参考。这些第三方代码**各自保留其原始许可证与版权声明**，与本仓库 MIT License 相互独立；本仓库对它们**不做任何修改**（或仅在 `README`/`launcher` 处额外说明，业务代码保持上游原样）。

> 许可证兼容性说明：本仓库以 MIT 发布，与第三方项目之间构成 **aggregate（聚合分发）** 关系，不改变第三方代码自身许可证。其中含 **copyleft（GPL/AGPL）** 的项目（见下表），其代码在使用时须遵循其自身许可证（如 GPL 的 copyleft 传染性要求）。

---

## `examples/` 收载的第三方项目

| 目录 | 项目 | 上游来源 | 作者 / 版权方 | 许可证 | 版本 | 是否改动 |
|------|------|---------|--------------|--------|------|---------|
| `examples/thonny` | **Thonny** | https://github.com/thonny/thonny（PyPI `thonny-5.0.0`） | Aivar Annamaa | **MIT** | 5.0.0 | 未改动（完整源码） |
| `examples/idle` | **IDLE**（Python 标准库 `Lib/idlelib`） | https://github.com/python/cpython | Python Software Foundation | **PSF License v2** | Python stdlib | 未改动 |
| `examples/pygubu-designer` | **pygubu-designer** | https://github.com/alejandroautalan/pygubu-designer | Alejandro Autalan | **GPL-3.0**（copyleft） | — | 未改动 |
| `examples/tkinter-designer` | **Tkinter-Designer** | https://github.com/ParthJadhav/Tkinter-Designer | Parth Jadhav | **BSD-3-Clause** | — | 未改动（vendored 供研读） |

---

## 各项目许可证全文

- **Thonny（MIT）**：见 `examples/thonny/LICENSE`
- **IDLE（PSF License v2）**：见 `examples/idle/LICENSE`
- **pygubu-designer（GPL-3.0）**：见 `examples/pygubu-designer/LICENSE`
- **Tkinter-Designer（BSD-3-Clause）**：见 `examples/tkinter-designer/LICENSE`

## 使用注意

- **Thonny / IDLE**：以原样提供，仅作参考学习；如需在其基础上二次开发，请遵循各自许可证。
- **pygubu-designer（GPL-3.0）**：GPL 具有 **copyleft 传染性**——基于其代码的衍生作品必须以 GPL 发布。请勿将其代码并入 MIT 许可的独立项目中；如需使用其功能，建议作为独立进程/子进程调用，或在 GPL 许可下另行分发。
- **Tkinter-Designer（BSD-3-Clause）**：允许以原样或修改形式再分发，需保留版权声明。

---

如有疑问，欢迎在 Issues 中指出，我们会及时修正标注。
