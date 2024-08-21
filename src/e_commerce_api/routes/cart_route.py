from flask import Blueprint
from flask_login import login_required
from e_commerce_api import app
from ..controllers import create_cart, fetch_cart_by_id

cart_blueprint = Blueprint("cart_blueprint", __name__)


@cart_blueprint.route("/", methods=["POST"])
@login_required
def post_cart():
    return create_cart()


@cart_blueprint.route("/<int:cart_id>/details", methods=["GET"])
def get_cart_by_id(cart_id: int):
    return fetch_cart_by_id(cart_id)


app.register_blueprint(cart_blueprint, url_prefix="/api/carts")
