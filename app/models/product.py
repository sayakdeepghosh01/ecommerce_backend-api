from pydantic import BaseModel
from bson import ObjectId

class Product(BaseModel):
    id: str  # Convert ObjectId to str
    name: str
    price: float
    quantity: int

    class Config:
        arbitrary_types_allowed = True
