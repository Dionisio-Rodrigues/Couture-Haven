from flask import request, jsonify

from src.app import app

items = []


@app.route('/api/logs', methods=['GET'])
def get_logs():
    data = {'teste': 'teste'}
    return jsonify(data)


@app.route('/api/logs', methods=['POST'])
def post_log():
    data = request.get_json()
    response = {"message": "Dados enviados com sucesso"}
    return jsonify(response)


@app.route('/api/logs/<int:log_id>', methods=['PUT'])
def put_log(item_id):
    data = request.get_json()
    if item_id < len(items):
        items[item_id] = data
        response = {"message": "Log atualizado com sucesso."}
    else:
        response = {"error": "Log não encontrado."}
    return jsonify(response)


@app.route('/api/logs/<int:log_id>', methods=['DELETE'])
def delete_log(item_id):
    for item in items:
        if item['id'] == item_id:
            items.remove(item)
            response = {"message": "Log excluído com sucesso."}
            return jsonify(response)
    response = {"error": "Log não encontrado."}
    return jsonify(response)
