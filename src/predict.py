import joblib
import pandas as pd
import warnings
warnings.filterwarnings("ignore")


# Load trained model and feature columns
model = joblib.load("models/salary_model.pkl")
model_columns = joblib.load("models/model_columns.pkl")



def predict_salary(input_dict):
    """
    Predict salary from raw user input
    """

    # Convert input dictionary → DataFrame
    input_df = pd.DataFrame([input_dict])

    # One-Hot Encode input
    input_encoded = pd.get_dummies(input_df)

    # Align columns with training data
    input_encoded = input_encoded.reindex(
        columns=model_columns,
        fill_value=0
    )

    # Predict salary
    prediction = model.predict(input_encoded)

    return prediction[0]


if __name__ == "__main__":

    sample_input = {
        "work_year": 2023,
        "experience_level": "SE",
        "employment_type": "FT",
        "job_title": "Data Scientist",
        "employee_residence": "US",
        "remote_ratio": 100,
        "company_location": "US",
        "company_size": "M"
    }

    result = predict_salary(sample_input)

    print("Predicted Salary:", result)
