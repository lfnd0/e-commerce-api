from ...repositories import ProductRepository

class ListProductsUseCase:

    def __init__(self, products_repository: ProductRepository):
        self.products_repository = products_repository

    def execute(self):
        return self.products_repository.list_products()
