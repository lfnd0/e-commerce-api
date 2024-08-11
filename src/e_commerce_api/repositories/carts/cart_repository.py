from abc import ABC, abstractmethod
from ...models import Cart, CartSchema


class CartRepository(ABC):

    @abstractmethod
    def create_cart(self, cart_data: Cart) -> None:
        pass

    @abstractmethod
    def fetch_cart_by_id(self, cart_id: int) -> CartSchema:
        pass
