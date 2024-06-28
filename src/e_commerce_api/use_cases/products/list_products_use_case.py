from ...repositories import ProductRepository

class ListProductsUseCase:

    def __init__(self, products_respository: ProductRepository):
        self.products_respository = products_respository

    def execute(self):
        return self.products_respository.list_products()
