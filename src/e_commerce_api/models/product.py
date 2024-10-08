from datetime import datetime
from e_commerce_api import db, ma
from .user import UserSchema


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, nullable=True)
    owner_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    owner = db.relationship("User", backref=db.backref("products", lazy="select"))


class ProductSchema(ma.Schema):
    owner = ma.Nested(UserSchema)

    class Meta:
        fields = (
            "id",
            "name",
            "price",
            "description",
            "created_at",
            "updated_at",
            "owner",
        )


product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
