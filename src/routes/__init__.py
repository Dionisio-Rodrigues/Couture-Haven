from flask import Blueprint

create_blueprint = lambda name: Blueprint(name=name, import_name=__name__)

category_blueprint = create_blueprint(name="category")
product_blueprint = create_blueprint(name="product")
log_blueprint = create_blueprint(name="log")

from src.routes import category, product, log
