from abc import ABC, abstractmethod
from typing import List, Dict
from ...models import Product, ProductSchema


class ProductRepository(ABC):

    @abstractmethod
    def create_product(self, product_data: Product) -> None:
        pass

    @abstractmethod
    def list_products(self) -> List[ProductSchema]:
        pass

    @abstractmethod
    def fetch_product_by_id_with_schema(self, product_id: int) -> ProductSchema:
        pass

    @abstractmethod
    def remove_product_by_id(self, product_id: int) -> None:
        pass

    @abstractmethod
    def update_product_by_id(self, product_id: int, product: Dict) -> None:
        pass

    @abstractmethod
    def fetch_product_by_id_no_schema(self, product_id: int) -> Product:
        pass

    @abstractmethod
    def list_products_by_owner_id(self, owner_id: int) -> List[ProductSchema]:
        pass
