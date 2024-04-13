FROM python:3.10-slim

WORKDIR /app
COPY ./requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
ENV FLASK_APP=my_flask.py
CMD ["flask", "run", "--host", "0.0.0.0"]