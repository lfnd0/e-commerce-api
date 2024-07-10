from datetime import datetime
from ..database import db, ma
from .user import UserSchema


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)
    owner_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, nullable=True)

    owner = db.relationship("User", backref=db.backref("products", lazy=True))


class ProductSchema(ma.Schema):
    owner = ma.Nested(UserSchema)

    class Meta:
        fields = (
            "id",
            "name",
            "price",
            "description",
            "owner_id",
            "created_at",
            "updated_at",
            "owner",
        )


product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
