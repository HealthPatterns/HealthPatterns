from pydantic import BaseModel
from uuid import UUID

class UserBase(BaseModel):
    nickname: str

class UserDisplayName(BaseModel):
    display_name: str

class UserOptionals(UserBase):
    full_name: str | None = None
    age: int | None = None
    gender: str | None = None
    email: str | None = None
    # other optional user-details

class UserCreate(UserOptionals): 
    """
    Contains password, so this is only used for creation of a new user and should NEVER be used as a response_model!
    """
    password: str

class UserPasswordReset(BaseModel):
    new_password: str
    nickname: str
    puk: str

class UserComplete(UserOptionals):
    id: UUID
    is_active: bool

    class Config:
        from_attributes = True

class UserForUpdate(BaseModel):
    nickname: str | None = None
    full_name: str | None = None
    age: int | None = None
    gender: str | None = None
    email: str | None = None
    is_active: bool | None = None
