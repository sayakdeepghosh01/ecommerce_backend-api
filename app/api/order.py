from fastapi import APIRouter, HTTPException
from app.models.order import Order
from app.database.mongo import orders_collection, products_collection

router = APIRouter()

@router.post("/", response_model=dict)
async def create_order(order: Order):
    # Calculate total amount
    total_amount = sum(
        item["boughtQuantity"] * products_collection.find_one({"id": item["productId"]})["price"]
        for item in order.items
    )

    # Insert the order into the database
    order_data = {
        "createdOn": None,  # Let MongoDB handle the creation timestamp
        "items": order.items,
        "total_amount": total_amount,
        "user_address": order.user_address.dict(),
    }

    result = orders_collection.insert_one(order_data)

    return {"order_id": str(result.inserted_id)}


# @router.get("/placed-orders", response_model = dict)
# def placed_orders(
    
# ):
#     response = {
#     "data" : orders
# }
#     return response




