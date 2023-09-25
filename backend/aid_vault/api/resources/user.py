from flask import request
from flask_restful import Resource

from aid_vault.extensions import db
from aid_vault.api.schemas.user import UserSchema
from aid_vault.models.user import User

class UserList(Resource):
    def get(self):
        schema = UserSchema(many=True)
        users = db.session.execute(db.select(User).order_by(User.name)).scalars()
        return schema.dump(users)

    def post(self):
        schema = UserSchema()
        user = schema.load(request.json)
        db.session.add(user)
        db.session.commit()
        return {"msg": "user created", "user": schema.dump(user)}

class UserResource(Resource):
    def put(self, id):
        schema = UserSchema()
        user_instance = db.get_or_404(User, id)
        user = schema.load(request.json, instance=user_instance)
        db.session.commit()
        return {"msg": "user updated", "user": schema.dump(user)}
    
    def get(self, id):
        schema = UserSchema()
        user = db.get_or_404(User, id)
        return schema.dump(user)
    
    def delete(self, id):
        user = db.get_or_404(User, id)
        db.session.delete(user)
        db.session.commit()
        return {"msg": f"user {id} deleted"}