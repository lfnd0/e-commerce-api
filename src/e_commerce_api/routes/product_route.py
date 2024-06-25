from e_commerce_api import set_blueprint
from ..controllers import create_product, list_products, fetch_product_by_id, remove_product_by_id, update_product_by_id

product_blueprint = set_blueprint("product_blueprint")

@product_blueprint.route("/", methods=["POST"])
def post_product():
    return create_product()

@product_blueprint.route("/", methods=["GET"])
def get_products():
    return list_products()

@product_blueprint.route("/<int:product_id>/details", methods=["GET"])
def get_product_by_id(product_id: int):
    return fetch_product_by_id(product_id)

@product_blueprint.route("/<int:product_id>", methods=["DELETE"])
def delete_product_by_id(product_id: int):
    return remove_product_by_id(product_id)

@product_blueprint.route("/<int:product_id>", methods=["PATCH"])
def patch_product_by_id(product_id: int):
    return update_product_by_id(product_id)
