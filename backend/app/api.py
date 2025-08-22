# api.py
# API routes and logic

# Definisce gli endpoint REST e usa le funzioni di autenticazione e ChatGPT:


from fastapi import APIRouter, Depends, HTTPException, Security
from fastapi.security import HTTPBearer
from app.auth import verify_token
from app.chatgpt import get_questions, get_interpretation


security = HTTPBearer()
router = APIRouter()
print("API router initialized.")


@router.post("/questions", dependencies=[Security(security)])
def questions(sogno: str, user=Depends(verify_token)):
    print("domande...")
    return {"domande": get_questions(sogno)}


@router.post("/interpretation", dependencies=[Security(security)])
def interpretation(sogno: str, risposte: list, user=Depends(verify_token)):
    print("interpretazione...")
    return {"interpretazione": get_interpretation(sogno, risposte)}