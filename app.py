import os
from flask import Flask, jsonify, abort, request
from flask_cors import CORS
from mongoengine import connect
from device.device_utilities import make_device_obj

#cloud database name
db_name = "patient-monitor"

#obtain user password stored in environment
db_pass = os.environ["db_pass"]

#databse URI
URI = "mongodb+srv://khoa:{}@cluster0.bfh4g.mongodb.net/{}?retryWrites=true&w=majority".format(db_pass, db_name)

#connect database
db = connect(host=URI)

#start Flask app
app = Flask(__name__)
CORS(app)

@app.route('/add-device', methods=["POST"])
def add_device():
    body = request.json
    device = make_device_obj(body)
    device.save()
    return jsonify(body), 201

@app.route('/', methods=["GET"])
def home():
    return "hello world\n"

if __name__ == '__main__':
    app.run(debug=True)