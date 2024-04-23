FROM python:3.10-slim

WORKDIR /flask
COPY ./requirements.txt /flask/
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /flask/app

EXPOSE 5000

ENV FLASK_APP=app/my_flask.py

CMD ["flask", "run", "--host", "0.0.0.0"]