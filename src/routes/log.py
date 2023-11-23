from flask import request

from src.models.log import Log
from src.routes import log_blueprint
from src.services.log import get_all_logs, get_log_by_id, save_log, delete_log


@log_blueprint.route(rule="/", methods=["GET"])
def index():
    found_logs = [result.to_dict() for result in get_all_logs()]

    return {"message": "Logs found successfully.", "logs": found_logs}, 200


@log_blueprint.route(rule="/<id>", methods=["GET"])
def view(id):
    found_log = get_log_by_id(id=id)

    if not found_log:
        return {"message": f"Log with ID '{id}' not found."}, 404

    found_log = found_log.to_dict()

    return {"message": "Log found successfully.", "log": found_log}, 200


@log_blueprint.route(rule="/", methods=["POST"])
def create():
    body = request.get_json()

    if "message" not in body.keys():
        return {"error": "Invalid payload", "message": "Please provide the required log fields."}, 400

    message = body["message"]

    new_log = save_log(Log(message=message)).to_dict()

    return {"message": "Log created successfully.", "log": new_log}, 201


@log_blueprint.route(rule="/<id>", methods=["PUT", "PATCH"])
def update(id):
    body = request.get_json()

    if "message" not in body.keys():
        return {"error": "Invalid payload", "message": "Please provide the required log fields."}, 400

    found_log = get_log_by_id(id=id)

    if not found_log:
        return {"message": f"Log with ID '{id}' not found."}, 404

    found_log.message = body["message"]

    found_log = save_log(log=found_log).to_dict()

    return {"message": "Log updated successfully.", "log": found_log}, 200


@log_blueprint.route(rule="/<id>", methods=["DELETE"])
def destroy(id):
    found_log = get_log_by_id(id=id)

    if not found_log:
        return {"message": f"Log with ID '{id}' not found."}, 404

    delete_log(log=found_log)

    return {}, 204
