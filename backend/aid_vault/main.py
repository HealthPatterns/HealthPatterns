from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .db.base_class import Base
from .db.database import engine
from .api.api import api

# create db tables
Base.metadata.create_all(bind=engine)

# init app
app = FastAPI()

# setup CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

# include api
app.include_router(api)