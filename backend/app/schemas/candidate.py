from pydantic import BaseModel

class CandidateResponse(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    skills: str

    class Config:
        from_attributes = True