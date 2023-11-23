from datetime import datetime

from src.app import db


class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(255))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    __repr__ = lambda self: f"Log: '{self.message}'"
    to_dict = lambda self: {"id": self.id, "message": self.message, "timestamp": self.timestamp}
