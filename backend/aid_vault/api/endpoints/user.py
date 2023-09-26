from fastapi import APIRouter, HTTPException, status, Response

from ...schemas.user import UserSchema, UserCreate
from ...common import crud_user
from ...db.database import SessionInstance

# declare router with default values
router = APIRouter(
    prefix="/users",
    tags=["users"] # -> makes endpoints show up in its own category in the documentation
)

@router.post("/", response_model=UserSchema, status_code=status.HTTP_201_CREATED)
def create_user(db: SessionInstance, user: UserCreate):
    if crud_user.read_user_by_email(db, email=user.email):
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
def put_user(db: SessionInstance, user_id: int, user: UserSchema, response: Response):
    if user_id is not user.id:
        raise HTTPException(status_code=400, detail="Bad Request: User ID's do not match in Path and Payload.")
    
    user_in_db = crud_user.read_user(db, user_id)
    # if user already exists:
    if user_in_db:
        if user_in_db.email != user.email and crud_user.read_user_by_email(db, email=user.email):
            raise HTTPException(status_code=400, detail="Email already registered.")
        return crud_user.update_user(db, user)
    # if user doesn't exist:
    if crud_user.read_user_by_email(db, email=user.email):
        raise HTTPException(status_code=400, detail="Email already registered.")
    response.status_code = status.HTTP_201_CREATED
    return crud_user.create_user(db, user)

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(db: SessionInstance, user_id: int):
    user_in_db = crud_user.read_user(db, user_id)
    if not user_in_db:
        raise HTTPException(status_code=404, detail="Not found.")
    crud_user.delete_user(db, user_id)