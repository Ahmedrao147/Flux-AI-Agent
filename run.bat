@echo off
echo ========================================
echo Starting Bob AI Agent...
echo ========================================
echo.

echo Checking if streamlit is installed...
python -m streamlit --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Streamlit is not installed!
    echo Please run install.bat first.
    echo.
    pause
    exit /b 1
)

echo Clearing Streamlit cache...
rmdir /s /q "%USERPROFILE%\.streamlit" 2>nul

echo Starting the application...
echo The app will open in your browser at http://localhost:8501
echo.
echo Press Ctrl+C to stop the server
echo.

python -m streamlit run app.py --server.headless=false

pause

@REM Made with Bob
