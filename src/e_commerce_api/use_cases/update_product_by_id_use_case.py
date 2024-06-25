from ..repositories import ProductRepository

class UpdateProductByIdUseCase:

    def __init__(self, products_respository: ProductRepository):
        self.products_respository = products_respository

    def execute(self, product_id: int, product_data: dict):
        self.products_respository.update_product_by_id(product_id, product_data)
