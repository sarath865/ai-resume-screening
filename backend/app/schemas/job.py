from pydantic import BaseModel

class JobCreate(BaseModel):
    title: str
    required_skills: str
    experience_required: str
    location: str
    employment_type: str
    description: str