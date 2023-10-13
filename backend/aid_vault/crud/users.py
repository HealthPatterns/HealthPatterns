from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from ..schemas.users import UserCreate, UserComplete

def create_user(db: Session, user: UserCreate):
    return

def read_user(db: Session, user_id: int):
    return

def update_user(db: Session, user: UserComplete):
    return

def delete_user(db: Session, user_id: int):
    return

def delete_trackings_from_user(db: Session, user_id: int):
    return