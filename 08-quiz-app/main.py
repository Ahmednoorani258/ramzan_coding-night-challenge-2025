import streamlit as st
import random
import time
st.title("Quiz App")

questions = [
    {
        "question": "What is the capital of France?",
        "answers": ["Paris", "London", "Berlin", "Madrid"],
        "correct_answer": "Paris"
    },
    {
        "question": "What is the capital of Germany?",
        "answers": ["Paris", "London", "Berlin", "Madrid"],
        "correct_answer": "Berlin"
    },
    {
        "question": "What is the capital of Spain?",
        "answers": ["Paris", "London", "Berlin", "Madrid"],
        "correct_answer": "Madrid"
    },
    {
        "question": "What is the capital of Italy?",
        "answers": ["Paris", "London", "Rome", "Madrid"],
        "correct_answer": "Rome"
    },
    {
        "question": "What is the capital of the United Kingdom?",
        "answers": ["Paris", "London", "Berlin", "Madrid"],
        "correct_answer": "London"
    },
]

if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(questions)

question = st.session_state.current_question
st.subheader(question["question"])
selected_answer = st.radio("Select an answer", question["answers"], key="answer")

if st.button("Submit"):
    if selected_answer == question["correct_answer"]:
        st.success("Correct!")
    else:
        st.error("Incorrect! the correct answer is: " + question["correct_answer"])

    time.sleep(3)
    st.session_state.current_question = random.choice(questions)
    st.rerun()