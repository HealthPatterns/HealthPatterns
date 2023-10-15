from sqlalchemy import ForeignKey, Column, Integer, String, Boolean

from ..db.base_class import Base

class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    nickname = Column(String, unique=True, nullable=False)
    full_name = Column(String, unique=False, nullable=True)
    age = Column(Integer, unique=False, nullable=True)
    gender = Column(String, unique=False, nullable=True)
    password = Column(String, unique=False, nullable=False)
    email = Column(String, unique=True, nullable=True)
    is_active = Column(Boolean, default=True, nullable=False)

    def __init__ (self, id, nickname, full_name, age, gender, password, email, is_active):
        self.id = id
        self.nickname = nickname
        self.full_name = full_name
        self.age = age
        self.gender = gender
        self.password = password
        self.email = email
        self.is_active = is_active