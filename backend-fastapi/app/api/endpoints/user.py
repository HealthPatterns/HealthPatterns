from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ...models import user
from ...schemas.user import UserSchema, UserCreate
from ...common import crud_user
from ...db.database import get_db

router = APIRouter(
    prefix="/users"
)

@router.post("/", response_model=UserSchema)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = crud_user.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    new_user = crud_user.create_user(db=db, user=user)
    return new_user

@router.get("/", response_model=list[UserSchema])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud_user.get_users(db, skip, limit)
    return users

