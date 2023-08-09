import json
from datetime import datetime
from flask import request, redirect, render_template
from docker_status import app
from docker_status.my_docker import update_status

last_updated = None

@app.route('/', methods=['GET', 'POST'])
def route_index():
    global last_updated
    last_updated = datetime.now()
    services = update_status()
    for name, service in services.items():
        containers = service["containers"]
        service["status"] = ", ".join([ x["status"] for x in containers ])
        service["names"] = ", ".join([ x["name"] for x in containers ])
    if request.method == 'GET':
        return render_template("index.html", services=services)
    return json.dumps(services)

@app.route('/stats')
def route_stats():
    return json.dumps({
        "last_updated": last_updated.strftime("%Y-%m-%dT%H:%M:%SZ%z") if last_updated is not None else None,
    })
    