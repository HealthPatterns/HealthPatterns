import random
from fastapi import APIRouter

from aid_vault import crud, schemas, models

from ...schemas.tooling import GeneratedTrackings
from ...db.database import SessionInstance
from ...common import tooling

router = APIRouter(prefix="/tooling", tags=["Tooling"])


@router.get("/tracking-generator", response_model=GeneratedTrackings)
def generate_trackings(amount: int = 1, seed: int | None = None):
    """
    Generate trackings and return them as JSON. Takes amount of trackings to generate and seed as query-parameters. For random seed leave empty.
    """
    if seed is None:
        seed = random.getrandbits(16)

    tracking_list = []
    for i in range(amount):
        tracking_list.append(tooling.generate_tracking(seed + i))

    return GeneratedTrackings(seed=seed, trackings=tracking_list)

@router.get("/all_users", response_model=list[schemas.UserComplete])
def get_users(db: SessionInstance) -> list[models.Users]:
    """
    Returns all users from DB.
    """
    return crud.users.read_all_users(db=db)
