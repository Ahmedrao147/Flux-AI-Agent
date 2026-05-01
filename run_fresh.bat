@echo off
echo ========================================
echo Bob AI Agent - Force Fresh Start
echo ========================================
echo.

echo Step 1: Killing all Python and Streamlit processes...
taskkill /F /IM python.exe 2>nul
taskkill /F /IM streamlit.exe 2>nul
timeout /t 2 /nobreak >nul

echo Step 2: Clearing all caches...
rmdir /s /q "%USERPROFILE%\.streamlit" 2>nul
for /d /r . %%d in (__pycache__) do @if exist "%%d" rd /s /q "%%d"
del /s /q *.pyc 2>nul

echo Step 3: Clearing browser cache (close all browsers first!)
echo Please close all browser windows now...
timeout /t 3

echo Step 4: Starting fresh Streamlit instance...
echo.
echo The app will open at: http://localhost:8501
echo.
echo If browser doesn't open, manually go to: http://localhost:8501
echo Press Ctrl+C to stop
echo.

cd /d "%~dp0"
python -m streamlit run app.py --server.port 8501 --server.headless false --browser.gatherUsageStats false

pause

@REM Made with Bob
