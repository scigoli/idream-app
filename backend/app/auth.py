# auth.py
# Authentication logic

# Gestisce la verifica del token Firebase:

import firebase_admin
from firebase_admin import auth, credentials
from fastapi import HTTPException, Header

print("Verifying credwentials...")
cred = credentials.Certificate("./app/firebase-credentials.json")
firebase_admin.initialize_app(cred)
print("Credentials OK")

def verify_token(authorization: str = Header(...)):
   try:
      token = authorization.split(" ")[1]
      decoded_token = auth.verify_id_token(token)
      return decoded_token
   except Exception as e:
      print(f"Token verification failed: {e}")
      raise HTTPException(status_code=401, detail="Invalid or missing token")