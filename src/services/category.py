from src.models.category import Category
from src.models.dao import BaseDAO

base_dao = BaseDAO(Category)

get_all_categories = lambda: base_dao.get_all()

get_category_by_id = lambda id: base_dao.get_by(filter={"id": id})

get_category_by_name = lambda name, exception_id=None: base_dao.get_by(filter={"name": name}, exception_id=exception_id)

save_category = lambda category: (
    base_dao.save(instance=category) or category
    if not (
            base_dao.get_by(filter={"name": category.name}, exception_id=category.id) and
            base_dao.get_by(filter={"name": category.name}, exception_id=category.id).first()
    )
    else None
)

delete_category = lambda category: base_dao.delete(instance=category)
