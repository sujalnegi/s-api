import os
import json
import firebase_admin
from firebase_admin import credentials, auth
from functools import wraps
from flask import request, jsonify, g

_sa = os.getenv("FIREBASE_SERVICE_ACCOUNT")
if not _sa:
    raise RuntimeError("FIREBASE_SERVICE_ACCOUNT not set")

try:
    if os.path.exists(_sa):
        cred = credentials.Certificate(_sa)
    else:
        cred = credentials.Certificate(json.loads(_sa))
except Exception as e:
    raise RuntimeError(f"invalid service account: {e}")

try:
    firebase_admin.get_app()
except ValueError:
    firebase_admin.initialize_app(cred)

def verify_firebase_token(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        header = request.headers.get("Authorization", "")
        if not header.startswith("Bearer "):
            return jsonify({"error": "missing token"}), 401
        id_token = header.split(" ", 1)[1].strip()
        try:
            decoded = auth.verify_id_token(id_token)
        except Exception:
            return jsonify({"error": "invalid token"}), 401
        g.uid = decoded.get("uid")
        g.firebase_user = decoded
        return f(*args, **kwargs)
    return wrapper



