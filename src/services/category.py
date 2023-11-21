from src.app import db
from src.models.category import Category
from src.models.dao import BaseDAO

base_dao = BaseDAO(Category)

get_all_categories = lambda: base_dao.get_all()

get_category_by_id = lambda id: base_dao.get_by({"id": id}).first()

get_category_by_name = lambda name, exception_id=None: base_dao.get_by({"name": name}, exception_id)

save_category = lambda category: base_dao.save(category) or category if not (base_dao.get_by({"name": category.name}, exception_id=category.id) and base_dao.get_by({"name": category.name}, exception_id=category.id).first()) else None

delete_category = lambda category: base_dao.delete(category)

