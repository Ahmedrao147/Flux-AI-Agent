# 📚 Usage Examples - Bob AI Agent

This document provides detailed examples of using Bob AI Agent for different scenarios.

## Table of Contents
1. [Basic Usage](#basic-usage)
2. [Web Interface Examples](#web-interface-examples)
3. [Command Line Examples](#command-line-examples)
4. [Advanced Use Cases](#advanced-use-cases)
5. [Tips and Tricks](#tips-and-tricks)

---

## Basic Usage

### Example 1: Converting a PDF Lecture

**Scenario:** You have a PDF lecture on "Introduction to Python Programming"

**Steps:**
1. Open Bob AI Agent: `streamlit run app.py`
2. Upload `python_intro.pdf`
3. Enter title: "Python Basics - Lecture 1"
4. Select: "Both (TXT & PDF)"
5. Click "Generate Notes"

**Output:**
- `Python_Basics_Lecture_1_notes.txt`
- `Python_Basics_Lecture_1_notes.pdf`

**Sample Output Structure:**
```
PYTHON BASICS - LECTURE 1
================================================================

KEY CONCEPTS:
----------------------------------------------------------------
• Python
• Variables
• Functions
• Data Types
• Programming

INTRODUCTION TO PYTHON
----------------------------------------------------------------
• Python is a high-level programming language
• Known for its simplicity and readability
• Used in web development, data science, and automation

VARIABLES AND DATA TYPES
----------------------------------------------------------------
• Variables store data values
• Common types: integers, strings, floats, booleans
• Python uses dynamic typing

SUMMARY
----------------------------------------------------------------
Python is a versatile programming language with simple syntax.
Variables store data, and Python supports multiple data types.
```

---

## Web Interface Examples

### Example 2: Processing PowerPoint Slides

**File:** `machine_learning_slides.pptx`

**Process:**
1. Upload the PPTX file
2. Leave title blank (auto-generate)
3. Select "PDF only"
4. Generate notes

**Result:**
- Extracts text from all slides
- Organizes by slide titles
- Creates formatted PDF

### Example 3: Converting Handwritten Notes (Image)

**File:** `lecture_notes_photo.jpg`

**Requirements:**
- Clear, high-resolution image
- Good lighting
- Typed or printed text (not handwritten)

**Process:**
1. Upload image
2. Wait for OCR processing
3. Review extracted text
4. Download notes

**Note:** OCR works best with:
- 300+ DPI images
- Black text on white background
- Horizontal text orientation

### Example 4: Processing Text Files

**File:** `study_notes.txt`

**Best for:**
- Raw text notes
- Copied content from websites
- Transcribed lectures

**Process:**
1. Upload TXT file
2. Add custom title
3. Select output format
4. Generate structured notes

---

## Command Line Examples

### Example 5: Batch Processing Multiple Files

```bash
# Process all PDFs in a directory
for file in lectures/*.pdf; do
    python bob_agent.py "$file" both
done
```

### Example 6: Quick TXT Conversion

```bash
# Convert single file to TXT only
python bob_agent.py lecture.pdf txt

# Output: lecture_notes.txt
```

### Example 7: PDF Output Only

```bash
# Generate formatted PDF
python bob_agent.py slides.pptx pdf

# Output: slides_notes.pdf
```

### Example 8: Processing with Custom Script

```python
from bob_agent import BobAIAgent

# Initialize
bob = BobAIAgent()

# Process file
extracted = bob.process_file('lecture.pdf')

# Create notes with custom title
notes = bob.create_notes(
    extracted['text'],
    title="Advanced Machine Learning - Week 3"
)

# Export
bob.export_to_txt(notes, 'week3_notes.txt')
bob.export_to_pdf(notes, 'week3_notes.pdf')

print("Notes created successfully!")
```

---

## Advanced Use Cases

### Example 9: Multi-Source Note Compilation

**Scenario:** Combine notes from multiple sources

```python
from bob_agent import BobAIAgent

bob = BobAIAgent()

# Process multiple files
sources = ['lecture.pdf', 'textbook.pdf', 'slides.pptx']
all_text = ""

for source in sources:
    extracted = bob.process_file(source)
    all_text += extracted['text'] + "\n\n"

# Create comprehensive notes
notes = bob.create_notes(all_text, title="Complete Study Guide")
bob.export_to_pdf(notes, 'complete_guide.pdf')
```

### Example 10: Custom Summarization

**Modify `bob_agent.py` for custom behavior:**

```python
# In _generate_summary method, change max_sentences
def _generate_summary(self, sentences: List[str], max_sentences: int = 5):
    # Now generates 5-sentence summaries instead of 3
    ...
```

### Example 11: Subject-Specific Processing

**For Math/Science:**
- Keep equations and formulas
- Preserve numbered steps
- Maintain theorem statements

**For Literature:**
- Extract quotes
- Identify themes
- Preserve character names

**For History:**
- Keep dates and events
- Maintain chronological order
- Preserve names and places

---

## Tips and Tricks

### Tip 1: Optimize PDF Quality

**Before uploading:**
- Ensure PDF is text-based (not scanned images)
- Remove password protection
- Check file isn't corrupted

**Test command:**
```bash
# Quick test
python bob_agent.py sample.pdf txt
```

### Tip 2: Improve OCR Results

**For images:**
1. Use high resolution (300+ DPI)
2. Ensure good contrast
3. Crop to text area only
4. Straighten rotated text

**Pre-processing script:**
```python
from PIL import Image, ImageEnhance

# Enhance image before OCR
img = Image.open('lecture_photo.jpg')
img = img.convert('L')  # Convert to grayscale
enhancer = ImageEnhance.Contrast(img)
img = enhancer.enhance(2)  # Increase contrast
img.save('enhanced.jpg')

# Now process with Bob AI
```

### Tip 3: Organize Output Files

**Create organized structure:**
```bash
# Create subject folders
mkdir -p notes/math notes/physics notes/cs

# Process and organize
python bob_agent.py math_lecture.pdf both
mv math_lecture_notes.* notes/math/

python bob_agent.py physics_lecture.pdf both
mv physics_lecture_notes.* notes/physics/
```

### Tip 4: Quick Review Workflow

**Daily routine:**
1. Upload today's lecture
2. Generate TXT for quick review
3. Generate PDF for printing
4. Review key concepts immediately
5. Add to study folder

### Tip 5: Combine with Other Tools

**Integration examples:**

**With Anki (flashcards):**
```python
# Extract key concepts for flashcards
notes = bob.create_notes(text)
concepts = notes['key_concepts']

# Create Anki cards
for concept in concepts:
    print(f"Front: What is {concept}?")
    print(f"Back: [Add definition]")
```

**With Notion:**
- Export as TXT
- Import to Notion
- Add tags and links

**With Google Drive:**
```bash
# Upload to Drive
python bob_agent.py lecture.pdf both
gdrive upload lecture_notes.pdf
```

---

## Real-World Scenarios

### Scenario 1: Exam Preparation

**Goal:** Create study guide from 10 lectures

**Process:**
```bash
# Process all lectures
for i in {1..10}; do
    python bob_agent.py "lecture_$i.pdf" both
done

# Combine TXT files
cat lecture_*_notes.txt > complete_study_guide.txt
```

### Scenario 2: Group Study

**Goal:** Share notes with study group

**Process:**
1. Process lecture with Bob AI
2. Generate PDF (formatted, professional)
3. Share via email/cloud
4. Everyone has same structured notes

### Scenario 3: Accessibility

**Goal:** Convert visual content to text

**Process:**
1. Take photos of whiteboard
2. Process with Bob AI (OCR)
3. Generate accessible text notes
4. Share with students who need text format

### Scenario 4: Language Learning

**Goal:** Extract vocabulary from reading material

**Process:**
1. Upload text/PDF in target language
2. Extract key concepts (vocabulary)
3. Create vocabulary list
4. Use for study

---

## Troubleshooting Examples

### Problem: Notes too brief

**Solution:**
```python
# Modify config.py
MAX_SUMMARY_SENTENCES = 5  # Increase from 3
NUM_KEY_CONCEPTS = 15      # Increase from 10
```

### Problem: Missing sections

**Solution:**
- Check if original has clear headings
- Add headings manually before processing
- Use text file with structured content

### Problem: OCR errors

**Solution:**
1. Improve image quality
2. Use better lighting
3. Increase image resolution
4. Try different OCR settings in config.py

---

## Performance Benchmarks

**Typical processing times:**

| File Type | Size | Processing Time |
|-----------|------|-----------------|
| TXT | 100 KB | 2-5 seconds |
| PDF | 5 MB | 10-20 seconds |
| PPTX | 10 MB | 15-30 seconds |
| Image | 2 MB | 20-40 seconds |

**Optimization tips:**
- Process smaller files when possible
- Close other applications
- Use SSD for faster I/O
- Increase RAM if processing large files

---

## Best Practices

1. **Regular Processing:** Convert lectures immediately after class
2. **Consistent Naming:** Use clear, descriptive titles
3. **Backup:** Keep original files and generated notes
4. **Review:** Always review generated notes for accuracy
5. **Customize:** Adjust settings in config.py for your needs
6. **Organize:** Create folder structure for different subjects
7. **Share:** Help classmates by sharing well-structured notes

---

**Need more help?** Check out:
- [README.md](README.md) - Full documentation
- [QUICKSTART.md](QUICKSTART.md) - Quick start guide
- GitHub Issues - Report problems or ask questions