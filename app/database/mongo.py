# from pymongo import MongoClient
#MONGODB_URI = "mongodb+srv://sayak-0012:1234@sayakghosh.lhh4cof.mongodb.net/"
# client = MongoClient(MONGODB_URI)
# db = client["ecommerce"]
# products_collection = db["products"]
# orders_collection = db["orders"]

from pymongo import MongoClient
from motor.motor_asyncio import AsyncIOMotorClient
from app.config import settings

#MONGODB_URI = "mongodb+srv://sayak-0012:1234@sayakghosh.lhh4cof.mongodb.net/"

client = MongoClient(settings.MONGODB_URI)
database = client[settings.MONGODB_DB]

async def get_database():
    return AsyncIOMotorClient(settings.MONGODB_URI)[settings.MONGODB_DB]
