from waitress import serve
from docker_status import app

serve(app, listen='*:1111')
