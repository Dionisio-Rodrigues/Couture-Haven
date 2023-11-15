from flask import request, jsonify
from src.app import app

items = []


@app.route('/api/products', methods=['GET'])
def get_products():
    data = {'teste': 'teste'}
    return jsonify(data)


@app.route('/api/products', methods=['POST'])
def post_product():
    data = request.get_json()
    response = {"message": "Dados enviados com sucesso."}
    return jsonify(response)


@app.route('/api/products/<int:prod_id>', methods=['PUT'])
def put_product(item_id):
    data = request.get_json()
    if item_id < len(items):
        items[item_id] = data
        response = {"message": "Produto atualizado com sucesso."}
    else:
        response = {"error": "Produto não encontrado."}
    return jsonify(response)


@app.route('/api/products/<int:prod_id>', methods=['DELETE'])
def delete_product(item_id):
    for item in items:
        if item['id'] == item_id:
            items.remove(item)
            response = {"message": "Produto excluído com sucesso."}
            return jsonify(response)
    response = {"error": "Produto não encontrado."}
    return jsonify(response)
