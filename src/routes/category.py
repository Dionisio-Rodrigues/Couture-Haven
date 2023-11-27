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
from src.utilities.general import models_to_dict

# Validations
contains_name_response = lambda body: (
    None
    if "name" in body.keys()
    else ({"error": "Invalid payload", "message": "Please provide the required category fields."}, 400)
)
category_name_exists_response = lambda name, exception_id=None: (
    ({"error": "Category already exists", "message": "A category with provided name already exists."}, 409)
    if get_category_by_name(name=name, exception_id=exception_id)
    else None
)
category_id_not_exists_response = lambda id: (
    ({"message": f"Category with ID '{id}' not found."}, 404)
    if not get_category_by_id(id=id)
    else None
)

# Index
index = lambda: ({"message": "Categories found successfully.", "categories": models_to_dict(get_all_categories())}, 200)

# View
view_response = lambda id, category: (
    ({"message": "Category found successfully.", "category": category.to_dict()}, 200)
    if category
    else ({"message": f"Category with ID '{id}' not found."}, 404)
)
view = lambda id: view_response(id, get_category_by_id(id=id))

# Create
create_response = lambda body: (
        contains_name_response(body) or
        category_name_exists_response(body["name"]) or
        (
            {
                "message": "Category created successfully.",
                "category": save_category(category=Category(name=body["name"])).to_dict()
            }, 201
        )
)
create = lambda: create_response(request.get_json())

# Update
update_response = lambda id, body, category: (
        contains_name_response(body) or
        category_id_not_exists_response(id) or
        category_name_exists_response(body["name"], id) or
        category.set_name(body["name"]) or
        (
            {
                "message": "Category updated successfully.",
                "category": save_category(category).to_dict()
            }, 200
        )
)
update = lambda id: update_response(id, request.get_json(), get_category_by_id(id=id))

# Destroy
destroy_response = lambda id, category: (
        category_id_not_exists_response(id) or
        (delete_category(category=category), ({}, 204))[1]
)
destroy = lambda id: destroy_response(id, get_category_by_id(id=id))

category_blueprint.add_url_rule(rule="/", endpoint="index", view_func=index, methods=["GET"])
category_blueprint.add_url_rule(rule="/<int:id>", endpoint="view", view_func=view, methods=["GET"])
category_blueprint.add_url_rule(rule="/", endpoint="create", view_func=create, methods=["POST"])
category_blueprint.add_url_rule(rule="/<id>", endpoint="update", view_func=update, methods=["PUT", "PATCH"])
category_blueprint.add_url_rule(rule="/<id>", endpoint="destroy", view_func=destroy, methods=["DELETE"])
