from aid_vault.models.user import User
from aid_vault.extensions import ma, db

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        sqla_session = db.session
        dump_only = ("id",)