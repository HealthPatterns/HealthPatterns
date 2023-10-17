from ..schemas.trackings import TrackingComplete
from sqlalchemy import Boolean


# fake details db for testing purposes

fake_trackings_db = [
        TrackingComplete(id="1", user_id=2, start_time=1697115011, region="head", intensity="5", sleep="7", diet="omnivore"),
        TrackingComplete(id="2", user_id=1, start_time=1697115011, end_time=1697115015, is_active=False, region="stomach", intensity="9", sleep="3", diet="burgers, pizza"),
        TrackingComplete(id="3", user_id=1, start_time=1697115011, region="foot", intensity="3", sleep="8", diet="vegan"),
        TrackingComplete(id="4", user_id=1, start_time=1697115011),
        TrackingComplete(id="5",
                         user_id=1,
                         start_time=1697115011, 
                         front_regions=[True, True, False, True, False, False],
                         back_regions=[False, True], 
                         intensity=5, 
                         sleep="8", 
                         diet="omnivore"),
        TrackingComplete(id="6",
                         user_id=1,
                         start_time=1697115011,
                         end_time=1697115045,
                         front_regions=[True, True, False, True, False, False],
                         back_regions=[False, True], 
                         intensity=5, 
                         sleep="8", 
                         diet="omnivore")
    ]