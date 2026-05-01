"""
Configuration file for Bob AI Agent
Customize settings here to adjust the behavior of the note-taking assistant
"""

# ============================================================================
# TEXT PROCESSING SETTINGS
# ============================================================================

# Summarization settings
MAX_SUMMARY_SENTENCES = 3  # Number of sentences in the summary
MIN_SENTENCE_LENGTH = 5    # Minimum words in a sentence to be considered

# Key concept extraction
NUM_KEY_CONCEPTS = 10      # Number of key concepts to extract
MIN_CONCEPT_LENGTH = 3     # Minimum character length for concepts
MAX_CONCEPT_LENGTH = 20    # Maximum character length for concepts

# Section detection
MIN_HEADING_LENGTH = 5     # Minimum characters for a heading
MAX_HEADING_LENGTH = 100   # Maximum characters for a heading

# ============================================================================
# FILE PROCESSING SETTINGS
# ============================================================================

# Supported file extensions
SUPPORTED_FORMATS = ['.pdf', '.ppt', '.pptx', '.txt', '.png', '.jpg', '.jpeg']

# Maximum file size (in MB)
MAX_FILE_SIZE_MB = 16

# ============================================================================
# OCR SETTINGS
# ============================================================================

# Tesseract OCR configuration
# Page Segmentation Modes (PSM):
# 0 = Orientation and script detection (OSD) only
# 1 = Automatic page segmentation with OSD
# 3 = Fully automatic page segmentation (default)
# 6 = Assume a single uniform block of text
# 11 = Sparse text. Find as much text as possible
TESSERACT_PSM = 6

# OCR Engine Mode (OEM):
# 0 = Legacy engine only
# 1 = Neural nets LSTM engine only
# 2 = Legacy + LSTM engines
# 3 = Default, based on what is available
TESSERACT_OEM = 3

# Custom Tesseract config string
TESSERACT_CONFIG = f'--oem {TESSERACT_OEM} --psm {TESSERACT_PSM}'

# ============================================================================
# OUTPUT SETTINGS
# ============================================================================

# PDF settings
PDF_FONT = 'Arial'
PDF_TITLE_SIZE = 16
PDF_HEADING_SIZE = 12
PDF_TEXT_SIZE = 10
PDF_LINE_HEIGHT = 5
PDF_MARGIN = 15

# Text file settings
TXT_LINE_WIDTH = 60  # Width of separator lines
TXT_ENCODING = 'utf-8'

# ============================================================================
# STREAMLIT UI SETTINGS
# ============================================================================

# Page configuration
PAGE_TITLE = "Bob AI Agent - Smart Note Taker"
PAGE_ICON = "📚"
LAYOUT = "wide"

# Theme colors (for custom CSS)
PRIMARY_COLOR = "#1E88E5"
SECONDARY_COLOR = "#E3F2FD"
TEXT_COLOR = "#666"

# ============================================================================
# DIRECTORY SETTINGS
# ============================================================================

# Directory paths
UPLOAD_DIR = "uploads"
OUTPUT_DIR = "outputs"
SAMPLE_DIR = "samples"

# ============================================================================
# NLTK SETTINGS
# ============================================================================

# NLTK data to download
NLTK_PACKAGES = ['punkt', 'stopwords']

# Language for stopwords
STOPWORDS_LANGUAGE = 'english'

# ============================================================================
# ADVANCED SETTINGS
# ============================================================================

# Enable/disable features
ENABLE_OCR = True           # Enable OCR for images
ENABLE_SUMMARIZATION = True # Enable automatic summarization
ENABLE_KEY_CONCEPTS = True  # Enable key concept extraction
ENABLE_SECTION_DETECTION = True  # Enable automatic section detection

# Performance settings
CHUNK_SIZE = 1000          # Characters to process at once for large files
TIMEOUT_SECONDS = 300      # Maximum processing time per file

# Debug settings
DEBUG_MODE = False         # Enable debug output
VERBOSE_LOGGING = False    # Enable verbose logging

# ============================================================================
# CUSTOM STOPWORDS
# ============================================================================

# Additional words to ignore (beyond NLTK stopwords)
CUSTOM_STOPWORDS = [
    'said', 'says', 'also', 'would', 'could', 'should',
    'may', 'might', 'must', 'can', 'will', 'shall'
]

# ============================================================================
# HEADING PATTERNS
# ============================================================================

# Regex patterns to identify headings
HEADING_PATTERNS = [
    r'^\d+\.(\d+\.)*\s+',      # Numbered headings (1., 1.1., etc.)
    r'^[A-Z][A-Z\s]+:$',        # All caps with colon
    r'^Chapter\s+\d+',          # Chapter headings
    r'^Section\s+\d+',          # Section headings
    r'^Part\s+[IVX]+',          # Part headings (Roman numerals)
]

# ============================================================================
# EXPORT TEMPLATES
# ============================================================================

# Template for text export header
TXT_HEADER_TEMPLATE = """
{'='*TXT_LINE_WIDTH}
{title}
{'='*TXT_LINE_WIDTH}
"""

# Template for section separator
TXT_SECTION_SEPARATOR = f"{'-'*TXT_LINE_WIDTH}"

# ============================================================================
# ERROR MESSAGES
# ============================================================================

ERROR_MESSAGES = {
    'file_not_found': "File not found. Please check the file path.",
    'unsupported_format': "Unsupported file format. Please use PDF, PPT, PPTX, TXT, or image files.",
    'ocr_failed': "OCR processing failed. Please ensure Tesseract is installed.",
    'pdf_extraction_failed': "Failed to extract text from PDF. The file may be corrupted or password-protected.",
    'empty_content': "No text content found in the file.",
    'processing_timeout': "Processing timeout. The file may be too large or complex.",
}

# ============================================================================
# SUCCESS MESSAGES
# ============================================================================

SUCCESS_MESSAGES = {
    'processing_complete': "✅ Notes generated successfully!",
    'file_uploaded': "✅ File uploaded successfully!",
    'export_complete': "✅ Notes exported successfully!",
}

# Made with Bob
