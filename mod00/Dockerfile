FROM python:3.10-alpine

WORKDIR /app

RUN apk update; \
    apk add \
    bash \
    git; \
    pip install DateTime; \
    pip install flake8; \
    pip install tqdm; \
    pip install numpy; \
    pip install pypi-install;

CMD bash
