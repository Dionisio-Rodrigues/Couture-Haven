from flask import Blueprint

category_blueprint = Blueprint(name="category", import_name=__name__)
product_blueprint = Blueprint(name="product", import_name=__name__)

from src.routes import category, product
