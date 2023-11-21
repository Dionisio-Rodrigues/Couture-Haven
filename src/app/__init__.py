from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///dev.db"

db = SQLAlchemy(app)

from src.routes import category_blueprint, product_blueprint, log_blueprint

app.register_blueprint(blueprint=category_blueprint, url_prefix="/category")
app.register_blueprint(blueprint=product_blueprint, url_prefix="/product")
app.register_blueprint(blueprint=log_blueprint, url_prefix="/log")
