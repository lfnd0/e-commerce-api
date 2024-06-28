from .. import UpdateProductByIdUseCase
from ....repositories import SQLiteProductRepository

def make_update_product_by_id_use_case():
    sqlite_product_repository = SQLiteProductRepository()
    update_product_by_id_use_case = UpdateProductByIdUseCase(sqlite_product_repository)

    return update_product_by_id_use_case
