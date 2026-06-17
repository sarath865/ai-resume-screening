from fastapi import APIRouter

from app.database import SessionLocal
from app.models.candidate import Candidate
from app.models.job import Job

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)

@router.get("/")
def dashboard():

    db = SessionLocal()

    total_candidates = db.query(
        Candidate
    ).count()

    total_jobs = db.query(
        Job
    ).count()

    return {
        "total_candidates":
        total_candidates,

        "total_jobs":
        total_jobs
    }
