from fastapi import APIRouter

from .endpoints import example, users

# init api
api = APIRouter()

# include user endpoints
api.include_router(example.router)
api.include_router(users.router)
### include more endpoints here