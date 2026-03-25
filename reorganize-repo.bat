@echo off
echo ================================================
echo  Python Learning Repository Reorganization
echo ================================================
echo.

echo Step 1: Creating directory structure...
mkdir 01-fundamentals 02-data-structures 03-oop 04-modules-packages 05-file-handling 06-error-handling 07-data-analysis 08-apis 09-projects 10-exercises notes scripts 2>nul

echo Step 2: Moving files...
move Python_Basics.py 01-fundamentals\ 2>nul
move hello.py 01-fundamentals\ 2>nul
move interactive_demo.py 01-fundamentals\ 2>nul
move classes.py 03-oop\ 2>nul
move building.py 03-oop\ 2>nul
move call.py 03-oop\ 2>nul

echo Step 3: Copying projects...
xcopy /E /I /Y project\sales-analysis 07-data-analysis\sales-analyzer >nul 2>&1
xcopy /E /I /Y project\weather 09-projects\weather >nul 2>&1

echo Step 4: Creating configuration files...
echo 3.12 > .python-version

echo Step 5: Creating __init__.py files...
type nul > 01-fundamentals\__init__.py
type nul > 02-data-structures\__init__.py
type nul > 03-oop\__init__.py
type nul > 04-modules-packages\__init__.py
type nul > 05-file-handling\__init__.py
type nul > 06-error-handling\__init__.py
type nul > 07-data-analysis\__init__.py
type nul > 08-apis\__init__.py
type nul > 09-projects\__init__.py
type nul > 10-exercises\__init__.py

echo.
echo ================================================
echo  ✓ Reorganization Complete!
echo ================================================
echo.
echo Next steps:
echo 1. Review the new structure
echo 2. Install uv: pip install uv
echo 3. Run: uv init .
echo 4. Run: uv sync
echo 5. Commit: git add . ^&^& git commit -m "refactor: Reorganize repo"
echo.
pause