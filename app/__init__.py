from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///taskvault.db"
    app.config["JWT_SECRET_KEY"] = "super-secret"
    db.init_app(app)
    jwt.init_app(app)

    from .routes import main
    app.register_blueprint(main)

    return app
