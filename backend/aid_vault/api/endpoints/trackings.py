from fastapi import APIRouter, HTTPException, status, Response

from ...schemas.trackings import TrackingBase, TrackingOptionals, TrackingSchema, TrackingStart, TrackingStop
from ...crud import users

import uuid

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
trackings = [
        TrackingSchema(id="1", start_time=1697115011, is_active=True),
        TrackingSchema(id="2", start_time=1697115011, end_time=1697115015, is_active=False),
        TrackingSchema(id="3", start_time=1697115011, is_active=True),
        TrackingSchema(id="4", start_time=1697115011, is_active=True)
    ]
tracking_details = [
    TrackingOptionals(id="1", region="head", intensity="5", sleep="7", diet="omnivore"),
    TrackingOptionals(id="2", region="stomach", intensity="9", sleep="3", diet="burgers, pizza"),
    TrackingOptionals(id="3", region="foot", intensity="3", sleep="8", diet="vegan"),
    TrackingOptionals(id="4")
]

#get all trackings
@router.get("", response_model=list[TrackingSchema])
def get_all_trackings():#skip: int = 0, limit: int = 10):
    #all_trackings = crud_trackings.read_trackings(db, skip, limit)
    return trackings

# create new tracking and post time
@router.post("", response_model=TrackingSchema, status_code=status.HTTP_201_CREATED)
def start_tracking(s_time: int):
    new_uuid=uuid.uuid4()
    new_tracking = TrackingSchema(id=str(new_uuid), start_time=s_time, is_active=True)
    trackings.append(new_tracking)
    return new_tracking

#get active trackings, 
@router.get("/active", response_model=list[TrackingSchema])
def get_active_trackings():#skip: int = 0, limit: int = 10):
    #active_trackings = crud_trackings.read_trackings(db, skip, limit)
    active_trackings = [tracking for tracking in trackings if tracking.is_active]
    return active_trackings

# get tracking by ID
@router.get("/{tracking_id}", response_model=TrackingSchema)
def get_tracking(tracking_id: str):
    mock_tracking = next((tracking for tracking in trackings if tracking.id == tracking_id), None)
    if not mock_tracking:
        raise HTTPException(status_code=404, detail="Resource not found")
    
    #crud_trackings.read_trackings(db, tracking_id)
    return mock_tracking

# put end time to specific tracking by ID
@router.put("/{tracking_id}", response_model=TrackingSchema)
def set_tracking_end(tracking_id: str, time: str):
    mock_tracking = next((tracking for tracking in trackings if tracking.id == tracking_id), None)
    if not mock_tracking:
        raise HTTPException(status_code=404, detail="Resource not found")
    mock_tracking.end_time = time
    mock_tracking.is_active = False
    return mock_tracking

# delete tracking by ID
@router.delete("/{tracking_id}", status_code=status.HTTP_200_OK)
def delete_tracking(tracking_id: str):
    mock_tracking = next((tracking for tracking in trackings if tracking.id == tracking_id), None)
    if not mock_tracking:
        raise HTTPException(status_code=404, detail="Resource not found")
    else: trackings.remove(mock_tracking)
    return "tracking deleted"

# get all details of tracking with specific ID
@router.get("/{tracking_id}/details", response_model=TrackingOptionals)
def get_all_tracking_details(tracking_id: str):
    mock_tracking = next((tracking for tracking in tracking_details if tracking.id == tracking_id), None)
    if not mock_tracking:
        raise HTTPException(status_code=404, detail="Resource not found")
    return mock_tracking

# put details to specific tracking by ID    
@router.put("/{tracking_id}/details", response_model=TrackingOptionals)
def put_tracking_detail(tracking_id: str, attribute: str, value: str ):
    mock_tracking = next((tracking for tracking in tracking_details if tracking.id == tracking_id), None)
    if not mock_tracking:
        raise HTTPException(status_code=404, detail="Resource not found")
    match attribute:
        case "region":
            mock_tracking.region=value
        case "intensity":
            mock_tracking.intensity=value
        case "sleep":
            mock_tracking.sleep=value
        case "diet":
            mock_tracking.diet=value
    return mock_tracking

# get specific detail of tracking with specific ID
@router.get("/{tracking_id}/details/{attribute}", response_model=TrackingOptionals)
def get_specific_tracking_details(tracking_id: str, attribute: str):
    mock_track = next((tracking for tracking in tracking_details if tracking.id == tracking_id), None)
    if not mock_track:
        raise HTTPException(status_code=404, detail="Resource not found")
    match attribute:
        case "region":
            mock_tracking = TrackingOptionals(id=tracking_id, region=mock_track.region)
        case "intensity":
            mock_tracking = TrackingOptionals(id=tracking_id, intensity=mock_track.intensity)
        case "sleep":
            mock_tracking = TrackingOptionals(id=tracking_id, sleep=mock_track.sleep)
        case "diet":
            mock_tracking = TrackingOptionals(id=tracking_id, diet=mock_track.diet)
    return mock_tracking