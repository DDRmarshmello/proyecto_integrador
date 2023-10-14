from fastapi import FastAPI
from routes.customer import customer    
from routes.products import product
from routes.order import order
app = FastAPI(
    title="Users API",
    description="a REST API using python and mysql",
    version="0.0.1",
)

app.include_router(customer)
app.include_router(product)
app.include_router(order)