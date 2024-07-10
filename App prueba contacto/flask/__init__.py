from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object('app.config.Config')

    db.init_app(app)
    migrate = Migrate(app, db)

    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
