import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key-change-in-prod")
    # SQLite DB stored in instance folder
    SQLALCHEMY_DATABASE_URI = (
        f"sqlite:///{BASE_DIR / 'instance' / 'mood.sqlite3'}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False