from datetime import datetime

from src.app import db


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())

    __repr__ = lambda self: f"User: '{self.username}'"
    to_dict = lambda self: {"id": self.id, "username": self.username}
    get_id = lambda self: self.id
    set_id = lambda self, new_id: setattr(self, "id", new_id)
    get_username = lambda self: self.username
    set_username = lambda self, new_username: setattr(self, "username", new_username)
    get_password = lambda self: self.password
    set_password = lambda self, new_password: setattr(self, "password", new_password)
    get_created_at = lambda self: self.created_at
    set_created_at = lambda self, new_created_at: setattr(self, "created_at", new_created_at)
