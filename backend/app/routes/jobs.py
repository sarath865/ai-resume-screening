from fastapi import APIRouter
from app.database import SessionLocal
from app.models.job import Job
from app.schemas.job import JobCreate

router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"]
)

@router.post("/")
def create_job(job: JobCreate):

    db = SessionLocal()

    new_job = Job(
        title=job.title,
        required_skills=job.required_skills,
        experience_required=job.experience_required,
        location=job.location,
        employment_type=job.employment_type,
        description=job.description
    )

    db.add(new_job)
    db.commit()
    db.refresh(new_job)

    return new_job


@router.get("/")
def get_jobs():

    db = SessionLocal()

    jobs = db.query(Job).all()

    return jobs


@router.get("/{job_id}")
def get_job(job_id: int):

    db = SessionLocal()

    job = db.query(Job).filter(
        Job.id == job_id
    ).first()

    return job


@router.delete("/{job_id}")
def delete_job(job_id: int):

    db = SessionLocal()

    job = db.query(Job).filter(
        Job.id == job_id
    ).first()

    if not job:
        return {
            "error": "Job not found"
        }

    db.delete(job)
    db.commit()

    return {
        "message": "Job Deleted"
    }