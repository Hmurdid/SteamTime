@echo off

if not exist venv (
    echo venv folder doesn't exist!
	exit /b 1
) else (
    venv\Scripts\python.exe main.py
	pause
)