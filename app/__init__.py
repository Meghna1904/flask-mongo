from flask import Flask
from app.config import Config
from app.routes.user_routes import user_bp

def create_app():
    app= Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(user_bp)
    return app