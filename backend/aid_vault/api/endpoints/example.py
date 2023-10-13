from fastapi import APIRouter, HTTPException, status, Response

from ...schemas.example import UserSchema, UserCreate
from ...crud import example
from ...db.database import SessionInstance

# declare router with default values
router = APIRouter(
    prefix="/example",
    tags=["Example"] # -> makes endpoints show up in its own category in the documentation
)

@router.post("", response_model=UserSchema, status_code=status.HTTP_201_CREATED)
def create_user(db: SessionInstance, user: UserCreate):
    if example.read_user_by_email(db, email=user.email):
        raise HTTPException(status_code=400, detail="Email already registered.")
    return example.create_user(db=db, user=user)

@router.get("", response_model=list[UserSchema])
def get_users(db: SessionInstance, skip: int = 0, limit: int = 100):
    users = example.read_users(db, skip, limit)
    return users

@router.get("/{user_id}", response_model=UserSchema)
def get_user(db: SessionInstance, user_id: int):
    user_in_db = example.read_user(db, user_id)
    if not user_in_db:
        raise HTTPException(status_code=404, detail="Not found.")
    return user_in_db

@router.put("/{user_id}", response_model=UserSchema)
def put_user(db: SessionInstance, user_id: int, user: UserSchema, response: Response):
    if user_id is not user.id:
        raise HTTPException(status_code=400, detail="Bad Request: User ID's do not match in Path and Payload.")
    
    user_in_db = example.read_user(db, user_id)
    # if user already exists:
    if user_in_db:
        if user_in_db.email != user.email and example.read_user_by_email(db, email=user.email):
            raise HTTPException(status_code=400, detail="Email already registered.")
        return example.update_user(db, user)
    # if user doesn't exist:
    if example.read_user_by_email(db, email=user.email):
        raise HTTPException(status_code=400, detail="Email already registered.")
    response.status_code = status.HTTP_201_CREATED
    return example.create_user(db, user)

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(db: SessionInstance, user_id: int):
    user_in_db = example.read_user(db, user_id)
    if not user_in_db:
        raise HTTPException(status_code=404, detail="Not found.")
    example.delete_user(db, user_id)