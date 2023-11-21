from requests import post

BASE_API_URL = "http://localhost:3001"

CATEGORIES = [
    {"name": "Camisas"},
    {"name": "Casacos"},
    {"name": "Calças"},
    {"name": "Bermudas"},
]

# PRODUCTS_DATA = [
#     {"id": 1, "name": "Camisa polo branca", "price": 79.99, "category_id": 1},
#     {"id": 2, "name": "Camisa careca cinza", "price": 49.99, "category_id": 1},
#     {"id": 3, "name": "Casaco zíper azul", "price": 139.99, "category_id": 2},
#     {"id": 4, "name": "Casaco simples amarelo", "price": 89.99, "category_id": 2},
#     {"id": 5, "name": "Calça jeans azul", "price": 124.99, "category_id": 3},
#     {"id": 6, "name": "Calça brim preta", "price": 69.99, "category_id": 3},
# ]


def seed():
    print("SEEDING DATABASE...")

    print("INSERTING CATEGORY(IES) INTO DATABASE...")
    [post(url=f"{BASE_API_URL}/category", json={"name": category["name"]}) for category in CATEGORIES]
    print(f"[SUCCESS] {len(CATEGORIES)} CATEGORY(IES) INSERTED.")

    print("[SUCCESS] SEED COMPLETE.")


if __name__ == "__main__":
    seed()
