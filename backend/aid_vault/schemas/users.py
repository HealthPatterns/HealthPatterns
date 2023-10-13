from pydantic import BaseModel

class UserBase(BaseModel):
    nickname: str

class UserOptionals(UserBase):
    full_name: str | None = None
    age: int | None = None
    # other optional user-details

class UserCreate(UserOptionals): 
    # this is only used for creation of a new user, and only as payload from the client
    password: str

class UserComplete(UserOptionals):
    id: int
    is_active: bool

    class Config:
        orm_mode = True