from app import db
from models.log import Log

get_all = lambda model: (model.query.all(), db.session.add(Log(message=f'get all {model.__tablename__}')) or db.session.commit())[0]
get_by = lambda model, filter: (model.query.filter_by(**filter), db.session.add(Log(message=f'get id {id} from {model.__tablename__}')) or db.session.commit())[0]
save = lambda instance: (db.session.add(instance), db.session.add(Log(message=f'save {instance} from {instance.__tablename__}')), db.session.commit())[0]
delete = lambda instance: (db.session.delete(instance) , db.session.add(Log(message=f'delete {instance} from {instance.__tablename__}')), db.session.commit())[0]
