from pydantic import BaseModel
from typing import Any, Dict
from uuid import UUID

class TrackingBase(BaseModel):
    id: UUID

class TrackingStart(TrackingBase):
    time_start: int

class TrackingSetStart(BaseModel):
    time_start: int

class TrackingActive(TrackingBase):
    time_start: int

class TrackingStop(BaseModel):
    time_end: int | None = None

class TrackingFrontRegions(BaseModel):
    front_regions: list[bool] | None = None

class TrackingBackRegions(BaseModel):
    back_regions: list[bool] | None = None

class TrackingIntensity(BaseModel):
    intensity: int | None = None

class TrackingDiet(BaseModel):
    diet: Dict[str, Any] | None = None

class TrackingOptionals(BaseModel):
    front_regions: list[bool] | None = None
    back_regions: list[bool] | None = None
    intensity: int | None = None
    diet: Dict[str, Any] | None = None

class TrackingSchema(BaseModel):
    time_start: int
    time_end: int | None = None

class TrackingComplete(TrackingBase):
    #user_id: UUID
    time_start: int
    time_end: int | None = None
    front_regions: list[bool] | None = None
    back_regions: list[bool] | None = None
    intensity: int | None = None
    diet: Dict[str, Any] | None = None

    class Config:
        from_attributes = True