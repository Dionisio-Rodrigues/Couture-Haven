from src.app import db


class Category(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)

    __repr__ = lambda self: f"Category: '{self.name}'"
    to_dict = lambda self: {"id": self.id, "name": self.name}
