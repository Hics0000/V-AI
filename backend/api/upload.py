from pathlib import Path
import shutil

from fastapi import APIRouter, File, HTTPException, UploadFile

from backend.services.document_reader import (
    read_docx,
    read_pdf,
    read_txt,
)
from backend.services.text_splitter import split_text
from backend.services.vector_store import vector_store

router = APIRouter(prefix="/api", tags=["Upload"])

UPLOAD_DIR = Path("data/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    """
    Upload a document, extract its text,
    split it into chunks, and store it in ChromaDB.
    """

    # Save uploaded file
    file_path = UPLOAD_DIR / file.filename

    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Detect file type and extract text
    suffix = file_path.suffix.lower()

    if suffix == ".pdf":
        text = read_pdf(str(file_path))

    elif suffix == ".docx":
        text = read_docx(str(file_path))

    elif suffix == ".txt":
        text = read_txt(str(file_path))

    else:
        raise HTTPException(
            status_code=400,
            detail="Unsupported file type"
        )

    # Split document into chunks
    chunks = split_text(text)

    # Store chunks in ChromaDB
    vector_store.add_document(chunks)

    # Return success response
    return {
        "status": "success",
        "filename": file.filename,
        "characters": len(text),
        "chunks": len(chunks),
        "message": "Document indexed successfully.",
        "preview": text[:500],
    }