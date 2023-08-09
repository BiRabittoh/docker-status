import json
from datetime import datetime
import docker, requests

with open("config.json", "r") as in_file:
    services = json.loads("".join(in_file.readlines()))
services = sorted_dict = dict(sorted(services.items()))

docker_client = docker.from_env()
last_updated = None

def healthcheck(container, status):
    container_name = container["name"]
    try:
        container_status = status[container_name]
        if container_status != "running" or container["test"] is None:
            return status[container_name]
    except KeyError:
        return "missing"
    
    try:
        result = requests.get(container["test"]).status_code
        if result == 200:
            return "healthy"
        print(f"Status Code for {container_name} is {result}.")
    except Exception as e:
        print(e)
    return "unhealthy"

def update_status():
    global last_updated
    last_updated = datetime.now()
    containers = docker_client.containers.list(all=True)
    status = { container.name: container.status for container in containers }
    
    for k, v in services.items():
        service_status = []
        for container in v["containers"]:
            container_name = container["name"]
            container["status"] = healthcheck(container, status)
    return services

def increment_counter(counter_dict, key):
    try:
        counter_dict[key] += 1
    except KeyError:
        counter_dict[key] = 1

def get_stats():
    if last_updated is None:
        update_status()
    tracked = 0
    counts = {}
    for k, v in services.items():
        for container in v["containers"]:
            tracked += 1
            increment_counter(counts, container["status"])
    return {
        "counts": counts,
        "total": tracked,
        "last_updated": last_updated.strftime("%Y-%m-%dT%H:%M:%SZ%z"),
    }

if __name__ == "__main__":
    print(update_status())
