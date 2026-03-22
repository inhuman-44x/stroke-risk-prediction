from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import Optional
from app.model import predict_stroke_risk

app = FastAPI(title = "Stroke Risk Predictor")
templates = Jinja2Templates(directory = "app/templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "result": None})


@app.post("/predict", response_class=HTMLResponse)
async def predict(
    request: Request,
    age: float = Form(...),
    avg_glucose_level: float = Form(...),
    bmi: Optional[float] = Form(None),
    hypertension: int = Form(...),
    heart_disease: int = Form(...),
    gender: str = Form(...),
    ever_married: str = Form(...),
    work_type: str = Form(...),
    residence_type: str = Form(...),
    smoking_status: str = Form(...),
):
    input_data = {
        "age": age,
        "avg_glucose_level": avg_glucose_level,
        "bmi": bmi,
        "hypertension": hypertension,
        "heart_disease": heart_disease,
        "gender": gender,
        "ever_married": ever_married,
        "work_type": work_type,
        "residence_type": residence_type,
        "smoking_status": smoking_status,
    }

    result = predict_stroke_risk(input_data)

    return templates.TemplateResponse("index.html", {
        "request": request,
        "result": result,
        "form_data": input_data
    })