from .. import CreateProductUseCase
from ...repositories import SQLiteProductRepository

def make_create_product_use_case():
    sqlite_product_repository = SQLiteProductRepository()
    create_product_use_case = CreateProductUseCase(sqlite_product_repository)

    return create_product_use_case
