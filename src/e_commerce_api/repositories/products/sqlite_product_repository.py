from typing import List, Dict
from e_commerce_api import db
from .product_repository import ProductRepository
from ...models import Product, ProductSchema, products_schema, product_schema


class SQLiteProductRepository(ProductRepository):

    def create_product(self, product_data: Product):
        db.session.add(product_data)
        db.session.commit()

    def list_products(self) -> List[ProductSchema]:
        products = Product.query.all()
        return products_schema.dump(products)

    def fetch_product_by_id_with_schema(self, product_id: int) -> ProductSchema:
        product = Product.query.get_or_404(product_id)
        return product_schema.dump(product)

    def remove_product_by_id(self, product_id: int) -> None:
        Product.query.filter(Product.id == product_id).delete()
        db.session.commit()

    def update_product_by_id(self, product_id: int, product: Dict) -> None:
        Product.query.filter(Product.id == product_id).update(product)
        db.session.commit()

    def fetch_product_by_id_no_schema(self, product_id: int) -> Product:
        product = Product.query.get_or_404(product_id)
        return product

    def list_products_by_owner_id(self, owner_id: int) -> List[ProductSchema]:
        products = Product.query.filter(Product.owner_id == owner_id)
        return products
