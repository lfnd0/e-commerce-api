from flask import request, make_response, jsonify
from flask_login import current_user
from ..use_cases import make_create_cart_use_case, make_fetch_cart_by_id_use_case


def create_cart():
    cart_data = request.json
    cart_data["client_id"] = current_user.id

    create_cart_use_case = make_create_cart_use_case()
    create_cart_use_case.execute(cart_data)

    return make_response("", 201)


def fetch_cart_by_id(cart_id: int):
    fetch_cart_by_id_use_case = make_fetch_cart_by_id_use_case()
    cart = fetch_cart_by_id_use_case.execute(cart_id)

    return make_response(jsonify({"cart": cart}), 200)
