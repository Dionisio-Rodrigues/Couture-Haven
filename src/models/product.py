from src.app import db
from src.utlities.general import format_currency


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"))
    category = db.relationship("Category", uselist=False, backref="product")

    __repr__ = lambda self: f"Product: '{self.name}' - R$ {format_currency(self.price)}"
    to_dict = lambda self: {"id": self.id, "name": self.name, "price": self.price, "category_id": self.category_id}
