from pydantic import BaseModel
from typing import List
from bson import ObjectId

class OrderItem(BaseModel):
    productId: str 
    boughtQuantity: int

class UserAddress(BaseModel):
    city: str
    country: str
    zip_code: str

class Order(BaseModel):
    items: List[OrderItem]
    total_amount: float
    user_address: UserAddress
    createdOn: str  

    class Config:
        arbitrary_types_allowed = True
