from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine

from app.models.user import User
from app.models.candidate import Candidate
from app.models.job import Job

from app.routes.auth import router as auth_router
from app.routes.candidates import router as candidate_router
from app.routes.jobs import router as job_router
from app.routes.analytics import router as analytics_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Resume Screening System"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(candidate_router)
app.include_router(job_router)
app.include_router(analytics_router)


@app.get("/")
def root():
    return {
        "message": "Backend Running Successfully"
    }