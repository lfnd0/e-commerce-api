from flask import Flask, Blueprint

app = Flask(__name__)

def set_blueprint(blueprint_name: str):
    return Blueprint(blueprint_name, __name__)

def main():
    app.run(debug=True, host="0.0.0.0")
