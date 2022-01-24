###########
# BUILDER #
###########
FROM python:3.7-slim-bullseye as builder
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update && \
    apt -y install build-essential libmariadb-dev

COPY requirements.txt /app/requirements.txt
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt

#########
# FINAL #
#########
FROM python:3.7-slim-bullseye
WORKDIR /app

RUN apt update && \
    apt install -y libmariadb-dev
RUN apt clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*

COPY --from=builder /app/wheels /wheels
RUN pip install --no-cache /wheels/*
COPY . /app/

EXPOSE 80/tcp

ENTRYPOINT gunicorn -w 4 -b 0.0.0.0:8000 myapi.wsgi