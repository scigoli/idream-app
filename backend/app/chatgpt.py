# chatgpt.py
# ChatGPT integration logic

import openai
import os

from dotenv import load_dotenv
load_dotenv()
print("API KEY:", os.getenv("OPENAI_API_KEY"))

# Usa la nuova API openai >= 1.0.0
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_questions(sogno):
    prompt = (
        f"L'utente ha descritto questo sogno: \"{sogno}\".\n"
        "Quali domande potrei fare all'utente per raccogliere informazioni utili all'interpretazione di questo sogno? "
        "Rispondi solo con una lista di domande, senza spiegazioni."
    )
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    # Estrai il testo e suddividi in domande
    return response.choices[0].message.content.split("\n")[:5]

def get_interpretation(sogno, risposte):
    prompt = (
        f"L'utente ha descritto questo sogno: \"{sogno}\".\n"
        "Ha risposto alle seguenti domande:\n"
    )
    for domanda, risposta in risposte:
        prompt += f"- {domanda}\n  Risposta: {risposta}\n"
    prompt += (
        "Fornisci una interpretazione dettagliata del sogno basandoti sulla descrizione e sulle risposte."
    )
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# Rimuovi il test automatico: lascia solo le funzioni
# Se vuoi testare, usa un file

if __name__ == "__main__":
    print("ChatGPT standalone test started.")