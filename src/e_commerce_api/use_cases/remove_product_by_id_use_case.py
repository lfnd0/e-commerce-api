from ..repositories import ProductRepository

class RemoveProductByIdUseCase:

    def __init__(self, products_repository: ProductRepository):
        self.products_repository = products_repository

    def execute(self, product_id: int):
        return self.products_repository.remove_product_by_id(product_id)
