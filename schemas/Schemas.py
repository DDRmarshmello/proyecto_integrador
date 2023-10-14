from typing import Optional
from datetime import datetime
from pydantic import BaseModel

class Customer(BaseModel):
    id: Optional[int]
    name: str   
    email: str
    address: str
    password: str
    
class Product(BaseModel):
    id: Optional[int]
    product_name: str
    price: float
    category_id: int 

class Category(BaseModel):
    id: Optional[int]
    category_name: str
    
class Order(BaseModel):
    id: Optional[int]
    order_date: datetime
    delivery_id: int
    customer_id: int
    t_price: float
    
class OrderStatus(BaseModel):
    id: Optional[int]
    status: str
    type: str

class Details(BaseModel):
    order: int
    produtc: str
    price: float
    amount: int
    
