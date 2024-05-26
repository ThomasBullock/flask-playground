FROM python:3.10-slim

EXPOSE 5000

WORKDIR /flask

COPY requirements.txt /flask
COPY app/__init__.py /flask/app/__init__.py
COPY app/templates/ /flask/app/templates
COPY app/db.py /flask/app/db.py
COPY app/routes.py /flask/app/routes.py
COPY main.py /flask/main.py
COPY config.py /flask/config.py

RUN pip install -r requirements.txt

ENV FLASK_APP=main.py
ENV FLASK_DEBUG=1
CMD flask run --host=0.0.0.0