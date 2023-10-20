from pydantic import BaseModel
from uuid import UUID

class UserBase(BaseModel):
    nickname: str

class UserFullName(BaseModel):
    full_name: str

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
