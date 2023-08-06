from session import Session
from session import engine
from table_models import Base
from table_models import Product, Order
from table_repository import TableRepository

if __name__ == "__main__":
    orders_data = [
        {'product_id': 1, 'quantity': 1},
        {'product_id': 2, 'quantity': 2},
        {'product_id': 3, 'quantity': 3},
        {'product_id': 4, 'quantity': 4},
        {'product_id': 5, 'quantity': 5},
    ]
    products_data = [
        {'name': 'Product 1', 'price': 1},
        {'name': 'Product 2', 'price': 2},
        {'name': 'Product 3', 'price': 3},
        {'name': 'Product 4', 'price': 4},
        {'name': 'Product 5', 'price': 5},
    ]
    table_repo = TableRepository()
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    table_repo.insert_data_into_table(products_data, Product)
    table_repo.insert_data_into_table(orders_data, Order)
    table_repo.insert_one(Product(name='Product 6', price=6))
    table_repo.insert_one(Order(product_id=6, quantity=6))

    products_with_orders = table_repo.get_products_with_orders()
    for row in products_with_orders:
        print(row)

    products = table_repo.get_all(Product)
    for row in products:
        print(row)

    order = table_repo.get_all(Order)
    for row in order:
        print(row)
