"""
parsers.py
Handles text extraction from PDF, DOCX, and TXT files.
"""

import io
from PyPDF2 import PdfReader
import docx


class ParsingError(Exception):
    """Raised when a file cannot be parsed into usable text."""
    pass


def extract_text_from_pdf(file_stream):
    """
    Extract text from a PDF file.
    file_stream: a file-like object (e.g., from Flask's request.files)
    Returns: extracted text as a string.
    """
    try:
        reader = PdfReader(file_stream)
        text_parts = []
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text_parts.append(page_text)
        return "\n".join(text_parts).strip()
    except Exception as e:
        raise ParsingError(f"Could not read this PDF file: {e}")


def extract_text_from_docx(file_stream):
    """
    Extract text from a DOCX file.
    file_stream: a file-like object
    Returns: extracted text as a string.
    """
    try:
        document = docx.Document(file_stream)
        text_parts = [para.text for para in document.paragraphs if para.text.strip()]
        return "\n".join(text_parts).strip()
    except Exception as e:
        raise ParsingError(f"Could not read this DOCX file: {e}")


def extract_text_from_txt(file_stream):
    """
    Extract text from a TXT file.
    file_stream: a file-like object
    Returns: extracted text as a string.
    """
    try:
        raw_bytes = file_stream.read()
        text = raw_bytes.decode("utf-8", errors="ignore")
        return text.strip()
    except Exception as e:
        raise ParsingError(f"Could not read this TXT file: {e}")


def extract_text(filename, file_stream):
    """
    Routes a file to the correct parser based on its extension.
    filename: original filename (used to detect extension)
    file_stream: a file-like object
    Returns: extracted text as a string.
    Raises: ParsingError if the extension is unsupported or extraction fails.
    """
    extension = filename.rsplit(".", 1)[-1].lower() if "." in filename else ""

    if extension == "pdf":
        text = extract_text_from_pdf(file_stream)
    elif extension == "docx":
        text = extract_text_from_docx(file_stream)
    elif extension == "txt":
        text = extract_text_from_txt(file_stream)
    else:
        raise ParsingError(f"Unsupported file type: .{extension}")

    if not text or len(text.strip()) < 10:
        raise ParsingError("This file appears to be empty or unreadable.")

    return text