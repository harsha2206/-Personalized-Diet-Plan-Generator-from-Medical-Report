from fastapi import FastAPI
from database import engine, Base
from schemas import PatientCreate
from ml_engine import analyze_health
from diet_generator import generate_diet
from pdf_export import create_pdf

app = FastAPI(title="AI-NutriCare")

Base.metadata.create_all(bind=engine)

@app.post("/generate-plan/")
def generate_plan(patient: PatientCreate):

    conditions = analyze_health(patient.hba1c, patient.ldl)
    diet = generate_diet(conditions)

    filename = f"{patient.name}_DietPlan.pdf"
    create_pdf(filename, patient.name, diet)

    return {
        "conditions_detected": conditions,
        "diet_plan": diet,
        "pdf_generated": filename
    }
