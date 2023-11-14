import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Logs(db.Model):
    __tablename__ = 'logs'
    id = db.Column(db.Integer, primary_key = True)
    message = db.Column(db.String(1000))
    data = db.Column(db.DateTime(default=datetime.datetime.utcnow))