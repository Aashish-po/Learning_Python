@echo off
echo Creating example files for all directories...
echo.

REM 01-fundamentals examples
echo Creating fundamentals examples...
python -c "import os; os.makedirs('01-fundamentals/examples', exist_ok=True)"

REM 02-data-structures examples  
echo Creating data structures examples...
python -c "import os; os.makedirs('02-data-structures/examples', exist_ok=True)"

REM Continue for all directories...

echo ✓ Example directories created!