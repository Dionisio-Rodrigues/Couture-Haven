from src.routes import auth_blueprint
from src.utilities.auth import auth

auth_blueprint.add_url_rule(rule="/", endpoint="auth", view_func=auth, methods=["POST"])
