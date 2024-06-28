from .. import ListProductsUseCase
from ....repositories import SQLiteProductRepository

def make_list_products_use_case():
    sqlite_product_repository = SQLiteProductRepository()
    list_products_use_case = ListProductsUseCase(sqlite_product_repository)

    return list_products_use_case
