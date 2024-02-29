from fastapi import APIRouter

from .endpoints import users, auth, trackings, tooling

base_path = "/api"
api = APIRouter(prefix=base_path)

"""
Routers for different functionalities/endpoint categories go below.
"""
api.include_router(auth.router)
api.include_router(users.router)
api.include_router(trackings.router)
api.include_router(tooling.router)
