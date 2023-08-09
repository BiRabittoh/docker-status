FROM python:3-alpine

WORKDIR /app
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .

CMD ["waitress-serve", "--host", "0.0.0.0", "--port", "1111", "docker_status:app"]
