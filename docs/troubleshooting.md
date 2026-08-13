# 常见错误与解决方案

> 按报错/症状检索。每条：现象 → 本质 → 解法。

## 布局与控件

**`_tkinter.TclError: cannot use geometry manager grid inside ... which already has slaves managed by pack`**
本质：同一容器内混用 pack 和 grid。解法：一个容器只用一种几何管理器；检查是不是把子控件 grid 到了用 pack 的父容器。

**窗口拉大后内容不动，右侧/下方大片空白**
本质：容器未配置行列权重。解法：给伸缩行列加 `rowconfigure/columnconfigure(weight=1)`，控件 `sticky="nsew"`。

**`_tkinter.TclError: unknown option "-bg"`（或 -fg/-relief 等）**
本质：给 ttk 控件传了经典 tk 选项。ttk 外观走样式系统。解法：`ttk.Style().configure("Custom.TButton", background=...)` 并 `style="Custom.TButton"`；或该属性本主题不可改（见下条）。

**ttk.Style configure 了颜色但界面没变化**
本质：vista/xpnative 等原生主题的许多元素由系统绘制，颜色不可覆盖。解法：`style.theme_use("clam")` 后再定制。

**Treeview 行高太小导致字体截断/遮掩/行紧叠（ttk 应用普遍问题）**

- **现象**：Treeview 行与行间距极小，文字上下被裁切、行与行之间几乎贴在一起，中文/长文本/下行字母（gjpqy）显示不全或互相覆盖。高 DPI（125%/150%）下更严重。截图典型症状：列表看似有数据但每行只能看到半截字。
- **本质**：ttk Treeview 默认 `rowheight=20`，这个值是 Tk 为 96DPI 英文环境（小字号、无下行字母延伸）设计的硬编码。中文方块字本身更高、下行字母需要 descent 空间、高 DPI 下字体放大但 rowheight 不跟随 → 行高 < 字体实际渲染高度 → 文字被裁切。
- **解法**：禁止使用默认值。必须用 `font.metrics('linespace')` 根据实际字体计算：
  ```python
  import tkinter.font as tkfont
  _font = tkfont.Font(family="Microsoft YaHei UI", size=10)
  style.configure("Treeview", rowheight=_font.metrics("linespace") + 8)  # 舒适模式 +8px
  ```
  正式项目应调用 `setup_treeview_rowheight()` 函数（含四档模式对照表）。完整公式/函数/症状表/反模式/自查清单见 `references/03-ui-design.md` §5.1~5.4 及 §11~12。
- **列宽同理**：默认列宽也不适配中文长文本，必须 `tree.column(cid, width=...)` 显式设置。

**图片 Label 显示空白**
本质：PhotoImage 被垃圾回收。解法：保持引用 `label.image = img`。

**菜单第一项是一条虚线**
本质：Tk 历史遗留 tearoff。解法：`tk.Menu(parent, tearoff=False)`。

**`grab failed: window not viewable`**
本质：Toplevel 尚未显示就 `grab_set()`。解法：先 `wait_visibility()` 再 grab；顺序 `transient → wait_visibility → grab_set`。

## 线程与事件

**偶发 `RuntimeError: main thread is not in main loop` / `Tcl_AsyncDelete` / 无提示闪退**
本质：子线程碰了 widget 或 tk 变量。解法：worker 只算不画，结果经 queue，主线程 after 轮询（见 05-threading-and-async.md）。

**界面点了没反应、卡死几秒**
本质：耗时操作写在事件回调里，阻塞了 mainloop。解法：>100ms 的操作移到 worker 线程。

**关闭窗口后报 `invalid command name "...tick"`**
本质：after 定时器在窗口销毁后触发。解法：保存 after id，`WM_DELETE_WINDOW` 处理器里 `after_cancel`。

**`TclError: no display` （CI/无显示环境）**
本质：Tk 需要图形会话，withdraw 也不能免。解法：该环境只跑 Model 层测试；GUI 冒烟放在有桌面的机器跑。

**View 渲染报 `KeyError: 'xxx'`，且只在选中行/切页联动时出现**
本质：View 层取行字典的字段名与数据库 schema 列名不一致（如臆写 `seq`/`name`，实际列是 `node_id`/`node_name`）。单元测试测不到 View，只有无头 GUI 冒烟里触发 `<<TreeviewSelect>>` 联动才会暴露。解法：View 取字段前先 `grep "CREATE TABLE"` 核对列名；冒烟脚本必须覆盖"选中主表行→从表联动"路径。

**冒烟脚本等待 worker+after 任务时卡死或报 `wrong # args: should be "after idle script"`**
本质：`root.after(20)`（无回调）会阻塞消息泵、`root.tk.call("after","idle")` 参数不合法——都不是驱动事件循环的正确姿势。解法：轮询循环固定写法 `while busy: root.update(); time.sleep(0.02)`——`update()` 才会执行到期的 after 回调。

## 数据层

**`sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread`**
本质：连接跨线程复用。解法：worker 内新开连接，或 DB 操作留主线程。

**外键约束不生效，孤儿数据出现**
本质：sqlite 外键默认关闭。解法：每个连接 `PRAGMA foreign_keys = ON`。

**打包后数据重启即丢**
本质：数据库写进了 _MEIPASS 临时目录。解法：可写路径基于 `sys.executable` 同级（07-project-structure.md）。

**测试/冒烟用环境变量覆盖数据目录，结果数据落到了 `<盘符>:\tmp\...`**
本质：从 Git Bash 传 `MYAPP_DB_DIR=/tmp/xxx` 给 Windows Python，`Path("/tmp/xxx")` 被解析为**当前盘符根目录**下的 `\tmp\xxx`，不是 bash 的 /tmp。解法：给 Windows 进程传环境变量一律用 Windows 绝对路径（如 `$(cygpath -w "$dir")` 或 PowerShell 里生成）。

