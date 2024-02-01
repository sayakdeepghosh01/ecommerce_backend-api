
from pydantic import BaseSettings

class Settings(BaseSettings):
    MONGODB_URI: str = "I remove my uri for security purpose"
    MONGODB_DB: str = "ecommerce"
    PRODUCTS_COLLECTION: str = "products"  

settings = Settings()
