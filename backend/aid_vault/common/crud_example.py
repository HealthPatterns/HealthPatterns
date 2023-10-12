from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from ..models.example import Users
from ..schemas.example import UserCreate, UserSchema

def read_user(db: Session, user_id: int) -> Users:
    return db.query(Users).filter(Users.id == user_id).first()

def read_user_by_email(db: Session, email: str) -> Users:
    return db.query(Users).filter(Users.email == email).first()

def read_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Users).offset(skip).limit(limit).all()

def create_user(db: Session, user: UserCreate | UserSchema) -> Users:
    user_in_db = Users(**jsonable_encoder(user))
    db.add(user_in_db)
    db.commit()
    db.refresh(user_in_db)
    return user_in_db

def update_user(db: Session, user: UserSchema) -> Users:
    updated_user = Users(**jsonable_encoder(user))
    db.merge(updated_user)
    db.commit()
    return updated_user

def delete_user(db: Session, user_id: int) -> None:
    user_in_db = read_user(db, user_id)
    db.delete(user_in_db)
    db.commit()