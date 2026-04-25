@echo off
chcp 65001 >nul
cd /d "%~dp0"

echo ========================================
echo    Quartz 内容监听自动推送
echo ========================================
echo.

:: 指定系统 Python 路径（避免使用虚拟环境）
set PYTHON_PATH=C:\Users\c3458\AppData\Local\Programs\Python\Python312\python.exe

:: 确保 watchdog 已安装
%PYTHON_PATH% -m pip install --quiet watchdog >nul 2>&1

:: 启动监听
%PYTHON_PATH% "%~dp0auto_sync.py"

pause