## Applicazione Flutter

La versione mobile Flutter è attualmente in lavorazione. Segui gli aggiornamenti nella cartella `mobile/`.

# idream-app

This project contains both a FastAPI backend and a Flutter mobile application.

## Structure
- `backend/`: FastAPI backend with OpenAI integration
- `mobile/`: Flutter mobile app

## Avvio dell'applicazione HTML

1. Avvia il backend FastAPI:
	- Da terminale:
	  ```powershell
	  cd backend
	  uvicorn app.main:app --reload
	  ```
	- Oppure usa il file `runserver.bat`.

2. Apri il browser e vai su:
	- [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
	- Si aprirà l'interfaccia HTML per login, inserimento sogno e interpretazione.

## Documentazione Backend

Consulta la documentazione tecnica e le guide nella cartella `backend`:

- [BACKEND_GUIDA.md](backend/BACKEND_GUIDA.md)
- [PIPELINE_PROXY.md](backend/PIPELINE_PROXY.md)
