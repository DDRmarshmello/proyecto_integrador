from fastapi import APIRouter
from config.db import conn

order = APIRouter()
ORDER_URL = '/orders'
ORDER_STATUS_URL = ORDER_URL + '/status'

@order.get(ORDER_URL + "/{id}")
async def get_order(id : int):
    od = conn.execute("SELECT OD.ID, OD.order_date, OD.t_price, DELI.status, DELI.type FROM proyecto_integrador.ORDER as OD INNER JOIN delivery AS DELI ON OD.delivery_id = DELI.ID INNER JOIN customer as client on OD.customer_id = client.id where id =" + id).fetchall()
    detail_od = conn.execute("SELECT PROD.product_name, DO.amount_product CATE.category_name DO.t_price, FROM details_order AS DO INNER JOIN products AS PROD ON DO.id_product = PROD.ID INNER JOIN categories AS CATE on PROD.category_id = CATE.ID WHERE DO.id_order =" + id).fetchall()
    return {"oder": od, "product_details": detail_od} 

@order.get(ORDER_STATUS_URL)
async def orders_status():
    order_status = conn.execute("SELECT OD.ID, OD.order_date, OD.t_price, DELI.status, DELI.type FROM proyecto_integrador.ORDER as OD INNER JOIN delivery AS DELI ON OD.delivery_id = DELI.ID INNER JOIN customer as client on OD.customer_id = client.id").fetchall()
    return order_status

@order.get(ORDER_STATUS_URL + "/{id}")
async def orders_status(id : int):
    order_status = conn.execute("SELECT OD.ID, OD.order_date, OD.t_price, DELI.status, DELI.type FROM proyecto_integrador.ORDER as OD INNER JOIN delivery AS DELI ON OD.delivery_id = DELI.ID INNER JOIN customer as client on OD.customer_id = client.id=" + id).fetchall()
    return order_status
  
