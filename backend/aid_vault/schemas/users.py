from pydantic import BaseModel
from uuid import UUID

class UserBase(BaseModel):
    nickname: str

class UserOptionals(UserBase):
    full_name: str | None = None
    age: int | None = None
    gender: int | None = None
    email: int | None = None
    # other optional user-details

class UserCreate(UserOptionals): 
    # this is only used for creation of a new user, and only as payload from the client
    plain_password: str

<<<<<<< HEAD
class UserComplete(UserCreate):
    id: int
=======
class UserComplete(UserOptionals):
    id: UUID
>>>>>>> 46e08e5790f0aa5e85d899d6d810ed09aad77f25
    is_active: bool

    class Config:
        orm_mode = True

class UserForUpdate(BaseModel):
    nickname: str | None = None
    full_name: str | None = None
    age: int | None = None
    gender: str | None = None
    email: str | None = None
    is_active: bool | None = None

class UserFakeDB(UserComplete):
    hashed_password: str
