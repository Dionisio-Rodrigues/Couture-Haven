from requests import post

BASE_API_URL = "http://localhost:3001"

CATEGORIES = [{"name": "Camisas"}, {"name": "Calçados"}, {"name": "Casacos"}, {"name": "Calças"}, {"name": "Bermudas"}]

PRODUCTS = [
    {"name": "Camisa Polo Branca", "price": 79.99, "category_id": 1},
    {"name": "Camisa Básica Cinza", "price": 49.99, "category_id": 1},
    {"name": "Nike Pegasus 34", "price": 499.99, "category_id": 2},
    {"name": "Casaco Zíper Azul", "price": 139.99, "category_id": 3},
    {"name": "Casaco Simples Amarelo", "price": 89.99, "category_id": 3},
    {"name": "Calça Jeans Azul", "price": 124.99, "category_id": 4},
    {"name": "Calça Brim Preta", "price": 69.99, "category_id": 4},
]

USERS = [
    {"username": "augustofaria", "password": "1710558"},
    {"username": "dionisiorodrigues", "password": "2010789"},
    {"username": "guthierremarques", "password": "2127307"},
    {"username": "victorkauan", "password": "2213002"},
]

authenticate = lambda username, password: post(url=f"{BASE_API_URL}/auth", auth=(username, password))

insert_users = lambda: (
    print("INSERTING USER(S) INTO DATABASE..."),
    [post(url=f"{BASE_API_URL}/user", json=user) for user in USERS],
    print(f"[SUCCESS] {len(USERS)} USER(S) INSERTED."),
)

insert_categories = lambda token: (
    print("INSERTING CATEGORY(IES) INTO DATABASE..."),
    [post(url=f"{BASE_API_URL}/category?token={token}", json=category) for category in CATEGORIES],
    print(f"[SUCCESS] {len(CATEGORIES)} CATEGORY(IES) INSERTED."),
)

insert_products = lambda token: (
    print("INSERTING PRODUCT(S) INTO DATABASE..."),
    [post(url=f"{BASE_API_URL}/product?token={token}", json=product) for product in PRODUCTS],
    print(f"[SUCCESS] {len(PRODUCTS)} PRODUCT(S) INSERTED."),
)

insert_entities = lambda auth_response: (
    insert_categories(auth_response["token"]),
    insert_products(auth_response["token"])
)

seed = lambda: (
    print("SEEDING DATABASE..."),
    insert_users(),
    insert_entities(authenticate(USERS[0]["username"], USERS[0]["password"]).json()),
    print("[SUCCESS] SEED COMPLETE.")
)

seed()
