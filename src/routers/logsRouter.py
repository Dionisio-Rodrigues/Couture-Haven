from flask import Flask, request, jsonify
from __main__ import app

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

@app.route('/api/logs/<int:item_id>', methods=['PUT'])
def put_log(item_id):
    data = request.get_json()
    if item_id < len(items):
        items[item_id] = data
        response = {"message": "Item atualizado com sucesso"}
    else:
        response = {"error": "Item não encontrado"}
    return jsonify(response)

@app.route('/api/logs/<int:item_id>', methods=['DELETE'])
def delete_log(item_id):
    for item in items:
        if item['id'] == item_id:
            items.remove(item)
            response = {"message": "Item excluído com sucesso"}
            return jsonify(response)
    response = {"error": "Item não encontrado"}
    return jsonify(response)