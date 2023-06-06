# Pull official base image
FROM python:3.11.0-alphine

# Set work Directory
WORKDIR /usr/src/app

# Set environment variables
# PYTHONDONTWRITEBYTECODE: Prevents Python from writing pyc files to disc (equivalent to "python -B" option)
ENV PYTHONDONTWRITEBYTECODE 1
# PYTHONUNBUFFERED: Prevents Python from buffering stdout and stderr (equivalent to "python -u" option)
ENV PYTHONUNBUFFERED 1

# Copy requirements file
COPY ./requirements.txt /usr/src/app/requirements.txt

# Install dependencies

RUN set -eux \
    && apk add --no-cache --virtual .build-deps build-base \
    openssl-dev libffi-dev gcc musl-dev python3-dev \
    && pip install --upgrade pip setuptools wheel \
    && pip install -r /usr/src/app/requirements.txt \
    && rm -rf /root/.cache/pip

# Copy project
COPY . /usr/src/app/