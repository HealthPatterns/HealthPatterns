from ..schemas.trackings import *
import uuid

def start_tracking(db: list[TrackingComplete], s_time: int):
    new_uuid = uuid.uuid4()
    new_tracking = TrackingComplete(id=str(new_uuid), start_time=s_time, is_active=True)
    db.append(new_tracking)
    return new_tracking

def read_active_tracking(db: list[TrackingComplete]):
    return [tracking for tracking in db if tracking.end_time is None]

def read_tracking(db: list[TrackingComplete], tracking_id: str):
    return next((tracking for tracking in db if tracking.id == tracking_id), None)

def read_trackings(db: list[TrackingComplete]):
    return db

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