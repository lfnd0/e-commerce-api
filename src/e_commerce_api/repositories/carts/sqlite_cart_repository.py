from e_commerce_api import db
from e_commerce_api.models import CartSchema
from .cart_repository import CartRepository
from ...models import Cart, cart_schema


class SqliteCartRepository(CartRepository):

    def create_cart(self, cart_data: Cart) -> None:
        # pass
        db.session.add(cart_data)
        db.session.commit()

        # cart_id = cart_data.id

        # cart_product_mappings_data = [
        #     {
        #         "cart_id": cart_id,
        #         "product_id": item["product_id"],
        #         "product_quantity": item["product_quantity"],
        #     }
        #     for item in product_in_cart
        # ]

        # db.session.execute(cart_product.insert(), cart_product_mappings_data)
        # db.session.commit()

    def fetch_cart_by_id(self, cart_id: int) -> CartSchema:
        cart = Cart.query.get_or_404(cart_id)
        return cart_schema.dump(cart)
