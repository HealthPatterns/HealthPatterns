from typing import Annotated
from datetime import datetime, timedelta
from uuid import UUID

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError

from ..schemas.users import UserComplete, UserFakeDB
from ..schemas.token import TokenData
from ..db.fake_db import fake_users_db

"""
This is used as a dependency in 'get_current_user()' so the function knows what
OAuth2 flow we are using and from what endpoint the JWT originates.
"""
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

"""
This data is to be put into a config.py file eventually.
Also SECRET_KEY will have to be stored in a safe way.
"""
SECRET_KEY = "3e7cde7fed126b5f15eefe7aac3895ac14c6c8cfa171743e9aefe29cd135579c"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


"""
Creates an access-token. The jwt payload should be fed as data: dict.
Main purpose is for creating an access-token after the "/auth/login" endpoint
has been called.
"""
def create_access_token(data: dict, expires_delta: timedelta | None = None):
    data_to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    data_to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(data_to_encode, SECRET_KEY, ALGORITHM)
    return encoded_jwt

"""
Two crud functions for reading the user from the fake database.
These will both be replaced with actual crud functions when the database is ready.
"""
def get_user(db: [UserFakeDB], user_id: UUID):
    mock_user = next((user for user in db if user.id == user_id), None)
    if mock_user:
        return mock_user

def get_user_by_name(db: [UserFakeDB], username: str):
    mock_user = next((user for user in db if user.nickname == username), None)
    if mock_user:
        return mock_user

"""
Returns the user attached to the jwt by decoding the token, checking if the sub is valid
and reading the user identified by the sub from the database.
Will throw errors if any step fails. 
"""    
async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, ALGORITHM)
        user_id: UUID = payload.get("sub")
        if user_id is None:
            credentials_exception.detail += " - no subject in token"
            raise credentials_exception
        token_data = TokenData(user_id=user_id)
    except JWTError as err:
        print(err)
        credentials_exception.detail += " - token decode error"
        raise credentials_exception
    
    user = get_user(fake_users_db, user_id=token_data.user_id)
    if user is None:
        credentials_exception.status_code=status.HTTP_404_NOT_FOUND
        credentials_exception.detail += " - unknown user"
        raise credentials_exception
    
    return user

"""
Checks if the user attached to the jwt is active.
"""
async def get_current_active_user(
        current_user: Annotated[UserComplete, Depends(get_current_user)]
):
    if not current_user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Inactive User"
        )
    return current_user

"""
Putting this as a type-hint into a path operation function will start the 
dependency injection cascade of token auth functions ending with the data
of the currently logged in user (or an auth error).
"""
CurrentUserToken = Annotated[UserComplete, Depends(get_current_active_user)]