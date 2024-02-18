FROM python:3.10-alpine

WORKDIR /app

RUN apk update; \
    apk add \
    bash \
    git \
    pip install DateTime

CMD bash