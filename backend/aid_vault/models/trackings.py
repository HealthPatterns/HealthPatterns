from sqlalchemy import ForeignKey, Column, BigInteger, String, Boolean, UUID, text, ARRAY, JSON, Integer

from ..db.base_class import Base

class Trackings(Base):
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()")
    )
    user_id = Column(UUID, ForeignKey("users.id"), nullable=False)
    time_start = Column(BigInteger, unique=False, nullable=False)
    time_end = Column(BigInteger, unique=False, nullable=True)
    front_regions = Column(ARRAY(Boolean), nullable = True)
    back_regions = Column(ARRAY(Boolean), nullable = True)
    intensity = Column(Integer, nullable = True)
    diet = Column(JSON, nullable = True)