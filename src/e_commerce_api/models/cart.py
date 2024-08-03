from datetime import datetime
from e_commerce_api import db, ma
from .product import ProductSchema

cart_product = db.Table(
    "cart_product",
    db.Column("cart_id", db.Integer, db.ForeignKey("cart.id"), primary_key=True),
    db.Column("product_id", db.Integer, db.ForeignKey("product.id"), primary_key=True),
    db.Column("product_quantity", db.Integer, nullable=False),
)


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, nullable=True)

    products = db.relationship(
        "Product", secondary=cart_product, backref=db.backref("carts", lazy="select")
    )


class CartSchema(ma.Schema):
    products = ma.Nested(ProductSchema)

    class Meta:
        fields = ("id", "created_at", "updated_at", "products")


cart_schema = CartSchema()
carts_schema = CartSchema(many=True)
