from passlib.context import CryptContext
from sqlalchemy.orm import Session

from ..models import Users
from ..crud import read_user_by_nickname

hash_context = CryptContext(schemes=["bcrypt"], deprecated= "auto")

def verify_password(plain_password, hashed_password):
    return hash_context.verify(plain_password, hashed_password)

def get_password_hash(plain_password):
    return hash_context.hash(plain_password)

def get_puk_hash(plain_puk):
    return hash_context.hash(plain_puk)

def verify_puk(plain_puk, hashed_puk):
    return hash_context.verify(plain_puk, hashed_puk)

def authenticate_user(db: Session, username: str, password: str):
    user = read_user_by_nickname(db, username)
    if not user:
        return False
    if not verify_password(plain_password=password, hashed_password=user.password):
        return False
    return user

def authenticate_puk(db: Session, username: str, puk: str):
    user = read_user_by_nickname(db, username)
    if not user:
        return False
    if not verify_puk(plain_puk=puk, hashed_puk=user.puk):
        return False
    return user

def change_password(db: Session, user: Users, password: str):
    hashed_password = get_password_hash(password)
    user.password = hashed_password
    db.commit()
    return user
