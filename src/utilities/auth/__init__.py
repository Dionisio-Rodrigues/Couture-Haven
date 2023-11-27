import jwt
from flask import request
from datetime import datetime, timedelta
from werkzeug.security import check_password_hash

from config import SECRET_KEY
from src.services.user import get_user_by_username

unauthorized_response = lambda: (
    {"message": "Could not verify.", "WWW-Authenticate": "Basic auth='Login required'"}, 401
)
verify_auth = lambda authorization: (
    None
    if authorization and authorization.username and authorization.password
    else unauthorized_response()
)
user_not_exists = lambda username, user: (
    None
    if user
    else ({"message": f"User with username '{username}' not found."}, 404)
)
check_password = lambda user, authorization: (
    ({
        "message": "User authenticated successfully.",
        "token": jwt.encode({"username": user.username, "exp": datetime.now() + timedelta(hours=12)}, SECRET_KEY),
    })
    if check_password_hash(user.password, authorization.password)
    else None
)
user_flow = lambda username, user, authorization: (
        user_not_exists(username, user) or
        check_password(user, authorization) or
        unauthorized_response()
)
auth_flow = lambda authorization: (
        verify_auth(authorization) or
        user_flow(authorization.username, get_user_by_username(authorization.username), authorization)
)
auth = lambda: auth_flow(request.authorization)


def token_required(function):
    def decorated(*args, **kwargs):
        token = request.args.get("token")
        if not token:
            return {"message": "Token is missing."}, 401

        try:
            jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        except Exception as exception:
            print(exception)
            return {"message": "Token is invalid or expired."}, 401

        return function(*args, **kwargs)

    return decorated
