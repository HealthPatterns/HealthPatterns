from ..schemas.trackings import TrackingSchema, TrackingOptionals, TrackingBase, TrackingComplete
import uuid

def start_tracking(db: list[TrackingComplete], s_time: int):
    new_uuid = uuid.uuid4()
    new_tracking = TrackingComplete(id=str(new_uuid), start_time=s_time, is_active=True)
    db.append(new_tracking)
    return new_tracking

def read_active_tracking(db: list[TrackingComplete]):
    return [tracking for tracking in db if tracking.is_active]

def read_tracking(db: list[TrackingComplete], tracking_id: str):
    return next((tracking for tracking in db if tracking.id == tracking_id), None)

def read_trackings(db: list[TrackingComplete]):
    return db

def set_tracking_end(db:list[TrackingComplete], tracking_id:str, e_time: int):
    tracking = read_tracking(db, tracking_id)
    tracking.end_time = e_time
    tracking.is_active = False
    return tracking

def delete_tracking(db: list[TrackingComplete], tracking_id: str) -> None:
    tracking = read_tracking(db, tracking_id)
    db.remove(tracking)

# probably not necessary
def get_all_tracking_details(db: list[TrackingComplete], tracking_id: str):
    return read_tracking(db, tracking_id)

def put_tracking_detail(db: list[TrackingComplete], tracking_id: str, attribute: str, value:str):
    tracking = read_tracking(db, tracking_id)
    match attribute:
        case "region":
            tracking.region=value
        case "intensity":
            tracking.intensity=value
        case "sleep":
            tracking.sleep=value
        case "diet":
            tracking.diet=value
    return tracking

def get_specific_tracking_details(db: list[TrackingComplete], tracking_id: str, attribute: str):
    tracking = read_tracking(db, tracking_id)
    match attribute:
        case "region":
            new_tracking = TrackingOptionals(id=tracking_id, region=tracking.region)
        case "intensity":
            new_tracking = TrackingOptionals(id=tracking_id, intensity=tracking.intensity)
        case "sleep":
            new_tracking = TrackingOptionals(id=tracking_id, sleep=tracking.sleep)
        case "diet":
            new_tracking = TrackingOptionals(id=tracking_id, diet=tracking.diet)
    return new_tracking
