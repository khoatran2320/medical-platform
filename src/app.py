import os
import logging 
from flask import Flask, Blueprint, redirect
from flask_restx import Api
from flask_cors import CORS
from mongoengine import connect
from controllers.appV1 import blueprint as api1

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
app.register_blueprint(api1)
CORS(app)

@app.route('/', methods=["GET"])
def home():
    return redirect('/api/1/doc')

if __name__ == '__main__':
    app.run(debug=True)