from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

from app.routes.portfolio import router as portfolio_router

load_dotenv()

app = FastAPI()

FRONTEND_URL = os.getenv("FRONTEND_URL")

origins = [FRONTEND_URL] if FRONTEND_URL else ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(portfolio_router)

@app.get("/")
def root():
    return {"message": "Portfolio API Running"}

@app.get("/health")
def health():
    return {"Status": "Ok"}
