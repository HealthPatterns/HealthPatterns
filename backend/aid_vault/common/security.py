from typing import Annotated
from datetime import datetime, timedelta

from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

from .oauth2 import get_user_by_name

hash_context = CryptContext(schemes=["bcrypt"], deprecated= "auto")

def verify_password(plain_password, hashed_password):
    return hash_context.verify(plain_password, hashed_password)

def get_password_hash(plain_password):
    return hash_context.hash(plain_password)

def authenticate_user(db, username: str, password: str):
    user = get_user_by_name(db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user