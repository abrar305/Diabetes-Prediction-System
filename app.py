import streamlit as st
from main import predict_diabetes

st.set_page_config(
    page_title="Diabetes Prediction",
    layout="centered"
)

st.title(" Diabetes Prediction System")

st.write("Enter the patient's information below.")

name = st.text_input("Patient Name")

gender = st.selectbox(
    "Gender",
    ["Female", "Male", "Other"]
)

age = st.slider(
    "Age",
    1,
    100,
    25
)

race = st.selectbox(
    "Race",
    [
        "AfricanAmerican",
        "Asian",
        "Caucasian",
        "Hispanic",
        "Other"
    ]
)

hypertension = st.checkbox("Hypertension")

heart_disease = st.checkbox("Heart Disease")

smoking_history = st.selectbox(
    "Smoking History",
    [
        "never",
        "former",
        "ever",
        "current"
    ]
)

bmi = st.number_input(
    "BMI",
    min_value=5.0,
    max_value=100.0,
    value=25.0
)

hba1c = st.number_input(
    "HbA1c Level",
    min_value=1.0,
    max_value=15.0,
    value=5.0
)

blood_glucose = st.number_input(
    "Blood Glucose Level",
    min_value=30,
    max_value=400,
    value=100
)

if st.button("Predict"):

    race_values = [
        1 if race == r else 0
        for r in [
            "AfricanAmerican",
            "Asian",
            "Caucasian",
            "Hispanic",
            "Other"
        ]
    ]

    input_data = [[
        gender,
        age,
        *race_values,
        int(hypertension),
        int(heart_disease),
        smoking_history,
        bmi,
        hba1c,
        blood_glucose
    ]]

    prediction, probability = predict_diabetes(input_data)

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error(f" High Risk of Diabetes")
        st.write(f"Model Probability: {probability:.2%}")
    else:
       st.success(f" Low Risk of Diabetes")
       st.write(f"Model Probability: {probability:.2%}")