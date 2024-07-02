from typing import List
from . import ProductRepository
from ...models import Product, ProductSchema, products_schema, product_schema
from ...database import db

class SQLiteProductRepository(ProductRepository):

    def create_product(self, product_data: Product):
        db.session.add(product_data)
        db.session.commit()

    def list_products(self) -> List[ProductSchema]:
        products = Product.query.all()
        return products_schema.dump(products)

    def fetch_product_by_id(self, product_id: int) -> ProductSchema:
        product = Product.query.get_or_404(product_id)
        return product_schema.dump(product)

    def remove_product_by_id(self, product: Product) -> None:
        db.session.delete(product)
        db.session.commit()

    def update_product_by_id(self, product: Product) -> None:
        db.session.commit()

    def fetch_product_by_id_no_schema(self, product_id: int) -> Product:
        product = Product.query.get_or_404(product_id)
        return product
