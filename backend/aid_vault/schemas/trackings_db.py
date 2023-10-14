from pydantic import BaseModel

class TrackingBase(BaseModel):
    id: str

class TrackingStart(TrackingBase):
    start_time: int

class TrackingStop(TrackingStart):
    end_time: int | None = None

"""
class TrackingRegion(TrackingBase):
    region: str | None = None

class TrackingIntensity(TrackingBase):
    intensity: str | None = None

class TrackingSleep(TrackingBase):
    sleep: str | None = None

class TrackingDiet(TrackingBase):
    diet: str | None = None
"""

class TrackingOptionals(TrackingBase):
    region: str | None = None
    intensity: str | None = None
    sleep: str | None = None
    diet: str | None = None

class TrackingSchema(TrackingStop):
    is_active: bool
    pass

    class Config:
        orm_mode = True

class TrackingComplete(TrackingSchema):
    region: str | None = None
    intensity: str | None = None
    sleep: str | None = None
    diet: str | None = None