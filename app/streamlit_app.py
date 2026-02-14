import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import streamlit as st
from src.predict import predict_salary

st.title("💼 Data Science Salary Predictor")

st.write("Enter job details to predict salary in USD")

# ---- User Inputs ----

work_year = st.number_input("Work Year", 2020, 2030, 2023)

experience_level = st.selectbox(
    "Experience Level",
    ["EN", "MI", "SE", "EX"]
)

employment_type = st.selectbox(
    "Employment Type",
    ["FT", "PT", "CT", "FL"]
)

job_title = st.text_input("Job Title", "Data Scientist")

employee_residence = st.text_input("Employee Residence", "US")

remote_ratio = st.slider("Remote Ratio (%)", 0, 100, 100)

company_location = st.text_input("Company Location", "US")

company_size = st.selectbox(
    "Company Size",
    ["S", "M", "L"]
)

# ---- Prediction Button ----

if st.button("Predict Salary 💰"):

    input_data = {
        "work_year": work_year,
        "experience_level": experience_level,
        "employment_type": employment_type,
        "job_title": job_title,
        "employee_residence": employee_residence,
        "remote_ratio": remote_ratio,
        "company_location": company_location,
        "company_size": company_size
    }

    prediction = predict_salary(input_data)

    st.success(f"Predicted Salary: ${prediction:,.2f}")
