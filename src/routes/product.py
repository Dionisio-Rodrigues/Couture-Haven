import re
from flask import request

from src.models.product import Product
from src.services.product import (
    get_all_products,
    get_products_by_id,
    save_product,
    delete_product,
)
from src.routes import product_blueprint

cache = dict()


is_valid = lambda body, obj_class : all([field in vars(obj_class).keys() for field in body.keys()])

read_bind = lambda id: get_products_by_id(id) if re.match(r"^[1-9][0-9]*$", id) else print('error') or None
read = lambda id: read_bind(id)

index = lambda : ({"message": "Products found successfully.", "products": [result.to_dict() for result in get_all_products()]}, 200)
product_blueprint.add_url_rule(rule="/", endpoint="list_product", view_func=index, methods=["GET"])

view = lambda id: ({"message": "Product found successfully.", "product": read(id).to_dict()}, 200) if read(id) is not None else ({"message": f"Product with ID '{id}' not found."}, 404)
product_blueprint.add_url_rule(rule="/<id>", endpoint="retrieve_product", view_func=view, methods=["GET"])

create_bind = lambda body: cache.update({"new_product":save_product(Product(**body))}) if is_valid(body, Product) and body.get("name") != None else None
create = lambda : ({"message": "Product created successfully.", "product": cache.pop("new_product").to_dict()}, 201) if create_bind(request.get_json()) or cache.get("new_product", None) else ({"error": "Invalid payload"}, 400)
product_blueprint.add_url_rule(rule="/", endpoint="create", view_func=create, methods=["POST"])

update_bind = lambda id, body: cache.update({'product':read(id)}) or [setattr(cache.get('product'), key, value) for key, value in body.items()] and cache.update({"updated_product":save_product(cache.pop("product"))}) if is_valid(body, Product) else None
update = lambda id :  ({"message": "Product updated successfully.", "product": cache.pop('updated_product').to_dict()}, 200) if read(id) is not None and (update_bind(id=id, body=request.get_json()) or cache.get("updated_product", None)) else ({"message": f"Product with ID '{id}' not found."}, 404)
product_blueprint.add_url_rule(rule="/<id>", endpoint="update_product", view_func=update, methods=["PUT", "PATCH"])

destroy = lambda id: delete_product(product=read(id)) or ({}, 200) if read(id) is not None else {"message": f"Product with ID '{id}' not found."}, 404
product_blueprint.add_url_rule(rule="/<id>", endpoint="delete_product", view_func=destroy, methods=["DELETE"])
