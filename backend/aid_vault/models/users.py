from sqlalchemy import Column, Integer, String, Boolean, UUID, text

from ..db.base_class import Base

class Users(Base):
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()")
    )
    nickname = Column(String, unique=True, nullable=False)
    full_name = Column(String, unique=False, nullable=True)
    age = Column(Integer, unique=False, nullable=True)
    gender = Column(String, unique=False, nullable=True)
    password = Column(String, unique=False, nullable=False)
    puk= Column(String, unique=False, nullable=False)
    email = Column(String, unique=True, nullable=True)
    is_active = Column(Boolean, default=True)