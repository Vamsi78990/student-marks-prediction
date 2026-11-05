import streamlit as st
import pandas as pd
import numpy as np
import os
import joblib

# Page Configuration
st.set_page_config(
    page_title="Student Marks Prediction",
    page_icon="🎓",
    layout="wide"
)

# Load Trained Model
model_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "models",
    "students_model.pkl"
)

model = joblib.load(model_path)

# Dashboard Title
st.title("🎓 Student Marks Prediction Dashboard")

st.write(
    "Predict student final marks using Machine Learning."
)

# User Inputs
st.header("Enter Student Details")

study_hours = st.number_input(
    "Study Hours",
    min_value=0.0,
    max_value=24.0,
    value=5.0
)

attendance = st.number_input(
    "Attendance (%)",
    min_value=0.0,
    max_value=100.0,
    value=75.0
)

previous_marks = st.number_input(
    "Previous Marks",
    min_value=0.0,
    max_value=100.0,
    value=70.0
)

sleep_hours = st.number_input(
    "Sleep Hours",
    min_value=0.0,
    max_value=24.0,
    value=7.0
)

social_media_hours = st.number_input(
    "Social Media Hours",
    min_value=0.0,
    max_value=24.0,
    value=2.0
)

# Prediction Button
if st.button("Predict Final Marks"):

    input_data = pd.DataFrame(
        [[
            study_hours,
            attendance,
            previous_marks,
            sleep_hours,
            social_media_hours
        ]],
        columns=[
            "StudyHours",
            "Attendance",
            "PreviousMarks",
            "SleepHours",
            "SocialMediaHours"
        ]
    )

    prediction = model.predict(input_data)

    predicted_marks = np.clip(prediction[0], 0, 100)

    st.success(
        f"Predicted Final Marks: {predicted_marks:.2f}"
    )
