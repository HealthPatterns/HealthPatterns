from fastapi import APIRouter, status, HTTPException

from health_patterns import crud, schemas, models
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

@router.get("/name", response_model=schemas.UserDisplayName)
def get_user_name(current_user: CurrentUserToken) -> models.Users:
    """
    Returns currently logged in user's display name. The display name is the full name, or nickname if the full name is null.
    """
    if current_user.full_name is not None:
        name = schemas.UserDisplayName(display_name=current_user.full_name)
        return name
    name = schemas.UserDisplayName(display_name=current_user.nickname)
    return name

@router.put("", response_model=schemas.UserComplete)
def update_user_data(
    db: SessionInstance,
    current_user: CurrentUserToken,
    input_data: schemas.UserForUpdate
) -> models.Users:
    """
    Updates currently logged in user. Fields that get put in as null or omitted will be set to null. If nickname is set to null or omitted it will stay unchanged, as it cannot be deleted.
    """
    if input_data.nickname is None:
        input_data.nickname = current_user.nickname

    if input_data.nickname != current_user.nickname:
        if crud.user_exists_by_nickname(db, input_data.nickname):
            raise HTTPException(
                status_code=400,
                detail="User with this username already exists."
            )
    if input_data.email != current_user.email:
        if crud.user_exists_by_email(db, input_data.email):
            raise HTTPException(
                status_code=400,
                detail="This email-address is already registered."
            )
    updated_user = crud.users.update_user(
        db=db,
        update_data=input_data,
        user_id=current_user.id
    )
    return updated_user

@router.delete("", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(db: SessionInstance, current_user: CurrentUserToken):
    """
    Deletes currently logged in user and their corresponding trackings, if there are any.
    """
    crud.trackings.delete_user_trackings(db=db, current_user_id=current_user.id)
    crud.users.delete_user_by_id(db=db, user_id=current_user.id)
    return
