@echo off
setlocal enabledelayedexpansion
# new-topic.bat - Create a new topic directory with starter files for learning Python concepts.
if "%1"=="" (
    echo Usage: new-topic.bat topic_name
    echo Example: new-topic.bat decorators
    exit /b 1
)

set TOPIC=%1
echo Creating new topic: %TOPIC%

REM Create directory
mkdir %TOPIC% 2>nul

REM Create __init__.py
echo # %TOPIC% package > %TOPIC%\__init__.py

REM Create README.md
(
echo # %TOPIC%
echo.
echo ## Overview
echo.
echo Brief description of %TOPIC%.
echo.
echo ## Key Concepts
echo.
echo - Concept 1
echo - Concept 2
echo - Concept 3
echo.
echo ## Examples
echo.
echo See `example.py` for practical examples.
echo.
echo ## Exercises
echo.
echo 1. Exercise 1
echo 2. Exercise 2
echo 3. Exercise 3
echo.
echo ## Resources
echo.
echo - [Python Docs](https://docs.python.org/3/)
echo - Additional resources here
) > %TOPIC%\README.md

REM Create example.py
(
echo """
echo Examples and demonstrations for %TOPIC%.
echo """
echo.
echo def example_function^(^):
echo     """Example function demonstrating %TOPIC%."""
echo     pass
echo.
echo.
echo if __name__ == "__main__":
echo     print^("Running %TOPIC% examples..."^)
echo     example_function^(^)
) > %TOPIC%\example.py

REM Create exercises.py
(
echo """
echo Practice exercises for %TOPIC%.
echo """
echo.
echo # Exercise 1
echo def exercise_1^(^):
echo     """Starter exercise for %TOPIC%."""
echo     print^("Exercise 1: practice %TOPIC%."^)
echo.
echo.
echo def exercise_2^(^):
echo     """Apply %TOPIC% in a small example."""
echo     print^("Exercise 2: build a small example using %TOPIC%."^)
echo.
echo.
echo if __name__ == "__main__":
echo     exercise_1^(^)
echo     exercise_2^(^)
) > %TOPIC%\exercises.py

echo.
echo ✓ Created %TOPIC%/ directory with:
echo   - __init__.py
echo   - README.md
echo   - example.py
echo   - exercises.py
echo.
echo Next: Edit the files and start learning!
