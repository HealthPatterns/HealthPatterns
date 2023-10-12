from pydantic import BaseModel

class TrackingBase(BaseModel):
    id: str

class TrackingStart(TrackingBase):
    start_time: int
    is_active: bool

class TrackingStop(TrackingStart):
    end_time: int | None = None

class TrackingOptionals(TrackingBase):
    region: str | None = None
    intensity: str | None = None
    sleep: str | None = None
    diet: str | None = None

class TrackingSchema(TrackingStop):
    pass

    class Config:
        orm_mode = True

