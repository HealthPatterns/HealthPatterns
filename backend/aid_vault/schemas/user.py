from pydantic import BaseModel

class UserBase(BaseModel):
    email: str
    name: str | None = None

class UserCreate(UserBase):
    pass

class UserSchema(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True

