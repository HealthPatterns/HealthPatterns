from uuid import uuid4, UUID

from fastapi import APIRouter, HTTPException, status, Response
from fastapi.encoders import jsonable_encoder
from pydantic import UUID4

from aid_vault import crud, schemas, models
from ...db.database import SessionInstance
from ...db import fake_db
from ...common.security import get_password_hash
from ...common.oauth2 import CurrentUserToken

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)

@router.post("/register", response_model=schemas.UserComplete, status_code=status.HTTP_201_CREATED)
def register_user(input: schemas.UserCreate):
    """
    Creates a user from the input data, hashes the plaintext password and saves
    the user into the database.
    The user still has to login afterwards.
    """

    user = schemas.UserFakeDB(
        nickname=input.nickname,
        full_name=input.full_name,
        age=input.age,
        id=uuid4(),
        is_active=True,
        hashed_password=get_password_hash(input.plain_password)
    )
    fake_db.fake_users_db.append(user)
    return user

@router.get("", response_model=schemas.UserComplete)
def get_user(current_user: CurrentUserToken):
    """
    Returns currently logged in user.
    """   
    return current_user

@router.get("/name", response_model=schemas.UserBase)
def get_user_nickname(current_user: CurrentUserToken):
    """
    Returns currently logged in user's nickname.
    """
    return current_user

@router.put("", response_model=schemas.UserComplete)
def update_user_data(current_user: CurrentUserToken, input_data: schemas.UserComplete):
    """
    Update currently logged in user.
    """
    if input_data.id.int != current_user.id.int:
        raise HTTPException(
            status_code=400,
            detail="Bad Request: User ID in body does not match currently logged in user."
        )
    if input_data.nickname is not None:
        current_user.nickname = input_data.nickname
    if input_data.full_name is not None:
        current_user.full_name = input_data.full_name
    if input_data.age is not None:
        current_user.age = input_data.age
    if input_data.is_active is not None:
        current_user.is_active = input_data.is_active    

    return current_user

@router.delete("", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(current_user: CurrentUserToken):
    """
    Deletes currently logged in user.
    """
    fake_db.fake_users_db.remove(current_user)
    return
