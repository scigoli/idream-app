# auth.py
# Authentication logic

# Gestisce la verifica del token Firebase:

import firebase_admin
from firebase_admin import auth, credentials
from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
import logging

# Initialize Firebase Admin SDK using service account JSON.
# Make sure the file exists at ./app/firebase-credentials.json and is the
# correct service account for your Firebase project.
print("Initializing Firebase Admin...")
cred = credentials.Certificate("./app/firebase-credentials.json")
firebase_admin.initialize_app(cred)
print("Firebase Admin initialized")

# Use HTTPBearer via Security so FastAPI/OpenAPI knows about the Bearer auth
bearer_scheme = HTTPBearer()

def verify_token(credentials: HTTPAuthorizationCredentials = Security(bearer_scheme)):
   """Verify Firebase ID token passed as Bearer token.

   Returns the decoded token on success or raises HTTPException(401) on failure.
   """
   token = credentials.credentials
   masked = token[:40] + '...' if token and len(token) > 40 else token
   logger = logging.getLogger("auth")
   try:
      logger.info(f"Verifica token: {masked}")
      decoded_token = auth.verify_id_token(token)
      logger.info(f"Token decodificato: {decoded_token}")
      return decoded_token
   except Exception as e:
      logger.error(f"Token non valido: {e}")
      raise HTTPException(status_code=401, detail="Invalid or missing token")