from fastapi import FastAPI
from app.api import product, order

app = FastAPI()

app.include_router(product.router, prefix="/products", tags=["products"])
app.include_router(order.router, prefix="/orders", tags=["orders"])
