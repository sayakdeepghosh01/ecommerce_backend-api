from fastapi import APIRouter, Depends
from motor.motor_asyncio import AsyncIOMotorDatabase
from app.models.product import Product
from app.database.mongo import get_database
from app.config import settings

router = APIRouter()

@router.get("/", response_model=list[Product])
async def list_products(
    limit: int = 10,
    offset: int = 0,
    min_price: float = 0.0,
    max_price: float = float("inf"),
    db: AsyncIOMotorDatabase = Depends(get_database),
):
    products = await db[settings.PRODUCTS_COLLECTION].find(
        {"price": {"$gte": min_price, "$lte": max_price}}
    ).to_list(limit + 1, offset)
    return products


