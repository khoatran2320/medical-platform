import time
from celery import Celery
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

app = Celery('speech_2_text_tasks',
             broker='amqp://admin:mypass@rabbit:5672',
             backend='mongodb://mongodb_container:27017/mydb')


@app.task()
def speech_2_text(audioFile):
    logger.info('Got Request - Starting work ')
    time.sleep(10)
    logger.info('Work Finished ')
    return "speech to text baby"