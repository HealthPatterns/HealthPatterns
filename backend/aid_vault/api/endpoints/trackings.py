from fastapi import APIRouter, status

from ...schemas.trackings import *
from ...crud import trackings
from ...db.database import SessionInstance
from ...common.oauth2 import CurrentUserToken

router = APIRouter(
    prefix="/trackings",
    tags=["Trackings"]
)

"""
@router.post("", response_model=TrackingSchema, status_code=status.HTTP_201_CREATED)
def create_tracking(tracking: TrackingStart):
    users.create_user(tracking)
    return
"""

@router.get("", response_model=list[TrackingComplete])
def get_all_trackings(db: SessionInstance, current_user: CurrentUserToken):#skip: int = 0, limit: int = 10):
    """
    Get all trackings owned by current user.
    """
    return trackings.read_trackings(db, current_user.id)

@router.post("", response_model=TrackingStart, status_code=status.HTTP_201_CREATED)
def start_tracking(db: SessionInstance, current_user: CurrentUserToken, input_data: TrackingSetStart):
    """
    Create new tracking and set its start time.
    """
    return trackings.start_tracking(db, input_data.time_start, current_user.id)

@router.get("/active", response_model=list[TrackingActive])
def get_active_trackings(db: SessionInstance, current_user: CurrentUserToken):#skip: int = 0, limit: int = 10):
    """
    Get all active trackings for current user.
    """
    return trackings.read_active_tracking(db, current_user.id)

@router.get("/{tracking_id}", response_model=TrackingSchema)
def get_tracking(db: SessionInstance, current_user: CurrentUserToken, tracking_id: UUID):
    """
    Get tracking by ID.
    """
    trackings.check_id_equal(db, tracking_id, current_user.id)
    return trackings.read_tracking(db, tracking_id)

@router.put("/{tracking_id}", response_model=TrackingSchema)
def set_tracking_end(db: SessionInstance, current_user: CurrentUserToken, tracking_id: UUID, tracking_input: TrackingStop):
    """
    Put end time to specific tracking by ID.
    """
    trackings.check_id_equal(db, tracking_id, current_user.id)
    return trackings.set_tracking_end(db, tracking_id, tracking_input)

@router.delete("/{tracking_id}", status_code=status.HTTP_200_OK)
def delete_tracking(db: SessionInstance, current_user: CurrentUserToken, tracking_id: UUID):
    """
    Delete tracking by ID.
    """
    trackings.check_id_equal(db, tracking_id, current_user.id)
    trackings.delete_tracking(db, tracking_id)
    return "tracking deleted"

@router.get("/{tracking_id}/details", response_model=TrackingOptionals)
def get_all_tracking_details(db: SessionInstance, current_user: CurrentUserToken, tracking_id: UUID):
    """
    Get all optional details of tracking by ID.
    """
    trackings.check_id_equal(db, tracking_id, current_user.id)
    return trackings.read_tracking(db, tracking_id)
 
@router.put("/{tracking_id}/details", response_model=TrackingOptionals)
def put_tracking_detail(db: SessionInstance, current_user: CurrentUserToken, tracking_id: UUID, tracking_input: TrackingOptionals):
    """
    Put detail or details to specific tracking by ID.
    """
    trackings.check_id_equal(db, tracking_id, current_user.id)
    return trackings.put_tracking_detail(db, tracking_id, tracking_input)

@router.get("/{tracking_id}/details_front", response_model=TrackingFrontRegions)
def get_front_regions(db: SessionInstance, current_user: CurrentUserToken, tracking_id: UUID):
    """
    Get front region details of tracking by ID.
    """
    trackings.check_id_equal(db, tracking_id, current_user.id)
    return trackings.read_tracking(db, tracking_id)

@router.get("/{tracking_id}/details_back", response_model=TrackingBackRegions)
def get_back_regions(db: SessionInstance, current_user: CurrentUserToken, tracking_id: UUID):
    """
    Get back region details of tracking by ID.
    """
    trackings.check_id_equal(db, tracking_id, current_user.id)
    return trackings.read_tracking(db, tracking_id)

@router.get("/{tracking_id}/details_intensity", response_model=TrackingIntensity)
def get_intensity(db: SessionInstance, current_user: CurrentUserToken, tracking_id: UUID):
    """
    Get intensity details of tracking by ID.
    """
    trackings.check_id_equal(db, tracking_id, current_user.id)
    return trackings.read_tracking(db, tracking_id)

"""
@router.get("/{tracking_id}/details_sleep", response_model=TrackingSleep)
def get_sleep(db: SessionInstance, current_user: CurrentUserToken, tracking_id: str):
    
    Get sleep details of tracking by ID.
    
    trackings.check_id_equal(db, tracking_id, current_user)
    tracking = trackings.read_tracking(db, tracking_id)
    return tracking
"""

@router.get("/{tracking_id}/details_diet", response_model=TrackingDiet)
def get_diet(db: SessionInstance, current_user: CurrentUserToken, tracking_id: UUID):
    """
    Get diet details of tracking by ID.
    """
    trackings.check_id_equal(db, tracking_id, current_user.id)
    return trackings.read_tracking(db, tracking_id)