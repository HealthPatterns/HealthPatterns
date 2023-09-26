from sqlalchemy.orm import Session

from ..models.user import User
from ..schemas.user import UserCreate, UserSchema

def read_user(db: Session, user_id: int) -> User:
    return db.query(User).filter(User.id == user_id).first()

def read_user_by_email(db: Session, email: str) -> User:
    return db.query(User).filter(User.email == email).first()

def read_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

def create_user(db: Session, user: UserCreate) -> User:
    user_in_db = User(**user.model_dump())
    db.add(user_in_db)
    db.commit()
    db.refresh(user_in_db)
    return user_in_db

def update_user(db: Session, user: UserSchema) -> User:
    user_in_db = read_user(db, user.id)
    if user_in_db:
        user_in_db.email = user.email
        user_in_db.name = user.name
        user_in_db.is_active = user.is_active
    else:
        user_in_db = User(**user.model_dump())
    db.add(user_in_db)
    db.commit()
    db.refresh(user_in_db)
    return user_in_db

def delete_user(db: Session, user_id: int) -> None:
    user_in_db = read_user(db, user_id)
    db.delete(user_in_db)
    db.commit()