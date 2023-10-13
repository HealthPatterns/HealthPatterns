from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, HTTPException, status, Response

from ..models.users import Users
from ..db.database import SessionInstance
from ..schemas.users_new import UserComplete, UserForUpdate

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

def read_all_users(db: SessionInstance):
    return db.query(Users).all()

def read_user_id(db: SessionInstance, user_id: int):
    return db.query(Users).filter(Users.id == user_id).first()

def read_user_email(db: SessionInstance, email: str):
    return db.query(Users).filter(Users.email == email).first()

def update_user(db: SessionInstance, update_data: UserForUpdate, user_id: int):
    ### Update any element in a row by entering the column/-s in json format (UserForUpdate)###
    for key, value in update_data:
        if value != None:
            db.query(Users).filter(Users.id == user_id).update({key: value})
            db.commit()

    return read_user_id(db=db, user_id=user_id)

def delete_user(db: SessionInstance, user_id: int):
    user = read_user_id(db=db, user_id=user_id);
    db.delete(user)
    db.commit()

def delete_trackings_from_user(db: SessionInstance, user_id: int):
    return