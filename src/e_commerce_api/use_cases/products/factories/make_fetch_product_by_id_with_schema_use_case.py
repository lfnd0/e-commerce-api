from .. import FetchProductByIdWithSchemaUseCase
from ....repositories import SQLiteProductRepository


def make_fetch_product_by_id_with_schema_use_case():
    sqlite_product_repository = SQLiteProductRepository()
    fetch_product_by_id_with_schema_use_case = FetchProductByIdWithSchemaUseCase(
        sqlite_product_repository
    )

    return fetch_product_by_id_with_schema_use_case
