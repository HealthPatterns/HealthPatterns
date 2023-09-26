from fastapi import APIRouter

from .endpoints import user

# init api
api = APIRouter()

# include user endpoints
api.include_router(user.router)

### include more endpoints here