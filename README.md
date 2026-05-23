# 🧠 QuizGenius AI

QuizGenius AI is an AI-Based Technical Quiz Generator developed using Python and Streamlit.  
The application helps users practice technical interview questions from different computer science and AI-related topics through interactive multiple-choice quizzes.

This project is designed for:
- Students
- Beginners in programming
- Technical interview preparation
- Internship project demonstrations
- Learning and self-assessment

---

# 🚀 Features

✅ Interactive Technical Quizzes  
✅ Multiple Topics Support  
✅ 5 Questions for Each Topic  
✅ Multiple Choice Questions  
✅ Real-Time Score Calculation  
✅ Correct Answer Display  
✅ Topic Information Section  
✅ Recommendation System  
✅ SQLite Database Integration  
✅ Simple and User-Friendly UI  
✅ Built using Python and Streamlit  

---

# 📚 Topics Included

- Python
- Java
- C Programming
- SQL
- Artificial Intelligence (AI)
- Machine Learning (ML)
- Generative AI (Gen AI)

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core Programming |
| Streamlit | Web Application UI |
| SQLite | Database Storage |
| Pyngrok | Public URL Generation |
| Random Module | Quiz Randomization |

---

# 📖 Topic Information Included

Each topic contains:
- Basic Introduction
- Applications
- Important Concepts
- Technical Knowledge
- Interview-Oriented Questions

---

# 🎯 Project Objectives

The main objective of this project is to:
- Help users improve technical knowledge
- Practice MCQ-based interview questions
- Learn programming and AI concepts
- Provide an interactive quiz experience
- Build a beginner-friendly educational platform

---

# 💻 Requirements

Install the following libraries before running the project:

```bash
pip install streamlit pyngrok
```

---

# ▶️ How to Run the Project

## Step 1 — Clone Repository

```bash
git clone https://github.com/yourusername/quizgenius-ai.git
```

---

## Step 2 — Open Project Folder

```bash
cd quizgenius-ai
```

---

## Step 3 — Run Streamlit Application

```bash
streamlit run app.py
```

---

# 🌐 Running in Google Colab

## Install Libraries

```python
!pip install streamlit pyngrok
```

---

## Run Streamlit

```python
!streamlit run app.py &>/content/logs.txt &
```

---

## Generate Public URL

```python
from pyngrok import ngrok

public_url = ngrok.connect(8501)

print(public_url)
```

---

# 📊 Database Functionality

The project uses SQLite database to:
- Store quiz scores
- Save user performance
- Manage quiz records

Database File:
```text
quizzes.db
```

---

# 🧠 Quiz Workflow

```text
Select Topic
      ↓
Generate Quiz
      ↓
Answer Questions
      ↓
Submit Quiz
      ↓
View Score
      ↓
Get Recommendations
```

---

# 📷 Application Features

### Quiz Generation
- Topic-based quizzes
- Multiple-choice questions
- Interactive answer selection

### Score Evaluation
- Automatic score calculation
- Correct answer checking
- Performance feedback

### Recommendation System
- Beginner-level recommendation
- Intermediate-level recommendation
- Advanced-level recommendation

---

# 🎓 Educational Benefits

This project helps users:
- Improve programming knowledge
- Practice technical MCQs
- Prepare for interviews
- Understand AI and ML concepts
- Learn database basics

---

# 🔥 Future Enhancements

Future improvements that can be added:
- Timer-based quizzes
- User authentication
- Leaderboard system
- AI-generated dynamic questions
- Difficulty levels
- Web deployment
- Analytics dashboard

---

# 📁 Project Structure

```text
quizgenius-ai/
│
├── app.py
├── quizzes.db
├── README.md
```


# 👩‍💻 Author

Sreeja Shetty

# 📌 Conclusion

QuizGenius AI is a beginner-friendly educational quiz platform that combines programming, AI concepts, and interactive learning into a single application.

The project demonstrates:
- Python programming
- Streamlit development
- Database integration
- Technical quiz generation
- Educational application design



