import random
from fastapi import APIRouter

from ...schemas.trackings import TrackingComplete
from ...schemas.tooling import GeneratedTrackings
from ...common.oauth2 import CurrentUserToken
from ...common import tooling

router = APIRouter(
    prefix="/tooling",
    tags=["Tooling"]
)

@router.get("/tracking-generator/", response_model=GeneratedTrackings)
def generate_trackings(amount: int = 1, seed: int | None = None):
    """
    Generate trackings and return them as JSON. 
    For random seed input 0.
    """
    if seed is None:
        seed = random.getrandbits(16)

    tracking_list = []
    for i in range(amount):
        tracking_list.append(tooling.generate_tracking(seed + i))

    return GeneratedTrackings(seed=seed, trackings=tracking_list)