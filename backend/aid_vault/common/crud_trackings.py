from fastapi import HTTPException, status

from ..schemas.trackings import *
from ..common.oauth2 import CurrentUserToken
import uuid

def check_id_equal(db: list[TrackingComplete], tracking_id: str, current_user: CurrentUserToken):
    tracking = read_tracking(db, tracking_id)
    if not tracking:
        raise HTTPException (status.HTTP_404_NOT_FOUND, detail="Resource not found")
    if tracking.user_id != current_user.id:
        raise HTTPException(status.HTTP_403_FORBIDDEN, detail="Access denied")
    else: 
        return True

def start_tracking(db: list[TrackingComplete], s_time: int, current_user: CurrentUserToken):
    new_uuid = uuid.uuid4()
    new_tracking = TrackingComplete(id=str(new_uuid), start_time=s_time, user_id=current_user.id)
    db.append(new_tracking)
    return new_tracking

def read_active_tracking(db: list[TrackingComplete], current_user: CurrentUserToken):
    return [tracking for tracking in db if tracking.end_time is None and tracking.user_id == current_user.id]

def read_tracking(db: list[TrackingComplete], tracking_id: str):
    return next((tracking for tracking in db if tracking.id == tracking_id), None)

def read_trackings(db: list[TrackingComplete], current_user: CurrentUserToken):
    return [tracking for tracking in db if tracking.user_id == current_user.id]

def set_tracking_end(db:list[TrackingComplete], tracking_input: TrackingStop):
    tracking = read_tracking(db, tracking_input.id)
    tracking.end_time = tracking_input.end_time
    return tracking

def delete_tracking(db: list[TrackingComplete], tracking_id: str) -> None:
    tracking = read_tracking(db, tracking_id)
    db.remove(tracking)

# probably not necessary
def get_all_tracking_details(db: list[TrackingComplete], tracking_id: str):
    return read_tracking(db, tracking_id)

def put_tracking_detail(db: list[TrackingComplete], tracking_input: TrackingOptionals):
    tracking = read_tracking(db, tracking_input.id)
    tracking.front_regions = tracking_input.front_regions
    tracking.back_regions = tracking_input.back_regions
    tracking.intensity = tracking_input.intensity
    tracking.sleep = tracking_input.sleep
    tracking.diet = tracking_input.diet
    return tracking