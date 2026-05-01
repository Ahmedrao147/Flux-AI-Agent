# 🚀 Quick Start Guide - Bob AI Agent

Get started with Bob AI Agent in just a few minutes!

## Step 1: Install Dependencies

Run the automated setup script:

```bash
python setup.py
```

This will:
- ✅ Install all Python packages
- ✅ Download NLTK data
- ✅ Create necessary directories
- ✅ Generate a sample test file

**Manual Installation (if needed):**

```bash
pip install -r requirements.txt
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
```

## Step 2: Install Tesseract OCR (for image processing)

### Windows
1. Download from: https://github.com/UB-Mannheim/tesseract/wiki
2. Run the installer
3. Add to PATH: `C:\Program Files\Tesseract-OCR`

### macOS
```bash
brew install tesseract
```

### Linux (Ubuntu/Debian)
```bash
sudo apt-get update
sudo apt-get install tesseract-ocr
```

## Step 3: Run the Application

### Web Interface (Recommended)

```bash
streamlit run app.py
```

The app will open at: http://localhost:8501

### Command Line

```bash
python bob_agent.py <input_file> [format]
```

**Examples:**
```bash
# Generate both TXT and PDF
python bob_agent.py lecture.pdf both

# Generate only TXT
python bob_agent.py slides.pptx txt

# Generate only PDF
python bob_agent.py notes.txt pdf

# Test with sample file
python bob_agent.py samples/sample_lecture.txt both
```

## Step 4: Use the Web Interface

1. **Upload File**
   - Click "Browse files"
   - Select your lecture material (PDF, PPT, TXT, or image)

2. **Customize (Optional)**
   - Enter a custom title
   - Choose output format (TXT, PDF, or both)

3. **Generate**
   - Click "🚀 Generate Notes"
   - Wait for processing (usually 5-30 seconds)

4. **Review & Download**
   - Preview notes in the right panel
   - Click download buttons to save

## 📝 Example Workflow

### Scenario: Converting a PDF Lecture

1. You have: `machine_learning_lecture.pdf`
2. Upload it to Bob AI Agent
3. Add title: "ML Fundamentals - Week 1"
4. Select: "Both (TXT & PDF)"
5. Click "Generate Notes"
6. Download both formats

**Result:**
- `ML_Fundamentals_Week_1_notes.txt` - Plain text version
- `ML_Fundamentals_Week_1_notes.pdf` - Formatted PDF version

## 🎯 Tips for Best Results

### 1. File Quality
- ✅ Use clear, readable PDFs
- ✅ Ensure images have good contrast
- ✅ Avoid heavily formatted documents

### 2. Content Structure
- ✅ Files with clear headings work best
- ✅ Bullet points are preserved
- ✅ Numbered lists are maintained

### 3. File Size
- ✅ Recommended: Under 10MB
- ✅ Large files may take longer to process
- ✅ Split very large documents if needed

### 4. Image Processing
- ✅ Use high-resolution images (300+ DPI)
- ✅ Ensure text is horizontal
- ✅ Avoid handwritten notes (OCR works best with typed text)

## 🔧 Troubleshooting

### Issue: "Tesseract not found"
**Solution:**
```bash
# Check if installed
tesseract --version

# If not found, install it (see Step 2)
```

### Issue: "NLTK data not found"
**Solution:**
```python
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
```

### Issue: "Module not found"
**Solution:**
```bash
pip install -r requirements.txt
```

### Issue: "PDF extraction failed"
**Possible causes:**
- PDF is password-protected
- PDF is corrupted
- PDF contains only images (use OCR-enabled PDF)

**Solution:**
- Remove password protection
- Try a different PDF
- Use image extraction instead

### Issue: "Out of memory"
**Solution:**
- Process smaller files
- Close other applications
- Increase system RAM if possible

## 📚 Sample Files

Test the application with the included sample:

```bash
python bob_agent.py samples/sample_lecture.txt both
```

Or upload `samples/sample_lecture.txt` in the web interface.

## 🎓 What Makes Good Notes?

Bob AI Agent creates notes that are:

✅ **Concise** - Removes unnecessary repetition
✅ **Structured** - Organized with clear headings
✅ **Readable** - Uses bullet points and short paragraphs
✅ **Focused** - Highlights key concepts and definitions
✅ **Complete** - Includes important examples and summaries

## 📖 Understanding the Output

### Note Structure

```
TITLE
================================================================

KEY CONCEPTS:
----------------------------------------------------------------
• Concept 1
• Concept 2
• Concept 3

SECTION 1 HEADING
----------------------------------------------------------------
• Point 1
• Point 2
• Point 3

SECTION 2 HEADING
----------------------------------------------------------------
• Point 1
• Point 2

SUMMARY
----------------------------------------------------------------
Brief overview of the main points...
```

### Key Concepts
- Most frequently mentioned important terms
- Filtered to remove common words
- Helps identify main topics

### Sections
- Automatically detected from content
- Organized logically
- Bullet points for clarity

### Summary
- 2-3 sentence overview
- Captures main ideas
- Useful for quick review

## 🚀 Next Steps

1. **Try it out** - Upload your first lecture file
2. **Experiment** - Test different file formats
3. **Customize** - Adjust settings in `bob_agent.py` if needed
4. **Share** - Help other students by sharing the tool

## 💡 Pro Tips

1. **Batch Processing**: Process multiple lectures at once using command line
2. **Custom Titles**: Use descriptive titles for better organization
3. **Format Choice**: Use TXT for quick review, PDF for printing
4. **Regular Use**: Convert lectures immediately after class
5. **Combine Notes**: Merge notes from multiple sources manually

## 📞 Need Help?

- 📖 Read the full [README.md](README.md)
- 🐛 Report issues on GitHub
- 💬 Ask questions in discussions
- 📧 Email: bob-ai-support@example.com

---

**Happy Note-Taking! 📚✨**