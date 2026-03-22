import joblib
import pandas as pd
import numpy as np
from pathlib import Path
import json

MODEL_PATH = Path("model/stroke_model.pkl")
model = joblib.load(MODEL_PATH)

with open("model/thresholds.json") as f:
    thresholds = json.load(f)

low_cutoff = thresholds["low_cutoff"]
high_cutoff = thresholds["high_cutoff"]

def predict_stroke_risk(input_data: dict) -> dict:

    bmi = input_data.get("bmi")
    bmi_missing = 1 if bmi is None else 0
    bmi_value = bmi if bmi is not None else 0.0

    df = pd.DataFrame([{
        "age": float(input_data["age"]),
        "avg_glucose_level": float(input_data["avg_glucose_level"]),
        "bmi": float(bmi_value),
        "bmi_missing": int(bmi_missing),
        "hypertension": int(input_data["hypertension"]),
        "heart_disease": int(input_data["heart_disease"]),
        "gender": input_data["gender"],
        "ever_married": input_data["ever_married"],
        "work_type": input_data["work_type"],
        "residence_type": input_data["residence_type"],
        "smoking_status": input_data["smoking_status"],
    }])

    prob = model.predict_proba(df)[0][1]
    prediction = 1 if prob >= low_cutoff else 0

    if prob >= high_cutoff:
        risk_level = "High"
        risk_color = "high"
        advice = "Several high-risk factors detected. Please seek medical advice promptly."
    elif prob >= low_cutoff:
        risk_level = "Moderate"
        risk_color = "moderate"
        advice = "Some risk factors are present. Consider consulting a healthcare professional."
    else:
        risk_level = "Low"
        risk_color = "low"
        advice = "Your risk indicators look favourable. Maintain a healthy lifestyle."

    return {
        "probability": round(prob * 100, 1),
        "prediction": int(prediction),
        "risk_level": risk_level,
        "risk_color": risk_color,
        "advice": advice,
        "bmi_missing": bmi_missing,
    }

