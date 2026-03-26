@echo off
echo ================================================================
echo                      CODE QUALITY CHECK
echo ================================================================
echo.

REM Check if ruff is installed
where ruff >nul 2>&1
if %errorlevel% neq 0 (
    echo ⚠ Ruff not installed. Installing...
    pip install ruff
)

echo [1/3] Linting with Ruff...
echo ----------------------------------------------------------------
ruff check . --fix
if %errorlevel% neq 0 (
    echo ❌ Linting found issues
    set LINT_FAILED=1
) else (
    echo ✓ Linting passed
)

echo.
echo [2/3] Formatting with Ruff...
echo ----------------------------------------------------------------
ruff format .
if %errorlevel% neq 0 (
    echo ❌ Formatting failed
    set FORMAT_FAILED=1
) else (
    echo ✓ Formatting complete
)

echo.
echo [3/3] Type checking with mypy (if installed)...
echo ----------------------------------------------------------------
where mypy >nul 2>&1
if %errorlevel% equ 0 (
    mypy . --ignore-missing-imports
    if %errorlevel% neq 0 (
        echo ⚠ Type checking found issues
    ) else (
        echo ✓ Type checking passed
    )
) else (
    echo ⚠ mypy not installed, skipping type check
    echo   Install with: pip install mypy
)

echo.
echo ================================================================
if defined LINT_FAILED (
    echo ❌ Code quality check failed
    exit /b 1
) else (
    echo ✓ Code quality check complete!
)
echo ================================================================