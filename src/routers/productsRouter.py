from flask import Flask, request, jsonify
from __main__ import app

items = []

@app.route('/api/products', methods=['GET'])
def get_products():
    data = {'teste': 'teste'}
    return jsonify(data)

@app.route('/api/products', methods=['POST'])
def post_product():
    data = request.get_json()
    response = {"message": "Dados enviados com sucesso"}
    return jsonify(response)

@app.route('/api/products/<int:item_id>', methods=['PUT'])
def put_product(item_id):
    data = request.get_json()
    if item_id < len(items):
        items[item_id] = data
        response = {"message": "Item atualizado com sucesso"}
    else:
        response = {"error": "Item não encontrado"}
    return jsonify(response)

@app.route('/api/products/<int:item_id>', methods=['DELETE'])
def delete_product(item_id):
    for item in items:
        if item['id'] == item_id:
            items.remove(item)
            response = {"message": "Item excluído com sucesso"}
            return jsonify(response)
    response = {"error": "Item não encontrado"}
    return jsonify(response)