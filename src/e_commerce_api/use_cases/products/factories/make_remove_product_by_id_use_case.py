from .. import RemoveProductByIdUseCase
from ....repositories import SQLiteProductRepository

def make_remove_product_by_id_use_case():
    sqlite_product_repository = SQLiteProductRepository()
    remove_product_by_id_use_case = RemoveProductByIdUseCase(sqlite_product_repository)

    return remove_product_by_id_use_case
