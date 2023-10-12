from fastapi import APIRouter

from .endpoints import example, users, test

# init api
api = APIRouter()

# include user endpoints
api.include_router(example.router)
api.include_router(users.router)
api.include_router(test.router)
### include more endpoints here