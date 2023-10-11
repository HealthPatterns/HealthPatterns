from fastapi import APIRouter

from .endpoints import example, users, auth

# init api
api = APIRouter()

# include user endpoints
api.include_router(example.router)
api.include_router(users.router)
### include more endpoints here

api.include_router(auth.router)