from datetime import datetime

from src.app import db


class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(255))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    __repr__ = lambda self: f"Log: '{self.message}'"
    to_dict = lambda self: {"id": self.id, "message": self.message, "timestamp": self.timestamp}
    get_id = lambda self: self.id
    set_id = lambda self, new_id: setattr(self, "id", new_id)
    get_message = lambda self: self.message
    set_message = lambda self, new_message: setattr(self, "message", new_message)
    get_timestamp = lambda self: self.timestamp
    set_timestamp = lambda self, new_timestamp: setattr(self, "timestamp", new_timestamp)
