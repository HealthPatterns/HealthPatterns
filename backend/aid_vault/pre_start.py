from sqlalchemy.orm import Session

from aid_vault import crud, schemas
from .common.security import get_password_hash, get_puk_hash


def create_test_user(db: Session) -> str:
    """
    Function to check if the test-user already exists. If it doesn't it is created with test data.
    """    
    if crud.user_exists_by_nickname(db, "admin"):
        return "Test-user creation: User 'admin' with password 'admin' already exists."
    admin = schemas.UserCreateAdmin(
        nickname="admin",
        age=42,
        email="admin@testuser.com",
        full_name="Mister Admin",
        puk=get_puk_hash("12345678"),
        gender="male",
        password=get_password_hash("admin"))
    if crud.user_exists_by_email(db, admin.email):
        admin.email = None
    crud.create_user(db, admin)
    return "Test-user creation: User 'admin' with password 'admin' created."