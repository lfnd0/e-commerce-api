from datetime import datetime
from ...repositories import ProductRepository

class UpdateProductByIdUseCase:

    def __init__(self, products_repository: ProductRepository):
        self.products_repository = products_repository

    def execute(self, product_id: int, product_data: dict):
        product = self.products_repository.fetch_product_by_id_no_schema(product_id)

        product.name = product_data.get("name", product.name)
        product.price = product_data.get("price", product.price)
        product.description = product_data.get("description", product.description)
        product.updated_at = datetime.now()

        self.products_repository.update_product_by_id(product)
