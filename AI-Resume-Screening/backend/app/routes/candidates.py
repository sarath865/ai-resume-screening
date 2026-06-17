from fastapi import APIRouter, UploadFile, File
from app.database import SessionLocal
from app.models.candidate import Candidate

from app.utils.resume_parser import (
    extract_text,
    extract_email,
    extract_phone,
    extract_skills
)

import os

router = APIRouter(
    prefix="/candidates",
    tags=["Candidates"]
)

UPLOAD_DIR = "uploads"

@router.post("/upload")
async def upload_resume(
    file: UploadFile = File(...)
):

    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        buffer.write(
            await file.read()
        )

    text = extract_text(file_path)

    email = extract_email(text)
    phone = extract_phone(text)
    skills = extract_skills(text)

    db = SessionLocal()

    candidate = Candidate(
        name=file.filename,
        email=email,
        phone=phone,
        skills=skills,
        resume_path=file_path
    )

    db.add(candidate)
    db.commit()
    db.refresh(candidate)

    return {
        "id": candidate.id,
        "name": candidate.name,
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
def get_candidate(candidate_id: int):

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
def delete_candidate(candidate_id: int):

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
