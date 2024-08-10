from datetime import datetime
from e_commerce_api import db, ma
from .user import UserSchema
from .product_in_cart import ProductInCartSchema


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    total = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, nullable=True)
    client_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    client = db.relationship("User", backref=db.backref("carts", lazy="select"))
    products_in_cart = db.relationship(
        "ProductInCart", backref=db.backref("cart", lazy="select")
    )


class CartSchema(ma.Schema):
    client = ma.Nested(UserSchema)
    products_in_cart = ma.List(ma.Nested(ProductInCartSchema))

    class Meta:
        fields = (
            "id",
            "total",
            "created_at",
            "updated_at",
            "client",
            "products_in_cart",
        )


cart_schema = CartSchema()
carts_schema = CartSchema(many=True)
