from tensorflow.keras.models import load_model
import pandas as pd
import joblib
model = load_model("diabetes_model.keras")
encoder = joblib.load("encoder.pkl")
model_columns = joblib.load("model_columns.pkl")

cat_cols = ["gender", "smoking_history"]
columns = [
    "gender",
    "age",
    "race:AfricanAmerican",
    "race:Asian",
    "race:Caucasian",
    "race:Hispanic",
    "race:Other",
    "hypertension",
    "heart_disease",
    "smoking_history",
    "bmi",
    "hbA1c_level",
    "blood_glucose_level"
]

def predict_diabetes(input_data):
    data = pd.DataFrame(input_data, columns=columns)
    encoded_data = encoder.transform(data[cat_cols])
    encoded_data = pd.DataFrame(
        encoded_data,
        columns=encoder.get_feature_names_out(cat_cols),
        index=data.index
    )
    data = data.drop(columns=cat_cols)
    data = pd.concat([data, encoded_data], axis=1)
    data = data.reindex(columns=model_columns, fill_value=0)
    prediction = model.predict(data, verbose=0)

    probability = float(prediction[0][0])

    if probability >= 0.5:
        return 1, probability
    else:
        return 0, probability