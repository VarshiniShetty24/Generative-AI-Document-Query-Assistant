@echo off
REM RAG System Setup Script for Windows

echo.
echo 🚀 Setting up RAG Document QA System...
echo.

REM Check Python version
python --version
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH
    exit /b 1
)

REM Create virtual environment if it doesn't exist
if not exist "venv" (
    echo 📦 Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo 🔧 Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo 📥 Installing dependencies...
pip install -r requirements.txt

REM Copy .env file if it doesn't exist
if not exist ".env" (
    echo 📝 Creating .env file...
    copy .env.example .env
    echo ⚠️  Please edit .env and add your API keys!
)

REM Create necessary directories
echo 📁 Creating data directories...
if not exist "data\documents" mkdir data\documents
if not exist "data\vectorstore" mkdir data\vectorstore

echo.
echo ✅ Setup complete!
echo.
echo Next steps:
echo 1. Edit .env and add your API keys
echo 2. Run: cd frontend ^&^& streamlit run app.py
echo.
pause
