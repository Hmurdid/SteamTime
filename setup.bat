@echo off
chcp 65001 > nul
echo.
echo ========================================
echo     	Installing Steam App
echo ========================================
echo.

if not exist venv (
    echo [1/2] Creating virtual environment...
    python -m venv venv
    if errorlevel 1 (
        echo Error creating venv!
        pause
        exit /b 1
    )
    echo Venv created
) else (
    echo Venv already exists
)

echo.
echo [2/2] Installing dependencies...
venv\Scripts\pip.exe install -r requirements.txt
if errorlevel 1 (
    echo Error installing packages!
    pause
    exit /b 1
)

echo.
echo ========================================
echo 		Installation complete!
echo ========================================
echo.
echo Run the app using run.bat
echo.
pause