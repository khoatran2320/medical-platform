#init a base image 
FROM python:3.8.9
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt

ENV FLASK_APP=app.py
# ENV FLASK_RUN_HOST=0.0.0.0
EXPOSE 5000
ENV FLASK_RUN_HOST 0.0.0.0
ENV FLASK_RUN_PORT 5000
CMD flask run
# CMD ["python", "app.py"]
# # "--host", "172.17.0.2"