from uuid import uuid4, UUID

from aid_vault import schemas

# fake data for testing until the db-models are done
fake_users_db = [
    schemas.UserFakeDB(
        nickname="admin", 
        id = UUID("0841d75f675644b2b25f28e6c32a78e1"), # as fixed UUID, so it persists during reloads
        is_active=True,
        hashed_password="$2b$12$gDLA/AMJnXGYsyJxQLOVAe3IKBxLtV2Ipk072eI5Z//wVUBea.rvK"
    ),
    schemas.UserFakeDB(
        nickname="maxi1981", 
        full_name="Maxi Mustermensch", 
        age=42, 
        id=uuid4(),
        is_active=True,
        hashed_password="$2b$12$qys7cDcvmHoRxhy4PO53GOXUkKWypayaGtz3BLo1Hduy6MQ8cwod6"
    )
]