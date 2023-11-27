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
from src.utilities.flask import maybe_bind_id
from src.utilities.auth import token_required

# Validations
field_validation_response = lambda body: (
    None
    if "name" in body.keys()
    else ({"error": "Invalid payload", "message": "Please provide the required category fields."}, 400)
)
name_exists_response = lambda name, exception_id=None: (
    ({"error": "Category already exists", "message": "A category with provided name already exists."}, 409)
    if get_category_by_name(name=name, exception_id=exception_id)
    else None
)
id_not_exists_response = lambda id: (
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
view_flow = lambda id: view_response(id, get_category_by_id(id=id))
view = lambda id: maybe_bind_id(id, view_flow)

# Create
create_response = lambda body: (
        field_validation_response(body) or
        name_exists_response(body["name"]) or
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
        field_validation_response(body) or
        id_not_exists_response(id) or
        name_exists_response(body["name"], id) or
        category.set_name(body["name"]) or
        (
            {
                "message": "Category updated successfully.",
                "category": save_category(category).to_dict()
            }, 200
        )
)
update_flow = lambda id: update_response(id, request.get_json(), get_category_by_id(id=id))
update = lambda id: maybe_bind_id(id, update_flow)

# Destroy
destroy_response = lambda id: (
        id_not_exists_response(id) or
        (delete_category(category=get_category_by_id(id=id)), ({}, 204))[1]
)
destroy = lambda id: maybe_bind_id(id, destroy_response)

category_blueprint.add_url_rule(
    rule="/",
    endpoint="index",
    view_func=token_required(index),
    methods=["GET"],
)
category_blueprint.add_url_rule(
    rule="/<int:id>",
    endpoint="view",
    view_func=token_required(view),
    methods=["GET"],
)
category_blueprint.add_url_rule(
    rule="/",
    endpoint="create",
    view_func=token_required(create),
    methods=["POST"],
)
category_blueprint.add_url_rule(
    rule="/<int:id>",
    endpoint="update",
    view_func=token_required(update),
    methods=["PUT", "PATCH"],
)
category_blueprint.add_url_rule(
    rule="/<int:id>",
    endpoint="destroy",
    view_func=token_required(destroy),
    methods=["DELETE"],
)
