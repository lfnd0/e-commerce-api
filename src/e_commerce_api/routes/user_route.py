from flask import Blueprint
from flask_login import LoginManager, login_required
from e_commerce_api import app
from ..models import User
from ..controllers import create_user, authenticate_user, revoke_user_authentication

login_manager = LoginManager()
login_manager.init_app(app)

user_blueprint = Blueprint("user_blueprint", __name__)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@user_blueprint.route("/", methods=["POST"])
def post_user():
    return create_user()


@user_blueprint.route("/login", methods=["POST"])
def login():
    return authenticate_user()


@user_blueprint.route("/logout", methods=["POST"])
@login_required
def logout():
    return revoke_user_authentication()


app.register_blueprint(user_blueprint, url_prefix="/api/users")
