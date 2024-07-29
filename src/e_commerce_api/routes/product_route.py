from flask import Blueprint
from flask_login import login_required
from e_commerce_api import app
from ..controllers import (
    create_product,
    list_products,
    fetch_product_by_id_with_schema,
    remove_product_by_id,
    update_product_by_id,
)

product_blueprint = Blueprint("product_blueprint", __name__)


@product_blueprint.route("/", methods=["POST"])
@login_required
def post_product():
    return create_product()


@product_blueprint.route("/", methods=["GET"])
@login_required
def get_products():
    return list_products()


@product_blueprint.route("/<int:product_id>/details", methods=["GET"])
@login_required
def get_product_by_id(product_id: int):
    return fetch_product_by_id_with_schema(product_id)


@product_blueprint.route("/<int:product_id>", methods=["DELETE"])
@login_required
def delete_product_by_id(product_id: int):
    return remove_product_by_id(product_id)


@product_blueprint.route("/<int:product_id>", methods=["PATCH"])
@login_required
def patch_product_by_id(product_id: int):
    return update_product_by_id(product_id)


app.register_blueprint(product_blueprint, url_prefix="/api/products")
