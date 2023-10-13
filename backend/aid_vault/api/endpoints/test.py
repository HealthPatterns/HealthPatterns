from fastapi import APIRouter, HTTPException, status, Response
from fastapi.encoders import jsonable_encoder

from ...models.users import Users
from ...schemas.users_new import UserComplete
from ...common import crud_users
from ...db.database import SessionInstance

# declare router with default values
router = APIRouter(
    prefix="/test",
    tags=["test"] # -> makes endpoints show up in its own category in the documentation
)

@router.get("/")
def get_user(db: SessionInstance, user_id: int):
    if not crud_users.user_exists_by_id(db=db, user_id=user_id):
        raise HTTPException(status_code=400, detail="User does not exist")
    
    return crud_users.read_user(db=db, user_id=user_id)

@router.post("/")
def create_user(db: SessionInstance, user: UserComplete):

    if crud_users.user_exists(db, email=user.email):
        raise HTTPException(status_code=400, detail="User already registered.")
    
    return crud_users.create_user(db=db, user=user)