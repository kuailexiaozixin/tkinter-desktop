# pywin32 离线文档全集

本目录是 **pywin32 全部公开文档的离线镜像**，所有内容均已提取为纯文本 Markdown，
**不含任何"请访问某网址"式的占位引用**，离线大模型可直接阅读、检索、处理。

## 覆盖来源

| 来源 | 处理方式 |
| --- | --- |
| https://github.com/mhammond/pywin32 | 仓库 27 个 md/txt 文档 + 27 个仓库内 HTML 文档（COM 教程、Pythonwin 文档、win32 help）+ 161 个官方示例 `.py` 源码，**全部全文内联** |
| https://pypi.org/project/pywin32/ | 发布页全文（版本、维护者、许可、分类器、Python 版本要求） |
| https://mhammond.github.io/pywin32/ | **整站 6771 个 HTML 页面全量抓取并转 Markdown**（模块、对象、常量、专题页，逐页正文内联） |
| https://gitcode.com/Universal-Tool/57b6b | 仓库说明全文。该仓库正文仅有 README，主体是二进制 `PyWin32帮助文档大全.rar`，无法文本化；其涵盖的 win32gui/win32api/win32con 内容已由上面三个来源完整覆盖 |

## 目录结构

| 目录 | 文件数 | 体积 | 内容 |
| --- | --- | --- | --- |
| `00-sources/` | 4 | 18 KB | 四个指定来源页（GitHub / PyPI / 官方文档站 / GitCode） |
| `01-repo-docs/` | 61 | 1134 KB | 仓库随附文档 + 官方示例源码全文 |
| `02-modules/` | 54 | 1072 KB | 模块参考（每模块一卷，含全部函数/方法正文） |
| `03-objects/` | 18 | 1182 KB | 对象参考（按首字母分卷，含全部方法/属性正文） |
| `04-constants/` | 23 | 236 KB | 常量参考（按模块分组） |
| `05-overviews/` | 15 | 212 KB | 专题/教程/杂项页面 |
| **合计** | **175** | **3853 KB** | 源自 **6771** 个文档页面 |

## 检索指引（给离线模型）

- 找 **函数/API**（如 `win32api.MessageBox`、`win32gui.FindWindow`）→ `02-modules/<模块名>.md`，
  文件内按 `<!-- page: 模块__函数_meth.html -->` 分节，直接搜函数名即可。
- 找 **对象/句柄/COM 接口**（如 `PyHANDLE`、`PyIDispatch`、`PyCWnd`）→ `03-objects/objects-*.md`，
  `Py` 开头的普通对象在 `objects-Py.md`，COM 接口在 `objects-PyI.md`，Win32 结构体按首字母分卷。
- 找 **常量**（如 `WM_CLOSE`、`SW_MAXIMIZE`）→ `04-constants/constants-<模块>.md`。
- 找 **可运行示例** → `01-repo-docs/demos__*.md`（官方 Demos 全文，含服务、COM、Shell、ISAPI、Pythonwin 等）。
- 找 **COM 编程教程** → `01-repo-docs/htmldoc__com__win32com__HTML__*.md`
  （客户端/服务端快速上手、makepy 生成支持、VARIANT、COM Records 等；这批文档在官网已 404，本镜像从仓库补录）。
- 找 **Pythonwin / 调试器文档** → `01-repo-docs/htmldoc__pythonwin__doc__*.md`。
- 找 **安装/构建/版本变更** → `01-repo-docs/README.md`、`build_env.md`、`CHANGES.md`、`NOGIL.md`。
- 交叉引用：正文中原本的站内超链接已转为纯文本符号名（如 `win32api::CloseHandle`、`PyHANDLE::Close`），
  直接全文检索该符号即可定位到对应章节，**不存在需要联网才能打开的链接**。
- 边界说明：官网自身有 404 死链，逐条核对结果见 `05-overviews/_missing-pages.md`。

## 模块清单（54 个）

