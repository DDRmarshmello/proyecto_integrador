from fastapi import APIRouter, status
from config.db import conn
from models.models import products, categories
from schemas.Schemas import Product, Category
from sqlalchemy import select

product = APIRouter()
URL = '/products'
CATEGORIES_URL = '/categories'

@product.get(URL)
async def get_products():
   return conn.execute(products.select()).fetchall()

@product.get(URL + "/{id}")
async def get_product(id: str):
    p = conn.execute(products.select().where(products.c.id == id)).first()
    
    if p is None:
        return { "estatus": status.HTTP_404_NOT_FOUND, "mesage": "El producto no fue encontrado"}
    
    return p


@product.post(URL)
async def create_product(product: Product):
    new_product = {"product_name": product.product_name, "price": product.price, "category": product.category}
    result = conn.execute(products.insert().values(new_product))
    return conn.execute(products.select().where(products.c.id == result.lastrowid)).first()


@product.put(URL + "/{id}")
async def update_products(product: Product, id: int):
    conn.execute(
        products.update()
        .values(product_name = product.product_name, price=product.price, category_id=product.category_id)
        .where(products.c.id == id)
    )
    return conn.execute(products.select().where(products.c.id == id)).first()


@product.delete(URL + "/{id}")
async def delete_product(id: int):
    conn.execute(products.delete().where(products.c.id == id))
    return conn.execute(products.select().where(products.c.id == id)).first()



@product.get(CATEGORIES_URL)
async def get_categories():
    return conn.execute(categories.select()).fetchall()

@product.get(CATEGORIES_URL + "{id}")
async def get_category(id: str):
    c = conn.execute(categories.select()).where(categories.c.id == id).first()
    if c is None:
        return {"status": status.HTTP_404_NOT_FOUND, "mesage": "La categoria no fue encontrado"}

    return c

