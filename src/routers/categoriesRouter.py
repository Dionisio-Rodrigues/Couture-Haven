from flask import Flask, request, jsonify
from __main__ import app


items = []

@app.route('/api/categories', methods=['GET'])
def get_categories():
    data = {'teste': 'teste'}
    return jsonify(data)

@app.route('/api/categories', methods=['POST'])
def post_category():
    data = request.get_json()
    response = {"message": "Dados enviados com sucesso."}
    return jsonify(response)

@app.route('/api/categories/<int:cat_id>', methods=['PUT'])
def put_category(item_id):
    data = request.get_json()
    if item_id < len(items):
        items[item_id] = data
        response = {"message": "Categoria atualizada com sucesso."}
    else:
        response = {"error": "Categoria não encontrada."}
    return jsonify(response)

@app.route('/api/categories/<int:cat_id>', methods=['DELETE'])
def delete_category(item_id):
    for item in items:
        if item['id'] == item_id:
            items.remove(item)
            response = {"message": "Categoria excluída com sucesso."}
            return jsonify(response)
    response = {"error": "Categoria não encontrada."}
    return jsonify(response)