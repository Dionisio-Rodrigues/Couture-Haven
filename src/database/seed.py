import json

# Category initial data load
categories_data = [
    {"id": 1, "name": "Camisas"},
    {"id": 2, "name": "Casacos"},
    {"id": 3, "name": "Calças"},
    {"id": 3, "name": "Bermudas"},
]

# Product initial data load
products_data = [
    {"id": 101, "name": "Camisa polo branca", "price": 79.99, "category_id": 1},
    {"id": 102, "name": "Camisa careca cinza", "price": 49.99, "category_id": 1},
    {"id": 201, "name": "Casaco zíper azul", "price": 139.99, "category_id": 2},
    {"id": 202, "name": "Casaco simples amarelo", "price": 89.99, "category_id": 2},
    {"id": 301, "name": "Calça jeans azul", "price": 124.99, "category_id": 3},
    {"id": 302, "name": "Calça brim preta", "price": 69.99, "category_id": 3},
]

# Parse entities to JSON
categories_json = json.dumps(categories_data, indent=4)
products_json = json.dumps(products_data, indent=4)
