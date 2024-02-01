from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.api import product, order
from app.database import mongo
from app.config import settings

app = FastAPI()

app.include_router(product.router, prefix="/products", tags=["products"])
app.include_router(order.router, prefix="/orders", tags=["orders"])

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
