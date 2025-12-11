from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from pathlib import Path
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    # Load config
    app.config.from_object(Config)

    # Ensure instance folder exists
    Path(app.instance_path).mkdir(parents=True, exist_ok=True)

    # Init DB
    db.init_app(app)

    # Register blueprints / routes
    from .routes import main_bp
    app.register_blueprint(main_bp)

    # Create tables on first run
    with app.app_context():
        from . import models  # noqa: F401
        db.create_all()

    return app