from fastapi import APIRouter, HTTPException, status

from aid_vault import crud, schemas, models
from ...db.database import SessionInstance
from ...common.security import get_password_hash
from ...common.oauth2 import CurrentUserToken

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)

@router.post(
        "/register",
        response_model=schemas.UserComplete,
        status_code=status.HTTP_201_CREATED
)
def register_user(db: SessionInstance, user_in: schemas.UserCreate) -> models.Users:
    """
    Creates a user from the input data, hashes the plaintext password and saves
    the user into the database. Returns the new user from the database.
    The user still has to login afterwards.
    """
    if crud.users.user_exists_by_nickname(db, user_in.nickname):
        raise HTTPException(
            status_code=400,
            detail="User with this username already exists."
        )

    hashed_password = get_password_hash(user_in.password)
    user_in.password = hashed_password
    new_user = crud.users.create_user(db=db, user=user_in)
    return new_user

@router.get("", response_model=schemas.UserComplete)
def get_user(current_user: CurrentUserToken) -> models.Users:
    """
    Returns currently logged in user.
    """   
    return current_user

@router.get("/name", response_model=schemas.UserBase | schemas.UserFullName)
def get_user_name(current_user: CurrentUserToken) -> models.Users:
    """
    Returns currently logged in user's full name, or nickname if the full name is null.
    """
    if current_user.full_name is not None:
        name = schemas.UserFullName(full_name=current_user.full_name)
        return name

    return current_user

@router.put("", response_model=schemas.UserComplete)
def update_user_data(
    db: SessionInstance,
    current_user: CurrentUserToken,
    input_data: schemas.UserForUpdate
) -> models.Users:
    """
    Updates currently logged in user. Fields that get put in as null or omitted will be set to null.
    """
    updated_user = crud.users.update_user(
        db,
        update_data=input_data,
        user_id=current_user.id
    )
    return updated_user

@router.delete("", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(db: SessionInstance, current_user: CurrentUserToken):
    """
    Deletes currently logged in user.
    """
    crud.users.delete_user_by_id(db=db, user_id=current_user.id)
    return
