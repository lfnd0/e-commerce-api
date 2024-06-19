from flask import Flask

app = Flask(__name__)

def main():
    app.run(debug=True, host="0.0.0.0")
