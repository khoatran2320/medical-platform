import time
from celery import Celery
from celery.utils.log import get_task_logger
import speech_recognition as sr
import os


logger = get_task_logger(__name__)

app = Celery('speech_2_text_tasks',
             broker='amqp://admin:mypass@rabbit:5672',
             backend='mongodb://mongodb_container:27017/mydb')


@app.task()
def speech_2_text(afile):
    if os.path.exists(afile):
        recognizer = sr.Recognizer()
        audioFile = sr.AudioFile(afile)
        with audioFile as source:
            data = recognizer.record(source)
        transcript = recognizer.recognize_google(data, key=None)
        print(transcript)
        # os.remove(afile)
        return transcript
    return "nothing"