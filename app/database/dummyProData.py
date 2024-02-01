from pymongo import MongoClient


MONGO_URI = "I remove my uri for security purpose"
database_name = "ecommerce"
collection_name = "products"

# Dummy products
dummy_products = [
    {"id": "1", "name": "TV", "price": 500.0, "quantity": 10},
    {"id": "2", "name": "Laptop", "price": 1000.0, "quantity": 5},
    {"id": "3", "name": "Headphones", "price": 50.0, "quantity": 20},
    {"id": "4", "name": "Air Conditioner", "price": 1200.0, "quantity": 8},
    {"id": "5", "name": "Smartphone", "price": 800.0, "quantity": 15},
    {"id": "6", "name": "Refrigerator", "price": 900.0, "quantity": 12},
    {"id": "7", "name": "Washing Machine", "price": 700.0, "quantity": 18},
    {"id": "8", "name": "Coffee Maker", "price": 60.0, "quantity": 25},
    {"id": "9", "name": "Blender", "price": 40.0, "quantity": 30},
    {"id": "10", "name": "Microwave Oven", "price": 150.0, "quantity": 10},
    {"id": "11", "name": "Vacuum Cleaner", "price": 80.0, "quantity": 22},
    {"id": "12", "name": "Gaming Console", "price": 300.0, "quantity": 7},
    {"id": "13", "name": "Home Theater System", "price": 200.0, "quantity": 15},
    {"id": "14", "name": "Smartwatch", "price": 100.0, "quantity": 30},
    {"id": "15", "name": "Digital Camera", "price": 250.0, "quantity": 12},
    {"id": "16", "name": "Router", "price": 70.0, "quantity": 25},
    {"id": "17", "name": "Printer", "price": 120.0, "quantity": 8},
    {"id": "18", "name": "Desk Chair", "price": 50.0, "quantity": 20},
    {"id": "19", "name": "LED Bulbs", "price": 5.0, "quantity": 50},
    {"id": "20", "name": "Smart Thermostat", "price": 80.0, "quantity": 15}
]

# Connecting
client = MongoClient(MONGO_URI)
db = client[database_name]
collection = db[collection_name]

# Inserting
collection.insert_many(dummy_products)

client.close()
