# bootstrap_project.ps1 - Tkinter 项目骨架生成（PowerShell 5.1 兼容）
# 用法: powershell -ExecutionPolicy Bypass -File bootstrap_project.ps1 -ProjectDir D:\work\my-tool -PkgName mytool -AppTitle "我的工具"
param(
    [Parameter(Mandatory = $true)][string]$ProjectDir,
    [Parameter(Mandatory = $true)][string]$PkgName,
    [string]$AppTitle = "My Tool",
    [string]$PythonExe = "python"
)

$ErrorActionPreference = "Stop"

Write-Host "[1/4] 创建目录结构..."
$dirs = @(
    "$ProjectDir",
    "$ProjectDir\src\$PkgName\common",
    "$ProjectDir\src\$PkgName\models",
    "$ProjectDir\src\$PkgName\views",
    "$ProjectDir\src\$PkgName\controllers",
    "$ProjectDir\tests",
    "$ProjectDir\scripts",
    "$ProjectDir\docs",
    "$ProjectDir\assets"
)
foreach ($d in $dirs) { New-Item -ItemType Directory -Force -Path $d | Out-Null }

Write-Host "[2/4] 复制蓝图模板..."
$blueprint = Join-Path $PSScriptRoot "..\templates\project-blueprints\tk-desktop-app"
if (-not (Test-Path $blueprint)) { throw "找不到蓝图目录: $blueprint" }

# 逐文件复制并替换占位符 __PKG__ / __TITLE__
Get-ChildItem -Path $blueprint -Recurse -File | ForEach-Object {
    $rel = $_.FullName.Substring((Resolve-Path $blueprint).Path.Length + 1)
    $rel = $rel -replace "__PKG__", $PkgName
    if ($rel.EndsWith(".tmpl")) { $rel = $rel.Substring(0, $rel.Length - 5) }
    $dest = Join-Path $ProjectDir $rel
    $destDir = Split-Path $dest -Parent
    if (-not (Test-Path $destDir)) { New-Item -ItemType Directory -Force -Path $destDir | Out-Null }
    $content = [System.IO.File]::ReadAllText($_.FullName, [System.Text.Encoding]::UTF8)
    $content = $content -replace "__PKG__", $PkgName
    $content = $content -replace "__TITLE__", $AppTitle
    # 源码写 UTF-8 无 BOM
    $utf8NoBom = New-Object System.Text.UTF8Encoding($false)
    [System.IO.File]::WriteAllText($dest, $content, $utf8NoBom)
    Write-Host "  + $rel"
}

Write-Host "[3/4] 创建 venv..."
& $PythonExe -m venv "$ProjectDir\.venv"
if ($LASTEXITCODE -ne 0) { throw "venv 创建失败" }

Write-Host "[4/4] 验证空壳可导入..."
$py = "$ProjectDir\.venv\Scripts\python.exe"
Push-Location "$ProjectDir\src"
& $py -c "import $PkgName" 2>&1
$code = $LASTEXITCODE
Pop-Location
if ($code -ne 0) { throw "包导入失败，请检查骨架" }

Write-Host ""
Write-Host "完成。下一步："
Write-Host "  cd $ProjectDir"
Write-Host "  .venv\Scripts\python.exe -m pip install -e . --group dev  # 或直接 pip install pytest"
Write-Host "  set PYTHONPATH=src && .venv\Scripts\python.exe -m $PkgName  # 弹出空壳窗口"
