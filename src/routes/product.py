from flask import request

from src.models.product import Product
from src.services.product import (
    get_all_products,
    get_products_by_id,
    save_product,
    delete_product,
)
from src.routes import product_blueprint


@product_blueprint.route(rule="/", methods=["GET"])
def index():
    found_products = [result.to_dict() for result in get_all_products()]

    return {"message": "Products found successfully.", "products": found_products}, 200


@product_blueprint.route(rule="/<id>", methods=["GET"])
def view(id):
    found_product = get_products_by_id(id=id)

    if not found_product:
        return {"message": f"Product with ID '{id}' not found."}, 404

    found_product = found_product.to_dict()

    return {"message": "Product found successfully.", "product": found_product}, 200


@product_blueprint.route(rule="/", methods=["POST"])
def create():
    body = request.get_json()

    if "name" not in body.keys():
        return {"error": "Invalid payload", "message": "Please provide the required product fields."}, 400

    try:
        new_product = save_product(Product(**body))
    except Exception as e:
        return {"message": str(e)}, 400

    return {"message": "Product created successfully.", "product": new_product.to_dict()}, 201


@product_blueprint.route(rule="/<id>", methods=["PUT", "PATCH"])
def update(id):
    body = request.get_json()

    found_product = get_products_by_id(id=id)

    if not found_product:
        return {"message": f"Product with ID '{id}' not found."}, 404

    [setattr(found_product, key, value) for key, value in body.items() if key != "id"]

    found_product = save_product(found_product)

    if not found_product:
        return {"message": 'It was not possible to save because the name already existed.'}, 400

    return {"message": "Product updated successfully.", "product": found_product.to_dict()}, 200


@product_blueprint.route(rule="/<id>", methods=["DELETE"])
def destroy(id):
    found_product = get_products_by_id(id=id)

    if not found_product:
        return {"message": f"Product with ID '{id}' not found."}, 404

    delete_product(product=found_product)

    return {}, 204
