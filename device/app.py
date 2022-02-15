import os
from flask import Flask, jsonify, abort, request
from flask_cors import CORS
from flask_mongoengine import MongoEngine

db = "patient-monitor"
db_pass = os.environ["db_pass"]
URI = "mongodb+srv://khoa:{db_pass}@cluster0.bfh4g.mongodb.net/{db}?retryWrites=true&w=majority"
db.connect(URI)
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
    app.run(debug=True)