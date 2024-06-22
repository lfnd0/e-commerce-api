from flask import jsonify

def read_root():
    return jsonify({ "message": "Welcome to E-Commerce API" }), 200