## 打包

**EXE 一闪即退，无任何提示**
本质：--windowed 下启动期异常无处显示。解法：先出 --console 调试版看栈；正式版必须挂 excepthook 写日志 + messagebox。

**`AttributeError: 'NoneType' object has no attribute 'write'`**
本质：--windowed 下 print / stderr 输出。解法：全走 logging；入口兜底 stdout/stderr 为 StringIO。

**`Can't find a usable init.tcl`**
本质：非标准 CPython（嵌入式/精简版）缺 Tcl 资源，PyInstaller 收集不到。解法：用 python.org 标准安装版重建 venv 打包。

**`ModuleNotFoundError`（冻结后才报）**
本质：动态 import 让静态分析漏收。解法：`--hidden-import 模块名`；入口用顶层 launcher.py + `--paths src` 防相对导入问题。

**任务栏图标不是我的图标**
本质：进程缺 AppUserModelID，Windows 按引导器归组。解法：Tk() 前 `SetCurrentProcessExplicitAppUserModelID`；窗口图标另用 `iconbitmap`。

**杀毒误报**
本质：--onefile 自解压行为特征像壳。解法：--noupx → 最小 venv → 必要时 --onedir + zip → 代码签名。

## 打包相关的「死重」误收（体积异常排查）

> 以下四类是打包后 EXE 体积莫名变大的典型原因，本质都是「PyInstaller 静态扫描误收了运行期根本用不到的依赖」。统一原则：**默认 `--exclude-module` 拒绝、未来真用到再 `--hidden-import` 放行（默认关、不禁止）**。机制与 opt-in 命令见 `references/08-packaging.md`。

**`启动.bat` 中文乱码 / 命令被拆成碎片**
本质：.bat 编码链不一致——① UTF-8 带 BOM 让首行 `@echo off` 变 `锘緺echo off` 报「不是内部或外部命令」；② 仅 LF 换行让 `>`/`=` 被当换行，把 `chcp 65001 >nul` / `set PYTHONUTF8=1` 拆成 `65001` / `ONUTF8` 碎片；③ 含中文的 .bat 存成 UTF-8 而非 GBK，控制台 OEM 代码页解析中文路径/注释乱码。解法：含中文的 .bat 存 **GBK(CP936/ANSI 中文) + CRLF + 无 BOM**；纯 ASCII 的 .bat 可 UTF-8 无 BOM；开头加 `chcp 65001 >nul` + `set PYTHONUTF8=1`。参考实现：`examples/idle/启动.bat`、`examples/thonny/启动.bat`。

**PIL（Pillow）被静默拖入 EXE（约占 21% / 5MB）**
本质：pygubu 核心 `pygubu.builder` 顶层硬依赖 `pygubu.stockimage`，其内 `from PIL import Image, ImageTk` 是惰性导入（仅加载 stock 图片时执行），却被 PyInstaller 静态扫描收进包；第三方插件 `ttkwidgets` / `customtkinter` 也 `import PIL` 并随 `PluginManager` 全量加载。本项目 `.ui` 不用 stock 图片、也不用需 PIL 的插件，PIL 纯死重。解法：默认 `--exclude-module=PIL` + `--exclude-module=pygubu.plugins.ttkwidgets` + `--exclude-module=pygubu.plugins.customtkinter`；核心 `pygubu` 仍 `--hidden-import` 保留。排除安全：惰性分支永不被触发。未来用到 stock 图片/需 PIL 插件时，删 `--exclude-module=PIL` 并补 `--hidden-import=PIL`（默认关、不禁止）。

**pygubu-designer / 插件被拖入 EXE（纯死重，甚至 +26MB）**
本质：`pygubudesigner` 只是开发期可视化编辑器，运行期只用 `pygubu.Builder` 加载 `.ui`；它的依赖链（autopep8 / Mako / numpy…）与运行期无关。若误加 `--hidden-import=pygubudesigner`，会把一整条开发依赖链冻结进 EXE（实测凭空 +26MB）。解法：**只** `--hidden-import=pygubu`（运行期加载器），严禁 hidden-import designer；标准插件 `pygubu.plugins.tk/.ttk/.pygubu.*` 保持默认收集（轻量、Builder 必需）。

**cryptography 被静默拖入 EXE（约占 27% / 最大类）**
本质：Tkinter + `requests` 的 HTTPS 走 `requests → urllib3 → ssl`（Python 标准库），运行期根本不 import `cryptography`。但 PyInstaller 静态扫描触发其运行时钩子 `pyi_rth_cryptography_openssl`，把整包（尤其 `cryptography\hazmat\bindings\_rust.pyd` ~3.4MB + `bcrypt._bcrypt.pyd`）冻结进来——实测在解释器里 block 掉 cryptography 后 `requests.get('https://...')` 仍返回 200，纯死重。解法：默认 `--exclude-module=cryptography --exclude-module=bcrypt`；注意 `libcrypto` / `libssl` 两个 DLL 仍随标准库 `_ssl` 保留、TLS 不受影响（体积工具里看到 "cryptography" 分类，往往只是这两个 DLL 被归类名误命中，非真包）。未来真要做自签证书校验/加解密时，删排除并补 `--hidden-import=cryptography`（默认关、不禁止）。

## 高 DPI

**高分屏整个界面模糊**
本质：进程未声明 DPI 感知，系统位图拉伸。解法：Tk() 前 `SetProcessDpiAwareness(1)`。

**声明 DPI 感知后字变小**
本质：系统不再代为放大。解法：统一改 named fonts 大小（03-ui-design.md 中文字体节）。
