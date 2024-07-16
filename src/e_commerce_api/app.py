import os
from flask import Flask
from flask_cors import CORS
from .database import DatabaseConfig


class _App:

    def __init__(self):
        self._secret_key = os.getenv("SECRET_KEY")
        self._database_uri = os.getenv("DATABASE_URI")
        self._host = os.getenv("HOST")

        self._app = Flask(__name__)
        self._app.config["SECRET_KEY"] = self._secret_key

        self._database_config = DatabaseConfig(self._app, self._database_uri)
        self._db = self._database_config.get_db()
        self._ma = self._database_config.get_ma()

        CORS(self._app)

    def get_app(self):
        return self._app

    def get_db(self):
        return self._db

    def get_ma(self):
        return self._ma

    def run(self):
        self._app.run(debug=True, host=self._host)


app_module = _App()

app = app_module.get_app()
db = app_module.get_db()
ma = app_module.get_ma()
