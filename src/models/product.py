from datetime import datetime

from src.app import db
from src.utilities.general import format_currency


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"))
    created_at = db.Column(db.DateTime, default=datetime.now())
    category = db.relationship("Category", uselist=False, backref="product")

    __repr__ = lambda self: f"Product: '{self.name}' - R$ {format_currency(self.price)}"
    to_dict = lambda self: {"id": self.id, "name": self.name, "price": self.price, "category_id": self.category_id}
    get_id = lambda self: self.id
    set_id = lambda self, new_id: setattr(self, "id", new_id)
    get_name = lambda self: self.name
    set_name = lambda self, new_name: setattr(self, "name", new_name)
    get_price = lambda self: self.price
    set_price = lambda self, new_price: setattr(self, "price", new_price)
    get_category_id = lambda self: self.category_id
    set_category_id = lambda self, new_category_id: setattr(self, "category_id", new_category_id)
    get_created_at = lambda self: self.created_at
    set_created_at = lambda self, new_created_at: setattr(self, "created_at", new_created_at)
