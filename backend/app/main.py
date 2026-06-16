from fastapi import FastAPI

from app.database import (
    Base,
    engine
)

from app.models.user import User
from app.models.candidate import Candidate
from app.models.job import Job

from app.routes.auth import (
    router as auth_router
)

from app.routes.candidates import (
    router as candidate_router
)

from app.routes.jobs import (
    router as job_router
)

Base.metadata.create_all(
    bind=engine
)

app = FastAPI(
    title="AI Resume Screening System"
)

app.include_router(
    auth_router
)

app.include_router(
    candidate_router
)

app.include_router(
    job_router
)

@app.get("/")
def root():
    return {
        "message": "Backend Running"
    }