FROM python:3.10-slim

EXPOSE 5000

WORKDIR /app

COPY requirements.txt /app
COPY app/__init__.py /app/app/__init__.py
COPY app/templates/ /app/app/templates
COPY main.py /app/main.py

RUN pip install -r requirements.txt

ENV FLASK_APP=main.py
CMD flask run --host=0.0.0.0