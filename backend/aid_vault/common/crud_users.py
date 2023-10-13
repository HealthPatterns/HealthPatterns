from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, HTTPException, status, Response

from ..models.users import Users
from ..db.database import SessionInstance
from ..schemas.users_new import UserComplete

def user_exists_by_email(db: SessionInstance, email: str) -> bool:
    result = db.query(Users).filter_by(email=email).first() is not None

    if result:
        return True
    return False

def user_exists_by_id(db: SessionInstance, user_id: int) -> bool:
    result = db.query(Users).filter_by(id=user_id).first() is not None

    if result:
        return True
    return False

def create_user(db: SessionInstance, user: UserComplete) -> Users:
    new_user = Users(**jsonable_encoder(user))
    db.add(new_user)
    db.commit()

    return new_user

def read_user(db: SessionInstance, user_id: int):
    result = db.query(Users).get(user_id)

    return jsonable_encoder(result)

def update_user(db: SessionInstance, user: UserComplete):
    return

def delete_user(db: SessionInstance, user_id: int):
    return

def delete_trackings_from_user(db: SessionInstance, user_id: int):
    return