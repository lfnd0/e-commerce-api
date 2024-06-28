from flask import request, make_response, jsonify
from ..use_cases import make_create_product_use_case, make_list_products_use_case, make_fetch_product_by_id_use_case, make_remove_product_by_id_use_case, make_update_product_by_id_use_case

def create_product():
    product_data = request.json

    create_product_use_case = make_create_product_use_case()
    create_product_use_case.execute(product_data)

    return make_response("", 201)

def list_products():
    list_products_use_case = make_list_products_use_case()
    products = list_products_use_case.execute()

    return make_response(jsonify({ "products": products }), 200)

def fetch_product_by_id(product_id: int):
    fetch_product_by_id_use_case = make_fetch_product_by_id_use_case()
    product = fetch_product_by_id_use_case.execute(product_id)

    return make_response(jsonify({ "product": product }), 200)

def remove_product_by_id(product_id: int):
    remove_product_by_id_use_case = make_remove_product_by_id_use_case()
    remove_product_by_id_use_case.execute(product_id)

    return make_response("", 204)

def update_product_by_id(product_id: int):
    product_data = request.json

    update_product_by_id_use_case = make_update_product_by_id_use_case()
    update_product_by_id_use_case.execute(product_id, product_data)

    return make_response("", 204)
