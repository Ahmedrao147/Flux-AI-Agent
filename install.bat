@echo off
echo ========================================
echo Bob AI Agent - Windows Installation
echo ========================================
echo.

echo Step 1: Upgrading pip...
python -m pip install --upgrade pip
echo.

echo Step 2: Installing Python packages...
pip install streamlit python-dotenv groq PyPDF2 python-pptx nltk fpdf2 tqdm
echo.

echo Step 3: Installing Pillow (image processing)...
pip install Pillow
echo.

echo Step 4: Installing pytesseract...
pip install pytesseract
echo.

echo Step 5: Downloading NLTK data...
python -c "import nltk; nltk.download('punkt', quiet=True); nltk.download('stopwords', quiet=True)"
echo.

echo ========================================
echo Installation Complete!
echo ========================================
echo.
echo Next steps:
echo 1. Make sure Tesseract OCR is installed (optional for images)
echo 2. Your .env file is already configured with the API key
echo 3. Run: streamlit run app.py
echo.
pause

@REM Made with Bob
