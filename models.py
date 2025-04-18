from datetime import date
from typing import Optional

from sqlmodel import SQLModel, Field


# Relación N:M -> Clientes y Productos -> un cliente compra muchos productos, y un producto es comprado por muchos clientes.

class CustomerBase(SQLModel):
    first_name: str
    last_name: str


class ProductBase(SQLModel):
    product_name: str
    stock: int
    category: str
    price: float


class CustomerProductLinkBase(SQLModel):
    purchase_date: date


class Customer(CustomerBase, table=True):
    customer_id: Optional[int] = Field(default=None, primary_key=True)


class Product(ProductBase, table=True):
    product_id: Optional[int] = Field(default=None, primary_key=True)


class CustomerProductLink(CustomerProductLinkBase, table=True):
    customer_id: Optional[int] = Field(foreign_key="customer.customer_id", primary_key=True)
    product_id: Optional[int] = Field(foreign_key="product.product_id", primary_key=True)


class CustomerPublic(CustomerBase):
    customer_id: int = Field(index=True, primary_key=True)


class ProductPublic(ProductBase):
    product_id: int = Field(index=True, primary_key=True)


class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(SQLModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None

class ProductCreate(ProductBase):
    pass

class ProductUpdate(SQLModel):
    product_name: Optional[str] = None
    stock: Optional[int] = None
    category: Optional[str] = None
    price: Optional[float] = None