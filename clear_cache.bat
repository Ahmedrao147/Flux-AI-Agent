@echo off
echo ========================================
echo Clearing Streamlit Cache
echo ========================================
echo.

echo Stopping any running Streamlit processes...
taskkill /F /IM streamlit.exe 2>nul
taskkill /F /IM python.exe /FI "WINDOWTITLE eq streamlit*" 2>nul

echo Clearing Streamlit cache directory...
rmdir /s /q "%USERPROFILE%\.streamlit" 2>nul

echo Clearing Python cache...
for /d /r . %%d in (__pycache__) do @if exist "%%d" rd /s /q "%%d"
del /s /q *.pyc 2>nul

echo.
echo ========================================
echo Cache cleared successfully!
echo ========================================
echo.
echo Now run: run.bat
echo.
pause

@REM Made with Bob
