from flask import request

from src.models.product import Product
from src.services.product import (
    get_all_products,
    get_products_by_id,
    save_product,
    delete_product,
)
from src.routes import product_blueprint
from src.utilities.flask import maybe_bind_id

# Validations
contains_name_response = lambda body: (
    None
    if "name" in body.keys()
    else ({"error": "Invalid payload", "message": "Please provide the required product fields."}, 400)
)

product_id_not_exists_response = lambda id: (
    ({"message": f"Product with ID '{id}' not found."}, 404)
    if not get_products_by_id(id=id)
    else None
)

# Index
index = lambda: (
    {
        "message": "Products found successfully.",
        "products": [result.to_dict() for result in get_all_products()]
    }, 200
)

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
        contains_name_response(body) or
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

product_blueprint.add_url_rule(rule="/", endpoint="index", view_func=index, methods=["GET"])
product_blueprint.add_url_rule(rule="/<int:id>", endpoint="view", view_func=view, methods=["GET"])
product_blueprint.add_url_rule(rule="/", endpoint="create", view_func=create, methods=["POST"])
product_blueprint.add_url_rule(rule="/<int:id>", endpoint="update", view_func=update, methods=["PUT", "PATCH"])
product_blueprint.add_url_rule(rule="/<int:id>", endpoint="destroy", view_func=destroy, methods=["DELETE"])
