import random
import uuid

from ..schemas import trackings as t

def generate_tracking(seed: int) -> t.TrackingComplete:
    random.seed(seed)
    time_start = random.randint(0, 2147483647)

    front_regions = []
    for i in range(19):
        front_regions.append(random.choice((True, False)))

    back_regions = []
    for i in range(18):
        back_regions.append(random.choice((True, False)))
    
    diet = {
        "Obst": None,
        "Gemüse": None,
        "Milchprodukte": None,
        "Fleisch": None,
        "Fisch": None,
        "Eier": None,
        "Weißmehl": None,
        "Vollkorn": None,
        "Soja": None
    }
    for food in diet:
        diet[food] = random.choice((True, False))

    tracking = t.TrackingComplete(
       id=uuid.UUID(int=random.getrandbits(128)),
       time_start=time_start,
       time_end=time_start + random.randint(1, 100000),
       front_regions=front_regions,
       back_regions=back_regions,
       intensity=random.randint(1, 10),
       diet=diet
    )
    return tracking