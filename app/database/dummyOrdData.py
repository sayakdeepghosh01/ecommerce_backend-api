from pymongo import MongoClient
from datetime import datetime

# MongoDB connection details
MONGO_URI = "I remove my uri for security purpose"
database_name = "ecommerce"
products_collection_name = "products"
orders_collection_name = "orders"

# Dummy products adding
dummy_products = [
    {"id": "1", "name": "TV", "price": 500.0, "quantity": 10},
    {"id": "2", "name": "Laptop", "price": 1000.0, "quantity": 5},
    {"id": "3", "name": "Headphones", "price": 50.0, "quantity": 20},
    
]

# Demo orders adding
demo_orders = [
    {
        "items": [
            {"productId": "1", "boughtQuantity": 2},
            {"productId": "2", "boughtQuantity": 1},
        ],
        "total_amount": 2000.0,
        "user_address": {"city": "DemoCity", "country": "DemoCountry", "zip_code": "12345"},
        "createdOn": datetime.utcnow(),
    },
    {
        "items": [
            {"productId": "3", "boughtQuantity": 5},
            {"productId": "4", "boughtQuantity": 3},
        ],
        "total_amount": 325.0,
        "user_address": {"city": "AnotherCity", "country": "AnotherCountry", "zip_code": "67890"},
        "createdOn": datetime.utcnow(),
    },
    
]

# Connection with DB
client = MongoClient(MONGO_URI)
db = client[database_name]
products_collection = db[products_collection_name]
orders_collection = db[orders_collection_name]

# Inserting
products_collection.insert_many(dummy_products)

orders_collection.insert_many(demo_orders)

client.close()
