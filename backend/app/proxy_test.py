import logging
from logging.handlers import RotatingFileHandler

# Configura logging avanzato
logger = logging.getLogger("proxy")
logger.setLevel(logging.INFO)
handler = RotatingFileHandler("proxy.log", maxBytes=500000, backupCount=3)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# Funzione di log sicura

def log_event(event, level="info"):
    if level == "error":
        logger.error(event)
    else:
        logger.info(event)

# Test automatici per proxy
import requests

def test_proxy_questions(token, sogno):
    try:
        res = requests.post("http://127.0.0.1:8000/proxy/questions", headers={"Authorization": token, "Content-Type": "application/json"}, json={"sogno": sogno})
        log_event(f"Test /proxy/questions status: {res.status_code}")
        return res.json()
    except Exception as e:
        log_event(f"Errore test /proxy/questions: {e}", level="error")
        return None

def test_proxy_interpretation(token, sogno, risposte):
    try:
        res = requests.post("http://127.0.0.1:8000/proxy/interpretation", headers={"Authorization": token, "Content-Type": "application/json"}, json={"sogno": sogno, "risposte": risposte})
        log_event(f"Test /proxy/interpretation status: {res.status_code}")
        return res.json()
    except Exception as e:
        log_event(f"Errore test /proxy/interpretation: {e}", level="error")
        return None

# Esempio di utilizzo (da commentare in produzione)
# token = "Bearer ..."
# print(test_proxy_questions(token, "Ho sognato di volare."))
# print(test_proxy_interpretation(token, "Ho sognato di volare.", [["Domanda 1", "Risposta 1"]]))
