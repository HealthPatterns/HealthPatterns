from pydantic import BaseModel

class UserComplete(BaseModel):
    id: int
    nickname: str
    full_name: str | None = None
    age: int | None = None
    email: str
    password: str
    is_active: bool
    
