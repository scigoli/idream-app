# Guida alla sezione Backend dell'applicazione idream-app

## Struttura del backend

La cartella `backend` contiene il server API che gestisce la logica dell'applicazione. È scritto in Python e utilizza il framework FastAPI per creare API REST moderne e veloci. L'autenticazione degli utenti avviene tramite Firebase.

### Principali file e cartelle
- `app/` — contiene il codice sorgente principale del backend
    - `main.py` — punto di ingresso dell'applicazione FastAPI
    - `api.py` — definisce gli endpoint REST (le "porte" tramite cui il frontend comunica col backend)
    - `auth.py` — gestisce l'autenticazione degli utenti tramite Firebase
    - `chatgpt.py` — integra OpenAI per l'interpretazione dei sogni
    - `firebase-credentials.json` — credenziali di servizio per Firebase
    - `idream-postman-collection.json` — raccolta di richieste di test per Postman
- `requirements.txt` — elenco delle dipendenze Python necessarie
- `backend.log` — file di log dove vengono scritte tutte le operazioni e gli errori
- `runserver.bat` — script batch per avviare il server

## Funzionamento del backend

1. **Avvio del server**
   - Si avvia tramite il comando `runserver.bat`.
   - Il server FastAPI parte e si mette in ascolto sulla porta 8000.

2. **Autenticazione**
   - Ogni richiesta deve includere un token Firebase nell'header `Authorization`.
   - Il backend verifica il token tramite le funzioni di `auth.py`.
   - Se il token è valido, l'utente può accedere agli endpoint protetti.

3. **Endpoint principali**
   - `/questions`: riceve una descrizione del sogno e restituisce una lista di domande utili per l'interpretazione. Utilizza OpenAI per generare le domande.
   - `/interpretation`: riceve le risposte alle domande e restituisce l'interpretazione del sogno, sempre tramite OpenAI.

4. **Gestione degli errori e dei log**
   - Tutte le operazioni e gli errori vengono scritti sia in console che nel file `backend.log`.
   - Se l'input non è corretto, il backend restituisce un errore chiaro e dettagliato.

## Come funziona il flusso di una richiesta

1. Il frontend invia una richiesta HTTP (POST) all'endpoint `/questions` o `/interpretation`, includendo il token Firebase.
2. Il backend verifica il token.
3. Se valido, processa la richiesta e restituisce la risposta.
4. Tutto viene tracciato nei log per facilitare il debug.

## Suggerimenti per migliorare il backend

- **Separazione dei moduli**: suddividere meglio le responsabilità tra i file, ad esempio creando una cartella `services/` per la logica di business.
- **Validazione input più robusta**: usare Pydantic per validare e documentare meglio i dati in ingresso.
- **Gestione degli errori più dettagliata**: restituire codici di errore e messaggi più specifici per ogni tipo di errore.
- **Documentazione automatica**: sfruttare le funzionalità di FastAPI per generare una documentazione interattiva degli endpoint (Swagger UI).
- **Test automatici**: aggiungere test unitari e di integrazione per garantire la stabilità del backend.
- **Configurazione tramite file .env**: gestire le variabili sensibili (API key, credenziali) tramite file di configurazione e non nel codice.
- **Logging strutturato**: migliorare il formato dei log per facilitare la ricerca e l'analisi.
- **Gestione delle dipendenze**: usare un ambiente virtuale Python (venv) per isolare le dipendenze.

---

Questo documento ti aiuta a comprendere la struttura e il funzionamento del backend, anche se non hai esperienza con Python, FastAPI o Firebase. Per ogni dubbio, consulta la documentazione ufficiale di FastAPI e Firebase oppure chiedi supporto al team di sviluppo.
