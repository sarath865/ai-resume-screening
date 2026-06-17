import re
import pdfplumber
from docx import Document

def extract_text(file_path):

    text = ""

    if file_path.endswith(".pdf"):

        with pdfplumber.open(file_path) as pdf:

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:

                    text += page_text + "\n"

    elif file_path.endswith(".docx"):

        doc = Document(file_path)

        for para in doc.paragraphs:

            text += para.text + "\n"

    return text


def extract_email(text):

    match = re.search(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        text
    )

    return match.group(0) if match else ""


def extract_phone(text):

    match = re.search(
        r"\+?\d[\d\s\-]{8,15}",
        text
    )

    return match.group(0) if match else ""


def extract_skills(text):

    skills_db = [
        "Python",
        "FastAPI",
        "Django",
        "Flask",
        "SQL",
        "MySQL",
        "PostgreSQL",
        "React",
        "Java",
        "JavaScript",
        "Docker",
        "Git"
    ]

    found_skills = []

    for skill in skills_db:

        if skill.lower() in text.lower():

            found_skills.append(skill)

    return ", ".join(found_skills)
