from fastapi import APIRouter

from .endpoints import example, users, auth, trackings

# init api
api = APIRouter()

# include endpoints here
api.include_router(example.router)
api.include_router(users.router)
api.include_router(auth.router)
api.include_router(trackings.router)