from passlib.context import CryptContext
from sqlalchemy.orm import Session

from ..crud import read_user_by_nickname

hash_context = CryptContext(schemes=["bcrypt"], deprecated= "auto")

def verify_password(plain_password, hashed_password):
    return hash_context.verify(plain_password, hashed_password)

def get_password_hash(plain_password):
    return hash_context.hash(plain_password)

def authenticate_user(db: Session, username: str, password: str):
    user = read_user_by_nickname(db, username)
    if not user:
        return False
    if not verify_password(plain_password=password, hashed_password=user.password):
        return False
    return user