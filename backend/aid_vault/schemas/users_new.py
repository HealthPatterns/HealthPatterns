from pydantic import BaseModel

class UserComplete(BaseModel):
    id: int
    nickname: str
    full_name: str | None = None
    age: int | None = None
    email: str
    password: str
    is_active: bool

class UserForUpdate(BaseModel):
    nickname: str | None = None
    full_name: str | None = None
    age: int | None = None
    email: str | None = None
    password: str | None = None
    is_active: bool | None = None