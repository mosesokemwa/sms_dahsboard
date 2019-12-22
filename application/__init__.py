from flask import Flask, g
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
import config

# Globally accessible libraries
db = SQLAlchemy()


def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    # Initialize Plugins
    db.init_app(app)

    with app.app_context():
        # Include our Routes
        from .main import main_routes

        # Register Blueprints
        app.register_blueprint(main_routes.main_bp, url_prefix="/main")

        return app