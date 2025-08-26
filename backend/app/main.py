# main.py
# Entry point for backend application

# Contiene l’entrypoint FastAPI e importa le route:

import uvicorn
from fastapi import FastAPI
from app.api import router
from fastapi import Request, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
import os
from dotenv import load_dotenv
import requests
import httpx
import logging
load_dotenv()
FIREBASE_API_KEY = os.getenv("FIREBASE_API_KEY")
FIREBASE_AUTH_DOMAIN = os.getenv("FIREBASE_AUTH_DOMAIN")
FIREBASE_PROJECT_ID = os.getenv("FIREBASE_PROJECT_ID")
BACKEND_API_URL = os.getenv("BACKEND_API_URL", "http://127.0.0.1:8000")
logging.basicConfig(level=logging.INFO)
from fastapi.responses import HTMLResponse

app = FastAPI()
app.include_router(router)
print("Let's go...")

if __name__ == "__main__":
    print("Backend app started.")

@app.get("/")
def serve_index():
    # Sostituisci i placeholder Firebase nell'HTML con i valori da .env
    with open("app/static/index.html", encoding="utf-8") as f:
        html = f.read()
    html = html.replace("INSERISCI_API_KEY_FIREBASE", FIREBASE_API_KEY or "")
    html = html.replace("INSERISCI_AUTH_DOMAIN", FIREBASE_AUTH_DOMAIN or "")
    html = html.replace("INSERISCI_PROJECT_ID", FIREBASE_PROJECT_ID or "")
    return HTMLResponse(content=html)

@app.post("/proxy/questions")
async def proxy_questions(request: Request):
    body = await request.json()
    token = request.headers.get("Authorization")
    logging.info(f"[PROXY] /questions: body={body}")
    logging.info(f"[PROXY] /questions: token={token}")
    url = f"{BACKEND_API_URL}/questions"
    logging.info(f"[PROXY] /questions: url={url}")
    if not token:
        logging.error("[PROXY] /questions: Token mancante")
        raise HTTPException(status_code=401, detail="Token mancante")
    try:
        logging.info(f"[PROXY] /questions: INIZIO chiamata backend (timeout=60s, async)")
        async with httpx.AsyncClient(timeout=60) as client:
            res = await client.post(url, headers={"Authorization": token, "Content-Type": "application/json"}, json=body)
        logging.info(f"[PROXY] /questions: FINE chiamata backend")
        logging.info(f"[PROXY] /questions: response status={res.status_code}")
        logging.info(f"[PROXY] /questions: response text={res.text}")
        res.raise_for_status()
        try:
            return JSONResponse(content=res.json())
        except Exception as json_err:
            logging.error(f"[PROXY] /questions: Errore parsing JSON: {json_err}")
            return JSONResponse(content={"error": "Risposta backend non valida", "raw": res.text}, status_code=502)
    except Exception as e:
        logging.error(f"[PROXY] /questions error: {e}")
        return JSONResponse(content={"error": f"Errore proxy /questions: {e}"}, status_code=502)

@app.post("/proxy/interpretation")
async def proxy_interpretation(request: Request):
    body = await request.json()
    token = request.headers.get("Authorization")
    if not token:
        raise HTTPException(status_code=401, detail="Token mancante")
    try:
        logging.info(f"[PROXY] /interpretation: INIZIO chiamata backend (timeout=60s, async)")
        async with httpx.AsyncClient(timeout=60) as client:
            res = await client.post(f"{BACKEND_API_URL}/interpretation", headers={"Authorization": token, "Content-Type": "application/json"}, json=body)
        logging.info(f"[PROXY] /interpretation: FINE chiamata backend")
        logging.info(f"[PROXY] /interpretation: response status={res.status_code}")
        logging.info(f"[PROXY] /interpretation: response text={res.text}")
        res.raise_for_status()
        try:
            return JSONResponse(content=res.json())
        except Exception as json_err:
            logging.error(f"[PROXY] /interpretation: Errore parsing JSON: {json_err}")
            return JSONResponse(content={"error": "Risposta backend non valida", "raw": res.text}, status_code=502)
    except Exception as e:
        logging.error(f"Proxy /interpretation error: {e}")
        raise HTTPException(status_code=502, detail=f"Errore proxy /interpretation: {e}")
