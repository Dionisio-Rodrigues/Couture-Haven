from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("config")

db = SQLAlchemy(app)

from src.routes import user_blueprint, auth_blueprint, category_blueprint, product_blueprint, log_blueprint

app.register_blueprint(blueprint=user_blueprint, url_prefix="/user")
app.register_blueprint(blueprint=auth_blueprint, url_prefix="/auth")
app.register_blueprint(blueprint=category_blueprint, url_prefix="/category")
app.register_blueprint(blueprint=product_blueprint, url_prefix="/product")
app.register_blueprint(blueprint=log_blueprint, url_prefix="/log")
