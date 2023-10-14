from fastapi import APIRouter, status
from config.db import conn
from models.models import customers
from schemas.Schemas import Customer
from typing import List
from cryptography.fernet import Fernet


customer = APIRouter()
key = Fernet.generate_key()
f = Fernet(key)
URL = '/customer'

@customer.get(URL)
async def get_customer():
   return conn.execute(customers.select()).fetchall()

@customer.get(URL + "/{id}")
def get_customer(id: str):
    customer = conn.execute(customers.select().where(customers.c.id == id)).first()
    
    if customer is None:
        return { "estatus": status.HTTP_404_NOT_FOUND, "mesage": "El usuario no fue encontrado"}
    
    return customer


@customer.post(URL)
def create_customer(customer : Customer):
    new_customer = {"name": customer.name, "email": customer.email}
    new_customer["password"] = f.encrypt(user.password.encode("utf-8"))
    result = conn.execute(customers.insert().values(new_customer))
    return conn.execute(custumers.select().where(custumers.c.id == result.lastrowid)).first()


@customer.put(URL + "/{id}")
def update_user(customer: Customer, id: int):
    conn.execute(
        customers.update()
        .values(name=customer.name, email=customer.email, password=customer.password, address=customer.address)
        .where(customers.c.id == id)
    )
    return conn.execute(custumers.select().where(custumers.c.id == id)).first()


@customer.delete(URL + "/{id}" , status_code=status.HTTP_204_NO_CONTENT)
def delete_customer(id: int):
    conn.execute(customers.delete().where(custumers.c.id == id))
    return conn.execute(custumers.select().where(custumers.c.id == id)).first()
