from flask import request

from src.services.category import (
    get_all_categories,
    get_category_by_id,
    get_category_by_name,
    save_category,
    delete_category,
)
from src.models.category import Category
from src.routes import category_blueprint


@category_blueprint.route(rule="/", methods=["GET"])
def index():
    found_categories = [result.to_dict() for result in get_all_categories()]

    return {"message": "Categories found successfully.", "categories": found_categories}, 200


@category_blueprint.route(rule="/<id>", methods=["GET"])
def view(id):
    found_category = get_category_by_id(id=id)

    if not found_category:
        return {"message": f"Category with ID '{id}' not found."}, 404

    found_category = found_category.to_dict()

    return {"message": "Category found successfully.", "category": found_category}, 200


@category_blueprint.route(rule="/", methods=["POST"])
def create():
    body = request.get_json()

    if "name" not in body.keys():
        return {"error": "Invalid payload", "message": "Please provide the required category fields."}, 400

    name = body["name"]

    if get_category_by_name(name=name):
        return {"error": "Category already exists", "message": "A category with provided name already exists."}, 409

    new_category = save_category(category=Category(name=name)).to_dict()

    return {"message": "Category created successfully.", "category": new_category}, 201


@category_blueprint.route(rule="/<id>", methods=["PUT", "PATCH"])
def update(id):
    body = request.get_json()

    if "name" not in body.keys():
        return {"error": "Invalid payload", "message": "Please provide the required category fields."}, 400

    found_category = get_category_by_id(id=id)

    if not found_category:
        return {"message": f"Category with ID '{id}' not found."}, 404

    name = body["name"]

    if get_category_by_name(name=name, exception_id=id):
        return {"error": "Category already exists", "message": "A category with provided name already exists."}, 409

    found_category.name = name
    found_category = save_category(category=found_category).to_dict()

    return {"message": "Category updated successfully.", "category": found_category}, 200


@category_blueprint.route(rule="/<id>", methods=["DELETE"])
def destroy(id):
    found_category = get_category_by_id(id=id)

    if not found_category:
        return {"message": f"Category with ID '{id}' not found."}, 404

    delete_category(category=found_category)

    return {}, 204
