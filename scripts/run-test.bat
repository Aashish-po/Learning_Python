@echo off
echo ================================================================
echo              PYTHON PROJECT SETUP
echo ================================================================
echo.

echo This will set up your Python project with modern tools.
echo.
pause

echo [1/5] Checking Python version...
python --version
if %errorlevel% neq 0 (
    echo ❌ Python not found! Please install Python 3.12+
    exit /b 1
)

echo.
echo [2/5] Installing uv package manager...
pip install uv
if %errorlevel% neq 0 (
    echo ❌ Failed to install uv
    exit /b 1
)

echo.
echo [3/5] Initializing project with uv...
if not exist pyproject.toml (
    uv init .
)

echo.
echo [4/5] Installing dependencies...
uv sync

echo.
echo [5/5] Installing development tools...
uv add --dev ruff pytest mypy

echo.
echo ================================================================
echo ✓ Setup complete!
echo.
echo Next steps:
echo 1. Activate virtual environment: .venv\Scripts\activate
echo 2. Start coding!
echo 3. Run tests: scripts\run-tests.bat
echo 4. Check code quality: scripts\lint.bat
echo ================================================================