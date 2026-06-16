import pdfplumber
import docx
import re


def extract_text_from_pdf(file_path):

    text = ""

    with pdfplumber.open(file_path) as pdf:

        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text


def extract_text_from_docx(file_path):

    document = docx.Document(file_path)

    text = "\n".join(
        para.text for para in document.paragraphs
    )

    return text


def extract_email(text):

    match = re.search(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        text
    )

    return match.group(0) if match else None


def extract_phone(text):

    match = re.search(
        r"(\+?\d[\d\s\-]{8,15})",
        text
    )

    return match.group(0) if match else None


def extract_skills(text):

    skills_db = [
        "Python",
        "Java",
        "JavaScript",
        "React",
        "FastAPI",
        "Django",
        "Flask",
        "SQL",
        "PostgreSQL",
        "MySQL",
        "Docker",
        "AWS",
        "Git",
        "Machine Learning",
        "TensorFlow",
        "PyTorch"
    ]

    found_skills = []

    text_lower = text.lower()

    for skill in skills_db:

        if skill.lower() in text_lower:
            found_skills.append(skill)

    return found_skills