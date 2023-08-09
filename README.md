# docker-status

A simple status page for my Docker containers.
# Config
First of all, copy `config.json.example` into `config.json` and fill it out accordingly.

### Poetry
1. Install dependencies: `poetry install`.
2. Start the program:
    * Debug: `poetry run flask --app docker_status run --port 1111 --debug`.
    * Production: `poetry run waitress-serve --host 0.0.0.0 --port 1111 docker_status:app`

### Docker
Just use `docker-compose up -d`.
