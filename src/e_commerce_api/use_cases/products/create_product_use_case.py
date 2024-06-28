from ...repositories import ProductRepository

class CreateProductUseCase:

    def __init__(self, products_respository: ProductRepository):
        self.products_respository = products_respository

    def execute(self, product_data: dict):
        self.products_respository.create_product(product_data)
