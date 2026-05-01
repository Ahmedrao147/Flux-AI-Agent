"""
Streamlit Web Application for Bob AI Agent with Groq Integration
Provides a user-friendly web interface with AI-powered note generation
"""

import streamlit as st
import os
from pathlib import Path
import tempfile
import io
from dotenv import load_dotenv
from bob_agent_groq import BobAIAgentGroq

# Load environment variables from .env file
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Bob AI Agent - Smart Note Taker",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        color: #1E88E5;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .section-header {
        font-size: 1.5rem;
        color: #1E88E5;
        margin-top: 1.5rem;
        margin-bottom: 0.5rem;
        border-bottom: 2px solid #1E88E5;
        padding-bottom: 0.3rem;
    }
    .key-concept {
        background-color: #E3F2FD;
        padding: 0.5rem;
        border-radius: 5px;
        margin: 0.3rem 0;
    }
    .stButton>button {
        width: 100%;
        background-color: #1E88E5;
        color: white;
    }
    .ai-badge {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.9rem;
        font-weight: bold;
        display: inline-block;
        margin-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'notes' not in st.session_state:
    st.session_state.notes = None
if 'bob' not in st.session_state:
    # Get API key from .env file
    try:
        st.session_state.bob = BobAIAgentGroq()
    except ValueError as e:
        st.error(f"⚠️ {str(e)}")
        st.info("Please create a .env file with your GROQ_API_KEY")
        st.stop()

def main():
    """Main application function."""
    
    # Header
    st.markdown('<h1 class="main-header">🤖 Bob AI Agent</h1>', unsafe_allow_html=True)
    st.markdown('<div class="ai-badge">✨ Powered by Groq AI</div>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Your Intelligent AI-Powered Note-Taking Assistant</p>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.image("https://img.icons8.com/fluency/96/000000/artificial-intelligence.png", width=80)
        st.title("About Bob AI")
        st.info("""
        **Bob AI Agent** uses advanced AI to convert lecture materials into structured, easy-to-read notes.
        
        **✨ AI Features:**
        - 🧠 Smart content understanding
        - 📝 Intelligent summarization
        - 🎯 Key concept extraction
        - 📊 Automatic structuring
        
        **Supported Formats:**
        - 📄 PDF
        - 📊 PowerPoint (PPT/PPTX)
        - 📝 Text files (TXT)
        - 🖼️ Images (PNG, JPG, JPEG)
        
        **Export Options:**
        - 📄 TXT (plain text)
        - 📕 PDF (formatted)
        """)
        
        st.markdown("---")
        st.markdown("### 🎯 How to Use")
        st.markdown("""
        1. Upload your lecture file
        2. (Optional) Add a custom title
        3. Click 'Generate AI Notes'
        4. Preview and download
        """)
        
        st.markdown("---")
        st.markdown("### ⚡ Powered by")
        st.markdown("**Groq** - Ultra-fast AI inference")
    
    # Main content area
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 📤 Upload Lecture Material")
        
        # File uploader
        uploaded_file = st.file_uploader(
            "Choose a file",
            type=['pdf', 'ppt', 'pptx', 'txt', 'png', 'jpg', 'jpeg'],
            help="Upload your lecture material in any supported format"
        )
        
        # Custom title input
        custom_title = st.text_input(
            "Custom Title (Optional)",
            placeholder="e.g., Introduction to Machine Learning",
            help="Leave empty to let AI generate a title"
        )
        
        # Output format selection
        output_format = st.radio(
            "Output Format",
            options=['Both (TXT & PDF)', 'TXT only', 'PDF only'],
            horizontal=True
        )
        
        # Generate button
        generate_button = st.button("🚀 Generate AI Notes", type="primary")
        
        if generate_button and uploaded_file is not None:
            with st.spinner("🤖 AI is processing your file... Please wait."):
                try:
                    # Save uploaded file temporarily
                    with tempfile.NamedTemporaryFile(delete=False, suffix=Path(uploaded_file.name).suffix) as tmp_file:
                        tmp_file.write(uploaded_file.getvalue())
                        tmp_path = tmp_file.name
                    
                    # Process file with detailed status
                    with st.status("🚀 Bob AI Agent is working...", expanded=True) as status:
                        # Step 1: Extract text
                        st.write("📄 Step 1: Extracting text from document...")
                        extracted = st.session_state.bob.process_file(tmp_path)
                        st.write(f"✅ Extracted {len(extracted['text'])} characters from {extracted['filename']}")
                        
                        # Step 2: AI Analysis
                        st.write("🧠 Step 2: AI is analyzing the content...")
                        st.write("⚡ Using Groq's Llama 3.1 70B model for intelligent processing")
                        
                        # Step 3: Generate notes
                        st.write("✨ Step 3: Generating structured AI notes...")
                        title = custom_title if custom_title.strip() else None
                        notes = st.session_state.bob.create_notes_with_ai(extracted['text'], title=title)
                        st.session_state.notes = notes
                        
                        # Step 4: Complete
                        st.write("🎯 Step 4: Formatting and organizing notes...")
                        st.write(f"📊 Generated {len(notes.get('key_concepts', []))} key concepts")
                        st.write(f"📚 Created {len(notes.get('sections', []))} organized sections")
                        
                        status.update(label="✅ AI Agent completed successfully!", state="complete")
                    
                    # Clean up temp file
                    os.unlink(tmp_path)
                    
                    st.success("🎉 AI-powered notes created successfully! Bob has analyzed and structured your content.")
                    st.balloons()
                    
                except Exception as e:
                    st.error(f"❌ Error processing file: {str(e)}")
                    st.info("💡 Tip: Make sure the file is not corrupted and is in a supported format.")
        
        elif generate_button and uploaded_file is None:
            st.warning("⚠️ Please upload a file first!")
    
    with col2:
        st.markdown("### 👁️ Preview AI-Generated Notes")
        
        if st.session_state.notes:
            notes = st.session_state.notes
            
            # AI Generation Info Box
            st.info("🤖 **Bob AI Agent** has analyzed your document and generated these intelligent notes using advanced AI (Groq Llama 3.1 70B)")
            
            # Display title with AI badge
            st.markdown(f"## {notes['title']}")
            st.markdown('<span style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 0.2rem 0.6rem; border-radius: 10px; font-size: 0.8rem;">🤖 AI Generated by Bob</span>', unsafe_allow_html=True)
            st.markdown("---")
            
            # Key Concepts - AI Extracted
            if notes.get('key_concepts') and len(notes['key_concepts']) > 0:
                st.markdown("### 🔑 AI-Extracted Key Concepts")
                st.caption("Bob identified these important concepts from your document")
                # Display in columns
                num_concepts = len(notes['key_concepts'])
                cols_per_row = 3
                for i in range(0, num_concepts, cols_per_row):
                    cols = st.columns(cols_per_row)
                    for j, col in enumerate(cols):
                        if i + j < num_concepts:
                            with col:
                                st.markdown(f'<div class="key-concept">• {notes["key_concepts"][i + j]}</div>', unsafe_allow_html=True)
                st.markdown("---")
            
            # Sections - AI Organized
            st.markdown("### 📚 AI-Organized Content Sections")
            st.caption("Bob has structured your document into logical sections")
            for idx, section in enumerate(notes['sections']):
                with st.expander(f"📖 {section['heading']}", expanded=(idx == 0)):
                    for point in section['content']:
                        st.markdown(f"• {point}")
            
            # Summary - AI Generated
            if notes.get('summary') and notes['summary'].strip():
                st.markdown("### 📋 AI-Generated Summary")
                st.caption("Bob's intelligent summary of the entire document")
                st.info(notes['summary'])
            
            # Download section
            st.markdown("---")
            st.markdown("### 💾 Download Notes")
            
            col_a, col_b = st.columns(2)
            
            # Prepare downloads based on format selection
            format_map = {
                'Both (TXT & PDF)': 'both',
                'TXT only': 'txt',
                'PDF only': 'pdf'
            }
            selected_format = format_map[output_format]
            
            # Generate files
            base_name = notes['title'].replace(' ', '_').replace('/', '_')[:30]
            
            if selected_format in ['txt', 'both']:
                with col_a:
                    # Generate TXT in memory
                    try:
                        # Create in-memory text buffer
                        txt_buffer = io.StringIO()
                        
                        # Write formatted content
                        txt_buffer.write(f"{'='*60}\n")
                        txt_buffer.write(f"{notes['title'].upper()}\n")
                        txt_buffer.write(f"{'='*60}\n\n")
                        
                        if notes.get('key_concepts'):
                            txt_buffer.write("KEY CONCEPTS:\n")
                            txt_buffer.write(f"{'-'*60}\n")
                            for concept in notes['key_concepts']:
                                txt_buffer.write(f"• {concept}\n")
                            txt_buffer.write("\n")
                        
                        for section in notes['sections']:
                            txt_buffer.write(f"\n{section['heading'].upper()}\n")
                            txt_buffer.write(f"{'-'*60}\n")
                            for point in section['content']:
                                txt_buffer.write(f"• {point}\n")
                            txt_buffer.write("\n")
                        
                        if notes.get('summary'):
                            txt_buffer.write(f"\nSUMMARY\n")
                            txt_buffer.write(f"{'-'*60}\n")
                            txt_buffer.write(f"{notes['summary']}\n")
                        
                        txt_content = txt_buffer.getvalue()
                        txt_buffer.close()
                        
                        st.download_button(
                            label="📄 Download TXT",
                            data=txt_content,
                            file_name=f"{base_name}_notes.txt",
                            mime="text/plain",
                            use_container_width=True
                        )
                    except Exception as e:
                        st.error(f"Error generating TXT: {str(e)}")
            
            if selected_format in ['pdf', 'both']:
                with col_b:
                    # Generate PDF using temporary file (required by FPDF)
                    try:
                        # Use context manager for automatic cleanup
                        with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_pdf:
                            tmp_pdf_path = tmp_pdf.name
                        
                        # Generate PDF
                        st.session_state.bob.export_to_pdf(notes, tmp_pdf_path)
                        
                        # Read PDF content immediately
                        with open(tmp_pdf_path, 'rb') as f:
                            pdf_content = f.read()
                        
                        # Clean up immediately after reading
                        try:
                            os.unlink(tmp_pdf_path)
                        except (PermissionError, OSError):
                            # If deletion fails, schedule for later cleanup
                            import atexit
                            atexit.register(lambda: os.path.exists(tmp_pdf_path) and os.unlink(tmp_pdf_path))
                        
                        st.download_button(
                            label="📕 Download PDF",
                            data=pdf_content,
                            file_name=f"{base_name}_notes.pdf",
                            mime="application/pdf",
                            use_container_width=True
                        )
                    except Exception as e:
                        st.error(f"Error generating PDF: {str(e)}")
        
        else:
            st.info("👈 Upload a file and click 'Generate AI Notes' to see the preview here.")
            st.markdown("""
            ### ✨ What makes our AI special?
            
            - **🧠 Smart Understanding**: AI comprehends context and meaning
            - **📝 Better Summaries**: More accurate and concise than basic algorithms
            - **🎯 Relevant Concepts**: Identifies truly important terms
            - **📊 Logical Structure**: Organizes content intelligently
            - **⚡ Lightning Fast**: Powered by Groq's ultra-fast inference
            """)
    
    # Footer
    st.markdown("---")
    st.markdown("""
        <div style='text-align: center; color: #666; padding: 1rem;'>
            <p>🤖 Powered by <strong>Groq AI</strong> | Made with ❤️ for Students</p>
            <p style='font-size: 0.9rem;'>Bob AI Agent - Transforming Learning Through AI</p>
        </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()

# Made with Bob
