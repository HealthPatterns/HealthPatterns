from flask import Blueprint
from flask_restful import Api

from aid_vault.api.resources import user

blueprint = Blueprint("api", __name__, url_prefix="/api")
api = Api(blueprint)

api.add_resource(user.UserList, "/users")
api.add_resource(user.UserResource, "/users/<int:id>")