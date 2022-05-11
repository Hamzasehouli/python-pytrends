FROM python:3.8-slim-buster

WORKDIR /app

RUN pip install pytrends

COPY app.py .

CMD [ "py", "app.py"]