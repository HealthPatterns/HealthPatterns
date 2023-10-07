"""
crud functions from crud_users.py don't do anything, as there is no db model yet.
They are just placeholders.
"""
from fastapi import APIRouter, HTTPException, status, Response

from ...db.database import SessionInstance
from ...schemas.users import UserComplete, UserCreate, UserBase
from ...common import crud_users

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("", response_model=UserComplete, status_code=status.HTTP_201_CREATED)
def create_user(db: SessionInstance, user: UserCreate):
    crud_users.create_user(db, user)
    return

@router.get("/{user_id}", response_model=UserComplete)
def get_user(db: SessionInstance, user_id: int):
    mock_user = UserComplete(
        nickname=f"maxi{user_id}",
        full_name="Maxi Mustermensch",
        age=42,
        id=user_id,
        is_active=True
    )
    if not mock_user:
        raise HTTPException(status_code=404, detail="Resource not found")
    
    crud_users.read_user(db, user_id)
    return mock_user

@router.get("/{user_id}/name", response_model=UserBase)
def get_user_nickname(db: SessionInstance, user_id: int):
    mock_user = UserBase(nickname=f"maxi{user_id}")
    if not mock_user:
        raise HTTPException(status_code=404, detail="Resource not found")
    return mock_user

@router.put("/{user_id}", response_model=UserComplete)
def update_user_data(db: SessionInstance, user_id: int, user: UserComplete):
    if user_id is not user.id:
        raise HTTPException(
            status_code=400,
            detail="Bad Request: User ID's do not match in Path and Payload."
        )
    user_exists = True
    if not user_exists:
        raise HTTPException(status_code=404, detail="Resource not found")
    
    crud_users.update_user(db, user)
    return user

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(db: SessionInstance, user_id: int):
    user_exists = True
    if not user_exists:
        raise HTTPException(status_code=404, detail="Resource not found")
    
    crud_users.delete_trackings_from_user(db, user_id)
    crud_users.delete_user(db, user_id)
    return
