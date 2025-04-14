from sqlmodel import Session
from models import Customer, Product, CustomerProductLink
from database import engine, create_db_and_tables


def create_products():
    with Session(engine) as session:
        apple = Product(product_name="apple", category="fruit", stock=10, price=0.99)
        orange = Product(product_name="orange", category="fruit", stock=7, price=0.69)

        session.add(apple)
        session.add(orange)
        session.commit()

        session.refresh(apple)
        session.refresh(orange)

def create_customers():
    with Session(engine) as session:
        customer_1 = Customer(first_name="nom1", last_name="cognom1")
        customer_2 = Customer(first_name="nom2", last_name="cognom2")

        session.add(customer_1)
        session.add(customer_2)
        session.commit()
        session.refresh(customer_1)
        session.refresh(customer_2)


def create_product_customer_link():
    with Session(engine) as session:
        purchase_1 = CustomerProductLink()

        session.add(purchase_1)
        session.commit()
        session.refresh(purchase_1)


def main():
    create_db_and_tables()

if __name__ == "__main__":
    main()