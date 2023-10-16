from sqlalchemy import ForeignKey, Column, Integer, String, Boolean, UUID, text

from ..db.base_class import Base

class Trackings(Base):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    time_start = Column(String, unique=False, nullable=False)
    time_end = Column(String, unique=False, nullable=True)
    front_regions = Column(Boolean[19], nullable = True)
    back_regions = Column(Boolean[18], nullable = True)
    intensity = Column(Integer, nullable = True)
    diet = Column(String, nullable = True)

    def __init__ (self, id, user_id, time_start, time_end, front_regions, back_regions, intensity, diet):
        self.id = id
        self.user_id = user_id
        self.time_start = time_start
        self.time_end = time_end
        self.front_regions = front_regions
        self.back_regions = back_regions
        self.intensity = intensity
        self.diet = diet