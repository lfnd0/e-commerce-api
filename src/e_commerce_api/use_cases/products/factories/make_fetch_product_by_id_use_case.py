from .. import FetchProductByIdUseCase
from ....repositories import SQLiteProductRepository

def make_fetch_product_by_id_use_case():
    sqlite_product_repository = SQLiteProductRepository()
    fetch_product_by_id_use_case = FetchProductByIdUseCase(sqlite_product_repository)

    return fetch_product_by_id_use_case
