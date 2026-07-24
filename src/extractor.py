import pdfplumber

def extract_text_from_pdf(pdf_path):
    """
    Takes path of a PDF file and returns all text inside it as a string.
    """
    text = ""
    
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    
    return text

from docx import Document

def extract_text_from_docx(docx_path):
    """
    Takes path of a DOCX file and returns all text inside it as a string.
    """
    doc = Document(docx_path)
    text = ""
    
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    
    return text

def extract_text(file_path):
    """
    Detects file type (PDF or DOCX) and extracts text accordingly.
    """
    if file_path.endswith(".pdf"):
        return extract_text_from_pdf(file_path)
    elif file_path.endswith(".docx"):
        return extract_text_from_docx(file_path)
    else:
        raise ValueError("Unsupported file format. Please use PDF or DOCX.")