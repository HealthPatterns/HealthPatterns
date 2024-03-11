from typing import Annotated

from fastapi import Depends, APIRouter, HTTPException, status, Form
from fastapi.security import OAuth2PasswordRequestForm


from aid_vault import schemas, crud
from ...common.security import authenticate_user, get_password_hash, get_puk_hash, reset_password
from ...common.oauth2 import (
    create_access_token,
    get_current_active_user,
    CurrentUserToken,
)
from ...db.database import SessionInstance
from ...crud.users import read_user_by_nickname

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post(
    "/register",
    response_model=schemas.UserRegistered,
    status_code=status.HTTP_201_CREATED,
)
def register_user(db: SessionInstance, password_in: schemas.UserCreate) -> schemas.UserRegistered:
    """
    Creates a user from the input data, hashes the plaintext password and saves
    the user into the database. Also generates a new nickname that does not yet exist
    and a new PUK. Returns the new user from the database, its token and its newly
    created puk in plain text so the user can write it down.
    """
    hashed_password = get_password_hash(password_in.password)    
    new_nickname = crud.users.generate_nickname(db)
    new_puk = crud.users.generate_puk()
    hashed_puk = get_puk_hash(new_puk)
    user_schema = schemas.UserCreateDB(nickname=new_nickname, puk=hashed_puk, password=hashed_password)
    new_user_db = crud.users.create_user(db=db, user=user_schema)
    access_token = create_access_token(new_user_db.id)
    token = schemas.Token(access_token=access_token, token_type="bearer")
    new_reg_user = schemas.UserRegistered(nickname=new_user_db.nickname, puk=new_puk, token=token)
    return new_reg_user

@router.post("/login", response_model=schemas.Token)
async def login_for_access_token(
    db: SessionInstance, form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    """
    Takes username and password as form data and returns an access token with the
    user-id as subject.
    """
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password!",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = create_access_token(user.id)
    token = schemas.Token(access_token=access_token, token_type="bearer")
    return token

@router.put("/password-reset", response_model=schemas.Message)
async def reset_password_logged_in(db: SessionInstance, current_user: CurrentUserToken, form_data: schemas.PasswordReset = Depends()):
    """
    Requires the user to be logged in. Takes the current password and a new password to change the current one.
    """
    authenticated_user = authenticate_user(db, current_user.nickname, form_data.current_password)
    if authenticated_user:
        reset_password(db, authenticated_user, form_data.new_password)
        return {"message": f"Password changed successfully for user: {current_user.nickname}"}
    if not authenticated_user:
        return {"message": f"Current password is wrong for user: {current_user.nickname}"}

@router.get("/test-token", response_model=schemas.Message)
async def test_access_token(current_user: CurrentUserToken):
    """
    Checks if the access token is valid by decoding it and returning the user attached to it.
    """
    return {"message": f"Valid token for user: {current_user.nickname}"}


@router.post("/password-recovery", response_model=schemas.Message)
def reset_password(db: SessionInstance, data: schemas.UserPasswordReset):
    user = read_user_by_nickname(db, data.nickname)

    if user.puk != data.puk:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Password update failed. Invalid data."
        )
    hashed_new_password = get_password_hash(data.new_password)
    user.password = hashed_new_password
    db.add(user)
    db.commit()

    return schemas.Message(message="Password succesfully updated.")
@router.get("/nickname", response_model=schemas.UserBase)
def generate_nickname(db: SessionInstance):
    """
    Generates a new nickname; crud function also checks if that nickname already exists in DB.
    """
    new_nickname = schemas.UserBase(nickname=crud.users.generate_nickname(db))
    return new_nickname

@router.get("/puk", response_model=schemas.UserPUK)
def generate_puk():
    """
    Generates a string with 8 single digits.
    """
    new_puk = schemas.UserPUK(puk=crud.users.generate_puk())
    return new_puk
