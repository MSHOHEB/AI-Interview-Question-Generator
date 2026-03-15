# 🎯 AI Interview Question Generator

A Gemini-powered web app that reads your resume, extracts your skills, and generates fresh personalized interview questions — every single time.

---

## 🚀 How to Run (VS Code)

### Step 1: Download & Open Project
1. Extract the zip file
2. Open VS Code → `File > Open Folder` → Select `Interview_Question_Generator`

### Step 2: Open Terminal in VS Code
Press `` Ctrl + ` `` (backtick) to open the integrated terminal

### Step 3: Create Virtual Environment (recommended)
```bash
python -m venv venv
```
Activate it:
- **Windows:** `venv\Scripts\activate`
- **Mac/Linux:** `source venv/bin/activate`

### Step 4: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 5: Run the App
```bash
streamlit run app.py
```

The app will open automatically at **http://localhost:8501** 🎉

---

## 📁 Project Structure
```
Interview_Question_Generator/
├── app.py                  # Main Streamlit UI
├── resume_parser.py        # PDF/DOCX text extraction + skill detection
├── skills_db.py            # 100+ tech skills database
├── question_generator.py   # Gemini API integration
├── requirements.txt
└── README.md
```

---

## 🔑 API Key
Get your free Gemini API key at: https://aistudio.google.com/

---

## ✨ Features
- Upload PDF or DOCX resume
- Auto-detects 100+ technical skills
- Generates fresh questions via **Gemini 1.5 Flash** (never from a fixed database)
- Conceptual + Practical + Scenario-based questions per skill
- Download questions as TXT
- Gemini-inspired clean UI
