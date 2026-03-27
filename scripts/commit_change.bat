@echo off
echo Committing changes...
scripts\lint.bat
if %errorlevel% neq 0 exit /b 1

git add .
git status
echo.
set /p msg="Commit message: "
git commit -m "%msg%"
git push
echo ✓ Pushed to GitHub!