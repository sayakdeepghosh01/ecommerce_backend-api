from pymongo import MongoClient
MONGODB_URI = "mongodb+srv://sayak-0012:1234@sayakghosh.lhh4cof.mongodb.net/"
client = MongoClient(MONGODB_URI)
db = client["ecommerce"]
products_collection = db["products"]
orders_collection = db["orders"]
