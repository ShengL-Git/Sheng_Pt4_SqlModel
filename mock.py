from sqlmodel import Session
from models import Customer, Product, Purchase
from database import engine, create_db_and_tables
from datetime import date


def create_products():
    with Session(engine) as session:
        apple = Product(product_name="apple", category="fruit", stock=10, price=0.99)
        orange = Product(product_name="orange", category="fruit", stock=7, price=0.69)
        banana = Product(product_name="banana", category="fruit", stock=0, price=0.40)

        session.add(apple)
        session.add(orange)
        session.add(banana)
        session.commit()

        session.refresh(apple)
        session.refresh(orange)
        session.refresh(banana)

def create_customers():
    with Session(engine) as session:
        customer_1 = Customer(first_name="nom1", last_name="cognom1")
        customer_2 = Customer(first_name="nom2", last_name="cognom2")
        customer_3 = Customer(first_name="nom3", last_name = "cognom3")

        session.add(customer_1)
        session.add(customer_2)
        session.add(customer_3)
        session.commit()
        session.refresh(customer_1)
        session.refresh(customer_2)
        session.refresh(customer_3)


def create_purchases():
    with Session(engine) as session:
        purchase_1 = Purchase(customer_id=1, product_id=1, purchase_date=date(day=1, month=11, year=2024))
        purchase_2 = Purchase(customer_id=2, product_id=2, purchase_date=date(day=1, month=11, year=2024))
        purchase_3 = Purchase(customer_id=2, product_id=2, purchase_date=date(day=24, month=12, year=2023))
        purchase_4 = Purchase(customer_id=2, product_id=2, purchase_date=date(day=25, month=12, year=2023))

        session.add(purchase_1)
        session.add(purchase_2)
        session.add(purchase_3)
        session.add(purchase_4)

        session.commit()

        session.refresh(purchase_1)
        session.refresh(purchase_2)
        session.refresh(purchase_3)
        session.refresh(purchase_4)


def main():
    create_db_and_tables()
    create_products()
    create_customers()
    create_purchases()

if __name__ == "__main__":
    main()