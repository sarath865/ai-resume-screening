from fastapi import (
    APIRouter,
    UploadFile,
    File
)

from app.models.candidate import Candidate
from app.database import SessionLocal

from app.utils.resume_parser import (
    extract_text_from_pdf,
    extract_text_from_docx,
    extract_email,
    extract_phone,
    extract_skills
)

import shutil
import os

router = APIRouter(
    prefix="/candidates",
    tags=["Candidates"]
)

UPLOAD_DIR = "uploads"

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)


@router.post("/upload")
async def upload_resume(
    file: UploadFile = File(...)
):

    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(
        file_path,
        "wb"
    ) as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    if file.filename.endswith(".pdf"):

        text = extract_text_from_pdf(
            file_path
        )

    elif file.filename.endswith(".docx"):

        text = extract_text_from_docx(
            file_path
        )

    else:

        return {
            "error": "Only PDF and DOCX files are allowed"
        }

    email = extract_email(text)

    phone = extract_phone(text)

    skills = extract_skills(text)

    db = SessionLocal()

    candidate = Candidate(
        name=file.filename,
        email=email,
        phone=phone,
        skills=", ".join(skills),
        resume_path=file_path
    )

    db.add(candidate)

    db.commit()

    db.refresh(candidate)

    return {
        "message": "Resume Uploaded Successfully",
        "candidate_id": candidate.id,
        "email": email,
        "phone": phone,
        "skills": skills
    }


@router.get("/")
def get_candidates():

    db = SessionLocal()

    candidates = db.query(
        Candidate
    ).all()

    return candidates


@router.get("/{candidate_id}")
def get_candidate(
    candidate_id: int
):

    db = SessionLocal()

    candidate = db.query(
        Candidate
    ).filter(
        Candidate.id == candidate_id
    ).first()

    if not candidate:

        return {
            "error": "Candidate not found"
        }

    return candidate


@router.delete("/{candidate_id}")
def delete_candidate(
    candidate_id: int
):

    db = SessionLocal()

    candidate = db.query(
        Candidate
    ).filter(
        Candidate.id == candidate_id
    ).first()

    if not candidate:

        return {
            "error": "Candidate not found"
        }

    db.delete(candidate)

    db.commit()

    return {
        "message": "Candidate deleted successfully"
    }