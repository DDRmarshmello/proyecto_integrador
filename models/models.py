from sqlalchemy.sql.sqltypes import Integer, String, DECIMAL
from config.db import meta, engine
from sqlalchemy import Table, ForeignKey, Column, Integer, Date, String, Identity

#TABLA CUSTOMER
customers = Table(
    "customer",
    meta,
    Column("id", Integer, Identity(start=1, cycle=True), primary_key=True),
    Column(
        "name",
        String(255),
    ),
    Column("email", String(255)),
    Column("address", String(255)),
    Column("password", String(255)),   
)

#TABLA ORDER
orders = Table(
    "order",
    meta,
    Column("id", Integer, Identity(start=1, cycle=True), primary_key=True),
    Column(
        "order_date",
        Date,  #si quieres ponle tipo date
    ),
    Column("delivery_id", Integer,ForeignKey("delivery.id")),
    Column("customer_id", Integer,ForeignKey("customer.id")),
    Column("t_price", DECIMAL(10,2)),
)

#TABLA PRODUCTS

products = Table(
    "products",
    meta,
    Column("id", Integer, Identity(start=1, cycle=True), primary_key=True),
    Column(
        "product_name",
        String(300),
    ),
    Column("category_id", Integer,ForeignKey("categories.id")),
    Column("price", DECIMAL(10,2)),
)

#TABLA CATEGORIES

categories = Table(
    "categories",
    meta,
    Column("id", Integer, Identity(start=1, cycle=True), primary_key=True),
    Column(
        "category_name",
        String(255)
    ),
)

#TABLA DELIVERY
deliverys = Table(
    "delivery",
    meta,
    Column("id", Integer, Identity(start=1, cycle=True), primary_key=True),
    Column(
        "type",
        String(255),
    ),
    Column("status", String(255)),
)

#TABLA DETALLE DE ORDEN
details_order = Table(
    "details_order",
    meta,
    Column("id", Integer, Identity(start=1, cycle=True), primary_key=True),
    Column("id_order", Integer, ForeignKey('order.id'),nullable=False),
    Column("id_product", Integer, ForeignKey("products.id"), nullable=False),
    Column("amount_product", Integer, nullable=False, default=0),   
    Column("t_price", DECIMAL(10,2), nullable=False)   
)


meta.create_all(engine)

