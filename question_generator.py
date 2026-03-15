import google.generativeai as genai

def generate_interview_questions(skills: list, api_key: str) -> str:
    genai.configure(api_key=api_key)

    skills_str = ", ".join(skills)  # All skills, no limit

    prompt = f"""Act as a technical interviewer. For each skill in [{skills_str}], give exactly 3 interview questions (1 conceptual, 1 practical, 1 scenario). Be concise.

Format:
## [Skill]
1. (Conceptual) question
2. (Practical) question  
3. (Scenario) question
---
"""
    model = genai.GenerativeModel("gemini-2.5-flash-lite")
    response = model.generate_content(prompt)
    return response.text
