FROM tecktron/python-waitress:slim

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./docker_status /app/docker_status
WORKDIR /app
ENV APP_MODULE=docker_status:app
