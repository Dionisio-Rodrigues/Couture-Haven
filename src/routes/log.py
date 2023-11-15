from flask import request

from src.services import log as log_service
from src.routes import log_blueprint


@log_blueprint.route(rule="/", methods=["GET"])
def index():
    found_logs = [result.to_dict() for result in log_service.get_all()]

    return {"message": "Logs found successfully.", "logs": found_logs}, 200


@log_blueprint.route(rule="/<id>", methods=["GET"])
def view(id):
    found_log = log_service.get_by_id(id=id)

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

    new_log = log_service.create(message=message).to_dict()

    return {"message": "Log created successfully.", "log": new_log}, 201


@log_blueprint.route(rule="/<id>", methods=["PUT", "PATCH"])
def update(id):
    body = request.get_json()

    if "message" not in body.keys():
        return {"error": "Invalid payload", "message": "Please provide the required log fields."}, 400

    found_log = log_service.get_by_id(id=id)

    if not found_log:
        return {"message": f"Log with ID '{id}' not found."}, 404

    message = body["message"]

    found_log = log_service.update(log=found_log, message=message).to_dict()

    return {"message": "Log updated successfully.", "log": found_log}, 200


@log_blueprint.route(rule="/<id>", methods=["DELETE"])
def destroy(id):
    found_log = log_service.get_by_id(id=id)

    if not found_log:
        return {"message": f"Log with ID '{id}' not found."}, 404

    log_service.delete(log=found_log)

    return {}, 204
