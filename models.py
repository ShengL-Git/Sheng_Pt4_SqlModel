from typing import Optional

from sqlmodel import SQLModel, Field

# Relación N:M -> Clientes y Productos -> un cliente compra muchos productos, y un producto es comprado por muchos clientes.

class CustomerBase(SQLModel):
    cutomer_id: int = Field(index=True, primary_key= True)
    first_name: str
    last_name: str


class ProductBase(SQLModel):
    product_id: int = Field(index=True, primary_key= True)
    product_name: str
    stock: int
    category: str

class CustomerProductLink(SQLModel):
    customer_id: Optional[int] = Field(foreign_key= "customer.id", primary_key= True)
    product_id: Optional[int] = Field(foreign_key= "product.id", primary_key= True)

class CustomerCreate(CustomerBase, table = True):
    pass

class ProductCreate(ProductBase, table = True):
    pass





