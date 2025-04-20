from datetime import date
from typing import Optional

from sqlmodel import SQLModel, Field


# Relación N:M -> Clientes y Productos -> un cliente compra muchos productos, y un producto es comprado por muchos clientes.

# Customer

class CustomerBase(SQLModel):
    first_name: str
    last_name: str


class Customer(CustomerBase, table=True):
    customer_id: Optional[int] = Field(default=None, primary_key=True)


class CustomerPublic(CustomerBase):
    customer_id: int = Field(index=True, primary_key=True)


class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(SQLModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None


# Products

class ProductBase(SQLModel):
    product_name: str
    stock: int
    category: str
    price: float


class Product(ProductBase, table=True):
    product_id: Optional[int] = Field(default=None, primary_key=True)


class ProductPublic(ProductBase):
    product_id: int = Field(index=True, primary_key=True)


class ProductCreate(ProductBase):
    pass

class ProductUpdate(SQLModel):
    product_name: Optional[str] = None
    stock: Optional[int] = None
    category: Optional[str] = None
    price: Optional[float] = None


# Purchases

class PurchaseBase(SQLModel):
    customer_id: int = Field(foreign_key="customer.customer_id")
    product_id: int = Field(foreign_key="product.product_id")
    purchase_id: Optional[int] = Field(default=None, primary_key=True)
    purchase_date: date


class Purchase(PurchaseBase, table=True):
    pass


class PurchaseCreate(PurchaseBase):
    pass


class PurchasePublic(PurchaseBase):
    pass


class PurchaseUpdate(SQLModel):
    customer_id: Optional[int] = None
    product_id: Optional[int] = None
    purchase_date: Optional[date] = None








