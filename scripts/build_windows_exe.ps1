# build_windows_exe.ps1 - Tkinter 应用打包（PowerShell 5.1 兼容）
# 用法: powershell -ExecutionPolicy Bypass -File build_windows_exe.ps1 `
#          -ProjectDir D:\work\my-tool -AppName MyTool [-IconPath assets\app.ico] [-ConsoleDebug]
param(
    [Parameter(Mandatory = $true)][string]$ProjectDir,
    [Parameter(Mandatory = $true)][string]$AppName,
    [string]$Entry = "src\launcher.py",
    [string]$IconPath = "",
    [string]$AddData = "",       # 例: "assets;assets"
    [string]$VersionFile = "version_info.txt",  # 存在则注入 EXE 版本信息
    [switch]$ConsoleDebug,       # 调试版: 带控制台
    [switch]$SkipTests
)

$ErrorActionPreference = "Stop"
$py = Join-Path $ProjectDir ".venv\Scripts\python.exe"
if (-not (Test-Path $py)) { throw "找不到 venv: $py（先跑 bootstrap_project.ps1）" }

Push-Location $ProjectDir
try {
    # ---- 门禁 1: pytest ----
    if (-not $SkipTests) {
        Write-Host "[1/5] pytest 门禁..."
        & $py -m pytest -q
        if ($LASTEXITCODE -ne 0) { throw "pytest 未全绿，禁止打包" }
    }

    # ---- 门禁 2: 无头 GUI 冒烟 ----
    $smoke = Join-Path $ProjectDir "scripts\smoke_test_gui.py"
    if (Test-Path $smoke) {
        Write-Host "[2/5] 无头 GUI 冒烟..."
        $env:PYTHONPATH = "src"
        & $py $smoke
        if ($LASTEXITCODE -ne 0) { throw "GUI 冒烟失败，禁止打包" }
        Remove-Item Env:\PYTHONPATH -ErrorAction SilentlyContinue
    }

    # ---- 确保 PyInstaller 就绪（构建期依赖，装在本 venv 不进 pyproject 运行时）----
    & $py -m PyInstaller --version 2>$null
    if ($LASTEXITCODE -ne 0) {
        Write-Host "安装 PyInstaller..."
        & $py -m pip install -q -i https://pypi.tuna.tsinghua.edu.cn/simple pyinstaller
        if ($LASTEXITCODE -ne 0) { throw "PyInstaller 安装失败" }
    }

    # ---- 构建 ----
    Write-Host "[3/5] PyInstaller 构建（可能需要几分钟）..."
    $buildArgs = @("-m", "PyInstaller", "--noconfirm", "--clean", "--onefile",
                   "--name", $AppName, "--paths", "src", "--noupx")
    if ($ConsoleDebug) { $buildArgs += "--console" } else { $buildArgs += "--windowed" }
    if ($IconPath -ne "" -and (Test-Path $IconPath)) { $buildArgs += @("--icon", $IconPath) }
    if ($AddData -ne "") { $buildArgs += @("--add-data", $AddData) }
    if ($VersionFile -ne "" -and (Test-Path $VersionFile)) { $buildArgs += @("--version-file", $VersionFile) }
    # ---- pygubu 感知：默认排除 PIL 与第三方插件（避免重型依赖被拖入 EXE）----
    # pygubu 核心（运行期加载 .ui 所需）由项目自行 --hidden-import；但 pygubu.builder 硬
    # 依赖 pygubu.stockimage，其内部惰性 `from PIL import ...` 会被 PyInstaller 收进包，
    # 拖入约 5MB 的 PIL 死重（项目 .ui 通常不用 stock 图片 / 需 PIL 的插件）。此外第三方插件
    # ttkwidgets/customtkinter 也会引用 PIL。故默认排除 PIL 与这两个插件包；需要时
    # （.ui 用到 pygubu stock 图片或需 PIL 的插件控件）删掉 --exclude-module=PIL 并补
    # --hidden-import=PIL（+ 对应插件）即可（默认关、不禁止）。
    & $py -c "import pygubu" 2>$null
    if ($LASTEXITCODE -eq 0) {
        $buildArgs += "--exclude-module=PIL"
        $buildArgs += "--exclude-module=pygubu.plugins.ttkwidgets"
        $buildArgs += "--exclude-module=pygubu.plugins.customtkinter"
    }
    # ---- 默认排除 cryptography（HTTPS 走标准库 ssl，无需 cryptography）----
    # Tkinter+requests 的 HTTPS 由 requests→urllib3→ssl（标准库）完成，运行期不 import
    # cryptography/OpenSSL/pyOpenSSL（实测 block 掉这些模块后 requests.get 仍 200）。
    # cryptography 被静态扫描收进包只是过度收集死重（~27%）。bcrypt 仅为 cryptography 依赖，一并排除。
    # 注意：libcrypto/libssl 两个 OpenSSL DLL 仍随标准库 _ssl 保留，TLS 不受影响。
    # 若应用确实要用 cryptography（自签证书/加解密），删掉这两行并补 --hidden-import=cryptography。
    $buildArgs += "--exclude-module=cryptography"
    $buildArgs += "--exclude-module=bcrypt"
    $buildArgs += $Entry
    $buildLog = Join-Path $ProjectDir "build_pyinstaller.log"
    # 关键：PyInstaller 把 INFO/WARNING 写到 stderr，PowerShell 在 Stop 模式下会把
    # 原生命令的 stderr 当作 NativeCommandError 中断构建（即使 2> 重定向也会触发）。
    # 因此构建调用期间临时放宽 ErrorActionPreference，真实退出码用 $LASTEXITCODE 判定。
    $prevEAP = $ErrorActionPreference
    $ErrorActionPreference = "Continue"
    & $py $buildArgs 2> $buildLog
    $rc = $LASTEXITCODE
    $ErrorActionPreference = $prevEAP
    if (Test-Path $buildLog) { Get-Content $buildLog | Out-Host }
    if ($rc -ne 0) { throw "PyInstaller 构建失败 (rc=$rc)，详见 build_pyinstaller.log" }

    # ---- 门禁 3: 产物检查 ----
    Write-Host "[4/5] 产物检查..."
    $exe = Join-Path $ProjectDir "dist\$AppName.exe"
    if (-not (Test-Path $exe)) { throw "产物不存在: $exe" }
    if (Test-Path (Join-Path $ProjectDir "dist\$AppName\_internal")) { throw "检测到 _internal/，违反 --onefile 铁律" }
    $sizeMB = [math]::Round((Get-Item $exe).Length / 1MB, 1)
    Write-Host "  EXE: $exe ($sizeMB MB)"

    # ---- 门禁 4: EXE 冒烟 ----
    # 注：Get-Process.MainWindowTitle 对 Tkinter 应用常返回空（Tk 窗口不被其识别为
    # 主窗口），故用 tasklist /v 探测真实窗口标题；并提供启动日志兜底校验。
    Write-Host "[5/5] EXE 冒烟..."
    $p = Start-Process -FilePath $exe -PassThru
    $ok = $false; $title = ""
    for ($i = 0; $i -lt 15; $i++) {
        Start-Sleep -Seconds 1
        if ($p.HasExited) {
            throw "EXE 启动即退出 (ExitCode=$($p.ExitCode))，用 -ConsoleDebug 重打调试版定位"
        }
        $tl = tasklist /fi "pid eq $($p.Id)" /v 2>$null
        if ($tl -match [regex]::Escape($AppName)) { $ok = $true; $title = $AppName; break }
    }
    if (-not $ok) {
        # 兜底：进程仍存活且启动日志出现主界面装配完成，则视为通过
        $log = Join-Path $ProjectDir "dist\logs\rdtk.log"
        if ((Test-Path $log) -and (Select-String -Path $log -Pattern "主界面装配完成" -Quiet)) {
            Write-Host "  窗口标题未直接探测到，但启动日志确认主界面已装配，视为通过"
            $ok = $true
        }
    }
    if (-not $ok) {
        Stop-Process -Id $p.Id -Force -ErrorAction SilentlyContinue
        throw "EXE 启动后未出现主窗口（标题=$AppName）"
    }
    Write-Host "  窗口标题: $title"
    Stop-Process -Id $p.Id -Force
    Write-Host ""
    Write-Host "构建成功: $exe ($sizeMB MB)"
}
finally {
    Pop-Location
}
