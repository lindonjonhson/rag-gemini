from PyPDF2 import PdfReader
from fastapi import HTTPException

def load_pdf(pdf_path):
    """Loads text from a PDF document."""
    text = ""
    try:
        with open(pdf_path, 'rb') as file:
            reader = PdfReader(file)
            for page in reader.pages:
                text += page.extract_text()
        return text
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"PDF file not found: {pdf_path}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading PDF: {e}")

def chunk_text(text, chunk_size=512, overlap=50):
    """Splits text into smaller chunks with overlap."""
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start = end - overlap
    return chunks