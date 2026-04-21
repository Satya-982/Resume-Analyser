# 🚀 Resume Analyzer (AI-Powered Job Matcher)

An AI-powered web application that analyzes resumes against job descriptions and provides a match score along with skill insights.

---

## 🧠 Features

* 📄 Upload resume (PDF)
* 📝 Paste job description
* 📊 Get match score (0–100%)
* ✅ Extract matched skills
* ❌ Identify missing skills

---

## 🛠️ Tech Stack

**Frontend**

* React.js
* Axios

**Backend**

* FastAPI
* Python

**NLP / Processing**

* PDFMiner (for resume parsing)
* Keyword-based skill matching (custom logic)

---

## 📂 Project Structure

```
resume-analyzer/
│
├── backend/
│   └── main.py
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
└── README.md
```

---

## ⚙️ How It Works

1. User uploads a resume (PDF)
2. Resume text is extracted using PDFMiner
3. Job description is analyzed
4. Skills are matched based on predefined keywords
5. Match score is calculated based on job requirements

---

## 🚀 Run Locally

### Backend

```
cd backend
pip install fastapi uvicorn pdfminer.six python-multipart
uvicorn main:app --reload
```

---

### Frontend

```
cd frontend
npm install
npm start
```

---

## 📊 Example Output

```
Match Score: 83%

Matched Skills:
Python, SQL, FastAPI

Missing Skills:
Machine Learning
```

---

## 📌 Future Improvements

* 🔍 Semantic matching using embeddings (NLP)
* 📈 Better scoring algorithm
* 🎨 Enhanced UI/UX
* ☁️ Deployment (cloud hosting)

---

## 👨‍💻 Author

**Marrivada Kota Satyanarayana**

* 📧 [satyamarrivada562@gmail.com](mailto:satyamarrivada562@gmail.com)
* 🔗 GitHub: https://github.com/Satya-982
* 🔗 LinkedIn: https://linkedin.com/in/satyamarrivada1292ab370

---

## ⭐ If you like this project

Give it a star ⭐ and feel free to contribute!
