from sqlalchemy import Column, Integer, String, Text
from app.database import Base

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String)
    required_skills = Column(Text)
    experience_required = Column(String)
    location = Column(String)
    employment_type = Column(String)
    description = Column(Text)
