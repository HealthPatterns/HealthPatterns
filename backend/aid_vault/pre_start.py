from sqlalchemy.orm import Session

from aid_vault import crud, schemas
from .db.database import SessionInstance
from .common.security import get_password_hash

def create_admin(db: Session) -> str:
    if crud.user_exists_by_nickname(db, "admin"):
        return "Test-user creation: User 'admin' with password 'admin' already exists."
    admin = schemas.UserCreate(nickname="admin", password=get_password_hash("admin"))
    crud.create_user(db, admin)
    return "Test-user creation: User 'admin' with password 'admin' created."