from datetime import datetime

from flask import Blueprint, jsonify, render_template, request
from sqlalchemy import func
from . import db
from .models import User, MoodEntry

main_bp = Blueprint("main", __name__)


@main_bp.route("/health")
def health():
    return jsonify({"status": "ok", "message": "Employee Mood Thermometer backend running"})


@main_bp.route("/", methods=["GET", "POST"])
def mood():
    message = None

    if request.method == "POST":
        user_name = request.form.get("user_name")
        mood_value = request.form.get("mood_value")
        comment = request.form.get("comment")

        if user_name and mood_value:
            user = User.query.filter_by(name=user_name).first()
            if not user:
                user = User(
                    name=user_name,
                    email=f"{user_name}@example.com",
                    role="EMPLOYEE",
                )
                db.session.add(user)
                db.session.commit()

            entry = MoodEntry(
                mood_value=mood_value,
                comment=comment,
                user_id=user.id,
            )
            db.session.add(entry)
            db.session.commit()

            message = "Mood submitted successfully."
        else:
            message = "Please fill all required fields."

    return render_template("mood_form.html", message=message)


@main_bp.route("/dashboard")
def dashboard():
    # Read optional date filters from query string
    start_date_str = request.args.get("start_date")
    end_date_str = request.args.get("end_date")

    query_entries = db.session.query(MoodEntry, User).join(User)
    query_counts = db.session.query(MoodEntry.mood_value, func.count(MoodEntry.id))

    if start_date_str and end_date_str:
        start_dt = datetime.strptime(start_date_str, "%Y-%m-%d")
        end_dt = datetime.strptime(end_date_str, "%Y-%m-%d")
        end_dt = end_dt.replace(hour=23, minute=59, second=59)

        query_entries = query_entries.filter(
            MoodEntry.created_at.between(start_dt, end_dt)
        )
        query_counts = query_counts.filter(
            MoodEntry.created_at.between(start_dt, end_dt)
        )

    recent_entries = (
        query_entries.order_by(MoodEntry.created_at.desc()).limit(20).all()
    )

    mood_counts = query_counts.group_by(MoodEntry.mood_value).all()
    counts_dict = {mood: count for mood, count in mood_counts}

    return render_template(
        "dashboard.html",
        recent_entries=recent_entries,
        counts=counts_dict,
    )