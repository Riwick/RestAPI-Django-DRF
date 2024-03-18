FROM python:3.12-alpine

RUN mkdir 'restapi'

COPY req-docker.txt /restapi

COPY restapi/. /restapi

WORKDIR /restapi

EXPOSE 8000

RUN pip install -r /restapi/req-docker.txt
