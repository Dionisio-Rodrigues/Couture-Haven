from requests import post

BASE_API_URL = "http://localhost:3001"

CATEGORIES = [
    {"name": "Camisas"},
    {"name": "Casacos"},
    {"name": "Calças"},
    {"name": "Bermudas"},
]

PRODUCTS = [
    {"name": "Camisa polo branca", "price": 79.99, "category_id": 1},
    {"name": "Camisa careca cinza", "price": 49.99, "category_id": 1},
    {"name": "Casaco zíper azul", "price": 139.99, "category_id": 2},
    {"name": "Casaco simples amarelo", "price": 89.99, "category_id": 2},
    {"name": "Calça jeans azul", "price": 124.99, "category_id": 3},
    {"name": "Calça brim preta", "price": 69.99, "category_id": 3},
]

seed = lambda: (
    print("SEEDING DATABASE..."),
    print("INSERTING CATEGORY(IES) INTO DATABASE..."),
    [post(url=f"{BASE_API_URL}/category", json={"name": category["name"]}) for category in CATEGORIES],
    print(f"[SUCCESS] {len(CATEGORIES)} CATEGORY(IES) INSERTED."),
    print("INSERTING PRODUCT(S) INTO DATABASE..."),
    [
        post(
            url=f"{BASE_API_URL}/product",
            json={"name": product["name"], "price": product["price"], "category_id": product["category_id"]},
        ) for product in PRODUCTS
    ],
    print(f"[SUCCESS] {len(PRODUCTS)} PRODUCT(S) INSERTED."),
    print("[SUCCESS] SEED COMPLETE.")
)

seed()
