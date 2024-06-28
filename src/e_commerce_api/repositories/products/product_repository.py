from abc import ABC, abstractmethod
from typing import List
from ...models import Product

class ProductRepository(ABC):

    @abstractmethod
    def create_product(self, product_data: dict) -> None:
        pass

    @abstractmethod
    def list_products(self) -> List[Product]:
        pass

    @abstractmethod
    def fetch_product_by_id(self, product_id: int) -> Product:
        pass

    @abstractmethod
    def remove_product_by_id(self, product_id: int) -> None:
        pass

    @abstractmethod
    def update_product_by_id(self, product_id: int, product_data: dict) -> None:
        pass
