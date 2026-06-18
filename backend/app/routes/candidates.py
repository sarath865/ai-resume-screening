from fastapi import APIRouter
from app.database import SessionLocal
from app.models.candidate import Candidate

router = APIRouter(
    prefix="/candidates",
    tags=["Candidates"]
)

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
        "message": "Candidate Deleted"
    }
