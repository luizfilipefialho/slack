# model.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class UserThread(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(80), unique=True, nullable=False)
    thread_id = db.Column(db.String(120), unique=False, nullable=False)

