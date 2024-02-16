from pydantic import BaseModel
from .trackings import TrackingComplete

class GeneratedTrackings(BaseModel):
    seed: int | float | str 
    trackings: list[TrackingComplete]