@echo off
chcp 65001 >nul
set PYTHONUTF8=1
REM 启动本示例目录中「本地源码」里的 IDLE（非系统 Python 自带的 idlelib）
cd /d "%~dp0"
python run.py
