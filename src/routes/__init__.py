from src.utilities.flask import create_blueprint

category_blueprint = create_blueprint(name="category")
product_blueprint = create_blueprint(name="product")
log_blueprint = create_blueprint(name="log")

from src.routes import category, product, log
