from flask import request, make_response
from flask_login import login_user, logout_user
from ..use_cases import make_create_user_use_case, make_authenticate_user_use_case


def create_user():
    user_data = request.json

    create_user_use_case = make_create_user_use_case()
    create_user_use_case.execute(user_data)

    return make_response("", 201)


def authenticate_user():
    user_data = request.json

    authenticate_user_use_case = make_authenticate_user_use_case()
    authenticated_user = authenticate_user_use_case.execute(user_data)

    login_user(user=authenticated_user)

    return make_response("", 200)


def revoke_user_authentication():
    logout_user()

    return make_response("", 204)
