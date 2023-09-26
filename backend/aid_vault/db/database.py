from typing import Annotated
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from fastapi import Depends

# this is quick and dirty, for production we should use some kind of config and not hardcode URIs
SQLALCHEMY_DATABASE_URI = "postgresql://name:password@aid-db:5432/aid-db"
engine = create_engine(SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

SessionInstance = Annotated[Session, Depends(get_db)]