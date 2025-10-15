from werkzeug.security import generate_password_hash, check_password_hash
from app.crud.base_crud import read_json, write_json
from app.services.tokens_service import (
    create_access_token,
    create_refresh_token,
    decode_token,
)
import os

USERS_FILE = os.getenv("USERS_FILE", "users.json")
REFRESH_FILE = os.getenv("REFRESH_FILE", "refresh_tokens.json")
ACCESS_MIN = int(os.getenv("ACCESS_TOKEN_EXPIRES_MIN", "60"))

def get_user(email):
    users = read_json(USERS_FILE)
    for u in users:
        if u["email"].lower() == email.lower():
            return u
    return None

def register_user(email, password, roles):
    if get_user(email):
        return {"error": "email_already_registered"}, 400
    user = {
        "email": email.lower(),
        "password_hash": generate_password_hash(password),
        "roles": roles,
    }
    users = read_json(USERS_FILE)
    users.append(user)
    write_json(USERS_FILE, users)
    return {"message": "user_registered", "email": user["email"], "roles": roles}, 201

def login_user(email, password):
    user = get_user(email)
    if not user or not check_password_hash(user["password_hash"], password):
        return {"error": "invalid_credentials"}, 401
    access = create_access_token(user["email"], user["roles"])
    refresh = create_refresh_token(user["email"])
    return {
        "access_token": access,
        "refresh_token": refresh,
        "expires_in_minutes": ACCESS_MIN,
    }, 200