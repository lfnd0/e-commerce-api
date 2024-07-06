from ..database import db, ma
from datetime import datetime
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password_hash = db.Column(db.String(100), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, nullable=True)

class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "username")

user_schema = UserSchema()
users_schema = UserSchema(many=True)
