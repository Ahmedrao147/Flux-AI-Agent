"""
Installation Verification Script for Bob AI Agent
Tests all components and dependencies
"""

import sys
import os


def print_header(text):
    """Print a formatted header."""
    print("\n" + "=" * 60)
    print(f"  {text}")
    print("=" * 60)


def print_status(component, status, message=""):
    """Print component status."""
    icon = "✅" if status else "❌"
    print(f"{icon} {component}: {'OK' if status else 'FAILED'}")
    if message:
        print(f"   {message}")


def check_python_version():
    """Check Python version."""
    print_header("Checking Python Version")
    version = sys.version_info
    required = (3, 8)
    
    current = f"{version.major}.{version.minor}.{version.micro}"
    print(f"Current version: Python {current}")
    
    if version >= required:
        print_status("Python Version", True, f"Python {version.major}.{version.minor}+ required")
        return True
    else:
        print_status("Python Version", False, f"Python {required[0]}.{required[1]}+ required")
        return False


def check_dependencies():
    """Check if all required packages are installed."""
    print_header("Checking Dependencies")
    
    dependencies = {
        'streamlit': 'Streamlit',
        'PyPDF2': 'PyPDF2',
        'pptx': 'python-pptx',
        'PIL': 'Pillow',
        'pytesseract': 'pytesseract',
        'nltk': 'NLTK',
        'fpdf': 'fpdf2',
    }
    
    all_ok = True
    for module, name in dependencies.items():
        try:
            __import__(module)
            print_status(name, True)
        except ImportError:
            print_status(name, False, f"Install with: pip install {name}")
            all_ok = False
    
    return all_ok


def check_nltk_data():
    """Check if NLTK data is downloaded."""
    print_header("Checking NLTK Data")
    
    try:
        import nltk
        
        datasets = ['punkt', 'stopwords']
        all_ok = True
        
        for dataset in datasets:
            try:
                nltk.data.find(f'tokenizers/{dataset}' if dataset == 'punkt' else f'corpora/{dataset}')
                print_status(f"NLTK {dataset}", True)
            except LookupError:
                print_status(f"NLTK {dataset}", False, f"Download with: nltk.download('{dataset}')")
                all_ok = False
        
        return all_ok
    except ImportError:
        print_status("NLTK", False, "NLTK not installed")
        return False


def check_tesseract():
    """Check if Tesseract OCR is installed."""
    print_header("Checking Tesseract OCR")
    
    try:
        import pytesseract
        version = pytesseract.get_tesseract_version()
        print_status("Tesseract OCR", True, f"Version: {version}")
        return True
    except Exception as e:
        print_status("Tesseract OCR", False, "Not installed or not in PATH")
        print("\nInstallation instructions:")
        print("  Windows: https://github.com/UB-Mannheim/tesseract/wiki")
        print("  macOS: brew install tesseract")
        print("  Linux: sudo apt-get install tesseract-ocr")
        return False


def check_directories():
    """Check if required directories exist."""
    print_header("Checking Directories")
    
    directories = ['uploads', 'outputs', 'samples']
    all_ok = True
    
    for directory in directories:
        if os.path.exists(directory):
            print_status(f"Directory: {directory}", True)
        else:
            print_status(f"Directory: {directory}", False, "Will be created automatically")
            try:
                os.makedirs(directory, exist_ok=True)
                print(f"   Created: {directory}")
            except Exception as e:
                all_ok = False
    
    return all_ok


def check_core_files():
    """Check if core application files exist."""
    print_header("Checking Core Files")
    
    files = {
        'bob_agent.py': 'Core AI Agent',
        'app.py': 'Streamlit Application',
        'requirements.txt': 'Dependencies List',
        'config.py': 'Configuration File',
    }
    
    all_ok = True
    for filename, description in files.items():
        if os.path.exists(filename):
            print_status(f"{description} ({filename})", True)
        else:
            print_status(f"{description} ({filename})", False, "File missing")
            all_ok = False
    
    return all_ok


def test_basic_functionality():
    """Test basic functionality of Bob AI Agent."""
    print_header("Testing Basic Functionality")
    
    try:
        from bob_agent import BobAIAgent
        
        # Initialize agent
        bob = BobAIAgent()
        print_status("Initialize BobAIAgent", True)
        
        # Test text processing
        test_text = "This is a test. Machine learning is important. Data science is growing."
        notes = bob.create_notes(test_text, title="Test Notes")
        
        if notes and 'title' in notes and 'sections' in notes:
            print_status("Text Processing", True)
        else:
            print_status("Text Processing", False, "Notes structure invalid")
            return False
        
        # Test export functions
        import tempfile
        
        with tempfile.NamedTemporaryFile(suffix='.txt', delete=False) as tmp:
            bob.export_to_txt(notes, tmp.name)
            if os.path.exists(tmp.name) and os.path.getsize(tmp.name) > 0:
                print_status("TXT Export", True)
                os.unlink(tmp.name)
            else:
                print_status("TXT Export", False)
                return False
        
        with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as tmp:
            bob.export_to_pdf(notes, tmp.name)
            if os.path.exists(tmp.name) and os.path.getsize(tmp.name) > 0:
                print_status("PDF Export", True)
                os.unlink(tmp.name)
            else:
                print_status("PDF Export", False)
                return False
        
        return True
        
    except Exception as e:
        print_status("Basic Functionality", False, str(e))
        return False


def main():
    """Main verification function."""
    print("\n" + "=" * 60)
    print("  BOB AI AGENT - INSTALLATION VERIFICATION")
    print("=" * 60)
    
    results = {
        'Python Version': check_python_version(),
        'Dependencies': check_dependencies(),
        'NLTK Data': check_nltk_data(),
        'Tesseract OCR': check_tesseract(),
        'Directories': check_directories(),
        'Core Files': check_core_files(),
        'Basic Functionality': test_basic_functionality(),
    }
    
    # Summary
    print_header("Verification Summary")
    
    passed = sum(results.values())
    total = len(results)
    
    for component, status in results.items():
        icon = "✅" if status else "❌"
        print(f"{icon} {component}")
    
    print("\n" + "=" * 60)
    print(f"  Results: {passed}/{total} checks passed")
    print("=" * 60)
    
    if passed == total:
        print("\n🎉 All checks passed! Bob AI Agent is ready to use.")
        print("\n🚀 Start the application with:")
        print("   streamlit run app.py")
    elif passed >= total - 1 and not results['Tesseract OCR']:
        print("\n⚠️  Almost ready! Tesseract OCR is optional for image processing.")
        print("   You can still use Bob AI Agent with PDF, PPT, and TXT files.")
        print("\n🚀 Start the application with:")
        print("   streamlit run app.py")
    else:
        print("\n❌ Some checks failed. Please fix the issues above.")
        print("\n💡 Quick fixes:")
        print("   1. Install dependencies: pip install -r requirements.txt")
        print("   2. Download NLTK data: python -c \"import nltk; nltk.download('punkt'); nltk.download('stopwords')\"")
        print("   3. Install Tesseract OCR (see documentation)")
    
    print("\n" + "=" * 60 + "\n")
    
    return passed == total


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

# Made with Bob
