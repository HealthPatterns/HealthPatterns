from fastapi import APIRouter

from .endpoints import example, users, trackings

# init api
api = APIRouter()

# include user endpoints
api.include_router(example.router)
api.include_router(users.router)
api.include_router(trackings.router)
### include more endpoints here