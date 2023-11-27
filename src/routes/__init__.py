from src.utilities.flask import create_blueprint

user_blueprint = create_blueprint(name="user")
auth_blueprint = create_blueprint(name="auth")
category_blueprint = create_blueprint(name="category")
product_blueprint = create_blueprint(name="product")
log_blueprint = create_blueprint(name="log")

from src.routes import user, auth, category, product, log
