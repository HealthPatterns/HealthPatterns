from typing import Annotated
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from fastapi import Depends

"""
This is quick and dirty, for production we should use some kind of config and not hardcode URIs.
See Issue #33 'Secret and config management' on GitHub.
"""
SQLALCHEMY_DATABASE_URI = "postgresql://name:password@aid-db:5432/aid-db"
engine = create_engine(SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """
    This function creates a new database session when injected as a dependency in another function and closes said connection after the calling function terminates.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

"""
Putting this as a type-hint into a path operation function injects 'get_db()' as a dependency, thus serving a database session that can be used inside of the calling function.
"""
SessionInstance = Annotated[Session, Depends(get_db)]