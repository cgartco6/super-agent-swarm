@echo off
:: Super Agent Swarm - Full Setup Script for Windows 10 Pro
:: Run as Administrator

echo ========================================
echo   Super Agent Swarm Setup for Windows
echo ========================================

:: Check for Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python not found. Please install Python 3.11+ from python.org
    pause
    exit /b
)

:: Create project directory
set PROJECT_DIR=%USERPROFILE%\super-agent-swarm
mkdir "%PROJECT_DIR%\ui" 2>nul
cd /d "%PROJECT_DIR%"

echo Creating virtual environment...
python -m venv venv
call venv\Scripts\activate.bat

echo Installing dependencies...
pip install --upgrade pip
pip install -r requirements.txt

:: Create .env
echo OPENAI_API_KEY=sk-your-key-here > .env

echo Creating launch script...
(
echo @echo off
echo cd /d "%%\~dp0"
echo call venv\Scripts\activate.bat
echo streamlit run ui\command_center.py --server.port 8501
) > launch.bat

echo.
echo ========================================
echo Setup Complete!
echo.
echo To start the Command Center:
echo 1. Double-click launch.bat
echo 2. Open browser to http://localhost:8501
echo ========================================

pause
