from src.app import db
from src.models.log import Log


def get_all():
    return Log.query.all()


def get_by_id(id):
    return Log.query.filter_by(id=id).first()


def create(message):
    new_log = Log(message=message)

    db.session.add(new_log)
    db.session.commit()

    return new_log


def update(log, message):
    log.message = message

    db.session.add(log)
    db.session.commit()

    return log


def delete(log):
    db.session.delete(log)
    db.session.commit()
