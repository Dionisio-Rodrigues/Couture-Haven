from src.app import db
from src.models.log import Log


class BaseDAO():
    def __init__(self, model):
        self.db = db
        self.model = model
        self.record_log = lambda message: db.session.add(Log(message=message)) or db.session.commit()
        self.get_all = lambda: (self.model.query.all(), self.record_log(f'get all {self.model.__tablename__}'))[0]
        self.get_by = lambda filter, exception_id=None: (self.model.query.filter_by(**filter).first() if not exception_id else self.model.query.filter(self.model.id != exception_id).filter_by(**filter).first(), self.record_log(f'filter by {filter.keys()} from {self.model.__tablename__}'))[0]
        self.save = lambda instance: (self.db.session.add(instance), self.record_log(f'save {instance} from {self.model.__tablename__}'))[0]
        self.delete = lambda instance: (self.db.session.delete(instance) , self.record_log(f'delete {instance} from {self.model.__tablename__}'))[0]
