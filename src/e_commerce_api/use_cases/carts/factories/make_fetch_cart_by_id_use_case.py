from .. import FetchCartByIdUseCase
from ....repositories import SqliteCartRepository


def make_fetch_cart_by_id_use_case():
    sqlite_cart_repository = SqliteCartRepository()
    create_cart_use_case = FetchCartByIdUseCase(sqlite_cart_repository)

    return create_cart_use_case
