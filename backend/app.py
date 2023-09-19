from flask import Flask, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

# init app
app = Flask(__name__)


# init db
username = "name"
password = "password"
hostname = "aid-db"
port = "5432"
database_name = "aid-db"
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{username}:{password}@{hostname}:{port}/{database_name}"
db = SQLAlchemy(app)

# db model
class User(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False)

with app.app_context():
    db.create_all()

# init api
api = Api(app)

# api resources
class ListUsers(Resource):
    def get(self):
        users = db.session.execute(db.select(User).order_by(User.name)).scalars()
        return users

class CreateUser(Resource):
    def post(self):
        user = User(name=request.form["name"])
        db.session.add(user)
        db.session.commit()
        return "", 201

class ModifyUser(Resource):
    def put(self, id):
        user = User(id=id, name=request.form["name"])
        db.session.add(user)
        db.session.commit()
        return "", 201
    
    def get(self, id):
        user = db.get_or_404(User, id)
        return user
    
    def delete(self, id):
        db.session.delete(User, id)
        db.session.commit()
        return "", 204
    
# api routes
api.add_resource(ListUsers, "/users")
api.add_resource(CreateUser, "/users/create")
api.add_resource(ModifyUser, "/users/<int:id>")

# run app
if __name__ == "__main__":
    app.run(debug=True)

