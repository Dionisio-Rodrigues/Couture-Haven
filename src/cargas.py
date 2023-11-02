import chDBConn
import json

# Carga inicial de categorias
categorias_data = [
    {"codigo": 1, "descricao": "Camisas"},
    {"codigo": 2, "descricao": "Casacos"},
    {"codigo": 3, "descricao": "Calças"},
    {"codigo": 3, "descricao": "Bermudas"},
]

# Carga inicial de produtos
produtos_data = [
    {"codigo": 101, "nome": "Camisa polo branca", "preco": 79.99, "categoria": 1},
    {"codigo": 102, "nome": "Camisa careca cinza", "preco": 49.99, "categoria": 1},
    {"codigo": 201, "nome": "Casaco zíper azul", "preco": 139.99, "categoria": 2},
    {"codigo": 202, "nome": "Casaco simples amarelo", "preco": 89.99, "categoria": 2},
    {"codigo": 301, "nome": "Calça jeans azul", "preco": 124.99, "categoria": 3},
    {"codigo": 302, "nome": "Calça brim preta", "preco": 69.99, "categoria": 3},
]

# Converter os dados para JSON
categorias_json = json.dumps(categorias_data, indent=4)
produtos_json = json.dumps(produtos_data, indent=4)

