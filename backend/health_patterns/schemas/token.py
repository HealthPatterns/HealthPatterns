from pydantic import BaseModel
from uuid import UUID

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    user_id: UUID | None = None