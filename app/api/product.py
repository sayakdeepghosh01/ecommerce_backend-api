from fastapi import APIRouter, Query
from app.models.product import Product
from app.database.mongo import products_collection

router = APIRouter()

@router.get("/", response_model=dict)
def list_products(
    limit: int = Query(10, alias="limit", ge=1, le=100),
    offset: int = Query(0, alias="offset", ge=0),
    min_price: float = None,
    max_price: float = None,
):
    query = {}
    if min_price is not None:
        query["price"] = {"$gte": min_price}
    if max_price is not None:
        query.setdefault("price", {})["$lte"] = max_price

    total_records = products_collection.count_documents(query)
    products = list(
        products_collection.find(query, {"_id": 0, "id": 1, "name": 1, "price": 1, "quantity": 1})
        .skip(offset)
        .limit(limit)
    )

    response = {
        "data": products,
        "page": {
            "limit": limit,
            "nextOffset": offset + limit if offset + limit < total_records else None,
            "prevOffset": offset - limit if offset - limit >= 0 else None,
            "total": total_records,
        },
    }

    return response
