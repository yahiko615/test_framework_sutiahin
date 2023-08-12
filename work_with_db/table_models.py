from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from base_model import Base


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)

    def __str__(self):
        return f'id:{self.id}\tname: {self.name}\tprice: {self.price}'


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)

    product = relationship('Product')

    def __str__(self):
        return f'id:{self.id}\tproduct_id: {self.product_id}\tquantity: {self.quantity}'
