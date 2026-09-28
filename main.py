from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from math_main import analyze_eq
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Equational Hunt API is running"}

@app.get("/analyze")
def analyze(equation:str):
    return analyze_eq(equation)
