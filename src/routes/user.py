from flask import request
from werkzeug.security import generate_password_hash

from src.routes import user_blueprint
from src.models.user import User
from src.services.user import get_user_by_username, save_user

# Validations
contains_username_response = lambda body: (
    None
    if "username" in body.keys() and "password" in body.keys()
    else ({"error": "Invalid payload", "message": "Please provide the required user fields."}, 400)
)
username_exists_response = lambda username: (
    ({"error": "User already exists", "message": "A user with provided username already exists."}, 409)
    if get_user_by_username(username=username)
    else None
)

# Create
create_response = lambda body: (
        contains_username_response(body) or
        username_exists_response(body["username"]) or
        (
            {
                "message": "User created successfully.",
                "category": save_user(user=User(
                    username=body["username"],
                    password=generate_password_hash(body["password"]),
                )).to_dict()
            }, 201
        )
)
create = lambda: create_response(request.get_json())

user_blueprint.add_url_rule(rule="/", endpoint="create", view_func=create, methods=["POST"])
