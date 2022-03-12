import os
import logging 
from flask import Flask, jsonify, abort, request
from flask_cors import CORS
from mongoengine import connect
from .device.device_utilities import make_device_obj
from .user.user_utilities import make_user_obj
from .Models.Device import Device


"""
logging config
"""
logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s -%(levelname)s -%(message)s")

"""
database startup
"""
#cloud database name
db_name = "patient-monitor"

#obtain user password stored in environment
db_pass = os.environ["db_pass"]

#databse URI
URI = "mongodb+srv://khoa:{}@cluster0.bfh4g.mongodb.net/{}?retryWrites=true&w=majority".format(db_pass, db_name)

#connect database
db = connect(host=URI)


logging.info("Database connected")

"""
Flask startup
"""
#start Flask app
app = Flask(__name__)
CORS(app)

@app.route('/add-device', methods=["POST"])
def add_device():
    retrieved_device = Device.objects
    print(retrieved_device)
    body = request.json
    try:
        device = make_device_obj(body)
        device.save()
        return "success!", 200
    except Exception as e:
        return "Invalid device fields", 400

@app.route('/add-user', methods=["POST"])
def add_user():
    body = request.json
    try:
        user = make_user_obj(body)
        user.save()
    except Exception as e:
        print(e)
        return "Invalid user fields"
    return "success!", 200

@app.route('/', methods=["GET"])
def home():
    return "hello world"

if __name__ == '__main__':
    app.run(debug=True)