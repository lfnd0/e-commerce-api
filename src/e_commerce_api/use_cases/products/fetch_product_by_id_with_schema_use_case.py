from ...repositories import ProductRepository


class FetchProductByIdWithSchemaUseCase:

    def __init__(self, products_repository: ProductRepository):
        self.products_repository = products_repository

    def execute(self, product_id: int):
        return self.products_repository.fetch_product_by_id_with_schema(product_id)
