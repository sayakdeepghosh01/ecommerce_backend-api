
from pydantic import BaseSettings

class Settings(BaseSettings):
    MONGODB_URI: str = "mongodb+srv://sayak-0012:1234@sayakghosh.lhh4cof.mongodb.net/"
    MONGODB_DB: str = "ecommerce"
    PRODUCTS_COLLECTION: str = "products"  # Add this line

settings = Settings()
