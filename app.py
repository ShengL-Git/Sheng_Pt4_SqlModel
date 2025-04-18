from http.client import HTTPException

from fastapi import FastAPI, HTTPException
from database import lifespan, engine
from sqlmodel import Session, select
from models import *

app = FastAPI(lifespan=lifespan)

@app.get("/")
def root():
    return {"message":"Welcome to FastAPI and SQLModel"}

# CUSTOMER

@app.post("/customers", response_model=CustomerPublic)
def create_customer(customer: CustomerCreate):
    with Session(engine) as session:
        new_customer = Customer.model_validate(customer)
        session.add(new_customer)
        session.commit()
        session.refresh(new_customer)
        return new_customer


@app.get("/customers", response_model=list[CustomerPublic])
def read_customers():
    with Session(engine) as session:
        customers = session.exec(select(Customer)).all()
    return customers


@app.get("/customers/{customer_id}", response_model=CustomerPublic)
def read_customer(customer_id: int):
    with Session(engine) as session:
        customer = session.get(Customer, customer_id)
    return customer


@app.patch("/customers/{customer_id}", response_model=CustomerPublic)
def update_customer(customer_id: int, new_customer: CustomerUpdate):
    with Session(engine) as session:
        customer = session.get(Customer, customer_id)
        if not customer:
            raise HTTPException(status_code=404, detail="Customer not found")
        customer_data = new_customer.model_dump(exclude_unset=True)
        for k, v in customer_data.items():
            setattr(customer, k, v)
        session.commit()
        session.refresh(customer)
        return customer


@app.delete("/customers/{customer_id}", response_model=CustomerPublic)
def delete_customer(customer_id: int):
    with Session(engine) as session:
        customer = session.get(Customer, customer_id)
        if not customer:
            raise HTTPException(status_code=404, detail="Customer not found")
        session.delete(customer)
        session.commit()
        return True

# PRODUCT

@app.post("/products", response_model=ProductPublic)
def create_product(product: ProductCreate):
    with Session(engine) as session:
        new_product = ProductCreate.model_validate(product)
        session.add(new_product)
        session.commit()
        session.refresh(new_product)
        return new_product


@app.get("/products")
def read_products():
    with Session(engine) as session:
        products = session.exec(select(Product)).all()
    return products


@app.get("/products/{product_id}")
def read_product(product_id: int):
    with Session(engine) as session:
        product = session.get(Product, product_id)
    return product


@app.put("/products/{product_id}", response_model=ProductPublic)
def update_product(product_id: int, new_product: ProductUpdate):
    with Session(engine) as session:
        product = session.get(Customer, product_id)
        if not product:
            raise HTTPException(status_code=404, detail="Customer not found")
        customer_data = new_product.model_dump(exclude_unset=True)
        for k, v in customer_data.items():
            setattr(product, k, v)
        session.commit()
        session.refresh(product)
        return product


@app.delete("/products/{product_id}", response_model=ProductPublic)
def delete_product(product_id: int):
    with Session(engine) as session:
        product = session.get(Product, product_id)
        if not product:
            raise HTTPException(status_code=404, detail="Customer not found")
        session.delete(product)
        session.commit()
        return True




