@echo off
setlocal enabledelayedexpansion

echo ================================================================
echo            PYTHON LEARNING REPOSITORY REORGANIZATION
echo ================================================================
echo.
echo This script will:
echo 1. Create organized directory structure
echo 2. Move existing files to proper locations
echo 3. Create configuration files
echo 4. Set up modern Python tooling
echo.
echo Press any key to continue or Ctrl+C to cancel...
pause >nul

REM ============================================================
REM STEP 1: Create Directory Structure
REM ============================================================
echo.
echo [1/8] Creating directory structure...

mkdir 01-fundamentals 2>nul
mkdir 02-data-structures 2>nul
mkdir 03-oop 2>nul
mkdir 04-modules-packages 2>nul
mkdir 05-file-handling 2>nul
mkdir 06-error-handling 2>nul
mkdir 07-data-analysis 2>nul
mkdir 08-apis 2>nul
mkdir 09-projects 2>nul
mkdir 10-exercises 2>nul
mkdir 10-exercises\leetcode 2>nul
mkdir notes 2>nul
mkdir scripts 2>nul
mkdir tests 2>nul

echo    ✓ Directories created

REM ============================================================
REM STEP 2: Create __init__.py files
REM ============================================================
echo.
echo [2/8] Creating package files...

echo # Fundamentals package > 01-fundamentals\__init__.py
echo # Data structures package > 02-data-structures\__init__.py
echo # OOP package > 03-oop\__init__.py
echo # Modules and packages > 04-modules-packages\__init__.py
echo # File handling package > 05-file-handling\__init__.py
echo # Error handling package > 06-error-handling\__init__.py
echo # Data analysis package > 07-data-analysis\__init__.py
echo # APIs package > 08-apis\__init__.py
echo # Projects package > 09-projects\__init__.py
echo # Exercises package > 10-exercises\__init__.py

echo    ✓ Package files created

REM ============================================================
REM STEP 3: Move Existing Files
REM ============================================================
echo.
echo [3/8] Moving existing files...

REM Move fundamentals
if exist Python_Basics.py (
    move /Y Python_Basics.py 01-fundamentals\ >nul 2>&1
    echo    ✓ Moved Python_Basics.py
)
if exist hello.py (
    move /Y hello.py 01-fundamentals\ >nul 2>&1
    echo    ✓ Moved hello.py
)
if exist interactive_demo.py (
    move /Y interactive_demo.py 01-fundamentals\ >nul 2>&1
    echo    ✓ Moved interactive_demo.py
)

REM Move OOP files
if exist classes.py (
    move /Y classes.py 03-oop\ >nul 2>&1
    echo    ✓ Moved classes.py
)
if exist building.py (
    move /Y building.py 03-oop\ >nul 2>&1
    echo    ✓ Moved building.py
)
if exist call.py (
    move /Y call.py 03-oop\ >nul 2>&1
    echo    ✓ Moved call.py
)

REM Move projects
if exist project\sales-analysis (
    xcopy /E /I /Y project\sales-analysis 07-data-analysis\sales-analyzer >nul 2>&1
    echo    ✓ Copied sales-analysis to 07-data-analysis/sales-analyzer
)
if exist project\weather (
    xcopy /E /I /Y project\weather 09-projects\weather >nul 2>&1
    echo    ✓ Copied weather to 09-projects/weather
)

REM Clean up temp files
if exist tempCodeRunnerFile.py del /F /Q tempCodeRunnerFile.py >nul 2>&1

echo    ✓ Files organized

REM ============================================================
REM STEP 4: Create .python-version
REM ============================================================
echo.
echo [4/8] Creating Python version file...
echo 3.12 > .python-version
echo    ✓ .python-version created

REM ============================================================
REM STEP 5: Move this script to scripts folder
REM ============================================================
echo.
echo [5/8] Setting up scripts folder...
REM Script will be moved manually later

REM ============================================================
REM STEP 6: Check for uv
REM ============================================================
echo.
echo [6/8] Checking for modern tools...

where uv >nul 2>&1
if %errorlevel% neq 0 (
    echo    ⚠ uv not found. Install with: pip install uv
    set UV_INSTALLED=0
) else (
    echo    ✓ uv is installed
    set UV_INSTALLED=1
)

REM ============================================================
REM STEP 7: Summary
REM ============================================================
echo.
echo [7/8] Creating summary file...

echo REORGANIZATION COMPLETE > REORGANIZATION_SUMMARY.txt
echo ======================== >> REORGANIZATION_SUMMARY.txt
echo. >> REORGANIZATION_SUMMARY.txt
echo Created directories: >> REORGANIZATION_SUMMARY.txt
echo - 01-fundamentals/ >> REORGANIZATION_SUMMARY.txt
echo - 02-data-structures/ >> REORGANIZATION_SUMMARY.txt
echo - 03-oop/ >> REORGANIZATION_SUMMARY.txt
echo - 04-modules-packages/ >> REORGANIZATION_SUMMARY.txt
echo - 05-file-handling/ >> REORGANIZATION_SUMMARY.txt
echo - 06-error-handling/ >> REORGANIZATION_SUMMARY.txt
echo - 07-data-analysis/ >> REORGANIZATION_SUMMARY.txt
echo - 08-apis/ >> REORGANIZATION_SUMMARY.txt
echo - 09-projects/ >> REORGANIZATION_SUMMARY.txt
echo - 10-exercises/ >> REORGANIZATION_SUMMARY.txt
echo - notes/ >> REORGANIZATION_SUMMARY.txt
echo - scripts/ >> REORGANIZATION_SUMMARY.txt
echo - tests/ >> REORGANIZATION_SUMMARY.txt

echo    ✓ Summary saved

REM ============================================================
REM STEP 8: Final Message
REM ============================================================
echo.
echo [8/8] Reorganization complete!
echo.
echo ================================================================
echo                    REORGANIZATION COMPLETE!
echo ================================================================
echo.
echo Your repository has been reorganized!
echo.
echo NEXT STEPS:
echo.
echo 1. Review the new structure:
echo    dir /B
echo.
echo 2. Copy the configuration files (see instructions below)
echo.
echo 3. Install modern tools:
echo    pip install uv
echo    uv sync
echo.
echo 4. Commit changes:
echo    git add .
echo    git commit -m "refactor: Reorganize repository structure"
echo    git push
echo.
echo 5. Check REORGANIZATION_SUMMARY.txt for details
echo.
echo ================================================================
pause