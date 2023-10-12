from fastapi import APIRouter, HTTPException, status, Response
from fastapi.encoders import jsonable_encoder


from sqlalchemy import insert, select
from ...models.example import *
from ...common import crud_example
from ...db.database import SessionInstance

# declare router with default values
router = APIRouter(
    prefix="/test",
    tags=["test"] # -> makes endpoints show up in its own category in the documentation
)

@router.get("/")
def test(db: SessionInstance):
    #insert(Users).values(id=1, name='Finn', email='test@gmail.com', is_active=True)

    #for row in result:
    #    print(f"{row.name}  {row.email}")

    #user = Users(201, "Test", "tessdt@gmail.com", True)
    tracking = Trackings(1, 1, 20, 30)
    db.add(tracking)
    db.commit()

    result = db.query(Trackings).all()
    for row in result:
        print(jsonable_encoder(row))
    