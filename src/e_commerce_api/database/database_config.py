from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


class DatabaseConfig:

    def __init__(self, app: Flask, database_uri: str):
        app.config["SQLALCHEMY_DATABASE_URI"] = database_uri
        self._db = SQLAlchemy(app)
        self._ma = Marshmallow(app)

    def get_db(self):
        return self._db

    def get_ma(self):
        return self._ma
