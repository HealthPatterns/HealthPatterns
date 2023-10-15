from pydantic import BaseModel

class TrackingBase(BaseModel):
    id: str

class TrackingStart(BaseModel):
    start_time: int

class TrackingActive(TrackingBase):
    start_time: int

class TrackingStop(TrackingBase):
    end_time: int | None = None

class TrackingFrontRegions(BaseModel):
    front_regions: list[bool] | None = None

class TrackingBackRegions(BaseModel):
    back_regions: list[bool] | None = None

class TrackingIntensity(BaseModel):
    intensity: int | None = None

class TrackingSleep(BaseModel):
    sleep: str | None = None

class TrackingDiet(BaseModel):
    diet: str | None = None

class TrackingOptionals(TrackingBase):
    front_regions: list[bool] | None = None
    back_regions: list[bool] | None = None
    intensity: int | None = None
    sleep: str | None = None
    diet: str | None = None

class TrackingSchema(TrackingStop):
    start_time: int
    pass

    class Config:
        orm_mode = True

class TrackingComplete(TrackingSchema):
    front_regions: list[bool] | None = None
    back_regions: list[bool] | None = None
    intensity: int | None = None
    sleep: str | None = None
    diet: str | None = None