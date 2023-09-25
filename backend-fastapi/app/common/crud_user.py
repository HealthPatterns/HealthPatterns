from sqlalchemy.orm import Session

from ..models.user import User
from ..schemas.user import UserCreate, UserSchema

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

def create_user(db: Session, user: UserCreate) -> User:
    db_user = User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# def update_user(db: Session, user: UserSchema) -> User:
#     updated_user = User(**user.model_dump())
#     db.merge(updated_user)
#     db.commit()
#     db.refresh(updated_user)
#     return updated_user

