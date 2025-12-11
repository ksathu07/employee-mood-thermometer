from datetime import datetime
from . import db

class Team(db.Model):
    __tablename__ = "teams"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    manager_name = db.Column(db.String(100))

    users = db.relationship("User", back_populates="team")

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    role = db.Column(db.String(50), nullable=False, default="EMPLOYEE")

    team_id = db.Column(db.Integer, db.ForeignKey("teams.id"))
    team = db.relationship("Team", back_populates="users")

    mood_entries = db.relationship("MoodEntry", back_populates="user")

class MoodEntry(db.Model):
    __tablename__ = "mood_entries"

    id = db.Column(db.Integer, primary_key=True)
    mood_value = db.Column(db.String(20), nullable=False)
    comment = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    user = db.relationship("User", back_populates="mood_entries")