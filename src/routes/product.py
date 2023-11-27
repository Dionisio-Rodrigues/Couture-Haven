from flask import request

from src.models.product import Product
from src.services.product import (
    get_all_products,
    get_products_by_id,
    get_products_by_name,
    save_product,
    delete_product,
)
from src.services.category import get_category_by_id
from src.routes import product_blueprint
from src.utilities.general import models_to_dict
from src.utilities.flask import maybe_bind_id
from src.utilities.auth import token_required

# Validations
contains_valid_fields_response = lambda body: (
    None
    if "name" in body.keys() and "price" in body.keys() and "category_id" in body.keys()
    else ({"error": "Invalid payload", "message": "Please provide the required product fields."}, 400)
)
contains_one_valid_field_response = lambda body: (
    None
    if "name" in body.keys() or "price" in body.keys() or "category_id" in body.keys()
    else ({"error": "Invalid payload", "message": "Please provide at least one required product field."}, 400)
)
name_exists_response = lambda name, exception_id=None: (
    ({"error": "Product already exists", "message": "A product with provided name already exists."}, 409)
    if get_products_by_name(name=name, exception_id=exception_id)
    else None
)
category_id_not_exists = lambda id: (
    None
    if get_category_by_id(id=id)
    else ({"error": "Category does not exists", "message": f"Category with ID '{id} not found.'"}, 404)
)

product_id_not_exists_response = lambda id: (
    ({"message": f"Product with ID '{id}' not found."}, 404)
    if not get_products_by_id(id=id)
    else None
)

# Index
index = lambda: ({"message": "Products found successfully.", "products": models_to_dict(get_all_products())}, 200)

# View
view_response = lambda id, product: (
    ({"message": "Product found successfully.", "product": product.to_dict()}, 200)
    if product
    else ({"message": f"Product with ID '{id}' not found."}, 404)
)
view_flow = lambda id: view_response(id, get_products_by_id(id=id))
view = lambda id: maybe_bind_id(id, view_flow)

# Create
create_response = lambda body: (
        contains_valid_fields_response(body) or
        name_exists_response(body["name"]) or
        category_id_not_exists(body["category_id"]) or
        (
            {
                "message": "Product created successfully.",
                "product": save_product(
                    Product(
                        name=body["name"],
                        price=body["price"],
                        category_id=body["category_id"]
                    )
                ).to_dict()
            }, 201
        )
)
create = lambda: create_response(request.get_json())

# Update
update_response = lambda id, body, product: (
        product_id_not_exists_response(id) or
        contains_one_valid_field_response(body) or
        name_exists_response(body.get("name") or product.name, id) or
        category_id_not_exists(body.get("category_id") or product.category_id) or
        product.set_name(body.get("name") or product.name) or
        product.set_price(body.get("price") or product.price) or
        product.set_category_id(body.get("category_id") or product.category_id) or
        ({"message": "Product updated successfully.", "product": save_product(product).to_dict()}, 200)
)
update_flow = lambda id: update_response(id, request.get_json(), get_products_by_id(id=id))
update = lambda id: maybe_bind_id(id, update_flow)

# Destroy
destroy_response = lambda id: (
        product_id_not_exists_response(id) or
        (delete_product(product=get_products_by_id(id=id)), ({}, 204))[1]
)
destroy = lambda id: maybe_bind_id(id, destroy_response)

product_blueprint.add_url_rule(
    rule="/",
    endpoint="index",
    view_func=token_required(index),
    methods=["GET"],
)
product_blueprint.add_url_rule(
    rule="/<int:id>",
    endpoint="view",
    view_func=token_required(view),
    methods=["GET"],
)
product_blueprint.add_url_rule(
    rule="/",
    endpoint="create",
    view_func=token_required(create),
    methods=["POST"],
)
product_blueprint.add_url_rule(
    rule="/<int:id>",
    endpoint="update",
    view_func=token_required(update),
    methods=["PUT", "PATCH"],
)
product_blueprint.add_url_rule(
    rule="/<int:id>",
    endpoint="destroy",
    view_func=token_required(destroy),
    methods=["DELETE"],
)
