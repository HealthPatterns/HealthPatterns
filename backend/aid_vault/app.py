from flask import Flask

from aid_vault.api.views import blueprint
from aid_vault.extensions import db, ma, migrate

def create_app():

    # init app
    app = Flask(__name__)

    # db config
    username = "name"
    password = "password"
    hostname = "aid-db"
    port = "5432"
    database_name = "aid-db"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{username}:{password}@{hostname}:{port}/{database_name}"

    configure_extensions(app)
    register_blueprints(app)

    return app

def configure_extensions(app):
    db.init_app(app)
    # with app.app_context():
    #     db.create_all()
    migrate.init_app(app, db)
    ma.init_app(app)

def register_blueprints(app):
    app.register_blueprint(blueprint)

app = create_app()



