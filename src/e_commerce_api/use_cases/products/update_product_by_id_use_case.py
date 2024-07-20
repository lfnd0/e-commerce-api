from typing import Dict
from datetime import datetime
from ...repositories import ProductRepository


class UpdateProductByIdUseCase:

    def __init__(self, products_repository: ProductRepository):
        self.products_repository = products_repository

    def execute(self, product_id: int, product_data: Dict):
        allowed_fields = ["name", "price", "description"]

        update_product = {
            field: value
            for field, value in product_data.items()
            if field in allowed_fields
        }
        update_product["updated_at"] = datetime.now()

        self.products_repository.update_product_by_id(product_id, update_product)
