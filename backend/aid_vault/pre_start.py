from sqlalchemy.orm import Session

from aid_vault import crud, schemas
from .common.security import get_password_hash


def create_test_user(db: Session) -> str:
    """
    Function to check if the test-user already exists. If it doesn't it is created with test data.
    """    
    if crud.user_exists_by_nickname(db, "admin"):
        return "Test-user creation: User 'admin' with password 'admin' already exists."
    admin = schemas.UserCreate(
        nickname="admin",
        age=42,
        email="admin@testuser.com",
        full_name="Mister Admin",
        gender="male",
        password=get_password_hash("admin"))
    crud.create_user(db, admin)
    return "Test-user creation: User 'admin' with password 'admin' created."