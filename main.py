from fastapi import FastAPI
from math_main import analyze_eq
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Equational Hunt API is running"}

@app.get("/analyze")
def analyze(equation:str):
    return analyze_eq(equation)
