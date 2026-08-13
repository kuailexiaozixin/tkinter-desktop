# 08 打包（PyInstaller × Tkinter 专项）

> Tkinter 打包比 Web 桌面壳简单得多：无 hidden-import 长名单、无 WebView2 DLL、
> 无端口/路由问题。但有自己的一套专属坑与可选项：windowed-stdout、Tcl 资源、图标、
> 误报，以及本篇新增的——**版本信息注入**、**非标准 Python 的 DLL 依赖链**、
> **受限/沙箱环境构建**、**`.spec` 文件的 CLI 陷阱**、**第三方美化库打包**。
>
> 本篇整合了 PyInstaller 打包的进阶要点。

---

## 标准命令（在项目专用 venv 中执行）

```powershell
.venv\Scripts\python.exe -m PyInstaller --noconfirm --clean `
  --onefile --windowed `
  --noupx `
  --name MyTool `
  --paths src `
  --icon assets\app.ico `
  --version-file version_info.txt `
  --add-data "assets;assets" `
  src\launcher.py
```

| 参数 | 说明 |
| ---- | ---- |
| `--onefile` | 单文件 EXE。验收：`dist/` 下无 `_internal/` |
| `--windowed` | GUI 无控制台。**调试版先用 `--console` 定位问题再切换** |
| `--noupx` | 禁用 UPX。UPX 是杀毒误报头号元凶，且对 Python 应用收益极低 |
| `--paths src` | 让 PyInstaller 找到 src 下的包（配合 `launcher.py` 顶层入口） |
| `--icon` | EXE 文件图标（.ico，含 16/32/48/256 多尺寸最佳）。窗口/任务栏图标另需在运行时 `root.iconbitmap` + `AppUserModelID` |
| `--version-file` | **EXE 右键属性的版本信息**（见下节） |
| `--add-data "assets;assets"` | 只读资源；Windows 分隔符是 **分号** |

Tcl/Tk 运行时（`tcl86t.dll`、`tk86t.dll`、tcl/tk 资源目录）由 PyInstaller
**自动收集**，不需要手动处理——前提是用官方 python.org 的 CPython。
（部分精简发行版/嵌入式 Python 缺 Tcl 资源，打包后报
`Can't find a usable init.tcl`，解法：换标准 CPython 构建；Conda 见下文「DLL 依赖链」）

---

## 四个专属坑（必读）

### 1. `--windowed` 下 stdout/stderr 为 None
`print()` 直接 `AttributeError: 'NoneType' object has no attribute 'write'`。
规则：交付代码零 print，全走 logging 文件；第三方库往 stderr 写也会炸，
保险起见入口处兜底：

```python
import sys, io
if sys.stdout is None: sys.stdout = io.StringIO()
if sys.stderr is None: sys.stderr = io.StringIO()
```

### 2. 窗口图标与任务栏图标是两回事
- EXE 文件图标：`--icon app.ico`
- 窗口左上角图标：运行时 `root.iconbitmap(resource_path("assets/app.ico"))`
  （.ico 必须 `--add-data` 打进去，用 `sys._MEIPASS` 取）
- 任务栏分组图标：再加
  `ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("company.mytool")`
  （在 `Tk()` 之前调用），否则任务栏可能仍显示 PyInstaller 引导器默认图标

### 3. 数据写到 _MEIPASS（只读临时区）
症状：程序看似正常，重启后数据全丢。原因：用 `__file__`/`_MEIPASS` 派生了
DB/日志路径。规则重申：**可写数据一律基于 `sys.executable` 同级**（见 07 config）。
口诀：**只读找 `_MEIPASS`，要写找 `sys.executable.parent`**。

### 4. 杀毒软件误报
`--onefile` 自解压模型易被 Windows Defender/国产杀软标记。缓解顺序：
① 保持 venv 最小化（越少 DLL 越少误报）→ ② 不加 UPX（`--noupx`）→
③ 仍误报则改 `--onedir` 交付 zip（例外场景，需在交付说明中注明原因）→
④ 企业分发考虑代码签名（见末节）。

---

## 版本信息与元数据注入

交付的 EXE 应在「右键 → 属性 → 详细信息」展示规范的版本信息，且程序内部能读到
构建元数据（关于页/日志）。两者需与 `pyproject` 的 `version` 保持一致。

### version_info.txt（Windows 文件属性）

`version_info.txt` 不是 JSON/YAML，而是 PyInstaller 专用的 **VSVersionInfo** 格式。
可用自带工具抓取模板再手工改字段：

