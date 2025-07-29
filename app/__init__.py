from flask import Flask
from flask_cors import CORS
from .extensions import db, bcrypt, jwt
from .routes import main
from .auth import auth

def create_app():
    app = Flask(__name__)

    # 🔐 Configurations
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/taskvault'
    app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'

    # 🌐 Enable CORS for frontend (React on Vite dev server)
    CORS(app, origins=["http://localhost:5173"])

    # 🔧 Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    # 🔗 Register blueprints (routes)
    app.register_blueprint(main)
    app.register_blueprint(auth)

    # 🛠️ Create DB tables
    with app.app_context():
        db.create_all()

    return app
