from typing import Optional

from sqlmodel import SQLModel, Field, Relationship


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
    customer_id: Optional[int] = Field(foreign_key="customer.customer_id", primary_key=True)
    product_id: Optional[int] = Field(foreign_key="product.product_id", primary_key=True)
    purchase_date: str


class Customer(CustomerBase, table=True):
    customer_id: Optional[int] = Field(default=None, primary_key=True)


class Product(ProductBase, table=True):
    product_id: Optional[int] = Field(default=None, primary_key=True)


class CustomerProductLink(CustomerProductLinkBase, table=True):
    customer: Optional[Customer] = Relationship(back_populates="")
    product: Optional[Product] = Field(default=None, primary_key=True)


class CustomerPublic(CustomerBase):
    cutomer_id: int = Field(index=True, primary_key=True)


class ProductPublic(ProductBase):
    product_id: int = Field(index=True, primary_key=True)
