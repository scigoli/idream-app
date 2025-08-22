# main.py
# Entry point for backend application

# Contiene l’entrypoint FastAPI e importa le route:

from fastapi import FastAPI
from app.api import router

app = FastAPI()
app.include_router(router)
print("Let's go...")

if __name__ == "__main__":
    print("Backend app started.")
