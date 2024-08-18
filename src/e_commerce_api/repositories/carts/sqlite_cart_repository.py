from e_commerce_api import db
from e_commerce_api.models import CartSchema
from .cart_repository import CartRepository
from ...models import Cart, cart_schema


class SqliteCartRepository(CartRepository):

    def create_cart(self, cart_data: Cart) -> None:
        db.session.add(cart_data)
        db.session.commit()

    def fetch_cart_by_id(self, cart_id: int) -> CartSchema:
        cart = Cart.query.get_or_404(cart_id)
        return cart_schema.dump(cart)
