from src.app import db


class Category(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"Category: {self.name}"

    def to_dict(self):
        return {"id": self.id, "name": self.name}
