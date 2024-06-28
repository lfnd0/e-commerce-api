from typing import List
from datetime import datetime
from . import ProductRepository
from ...models import Product, products_schema, product_schema
from ...database import db

class SQLiteProductRepository(ProductRepository):

    def create_product(self, product_data: dict):
        new_product = Product(
            name=product_data["name"],
            price=product_data["price"],
            description=product_data.get("description", None)
        )

        db.session.add(new_product)
        db.session.commit()

    def list_products(self) -> List[Product]:
        products = Product.query.all()
        return products_schema.dump(products)

    def fetch_product_by_id(self, product_id: int) -> Product:
        product = Product.query.get_or_404(product_id)
        return product_schema.dump(product)

    def remove_product_by_id(self, product_id: int) -> None:
        product = Product.query.get_or_404(product_id)

        db.session.delete(product)
        db.session.commit()

    def update_product_by_id(self, product_id: int, product_data: dict) -> None:
        product = Product.query.get_or_404(product_id)

        product.name = product_data.get("name", product.name)
        product.price = product_data.get("price", product.price)
        product.description = product_data.get("description", product.description)
        product.updated_at = datetime.now()

        db.session.commit()
