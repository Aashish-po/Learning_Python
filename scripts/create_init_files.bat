@echo off
echo Creating __init__.py files...

REM Loop through all directories and create basic __init__.py
for %%d in (01-fundamentals 02-data-structures 03-oop 04-modules-packages 05-file-handling 06-error-handling 07-data-analysis 08-apis 09-projects 10-exercises) do (
    echo """%%d package.""" > %%d\__init__.py
    echo Created %%d\__init__.py
)

echo ✓ All __init__.py files created!