```bash
.venv\Scripts\python.exe -m PyInstaller.utils.cli.grab_version > version_info.txt
# 或从已有 EXE 提取：... grab_version existing_app.exe
```

```python
# version_info.txt
VSVersionInfo(
  ffi=FixedFileInfo(filevers=(1, 0, 0, 0), prodvers=(1, 0, 0, 0),
                    mask=0x3f, flags=0x0, OS=0x40004, fileType=0x1,
                    subtype=0x0, date=(0, 0)),
  kids=[
    StringFileInfo([StringTable('040904B0', [
      StringStruct('CompanyName', 'My Company'),
      StringStruct('FileDescription', 'My Application'),
      StringStruct('FileVersion', '1.0.0'),
      StringStruct('InternalName', 'MyApp'),
      StringStruct('LegalCopyright', 'Copyright 2025 My Company'),
      StringStruct('OriginalFilename', 'MyApp.exe'),
      StringStruct('ProductName', 'MyApp'),
      StringStruct('ProductVersion', '1.0.0')])]),
    VarFileInfo([VarStruct('Translation', (1033, 1200))])
  ]
)
```

注入：命令行 `--version-file version_info.txt`，或在 `.spec` 的 `EXE(..., version='version_info.txt')`。

### build_info.json（程序内部构建元数据）

打包前动态生成，随 `--add-data` 打进资源；程序启动时读取用于「关于」展示/日志。

```json
{ "version": "1.0.0", "build_datetime": "2025-11-13T10:00:00",
  "build_platform": "Windows-10", "python_version": "3.13.0" }
```

```python
# scripts/generate_build_info.py（打包前运行，输出到 src/<pkg>/config/build_info.json）
import json, platform
from datetime import datetime
from pathlib import Path

def generate_build_info(version: str, out: Path):
    info = {"version": version, "build_datetime": datetime.now().isoformat(),
            "build_platform": platform.platform(),
            "python_version": platform.python_version()}
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(info, indent=2, ensure_ascii=False), encoding="utf-8")
```

读取（兼容打包前后，`RESOURCE_DIR` 见 07 config 的 `sys.frozen` 分支）：

```python
import json, sys
from pathlib import Path
if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    base = Path(sys._MEIPASS)
else:
    base = Path(__file__).resolve().parent
p = base / "config" / "build_info.json"
build_info = json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}
```

### 版本一致性原则

- `version_info.txt`、`build_info.json` 与 `pyproject`/`__version__` 三者 **必须同步**
- 遵循 **SemVer**（`MAJOR.MINOR.PATCH`）
- 每次发布同步更新 `CHANGELOG.md`（Keep a Changelog 标准）

---

## 体积控制与 excludes

- **必须最小 venv 打包**：全局环境打包动辄 150MB+，干净 venv 的纯标准库
  Tkinter 应用约 11~15MB
- 检查手段：打包前 `pip list` 审查；venv 里只应有 `pyinstaller` + 实际业务依赖
- 用了 pandas 才处理它的 exclude/hook，纯标准库项目无需任何 exclude
- **可安全排除**（在 `.spec` 的 `Analysis(excludes=[...])` 或用 `--exclude-module`）：
  `unittest`、`pydoc`、`test`、`distutils`、`email`、`http.server`、`xmlrpc`、`pdb`、`inspect`
- **严禁排除 `pip` / `wheel` / `setuptools`**：某些 setuptools 钩子依赖它们，
  排除会导致 `PackageNotFoundError` 或钩子冲突

---

## 非标准 Python / Conda 的 DLL 依赖链

如果用 **Conda/Anaconda** 的 Python 而非官方 python.org 版本，PyInstaller 常漏打包
Conda 私有目录里的 DLL，导致运行期 `ModuleNotFoundError` / `OperationalError`。
Tkinter 项目尤其要注意：`_tkinter.pyd` 与 `_sqlite3.pyd` 都依赖 Conda `Library/bin` 的 DLL。

