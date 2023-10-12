"""
crud functions from crud_users.py don't do anything, as there is no db model yet.
They are just placeholders.
"""
from fastapi import APIRouter, HTTPException, status, Response

from aid_vault import crud, schemas, models
from ...db.database import SessionInstance
from ...db import fake_db
from ...common.security import get_password_hash

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("", response_model=schemas.UserComplete, status_code=status.HTTP_201_CREATED)
def create_user(input: schemas.UserCreate):
    """
    Creates a user from the input data, hashes the plaintext password and saves
    the user into the database.
    The user still has to login afterwards.
    """
    fake_db.user_id_increment += 1
    user = schemas.UserFakeDB(
        nickname=input.nickname,
        full_name=input.full_name,
        age=input.age,
        id=fake_db.user_id_increment,
        is_active=True,
        hashed_password=get_password_hash(input.plain_password)
    )
    fake_db.fake_users_db.append(user)
    return user

@router.get("/{user_id}", response_model=schemas.UserComplete)
def get_user(db: SessionInstance, user_id: int):
    mock_user = schemas.UserComplete(
        nickname=f"maxi{user_id}",
        full_name="Maxi Mustermensch",
        age=42,
        id=user_id,
        is_active=True
    )
    if not mock_user:
        raise HTTPException(status_code=404, detail="Resource not found")
    
    crud.users.read_user(db, user_id)
    return mock_user

@router.get("/{user_id}/name", response_model=schemas.UserBase)
def get_user_nickname(db: SessionInstance, user_id: int):
    mock_user = schemas.UserBase(nickname=f"maxi{user_id}")
    if not mock_user:
        raise HTTPException(status_code=404, detail="Resource not found")
    return mock_user

@router.put("/{user_id}", response_model=schemas.UserComplete)
def update_user_data(db: SessionInstance, user_id: int, user: schemas.UserComplete):
    if user_id is not user.id:
        raise HTTPException(
            status_code=400,
            detail="Bad Request: User ID's do not match in Path and Payload."
        )
    user_exists = True
    if not user_exists:
        raise HTTPException(status_code=404, detail="Resource not found")
    
    crud.users.update_user(db, user)
    return user

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(db: SessionInstance, user_id: int):
    user_exists = True
    if not user_exists:
        raise HTTPException(status_code=404, detail="Resource not found")
    
    crud.users.delete_trackings_from_user(db, user_id)
    crud.users.delete_user(db, user_id)
    return
