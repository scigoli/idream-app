# api.py
# API routes and logic

# Definisce gli endpoint REST e usa le funzioni di autenticazione e ChatGPT:


from fastapi import APIRouter, Depends, HTTPException, Request
import logging
from pydantic import BaseModel
class InterpretationRequest(BaseModel):
    sogno: str
    risposte: list
from app.auth import verify_token
from app.chatgpt import get_questions, get_interpretation


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
    handlers=[
        logging.FileHandler("backend.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("api")
router = APIRouter()
logger.info("API router initialized.")




# Modello per il body JSON

class SognoRequest(BaseModel):
    sogno: str

@router.post("/questions")
async def questions(payload: SognoRequest, request: Request, user=Depends(verify_token)):
    """
    Restituisce le domande da porre all'utente in base al sogno.
    Accetta solo body JSON con campo 'sogno'.
    """
    try:
        logger.debug(f"Content-Type: {request.headers.get('content-type')}")
        logger.debug(f"Payload ricevuto: {payload}")
        sogno = payload.sogno
        logger.info(f"domande... user: {user}")
        return {"domande": get_questions(sogno)}
    except Exception as e:
        logger.error(f"ERRORE questions: {e}")
        raise HTTPException(status_code=500, detail=str(e))



@router.post("/interpretation")
async def interpretation(request: InterpretationRequest, req: Request, user=Depends(verify_token)):
    try:
        logger.info(f"interpretazione... user: {user}")
        logger.debug(f"DEBUG request type: {type(request)}")
        logger.debug(f"DEBUG request value: {request}")
        # Validazione input: risposte deve essere lista di coppie
        if not isinstance(request.risposte, list) or not all(isinstance(r, list) and len(r) == 2 for r in request.risposte):
            logger.error(f"Input risposte non valido: {request.risposte}")
            raise HTTPException(status_code=400, detail="Il campo 'risposte' deve essere una lista di coppie [domanda, risposta]")
        result = get_interpretation(request.sogno, request.risposte)
        return {"interpretazione": result}
    except Exception as e:
        logger.error(f"ERRORE interpretazione: {e}")
        raise HTTPException(status_code=500, detail=str(e))