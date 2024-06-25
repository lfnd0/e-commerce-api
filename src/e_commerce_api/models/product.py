from ..database import db, ma
from datetime import datetime

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, nullable=True)

class ProductSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "price", "description", "created_at", "updated_at")

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
