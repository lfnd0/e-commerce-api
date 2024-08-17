from typing import Dict
from ...repositories import ProductRepository, CartRepository
from ...models import Cart, ProductInCart


class CreateCartUseCase:

    def __init__(
        self, products_repository: ProductRepository, carts_repository: CartRepository
    ):
        self.products_repository = products_repository
        self.carts_repository = carts_repository

    def execute(self, cart_data: Dict):
        total = 0
        new_cart = Cart(client_id=cart_data["client_id"], total=total)

        products = cart_data["products"]
        for item in products:
            product_id = item["product_id"]
            product_quantity = item["product_quantity"]

            product = self.products_repository.fetch_product_by_id_no_schema(product_id)

            new_product_in_cart = ProductInCart(
                product_id=product_id, product_quantity=product_quantity
            )
            new_cart.products_in_cart.append(new_product_in_cart)

            total += product.price * product_quantity

        new_cart.total = (total * 100) / 100

        self.carts_repository.create_cart(new_cart)
