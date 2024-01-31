from typing import List
from pydantic import BaseModel
from app.models.product import Product

class UserAddress(BaseModel):
    city: str
    country: str
    zip_code: str

class OrderItem(BaseModel):
    productId: str
    boughtQuantity: int

class Order(BaseModel):
    items: List[OrderItem]
    total_amount: float
    user_address: UserAddress
