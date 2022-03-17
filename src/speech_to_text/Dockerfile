FROM python:3.8.9

# layer caching for faster builds
COPY requirements.txt /
RUN pip install -r /requirements.txt

#COPY app.py /app.py
ADD . /speech_to_text
WORKDIR /speech_to_text

ENTRYPOINT celery -A task worker --loglevel=info