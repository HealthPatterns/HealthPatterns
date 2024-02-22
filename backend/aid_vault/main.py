from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .db.base_class import Base
from .db.database import engine, SessionLocal
from .api.api import api
from .pre_start import create_test_user

# create db tables
Base.metadata.create_all(bind=engine)

# create admin user for testing
db = SessionLocal()
print(create_test_user(db))

# init app
app = FastAPI()

# setup CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost","https://localhost"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

# include main api
app.include_router(api)