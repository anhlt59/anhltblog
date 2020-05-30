FROM python:3.8-alpine
MAINTAINER AnhLT59

ENV PYTHONUNBUFFERED 1

RUN mkdir /app/
WORKDIR /app/

RUN apk add --no-cache --update \
    build-base \
    bash \
    && rm -rf /var/cache/apk/*

COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt
COPY ./app/ /app