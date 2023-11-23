from src.models.log import Log
from src.models.dao import BaseDAO

base_dao = BaseDAO(Log)

get_all_logs = lambda: base_dao.get_all()
get_log_by_id = lambda id: base_dao.get_by(conditions={"id": id})
save_log = lambda log: base_dao.save(instance=log) or log
delete_log = lambda log: base_dao.delete(instance=log)
