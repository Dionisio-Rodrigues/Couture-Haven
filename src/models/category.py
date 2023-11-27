from datetime import datetime

from src.app import db


class Category(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())

    __repr__ = lambda self: f"Category: '{self.name}'"
    to_dict = lambda self: {"id": self.id, "name": self.name}
    get_id = lambda self: self.id
    set_id = lambda self, new_id: setattr(self, "id", new_id)
    get_name = lambda self: self.name
    set_name = lambda self, new_name: setattr(self, "name", new_name)
    get_created_at = lambda self: self.created_at
    set_created_at = lambda self, new_created_at: setattr(self, "created_at", new_created_at)