| 缺失 DLL | 症状 | 关联模块 | 修复（--add-binary） |
| -------- | ---- | -------- | -------------------- |
| `_tkinter.pyd` + `tcl86t.dll` + `tk86t.dll` | `import tkinter` 失败 / `Can't find init.tcl` | tkinter 标准库 | `--add-binary "path\to\_tkinter.pyd;."` + 同目录 `tcl86t.dll`/`tk86t.dll` + tcl/tk 资源 |
| `_sqlite3.pyd` + `sqlite3.dll` | `sqlite3.OperationalError: no such module: _sqlite3` | sqlite3 标准库 | `--add-binary "path\to\_sqlite3.pyd;."` + 同目录 `sqlite3.dll` |
| `_ctypes.pyd` + `ffi-8.dll` | `module 'ctypes' has no attribute 'CDLL'` | ctypes 标准库（DPI/AppUserModelID 用到） | `--add-binary "path\to\_ctypes.pyd;."` + `ffi-8.dll` |

> **首选方案**：直接用官方 CPython 构建 venv，可彻底回避上述全部问题。
> 若必须用 Conda 环境，推荐在 `.spec` 的 `binaries` 列表显式添加，而非命令行 `--add-binary`（更可控、可重复），并逐个 DLL 添加后重测。

诊断脚本（定位缺失 DLL）：

```python
import sys
from pathlib import Path
bin_dir = Path(sys.base_prefix) / "Library" / "bin"   # Conda 路径
for dll in ["tcl86t.dll", "tk86t.dll", "sqlite3.dll", "ffi-8.dll"]:
    p = bin_dir / dll
    print(f"[{'OK' if p.exists() else 'MISS'}] {dll} -> {p}")
```

---

## 第三方美化库打包

引入第三方增强库（如 tksheet / tkchart）后会引入
**运行期第三方依赖**，打包需额外处理。详见 `references/03-ui-design.md`（§10 可选增强）。要点：

- **纯元数据发行包（罕见）**：个别包只有元数据无代码，运行期
  `importlib.metadata.version()` 会 `PackageNotFoundError`，需
  `--additional-hooks-dir` 放 `copy_metadata("pkgname")` 钩子（见 PyInstaller 文档）

### 裁剪优于全量收集（高级）

对含大量子模块的大包，**优先用精确的 `hiddenimports` + `excludes` 掉未用 provider/TUI**，
而非无脑 `--collect-submodules big_pkg`（会膨胀体积并可能触发沙箱资源上限）。

### 可选依赖被 try/except 静默导入的陷阱

有些库在 `try: import x` 里静默导入可选 backend；缺失时**进程照常启动却悄悄少功能**。
排查：运行目标程序后查日志，搜 `not installed` / `not available` / `No adapter`，
定位后在 venv 安装并在 `hiddenimports` 显式加入。

### 误把「设计器 / 开发期」包 hidden-import 进 EXE 的陷阱

pygubu 路线下，`pygubu-designer`（发行名 `pygubudesigner`）只是**开发期可视化编辑器**，
运行期只用 `pygubu.Builder` 加载 `.ui`。**切勿**加 `--hidden-import=pygubudesigner`。

- **为什么危险**：该包会把整个 designer 闭包冻结进 EXE；其中一条 import 链会触达
  `setuptools._distutils.compat.numpy` 这个 distutils 兼容垫片，它**重新导出真实 numpy
  整包**（含 `numpy.libs` 约 26MB），从而把 numpy 静默打进 EXE——而运行期根本用不上，
  纯死重，体积凭空 +26MB。
- **隐蔽性**：`pygubu-designer` 自身的 `Requires` 并不含 numpy（autopep8/Mako/pygubu/screeninfo…
  都不依赖 numpy），所以这是「隐式传递 + setuptools 垫片」导致的隐蔽膨胀，光看 `pip show` 看不出来。
- **正确做法**：只 hidden-import `pygubu`（运行时加载器）。若仍担心某条链误拖 numpy，
  显式加 `--exclude-module=numpy` 作为安全网（注意：`setuptools`/`pip`/`wheel` 本身**严禁** exclude）。
- **通用原则**：任何 `--hidden-import` 都要先问一句「运行期真的 import 它吗？」。把「开发期工具」
  当运行时依赖冻结，是 PyInstaller 体积爆炸的最常见原因之一。

### pygubu 默认排除 PIL 与第三方插件（避免重型依赖被拖入）

> 排障视角（现象/本质/解法）见 `docs/troubleshooting.md` 打包节「PIL 被静默拖入 EXE」「pygubu-designer / 插件被拖入 EXE」。

承接上节：即便只 hidden-import `pygubu`（不加 designer），EXE 仍可能被塞进 **Pillow/PIL**
（本项目实测约占 21% 体积）。根因在 pygubu 自己的内部依赖，与 designer 无关。

