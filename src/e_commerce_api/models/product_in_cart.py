from e_commerce_api import db, ma
from .product import ProductSchema


class ProductInCart(db.Model):
    product_quantity = db.Column(db.Integer, nullable=False)
    cart_id = db.Column(db.Integer, db.ForeignKey("cart.id"), primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"), primary_key=True)

    product = db.relationship("Product", backref=db.backref("carts", lazy="select"))


class ProductInCartSchema(ma.Schema):
    product = ma.Nested(ProductSchema)
    product_quantity = ma.Integer()

    class Meta:
        fields = ("product", "product_quantity")


product_in_cart_schema = ProductInCartSchema()
product_in_carts_schema = ProductInCartSchema(many=True)
