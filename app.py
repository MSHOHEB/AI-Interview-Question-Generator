import streamlit as st
from resume_parser import extract_text, extract_skills
from skills_db import SKILLS_DB
from question_generator import generate_interview_questions

# ─── Page Config ────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="AI Interview Question Generator",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─── Custom CSS (Gemini-inspired) ────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500;600&family=Roboto:wght@300;400;500&display=swap');

    html, body, [class*="css"] {
        font-family: 'Google Sans', 'Roboto', sans-serif;
        color: #202124 !important;
    }

    .stApp {
        background: linear-gradient(135deg, #f8f9ff 0%, #f0f4ff 100%) !important;
    }

    /* Force all text to be dark */
    p, span, div, label, h1, h2, h3, h4, h5, h6 {
        color: #202124;
    }

    [data-testid="stMarkdownContainer"] p,
    [data-testid="stMarkdownContainer"] span {
        color: #202124 !important;
    }

    /* Header */
    .main-header {
        text-align: center;
        padding: 2.5rem 1rem 1rem 1rem;
    }
    .main-header h1 {
        font-size: 2.8rem;
        font-weight: 600;
        background: linear-gradient(90deg, #4285F4, #9B59B6, #EA4335);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.5rem;
    }
    .main-header p {
        color: #5f6368;
        font-size: 1.1rem;
        font-weight: 400;
    }

    /* Cards */
    .card {
        background: white;
        border-radius: 16px;
        padding: 1.5rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.08), 0 4px 16px rgba(66,133,244,0.08);
        margin-bottom: 1rem;
        border: 1px solid #e8eaed;
        transition: box-shadow 0.2s;
    }
    .card:hover {
        box-shadow: 0 2px 8px rgba(0,0,0,0.12), 0 8px 24px rgba(66,133,244,0.12);
    }

    /* Upload Area */
    .upload-card {
        background: white;
        border-radius: 20px;
        padding: 2rem;
        text-align: center;
        border: 2px dashed #c5cae9;
        box-shadow: 0 2px 12px rgba(66,133,244,0.08);
        transition: border-color 0.2s;
    }
    .upload-card:hover {
        border-color: #4285F4;
    }

    /* Skill Tags */
    .skill-tag {
        display: inline-block;
        background: linear-gradient(135deg, #e8f0fe, #f3e5f5);
        color: #1a73e8;
        padding: 6px 16px;
        border-radius: 20px;
        margin: 4px;
        font-size: 0.88rem;
        font-weight: 500;
        border: 1px solid #c5cae9;
    }

    /* Generate Button */
    .stButton > button {
        background: linear-gradient(135deg, #4285F4 0%, #9B59B6 100%);
        color: white !important;
        border: none;
        border-radius: 24px;
        padding: 0.75rem 2.5rem;
        font-size: 1rem;
        font-weight: 500;
        font-family: 'Google Sans', sans-serif;
        cursor: pointer;
        transition: all 0.2s;
        box-shadow: 0 2px 8px rgba(66,133,244,0.3);
        width: 100%;
    }
    .stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 16px rgba(66,133,244,0.4);
    }

    /* Questions Output */
    .questions-container {
        background: white;
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 2px 12px rgba(0,0,0,0.08);
        border: 1px solid #e8eaed;
        line-height: 1.8;
    }

    /* Section titles */
    .section-title {
        font-size: 1.1rem;
        font-weight: 600;
        color: #1a73e8;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    /* Stats bar */
    .stat-pill {
        background: #e8f0fe;
        color: #1a73e8;
        padding: 4px 12px;
        border-radius: 12px;
        font-size: 0.85rem;
        font-weight: 500;
        display: inline-block;
        margin: 2px;
    }

    /* Divider */
    hr {
        border: none;
        border-top: 1px solid #e8eaed;
        margin: 1.5rem 0;
    }

    /* API Key Input */
    .stTextInput > div > div > input {
        border-radius: 12px;
        border: 1.5px solid #e8eaed;
        padding: 0.6rem 1rem;
        font-size: 0.95rem;
        transition: border-color 0.2s;
    }
    .stTextInput > div > div > input:focus {
        border-color: #4285F4;
        box-shadow: 0 0 0 3px rgba(66,133,244,0.15);
    }

    /* File uploader */
    [data-testid="stFileUploader"] {
        background: white;
        border-radius: 16px;
        padding: 1rem;
        border: 2px dashed #4285F4;
    }

    [data-testid="stFileUploaderDropzone"] {
        background: #f0f4ff !important;
        border-radius: 12px !important;
    }

    [data-testid="stFileUploaderDropzone"] * {
        color: #3c4043 !important;
    }

    /* Download button - dark */
    [data-testid="stDownloadButton"] > button {
        background: #202124 !important;
        color: white !important;
        border-radius: 24px !important;
        font-weight: 500 !important;
        border: none !important;
        padding: 0.75rem 2rem !important;
        width: 100% !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.3) !important;
    }
    [data-testid="stDownloadButton"] > button:hover {
        background: #3c4043 !important;
    }

    /* Success/Error messages */
    .stSuccess {
        border-radius: 12px;
    }
    .stError {
        border-radius: 12px;
    }

    /* Spinner */
    .stSpinner > div {
        border-top-color: #4285F4 !important;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background: white;
        border-right: 1px solid #e8eaed;
    }

    /* Expander */
    .streamlit-expanderHeader {
        background: #f8f9ff !important;
        border-radius: 12px !important;
        font-weight: 500 !important;
        color: #3c4043 !important;
    }

    /* Remove default streamlit padding */
    .block-container {
        padding-top: 0rem;
        max-width: 1100px;
    }
</style>
""", unsafe_allow_html=True)

# ─── Header ─────────────────────────────────────────────────────────────────
st.markdown("""
<div class="main-header">
    <h1>✨ AI Interview Question Generator</h1>
    <p>Upload your resume · Extract skills · Get personalized interview questions powered by Gemini</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ─── Layout ──────────────────────────────────────────────────────────────────
col_left, col_right = st.columns([1, 1.6], gap="large")

# ─── LEFT PANEL ──────────────────────────────────────────────────────────────
with col_left:
    st.markdown("### 📎 Upload Resume")
    uploaded_file = st.file_uploader(
        "Drop your resume here",
        type=["pdf", "docx"],
        label_visibility="collapsed",
        help="Supports PDF and DOCX formats"
    )

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 🔑 Gemini API Key")
    api_key = st.text_input(
        "Gemini API Key",
        type="password",
        placeholder="AIzaSy...",
        label_visibility="collapsed",
        help="Get your free API key from aistudio.google.com"
    )

    if uploaded_file and api_key:
        st.markdown("<br>", unsafe_allow_html=True)
        generate_btn = st.button("✨ Generate Interview Questions", use_container_width=True)
    else:
        st.markdown("<br>", unsafe_allow_html=True)
        st.button("✨ Generate Interview Questions", disabled=True, use_container_width=True)
        if not uploaded_file:
            st.caption("⬆️ Please upload your resume first")
        elif not api_key:
            st.caption("🔑 Please enter your Gemini API key")

    # Tips section
    st.markdown("<br>", unsafe_allow_html=True)
    with st.expander("💡 Tips for best results"):
        st.markdown("""
        - Use a well-formatted PDF or DOCX resume
        - Include clear skill sections in your resume
        - List programming languages, frameworks, and tools
        - The more skills listed, the more questions generated
        """)

    with st.expander("🔒 About your API key"):
        st.markdown("""
        - Your API key is used only for this session
        - It is never stored or logged
        - Get a free key at [aistudio.google.com](https://aistudio.google.com)
        """)

# ─── RIGHT PANEL ─────────────────────────────────────────────────────────────
with col_right:
    if uploaded_file:
        with st.spinner("📄 Parsing resume..."):
            resume_text = extract_text(uploaded_file)

        if resume_text.startswith("Error") or resume_text.startswith("Unsupported"):
            st.error(f"❌ {resume_text}")
        else:
            skills = extract_skills(resume_text, SKILLS_DB)

            if skills:
                st.markdown(f"""
                <div class="card">
                    <div class="section-title">🎯 Detected Skills <span class="stat-pill">{len(skills)} found</span></div>
                    <div>{"".join([f'<span class="skill-tag">{s}</span>' for s in skills])}</div>
                </div>
                """, unsafe_allow_html=True)

                # Store skills in session
                st.session_state["skills"] = skills
                st.session_state["resume_text_preview"] = resume_text[:300] + "..."
            else:
                st.warning("⚠️ No recognizable tech skills found. Try a more detailed resume.")

            # Show text preview
            with st.expander("📃 Resume Text Preview"):
                st.text_area("", resume_text[:800] + "..." if len(resume_text) > 800 else resume_text,
                             height=150, disabled=True)

    # ─── Generate Questions ──────────────────────────────────────────────────
    if uploaded_file and api_key and 'generate_btn' in dir() and generate_btn:
        if "skills" in st.session_state and st.session_state["skills"]:
            with st.spinner("🤖 Gemini is generating your personalized questions..."):
                try:
                    questions = generate_interview_questions(
                        st.session_state["skills"], api_key
                    )

                    st.markdown("""
                    <div class="section-title" style="margin-top:1rem;">
                        📋 Your Interview Questions
                    </div>
                    """, unsafe_allow_html=True)

                    st.markdown(f"""
                    <div class="questions-container">
                        {questions.replace(chr(10), '<br>').replace('## ', '<h3 style="color:#1a73e8;margin-top:1.5rem;">').replace('**Conceptual:**', '<strong style="color:#34a853;">📚 Conceptual:</strong>').replace('**Practical:**', '<strong style="color:#ea4335;">💻 Practical:</strong>').replace('**Scenario-Based:**', '<strong style="color:#fbbc04;">🌍 Scenario-Based:</strong>')}
                    </div>
                    """, unsafe_allow_html=True)

                    # Download button
                    st.markdown("<br>", unsafe_allow_html=True)
                    st.download_button(
                        label="⬇️ Download Questions as TXT",
                        data=questions,
                        file_name="interview_questions.txt",
                        mime="text/plain",
                        use_container_width=True
                    )

                    st.success(f"✅ Generated questions for {len(st.session_state['skills'])} skills!")

                except Exception as e:
                    st.error(f"❌ Error generating questions: {str(e)}")
                    st.info("💡 Make sure your Gemini API key is valid and has quota available.")
        else:
            st.warning("⚠️ No skills detected. Please upload a resume with clear skill mentions.")

    elif not uploaded_file:
        # Welcome state
        st.markdown("""
        <div class="card" style="text-align:center; padding: 3rem 2rem; border: 2px dashed #c5cae9;">
            <div style="font-size: 4rem; margin-bottom: 1rem;">🎯</div>
            <div style="font-size: 1.3rem; font-weight: 600; color: #3c4043; margin-bottom: 0.5rem;">Ready to prep for interviews?</div>
            <div style="color: #5f6368; font-size: 0.95rem;">Upload your resume on the left to get started.<br>Gemini will generate fresh, personalized questions just for you.</div>
        </div>
        """, unsafe_allow_html=True)

# ─── Footer ──────────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown("""
<div style="text-align:center; color:#9aa0a6; font-size:0.82rem; padding: 1rem;">
    Powered by <strong>Google Gemini 1.5 Flash</strong> · Built with <strong>Streamlit</strong> · NLP via <strong>Python regex + Skill DB</strong>
</div>
""", unsafe_allow_html=True)
