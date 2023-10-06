from fastapi import APIRouter

from .endpoints import example

# init api
api = APIRouter()

# include user endpoints
api.include_router(example.router)

### include more endpoints here