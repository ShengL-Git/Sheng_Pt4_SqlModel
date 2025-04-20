from fastapi import FastAPI, HTTPException
from sqlalchemy.sql.functions import count

from database import lifespan, engine
from sqlmodel import Session, select, desc
from models import *

app = FastAPI(lifespan=lifespan)

@app.get("/")
def root():
    return {"message":"Welcome to FastAPI and SQLModel"}

# ADDITIONAL ENDPOINTS

@app.get("/customers/most_purchases", response_model=list[Customer])
def order_customer_by_purchases():
    # select c.* as 'purchases' from purchase p join customer c on p.customer_id = c.customer_id group by p.customer_id order by count(p.customer_id) desc;

    with Session(engine) as session:
        customers = session.exec(select(Customer).join(Purchase, Purchase.customer_id == Customer.customer_id).group_by(Purchase.customer_id).order_by(count(Purchase.customer_id).desc())).all()

        return customers


@app.get("/products/order_by_price", response_model=list[Product])
def order_products_by_price():
    with Session(engine) as session:
        ordered_products = session.exec(select(Product).order_by(desc(Product.price)))
        return ordered_products.all()


@app.get("/purchases/customer/{customer_id}", response_model=list[Purchase])
def num_purchases_by_customer(customer_id:int):
    with Session(engine) as session:
        if not session.get(Customer, customer_id):
            raise HTTPException(status_code=404, detail="Customer not found")
        purchase_list = session.exec(select(Purchase).where(Purchase.customer_id == customer_id)).all()
        return purchase_list


@app.get("/purchases/product/{product_id}", response_model=list[Purchase])
def num_purchases_by_product(product_id:int):
    with Session(engine) as session:
        if not session.get(Product, product_id):
            raise HTTPException(status_code=404, detail="Product not found")
        purchase_list = session.exec(select(Purchase).where(Purchase.product_id == product_id)).all()
        return purchase_list


@app.get("/products/out_of_stock", response_model=list[Product])
def products_out_of_stock():
    with Session(engine) as session:
        product_list = session.exec(select(Product).where(Product.stock == 0)).all()
        return product_list


# CUSTOMERS CRUD

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


@app.delete("/customers/{customer_id}", response_model=bool)
def delete_customer(customer_id: int):
    with Session(engine) as session:
        customer = session.get(Customer, customer_id)
        if not customer:
            raise HTTPException(status_code=404, detail="Customer not found")
        session.delete(customer)
        session.commit()
        return True

# PRODUCTS CRUD

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


@app.patch("/products/{product_id}", response_model=ProductPublic)
def update_product(product_id: int, new_product: ProductUpdate):
    with Session(engine) as session:
        product = session.get(Product, product_id)
        if not product:
            raise HTTPException(status_code=404, detail="Customer not found")
        product_data = new_product.model_dump(exclude_unset=True)
        for k, v in product_data.items():
            setattr(product, k, v)
        session.commit()
        session.refresh(product)
        return product


@app.delete("/products/{product_id}", response_model=bool)
def delete_product(product_id: int):
    with Session(engine) as session:
        product = session.get(Product, product_id)
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        session.delete(product)
        session.commit()
        return True

# PURCHASES CRUD

@app.post("/purchases", response_model=PurchasePublic)
def create_purchase(new_purchase: PurchaseCreate):
    with Session(engine) as session:
        purchase = Purchase.model_validate(new_purchase)
        session.add(purchase)
        session.commit()
        session.refresh(purchase)
        return purchase


@app.get("/purchases", response_model=list[Purchase])
def read_purchases():
    with Session(engine) as session:
        purchases = session.exec(select(Purchase)).all()
        return purchases


@app.get("/purchases/{purchase_id}")
def read_purchase(purchase_id:int):
    with Session(engine) as session:
        purchase = session.get(Purchase, purchase_id)
        return purchase


@app.patch("/purchases/{purchase_id}", response_model=PurchasePublic)
def update_purchase(purchase_id:int, new_purchase:PurchaseUpdate):
    with Session(engine) as session:
        purchase = session.get(Purchase, purchase_id)
        if not purchase:
            raise HTTPException(status_code=404, detail="Purchase not found")
        purchase_date = new_purchase.model_dump(exclude_unset=True)
        for k, v in purchase_date.items():
            setattr(purchase, k, v)
        session.add(purchase)
        session.commit()
        session.refresh(purchase)
        return purchase


@app.delete("/purchases/{purchase_id}", response_model=bool)
def delete_purchase(purchase_id:int):
    with Session(engine) as session:
        purchase = session.get(Purchase, purchase_id)
        if not purchase:
            raise HTTPException(status_code=404, detail="Purchase not found")
        session.delete(purchase)
        session.commit()
        return True

