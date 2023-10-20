from uuid import UUID

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from ..models.users import Users
from ..schemas.users import UserForUpdate, UserCreate

def user_exists_by_id(db: Session, user_id: UUID) -> bool:
    result = db.query(Users).filter_by(id=user_id).first() is not None

    return True if result else False

def user_exists_by_nickname(db: Session, nickname: str) -> bool:
    result = db.query(Users).filter_by(nickname=nickname).first() is not None

    return True if result else False

def user_exists_by_email(db: Session, email: str) -> bool:
    result = db.query(Users).filter_by(email=email).first() is not None

    return True if result else False

def create_user(db: Session, user: UserCreate) -> Users:
    new_user = Users(**jsonable_encoder(user))
    db.add(new_user)
    db.commit()

    return new_user

def read_all_users(db: Session):
    return db.query(Users).all()

def read_user_by_id(db: Session, user_id: UUID) -> Users:
    return db.query(Users).filter(Users.id == user_id).first()

def read_user_by_nickname(db: Session, nickname: str) -> Users:
    return db.query(Users).filter(Users.nickname == nickname).first()

def update_user(db: Session, update_data: UserForUpdate, user_id: UUID) -> Users:
    print(update_data)
    for key, value in update_data:
        db.query(Users).filter(Users.id == user_id).update({key: value})
        db.commit()

    return read_user_by_id(db=db, user_id=user_id)

def delete_user_by_id(db: Session, user_id: UUID) -> None:
    user = read_user_by_id(db=db, user_id=user_id)
    db.delete(user)
    db.commit()

def delete_user_by_email(db: Session, email: str) -> None:
    user = read_user_by_id(db=db, email=email)
    db.delete(user)
    db.commit()