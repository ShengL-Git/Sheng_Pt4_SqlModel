from fastapi import FastAPI
from database import lifespan, engine
from sqlmodel import Session, select
from models import *

app = FastAPI(lifespan=lifespan)

@app.get("/")
def root():
    return {"message":"Welcome to FastAPI and SQLModel"}

# CUSTOMER

@app.get("/customers")
def get_customers():
    with Session(engine) as session:
        customers = session.exec(select(Customer)).all()
    return customers


@app.get("/customers/{customer_id}")
def get_customer(customer_id: int):
    with Session(engine) as session:
        customer = session.get(Customer, customer_id)
    return customer


@app.post("/customers", response_model=CustomerPublic)
def create_customer(customer: CustomerCreate):
    with Session(engine) as session:
        new_customer = Customer.model_validate(customer)
        session.add(new_customer)
        session.commit()
        session.refresh(new_customer)
        return new_customer


# PRODUCT

@app.get("/products")
def get_products():
    with Session(engine) as session:
        products = session.exec(select(Product)).all()
    return products


@app.get("/products/{product_id}")
def get_product(product_id: int):
    with Session(engine) as session:
        product = session.get(Product, product_id)
    return product


@app.post("/products", response_model=ProductPublic)
def create_product(product: ProductCreate):
    with Session(engine) as session:
        new_product = Product.model_validate(product)
        session.add(new_product)
        session.commit()
        session.refresh(new_product)
        return new_product

