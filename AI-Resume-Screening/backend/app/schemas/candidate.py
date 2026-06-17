from pydantic import BaseModel

class CandidateResponse(BaseModel):
    id: int
    name: str | None = None
    email: str | None = None
    phone: str | None = None
    skills: str | None = None
