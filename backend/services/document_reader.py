from pathlib import Path
from pypdf import PdfReader
from docx import Document


def read_pdf(file_path: str) -> str:
    reader = PdfReader(file_path)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    return text


def read_docx(file_path: str) -> str:
    doc = Document(file_path)
    return "\n".join([p.text for p in doc.paragraphs])


def read_txt(file_path: str) -> str:
    return Path(file_path).read_text(encoding="utf-8")