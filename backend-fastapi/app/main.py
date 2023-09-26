from fastapi import FastAPI

from .db.base_class import Base
from .db.database import engine
from .api.api import api

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(api)
