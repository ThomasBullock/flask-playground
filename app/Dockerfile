FROM python:3.10-slim

EXPOSE 5000

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY app.py /app
COPY templates/ /app/templates

ENV FLASK_APP=app.py

CMD flask run --host=0.0.0.0