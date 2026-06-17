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

    return db.query(Job).all()

@router.get("/{job_id}")
def get_job(job_id: int):

    db = SessionLocal()

    job = db.query(Job).filter(
        Job.id == job_id
    ).first()

    if not job:
        return {
            "error": "Job not found"
        }

    return job

@router.put("/{job_id}")
def update_job(
    job_id: int,
    updated_job: JobCreate
):

    db = SessionLocal()

    job = db.query(Job).filter(
        Job.id == job_id
    ).first()

    if not job:
        return {
            "error": "Job not found"
        }

    job.title = updated_job.title
    job.required_skills = updated_job.required_skills
    job.experience_required = updated_job.experience_required
    job.location = updated_job.location
    job.employment_type = updated_job.employment_type
    job.description = updated_job.description

    db.commit()

    return {
        "message": "Job updated successfully"
    }

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
        "message": "Job deleted successfully"
    }
