from fastapi import FastAPI

from .db.base_class import Base
from .db.database import engine
from .api.api import api

# create db tables
Base.metadata.create_all(bind=engine)

# init app
app = FastAPI()

# include api
app.include_router(api)