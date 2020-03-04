from config import Config
from flask import Flask, g
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_login import LoginManager
from flask_migrate import Migrate

# Globally accessible libraries
db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()

def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    # Initialize Plugins
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        # Include our Routes
        from .main import main_routes, models

        # Register Blueprints
        app.register_blueprint(main_routes.main_bp)
         # Initialize Global db
        db.create_all()

        return app