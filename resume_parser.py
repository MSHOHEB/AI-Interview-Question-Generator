import io
import re

def extract_text_from_pdf(file):
    try:
        import PyPDF2
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text
    except Exception as e:
        return f"Error reading PDF: {str(e)}"

def extract_text_from_docx(file):
    try:
        import docx
        doc = docx.Document(file)
        text = "\n".join([para.text for para in doc.paragraphs])
        return text
    except Exception as e:
        return f"Error reading DOCX: {str(e)}"

def extract_text(uploaded_file):
    filename = uploaded_file.name.lower()
    file_bytes = io.BytesIO(uploaded_file.read())
    
    if filename.endswith(".pdf"):
        return extract_text_from_pdf(file_bytes)
    elif filename.endswith(".docx") or filename.endswith(".doc"):
        return extract_text_from_docx(file_bytes)
    else:
        return "Unsupported file format. Please upload PDF or DOCX."

def extract_skills(text, skills_db):
    text_lower = text.lower()
    # Clean text
    text_lower = re.sub(r'[^\w\s\+\#\.]', ' ', text_lower)
    
    found_skills = []
    for skill in skills_db:
        # Use word boundary matching for short skills to avoid false positives
        pattern = r'\b' + re.escape(skill) + r'\b'
        if re.search(pattern, text_lower):
            if skill not in found_skills:
                found_skills.append(skill)
    
    # Capitalize for display
    return [s.title() for s in found_skills]
