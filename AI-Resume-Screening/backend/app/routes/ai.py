from fastapi import APIRouter
from app.database import SessionLocal

from app.models.candidate import Candidate
from app.models.job import Job

router = APIRouter(
    prefix="/ai",
    tags=["AI"]
)

@router.post("/match")
def match_candidate(
    candidate_id: int,
    job_id: int
):

    db = SessionLocal()

    candidate = db.query(Candidate).filter(
        Candidate.id == candidate_id
    ).first()

    job = db.query(Job).filter(
        Job.id == job_id
    ).first()

    if not candidate:
        return {"error": "Candidate not found"}

    if not job:
        return {"error": "Job not found"}

    candidate_skills = []

    if candidate.skills:
        candidate_skills = [
            skill.strip().lower()
            for skill in candidate.skills.split(",")
        ]

    required_skills = [
        skill.strip().lower()
        for skill in job.required_skills.split(",")
    ]

    matching_skills = []
    missing_skills = []

    for skill in required_skills:

        if skill in candidate_skills:
            matching_skills.append(skill)

        else:
            missing_skills.append(skill)

    score = int(
        (len(matching_skills) / len(required_skills))
        * 100
    )

    return {
        "candidate_id": candidate.id,
        "candidate_name": candidate.name,
        "job_id": job.id,
        "job_title": job.title,
        "match_score": score,
        "matching_skills": matching_skills,
        "missing_skills": missing_skills,
        "strengths": matching_skills,
        "weaknesses": missing_skills
    }

@router.post("/summary")
def candidate_summary(candidate_id: int):

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

    summary = f"""
Candidate: {candidate.name}

Skills:
{candidate.skills}

Email:
{candidate.email}

Phone:
{candidate.phone}
"""

    return {
        "summary": summary,
        "recommendation":
        "Recommended for Interview"
    }

@router.post("/questions")
def generate_questions(candidate_id: int):

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

    questions = []

    if candidate.skills:

        for skill in candidate.skills.split(","):

            questions.append(
                f"Explain your experience with {skill.strip()}?"
            )

    questions.extend([
        "Tell me about yourself.",
        "What are your strengths?",
        "Describe a challenging project."
    ])

    return {
        "candidate": candidate.name,
        "questions": questions
    }
