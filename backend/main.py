from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from pdfminer.high_level import extract_text

app = FastAPI()

# Enable CORS (for frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Skills list (can expand later)
SKILLS = [
    "python", "java", "sql", "machine learning",
    "deep learning", "react", "fastapi", "django",
    "aws", "docker", "api", "backend"
]

# Extract text from PDF
def extract_resume_text(file):
    with open("temp.pdf", "wb") as f:
        f.write(file.file.read())
    text = extract_text("temp.pdf")
    return text.lower()

# Improved matching logic (BASED ON JOB DESCRIPTION)
def match_skills(resume_text, job_desc):
    resume_text = resume_text.lower()
    job_desc = job_desc.lower()

    job_skills = []
    matched = []
    missing = []

    for skill in SKILLS:
        if skill in job_desc:
            job_skills.append(skill)

            if skill in resume_text:
                matched.append(skill)
            else:
                missing.append(skill)

    if len(job_skills) == 0:
        score = 0
    else:
        score = int((len(matched) / len(job_skills)) * 100)

    return matched, missing, score

# Home route
@app.get("/")
def home():
    return {"message": "Resume Analyzer API running"}

# Main API
@app.post("/analyze")
async def analyze(
    file: UploadFile = File(...),
    job_desc: str = Form(...)
):
    resume_text = extract_resume_text(file)

    matched, missing, score = match_skills(resume_text, job_desc)

    return {
        "match_score": score,
        "matched_skills": matched,
        "missing_skills": missing
    }