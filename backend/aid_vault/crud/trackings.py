from fastapi import HTTPException, status
from fastapi.encoders import jsonable_encoder
from sqlalchemy import update
from sqlalchemy.orm import Session

from ..schemas.trackings import *
from ..models.trackings import Trackings

import uuid

def check_id_equal(db: Session, tracking_id: UUID, current_user_id: UUID):
    """
    Checks if the tracking exists and raises an error if not.
    Checks whether the given tracking belongs to the current user.
    """
    tracking = read_tracking(db, tracking_id)
    if not tracking:
        raise HTTPException (status.HTTP_404_NOT_FOUND, detail="Resource not found")
    if tracking.user_id != current_user_id:
        raise HTTPException(status.HTTP_403_FORBIDDEN, detail="Access denied")
    else: 
        return True

def start_tracking(db: Session, s_time: int, current_user_id: UUID):
    """
    Generates a new UUID and starts that tracking with the given time.
    """
    new_uuid = uuid.uuid4()
    new_tracking = Trackings(id=new_uuid, user_id=current_user_id, time_start=s_time)
    db.add(new_tracking)
    db.commit()
    return new_tracking

def read_active_tracking(db: Session, current_user_id: UUID):
    """
    Filters the trackings, which don't have an end time set.
    """
    return db.query(Trackings).filter_by(time_end=None, user_id=current_user_id).all()

def read_tracking(db: Session, tracking_id: UUID):
    """
    Filters the trackings by given tracking ID and selects this one.
    """
    return db.query(Trackings).filter(Trackings.id == tracking_id).first()

def read_trackings(db: Session, current_user_id: UUID):
    """
    Filters the trackings by given User ID and selects all their trackings.
    """
    return db.query(Trackings).filter(Trackings.user_id == current_user_id).all()

def set_tracking_end(db: Session, tracking_id: UUID, tracking_input: TrackingStop):
    """
    Filters trackings by given ID and updates the end time.
    """
    db.query(Trackings).filter(Trackings.id == tracking_id).update({Trackings.time_end: tracking_input.time_end})
    db.commit()
    return read_tracking(db, tracking_id)

def delete_tracking(db: Session, tracking_id: UUID) -> None:
    """
    Deletes tracking by ID.
    """
    tracking = read_tracking(db, tracking_id)
    db.delete(tracking)
    db.commit()

def put_tracking_detail(db: Session, tracking_id: UUID, tracking_input: TrackingOptionals):
    """
    Puts (updates) tracking details by ID only if tracking detail is provided.
    """
    for key, value in tracking_input:
        if value != None:
            db.query(Trackings).filter(Trackings.id == tracking_id).update({key: value})
    db.commit()
    return read_tracking(db, tracking_id)