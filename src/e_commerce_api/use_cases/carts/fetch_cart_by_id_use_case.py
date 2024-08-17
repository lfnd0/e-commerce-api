from typing import Dict
from ...repositories import CartRepository
from ...models import Cart


class FetchCartByIdUseCase:

    def __init__(self, carts_repository: CartRepository):
        self.carts_repository = carts_repository

    def execute(self, cart_id: int):
        return self.carts_repository.fetch_cart_by_id(cart_id)
