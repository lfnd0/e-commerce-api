from .root_route import get_root
from .product_route import (
    product_blueprint,
    post_product,
    get_products,
    get_product_by_id,
    delete_product_by_id,
    patch_product_by_id,
)
from .user_route import user_blueprint, post_user, login, logout
from .cart_route import cart_blueprint, post_cart
