from pathlib import Path
import shutil

from fastapi import APIRouter, File, HTTPException, UploadFile

from backend.services.document_reader import (
    read_docx,
    read_pdf,
    read_txt,
)

router = APIRouter(prefix="/api", tags=["Upload"])

UPLOAD_DIR = Path("data/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_path = UPLOAD_DIR / file.filename

    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    suffix = file_path.suffix.lower()

    if suffix == ".pdf":
        text = read_pdf(str(file_path))
    elif suffix == ".docx":
        text = read_docx(str(file_path))
    elif suffix == ".txt":
        text = read_txt(str(file_path))
    else:
        raise HTTPException(status_code=400, detail="Unsupported file type")

    return {
        "filename": file.filename,
        "characters": len(text),
        "preview": text[:500],
    }