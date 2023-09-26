from fastapi import APIRouter, HTTPException

from ...schemas.user import UserSchema, UserCreate
from ...common import crud_user
from ...db.database import SessionInstance

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.post("/", response_model=UserSchema)
def create_user(db: SessionInstance, user: UserCreate):
    user_in_db = crud_user.read_user_by_email(db, email=user.email)
    if user_in_db:
        raise HTTPException(status_code=400, detail="Email already registered.")
    return crud_user.create_user(db=db, user=user)

@router.get("/", response_model=list[UserSchema])
def get_users(db: SessionInstance, skip: int = 0, limit: int = 100):
    users = crud_user.read_users(db, skip, limit)
    return users

@router.get("/{user_id}", response_model=UserSchema)
def get_user(db: SessionInstance, user_id: int):
    user_in_db = crud_user.read_user(db, user_id)
    if not user_in_db:
        raise HTTPException(status_code=404, detail="Not found.")
    return user_in_db

@router.put("/{user_id}", response_model=UserSchema)
def put_user(db: SessionInstance, user_id: int, user: UserSchema):
    if user_id is not user.id:
        raise HTTPException(status_code=400, detail="Bad Request: User ID's do not match in Path and Payload.")
    return crud_user.update_user(db, user)

@router.delete("/{user_id}")
def delete_user(db: SessionInstance, user_id: int):
    user_in_db = crud_user.read_user(db, user_id)
    if not user_in_db:
        raise HTTPException(status_code=404, detail="Not found.")
    crud_user.delete_user(db, user_id)
    return {"message": f"User {user_id} deleted."}