from fastapi import APIRouter

from .endpoints import users, auth, trackings, tooling

api = APIRouter()

"""
Routers for different functionalities/endpoint categories go below.
"""
api.include_router(auth.router)
api.include_router(users.router)
api.include_router(trackings.router)
api.include_router(tooling.router)