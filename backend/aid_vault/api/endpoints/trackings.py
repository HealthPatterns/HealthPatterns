from fastapi import APIRouter, HTTPException, status, Response

from ...schemas.trackings import TrackingBase, TrackingOptionals, TrackingSchema, TrackingStart, TrackingStop, TrackingComplete
from ...common import crud_trackings

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
db = [
        TrackingComplete(id="1", start_time=1697115011, is_active=True, region="head", intensity="5", sleep="7", diet="omnivore"),
        TrackingComplete(id="2", start_time=1697115011, end_time=1697115015, is_active=False, region="stomach", intensity="9", sleep="3", diet="burgers, pizza"),
        TrackingComplete(id="3", start_time=1697115011, is_active=True, region="foot", intensity="3", sleep="8", diet="vegan"),
        TrackingComplete(id="4", start_time=1697115011, is_active=True)
    ]

#get all db
@router.get("", response_model=list[TrackingComplete])
def get_all_trackings():#skip: int = 0, limit: int = 10):
    all_trackings = crud_trackings.read_trackings(db)
    return all_trackings

# create new tracking and post time
@router.post("", response_model=TrackingSchema, status_code=status.HTTP_201_CREATED)
def start_tracking(s_time: int):
    new_tracking = crud_trackings.start_tracking(db, s_time)
    return new_tracking

#get active db, 
@router.get("/active", response_model=list[TrackingSchema])
def get_active_trackings():#skip: int = 0, limit: int = 10):
    active_trackings = crud_trackings.read_active_tracking(db)
    return active_trackings

# get tracking by ID
@router.get("/{tracking_id}", response_model=TrackingSchema)
def get_tracking(tracking_id: str):
    tracking = crud_trackings.read_tracking(db, tracking_id)
    if not tracking:
        raise HTTPException(status_code=404, detail="Resource not found")
    return tracking

# put end time to specific tracking by ID
@router.put("/{tracking_id}", response_model=TrackingSchema)
def set_tracking_end(tracking_id: str, time: int):
    tracking = crud_trackings.set_tracking_end(db, tracking_id, time)
    if not tracking:
        raise HTTPException(status_code=404, detail="Resource not found")
    return tracking

# delete tracking by ID
@router.delete("/{tracking_id}", status_code=status.HTTP_200_OK)
def delete_tracking(tracking_id: str):
    crud_trackings.delete_tracking(db, tracking_id)
    #if not mock_tracking:
    #    raise HTTPException(status_code=404, detail="Resource not found")
    #else: db.remove(mock_tracking)
    return "tracking deleted"

# get all details of tracking with specific ID
@router.get("/{tracking_id}/details", response_model=TrackingOptionals)
def get_all_tracking_details(tracking_id: str):
    tracking = crud_trackings.read_tracking(db, tracking_id)
    if not tracking:
        raise HTTPException(status_code=404, detail="Resource not found")
    return tracking

# put details to specific tracking by ID    
@router.put("/{tracking_id}/details", response_model=TrackingOptionals)
def put_tracking_detail(tracking_id: str, attribute: str, value: str ):
    tracking = crud_trackings.put_tracking_detail(db, tracking_id, attribute, value)
    if not tracking:
        raise HTTPException(status_code=404, detail="Resource not found")
    return tracking

# get specific detail of tracking with specific ID
@router.get("/{tracking_id}/details/{attribute}", response_model=TrackingOptionals)
def get_specific_tracking_details(tracking_id: str, attribute: str):
    tracking = crud_trackings.get_specific_tracking_details(db, tracking_id, attribute)
    if not tracking:
        raise HTTPException(status_code=404, detail="Resource not found")
    return tracking