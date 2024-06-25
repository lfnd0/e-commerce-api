from flask import Blueprint
from .app import app, main, set_blueprint
from .database import db
from .routes import product_blueprint, get_root, post_product, get_products, get_product_by_id, delete_product_by_id, patch_product_by_id
from .models import Product

app.register_blueprint(product_blueprint, url_prefix='/api/products')
