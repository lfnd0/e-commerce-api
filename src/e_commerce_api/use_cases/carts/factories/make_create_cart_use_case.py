from .. import CreateCartUseCase
from ....repositories import SQLiteProductRepository, SqliteCartRepository


def make_create_cart_use_case():
    sqlite_product_repository = SQLiteProductRepository()
    sqlite_cart_repository = SqliteCartRepository()
    create_cart_use_case = CreateCartUseCase(
        sqlite_product_repository, sqlite_cart_repository
    )

    return create_cart_use_case
