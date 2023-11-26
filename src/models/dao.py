from src.app import db
from src.models.log import Log
from src.utilities.database import format_conditions


class BaseDAO:
    def __init__(self, model):
        self.db = db
        self.model = model
        self.record_log = lambda message: db.session.add(Log(message=message)) or db.session.commit()
        self.get_all = lambda: (self.model.query.all(), self.record_log(f"GET ALL {self.model.__tablename__}"))[0]
        self.get_by = lambda conditions, exception_id=None: (
            (
                self.model.query.filter_by(**conditions).first()
                if not exception_id
                else self.model.query.filter(self.model.id != exception_id).filter_by(**conditions).first()
            ),
            self.record_log(f"FILTER BY {format_conditions(conditions)} FROM {self.model.__tablename__}")
        )[0]
        self.save = lambda instance: (
            self.db.session.add(instance),
            self.record_log(f"SAVE {instance} INTO {self.model.__tablename__}")
        )[0]
        self.delete = lambda instance: (
            self.model.query.filter_by(id=instance.id).delete(),
            self.record_log(f"DELETE {instance} FROM {self.model.__tablename__}")
        )[0]
