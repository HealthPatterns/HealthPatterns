from typing import Annotated
from datetime import timedelta

from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm


from aid_vault import crud, models, schemas
from ...common.security import authenticate_user
from ...common.oauth2 import (
    create_access_token, 
    CurrentUserToken, 
    ACCESS_TOKEN_EXPIRE_MINUTES
)
from ...db.database import SessionInstance
from ...db.fake_db import fake_users_db

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/login", response_model=schemas.Token)
async def login_for_access_token(
    db: SessionInstance,
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    """
    Takes username and password as form data and returns an access token with the 
    user-id as subject.
    """
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"}
        )
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.id.hex}, expires_delta=access_token_expires
    )
    
    token = schemas.Token(access_token=access_token, token_type="bearer")
    return token


@router.get("/test-token", response_model=schemas.Message)
async def test_access_token(current_user: CurrentUserToken):
    """
    Checks if the access token is valid by decoding it and returning the user attached to it.
    """
    return {"message": f"Valid token for user: {current_user.nickname}"}