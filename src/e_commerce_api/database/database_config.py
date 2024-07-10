from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from e_commerce_api import app

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ecommerce.db"

db = SQLAlchemy(app)
ma = Marshmallow(app)
