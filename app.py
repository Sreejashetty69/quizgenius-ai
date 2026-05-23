```python
%%writefile app.py

import streamlit as st
import sqlite3

# -----------------------------------
# DATABASE SETUP
# -----------------------------------

conn = sqlite3.connect(
    "quizzes.db",
    check_same_thread=False
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS scores(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    topic TEXT,
    score INTEGER
)
""")

conn.commit()

# -----------------------------------
# QUIZ QUESTIONS DATA
# -----------------------------------

quiz_data = {

    "python": [

        {
            "question": "What is Python?",
            "options": [
                "Programming Language",
                "Database",
                "Operating System",
                "Compiler"
            ],
            "answer": "Programming Language"
        },

        {
            "question": "Who developed Python?",
            "options": [
                "James Gosling",
                "Dennis Ritchie",
                "Guido van Rossum",
                "Bjarne Stroustrup"
            ],
            "answer": "Guido van Rossum"
        },

        {
            "question": "Which keyword is used to define a function?",
            "options": [
                "func",
                "define",
                "def",
                "function"
            ],
            "answer": "def"
        },

        {
            "question": "Which data type is mutable?",
            "options": [
                "Tuple",
                "String",
                "List",
                "Integer"
            ],
            "answer": "List"
        },

        {
            "question": "Python is mainly used for?",
            "options": [
                "AI",
                "Web Development",
                "Automation",
                "All of the above"
            ],
            "answer": "All of the above"
        }

    ],

    "java": [

        {
            "question": "Java is a?",
            "options": [
                "Programming Language",
                "Database",
                "IDE",
                "Compiler"
            ],
            "answer": "Programming Language"
        },

        {
            "question": "Who developed Java?",
            "options": [
                "James Gosling",
                "Dennis Ritchie",
                "Guido van Rossum",
                "Linus Torvalds"
            ],
            "answer": "James Gosling"
        },

        {
            "question": "JVM stands for?",
            "options": [
                "Java Variable Machine",
                "Java Virtual Machine",
                "Joint Virtual Machine",
                "Java Verified Machine"
            ],
            "answer": "Java Virtual Machine"
        },

        {
            "question": "Which concept supports code reusability?",
            "options": [
                "Inheritance",
                "Encapsulation",
                "Polymorphism",
                "Abstraction"
            ],
            "answer": "Inheritance"
        },

        {
            "question": "Java follows which programming paradigm?",
            "options": [
                "Procedural",
                "Object-Oriented",
                "Functional",
                "Logic"
            ],
            "answer": "Object-Oriented"
        }

    ],

    "c": [

        {
            "question": "Who developed C language?",
            "options": [
                "James Gosling",
                "Dennis Ritchie",
                "Guido van Rossum",
                "Bjarne Stroustrup"
            ],
            "answer": "Dennis Ritchie"
        },

        {
            "question": "C language is a?",
            "options": [
                "High-level",
                "Low-level",
                "Middle-level",
                "Assembly language"
            ],
            "answer": "Middle-level"
        },

        {
            "question": "Which symbol is used for address operator?",
            "options": [
                "%",
                "*",
                "&",
                "@"
            ],
            "answer": "&"
        },

        {
            "question": "Which function is entry point in C?",
            "options": [
                "start()",
                "main()",
                "execute()",
                "run()"
            ],
            "answer": "main()"
        },

        {
            "question": "C supports?",
            "options": [
                "Pointers",
                "Arrays",
                "Functions",
                "All of the above"
            ],
            "answer": "All of the above"
        }

    ],

    "sql": [

        {
            "question": "SQL stands for?",
            "options": [
                "Structured Query Language",
                "Simple Query Language",
                "Sequential Query Language",
                "System Query Language"
            ],
            "answer": "Structured Query Language"
        },

        {
            "question": "Which command is used to retrieve data?",
            "options": [
                "GET",
                "FETCH",
                "SELECT",
                "DISPLAY"
            ],
            "answer": "SELECT"
        },

        {
            "question": "Which command removes all rows but keeps table structure?",
            "options": [
                "DELETE",
                "DROP",
                "TRUNCATE",
                "REMOVE"
            ],
            "answer": "TRUNCATE"
        },

        {
            "question": "Which key uniquely identifies records?",
            "options": [
                "Foreign Key",
                "Primary Key",
                "Alternate Key",
                "Composite Key"
            ],
            "answer": "Primary Key"
        },

        {
            "question": "Which clause filters rows?",
            "options": [
                "ORDER BY",
                "GROUP BY",
                "WHERE",
                "HAVING"
            ],
            "answer": "WHERE"
        }

    ],

    "ai": [

        {
            "question": "AI stands for?",
            "options": [
                "Artificial Intelligence",
                "Automated Internet",
                "Advanced Interface",
                "Artificial Internet"
            ],
            "answer": "Artificial Intelligence"
        },

        {
            "question": "AI is mainly used for?",
            "options": [
                "Automation",
                "Prediction",
                "Decision Making",
                "All of the above"
            ],
            "answer": "All of the above"
        },

        {
            "question": "Which field is related to AI?",
            "options": [
                "Machine Learning",
                "NLP",
                "Computer Vision",
                "All of the above"
            ],
            "answer": "All of the above"
        },

        {
            "question": "Chatbots are example of?",
            "options": [
                "AI",
                "Database",
                "Compiler",
                "OS"
            ],
            "answer": "AI"
        },

        {
            "question": "AI systems simulate?",
            "options": [
                "Human Intelligence",
                "Networks",
                "Databases",
                "Compilers"
            ],
            "answer": "Human Intelligence"
        }

    ],

    "ml": [

        {
            "question": "ML stands for?",
            "options": [
                "Machine Learning",
                "Memory Learning",
                "Model Learning",
                "Machine Logic"
            ],
            "answer": "Machine Learning"
        },

        {
            "question": "ML is a subset of?",
            "options": [
                "AI",
                "DBMS",
                "Networking",
                "Cloud Computing"
            ],
            "answer": "AI"
        },

        {
            "question": "Which learning uses labeled data?",
            "options": [
                "Supervised Learning",
                "Unsupervised Learning",
                "Reinforcement Learning",
                "Deep Learning"
            ],
            "answer": "Supervised Learning"
        },

        {
            "question": "Which library is used in ML?",
            "options": [
                "NumPy",
                "Pandas",
                "Scikit-learn",
                "All of the above"
            ],
            "answer": "All of the above"
        },

        {
            "question": "Which algorithm is used in ML?",
            "options": [
                "Linear Regression",
                "Decision Trees",
                "KNN",
                "All of the above"
            ],
            "answer": "All of the above"
        }

    ],

    "gen ai": [

        {
            "question": "Generative AI is used to?",
            "options": [
                "Generate Content",
                "Delete Data",
                "Store Files",
                "Manage Networks"
            ],
            "answer": "Generate Content"
        },

        {
            "question": "ChatGPT is an example of?",
            "options": [
                "Compiler",
                "Generative AI",
                "Database",
                "Operating System"
            ],
            "answer": "Generative AI"
        },

        {
            "question": "Which company developed Gemini?",
            "options": [
                "Google",
                "Microsoft",
                "Amazon",
                "Meta"
            ],
            "answer": "Google"
        },

        {
            "question": "Generative AI creates?",
            "options": [
                "Text",
                "Images",
                "Code",
                "All of the above"
            ],
            "answer": "All of the above"
        },

        {
            "question": "Generative AI mainly uses?",
            "options": [
                "Deep Learning",
                "Networking",
                "DBMS",
                "Compiler Design"
            ],
            "answer": "Deep Learning"
        }

    ]

}

# -----------------------------------
# TOPIC INFORMATION
# -----------------------------------

topic_info = {

    "python": "Python is used in AI, ML, Web Development, Automation and Data Science.",

    "java": "Java is an object-oriented programming language used in enterprise and Android applications.",

    "c": "C language is used in operating systems, compilers and embedded systems.",

    "sql": "SQL is used to manage and manipulate relational databases.",

    "ai": "Artificial Intelligence simulates human intelligence using machines.",

    "ml": "Machine Learning enables systems to learn patterns from data.",

    "gen ai": "Generative AI creates text, images, code and other content."
}

# -----------------------------------
# STREAMLIT PAGE
# -----------------------------------

st.set_page_config(
    page_title="QuizGenius AI",
    layout="centered"
)

st.title("🧠 QuizGenius AI")

st.subheader(
    "AI-Based Technical Quiz Generator"
)

# -----------------------------------
# USER INPUTS
# -----------------------------------

username = st.text_input(
    "Enter Your Name"
)

topic = st.selectbox(
    "Select Topic",
    [
        "python",
        "java",
        "c",
        "sql",
        "ai",
        "ml",
        "gen ai"
    ]
)

# -----------------------------------
# TOPIC INFORMATION
# -----------------------------------

st.subheader("📚 Topic Information")

st.info(topic_info[topic])

# -----------------------------------
# SESSION STATE
# -----------------------------------

if "show_quiz" not in st.session_state:
    st.session_state.show_quiz = False

# -----------------------------------
# GENERATE QUIZ
# -----------------------------------

if st.button("Generate Quiz"):
    st.session_state.show_quiz = True

# -----------------------------------
# DISPLAY QUIZ
# -----------------------------------

if st.session_state.show_quiz:

    st.subheader(f"📘 {topic.upper()} Quiz")

    questions = quiz_data[topic]

    user_answers = []

    for i, q in enumerate(questions):

        st.write(f"### Q{i+1}. {q['question']}")

        selected = st.radio(
            "Choose your answer:",
            q["options"],
            key=f"{topic}_question_{i}"
        )

        user_answers.append(selected)

        st.markdown("---")

    # -----------------------------------
    # SUBMIT QUIZ
    # -----------------------------------

    if st.button("Submit Quiz"):

        score_count = 0

        for i, q in enumerate(questions):

            if user_answers[i] == q["answer"]:

                score_count += 1

        st.success(
            f"✅ You scored {score_count} out of {len(questions)}"
        )

        st.balloons()

        st.subheader("📌 Correct Answers")

        for i, q in enumerate(questions):

            st.write(
                f"Q{i+1}: {q['answer']}"
            )

# -----------------------------------
# SAVE SCORE SECTION
# -----------------------------------

st.subheader("🎯 Save Your Score")

score = st.slider(
    "Select Your Score",
    0,
    100,
    50
)

if st.button("Save Score"):

    cursor.execute(
        "INSERT INTO scores(username, topic, score) VALUES (?, ?, ?)",
        (username, topic, score)
    )

    conn.commit()

    st.success(
        "Score Saved Successfully!"
    )

# -----------------------------------
# AI RECOMMENDATION
# -----------------------------------

st.subheader("🧠 AI Recommendation")

if score < 50:

    st.warning(
        "Practice beginner-level quizzes."
    )

elif score < 80:

    st.info(
        "Try medium and hard quizzes."
    )

else:

    st.success(
        "Excellent! Try interview-level questions."
    )

# -----------------------------------
# FOOTER
# -----------------------------------

st.markdown("---")

st.markdown(
    "🚀 Built using Python and Streamlit"
)
```
