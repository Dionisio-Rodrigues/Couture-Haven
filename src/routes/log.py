from flask import request, jsonify

from src.routes import log_blueprint

items = []


@log_blueprint.route(rule="/", methods=["GET"])
def get_logs(data):
    return jsonify(data)


@log_blueprint.route(rule="/", methods=["POST"])
def post_log():
    data = request.get_json()
    response = {"message": "Dados enviados com sucesso"}
    return jsonify(response)


@log_blueprint.route(rule="/<id>", methods=["PUT", "PATCH"])
def put_log(id):
    data = request.get_json()
    if id < len(items):
        items[id] = data
        response = {"message": "Log atualizado com sucesso."}
    else:
        response = {"error": "Log não encontrado."}
    return jsonify(response)


@log_blueprint.route(rule="/<id>", methods=["DELETE"])
def delete_log(id):
    for item in items:
        if item["id"] == id:
            items.remove(item)
            response = {"message": "Log excluído com sucesso."}
            return jsonify(response)
    response = {"error": "Log não encontrado."}
    return jsonify(response)
