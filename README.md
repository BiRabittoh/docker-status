# artbound-python

A client-server reimplementation of the administration panel for ArtBound.

## Instructions
1. Copy `config.json.example` into `config.json` and fill it out;
2. Install dependencies: `poetry install`.

## Usage (poetry)
* Debug: `poetry run flask --app docker_status run --port 1111 --debug`.
* Production: `poetry run waitress-serve --host 0.0.0.0 --port 1111 docker_status:app`

## Usage (docker)
1. Generate a `token.json` file: `poetry run python get_token.py`;
2. Build the image and start the container: `docker-compose up -d`.
