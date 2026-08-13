@echo off
setlocal
cd /d "%~dp0"
where pythonw >nul 2>nul && set "PY=pythonw" || set "PY=python"
start "" %PY% run.py
