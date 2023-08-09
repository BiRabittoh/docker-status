import bjoern
from docker_status import app

bjoern.run(app, "0.0.0.0", 1111)
