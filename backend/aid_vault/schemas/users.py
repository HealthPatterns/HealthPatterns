from pydantic import BaseModel
from uuid import UUID
from aid_vault.schemas import Token

class UserBase(BaseModel):
    nickname: str

class UserPUK(BaseModel):
    puk: str

class UserDisplayName(BaseModel):
    display_name: str

class UserOptionals(UserBase):
    full_name: str | None = None
    age: int | None = None
    gender: str | None = None
    email: str | None = None
    # other optional user-details

class UserCreateAdmin(BaseModel):
    nickname: str
    age: int
    email: str
    full_name: str
    puk: str
    gender: str
    password: str

class UserCreate(BaseModel): 
    """
    Contains password, so this is only used for creation of a new user and should NEVER be used as a response_model!
    """
    password: str

class UserCreateDB(UserBase):
    puk: str
    password: str

class UserRegistered(UserBase):
    puk: str
    token: Token

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
