from flask import Flask, request, jsonify

app = Flask(__name__)
items = []

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {'teste': 'teste'}
    return jsonify(data)

@app.route('/api/data', methods=['POST'])
def post_data():
    data = request.get_json()
    response = {"message": "Dados enviados com sucesso"}
    return jsonify(response)

@app.route('/api/data/<int:item_id>', methods=['PUT'])
def put_data(item_id):
    data = request.get_json()
    if item_id < len(items):
        items[item_id] = data
        response = {"message": "Item atualizado com sucesso"}
    else:
        response = {"error": "Item não encontrado"}
    return jsonify(response)

@app.route('/api/data/<int:item_id>', methods=['DELETE'])
def delete_data(item_id):
    for item in items:
        if item['id'] == item_id:
            items.remove(item)
            response = {"message": "Item excluído com sucesso"}
            return jsonify(response)
    response = {"error": "Item não encontrado"}
    return jsonify(response)