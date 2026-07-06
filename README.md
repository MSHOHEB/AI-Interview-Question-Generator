---

## 🚀 How to Run (VS Code)

### Step 1 — Download & Open Project
1. Extract the zip file
2. Open VS Code → `File > Open Folder` → Select `Interview_Question_Generator`

### Step 2 — Open Terminal
Press Ctrl + ` (backtick) to open the integrated terminal

### Step 3 — Create Virtual Environment
    python -m venv venv

Activate it:
- **Windows:** `venv\Scripts\activate`
- **Mac/Linux:** `source venv/bin/activate`

### Step 4 — Install Dependencies
    pip install -r requirements.txt

### Step 5 — Add Your API Key
Get your free Gemini API key at: https://aistudio.google.com/

### Step 6 — Run the App
    streamlit run app.py

The app will open automatically at **http://localhost:8501** 🎉

---

## 📁 Project Structure

| File | Description |
|------|-------------|
| `app.py` | Main Streamlit UI |
| `resume_parser.py` | PDF/DOCX text extraction + skill detection |
| `skills_db.py` | 100+ tech skills database |
| `question_generator.py` | Gemini API integration |
| `requirements.txt` | Python dependencies |
| `README.md` | Project documentation |

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python 3.10+** | Core language |
| **Streamlit** | Web UI framework |
| **Gemini 1.5 Flash** | AI question generation |
| **PyPDF2 / pdfplumber** | PDF text extraction |
| **python-docx** | DOCX file reading |
| **Google Generative AI** | Gemini API client |

---

## 🎯 Use Cases

- 🎓 **Students** — Practice before campus placements
- 💼 **Job Seekers** — Prepare for technical interviews
- 🧑‍💻 **Developers** — Test knowledge in new tech stacks
- 🏢 **HR Teams** — Generate questions for candidate interviews
- 📚 **Trainers** — Create quiz content from skills

---

## 🔍 How It Works

    1. Upload Resume (PDF or DOCX)
            ↓
    2. resume_parser.py extracts text
            ↓
    3. skills_db.py matches 100+ skills
            ↓
    4. question_generator.py calls Gemini API
            ↓
    5. Fresh questions displayed on screen
            ↓
    6. Download as TXT file

---

## 💡 Future Updates

- [ ] Support for more file formats (TXT, PNG)
- [ ] Difficulty level selection (Easy/Medium/Hard)
- [ ] Export questions as PDF
- [ ] Interview timer mode
- [ ] Answer hints toggle
- [ ] Multi-language support
- [ ] Company-specific question mode (Google, Amazon, TCS)
- [ ] Save question history

---

## 📅 Daily Development Log

| Day | Update |
|-----|--------|
| Day 1 | ✅ Project setup and basic UI |
| Day 2 | ✅ Resume PDF/DOCX parser built |
| Day 3 | ✅ Skills database (100+ skills) created |
| Day 4 | ✅ Gemini API integration done |
| Day 5 | ✅ Question generation logic completed |
| Day 6 | ✅ Download TXT feature added |
| Day 7 | ✅ UI styling and cleanup |
| Day 8 | ✅ Testing and bug fixes |
| Day 9 | ✅ README and documentation updated |

---

## 🤝 Contributing

Pull requests are welcome!
For major changes, please open an issue first.

---

## 📄 License

MIT License — free to use for learning and portfolio purposes.


