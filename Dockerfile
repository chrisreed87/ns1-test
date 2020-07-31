FROM python:3-alpine
RUN pip install --upgrade pip
COPY ./requirements.txt requirements.txt
COPY ./server.py server.py
RUN pip install -r requirements.txt

