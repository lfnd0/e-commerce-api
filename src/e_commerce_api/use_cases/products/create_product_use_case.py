from ...repositories import ProductRepository
from ...models import Product

class CreateProductUseCase:

    def __init__(self, products_repository: ProductRepository):
        self.products_repository = products_repository

    def execute(self, product_data: dict):
        new_product = Product(
            name=product_data["name"],
            price=product_data["price"],
            description=product_data.get("description", None)
        )

        self.products_repository.create_product(new_product)
