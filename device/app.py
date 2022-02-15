import os
from flask import Flask, jsonify, abort, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/device', methods=["POST"])
def add_device():
    body = request.get_json()
    return jsonify(body), 201

@app.route('/', methods=["GET"])
def home():
    return "hello world\n"

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")