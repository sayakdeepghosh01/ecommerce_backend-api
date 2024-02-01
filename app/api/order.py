from fastapi import APIRouter, Depends
from motor.motor_asyncio import AsyncIOMotorDatabase
from app.models.order import Order
from app.database.mongo import get_database
from app.config import settings

router = APIRouter()

@router.post("/create-order", response_model=Order)
async def create_order(order: Order, db: AsyncIOMotorDatabase = Depends(get_database)):
    inserted_order = await db[settings.ORDERS_COLLECTION].insert_one(order.dict())
    return {**order.dict(), "id": str(inserted_order.inserted_id)}

# @router.get("/placed-orders", response_model = dict)
# def placed_orders(
    
# ):
#     response = {
#     "data" : orders
# }
#     return response




