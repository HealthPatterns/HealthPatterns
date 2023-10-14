from aid_vault import schemas

# fake data for testing until the db-models are done
fake_users_db = [
    schemas.UserFakeDB(
        nickname="admin", 
        id=1, 
        is_active=True,
        hashed_password="$2b$12$gDLA/AMJnXGYsyJxQLOVAe3IKBxLtV2Ipk072eI5Z//wVUBea.rvK"
    ),
    schemas.UserFakeDB(
        nickname="maxi1981", 
        full_name="Maxi Mustermensch", 
        age=42, 
        id=2, 
        is_active=True,
        hashed_password="$2b$12$qys7cDcvmHoRxhy4PO53GOXUkKWypayaGtz3BLo1Hduy6MQ8cwod6"
    )
]

user_id_increment = 2