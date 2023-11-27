from flask import request

from src.models.log import Log
from src.routes import log_blueprint
from src.services.log import get_all_logs, get_log_by_id, save_log, delete_log
from src.utilities.general import models_to_dict
from src.utilities.flask import maybe_bind_id
from src.utilities.auth import token_required

# Validations
contains_message_response = lambda body: (
    None
    if "message" in body.keys()
    else ({"error": "Invalid payload", "message": "Please provide the required log fields."}, 400)
)

log_id_not_exists_response = lambda id: (
    ({"message": f"Log with ID '{id}' not found."}, 404)
    if not get_log_by_id(id=id)
    else None
)

# Index
index = lambda: ({"message": "Logs found successfully.", "logs": models_to_dict(get_all_logs())}, 200)

# View
view_response = lambda id, log: (
    ({"message": "Log found successfully.", "log": log.to_dict()}, 200)
    if log
    else ({"message": f"Log with ID '{id}' not found."}, 404)
)
view_flow = lambda id: view_response(id, get_log_by_id(id=id))
view = lambda id: maybe_bind_id(id, view_flow)

# Create
create_response = lambda body: (
        contains_message_response(body) or
        ({"message": "Log created successfully.", "log": save_log(Log(message=body["message"])).to_dict()}, 201)
)
create = lambda: create_response(request.get_json())

# Update
update_response = lambda id, body, log: (
        contains_message_response(body) or
        log_id_not_exists_response(id) or
        log.set_message(body["message"]) or
        ({"message": "Log updated successfully.", "log": save_log(log).to_dict()}, 200)
)
update_flow = lambda id: update_response(id, request.get_json(), get_log_by_id(id=id))
update = lambda id: maybe_bind_id(id, update_flow)

# Destroy
destroy_response = lambda id: log_id_not_exists_response(id) or (delete_log(log=get_log_by_id(id=id)), ({}, 204))[1]
destroy = lambda id: maybe_bind_id(id, destroy_response)

log_blueprint.add_url_rule(
    rule="/",
    endpoint="index",
    view_func=token_required(index),
    methods=["GET"],
)
log_blueprint.add_url_rule(
    rule="/<int:id>",
    endpoint="view",
    view_func=token_required(view),
    methods=["GET"],
)
log_blueprint.add_url_rule(
    rule="/",
    endpoint="create",
    view_func=token_required(create),
    methods=["POST"],
)
log_blueprint.add_url_rule(
    rule="/<int:id>",
    endpoint="update",
    view_func=token_required(update),
    methods=["PUT", "PATCH"],
)
log_blueprint.add_url_rule(
    rule="/<int:id>",
    endpoint="destroy",
    view_func=token_required(destroy),
    methods=["DELETE"],
)