| 模块 | 成员页数 | 体积 |
| --- | --- | --- |
| `win32gui` | 339 | 152 KB |
| `win32api` | 205 | 150 KB |
| `win32file` | 140 | 97 KB |
| `win32ui` | 115 | 41 KB |
| `pythoncom` | 96 | 48 KB |
| `win32security` | 84 | 50 KB |
| `win32net` | 66 | 56 KB |
| `shell` | 58 | 33 KB |
| `win32process` | 50 | 28 KB |
| `win32print` | 47 | 25 KB |
| `win32crypt` | 42 | 31 KB |
| `win32evtlog` | 42 | 24 KB |
| `win32inet` | 37 | 36 KB |
| `win32service` | 34 | 19 KB |
| `exchange` | 23 | 9 KB |
| `win32event` | 23 | 13 KB |
| `win32pdh` | 21 | 11 KB |
| `mapi` | 20 | 8 KB |
| `win32clipboard` | 20 | 27 KB |
| `win32console` | 20 | 8 KB |
| `propsys` | 19 | 9 KB |
| `win32ts` | 19 | 12 KB |
| `win32cred` | 18 | 11 KB |
| `win32pipe` | 17 | 10 KB |
| `_winxptheme` | 15 | 11 KB |
| `pywintypes` | 15 | 5 KB |
| `servicemanager` | 15 | 6 KB |
| `win32wnet` | 14 | 10 KB |
| `win32ras` | 13 | 11 KB |
| `isapi.install` | 12 | 6 KB |
| `win32profile` | 11 | 5 KB |
| `win32uiole` | 11 | 3 KB |
| `directsound` | 10 | 3 KB |
| `win32help` | 9 | 12 KB |
| `win32job` | 8 | 5 KB |
| `adsi` | 7 | 3 KB |
| `win32transaction` | 7 | 4 KB |
| `axcontrol` | 5 | 4 KB |
| `perfmon` | 5 | 2 KB |
| `win32lz` | 5 | 3 KB |
| `win32timezone` | 4 | 12 KB |
| `internet` | 3 | 1 KB |
| `odbc` | 2 | 1 KB |
| `timer` | 2 | 1 KB |
| `mmapfile` | 1 | 2 KB |
| `axdebug` | 0 | 0 KB |
| `axscript` | 0 | 0 KB |
| `dde` | 0 | 0 KB |
| `isapi` | 0 | 0 KB |
| `isapi.isapicon` | 0 | 0 KB |
| `isapi.simple` | 0 | 1 KB |
| `isapi.threaded_extension` | 0 | 0 KB |
| `sspi` | 0 | 1 KB |
| `win32com.authorization.authorization` | 0 | 0 KB |

## 对象分卷

| 文件 | 对象数 | 体积 |
| --- | --- | --- |
| `objects-C.md` | 11 | 8 KB |
| `objects-D.md` | 2 | 1 KB |
| `objects-E.md` | 7 | 11 KB |
| `objects-F.md` | 2 | 1 KB |
| `objects-H.md` | 8 | 5 KB |
| `objects-I.md` | 5 | 8 KB |
| `objects-L.md` | 3 | 2 KB |
| `objects-M.md` | 1 | 1 KB |
| `objects-N.md` | 3 | 2 KB |
| `objects-P.md` | 3 | 1 KB |
| `objects-Py.md` | 298 | 572 KB |
| `objects-PyI.md` | 238 | 476 KB |
| `objects-R.md` | 3 | 2 KB |
| `objects-S.md` | 12 | 9 KB |
| `objects-T.md` | 5 | 4 KB |
| `objects-U.md` | 1 | 0 KB |
| `objects-V.md` | 1 | 1 KB |
| `objects-W.md` | 3 | 13 KB |

## 常量分组

| 文件 | 常量数 | 体积 |
| --- | --- | --- |
| `constants-mapi.md` | 255 | 32 KB |
| `constants-win32security.md` | 228 | 27 KB |
| `constants-win32file.md` | 198 | 27 KB |
| `constants-win32ui.md` | 194 | 22 KB |
| `constants-win32evtlog.md` | 175 | 19 KB |
| `constants-win32help.md` | 168 | 17 KB |
| `constants-win32service.md` | 101 | 15 KB |
| `constants-isapi.isapicon.md` | 84 | 12 KB |
| `constants-axdebug.md` | 66 | 8 KB |
| `constants-win32job.md` | 61 | 8 KB |
| `constants-win32gui.md` | 55 | 4 KB |
| `constants-directsound.md` | 48 | 11 KB |
| `constants-win32process.md` | 44 | 11 KB |
| `constants-internet.md` | 36 | 4 KB |
| `constants-win32ras.md` | 31 | 4 KB |
| `constants-win32event.md` | 28 | 3 KB |
| `constants-axcontrol.md` | 22 | 2 KB |
| `constants-win32pipe.md` | 16 | 2 KB |
| `constants-win32uiole.md` | 11 | 1 KB |
| `constants-exchange.md` | 5 | 1 KB |
| `constants-.md` | 4 | 0 KB |
| `constants-isapi.threaded.md` | 3 | 0 KB |
| `constants-win32timezone.md` | 1 | 0 KB |

## 专题文档

- `objectmodmethods.md`（126 KB）
- `ASP_and_Python.md`（9 KB）
- `Windows_NT_Eventlog_and_Threading.md`（8 KB）
- `win32com.shell_and_Windows_Shell_Links.md`（7 KB）
- `Python.2c_C.2b.2b.2c_and_COM.md`（6 KB）
- `Windows_NT_Files_.2d.2d_Locking.md`（6 KB）
- `Windows_NT_Eventlog.md`（6 KB）
- `MTS_and_Python_for_NT.md`（5 KB）
- `Keyboard_Bindings.md`（4 KB）
- `Windows_NT_Security_.2d.2d_Impersonation.md`（3 KB）
- `DirectSound_examples.md`（3 KB）
- `Recursive_directory_deletes_and_special_files.md`（2 KB）
- `Tabs_and_indentation_in_the_editor.md`（2 KB）
- `_misc-pages.md`（其余 26 个短页合集）

---

抓取时间：2026-08-01。文档站为 Autoduck 生成的静态 HTML，本镜像逐页转换，保留原始层级与交叉引用关系。

---
