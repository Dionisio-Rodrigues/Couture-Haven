from src.app import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"))
    category = db.relationship("Category", uselist=False, backref="product")

    def to_dict(self):
        return {"id": self.id, "name":self.name, "price": self.price, "category_id": self.category_id}