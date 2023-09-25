from fastapi import APIRouter

from .endpoints import user

api = APIRouter()

api.include_router(user.router)
### include more routers here