- **真正的 PIL 来源**：`pygubu.builder` 在顶层 `from .stockimage import StockImage`
  （`pygubu/builder.py:10`），硬依赖 `pygubu.stockimage`；而 `pygubu/stockimage/registry.py`
  在函数内部惰性写 `from PIL import Image, ImageTk`（仅当真正加载 stock 图片时才执行）。
  PyInstaller 的静态扫描会把这行 import 收进 EXE，于是 PIL 被静默拖入——尽管项目运行期根本不
  加载任何 stock 图片。这是「核心库里一段惰性 import 被打包器误收」的典型死重。
- **第三方插件雪上加霜**：`pygubu.plugins.ttkwidgets` / `pygubu.plugins.customtkinter` 也会
  `from PIL import ...`；它们经 `PluginManager.load_plugins()` 在启动时全量 import，进一步把 PIL
  及其重型依赖拉进来。
- **默认做法（默认关、不禁止）**：
  ```
  --hidden-import=pygubu            # 核心必需：运行期 Builder 加载 .ui
  --exclude-module=PIL              # 核心里的惰性 PIL import 不触发，安全剔除
  --exclude-module=pygubu.plugins.ttkwidgets
  --exclude-module=pygubu.plugins.customtkinter
  ```
  `pygubu.plugins.tk` / `pygubu.plugins.ttk`（标准 ttk/tk 控件定义，Builder 必需）与
  `pygubu.plugins.pygubu.*`（内置扩展控件如 ScrolledFrame，轻量无重型依赖）保持默认收集，
  不影响体积。
- **为什么排除 PIL 是安全的**：`pygubu.stockimage` 顶层 import 不碰 PIL；`from PIL ...` 只在
  「加载 stock 图片」这个函数里执行。本项目 `.ui` 不用 stock 图片、也不用了需 PIL 的插件控件，
  该惰性分支永不运行，故 EXE 启动/加载 `.ui` 都不会触及 PIL。
- **开启（未来需要某插件/stock 图片时）**：若 `.ui` 用到了 pygubu stock 图片，或需 PIL 的插件
  控件（如 ttkwidgets.Calendar、CTkTabview），**删掉 `--exclude-module=PIL`** 并补
  `--hidden-import=PIL`（如用到对应插件，再删掉该插件的 `--exclude-module` 并补
  `--hidden-import=pygubu.plugins.<插件>`）。不要一刀切禁止——按项目实际用到的控件取舍。
- **通用原则**：`pygubu` 核心属于「运行期」，其 **第三方插件** 与 **惰性重型依赖（PIL）** 属于
  「按需」；用 `--exclude-module` 做默认拒绝、用 `--hidden-import` 做按需放行。

### 默认排除 cryptography（HTTPS 走标准库 ssl，避免 ~27% 死重）

> 排障视角（现象/本质/解法）见 `docs/troubleshooting.md` 打包节「cryptography 被静默拖入 EXE」。

Tkinter + `requests` 桌面应用的 HTTPS 请求，实际由 Python 标准库 `ssl` 完成
（`requests → urllib3 → ssl`），**运行期根本不 import `cryptography` / `OpenSSL` / `pyOpenSSL`**。

- **实测证明**：在解释器里用 meta-path finder 拦截 `cryptography`/`OpenSSL`/`pyOpenSSL`/`bcrypt` 后，
  `requests.get('https://www.baidu.com')` 仍返回 200，全程无这些模块被 import。
- **为什么会被收进 EXE（死重）**：PyInstaller 静态扫描发现某条 import 链依赖 `cryptography`，于是触发
  它的运行时钩子 `pyi_rth_cryptography_openssl`，把整包（尤其是
  `cryptography\hazmat\bindings\_rust.pyd` 约 3.4MB 的 Rust 编译扩展 + `bcrypt._bcrypt.pyd`）冻结进来。
  本项目（announcement-downloader 实测）`cryptography` 占约 27% 体积，全是死重。
- **默认做法（默认关、不禁止）**：
  ```
  --exclude-module=cryptography
  --exclude-module=bcrypt       # 仅为 cryptography 的依赖
  ```
- **保留的部分（不要动）**：`libcrypto-3-x64.dll` / `libssl-3-x64.dll` 这两个 OpenSSL 动态库会随标准库
  `_ssl` 一起被 PyInstaller 收集，HTTPS/TLS 正是靠它们。排除 `cryptography` **不会**移除这两个 DLL，
  TLS 完全正常。若用 `inspect_exe` 之类工具仍看到 `cryptography` 分类，那通常只是 `libcrypto`/`libssl`
  被归类名（`crypto` 子串）误命中，属正常现象。
