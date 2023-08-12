from session import Session
from table_models import Product, Order


class TableRepository:
    def __init__(self):
        self.__session = Session()
        self.__session.autocommit = True

    def get_all(self, cls):
        result = (
            self.__session.query(cls).all()
        )
        return result

    def insert_one(self, value):
        self.__session.add(value)

    def insert_many(self, values: list):
        self.__session.add_all(values)

    def insert_data_into_table(self, data, table):
        for element in data:
            self.__session.add(table(**element))

    def get_products_with_orders(self):
        result = (
            self.__session.query(Product.name, Product.price, Order.quantity,
                                 (Product.price * Order.quantity).label('total_price'))
            .join(Order, Product.id == Order.product_id)
            .all()
        )
        return result
