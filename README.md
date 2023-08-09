# docker-status
A simple status page for my Docker containers.

## Config
First of all, copy `config.json.example` into `config.json` and fill it out accordingly.

### Docker
Just use `docker-compose up --build --detach`.

### Poetry (debug)
1. Install dependencies: `poetry install`;
2. Start the server: `poetry run flask --app docker_status run --port 1111 --debug`.

### Poetry (production)
1. Install dependencies: `poetry install --with prod`;
2. Start the server: `poetry run python docker_status`.