- **开启（未来需要 cryptography 时）**：若应用确实要做自签证书校验、对称/非对称加解密等，删掉
  `--exclude-module=cryptography`（及 `--exclude-module=bcrypt`）并补 `--hidden-import=cryptography`。
- **通用原则**：`cryptography` 对「走标准库 ssl 的 HTTPS 客户端」属于「按需」，用 `--exclude-module`
  做默认拒绝、用 `--hidden-import` 做按需放行——与 PIL 完全一致。

---

## 受限 / 沙箱环境构建

企业安全沙箱可能劫持 `os.remove`/`shutil.rmtree`，使 PyInstaller 反复清理
`build/`/`dist/`/`_MEIxxxx` 时中止构建。解法：把工作/产物/规格目录重定向到
沙箱允许写入的临时目录。

```python
import tempfile
from pathlib import Path
tmp = Path(tempfile.gettempdir()) / "pyinstaller_build"
tmp.mkdir(exist_ok=True)
PyInstaller.__main__.run([
    "src/launcher.py", "--onefile", "--windowed", "--noupx",
    "--workpath", str(tmp / "work"),
    "--distpath", str(tmp / "dist"),
    "--specpath", str(tmp / "spec"),
])
```

若沙箱连临时目录删除都禁止，则把三个 path 指到 `%LOCALAPPDATA%` 下的专用子目录，
并在构建前手动清理该目录。

---

## 使用 `.spec` 文件时的 CLI 陷阱

一旦命令传入一个 `.spec` 文件路径，PyInstaller 会**忽略所有 makespec 类 CLI 参数**并直接报错：

- `--onefile` / `--windowed` / `--console` / `--specpath` / `--upx` / `--upx-dir`
  全部非法 → `error: ... makespec options not valid when a .spec file is given`
- `--collect-submodules` / `--hidden-import` 等**可以**在 CLI 用，但既已写进 spec 的
  `hiddenimports`/`Analysis` 就无需重复

**正确做法**：用 `.spec` 驱动构建时，命令行只保留
`--clean --noconfirm --workpath --distpath <spec文件>`；`onefile`/`console`/`upx`
全部在 spec 内用 `EXE(..., upx=False, console=False)` 设定。

最小 spec 模板要点：

```python
exe = EXE(
    pyz, a.scripts, [],
    exclude_binaries=True,
    name='MyTool',
    debug=False,
    upx=False,            # 禁用 UPX（防误报）
    console=False,        # GUI 必须为 False
    icon='assets/app.ico',
    version='version_info.txt',
)
```

---

## 调试打包问题的正确姿势

1. 先 `--console` 版打包，直接看报错栈
2. 复杂问题设 `set PYINSTALLER_DEBUG=1` 或加 `--log-level DEBUG`
3. 运行期报缺模块 → `--hidden-import 模块名`（Tkinter 标准库项目极少需要；
   动态 import 的业务模块或刚引入的第三方美化库才会触发）
4. 确认无误后切回 `--windowed` 出正式版

---

## 代码签名（缓解杀软误报 · 企业分发）

`--noupx` 仍可能被未签名 EXE 误报。企业分发推荐用 `signtool` 数字签名：

```powershell
signtool sign /fd SHA256 /a /tr http://timestamp.digicert.com `
  /td SHA256 dist\MyTool.exe
```

---

## 构建脚本与门禁

统一走 `scripts/build_windows_exe.ps1`（本技能自带），流程：

```
pytest 全绿（非零退出即中止） → 无头 GUI 冒烟 → PyInstaller → 产物存在性检查
  → dist 无 _internal 检查 → EXE 冒烟（启动→窗口出现→优雅退出）
```

- **构建命令必须带大超时（>=600s）或后台运行**：--onefile 常超 120s
- EXE 冒烟最低标准：进程启动 5s 内不退出 + 出现顶层窗口。**注意**：Tkinter 窗口常不被
  `Get-Process` 识别为 `MainWindowTitle`（返回空），须用 `tasklist /fi "pid eq <id>" /v`
  探测真实窗口标题，并以启动日志兜底（详见 `scripts/build_windows_exe.ps1` 的 EXE 冒烟门禁）。
- 交付前把 `dist/*.exe` 拷到**无 Python 的干净目录**再双击一次（模拟用户环境）
- 推荐在打包流程里串联：生成 `build_info.json` → 打包 → 校验版本信息写入正确
