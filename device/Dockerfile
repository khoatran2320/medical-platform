#init a base image 
FROM python:3.8.9
WORKDIR /device-app
ADD . /device-app
RUN pip install -r requirements.txt

ENV FLASK_APP=app.py
# ENV FLASK_RUN_HOST=0.0.0.0
EXPOSE 5000
CMD ["flask", "run", "-h", "0.0.0.0", "-p", "5000"]
# "--host", "172.17.0.2"