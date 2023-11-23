from src.models.product import Product
from src.models.dao import BaseDAO

base_dao = BaseDAO(Product)

get_all_products = lambda: base_dao.get_all()
get_products_by_id = lambda id: base_dao.get_by(conditions={"id": id})
get_products_by_name = lambda name, exception_id=None: base_dao.get_by(
    conditions={"name": name},
    exception_id=exception_id,
)
get_products_by_category = lambda category_id, exception_id=None: base_dao.get_by(
    conditions={"category_id": category_id},
    exception_id=exception_id,
)
save_product = lambda product: (
    base_dao.save(instance=product) or product
    if not (
            base_dao.get_by(conditions={"name": product.name}, exception_id=product.id) and
            base_dao.get_by(conditions={"name": product.name}, exception_id=product.id).first()
    )
    else None
)
delete_product = lambda product: base_dao.delete(instance=product)
