from fastapi import APIRouter

<<<<<<< HEAD
from .endpoints import example, users, test
=======
from .endpoints import example, users, auth, trackings
>>>>>>> 46e08e5790f0aa5e85d899d6d810ed09aad77f25

# init api
api = APIRouter()

# include endpoints here
api.include_router(example.router)
api.include_router(users.router)
<<<<<<< HEAD
api.include_router(test.router)
### include more endpoints here
=======
api.include_router(auth.router)
api.include_router(trackings.router)
>>>>>>> 46e08e5790f0aa5e85d899d6d810ed09aad77f25
