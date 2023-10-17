from fastapi import APIRouter, HTTPException, status

from ...schemas.trackings import *
from ...common import crud_trackings
from ...db.fake_db_details import fake_trackings_db
from ...common.oauth2 import CurrentUserToken

router = APIRouter(
    prefix="/trackings",
    tags=["Trackings"]
)

"""
@router.post("", response_model=TrackingSchema, status_code=status.HTTP_201_CREATED)
def create_tracking(tracking: TrackingStart):
    crud_users.create_user(tracking)
    return
"""

@router.get("", response_model=list[TrackingComplete])
def get_all_trackings(current_user: CurrentUserToken):#skip: int = 0, limit: int = 10):
    """
    get all trackings
    """
    all_trackings = crud_trackings.read_trackings(fake_trackings_db, current_user)
    return all_trackings

@router.post("", response_model=TrackingBase, status_code=status.HTTP_201_CREATED)
def start_tracking(current_user: CurrentUserToken, input_data: TrackingStart):
    """
    create new tracking and post time
    """
    new_tracking = crud_trackings.start_tracking(fake_trackings_db, input_data.start_time, current_user)
    return new_tracking

@router.get("/active", response_model=list[TrackingActive])
def get_active_trackings(current_user: CurrentUserToken):#skip: int = 0, limit: int = 10):
    """
    get all active trackings
    """
    active_trackings = crud_trackings.read_active_tracking(fake_trackings_db, current_user)
    return active_trackings

@router.get("/tracking", response_model=TrackingSchema)
def get_tracking(current_user: CurrentUserToken, tracking_input_id: str):
    """
    get tracking by ID
    """
    crud_trackings.check_id_equal(fake_trackings_db, tracking_input_id, current_user)
    tracking = crud_trackings.read_tracking(fake_trackings_db, tracking_input_id)
    return tracking

@router.put("/tracking", response_model=TrackingSchema)
def set_tracking_end(current_user: CurrentUserToken, tracking_input: TrackingStop):
    """
    put end time to specific tracking by ID
    """
    crud_trackings.check_id_equal(fake_trackings_db, tracking_input.id, current_user)
    tracking = crud_trackings.set_tracking_end(fake_trackings_db, tracking_input)
    return tracking

@router.delete("/tracking", status_code=status.HTTP_200_OK)
def delete_tracking(current_user: CurrentUserToken, tracking_id: str):
    """
    delete tracking by ID
    """
    crud_trackings.check_id_equal(fake_trackings_db, tracking_id, current_user)
    crud_trackings.delete_tracking(fake_trackings_db, tracking_id)
    return "tracking deleted"

@router.get("/tracking/details", response_model=TrackingOptionals)
def get_all_tracking_details(current_user: CurrentUserToken, tracking_id: str):
    """
    get all details of tracking with specific ID
    """
    check_equal = crud_trackings.check_id_equal(fake_trackings_db, tracking_id, current_user)
    tracking = crud_trackings.read_tracking(fake_trackings_db, tracking_id)
    return tracking
 
@router.put("/tracking/details", response_model=TrackingOptionals)
def put_tracking_detail(current_user: CurrentUserToken, tracking_input: TrackingOptionals):
    """
    put details to specific tracking by ID
    """
    crud_trackings.check_id_equal(fake_trackings_db, tracking_input.id, current_user)
    tracking = crud_trackings.put_tracking_detail(fake_trackings_db, tracking_input)
    return tracking

@router.get("/tracking_id/details_front", response_model=TrackingFrontRegions)
def get_front_regions(current_user: CurrentUserToken, tracking_id: str):
    """
    get front region details of tracking with specific ID
    """
    check_equal = crud_trackings.check_id_equal(fake_trackings_db, tracking_id, current_user)
    tracking = crud_trackings.read_tracking(fake_trackings_db, tracking_id)
    return tracking

@router.get("/tracking_id/details_back", response_model=TrackingBackRegions)
def get_back_regions(current_user: CurrentUserToken, tracking_id: str):
    """
    get back region details of tracking with specific ID
    """
    crud_trackings.check_id_equal(fake_trackings_db, tracking_id, current_user)
    tracking = crud_trackings.read_tracking(fake_trackings_db, tracking_id)
    return tracking

@router.get("/tracking_id/details_intensity", response_model=TrackingIntensity)
def get_intensity(current_user: CurrentUserToken, tracking_id: str):
    """
    get intensity details of tracking with specific ID
    """
    crud_trackings.check_id_equal(fake_trackings_db, tracking_id, current_user)
    tracking = crud_trackings.read_tracking(fake_trackings_db, tracking_id)
    return tracking

@router.get("/tracking_id/details_sleep", response_model=TrackingSleep)
def get_sleep(current_user: CurrentUserToken, tracking_id: str):
    """
    get sleep details of tracking with specific ID
    """
    crud_trackings.check_id_equal(fake_trackings_db, tracking_id, current_user)
    tracking = crud_trackings.read_tracking(fake_trackings_db, tracking_id)
    return tracking

@router.get("/tracking_id/details_diet", response_model=TrackingDiet)
def get_diet(current_user: CurrentUserToken, tracking_id: str):
    """
    get sleep details of tracking with specific ID
    """
    crud_trackings.check_id_equal(fake_trackings_db, tracking_id, current_user)
    tracking = crud_trackings.read_tracking(fake_trackings_db, tracking_id)
    return tracking