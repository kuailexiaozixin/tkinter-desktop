@echo off
chcp 65001 >nul
set PYTHONUTF8=1
REM 启动本示例目录中的 Inventory Management System（本地源码，非系统 Python 安装的库）
cd /d "%~dp0"
python run.py
