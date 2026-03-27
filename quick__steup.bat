@echo off
echo Quick Setup Starting...

REM Reorganize
call REORGANIZE.bat

REM Install tools
pip install uv
uv sync

REM Commit
git add .
git commit -m "refactor: Reorganize repository"
git push

echo.
echo ✓ Setup Complete!
echo Next: Review the new structure
pause