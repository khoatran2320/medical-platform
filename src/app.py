from asyncio import tasks
import os
import logging 
from flask import Flask, Blueprint, redirect, request
from flask_restx import Api
from flask_cors import CORS
from mongoengine import connect
from celery import Celery
from .controllers.appV1 import blueprint as api1
from .Response import Response

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

worker = Celery('speech_2_text_tasks',
                    broker='amqp://admin:mypass@rabbit:5672',
                    backend='mongodb://mongodb_container:27017/mydb')

@app.route('/speech-2-text/start', methods=["POST"])
def speech_2_text():
    audioFile = None
    try:
        audioFile = request.files['file']
    except:
        return Response("No file detected", status=400)
    
    if audioFile.filename == "":
        return Response("Invalid name", statud=400)
    audioFile.save("speech_to_text/"+audioFile.filename)
    print("WORKING")
    r = worker.send_task('task.speech_2_text', kwargs={'afile': audioFile.filename})
    return Response(r.id, status=200)

@app.route('/speech-2-text/status/<task_id>')
def status(task_id):
    status = worker.AsyncResult(task_id, app=worker)

    return Response({'status': str(status.state)}, status=200)

@app.route('/speech-2-text/result/<task_id>')
def result(task_id):
    result = worker.AsyncResult(task_id).result
    print(result)
    return Response({'result': str(result)}, status=200)


@app.route('/', methods=["GET"])
def home():
    return redirect('/api/1/doc')

if __name__ == '__main__':
    app.run(debug=True)