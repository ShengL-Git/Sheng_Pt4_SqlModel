import requests

customers_url = "http://localhost:8000/customers"
products_url = "http://localhost:8000/products"
purchases_url = "http://localhost:8000/purchases"


# ADDITIONAL ENDPOINTS

def order_customer_by_purchases():
    data = requests.get(f"{customers_url}/most_purchases")
    print(data.status_code)
    for customer in data.json():
        print(customer)


def order_products_by_price():
    data = requests.get(f"{products_url}/order_by_price")
    print(data.status_code)
    for product in data.json():
        print(product)


def num_purchases_by_costumer(customer_id: int):
    data = requests.get(f"{purchases_url}/customer/{customer_id}")
    print(data.status_code)
    for purchase in data.json():
        print(purchase)


def num_purchases_by_product(product_id: int):
    data = requests.get(f"{purchases_url}/product/{product_id}")
    print(data.status_code)
    for purchase in data.json():
        print(purchase)


def products_out_of_stock():
    data = requests.get(f"{products_url}/out_of_stock").json()
    for product in data:
        print(product)


# Customers

def create_customer(customer: dict):
    data = requests.post(f"{customers_url}", json=customer)
    print(data.status_code)
    print(data.json())


def read_customers():
    data = requests.get(f"{customers_url}")
    print(data.status_code)
    for customer in data:
        print(customer)


def read_customer(customer_id: int):
    data = requests.get(f"{customers_url}/{customer_id}")
    print(data.status_code)
    print(data.json())


def update_customer(customer_id:int, new_customer: dict):
    data = requests.patch(f"{customers_url}/{customer_id}", json=new_customer)
    print(data.status_code)


def delete_customer(customer_id:int):
    data = requests.delete(f"{customers_url}/{customer_id}")
    print(data.status_code)

# Products


def create_product(product: dict):
    data = requests.post(f"{products_url}", json=product)
    print(data.status_code)
    print(data.json())


def read_products():
    data = requests.get(f"{products_url}")
    print(data.status_code)
    for product in data:
        print(product)


def read_product(product_id: int):
    data = requests.get(f"{products_url}/{product_id}")
    print(data.status_code)
    print(data.json())


def update_product(product_id:int, new_product: dict):
    data = requests.patch(f"{products_url}/{product_id}", json=new_product)
    print(data.status_code)


def delete_product(product_id:int):
    data = requests.delete(f"{products_url}/{product_id}")
    print(data.status_code)


# Purchases

def create_purchase(purchase: dict):
    data = requests.post(f"{purchases_url}", json=purchase)
    print(data.status_code)
    print(data.json())


def read_purchases():
    data = requests.get(f"{purchases_url}")
    print(data.status_code)
    for purchase in data:
        print(purchase)


def read_purchase(purchase_id: int):
    data = requests.get(f"{purchases_url}/{purchase_id}")
    print(data.status_code)
    print(data.json())


def update_purchase(purchase_id:int, new_purchase: dict):
    data = requests.patch(f"{purchases_url}/{purchase_id}", json=new_purchase)
    print(data.status_code)


def delete_purchase(purchase_id:int):
    data = requests.delete(f"{purchases_url}/{purchase_id}")
    print(data.status_code)

def main():
    delete_customer(5)

if __name__ == "__main__":
    main()
