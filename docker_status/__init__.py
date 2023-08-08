from flask import Flask

app = Flask(__name__)

import docker_status.views
