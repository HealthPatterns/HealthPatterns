from sqlalchemy import Column, Integer, String, Boolean

from ..db.base_class import Base

class User(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=False, nullable=True)
    email = Column(String, unique=True, nullable=False)
    is_active = Column(Boolean, default=True)