from app.utils.resume_parser import extract_email

text = """
Sarath Balaji
Email: sarath@gmail.com
"""

print(extract_email(text))