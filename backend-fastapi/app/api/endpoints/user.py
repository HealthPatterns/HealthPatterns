from fastapi import APIRouter, HTTPException

from ...schemas.user import UserSchema, UserCreate
from ...common import crud_user
from ...db.database import SessionDep

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.post("/", response_model=UserSchema)
def create_user(db: SessionDep, user: UserCreate):
    db_user = crud_user.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered.")
    return crud_user.create_user(db=db, user=user)

@router.get("/", response_model=list[UserSchema])
def get_users(db: SessionDep, skip: int = 0, limit: int = 100):
    users = crud_user.get_users(db, skip, limit)
    return users

@router.get("/{user_id}", response_model=UserSchema)
def get_user(db: SessionDep, user_id: int):
    db_user = crud_user.get_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="Not found.")
    return db_user

# @router.put("/{user_id}", response_model=UserSchema)
# def put_user(db: SessionDep, user_id: int, user: UserSchema):
#     db_user = crud_user.get_user(db, user_id)
#     if not db_user:
#         raise HTTPException(status_code=404, detail="Not found.")
#     return crud_user.update_user(db, user)
    