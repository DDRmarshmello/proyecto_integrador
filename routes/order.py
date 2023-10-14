from fastapi import APIRouter
from config.db import conn
from models.models import orders, details_order
from schemas.Schemas import Order, OrderStatus, Details
from sqlalchemy import select, join

order = APIRouter()
ORDER_URL = '/orders'

@order.get(ORDER_URL)
async def get_order():
    r = select(orders.join(details_order, orders.c.id == details_order.c.id_order))
    return conn.execute(r).fetchall()
 
  

    
""" from sqlalchemy import join

j = user_table.join(address_table,
                user_table.c.id == address_table.c.user_id)
stmt = select(user_table).select_from(j) """