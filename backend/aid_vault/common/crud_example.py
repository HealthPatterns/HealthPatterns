from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from ..models.example import User
from ..schemas.example import UserCreate, UserSchema

def read_user(db: Session, user_id: int) -> User:
    return db.query(User).filter(User.id == user_id).first()

def read_user_by_email(db: Session, email: str) -> User:
    return db.query(User).filter(User.email == email).first()

def read_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

def create_user(db: Session, user: UserCreate | UserSchema) -> User:
    user_in_db = User(**jsonable_encoder(user))
    db.add(user_in_db)
    db.commit() 
    db.refresh(user_in_db)
    return user_in_db

def update_user(db: Session, user: UserSchema) -> User:
    updated_user = User(**jsonable_encoder(user))
    db.merge(updated_user)
    db.commit()
    return updated_user

def delete_user(db: Session, user_id: int) -> None:
    user_in_db = read_user(db, user_id)
    db.delete(user_in_db)
    db.commit()