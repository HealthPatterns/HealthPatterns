from sqlalchemy import ForeignKey, Column, Integer, String, Boolean

from ..db.base_class import Base

class Trackings(Base):
    __tablename__ = "trackings"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    time_start = Column(String, unique=False, nullable=True)
    time_end = Column(String, unique=False, nullable=True)

    def __init__ (self, id, user_id, time_start, time_end):
        self.id = id
        self.user_id = user_id
        self.time_start = time_start
        self.time_end = time_end

class TrackingDetails(Base):
    __tablename__ = "tracking_details"
    id = Column(Integer, primary_key=True)
    tracking_id = Column(Integer, ForeignKey("trackings.id"), nullable=False)
    front_regions = Column(Boolean[19], nullable = False)
    back_regions = Column(Boolean[18], nullable = False)
    intensity = Column(Integer, nullable = True)
    diet = Column(String, nullable = True)

    def __init__ (self, id, tracking_id, front_regions, back_regions, intensity, diet):
        self.id = id
        self.tracking_id = tracking_id
        self.front_regions = front_regions
        self.back_regions = back_regions
        self.intensity = intensity
        self.diet = diet